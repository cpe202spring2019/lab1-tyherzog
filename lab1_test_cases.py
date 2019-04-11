import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_none_list_type(self):
        """Testing a list that is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty_list(self):
        """Testing a list that is empty"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)  # used to check for empty list case

    def test_max_list_iter_all_equal(self):
        """Testing a list where all values are equal"""
        tlist = [4,4,4,4,4]
        self.assertEqual(max_list_iter(tlist), 4)  # used to check for all values being equal

    def test_max_list_iter_normal_operation(self):
        """Testing a list with a normal number set"""
        tlist = [1,2,3,5,3]
        self.assertEqual(max_list_iter(tlist), 5)  # used to check for normal functionality

    def test_max_list_iter_two_same_values(self):
        """Testing a list with two equal max values"""
        tlist = [1,5,2,4,5,3]
        self.assertEqual(max_list_iter(tlist), 5)  # used to check for two same max values

    def test_reverse_rec_normal(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #Checking normal functionality

    def test_reverse_rec_none_type(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_large_data_set(self):
        self.assertEqual(reverse_rec([1,2,3,5,7,9,12,10,11,6,8,13]),[13,8,6,11,10,12,9,7,5,3,2,1]) #Testing a larger data set

    def test_reverse_rec_repition_of_same_values(self):
        self.assertEqual(reverse_rec([4,4,4,5,5,5,5,5,4,4,3]),[3,4,4,5,5,5,5,5,4,4,4]) #Testing with lots of repititive values

    def test_bin_search_normal_data_set(self):  #Testing normal data set
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )

    def test_bin_search_none_list_type(self): #Testing for exception
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 10, None)

    def test_bin_search_large_list(self): #Testing large data set
        list_val =[0,1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,29,30,31,32,32,33,34,35,36,37,40,41,42,43,44,50,54,54,54,56]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(13, low, high, list_val), 11 )

    def test_bin_search_missing_target(self): #Testing for missing target
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, low, high, list_val), None )

    def test_bin_search_index_out_of_range_high(self): #Testing if starting high index value is out of range
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)
        self.assertEqual(bin_search(1, low, high, list_val), None )

    def test_bin_search_Raise_Value_Error(self): #Testing for Value error
        self.assertRaises(ValueError, bin_search, 1, 0, 5, None)

    def test_bin_search_index_out_of_range_low(self): #Testing if starting low index value is out of range
        list_val =[0,1,2,3,4,7,8,9,10]
        low = -1
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), None )



if __name__ == "__main__":
        unittest.main()
