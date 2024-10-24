########## Longest Word ##########
##### by Ludiah Bagakas #####

# define function

def longest_word(sentence): 

  

    # define words 

    words = sentence.split() 

     

    # define the longest word as maximum character length 

    # note: this function automatically outputs the first occurring longest word 

    lw = max(words, key = len) 

     

    return lw 

       

# test function 

    # test 1 

sentence1 = "some line with text"

longest1 = longest_word(sentence1) 

print(longest1)

    # test 2

sentence2 = "another line" 

longest2 = longest_word(sentence2) 

print(longest2)
