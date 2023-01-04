# Changelog

All notable changes to this project will be documented in this file.

## 1.4.0 Chinilla blockchain 2023-01-03

This release aligns with Chia 1.6.2

### Added

- Add WalletConnect
- Add Bladebit v2 plotting support (RAM and Disk)
- Add `chinilla keys show --json` (display all keys as json) (thanks @kimsk)
- Add `chinilla data get_sync_status` CLI and RPC.
- Add download progress log and stream in Datalayer (thanks @Chida82)
- Add wallet RPC `/get_spendable_coins`
- Add wallet RPC `/get_coin_records_by_names`
- Add wallet RPC `/verify_signature`
- Add wallet RPC `/did_message_spend`
- Add wallet RPC `/did_get_info`
- Add wallet RPC `/nft_set_did_bulk`
- Add options `--max-coin-amount` and `--exclude-coin-ids` to `chinilla wallet send`
- Add `--fingerprint` option to `chinilla keys show`
- Add SECURITY.md
- Add GUI support for adding and removing full node peers
- New GUI setting for NFT image scaling
- New GUI warning if the GUI version is different from the back-end version

### Changed

- Remove legacy keyring support
- Drop support for bladebit v1 and use bladebit v2 for RAM and Disk plots
- Removed remaining vestiges of defunct backup service
- `debug_spend_bundle` -- print coin id as hex string
- Only open SQLite log file once per db wrapper
- Switch to context manager for task timing instrumentation
- Revert rate limiting messages from `warning` back to `debug`
- `add_private_key` now returns the fingerprint of the added key
- SQLite log the full node db version check
- Delete DID wallet after transfer
- Don't validate weight proof on wallet log_in
- Drop broken message types logging
- Return minted NFT ID & Allow transfer NFT with NFT ID
- Display key labels when making a wallet key selection
- Add support for pending transactions to `get_mempool_item_by_tx_id()` (thanks @rwarren)
- Simplify the mempool manager instantiation
- Add coin id and address to NFT Details screen in GUI
- New GUI prefs location under `CHINILLA_ROOT`
- Removed SkyNFT references
- Add GUI memo field when sending HCX
- Update to Electron 20.3.5

### Fixed

