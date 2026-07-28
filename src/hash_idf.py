"""
By Mr_First
hash_idf.py

Identify what kind of hash a string is, by inspecting its shape.
"""

import argparse
import re
from dataclasses import dataclass, replace

from rich.console import Console
from rich.table import Table

# Import RULES. Support both `python src/hash_idf.py` and package imports.
try:
    from . import rule_and_confidence
except ImportError:
    import rule_and_confidence


PREFIX_RULES = rule_and_confidence.PREFIX_RULES
RAW_HEX_RULES = rule_and_confidence.RAW_HEX_RULES
FULL_FORMAT_RULES = rule_and_confidence.FULL_FORMAT_RULES
Confidence = rule_and_confidence.Confidence


@dataclass(frozen=True, slots=True)
class HashCandidate:
    # Candidate contains Algorithm, Confidence, Reason and Description.
    algorithm: str
    confidence: Confidence  # Only have three options: High, Medium, Low
    reason: str
    describe: str
    prefix: str = ""

    def print_candidate(self):
        print(f"Algorithm: {self.algorithm}")
        print(f"Confidence: {self.confidence}")
        print(f"reason: {self.reason}")
        print(f"describe: {self.describe}")


def confirm(value: str, hash_list: list[HashCandidate]) -> list[HashCandidate]:
    """Upgrade a prefix candidate to High when its complete format is valid."""

    confirmed_list: list[HashCandidate] = []

    for candidate in hash_list:
        matched_pattern = ""

        for algorithm, pattern in FULL_FORMAT_RULES:
            if candidate.algorithm == algorithm and re.fullmatch(pattern, value):
                matched_pattern = pattern
                break

        if matched_pattern:
            confirmed_list.append(replace(
                candidate,
                confidence="High",
                reason=(
                    f"Prefix {candidate.prefix!r} and the complete "
                    f"{candidate.algorithm} format are valid"
                ),
            ))
        else:
            confirmed_list.append(candidate)

    return confirmed_list


def identify(value: str) -> list[HashCandidate]:
    """Return every hash algorithm whose prefix or raw shape matches value."""

    if not isinstance(value, str):
        raise TypeError("hash value must be a string")

    value = value.strip()
    if not value:
        return []

    candidate_list: list[HashCandidate] = []

    # Check PREFIX_RULES
    for prefix, algorithm, description in PREFIX_RULES:
        if value.startswith(prefix):
            candidate_list.append(HashCandidate(
                algorithm=algorithm,
                confidence="Low",
                reason=f"Starts with the known prefix {prefix!r}",
                describe=description,
                prefix=prefix,
            ))

    # Check full format for prefix candidates. A prefix alone remains Low.
    candidate_list = confirm(value, candidate_list)

    # Check Length and format for a raw hexadecimal hash. Raw hashes remain
    # Medium because many algorithms have the same output length and shape.
    if re.fullmatch(r"[0-9a-fA-F]+", value):
        for algorithm, description in RAW_HEX_RULES.get(len(value), ()):
            candidate_list.append(HashCandidate(
                algorithm=algorithm,
                confidence="Medium",
                reason=(
                    f"Contains only hexadecimal characters and has "
                    f"{len(value)} characters"
                ),
                describe=description,
            ))

    # Show the strongest matches first while preserving rule order.
    confidence_order = {"High": 0, "Medium": 1, "Low": 2}
    candidate_list.sort(key=lambda candidate: confidence_order[candidate.confidence])

    return candidate_list


def print_results(results: list[HashCandidate]):
    console = Console()

    if not results:
        console.print("[yellow]No matching hash format found.[/yellow]")
        return

    table = Table(title="Hash Identifier")
    table.add_column("Algorithm")
    table.add_column("Confidence")
    table.add_column("Reason")
    table.add_column("Description")

    confidence_color = {
        "High": "green",
        "Medium": "yellow",
        "Low": "red",
    }

    for candidate in results:
        color = confidence_color[candidate.confidence]
        table.add_row(
            candidate.algorithm,
            f"[{color}]{candidate.confidence}[/{color}]",
            candidate.reason,
            candidate.describe,
        )

    console.print(table)


def main():
    parser = argparse.ArgumentParser(
        description="Identify possible algorithms from a hash string."
    )
    parser.add_argument("hash", help="Hash string to identify")
    args = parser.parse_args()

    print_results(identify(args.hash))


if __name__ == "__main__":
    main()
