import nltk
import random
#nltk.download()
from nltk.corpus import words

#this is a function that opens files
def open_file(filename):
	f = open(filename, "r")
	sample = f.readlines()
	output = []
	for line in sample:
		line_words = []
		for word in line.split():
			line_words.append(word.lower())
		output.append(line_words)
	return (output)

#this is a function that writes files
def write_file(filename, data):
	new_file = open(filename, "w")
	for sentence in data:
		for word in sentence:
			new_file.write(word + " ")
		new_file.write("\n")
	new_file.close()

def encrypt_character(character, shift):
  cipher_char = ord(character) + shift
  if cipher_char > ord("z"):
    cipher_char -= 26
  return chr(cipher_char)

def encrypt_word(word, shift):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  cipher_word = ""
  for letter in word:
    if letter in letters:
      cipher_word += encrypt_character(letter, shift)
    else:
      cipher_word += letter
  return cipher_word

def encrypt_message(message, shift):
  cipher_message =[]
  for line in message:
    cipher_line = []
    for word in line:
      cipher_line.append(encrypt_word(word, shift))
    cipher_message.append(cipher_line)
  return cipher_message

def decrypt_character(character, shift):
  plain_char = ord(character) - shift
  if plain_char < ord("a"):
    plain_char += 26
  return chr(plain_char)

def decrypt_word(word, shift):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  plain_word = ""
  for letter in word:
    if letter in letters:
      plain_word += decrypt_character(letter, shift)
    else:
      plain_word += letter
  return plain_word

def decrypt_message(message, shift):
  plain_message =[]
  for line in message:
    plain_line = []
    for word in line:
      plain_line.append(decrypt_word(word, shift))
    plain_message.append(plain_line)
  return plain_message
  
#######################################################
#purpose of this function is to print all of the decrypted messages
def print_all_messages(encoded_message):
  #displays all possible decodings of messages using every possible key, 1-25.
  #print the shift and the decrypted message
  for shift in range(1,26):
    print(shift, '|', decrypt_message(encoded_message, shift))
  

def crack_cipher(encoded_message):
  #dictionary
  word_list = words.words()
  #create a variable to track the best count so far
  count = 0
  #create a variable to track the key with the best count
  bestKeyCount = 0
  #keep track of the key with the best count
  best_key = 0 
  #prints the decoded message using the best key
  print(decrypt_message, bestKeyCount) 
  #for loop to generate every possible Key
  for shift in range(1,26):
    counter = 0 #initialize counter to 0
    sample = decrypt_message(encoded_message, shift)
    #for each decrypted message check each word in the message to see if its in word_list,
    for line in sample:
      for word in line:
        # if it is increment a counter
        if word in word_list:
          counter += 1
    #once the loop is finished check the count if its greater than the max count so far reset the max count to this count and reset the key to this key
    if counter > bestKeyCount:
      bestKeyCount = counter
      #save the key here!
      best_key = shift
        
  #return the best key
  return best_key

#############################################
#TESTING CODE HERE 

#set shift to random number
plain_text = open_file('caesar1.txt')
encoded_message = encrypt_message(plain_text, random.randint(1, 25))

#want to print all the possible decrypted messages
print_all_messages(encoded_message)

#assign the bestKeyCount to the variable key
key = crack_cipher(encoded_message)

#we want to print the decrypted message using the best key we could find
#and this will be our result/final goal
print(decrypt_message(encoded_message, key))



