from __future__ import annotations

from typing import Any, Awaitable, Callable, List, Optional

import pytest
from blspy import G2Element

from chinilla.consensus.block_record import BlockRecord
from chinilla.consensus.default_constants import DEFAULT_CONSTANTS
from chinilla.full_node.mempool_manager import MempoolManager
from chinilla.types.blockchain_format.classgroup import ClassgroupElement
from chinilla.types.blockchain_format.coin import Coin
from chinilla.types.blockchain_format.program import Program
from chinilla.types.blockchain_format.sized_bytes import bytes32, bytes100
from chinilla.types.coin_record import CoinRecord
from chinilla.types.coin_spend import CoinSpend
from chinilla.types.condition_opcodes import ConditionOpcode
from chinilla.types.spend_bundle import SpendBundle
from chinilla.util.errors import ValidationError
from chinilla.util.ints import uint8, uint32, uint64, uint128

IDENTITY_PUZZLE = Program.to(1)
IDENTITY_PUZZLE_HASH = IDENTITY_PUZZLE.get_tree_hash()

TEST_TIMESTAMP = uint64(1616108400)
TEST_COIN = Coin(IDENTITY_PUZZLE_HASH, IDENTITY_PUZZLE_HASH, uint64(1000000000))
TEST_HEIGHT = uint32(1)


async def zero_calls_get_coin_record(_: bytes32) -> Optional[CoinRecord]:
    assert False


async def instantiate_mempool_manager(
    get_coin_record: Callable[[bytes32], Awaitable[Optional[CoinRecord]]]
) -> MempoolManager:
    mempool_manager = MempoolManager(get_coin_record, DEFAULT_CONSTANTS)
    test_block_record = BlockRecord(
        IDENTITY_PUZZLE_HASH,
        IDENTITY_PUZZLE_HASH,
        TEST_HEIGHT,
        uint128(0),
        uint128(0),
        uint8(0),
        ClassgroupElement(bytes100(b"0" * 100)),
        None,
        IDENTITY_PUZZLE_HASH,
        IDENTITY_PUZZLE_HASH,
        uint64(0),
        IDENTITY_PUZZLE_HASH,
        IDENTITY_PUZZLE_HASH,
        uint64(0),
        uint8(0),
        False,
        uint32(TEST_HEIGHT - 1),
        TEST_TIMESTAMP,
        None,
        uint64(0),
        None,
        None,
        None,
        None,
        None,
    )
    await mempool_manager.new_peak(test_block_record, None)
    return mempool_manager


def spend_bundle_from_conditions(conditions: List[List[Any]]) -> SpendBundle:
    solution = Program.to(conditions)
    coin_spend = CoinSpend(TEST_COIN, IDENTITY_PUZZLE, solution)
    return SpendBundle([coin_spend], G2Element())


@pytest.mark.asyncio
async def test_negative_addition_amount() -> None:
    mempool_manager = await instantiate_mempool_manager(zero_calls_get_coin_record)
    conditions = [[ConditionOpcode.CREATE_COIN, IDENTITY_PUZZLE_HASH, -1]]
    sb = spend_bundle_from_conditions(conditions)
    # chia_rs currently emits this instead of Err.COIN_AMOUNT_NEGATIVE
    # Addressed in https://github.com/Chinilla/chia_rs/pull/99
    with pytest.raises(ValidationError, match="Err.INVALID_CONDITION"):
        await mempool_manager.pre_validate_spendbundle(sb, None, sb.name())


@pytest.mark.asyncio
async def test_valid_addition_amount() -> None:
    mempool_manager = await instantiate_mempool_manager(zero_calls_get_coin_record)
    max_amount = mempool_manager.constants.MAX_COIN_AMOUNT
    conditions = [[ConditionOpcode.CREATE_COIN, IDENTITY_PUZZLE_HASH, max_amount]]
    sb = spend_bundle_from_conditions(conditions)
    npc_result = await mempool_manager.pre_validate_spendbundle(sb, None, sb.name())
    assert npc_result.error is None


@pytest.mark.asyncio
async def test_too_big_addition_amount() -> None:
    mempool_manager = await instantiate_mempool_manager(zero_calls_get_coin_record)
    max_amount = mempool_manager.constants.MAX_COIN_AMOUNT
    conditions = [[ConditionOpcode.CREATE_COIN, IDENTITY_PUZZLE_HASH, max_amount + 1]]
    sb = spend_bundle_from_conditions(conditions)
    # chia_rs currently emits this instead of Err.COIN_AMOUNT_EXCEEDS_MAXIMUM
    # Addressed in https://github.com/Chinilla/chia_rs/pull/99
    with pytest.raises(ValidationError, match="Err.INVALID_CONDITION"):
        await mempool_manager.pre_validate_spendbundle(sb, None, sb.name())


@pytest.mark.asyncio
async def test_duplicate_output() -> None:
    mempool_manager = await instantiate_mempool_manager(zero_calls_get_coin_record)
    conditions = [
        [ConditionOpcode.CREATE_COIN, IDENTITY_PUZZLE_HASH, 1],
        [ConditionOpcode.CREATE_COIN, IDENTITY_PUZZLE_HASH, 1],
    ]
    sb = spend_bundle_from_conditions(conditions)
    with pytest.raises(ValidationError, match="Err.DUPLICATE_OUTPUT"):
        await mempool_manager.pre_validate_spendbundle(sb, None, sb.name())


@pytest.mark.asyncio
async def test_block_cost_exceeds_max() -> None:
    mempool_manager = await instantiate_mempool_manager(zero_calls_get_coin_record)
    conditions = []
    for i in range(2400):
        conditions.append([ConditionOpcode.CREATE_COIN, IDENTITY_PUZZLE_HASH, i])
    sb = spend_bundle_from_conditions(conditions)
    with pytest.raises(ValidationError, match="Err.BLOCK_COST_EXCEEDS_MAX"):
        await mempool_manager.pre_validate_spendbundle(sb, None, sb.name())
