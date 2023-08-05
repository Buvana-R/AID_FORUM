#doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
#doc2 = "My father spends a lot of time driving my sister around to dance practice."
#doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
#doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
#doc5 = "Health experts say that Sugar is not good for your lifestyle."
with open("myfile.txt") as f:
    file_content = f.readlines()
doc_complete = list(file_content)

import nltk
from tkinter import *
# from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
# from request import *

#mypass = "root"
#mydatabase="db"
#con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
#cur = con.cursor()
#doc_complete="select item from request"
#cur.execute(doc_complete)
#con.commit()
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]     


# Importing Gensim
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]




# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

abc=ldamodel.print_topics(num_topics=3, num_words=3)
print(abc)
