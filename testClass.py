from nose.tools import assert_is, assert_is_instance, assert_in, assert_equal, raises
from ocr import *

class TestOcrNumeral:

  def testOcrNumeralInstantiationAndInit(self):
    ocrString = ( "   " 
                  "|_|" 
                  "  |" )
    ocrNum = OcrNumeral(ocrString, 4, [9])
    assert_equal(ocrString, ocrNum.asciiValue)
    assert_equal(4, ocrNum.numeralValue)
    assert_equal([9], ocrNum.alternateValues)
