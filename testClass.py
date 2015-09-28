from nose.tools import assert_is, assert_is_instance, assert_in, assert_equal, raises
from ocr import *

class TestOcrNumeral:

  def testOcrNumeralInstantiationAndInit(self):
    ocrString = ( "   " +
                  "|_|" +
                  "  |" )
    ocrNum = OcrNumeral(ocrString, 4, [9])
    assert_is_instance(ocrNum, OcrNumeral)
    assert_equal(ocrString, ocrNum.asciiValue)
    assert_equal(4, ocrNum.numeralValue)
    assert_equal([9], ocrNum.alternateValues)


class TestAccountNumber:

  def testAccountNumber(self):
    acct = AccountNumber(45)
    assert_is_instance(acct, AccountNumber)
    assert_equal(45, acct.accountNumber)
    assert_equal("000000045", acct.accountString)


class TestNumeralFactory:

  def testNumeralFactory(self):
    numAsc = ("   " +
              "|_|" +
              "  |")
    nf = NumeralFactory()
    ocrNum1 = nf.getOcrSingleton(4)
    assert_equal(numAsc, ocrNum1.asciiValue)
    assert_equal(4, ocrNum1.numeralValue)
    assert_equal([], ocrNum1.alternateValues)

  def testNumeralFactoryList(self):
    num1 = 45
    pad1 = 9
    num2 = 111111111
    pad2 = 9
    num3 = 45
    pad3 = 1
    nf = NumeralFactory()

    #should generate a 9 element list of OcrNumeral classes based on the string "000000045"
    list1 = nf.getOcrNumerals(num1, pad1)
    assert_equal(9, len(list1))
    assert_equal(0, list1[0].numeralValue)
    assert_equal(5, list1[8].numeralValue)

    #should generate a 9 element list of OcrNumeral classes based on the string "111111111"
    list2 = nf.getOcrNumerals(num2, pad2)
    assert_equal(9, len(list2))
    assert_equal(1, list2[0].numeralValue)
    assert_equal(1, list2[8].numeralValue)
    
    #should generate a 2 element list of OcrNumeral classes based on the string "45"
    list3 = nf.getOcrNumerals(num3, pad3)
    assert_equal(2, len(list3))
    assert_equal(4, list3[0].numeralValue)
    assert_equal(5, list3[1].numeralValue)
    

