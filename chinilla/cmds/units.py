from __future__ import annotations

from typing import Dict

# The rest of the codebase uses vojos everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "chinilla": 10**12,  # 1 chinilla (HCX) is 1,000,000,000,000 vojo (1 trillion)
    "vojo": 1,
    "cat": 10**3,  # 1 CAT is 1000 CAT vojos
}
