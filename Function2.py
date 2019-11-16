def getGuessedWord(secretWord, lettersGuessed):

   word = ""
   for i in secretWord:
        if i in lettersGuessed:
            word+= i
        else:
            word += "_"
   return word