class testOcrNumeralParser:

  def testOcrNumeralParserInstantiationAndInit(self):
    ocrNumParser = OcrNumeralParser()
    assert_is_instance(ocrNumParser, OcrNumeralParser)

  def testOcrNumeralsListInOcrNumeralParser(self):
    onp = OcrNumeralParser()
    num1 = ("   " +
            "  |" +
            "  |")
    num2 = (" _ " +
            " _|" +
            "|_ ")
    num3 = (" _ " +
            " _|" +
            " _|")
    num4 = ("   " +
            "|_|" +
            "  |")
    num5 = (" _ " +
            "|_ " +
            " _|")
    num6 = (" _ " +
            "|_ " +
            "|_|")
    num7 = (" _ " +
            "  |" +
            "  |")
    num8 = (" _ " +
            "|_|" +
            "|_|")
    num9 = (" _ " +
            "|_|" +
            " _|")
    num0 = (" _ " +
            "| |" +
            "|_|")
    assert_equal(num1, onp.numeralList[0].asciiValue)
    assert_equal(num2, onp.numeralList[1].asciiValue)
    assert_equal(num3, onp.numeralList[2].asciiValue)
    assert_equal(num4, onp.numeralList[3].asciiValue)
    assert_equal(num5, onp.numeralList[4].asciiValue)
    assert_equal(num6, onp.numeralList[5].asciiValue)
    assert_equal(num7, onp.numeralList[6].asciiValue)
    assert_equal(num8, onp.numeralList[7].asciiValue)
    assert_equal(num9, onp.numeralList[8].asciiValue)
    assert_equal(num0, onp.numeralList[9].asciiValue)

    assert_equal(1, onp.numeralList[0].numeralValue)
    assert_equal(2, onp.numeralList[1].numeralValue)
    assert_equal(3, onp.numeralList[2].numeralValue)
    assert_equal(4, onp.numeralList[3].numeralValue)
    assert_equal(5, onp.numeralList[4].numeralValue)
    assert_equal(6, onp.numeralList[5].numeralValue)
    assert_equal(7, onp.numeralList[6].numeralValue)
    assert_equal(8, onp.numeralList[7].numeralValue)
    assert_equal(9, onp.numeralList[8].numeralValue)
    assert_equal(0, onp.numeralList[9].numeralValue)

    assert_equal([7], onp.numeralList[0].alternateValues)
    assert_equal([], onp.numeralList[1].alternateValues)
    assert_equal([9], onp.numeralList[2].alternateValues)
    assert_equal([], onp.numeralList[3].alternateValues)
    assert_equal([6, 9], onp.numeralList[4].alternateValues)
    assert_equal([5, 8], onp.numeralList[5].alternateValues)
    assert_equal([1], onp.numeralList[6].alternateValues)
    assert_equal([6, 9, 0], onp.numeralList[7].alternateValues)
    assert_equal([3, 8], onp.numeralList[8].alternateValues)
    assert_equal([9], onp.numeralList[9].alternateValues)

  def TestParseNumeral(self):
    onp = OcrNumeralParser()
    # 1
    ascii1 = "     |  |"
    # 4
    ascii2 = "   |_|  |"
    # 9
    ascii3 = " _ |_| _|"

    rnum1 = onp.parseOcrNumeral(ascii1)
    rnum2 = onp.parseOcrNumeral(ascii2)
    rnum3 = onp.parseOcrNumeral(ascii3)

    assert_equal(1, rnum1.numeralValue)
    assert_equal(ascii1, rnum1.asciiValue)
    assert_equal([7], rnum1.alternateValues)

    assert_equal(4, rnum2.numeralValue)
    assert_equal(ascii2, rnum2.asciiValue)
    assert_equal([], rnum2.alternateValues)

    assert_equal(9, rnum3.numeralValue)
    assert_equal(ascii3, rnum3.asciiValue)
    assert_equal([3, 8], rnum3.alternateValues)

  def TestParseOcrLines(self):
    onp = OcrNumeralParser()

    #111111111
    ocrAscii1 = ["                           ", "  |  |  |  |  |  |  |  |  |", "  |  |  |  |  |  |  |  |  |", "                           "]    
    #444444444
    ocrAscii2 = ["                           ", "|_||_||_||_||_||_||_||_||_|", "  |  |  |  |  |  |  |  |  |", "                           "]
    #123456789
    ocrAscii3 = ["    _  _     _  _  _  _  _ ", "  | _| _||_||_ |_   ||_||_|", "  ||_  _|  | _||_|  ||_| _|", "                           "]

    numList1 = onp.parseOcrLines(ocrAscii1)
    numList2 = onp.parseOcrLines(ocrAscii2)
    numList3 = onp.parseOcrLines(ocrAscii3)

    # Test list 1
    assert_equal("     |  |", numList1[0].asciiValue)
    assert_equal(1, numList1[0].numeralValue)
    assert_equal([7], numList1[0].alternateValues)

    # Test list 2
    assert_equal("   |_|  |", numList2[0].asciiValue)
    assert_equal(4, numList2[0].numeralValue)
    assert_equal([], numList2[0].alternateValues)

    # Test list 3
    assert_equal(" _   |  |", numList3[6].asciiValue)
    assert_equal(7, numList3[6].numeralValue)
    assert_equal([1], numList3[6].alternateValues)
    
  @raises(OcrLastLineError)
  def TestParseOcrLinesExceptionLastLineErrorMalformed(self):
    onp = OcrNumeralParser()
    #Non-blank last line.
    ocrAscii = ["                           ", "  |  |  |  |  |  |  |  |  |", "  |  |  |  |  |  |  |  |  |", "           ++              "]
    numListTest = onp.parseOcrLines(ocrAscii)

  @raises(OcrLastLineError)  
  def TestParseOcrLinesExceptionLastLineErrorWrongLength(self):
    onp = OcrNumeralParser()
    #Short last line.
    ocrAscii = ["                           ", "  |  |  |  |  |  |  |  |  |", "  |  |  |  |  |  |  |  |  |", "                         "]
    numListTest = onp.parseOcrLines(ocrAscii)

  @raises(OcrLinesParseError)
  def TestParseOcrLinesExceptionParseError(self):
    onp = OcrNumeralParser()
    #Short line 2 (ocrAscii[1]).
    ocrAscii = ["                           ", "  |  |  |  |  |  |  |  |  |", "  |  |  |  |  |  |  |  |", "                           "]
    numListTest = onp.parseOcrLines(ocrAscii)
     
  def TestParseOcrNumList(self):
    onp = OcrNumeralParser()
    nf = NumeralFactory()
    list = nf.getOcrNumerals(873626531, 9)
    numStr = onp.parseOcrNumList(list)

    assert_equal("873626531", numStr)

  def TestParseOCRFile(self):
    onp = OcrNumeralParser()
    filePath = "./testcase1-validonly.ocr"
    listOfOcrLists = onp.parseOcrFile(filePath)
    listOfAcctStrings = []

    for ocrList in listOfOcrLists:
      listOfAcctStrings.extend([onp.parseOcrNumList(ocrList)])

    assert_equal("000000000", listOfAcctStrings[0])
    assert_equal("111111111", listOfAcctStrings[1])
    assert_equal("222222222", listOfAcctStrings[2])
    assert_equal("333333333", listOfAcctStrings[3])
    assert_equal("444444444", listOfAcctStrings[4])
    assert_equal("555555555", listOfAcctStrings[5])
    assert_equal("666666666", listOfAcctStrings[6])
    assert_equal("777777777", listOfAcctStrings[7])
    assert_equal("888888888", listOfAcctStrings[8])
    assert_equal("999999999", listOfAcctStrings[9])
    assert_equal("123456789", listOfAcctStrings[10])


class TestCustomExceptions:

  def testOcrLastLineError(self):
    ex = OcrLastLineError()
    assert_is_instance(ex, OcrLastLineError)
    
    ex = OcrLinesParseError(self)
    assert_is_instance(ex, OcrLinesParseError)



