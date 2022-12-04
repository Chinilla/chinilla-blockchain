from __future__ import annotations

from chinilla.types.blockchain_format.program import Program
from chinilla.types.blockchain_format.sized_bytes import bytes32
from chinilla.util.ints import uint64
from chinilla.wallet.puzzles.load_clvm import load_clvm_maybe_recompile

NOTIFICATION_MOD = load_clvm_maybe_recompile("notification.clvm")


def construct_notification(target: bytes32, amount: uint64) -> Program:
    return NOTIFICATION_MOD.curry(target, amount)
