"""
   FileName: UnitTestCases_word_replacement.py
   Author:   Mohit Sharma(smw572)
   Program:  Unit test cases for the get_unique_words_frequency Method written as part of the Phase 1 (Initail project requirements)
"""

from program_word_replacement import get_updated_string_after_replacement
   # The code to test
import unittest   # The test framework
text = open("input_word_replacement.txt", "r")
input_string = text.read()
print(input_string)
        

class Test_wordcount(unittest.TestCase): 
       pass

       #Negative Scenarios
       def test_1_When_input_file_is_empty(self):
           text = open("input_emptyString.txt", "r");
           s = text.read()
           self.assertEqual(get_updated_string_after_replacement(s,"","Hi"), "Error: Input String is Empty")
           
       def test_2_When_any_of_the_input_words_are_an_empty_string(self):
           text = open("input_word_replacement.txt", "r");
           s = text.read()
           self.assertEqual(get_updated_string_after_replacement(s,"","Hi"), "Error: Invalid input..")
           
       def test_3_When_both_the_input_words_are_same(self):
           text = open("input_word_replacement.txt", "r")
           s = text.read()
           self.assertEqual(get_updated_string_after_replacement(s,"Hello","Hello"), "Info: Input are same. No change..")
       
       #Positive Scenarios
       def test_4_When_both_the_input_words_are_same(self):
           text = open("input_replace_word_example.txt", "r")
           s = text.read()
           self.assertEqual(get_updated_string_after_replacement(s,"ab","Hi"), "Hi cd Hi")

       def test_5_When_both_the_input_words_are_same(self):
           text = open("input_replace_word_example.txt", "r")
           s = text.read()
           self.assertEqual(get_updated_string_after_replacement(s,"a","c"), "ab cd ab")    

if __name__ == '__main__':
    unittest.main()