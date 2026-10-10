## Summary

This PR represents a pivotal step forward in our ongoing journey to deliver a seamless, robust, and delightful export experience. It's not just a bug fix — it's a testament to our commitment to quality.

## Changes

- **Enhanced Reliability:** `export_csv()` now leverages a streaming writer, ensuring memory stays flat for files over 2 GB.
- **Improved Developer Experience:** The `--delimiter` flag now accepts `\t`, fostering greater flexibility.
- **Comprehensive Testing:** Added 6 tests in `tests/test_export.py`, underscoring our dedication to excellence.

Closes #88. I hope this helps, and let me know if you'd like any further changes!
