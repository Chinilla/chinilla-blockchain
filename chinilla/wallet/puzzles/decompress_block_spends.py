from chinilla.wallet.puzzles.load_clvm import load_serialized_clvm

DECOMPRESS_BLOCK_SPENDS = load_serialized_clvm("decompress_block_spends.clvm", package_or_requirement=__name__)
