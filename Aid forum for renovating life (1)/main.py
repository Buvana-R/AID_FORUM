from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from signup import *
from login import *
from add import *
from view import *
from request import*

# Add your own database name and password here to reflect in the code
mypass = "Suthan"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Aid Forum for Renovating life")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=1.33

# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to\n Aid Forum for renovating life", bg='black', fg='white', font=('Courier',12))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Signup",bg='black', fg='white', command=register)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Login",bg='black', fg='white', command=login)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="Add",bg='black', fg='white', command=addProduct)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="View",bg='black', fg='white', command=View)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Request",bg='black', fg='white', command=request)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0,rely=0.89,relwidth=1,relheight=0.16)


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

#Machine Learning
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



headingLabel = Label(headingFrame1, text="People requested for\n"+str(abc), bg='black', fg='white', font=('Courier',12))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

root.mainloop()



