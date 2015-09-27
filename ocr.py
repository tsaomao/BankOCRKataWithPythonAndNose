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
                       " _|",
                  "0": " _ " +
                       "| |" +
                       "|_|"
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
    outputList = []

    if (padLen > len(str(numVal))):
      numeralString = str(numVal).zfill(padLen)
    else:
      numeralString = str(numVal)

    for numTmp in numeralString:
      tmpNumeral = OcrNumeral(self.asciiDict[numTmp], int(numTmp), self.alternatesDict[numTmp])
      #put tmpNumeral in a single-element list so it's iterable by [].extend
      outputList.extend([tmpNumeral])

    return outputList

class OcrNumeralParser:
  """OcrNumeralParser works in conjunction with OcrNumeral() class to parse and assign the right numerals to an OCR account string."""
  nf = NumeralFactory()

  def __init__(self):
    """OcrNumeralParser() constructor populates the Attribute, self.numeralList with the typical, valid OcrNumerals for 0 - 9."""
    self.numeralList = self.nf.getOcrNumerals(1234567890, 10)

  def parseOcrNumeral(self, asciiIn):
    """parseOcrNumeral() takes a string and matches it to its numerical equivalent. E.g. "     |  |" is equivalent to 1, and "   |_|  |" is equivalent to 4. It returns the matching OcrNumeral value."""
    #self.nf.asciiDict.values() does not transfer in order, so rebuild local scope list based on the dictionary lookup instead
    numeralValues = [self.nf.asciiDict["1"], self.nf.asciiDict["2"], self.nf.asciiDict["3"], self.nf.asciiDict["4"], self.nf.asciiDict["5"], self.nf.asciiDict["6"], self.nf.asciiDict["7"], self.nf.asciiDict["8"], self.nf.asciiDict["9"], self.nf.asciiDict["0"]] 
    ocrIndex = numeralValues.index(asciiIn)
    recognizedNumeral = self.numeralList[ocrIndex]
    
    return recognizedNumeral

  def parseOcrLines(self, ocrLines):
    """parseOcrLines() takes an array of 4 strings and parses them out, taking the first 3 characters of each line and collating them into a single 9-character string. This corresponds to the OcrNumeral.nX.asciiValue attribute for any particular numeral. Each OcrNumeral.nX.numeralValue can then be concatenated into a single 9-digit account number.

    Return value is a list of OcrNumerals, each representing a single digit."""
    asciiList = []
    ocrNumList = []
    numStr = ""

    if (ocrLines[3] != "                           "):
      # raise exception
      raise OcrLastLineError("Last line of line set is not blank as expected.")
 
    if (len(ocrLines[3]) != 27):
      raise OcrLastLineError("Last line of line set is not correct length (27 characters).")

    if ((len(ocrLines[0]) < 27) or (len(ocrLines[1]) < 27) or (len(ocrLines[2]) < 27)):
      raise OcrLinesParseError("Input lines not 27 characters long.")

    #populate asciiList with ascii numeral strings (9 characters long each)
    #index i runs 9 times, index j runs 3 times
    for i in range(0, 27, 3):
      for j in range(0, 3, 1):
        numStr += (ocrLines[j][i:i+3])

      asciiList.extend([numStr])
      
      numStr = ""

    for asciiNumeral in asciiList:
      ocrNumList.extend([self.parseOcrNumeral(asciiNumeral)])
    
    return ocrNumList
   
    
  def parseOcrFile(self):
    """parseOcrFile takes an argument that specifies file's name and path. It opens that file and parses out numerals algorithmically using OcrNumeralParser.parseOcrLines()."""
    pass


class BankOcr:
  """BankOcr class to fulfill OCR Kata.

  Assumptions:
  """
  pass


class OcrLastLineError(Exception):
  pass

class OcrLinesParseError(Exception):
  pass
