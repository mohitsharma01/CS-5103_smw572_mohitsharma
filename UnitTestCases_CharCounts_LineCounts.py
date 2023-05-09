"""
   FileName: UnitTestCases_CharCounts_LineCounts.py
   Author:   Mohit Sharma(smw572)
   Program:  Unit test cases for the getNumberOfCharacters and getNumberOfLines Methods written as part of the Phase 2 (First requirement Changes)

"""
from program_count_characters_line_distinct_words import getNumberOfCharacters, getNumberOfLines
   # The code to test
import unittest   # The test framework
text = open("input_multiple_lines.txt", "r")

class Test_CharCount_LineCount(unittest.TestCase): 
       pass      
       def test_1_Empty_String_test_should_count_zero_char_zero_lines(self):
           self.assertEqual(getNumberOfCharacters("input_emptyString.txt"), 0)
           self.assertEqual(getNumberOfLines("input_emptyString.txt"), 0)

       def test_2_when_String_has_only_tabs_and_spaces(self):
           self.assertEqual(getNumberOfCharacters("input_only_tabs_and_spaces.txt"), 21)
           self.assertEqual(getNumberOfLines("input_only_tabs_and_spaces.txt"), 1) 
       
       def test_3_when_String_has_only_one_period(self):
           self.assertEqual(getNumberOfCharacters("input_only_period.txt"), 1)
           self.assertEqual(getNumberOfLines("input_only_period.txt"), 1) 

       def test_4_when_String_has_alphanumeric_and_special_chars_also(self):
           self.assertEqual(getNumberOfCharacters("input_special_and_alphanumeric.txt"), 24)
           self.assertEqual(getNumberOfLines("input_special_and_alphanumeric.txt"), 4)     

       def test_5_only_new_line_char_in_file(self):
           self.assertEqual(getNumberOfCharacters("input_only_new_line_char.txt"), 1)
           self.assertEqual(getNumberOfLines("input_only_new_line_char.txt"), 1)

       def test_6_when_String_has_multiple_tabs_and_spaces(self):
           self.assertEqual(getNumberOfCharacters("input_multiple_spaces_and_tabs_between_Words.txt"), 47)
           self.assertEqual(getNumberOfLines("input_multiple_spaces_and_tabs_between_Words.txt"), 1)

       def test_7_multiple_lines_are_in_file(self):
           self.assertEqual(getNumberOfCharacters("input_multiple_lines.txt"), 869)
           self.assertEqual(getNumberOfLines("input_multiple_lines.txt"), 16) 

       def test_8_when_size_of_input_file_is_high(self):
           self.assertEqual(getNumberOfCharacters("input_large_size_file.txt"), 79948)
           self.assertEqual(getNumberOfLines("input_large_size_file.txt"), 1381)     

       def test_9_When_there_is_just_one_word_without_a_new_line(self):
           self.assertEqual(getNumberOfCharacters("input_oneWord.txt"), 5)
           self.assertEqual(getNumberOfLines("input_oneWord.txt"), 1)

       def test_10_when_leading_spaces_are_there_in_the_string(self):
           self.assertEqual(getNumberOfCharacters("input_leading_spaces_tabs.txt"), 38)
           self.assertEqual(getNumberOfLines("input_leading_spaces_tabs.txt"), 2)  


if __name__ == '__main__':
    unittest.main()
