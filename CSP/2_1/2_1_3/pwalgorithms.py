# Module pwalgorithms

#how do i add "\" bro o_O
symbols = ["~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|",":","<",">"]

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_words(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
    #second word
    for o in words:
      guesses += 1
      if (w+o == password):
        return True, guesses
  return False, guesses

def two_words_and_digit(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
    #add number out of 9 to beginning, 1 word
    for i in range(9):
      guesses += 1
      if (str(i)+w == password):
        return True, guesses
      
    #second word
    for o in words:
      guesses += 1
      if (w+o == password):
        return True, guesses
      #try word + digit + secondword
      for i in range(9):
        guesses += 1
        if(w+str(i)+o == password):
          return True, guesses
      #try word + secondword + digit
      for i in range(9):
        guesses += 1
        if(w+o+str(i) == password):
          return True, guesses
  return False, guesses

def two_words_and_digit_and_symbol(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
    
    #add number out of 9 to beginning, 1 word
    for i in range(9):
      guesses += 1
      if (str(i)+w == password):
        return True, guesses
      
      #attempt symbols
      for a in symbols:
        guesses += 1 
        if(str(i)+w+a == password):
          return True, guesses
      
    #second word
    for o in words:
      guesses += 1
      if (w+o == password):
        return True, guesses
      
      #try word + digit + secondword
      for i in range(9):
        guesses += 1
        if(w+str(i)+o == password):
          return True, guesses
        
      #try word + secondword + digit
      for i in range(9):
        guesses += 1
        if(w+o+str(i) == password):
          return True, guesses

        #attempt symbols
        for a in symbols:
          guesses += 1 
          if(w+o+str(i)+a == password):
            return True, guesses
  return False, guesses


def three_words_and_digit_and_symbol(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
    
    #add number out of 9 to beginning, 1 word
    for i in range(9):
      guesses += 1
      if (str(i)+w == password):
        return True, guesses
      
      #attempt symbols
      for a in symbols:
        guesses += 1 
        if(str(i)+w+a == password):
          return True, guesses
      
    #second word
    for o in words:
      guesses += 1
      if (w+o == password):
        return True, guesses
      
      #try word + digit + secondword
      for i in range(9):
        guesses += 1
        if(w+str(i)+o == password):
          return True, guesses
        
      #try word + secondword + digit
      for i in range(9):
        guesses += 1
        if(w+o+str(i) == password):
          return True, guesses

    # third word
    for r in words:
        guesses += 1
        if(w+o+r == password):
          return True, guesses
        
        #guess numbers
        for i in range(9):
          guesses += 1

        #attempt symbols
          for a in symbols:
            guesses += 1 
            if(w+o+r+str(i)+a == password):
              return True, guesses
  return False, guesses
