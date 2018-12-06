from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

print("*"*50)
#
text="the touch is not bad. the product is not a bad. i love this mobile fisrt. the product is awesome. it is easy to use. cost is too high to buy. camera is not good. comparing with other the quality is very bad. bad mobile. not good to say."
print("*"*50)
text=input("Enter the review here: ")
print("*"*50)
positive=['good','happy','love','awesome']
negative=['sad','bad','not','sad','no','wont']

"""
for line in text:
    sentence = line.split('.')
    for word in sentence:
        li=list(word.split(' '))
        #print(li)
"""    
#remove punctuations

punc='''.,!#@'''
no_punc=""
for char in text:
    if char not in punc:
        no_punc+=char
#print(no_punc)

#remove stopwords
#stop_words=set(stopwords.words('english'))
word_tokens=word_tokenize(no_punc)

stop_words={'on','a','the','is','was','i','it','to','with','other','this'}

filtered_sentence=[]

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


#filtered_sentence=list(no_punc.split(' '))
#print(filtered_sentence)

''' Calculating without Negation words '''

pos_count, neg_count, neutral_count=0,0,0
for i in range(len(filtered_sentence)):
    for j in range(len(positive)):
        if (filtered_sentence[i]==positive[j]):
                pos_count +=1
                #print("Positive Word:", filtered_sentence[i])
    for k in range(len(negative)):
        if (filtered_sentence[i]==negative[k]):
                neg_count+=-1
                print("Negative Word:", filtered_sentence[i])
                break
            #else:
             #   neutral_count+=neutral_count
                
total_score = pos_count+neg_count           
print("Positive Count: ", +pos_count)
print("Negative Count: ", +neg_count)
print("Total Setiment Score without calculating Negated word: ", +total_score)
print("*"*75)

#print(stop_words)

if total_score>0:
    print("The content is Positive")
elif total_score<0:
    print("The content is Negative")
else:
    print("The content is Neutral")
print("*"*75)

''' Claculating with Negation words '''

score,nscore=0,0
negation_words=['not','never','ever','didnt','no','wont']
pos_count,neg_count,negated_word,nnegated_word=0,0,0,0
for i in range(len(filtered_sentence)):
    for j in range(len(positive)):
        for k in range(len(negation_words)):
            if(filtered_sentence[i]==negation_words[k]) and (filtered_sentence[i+1]==positive[j]):
                #print(negation_words[k])
                #print(filtered_sentence[i]+'_'+filtered_sentence[i+1])
                score=1*-1
                negated_word+=1
    for l in range(len(negative)):
        for m in range(len(negation_words)):
            if(filtered_sentence[i]==negation_words[m]) and (filtered_sentence[i+1]==negative[l]):
                #print(negation_words[m])
                print(filtered_sentence[i]+'_'+filtered_sentence[i+1])
                nscore=1
                nnegated_word+=1
                #break
        #break
            
print(filtered_sentence)
print("Total number of Negated words: ", negated_word)
print("The Total Score of Positive word with Negated_word is: ", score*negated_word)
print('\n')
print("Total number of Negative word with Negated words: ", nnegated_word)
print("The Total Score of Negative word with Negated_word is: ", nscore*nnegated_word)
print('\n')
print("The Total Sentiment Score with Negation words only: ", (score*negated_word)+(nscore*nnegated_word))
print("*"*75)
neg_total_score=(score*negated_word)+(nscore*nnegated_word)
if neg_total_score>0:
    print("The content is Positive")
elif neg_total_score<0:
    print("The content is Negative")
else:
    print("The content is Neutral")
print("*"*75)    
    
