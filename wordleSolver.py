#Wordle Solver

word_list = []
green_letters = []

def list_up():
    words = open("fiveLetterWords.txt", "r")
    for word in words:
        word_list.append(word[:5])
    words.close()

def get_stats():
    stats_dict = {}
    for word in word_list:
        for letter in word:
            if(letter in stats_dict.keys()):
                stats_dict[letter]+= 1.0
            else:
                stats_dict[letter] = 1.0
    count = len(word_list)*5
    for key in stats_dict.keys():
        stats_dict[key] = stats_dict[key]/count # normalize values
    return stats_dict

def get_prob(stats_dict):
    prob_list = []
    for word in word_list:
        prob = 0
        if(len(set(word)) == len(word)):
            prob = 0.5
        for letter in word:
            if (letter in ['a', 'e', 'i', 'o', 'u']):
                prob+= 0.2
            prob += stats_dict[letter]
        prob_list.append((prob, word))
    return prob_list

def eliminate_words(letter, colour, location, prob_list):
    #print("LETTER: ", letter, "STATUS: ", colour)
    elimination_words = [] #fill up with unqualifying words
    if (colour == 'G'):
        green_letters.append(letter)
        for i in range(len(prob_list)):
            word = prob_list[i][1]
            if (word[location] != letter):
                elimination_words.append(word)
    if (colour == '?'):
        for i in range(len(prob_list)):
            word = prob_list[i][1]
            if (letter in word and letter not in green_letters):
                elimination_words.append(word)
    
    if (colour == 'Y'):
        for i in range(len(prob_list)):
            word = prob_list[i][1]
            if(word[location] == letter):
                elimination_words.append(word)
            if(letter not in word):
                elimination_words.append(word)

    #remove the words from the list
    for word in elimination_words:
        for w in prob_list:
            if (w[1] == word):
                prob_list.remove(w)
                break
    return prob_list
        
def format_prob(prob_list):
    for word in prob_list:
        print(word[1], ": ", "{:.2f}".format(word[0]))

def play(prob_list):
    current_list = prob_list
    while(1):
        guessed_word = input("What word did you guess   : ")
        response_seq = input("Enter response after guess: ")
        if(len(guessed_word) != 5 or len(response_seq)!=5):
            print("Invalid Input")
            continue
        for i in range(5):
            current_list = eliminate_words(guessed_word[i], response_seq[i], i, current_list)
        format_prob(current_list)
        

if __name__ == "__main__":
    list_up() # create word list
    stats_dict = get_stats() # frequency of every letter
    prob_list = get_prob(stats_dict)
    prob_list.sort(reverse=1)
    play(prob_list)
    '''print(prob_list[:10])
    print(len(prob_list))
    prob_list = eliminate_words('g', 'G', 2, prob_list)
    print(prob_list[:10])
    print(len(prob_list))
    prob_list = eliminate_words('a', '?', 2, prob_list)
    print(prob_list[:10])
    print(len(prob_list))
    prob_list = eliminate_words('e', '?', 2, prob_list)
    format_prob(prob_list)
    print(len(prob_list))
    prob_list = eliminate_words('y', 'Y', 4, prob_list)
    format_prob(prob_list)
    print(len(prob_list))'''
    
