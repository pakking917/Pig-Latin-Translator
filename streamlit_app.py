import streamlit as st

st.title("🎈 Pig Latin Translator")

def is_vowel(letter):
    '''Checks if each letter is a vowel'''
    # Determine if letter is vowel or not and returns True or False
    return letter.lower() in 'aeiouy'

def translate_word(word):
    '''Translate a single English word into Pig Latin'''
    # Returns the string if it is not entirely constructed of alphabets
    if word.isalpha() != True:
        return word
    
    # Checks if word is capitalized then lowercase the entire word
    if_capitalized = word[0].isupper()
    word = word.lower()
    
    # Checks if word starts with a vowel and return latin word if it is
    if is_vowel(word[0]):  
        latin_word = word + "yay"
        
    # Translate word if it is does not start with vowel
    else:
        for index in range(len(word)):
            if is_vowel(word[index]):
                prefix = word[:index]
                stem = word[index:]
                latin_word = stem + prefix + "ay"
                break
            
            # Added condition if there are no vowels in the word
            latin_word = word + "ay"
    
    #Capitalize if necessary
    if if_capitalized:
        latin_word = latin_word.capitalize()
    
    return latin_word
    
def translate_text(text):
    '''Translate the entire text'''
    # Sets up intial variables for accumulator
    latin_text = ''
    word_length = 0
    start_index = 0
    
    for index in range(len(text)):
        
        # Detects if a word has ended
        if text[index] in " .,?!":
            # If statement prevents cases of consecutive punctuation
            if word_length > 0:
                latin_text += translate_word(text[start_index:start_index + word_length])
            # Adds the punctuation and sets up for the next word
            latin_text += text[index]
            word_length = 0
            start_index = index + 1
        
        # Tell program how long the individual word is 
        else:
            word_length += 1
    
    # translate the last word in case text does not end with a punctuation
    if word_length > 0:
        latin_text += translate_word(text[start_index:start_index + word_length])
            
    return latin_text            

sentence = st.text_input("Text: ")
st.write(translate_text(sentence))
