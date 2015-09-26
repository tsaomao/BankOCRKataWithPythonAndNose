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

class AccountNumber:
  """AccountNumber holds account number and associated information."""
  accountNumber = 0
  accountString = ""
  accountNumerals = []

  def __init__(self, acctNum):
    self.accountNumber = acctNum
    self.accountString = str(self.accountNumber).zfill(9)

class NumeralFactory:
  """NumeralFactory outputs OcrNumerals for use in the rest of this project."""
  asciiDict = {}
  alternatesDict = {}

  def __init__(self):
    self.asciiDict = {
                  "0": " _ " +
                       "| |" +
                       "|_|",
                  "1": "   " +
                       "  |" +
                       "  |",
                  "2": " _ " +
                       " _|" +
                       "|_ ",
                  "3": " _ " +
                       " _|" +
                       " _|",
                  "4": "   " +
                       "|_|" +
                       "  |",
                  "5": " _ " +
                       "|_ " +
                       " _|",
                  "6": " _ " +
                       "|_ " +
                       "|_|",
                  "7": " _ " +
                       "  |" +
                       "  |",
                  "8": " _ " +
                       "|_|" +
                       "|_|",
                  "9": " _ " +
                       "|_|" +
                       " _|"
                }
    self.alternatesDict = {
                       "0": [9],
                       "1": [7],
                       "2": [],
                       "3": [9],
                       "4": [],
                       "5": [6, 9],
                       "6": [5, 8],
                       "7": [1],
                       "8": [6, 9, 0],
                       "9": [3, 8]
                     }

  def getOcrSingleton(self, numVal):
    """getOcrSingleton() returns a single OcrNumeral object based on a lookup for the first numeral in given number."""
    numStrTmp = str(numVal)[0]
    asciiTmp = self.asciiDict[numStrTmp]
    altsTmp = self.alternatesDict[numStrTmp]
    return (OcrNumeral(asciiTmp, int(numVal), altsTmp))

  def getOcrNumerals(self, numVal, padLen):
    """getOcrNumeral() returns a list of OcrNumerals based on the specified string length specified."""
    if (padLen > len(str(numVal))):
      numeralString = str(numVal).zfill(padLen)
    else:
      numeralString = str(numVal)

    for numeral in numeralString:
      outputList = outputList.extend(OcrNumeral((self.asciiDict[numeral], int(numeral), self.alternatesDict[numeral])))

    return outputList

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

  def parseOcrLines(self):
    """parseOcrLines() takes an array of 3 strings and parses them out, taking the first 3 characters of each line and collating them into a single string. This corresponds to the OcrNumeral.nX.asciiValue attribute for any particular numeral. Each OcrNumeral.nX.numeralValue can then be concatenated into a single 9-digit account number."""
    pass
    
  def parseOcrFile(self):
    """parseOcrFile takes an argument that specifies file's name and path. It opens that file and parses out numerals algorithmically using OcrNumeralParser.parseOcrLines()."""
    pass


class BankOcr:
  """BankOcr class to fulfill OCR Kata.

  Assumptions:
  """
  pass

