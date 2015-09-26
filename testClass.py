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

  def testOcrNumeralInstantiationAndInit(self):
    ocrNumParser = OcrNumeralParser()
    assert_is_instance(ocrNumParser, OcrNumeralParser)

  def testOcrNumeralsInOcrNumeralParser(self):
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
