from __future__ import annotations

import math
from dataclasses import dataclass

import typing_extensions

from chinilla.types.clvm_cost import CLVMCost
from chinilla.types.vojos import Vojos
from chinilla.util.ints import uint64
from chinilla.util.streamable import Streamable, streamable


@typing_extensions.final
@streamable
@dataclass(frozen=True)
class FeeRate(Streamable):
    """
    Represents Fee Rate in vojos divided by CLVM Cost.
    Performs HCX/vojo conversion.
    Similar to 'Fee per cost'.
    """

    vojos_per_clvm_cost: uint64

    @classmethod
    def create(cls, vojos: Vojos, clvm_cost: CLVMCost) -> FeeRate:
        return cls(uint64(math.ceil(vojos / clvm_cost)))
