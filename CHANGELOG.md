# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project does not yet adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
for setuptools_scm/PEP 440 reasons.

## [Unreleased]


## 1.1.0 Chinilla Blockchain 2022-04-04

### WARNING

- This is a hard fork from last release with a completely new genesis challenge.
- There was an issue with the previous release as the initial difficulty was set too low and was causing the timelords to overload.  The difficulty is now sreset to initial Chia defaults.
- ***NOTE You will have to delete your Chinilla data folders and re initialize with this version if you downloaded the blockchain before 9:00pm PST.  This was determined as the best course of action to fix the issue.***
- Chinilla folders usually located at `~/.chinilla`

### Changed

- Changed genesis challenge


## 1.0.0 Chinilla Blockchain 2022-04-03

### Notes

- This is the inital release of the Chinilla blockchain.
- This release is aligned with Chia version 1.3.3
- Uses port 42444

### Changed

- `mainnet` is now `vanillanet`
- `xch`, `txch` is now `hcx`, `thcx` respectively
- `mojo` is now `vojo`
- Updated gui theme and colors to make unique and separate from other forks
- Changed pre-mine to a 21,000 HCX as a modest dev fee and to support future development and products