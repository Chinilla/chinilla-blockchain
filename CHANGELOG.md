# Changelog

All notable changes to this project will be documented in this file.

## 1.0.3 Chinilla Blockchain 2022-04-25

### Notes

- This is a minor update to support the release of our first Chinilla Asset Tokens.

### Added

- Added The first two Chinilla Asset Tokens to the GUI:

  *  `Founder Token`: The first 100 farmers who won a block will receive ONE (1) by April 27, 2022
  *  `Early Farmer Token`: Every farmer who received a block reward in the first 100,000 blocks will receive FIVE (5) by April 27, 2022

### Fixed

- redirected `taildatabase.com` links to `Chinilla.com`


## 1.0.2 Chinilla Blockchain 2022-04-20

### Notes

- This release aligns with Chia 1.3.4

### Added

- Creating an offer now allows you to edit the exchange between two tokens that will auto calculate either the sending token amount or the receiving token amount
- When making an offer, makers can now create an offer including a fee to help get the transaction into the mempool when an offer is accepted
- Implemented `chinilla rpc` command
- New RPC `get_coin_records_by_hint` - Get coins for a given hint (Thanks @freddiecoleman)
- Add maker fee to remaining offer RPCs
- Add healthcheck endpoint to rpc services
- Optional wallet type parameter for `get_wallets` and `wallet show`
- Add `select_coins` RPC method by (Thanks @ftruzzi)
- Added `-n`/`--new-address` option to `chinilla wallet get_address`
- New DBWrapper supporting concurrent readers
- Added `config.yaml` option to run the `full_node` in single-threaded mode
- Build cli only version of debs
- Add `/get_stray_cats` API for accessing unknown CATs

### Changed

- Left navigation bar in the GUI has been reorganized and icons have been updated
- Settings has been moved to the new left hand nav bar
- Token selection has been changed to a permanent column in the GUI instead of the drop down list along
- Manage token option has been added at the bottom of the Token column to all users to show/hide token wallets
- Users can show/hide token wallets. If you have auto-discover cats in config.yaml turned off, new tokens will still show up there, but those wallets won’t get created until the token has been toggled on for the first time
- CATs now have a link to Chinilla.com tail database to look up the Asset ID
- Ongoing improvements to the internal test framework for speed and reliability.
- Significant harvester protocol update: You will need to update your farmer and all your harvesters as this is a breaking change in the harvester protocol. The new protocol solves many scaling issues. In particular, the protocol supports sending delta changes to the farmer - so for example, adding plots to a farm results in only the new plots being reported. We recommend you update your farmer first.
- Updated clvm_tools to 0.4.4
- Updated clvm_tools_rs to 0.1.7
- Changed code to use by default the Rust implementation of clvm_tools (clvm_tools_rs)
- Consolidated socket library to aiohttp and removed websockets dependency
- During node startup, missing blocks in the DB will throw an exception
- Updated cryptography to 36.0.2
- The rust implementation of CLVM is now called `chia_rs` instead of `clvm_rs`.
- Updated code to use improved rust interface `run_generator2`
- Code improvements to prefer connecting to a local trusted node over untrusted nodes

### Fixed

- Fixed issues with claiming self-pool rewards with and without a fee
- Fixed wallet creation in edge cases around chain reorgs
- Harvester: Reuse legacy refresh interval if new params aren't available
- Fixed typos `lastest` > `latest` (Thanks @daverof)
- Fixed typo in command line argument parsing for `chinilla db validate`
- Improved backwards compatibility for node RPC calls `get_blockchain_state` and `get_additions_and_removals`
- Fixed issue where `--root_path` option was not honored by `chinilla configure` CLI command
- Fixed cases where node DB was not created initially using v2 format
- Improved error messages from `chinilla db upgrade`
- Capitalized display of `Rpc` -> `RPC` in `chinilla show -s` by (Thanks @hugepants)
- Improved handling of chain reorgs with atomic rollback for the wallet
- Handled cases where one node doesn't have the coin we are looking for
- Fixed timelord installation for Debian
- Checked for requesting items when creating an offer
- Minor output formatting/enhancements for `chinilla wallet show`
- Fixed typo and index issues in wallet database
- Used the rust clvm version instead of python in more places
- Fixed trailing bytes shown in CAT asset ID row when using `chinilla wallet show`
- Maintain all chain state during reorg until the new fork has been fully validated
- Improved performance of `get_coin_records_by_names` by using proper index (Thanks @roseiliend)
- Improved handling of unknown pending balances
- Improved plot load times

### Known Issues

- You cannot install and run chinilla blockchain using the macOS packaged DMG on macOS Mojave (10.14).
- Pending transactions are not retried correctly and so can be stuck in the pending state unless manually removed and re-submitted


## 1.0.1 Chinilla Blockchain 2022-04-08

### Notes

- This release contains some minor fixes and adjustments that were noted during the launch.
- If you generated a seed on the inital release that contained the mispelled word `ehcxange` you will need to keep a note of that in the future as the spelling has been corrected to `exchange`.

### Added

- added discord and Github Discussions links in menu in GUI.

### Changed

- fixed spelling error in `english.txt` file
- updated chinilla explorer links


## 1.0.0 Chinilla Blockchain 2022-04-06

### Notes

- Due to a side-chain attack on the initial launch and the difficulty also being too low we have changed the ports and are relaunching fresh with 1.0.0 again.
- Somehow the Chia certs also ended up in the final release which was not intended.
- This is the inital release of the Chinilla blockchain.
- This release is aligned with Chia version 1.3.3
- Uses port 43444

### Changed

-  `mainnet` is now `vanillanet`
-  `xch`, `txch` is now `hcx`, `thcx` respectively
-  `mojo` is now `vojo`
- Updated gui theme and colors to make unique and separate from other forks
- Changed pre-mine to a 21,000 HCX as a modest dev fee and to support future development and products


#

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),

and this project does not yet adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

for setuptools_scm/PEP 440 reasons.
