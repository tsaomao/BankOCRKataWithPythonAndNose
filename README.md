# Bank OCR Kata

Implement OCR Scan parsing and validating for 9-digit ASCII presented account numbers.

(Details: http://codingdojo.org/cgi-bin/index.pl?KataBankOCR)

# Status

This kata is currently in progress, on use case step/user story 1.

## To do:
### Step 1:
- Implement OcrNumeralParser.parseOcrLines() Method.
- Implement OcrNumeralParser.parseOcrFile() Method.

### Step 3:
- Refactor numeral storage so it's easier to look up abnormal scan results against dictionary or other storage scheme for numeral definitions (data storage should support easy slices, slice comparisons, lookups, and indexing).

## Problem statements:
- Parse 3-high ASCII based numerical characters into numerical strings. E.g.:

            _  _     _  _ _  _  _  _
          | _| _||_||_ |_  ||_||_|| |
          ||_  _|  | _||_| ||_| _||_|
          
  should parse as "1234567890"
- Each entry is 4 lines long, and each line has 27 characters. The first 3 lines of each entry contain an account number written using pipes and underscores, and the fourth line is blank. Each account number should have 9 digits, all of which should be in the range 0-9. A normal file contains around 500 entries.
- Not all scans are perfect. Validate account numbers according to a checksum
- Output a report including valid numbers, errors in checksums (ERR), and illegible characters (ILL)
- Use some intelligence to try to narrow the field in cases of illegible character that may be missing one pipe or underscore. Use the checksum to compare possible interpretations of illegible characters with valid account numbers. Add readout with ambiguous reports tatus (AMB) and a list of possible valid account numbers.
- Write the key algorithms in both iteration and recursion methods
- See Kata URL for proposed test cases.
