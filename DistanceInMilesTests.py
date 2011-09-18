from nose.tools import istest
import unittest
from DistanceInMiles import NegativeNumberException, DistanceInMiles
from UnittestAnnotations import should_raise

class DistanceInMilesTests(unittest.TestCase):

    @istest
    def raises_an_exception_when_attempting_to_convert_a_negative_number_using_try(self):
        try:
            DistanceInMiles.calculated_from(-5, "miles")
            self.fail("should raise an exception when converting from negative number")
        except:
            pass

    @istest
    def raises_an_exception_when_attempting_to_convert_a_negative_number_using_assertion(self):
        self.assertRaises(NegativeNumberException, DistanceInMiles.calculated_from, -5, "miles")

    @istest
    @should_raise(NegativeNumberException)
    def raises_an_exception_when_attempting_to_convert_a_negative_number_using_annotation(self):
        DistanceInMiles.calculated_from(-5, "miles")

    @istest
    @should_raise(NegativeNumberException)
    def should_not_be_creatable_using_negative_values(self):
        DistanceInMiles(-5, "miles")

    @istest
    def should_return_the_same_value_whenConverting_miles_to_miles(self):
        self.assertEquals(5 , DistanceInMiles.calculated_from(5, "miles"))

    @istest
    def should_return_the_distance_times_one_point_six_when_converting_from_kilometers(self):
        self.assertEquals( 5 * 1.6 , DistanceInMiles.calculated_from(5, "km"))


