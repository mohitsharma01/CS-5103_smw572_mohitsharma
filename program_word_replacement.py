"""
   FileName: program_word_replacement.py
   Author:   Mohit Sharma(smw572)
   Program:  Word replacement
             Replaces all the occurences of a given word in an input String with the new word 
"""
import re


def get_updated_string_after_replacement(input_String, word_to_be_replaced, new_word): 

    if len(input_String) == 0:
       print("The input string is empty")
       return("Error: Input String is Empty")
    elif len(word_to_be_replaced) == 0 or len(new_word) == 0:
       print("Invalid input..")
       return("Error: Invalid input..")
    elif (new_word == word_to_be_replaced):
       print("Nothing Changed!! Both the user inputs are SAME.")
       return "Info: Input are same. No change.."
          # Replace all the occurrences in the input string.
    else: 
       replaced   = re.sub(r'(?<!\S)' + re.escape(word_to_be_replaced) + r'(?!\S)', new_word, input_String)  
       with open('input_word_replacement.txt', 'w') as file:
          # Update the replacing word with new onein the file
          file.write(replaced)
          return replaced
          
          
          

def Driver():   
    text = open("input_word_replacement.txt", "r")     
    input_String = text.read()

    word_to_be_replaced = input("Enter the word/character you want to replace :")
    new_word = input("Enter the new word/character you want the old one to replace with :")

    replacedContent = get_updated_string_after_replacement(input_String, word_to_be_replaced, new_word)

    if("Error:" not in replacedContent):
       print("updated content: ", replacedContent)
    
if __name__=="__main__": 
   Driver()          # call Driver() function