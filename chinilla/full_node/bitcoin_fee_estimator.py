from __future__ import annotations

from datetime import datetime

from chinilla.full_node.fee_estimate_store import FeeStore
from chinilla.full_node.fee_estimation import FeeBlockInfo, FeeMempoolInfo
from chinilla.full_node.fee_estimator import SmartFeeEstimator
from chinilla.full_node.fee_estimator_interface import FeeEstimatorInterface
from chinilla.full_node.fee_tracker import FeeTracker
from chinilla.types.clvm_cost import CLVMCost
from chinilla.types.fee_rate import FeeRate
from chinilla.types.mempool_item import MempoolItem
from chinilla.types.vojos import Vojos
from chinilla.util.ints import uint32, uint64


class BitcoinFeeEstimator(FeeEstimatorInterface):
    """
    A Fee Estimator based on the concepts and code at:
    https://github.com/bitcoin/bitcoin/tree/5b6f0f31fa6ce85db3fb7f9823b1bbb06161ae32/src/policy
    """

    def __init__(self, fee_tracker: FeeTracker, smart_fee_estimator: SmartFeeEstimator) -> None:
        self.fee_rate_estimator: SmartFeeEstimator = smart_fee_estimator
        self.tracker: FeeTracker = fee_tracker
        self.last_mempool_info = FeeMempoolInfo(
            CLVMCost(uint64(0)),
            FeeRate.create(Vojos(uint64(0)), CLVMCost(uint64(1))),
            CLVMCost(uint64(0)),
            datetime.min,
            CLVMCost(uint64(0)),
        )

    def new_block(self, block_info: FeeBlockInfo) -> None:
        self.tracker.process_block(block_info.block_height, block_info.included_items)

    def add_mempool_item(self, mempool_info: FeeMempoolInfo, mempool_item: MempoolItem) -> None:
        self.last_mempool_info = mempool_info

    def remove_mempool_item(self, mempool_info: FeeMempoolInfo, mempool_item: MempoolItem) -> None:
        self.last_mempool_info = mempool_info
        self.tracker.remove_tx(mempool_item)

    def estimate_fee_rate(self, *, time_offset_seconds: int) -> FeeRate:
        """
        time_offset_seconds: Target time in the future we want our tx included by
        """
        fee_estimate = self.fee_rate_estimator.get_estimate(time_offset_seconds)
        if fee_estimate.error is not None:
            return FeeRate(uint64(0))
        return fee_estimate.estimated_fee_rate

    def estimate_fee_rate_for_block(self, block: uint32) -> FeeRate:
        fee_estimate = self.fee_rate_estimator.get_estimate_for_block(block)
        if fee_estimate.error is not None:
            return FeeRate(uint64(0))
        return fee_estimate.estimated_fee_rate

    def mempool_size(self) -> CLVMCost:
        """Report last seen mempool size"""
        return self.last_mempool_info.current_mempool_cost

    def mempool_max_size(self) -> CLVMCost:
        """Report current mempool max size (cost)"""
        return self.last_mempool_info.max_size_in_cost

    def get_tracker(self) -> FeeTracker:
        """
        `get_tracker` is for testing the BitcoinFeeEstimator.
        Not part of `FeeEstimatorInterface`
        """
        return self.tracker


def create_bitcoin_fee_estimator(max_block_cost_clvm: uint64) -> BitcoinFeeEstimator:
    # fee_store and fee_tracker are particular to the BitcoinFeeEstimator, and
    # are not necessary if a different fee estimator is used.
    fee_store = FeeStore()
    fee_tracker = FeeTracker(fee_store)
    smart_fee_estimator = SmartFeeEstimator(fee_tracker, max_block_cost_clvm)
    return BitcoinFeeEstimator(fee_tracker, smart_fee_estimator)
