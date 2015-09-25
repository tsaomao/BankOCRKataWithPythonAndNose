"""Module to implement Bank OCR Kata. See README.md for more information.

Bank OCR kata implements a thing that reads and validates example OCR numbers."""

class OcrNumeral:
  """OcrNumeral tracks each digit in an OCR application."""
  asciiValue = ""
  numeralValue = -1
  alternateValues = []
  
  def __init__(self, asciiVal, numVal, altVals):
    self.asciiValue = asciiVal
    self.numeralValue = numVal
    self.alternateValues = altVals

class OcrNumeralParser:
  """OcrNumeralParser works in conjunction with OcrNumeral() class to parse and assign the right numerals to an OCR account string."""
  pass


class BankOcr:
  """BankOcr class to fulfill OCR Kata.

  Assumptions:
  """
  pass

