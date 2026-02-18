from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for item in cpdomains:
            c, domain = item.split()
            c = int(c)

            parts = domain.split(".")

            for i in range(len(parts)):
                sub = ".".join(parts[i:])
                counts[sub] += c

        return [f"{v} {k}" for k, v in counts.items()]
