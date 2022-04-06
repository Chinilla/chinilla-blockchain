# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project does not yet adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
for setuptools_scm/PEP 440 reasons.

## [Unreleased]


## 1.0.0 Chinilla Blockchain 2022-04-03

### Notes

- Due to a side-chain attack on the initial launch and the difficulty also being too low we have changed the ports and are relaunching fresh with 1.0.0 again.
- Somehow the Chia certs also ended up in the final release which was not intended.
- This is the inital release of the Chinilla blockchain.
- This release is aligned with Chia version 1.3.3
- Uses port 43444

### Changed

- `mainnet` is now `vanillanet`
- `xch`, `txch` is now `hcx`, `thcx` respectively
- `mojo` is now `vojo`
- Updated gui theme and colors to make unique and separate from other forks
- Changed pre-mine to a 21,000 HCX as a modest dev fee and to support future development and products
