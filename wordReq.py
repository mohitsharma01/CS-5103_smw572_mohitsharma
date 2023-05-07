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

def findUniqueWords():
    text = open("example.txt", "r")
    input_string = text.read()
    """ python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yespython csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes python csharp javascript php python javascript csharp python csharp php\tmahi\nmahi please test c,c \
      yes"""
    print(input_string) 
    get_unique_words_frequency(input_string)                

if __name__=="__main__": 
   findUniqueWords()          # call findUniqueWords() function
