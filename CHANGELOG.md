## V1.0.0 (12/24/24)

```
-Updated README
-Added convert_file function
```

## V1.0.1 (12/24/24)

```
-Added github repository to PyPi page.
```

## V1.0.2 (12/24/24)

```
-Updated README.md to include all current features.
  -Removed roadmap section.
```

## V1.0.3 - 1.0.9 (12/24/24)

```
-Fixed convert_file function not responding in CMD.
-Tested higher quality video downloads.
```

## V1.1.0 (12/29/24)

```
-Formated using black.
```

## V2.0.0 (6/23/25)

```
Added
-----
- Created separate files for each function to improve readability.
- Added file conversion functionality using ffmpeg.
- Included reminder that file paths with spaces must be enclosed in double quotes.
- Built base functionality for a home screen.
- Implemented error detection and handling.
- Added reminder to install required packages when using the .exe version.
- Restored and updated requirements.txt with all necessary dependencies.

Changed
-------
- Converted convert_file.py from raw script to a structured function.
- Updated convert_file function to import directly from convert_file.py.
- Replaced the main download function with a modular, file-based version.
- Updated README.md with new instructions and usage information.
- Corrected project naming from "EToolsByEndie" to "EToolsbyEndie".

Fixed
-----
- Improved file download formatting to follow best practices.

Removed
-------
- Removed requirements.txt temporarily during cleanup.
- Removed requirements from setup.py.
- Removed old testing code and comment labels.

Restored
--------
- Re-added requirements section to setup.py after earlier removal.
```

## V2.1.0 (6/27/25)

Added - Error detection with colors
Fixed - All functions running at program start