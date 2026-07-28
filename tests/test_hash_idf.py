import unittest

from src.hash_idf import HashCandidate, confirm, identify


class IdentifyInputTest(unittest.TestCase):
    def test_empty_and_whitespace_return_empty_list(self):
        self.assertEqual(identify(""), [])
        self.assertEqual(identify("   \n\t"), [])

    def test_non_string_raises_type_error(self):
        for value in (None, 123, b"abc"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "must be a string"):
                    identify(value)

    def test_unknown_value_returns_empty_list(self):
        self.assertEqual(identify("this-is-not-a-hash"), [])

    def test_outer_whitespace_is_ignored(self):
        results = identify("  d41d8cd98f00b204e9800998ecf8427e  ")
        self.assertEqual(
            {candidate.algorithm for candidate in results},
            {"MD4", "MD5", "NTLM"},
        )


class RawHexTest(unittest.TestCase):
    def test_supported_lengths_return_expected_algorithms(self):
        expected = {
            8: {"CRC-32"},
            16: {"MySQL 3.23"},
            32: {"MD4", "MD5", "NTLM"},
            40: {"SHA-1", "RIPEMD-160"},
            56: {"SHA-224", "SHA3-224"},
            64: {"SHA-256", "SHA3-256", "BLAKE2s-256"},
            96: {"SHA-384", "SHA3-384"},
            128: {"SHA-512", "SHA3-512", "BLAKE2b-512", "Whirlpool"},
        }

        for length, algorithms in expected.items():
            with self.subTest(length=length):
                results = identify("a" * length)
                self.assertEqual(
                    {candidate.algorithm for candidate in results}, algorithms
                )
                self.assertTrue(
                    all(candidate.confidence == "Medium" for candidate in results)
                )
                self.assertTrue(all(candidate.prefix == "" for candidate in results))

    def test_hex_check_is_case_insensitive(self):
        lower_results = identify("abcdef0123456789" * 2)
        upper_results = identify("ABCDEF0123456789" * 2)
        self.assertEqual(
            [candidate.algorithm for candidate in lower_results],
            [candidate.algorithm for candidate in upper_results],
        )

    def test_same_length_non_hex_value_does_not_match(self):
        self.assertEqual(identify("z" * 32), [])

    def test_unsupported_hex_length_does_not_match(self):
        self.assertEqual(identify("a" * 24), [])


class PrefixAndConfidenceTest(unittest.TestCase):
    def test_prefix_only_candidate_has_low_confidence(self):
        results = identify("$2b$not-a-complete-bcrypt-hash")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].algorithm, "bcrypt")
        self.assertEqual(results[0].confidence, "Low")
        self.assertEqual(results[0].prefix, "$2b$")

    def test_valid_bcrypt_format_has_high_confidence(self):
        results = identify("$2b$12$" + "." * 53)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].algorithm, "bcrypt")
        self.assertEqual(results[0].confidence, "High")

    def test_bcrypt_cost_outside_valid_range_stays_low(self):
        results = identify("$2b$99$" + "." * 53)
        self.assertEqual(results[0].confidence, "Low")

    def test_mysql_full_format_has_high_confidence(self):
        results = identify("*" + "A" * 40)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].algorithm, "MySQL 4.1+ SHA-1")
        self.assertEqual(results[0].confidence, "High")

    def test_tagged_sha256_full_format_has_high_confidence(self):
        results = identify("$sha256$" + "a" * 64)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].algorithm, "SHA-256")
        self.assertEqual(results[0].confidence, "High")

    def test_duplicate_prefix_candidates_are_preserved(self):
        results = identify("$md5$" + "a" * 32)
        result_by_algorithm = {
            candidate.algorithm: candidate.confidence for candidate in results
        }

        self.assertEqual(result_by_algorithm["MD5"], "High")
        self.assertEqual(result_by_algorithm["Sun MD5-crypt"], "Low")

    def test_high_confidence_results_are_sorted_first(self):
        results = identify("$md5$" + "a" * 32)
        self.assertEqual(results[0].confidence, "High")


class ConfirmTest(unittest.TestCase):
    def test_confirm_does_not_mutate_original_candidate(self):
        candidate = HashCandidate(
            algorithm="bcrypt",
            confidence="Low",
            reason="prefix match",
            describe="bcrypt hash",
            prefix="$2b$",
        )

        confirmed = confirm("$2b$12$" + "." * 53, [candidate])

        self.assertEqual(candidate.confidence, "Low")
        self.assertEqual(confirmed[0].confidence, "High")
        self.assertIsNot(candidate, confirmed[0])


if __name__ == "__main__":
    unittest.main()