- Fixed a missing state_changed GUI notification
- Minor sync optimizations and refactor; eliminate redundant weight proof requests
- Upped the number of file handles for madmax
- Catch exceptions raised when resolving plot directories (fix #13723)
- Call close callback for already closed connections (fix #9172)
- Set GUI binary name to `chinilla-blockchain` in the Fedora rpm and Ubuntu deb (fix #13847)
- Add simple fix to set farmer response timer for `SP: 0` (fix #11869, #10900) (thanks @neurosis69)
- Preserve correct `MempoolItem` block height when rebuilding mempool
- Windows: start daemon without a window and detached from current console (fix #13175) (thanks @jcteng)
- Fix pool singleton sync height in DB
- Remove duplicate nft wallet deletion in reorg
- Fix DID unnecessary wallet deletion
- Improve performance of wallets with many NFTs
- Stop creating unecessary index in notification store (fix #13955)
- Fix issues in switching pools introduced in 1.6.0 (fix #13872)
- Handle incoming unknown capabilities
- GUI Offer Builder displays totals with royalties when requesting an NFT
- Fixed NFT inbox detection
- Convert and cache NFT metadata as UTF-8
- Fixed issue with switching between farmer and wallet modes (GUI issue #1005)
- Improve error message when sending more mojos than Spendable Balance

## 1.3.0 Chinilla blockchain 2022-10-16

This release aligns with Chia 1.6.0.

### Added
- DataLayer
- HCX Spam Filter
- GUI Settings `Auto-Login` toggle (GUI only)
- GUI Settings section for `DataLayer`
  - `Enable DataLayer` toggle
  - `Enable File Propagation Server` toggle

### Modified
- Delayed pool config update until after sync
- Minor change to handling sync height to avoid race condition with blockchain DB
- Ignore `FileNotFoundError` when checking SSL file permissions if the file doesn’t exist

### Fixed
- Fixed missing wallet `state_changed` events for GUI
- Fixed several bugs related to wallet sync status
- Fixed GUI issue for CAT offers where the CAT Tail would not show in the tooltip for `Unknown CAT`s (https://github.com/Chinilla-Network/chinilla-blockchain-gui/issues/950)

### Known Issues
- The CLI command `chinilla configure --enable-data-server`, and the `config.yaml` parameter at `data_layer.run_server` have no effect, and will be removed in the future
- DataLayer offers cannot be accepted (`take_offer`) if the offer has inclusions for the exact same key/value data for both maker and taker inclusions.


## 1.2.1 Chinilla blockchain unreleased

### Notes

This release aligns with Chia 1.5.1

### Added

- Add Source and Changelog to project_urls (Thanks @strayer!)
- Add condition code constant for REMARK, an always true Chinillalisp condition
- Add several wallet optimizations
- Add `chinilla db backup --backup-file <backup_file_destination>` (Thanks @neurosis69!)
- Add debug option to log all SQL commands for wallet db (Thanks @neurosis69!)
- Additional data for `get_wallet_balance` and `get_wallets` endpoints
- Add `change_data` to `_state_changed` since the later calls expect it
- Add `Program.replace`
- Add `new_transaction()` to `DBWrapper2`
- Add RPCs for getting/extending the current derivation path index
- Add symlinks to the UI RPM to mirror the .deb UI and the CLI installers
- Add support for excluding coins in `create_signed_transaction` wallet RPC (Thanks @felixbrucker!)
- Add small coin selection improvements
- Add bulk cancel API
- Introduce `streamable.Field`
- Introduce `Streamable.__post_init__` processing cache
- Added minimum coin amount to various RPC calls
- Added new full_node RPC called `get_block_spends` - Get spends for block using transaction generator
- Support for remembering the last used wallet key
- Documented deserialization length limitations (8191 bytes) in CLVM ROM. We recommend using a local version of the chinillalisp code when necessary

### Changed

- Huge speedup in trusted wallet sync
  - Previous time to sync 1000 tx: 90 seconds
  - New time: 2 seconds
- Force keyring migration / Deprecate legacy keyring support
- Renaming series -> editions (full deprecation) (Thanks @DrakoPensulo!)
- Made various additions to the cache, and changes to validation to reduce CPU usage significantly
- Log full errors when `run_as_generator()` throws error
- Sort `plot_paths` before splitting it into batches
- Skip `plot_sync_callback` if `delta` is `None`
- Validate the path in `add_plot_directory`
- Cache convert functions from `dataclass_from_dict`
- Big thanks to @neurosis69 for the following:
  - Allow bigger chunks of bind variables per SQL statement
  - Execute SQL updates as chunks in `_set_spent function` for `tx_removals`
  - Optimized column selection in various tables to use specific columns rather than all columns
  - Write blockchain DB full node startup progress to debug.log
- Clean up and Refactor `chinilla show` command
- Increment the dirty counter when setting `height-to-hash` map entries
- `plotting.cache.DiskCache` -> `util.misc.VersionedBlob`
- Improve `chinilla farm summary`
- Optimize `std_hash` in `coin.py`
- Improved many tests
- Remove `big_ints` list
- Improved UX for `plotnft claim`
- Upgrade `chia-rs` to streamable support
- Allow switching keys during sync
- Optimize `get_hash` by not double converting
- Don't re-hash the same objects
- Drop redundant `PlotPathRequestData` conversion
- Make `PlotsRefreshParameter` streamable + use `from_json_dict`
- Make `Plot{Info|Path}RequestData` streamable + use `from_json_dict`
- Optimize request additions
- Stop and join watchdog observer
- Remove chinilla.util.path.mkdir()
- Remove the constants_json field
- Don't convert `ConsensusConstants` to/from JSON
- Move some class methods out of `Streamable`
- Request header blocks, and new rate limits
- Replaced the python implementation of `Coin` with the Rust native `Coin` from `chia_rs`
- Watchdog==2.1.9 for bad file descriptor avoidance
- Be specific about `*args` in `RpcServer` state changed methods
- Make WalletUserStore.create_wallet() raise on failure, and return non-optional
- Switch back to official dnspython for v2.2.0
- Not optional - `WalletNode.wallet_state_manager`, `.server`, `.keychain_proxy`
- More `uint64()` for NFT coin amount
- Delay `WalletNode._new_peak_queue` instantiation to avoid errors
- Remove unused `WalletCoinStore.get_unspent_coins_at_height`
- `NFTInfo.royalty_puzzle_hash` is `Optional` but not `None` here
- Handle `KeychainProxyConnectionFailure` in `Farmer.setup_keys`
- Made simplifications to the `WalletCoinStore` class
- Removed wallet transaction store cache
- Removed double `bytes32` conversion
- Turn `dataclass_from_dict` into `streamable_from_dict`
- Replace service `running_new_process=` parameter by `.setup_process_global_state()` method
- Changed wallet peer selection to prefer nodes in the following order
  1. trusted & synced
  2. untrusted & synced
  3. trusted & unsynced
  4. untrusted & unsynced
- Simplified pool cache
- Remove unused finished_sync_up_to (Thanks @olivernyc!)
- Expand `Field` and introduce `Streamable._streamable_fields`
- Removing `logging.basicConfig()` from `ChinillaServer.__init__()`
- Use coin selection algorithm for DID wallets
- Simplify service start configuration loading
- Wallet network messages now have higher priority than Node network messages
- Wallet now checks the mempool before adding new transactions to the queue
- Implemented new context manager for DB access (DBWrapper2) that supports nested transactions, improved support for concurrency, and simplified exception handling
- Upgraded `clvm-tools-rs` to `0.1.19`
- Upgraded `clvm_tools` to `0.4.5`
- Simplify wallet transaction store
- Remove unused `_clear_database()` functions
- Optimized wallet DB queries using `execute_fetchall`
- Optimize wallet `set_spent()`
- Added support for minimum coin amount and excluding coins in `select_coin` RPC
- Log `chinilla_full_version_str` in daemon and all services
- On failure to get keys, log and return exception
- Update certificate store as of July 19, 2022
- Optimize puzzlehash generation (~65% faster)
- Deprecated the ability to disable the keyring passphrase feature
- Minor simplifications to derivation records
- Update protocol message checks
- Changed `initial_num_public_keys` default to 425
- Minor optimizations for block store
- Optimize get_coins_to_check()
- Minor wallet optimizations when determining coin type
- Avoid redundant printing of puzzle program in NFT uncurry attempt
- Substantially reduced overall size of Chinilla packages
- Log the plot refresh parameter on start
- Log blockchain database file used along with schema version on startup
- Removed redundant request for SubEpochData

### Fixed

- Log error for failed service start
- Improve logging in `plot_sync.{receiver|delta}`
- Fix default value assignments for `dataclass_from_dict` for streamable
- Fix `change_payout_instructions` for invalid addresses
- Fix SQL error when only config file is deleted
- Fix issue with wallet not handling rejection from unsynced local node properly
- Fix for transfer NFT with DID
- Fix misleading argument name (Thanks @olivernyc!)
- Fix knapsack coin selection
  - Old performance with 200k coins: 60 seconds
  - New: 0.78 seconds.
- Fix trusted_peer example in initial-config.yaml by (Thanks @ojura!)
- Replace existing simulator config & Fix simulator
- Fix attribute error on `FullNode.simulator_transaction_callback`
- Fix passphrase hint
- Bump clvm_tools_rs for bug fix
- Fix NFT > CAT Royalty splitting bug
- Fixed `mint_nft`
- Fix no keys loaded error by making KeychainProxy automatically reconnect when a connection is lost
- Fix a migration bug of NFT table change
- NFT wallet reorg fix
- Fix NFT wallet naming issue
- Can't shadow `info` which is `NFTInfo` in the first place
- Initialize logging before Service instantiation
- Make sure chinilla commands output help when no args are given (#11013) (Thanks @noneus!)
- Fixed bugs in fork point calculation, and reduced number of times weight-proofs are validated
- Fixed bug in starting the crawler (set service name to `full_node`)
- NFT transfer/minting commands now validate the specified addresses
- Block summaries of CAT1 offers in the RPC and CLI

## 1.2.0 Chinilla blockchain 2022-7-26

### Notes

This release aligns with Chia 1.5.0

### Added

- Added derivation index information to the Wallet UI to show the current derivation index height
- Added section in Settings to allow the user to manually update the derivation index height in order to ensure the wallet finds all the coins
- Added a tooltip for users to understand why their CAT balance has changed as new CAT2 tokens get re-issued
- There is now a `blockchain_wallet_v2_r1_*.sqlite` DB that will be created, which will sync from 0 to look for CAT2 tokens. This preserves a copy of your previous wallet DB so that you are able to look up previous transactions by using an older wallet client
- Extended `min_coin` to RPC calls, and CLI for coin selection
- Show DID in the offer preview for NFTs
- Added wallet RPCs (`get_derivation_index`, `update_derivation_index`) to enable the GUI, and CLI to report what the current derivation index is for scanning wallet addresses, and also allows a user to move that index forward to broaden the set of addresses to scan for coins

### Changed

- Changed the DID Wallet to use the new coin selection algorithm that the Standard Wallet, and the CAT Wallet already use
- Changed returning the result of send_transaction to happen after the transaction has been added to the queue, rather than it just being added to the mempool.
- Increased the priority of wallet transactions vs full node broadcasted transactions, so we don't have to wait in line as a wallet user
- Deprecated the `-st, --series-total` and `-sn, --series-number` RPC and CLI NFT minting options in favor of `-ec, --edition-count` and `-en, --edition-number` to align with NFT industry terms
- When creating a DID profile, a DID-linked NFT wallet is automatically created
- Update `chinilla wallet take_offer` to show NFT royalties that will be paid out when an offer is taken
- Added a parameter to indicate how many additional puzzle hashes `create_more_puzzle_hashes` should create

### Fixed

- Fixed [CVE-2022-36447] where in tokens previously minted on the Chinilla blockchain using the `CAT1` standard can be inflated in arbitrary amounts by any holder of the token. Total amount of the token can be increased as high as the malicious actor pleases. This is true for every `CAT1` on the Chinilla blockchain, regardless of issuance rules. This attack is auditable on-chain, so maliciously altered coins can potentially be "marked" by off-chain observers as malicious.
- Fixed issue that prevented websockets from being attempted if an earlier websocket failed
- Fixed issue where `test_smallest_coin_over_amount` did not work properly when all coins were smaller than the amount
- Fixed a performance issue with knapsack that caused it to keep searching for more coins than could actually be selected. Performance with 200k coins:
  - Old: 60 seconds
  - New: 0.78 seconds
- Fixed offer compression backwards compatibility
- Fixed royalty percentage check for NFT0 NFTs, and made the check for an offer containing an NFT more generalized
- Fixed timing with asyncio context switching that could prevent networking layer from responding to ping

## 1.1.0 Chinilla blockchain 2022-6-29

### Notes

This release aligns with Chia 1.4.0

### Added

- Added support for NFTs!!! :party:
- Added `chinilla wallet nft` command (see https://docs.chia.net/docs/13cli/did_cli)
- Added `chinilla wallet did` command (see https://docs.chia.net/docs/12rpcs/nft_rpcs)
- Added RPCs for DID (see https://docs.chia.net/docs/12rpcs/did_rpcs)
- Added RPCs for NFT (see https://docs.chia.net/docs/12rpcs/nft_rpcs)
- Enable stricter mempool rule when dealing with multiple extra arguments
- Added a retry when loading pool info from a pool at 2 minute intervals
- Added CLI options `--sort-by-height` and –sort-by-relevance` to `chinilla wallet get_transactions`
- Harvester: Introduce `recursive_plot_scan`
- Add libgmp-dev to Bladebit installation - thanks to @TheLastCicada
- Add support for multiple of the same CAT in aggregate offers - Thanks to @roseiliend

### Changed

- New coin selection algorithm based on bitcoin knapsack. Previously chinilla selected the largest coin
- Updated chiapos to 1.0.10
- Updated chiavdf to 1.0.6
- Updated blspy to 1.0.13
- Updated setproctitle to 1.2.3
- Updated PyYAML to 6.0
- Updated pyinstaller to 5.0
- Bump clvm_tools_rs version to 0.1.9 for clvm stepper and add a test
- Modest speedup of syncing by batching coin lookups
- Cmds: Use the new `plot_count` of `get_pool_state` in `plotnft show`
- Set mempool size back to the original size at launch
- Plotting|tests|setup: Improve `PlotManager` cache
- Wallet: Drop unused `WalletStateManager.get_derivation_index`
- Harvester: Tweak `get_plots` RPC
- Remove explicit multidict version from setup.py
- Simplify install.sh ubuntu version tracking
- Optimize BLS verification when public key is repeated
- Use Install.ps1 in build_windows.ps1
- Updated warning about `CHINILLA_ROOT` being set when running init
- Cmds: Adjust stop daemon output
- Remove unused functions on MerkleSet
- Optimize `hash_coin_list()`
- Update CONTRIBUTING.md
- Remove outdated 3.8 upgrade comment
- Hint refactor
- Replace MerkleSet with the rust implementation
- Simplify SizedBytes and StructStream
- Allow services to set a non-default max request body size limit
- Reduce the redundant computations of coin_ids in block_body_validation
- Uses the new `from_bytes_unchecked` method in blspy, to improve perfo…
- Remove the cache from CoinStore
- Keep daemon websocket alive during keyring unlock
- Support searching derived addresses on testnet.
- Optimize code to not perform useless subgroup checks
- Restore missing hints being stored as None (instead of 0-length bytes)
- Coin simplification
- Harvester: Use a set instead of a list to speed up availability checks
- Improved performance of debug log output
- Update plotters installation to include an `apt update` - thanks to @TheLastCicada
- Early return from `_set_spent function` - Thanks @neurosis69
- Remove redundant condition in `get_coin_records` - Thanks @neurosis69
- Write python version error to stderr - thanks to @LuaKT

### Fixed

- Fixed issues with harvesters not reconnecting properly - fixes #11466
- Return not synced if there are no connections - fixes #12090
- Fix issues with wallet resending transactions on various mempool and node errors - fixes #10873
- Fix some issues with `plotnft show` (#11897)
- Handle ephemeral ports and dual stack (ipv4 & ipv6)
- Fix issues when wallet syncing and rolling back too far in the past
- Fixes issues with the Farmer Reward dialog incorrectly reporting there is no private key (#11036)
- Fix race condition, blockchain can change between two calls to get_peak
- Wallet: Fix `CATLineageStore` creation in `create_new_cat_wallet`
- Fix incorrect return in "rollback_to_block"
- Wallet: Some rollback fixes
- Fix issue with missing coins
- Fix Newer block issue
- Fix jsonify bool
- Fix wallet introducers for testnet
- Correct wallet CLI sent/received indication
- Correct "Older block not found" error message
- Print MempoolInclusionStatus as string
- Optimize Program.curry()
- Improve detection of disconnected websocket between services
- Correct install.sh usage short options list
- Make sure we set the sync to height correctly when we roll back

## 1.0.5 Chinilla blockchain 2022-5-11

### Notes

This release aligns with Chia 1.3.5

### Added

- Added Support for Python 3.10
- Performance improvements in harvesters during plot refresh. Large farmers likely no longer need to specify a very high plot refresh interval in config.yaml
- Added CLI only `.rpm` and `.deb` packages to official release channels
- Fixed an issue where some coins would be missing after a full sync
- Enabled paginated plot loading and improved plot state reporting
- Updated the farming GUI tab to fix several bugs
- Fix infinite loop with timelord closing
- Simplified install.sh ubuntu version tracking
- Fixed memory leak on the farm page
- Fixed list of plot files "in progress"
- Various farmer rpc improvements
- Improvements to the harvester `get_plots` RPC

### Known Issues

There is a known issue where harvesters will not reconnect to the farmer automatically unless you restart the harvester. This bug was introduced in 1.3.4 and we plan to patch it in a coming release.

## 1.0.4 Chinilla Blockchain 2022-05-02

### Added

- Added support for sharing offers to the Chinilla.com Offer Trader from the GUI.

### Fixed

- Changed remaining references of `tails` to `tokens`


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
- CATs now have a link to Chinilla.com token database to look up the Asset ID
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

-  `vanillanet` is now `vanillanet`
-  `hcx`, `txch` is now `hcx`, `thcx` respectively
-  `mojo` is now `vojo`
- Updated gui theme and colors to make unique and separate from other forks
- Changed pre-mine to a 21,000 HCX as a modest dev fee and to support future development and products


#

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project does not yet adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for setuptools_scm/PEP 440 reasons.
