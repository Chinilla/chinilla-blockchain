import json
from pathlib import Path
from typing import List

from chinilla.consensus.default_constants import DEFAULT_CONSTANTS
from chinilla.types.condition_opcodes import ConditionOpcode
from chinilla.types.condition_with_args import ConditionWithArgs
from tools.run_block import run_json_block

testnet10 = {
    "AGG_SIG_ME_ADDITIONAL_DATA": bytes.fromhex("ae7d0fd40f1be9e29e8408cb23c18c73751889e8f2eca3b55bf4a9b8dbe90643"),
    "DIFFICULTY_CONSTANT_FACTOR": 10052721566054,
    "DIFFICULTY_STARTING": 30,
    "EPOCH_BLOCKS": 768,
    "GENESIS_CHALLENGE": bytes.fromhex("ae7d0fd40f1be9e29e8408cb23c18c73751889e8f2eca3b55bf4a9b8dbe90643"),
    "GENESIS_PRE_FARM_FARMER_PUZZLE_HASH": bytes.fromhex(
        "09c505b9aae9fe97ba20d8622b63574fa2bfc19dcb9cbf2d45f3b53bcac60072"
    ),
    "GENESIS_PRE_FARM_POOL_PUZZLE_HASH": bytes.fromhex(
        "63a6b7cf123828c913c50580ee2a8beda829a464ee1a7cfcfe312d5b89496b12"
    ),
    "MEMPOOL_BLOCK_BUFFER": 10,
    "MIN_PLOT_SIZE": 18,
    "NETWORK_TYPE": 1,
}

constants = DEFAULT_CONSTANTS.replace(**testnet10)
retire_bytes = (
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)


def find_retirement(tocheck: List[ConditionWithArgs]) -> bool:
    for c in tocheck:
        if c.opcode != ConditionOpcode.CREATE_COIN:
            continue
        if len(c.vars) < 3:
            continue
        if c.vars[2] == retire_bytes:
            return True

    return False


def test_block_no_generator():
    dirname = Path(__file__).parent
    with open(dirname / "300000.json") as f:
        full_block = json.load(f)

    cat_list = run_json_block(full_block, dirname, constants)

    assert not cat_list


def test_block_retired_cat_with_memo():
    dirname = Path(__file__).parent
    with open(dirname / "396963.json") as f:
        full_block = json.load(f)

    cat_list = run_json_block(full_block, dirname, constants)

    assert cat_list
    assert cat_list[0].asset_id == "86bf9abe0600edf96b2e0fa928d19435b5aa756a9c9151c4b53c2c3da258502f"
    assert cat_list[0].memo == "Hello, please find me, I'm a memo!"
    assert cat_list[0].npc.coin_name.hex() == "244854a6fadf837b0fbb78d19b94b0de24fd2ffb440e7c0ec7866104b2aecd16"
    assert cat_list[0].npc.puzzle_hash.hex() == "4aa945b657928602e59d37ad165ba12008d1dbee3a7be06c9bd19b4f00da456c"
    found = False
    for cond in cat_list[0].npc.conditions:
        if cond[0] != ConditionOpcode.CREATE_COIN:
            continue
        found |= find_retirement(cond[1])
    assert found


def test_block_retired_cat_no_memo():
    dirname = Path(__file__).parent
    with open(dirname / "392111.json") as f:
        full_block = json.load(f)

    cat_list = run_json_block(full_block, dirname, constants)

    assert cat_list
    assert cat_list[0].asset_id == "86bf9abe0600edf96b2e0fa928d19435b5aa756a9c9151c4b53c2c3da258502f"
    assert not cat_list[0].memo
    assert cat_list[0].npc.coin_name.hex() == "f419f6b77fa56b2cf0e93818d9214ec6023fb6335107dd6e6d82dfa5f4cbb4f6"
    assert cat_list[0].npc.puzzle_hash.hex() == "714655375fc8e4e3545ecdc671ea53e497160682c82fe2c6dc44c4150dc845b4"

    found = False
    for cond in cat_list[0].npc.conditions:
        if cond[0] != ConditionOpcode.CREATE_COIN:
            continue
        found |= find_retirement(cond[1])
    assert found


def test_block_cat():
    dirname = Path(__file__).parent
    with open(dirname / "149988.json") as f:
        full_block = json.load(f)

    cat_list = run_json_block(full_block, dirname, constants)

    assert cat_list
    assert cat_list[0].asset_id == "8829a36776a15477a7f41f8fb6397752922374b60be7d3b2d7881c54b86b32a1"
    assert not cat_list[0].memo
    assert cat_list[0].npc.coin_name.hex() == "4314b142cecfd6121474116e5a690d6d9b2e8c374e1ebef15235b0f3de4e2508"
    assert cat_list[0].npc.puzzle_hash.hex() == "ddc37f3cbb49e3566b8638c5aaa93d5e10ee91dfd5d8ce37ad7175432d7209aa"


def test_generator_ref():
    """Run a block containing a back reference without error"""
    dirname = Path(__file__).parent
    with open(dirname / "466212.json") as f:
        full_block = json.load(f)

    cat_list = run_json_block(full_block, dirname, constants)

    assert cat_list == []
