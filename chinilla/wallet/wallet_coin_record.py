from __future__ import annotations

from dataclasses import dataclass

from chinilla.types.blockchain_format.coin import Coin
from chinilla.types.blockchain_format.sized_bytes import bytes32
from chinilla.types.coin_record import CoinRecord
from chinilla.util.ints import uint32, uint64
from chinilla.wallet.util.wallet_types import WalletType


@dataclass(frozen=True)
class WalletCoinRecord:
    """
    These are values that correspond to a CoinName that are used
    in keeping track of the unspent database.
    """

    coin: Coin
    confirmed_block_height: uint32
    spent_block_height: uint32
    spent: bool
    coinbase: bool
    wallet_type: WalletType
    wallet_id: int

    def name(self) -> bytes32:
        return self.coin.name()  # type: ignore

    def to_coin_record(self, timestamp: uint64) -> CoinRecord:
        return CoinRecord(self.coin, self.confirmed_block_height, self.spent_block_height, self.coinbase, timestamp)
