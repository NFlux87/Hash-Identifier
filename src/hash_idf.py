"""
By Mr_First
hash_idf.py

Identify what kind of hash a string is, by inspecting its shape
...
"""

import hashlib
import sys
import argparse
from dataclasses import dataclass
from typing import Literal

from rich.console import Console
from rich.table import Table

# Import Prefix-Rule and Confidence
import rule_and_confidence

PREFIX_RULES = rule_and_confidence.PREFIX_RULES
Confidence = rule_and_confidence.Confidence


@dataclass(frozen=True, slots=True)
class HashCanndidate:
    # Crate Class for Algorithm, Confidence, Reason
    algorithm : str
    confidence : Confidence # Only have three options "High", "Medium", "Low"
    reason : str
    describe: str

    def print_canndidat(self):
        print(f"Algorithm: {self.algorithm}")
        print(f"Confidence: {self.confidence}")
        print(f"reason: {self.reason}")
        print(f"describe: {self.describe}")



def indentify(hash) -> HashCanndidate:

    # Check PREFIX_RULES
    for rule in PREFIX_RULES:
        if hash.startswith(rule[0]):
            # append Rule to Possible
            
            return HashCanndidate(
                algorithm=f"{rule[1]}",
                confidence= "High",
                reason=f"Reason Start with: {rule[0]}",
                describe=f"{rule[2]}"
            )
    
        
    # Check for none prefix hash



def main():

    hash = "scrypt$KYVbZ5JFVfqu0oV98LnF5eTk4QTe2e4PQG7QNYfhumEpGdi/867AO"
    result = indentify(hash)
    result.print_canndidat()

           
        
if __name__ == "__main__":
    main()