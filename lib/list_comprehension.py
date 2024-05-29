#!/usr/bin/env python3
def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers


input_list = [1, 3, 5, 7, 8, 9,10,11,12,13,14,15]
result = return_evens(input_list)
print(result)  

def make_exclamation(sentences):
    exclamation_sentences = [sentence + "!" for sentence in sentences]
    return exclamation_sentences

input_sentences = ["Hello", "I'm doing great", "Python is fun"]
result = make_exclamation(input_sentences)
print(result)