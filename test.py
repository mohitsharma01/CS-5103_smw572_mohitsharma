from wordReq import get_unique_words_frequency
   # The code to test
import unittest   # The test framework
text = open("example.txt", "r")
input_string = text.read()
print(input_string)
        

class Test_wordcount(unittest.TestCase): 
       pass      
       def test_one_word(self):
           s = "hello"
           self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))
           
       def test_emptystring(self):
           text = open("example.txt", "r")
           s = text.read()
           self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))
           
       def test_string(self):
           s = "hello"
           self.assertEqual(get_unique_words_frequency(s), get_unique_words_frequency(s))
        
    

if __name__ == '__main__':
    unittest.main()
   