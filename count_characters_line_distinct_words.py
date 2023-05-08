"""
 unique word count Program: This program counts the frequency of each unique word. Input string is passed in program for testing through a text file.
"""
import re

def get_unique_words_frequency(input_string): 

   # First convert the input into a list of words
   input_string_list = input_string.strip().split()
   unique_strings_list = [] 

   # iterate through the list of input words to find the unique words 
   for str in input_string_list:         

      # check for duplicate strigns 
      if str not in unique_strings_list: 

         # if a unique word then add it to the unique_string_list list
         unique_strings_list.append(str) 

   print("unique strings => => \n")
   print("---------------------------------------------------------------")
   print(unique_strings_list)  
   print("---------------------------------------------------------------\n")
   for i in range(0, len(unique_strings_list)): 

      # compute the frequency of each unique word in the input 
      print('Word Frequency [{}]: {}'.format(unique_strings_list[i], input_string_list.count(unique_strings_list[i])))
    
   print("*******************")

def getUniqueWords(fileName):
   file = open(fileName, "r")
   input_string = file.read()
    
   get_unique_words_frequency(input_string)
   file.close()

def getNumberOfLines(fileName):
   file = open(fileName, "r")
   num_lines= len(file.readlines())

   file.close()

   file = open(fileName, "r")
   data = file.read()
   totalCharacters = len(data)

   # handle the scenario when there is just one word is there in the file but no new line character
   if num_lines == 0 and totalCharacters != 0:
      num_lines = 1
  
   print("The number of lines in the input file is:  ", num_lines)
   print("*****************************************\n")
   file.close()
   return num_lines

def getNumberOfCharacters(fileName):
   file = open(fileName, "r")
   data = file.read()
   totalCharacters = len(data)

   print("\n The total number of characters in the input file including spaces is:  ", totalCharacters) 
   print("************************************************************************\n")
   file.close()
   return totalCharacters      

if __name__=="__main__": 
   fileName= "input_example.txt"
   getUniqueWords(fileName)          # call findUniqueWords() function
   getNumberOfLines(fileName)          # call findNumberOfLines() function
   getNumberOfCharacters(fileName)     # call getNumberOfCharacters() function
