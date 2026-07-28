# Hash Identifier

```text
██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██╗██████╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ██║██╔══██╗
███████║███████║███████╗███████║    ██║██║  ██║
██╔══██║██╔══██║╚════██║██╔══██║    ██║██║  ██║
██║  ██║██║  ██║███████║██║  ██║    ██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚═╝╚═════╝
```

Hash Identifier is a Python CLI and library that finds possible hash algorithms by inspecting a value's prefix, character set, length, and complete encoded format.

It returns every plausible candidate instead of pretending that a raw digest can always be identified with certainty.

## Features

- Recognizes common password-hash, framework, database, archive, operating-system, and application prefixes.
- Detects raw hexadecimal digests from 8 to 128 characters.
- Returns multiple candidates when algorithms share the same shape.
- Validates complete formats for selected algorithms such as bcrypt, Argon2, Unix crypt, MySQL, Django, and tagged raw digests.
- Assigns `High`, `Medium`, or `Low` confidence with an explanation.
- Provides colored terminal output using Rich.
- Includes unit tests for input validation, raw hashes, prefixes, full-format validation, and ambiguous results.

## Confidence Model

| Confidence | Meaning |
| --- | --- |
| `High` | The prefix and complete encoded format match a validator for that algorithm. |
| `Medium` | The value is valid hexadecimal and its length matches one or more raw digest algorithms. |
| `Low` | A known prefix matches, but the complete format has not been validated. |

`High` means high confidence in the **format**, not cryptographic proof that the value was produced by that algorithm.

For example, a 32-character hexadecimal value may be MD4, MD5, NTLM, or another 128-bit digest. Without additional context, the program must return multiple candidates.

## Requirements

- Python 3.11 or newer
- `uv` for dependency and environment management

## Installation

Clone the repository and synchronize its dependencies:

```bash
git clone <repository-url>
cd Hash-Identifier
uv sync
```

## CLI Usage

Pass the hash as the first positional argument:

```bash
uv run python src/hash_idf.py '<hash-value>'
```

Always quote values containing `$` so that the shell does not interpret them as environment variables.

### Raw hexadecimal digest

```bash
uv run python src/hash_idf.py 'd41d8cd98f00b204e9800998ecf8427e'
```

Possible results include:

```text
MD4   Medium
MD5   Medium
NTLM  Medium
```

### Valid bcrypt format

```bash
uv run python src/hash_idf.py '$2b$12$.....................................................'
```

The bcrypt candidate receives `High` confidence because its revision, cost, length, and character set match the complete bcrypt format.

### Prefix with an invalid complete format

```bash
uv run python src/hash_idf.py '$2b$not-a-complete-bcrypt-hash'
```

This still produces a bcrypt candidate, but its confidence remains `Low` because only the prefix matches.

### Unknown input

```bash
uv run python src/hash_idf.py 'this-is-not-a-hash'
```

```text
No matching hash format found.
```

## Python API

Import and call `identify()` to receive a list of candidates:

```python
from src.hash_idf import identify

results = identify("d41d8cd98f00b204e9800998ecf8427e")

for candidate in results:
    print(candidate.algorithm)
    print(candidate.confidence)
    print(candidate.reason)
```

Each candidate contains:

| Field | Description |
| --- | --- |
| `algorithm` | Possible algorithm or encoded-hash format. |
| `confidence` | `High`, `Medium`, or `Low`. |
| `reason` | Evidence used to assign the confidence. |
| `describe` | Short description of the algorithm or format. |
| `prefix` | Matching prefix, or an empty string for raw hexadecimal candidates. |

`identify()` always returns a list. Unknown and empty values return an empty list, while non-string values raise `TypeError`.

## Raw Hexadecimal Lengths

| Length | Possible algorithms |
| ---: | --- |
| 8 | CRC-32 |
| 16 | MySQL 3.23 |
| 32 | MD4, MD5, NTLM |
| 40 | SHA-1, RIPEMD-160 |
| 56 | SHA-224, SHA3-224 |
| 64 | SHA-256, SHA3-256, BLAKE2s-256 |
| 96 | SHA-384, SHA3-384 |
| 128 | SHA-512, SHA3-512, BLAKE2b-512, Whirlpool |

The input must consist entirely of hexadecimal characters (`0-9`, `a-f`, or `A-F`) before its length is considered.

## Running Tests

Run the complete test suite with:

```bash
uv run python -m unittest discover -s tests -v
```

The tests cover:

- Empty, whitespace, unknown, and non-string inputs
- Uppercase and lowercase hexadecimal values
- Every supported raw digest length
- Invalid characters and unsupported lengths
- Valid and malformed bcrypt values
- MySQL and tagged digest validation
- Duplicate prefix candidates
- Confidence ordering
- Immutable candidate confirmation

## Project Structure

```text
Hash-Identifier/
├── src/
│   ├── hash_idf.py
│   └── rule_and_confidence.py
├── tests/
│   └── test_hash_idf.py
├── pyproject.toml
├── uv.lock
└── README.md
```

- `src/hash_idf.py` contains identification, confirmation, output, and CLI logic.
- `src/rule_and_confidence.py` contains prefix rules, raw-length rules, and full-format validators.
- `tests/test_hash_idf.py` defines the behavior expected from the public functions.

## Adding a New Rule

1. Add its prefix, algorithm name, and description to `PREFIX_RULES`.
2. If it is a raw hexadecimal digest, add the algorithm under the correct length in `RAW_HEX_RULES`.
3. Add a complete regular-expression validator to `FULL_FORMAT_RULES` only when the complete format is known.
4. Add valid and malformed examples to the test suite.
5. Run all tests before committing the change.

Do not assign `High` confidence from a prefix or length alone.

## Limitations

- Hash identification is heuristic and can produce false positives.
- Raw digests are inherently ambiguous when algorithms share the same output length.
- Not every prefix rule currently has a complete validator.
- A value matching a format may still be random data rather than a real hash.
- The tool identifies possible formats; it does not crack hashes, recover passwords, or verify plaintext.

## Legal and Ethical Use

Use this project only with data and systems you own or are explicitly authorized to test. The project is intended for education, defensive analysis, and authorized security work.
