from wordReq import get_unique_words_frequency
   # The code to test
import unittest   # The test framework
text = open("example.txt", "r")

        

class Test_wordcount(unittest.TestCase): 
       pass      
       def test_Empty_String(self):
           s = ""
           self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))

       def test_Single_Word_String(self):
           s = "Hello Hello"
           self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))

       def test_Unique_Word_String(self):
           s = text.read()
           self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))

       def test_Large_String_Size(self):
        s = text.read()
        self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))

       def test_Special_Characters_In_String(self):
        s = text.read()
        self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))

       def test_Alphanumeric_Characters_In_String(self):
        s = text.read()
        self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))


if __name__ == '__main__':
    unittest.main()
   
