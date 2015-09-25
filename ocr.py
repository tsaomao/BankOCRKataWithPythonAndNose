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

  def __init__(self):
    self.n1 = OcrNumeral(("   " +
                          "  |" +
                          "  |"), 1, [7])
    self.n2 = OcrNumeral((" _ " +
                          " _|" +
                          "|_ "), 2, [])
    self.n3 = OcrNumeral((" _ " +
                          " _|" +
                          " _|"), 3, [9])
    self.n4 = OcrNumeral(("   " +
                          "|_|" +
                          "  |"), 4, [])
    self.n5 = OcrNumeral((" _ " +
                          "|_ " +
                          " _|"), 5, [6, 9])
    self.n6 = OcrNumeral((" _ " +
                          "|_ " +
                          "|_|"), 6, [5, 8])
    self.n7 = OcrNumeral((" _ " +
                          "  |" +
                          "  |"), 7, [1])
    self.n8 = OcrNumeral((" _ " +
                          "|_|" +
                          "|_|"), 8, [6, 9, 0])
    self.n9 = OcrNumeral((" _ " +
                          "|_|" +
                          " _|"), 9, [3, 8])
    self.n0 = OcrNumeral((" _ " +
                          "| |" +
                          "|_|"), 0, [9])


class BankOcr:
  """BankOcr class to fulfill OCR Kata.

  Assumptions:
  """
  pass

