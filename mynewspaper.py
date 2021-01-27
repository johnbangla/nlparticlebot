from newspaper import Article

import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')
nltk.download('punkt', quiet = True)
article = Article('https://www.webmd.com/depression/guide/chronic-depression-dysthymia#1')
article.download()
article.parse()
article.nlp()
corpus = article.text
#Tokenize
text = corpus
sentence_list = nltk.sent_tokenize(text)
# print(sentence_tokenize)


#Greeting Function

def greeting_response(text):
    text = text.lower()
    bot_response = ['HI MAN','Hello Sir','Dear Mam','Please speak']
    user_response = ['Whats up','hi','hello','are you ','anybody']
    
    for word in text.split():
        if word in user_response:
            return random.choice(bot_response)
        
#shorting function


def index_short(list_var):
    
    length = len(list_var)
    list_index = list(range(0,length))
    x =  list_var
    
    
    for i in range(length):
        for j in range(length):
            if x[list_index[i]]  >  x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index

#The AI will talk                   
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_short(similarity_scores_list)
    index= index[1:]
    response_flag = 0
    j = 0
    
    for i in range(len(index)):
        if similarity_scores_list[index[i]] >  0.0:
            bot_response = bot_response + '' + sentence_list[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break
    if response_flag == 0 :
        bot_response = bot_response + 'sorry'
    sentence_list.remove(user_input)
    return bot_response

exit_list = ['bue','Good bye','Tired']


#program start
while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Talk to you later')
        break 
    else:
        if greeting_response(user_input) != None:
            print('I am a virtual Doctor')
        else:
           print(bot_response(user_input))
        
                
            
    
    
    
            


    