import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import pickle
import requests
import json 


def recommend(book_name):
    if book_name not in pivot.index: # Checking if the book is in the list
        return None
    else:
        book_id=pivot.index.get_loc(book_name) # Getting the index of the book
        similar_books=list(enumerate(similar[book_id])) # Getting the list of books with their similarity score
        similar_books=sorted(similar_books,key=lambda x:x[1],reverse=True) # Sorting the book_list in descending order of similarity score
        similar_books=similar_books[1:6] # Selecting the top 5 books
        data=[]
        for i in similar_books:
            item=[]
            df=books[books['Book-Title']==pivot.index[i[0]]]
            item.extend(list(df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)
        return data    
st.title("Book Recommender System")

popular=pickle.load(open('popular.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
books=pd.DataFrame(books)
similar=pickle.load(open('similarity_score.pkl','rb'))
pivot=pickle.load(open('pivot_t.pkl','rb'))



book_list=pivot.index.values
image_url=popular["Image-URL-M"].tolist()
book_title=popular['Book-Title'].tolist()
book_author=popular['Book-Author'].tolist()
total_ratings=popular['Number-of-Ratings'].tolist()
avg_ratings=popular['Average-Ratings'].tolist()

st.sidebar.title("Top 20 Books")
if st.sidebar.button("SHOW"):
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[0])
        st.text(book_author[0])
        st.text("Ratings:" + str(total_ratings[0]))
        st.text("Avg.Rating:" + str(round(avg_ratings[0],2)))
    with col2:
        st.image(image_url[1])
        st.text(book_author[1])
        st.text("Ratings:" + str(total_ratings[1]))
        st.text("Avg.Rating:" + str(round(avg_ratings[1],2)))
    with col3:
        st.image(image_url[2])
        st.text(book_author[2])
        st.text("Ratings:" + str(total_ratings[2]))
        st.text("Avg.Rating:" + str(round(avg_ratings[2],2)))
    with col4:
        st.image(image_url[3])
        st.text(book_author[3])
        st.text("Ratings:" + str(total_ratings[3]))
        st.text("Avg.Rating:" + str(round(avg_ratings[3],2)))
    with col5:
        st.image(image_url[4])
        st.text(book_author[4])
        st.text("Ratings:" + str(total_ratings[4]))
        st.text("Avg.Rating:" + str(round(avg_ratings[4],2)))
        
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[5])
        st.text(book_author[5])
        st.text("Ratings:" + str(total_ratings[5]))
        st.text("Avg.Rating:" + str(round(avg_ratings[5],2)))
    with col2:
        st.image(image_url[6])
        st.text(book_author[6])
        st.text("Ratings:" + str(total_ratings[6]))
        st.text("Avg.Rating:" + str(round(avg_ratings[6],2)))
    with col3:
        st.image(image_url[7])
        st.text(book_author[7])
        st.text("Ratings:" + str(total_ratings[7]))
        st.text("Avg.Rating:" + str(round(avg_ratings[7],2)))
    with col4:
        st.image(image_url[8])
        st.text(book_author[8])
        st.text("Ratings:" + str(total_ratings[8]))
        st.text("Avg.Rating:" + str(round(avg_ratings[8],2)))
    with col5:
        st.image(image_url[9])
        st.text(book_author[9])
        st.text("Ratings:" + str(total_ratings[9]))
        st.text("Avg.Rating:" + str(round(avg_ratings[9],2)))

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[10])
        st.text(book_author[10])
        st.text("Ratings:" + str(total_ratings[10]))
        st.text("Avg.Rating:" + str(round(avg_ratings[10],2)))
    with col2:
        st.image(image_url[11])
        st.text(book_author[11])
        st.text("Ratings:" + str(total_ratings[11]))
        st.text("Avg.Rating:" + str(round(avg_ratings[11],2)))
    with col3:
        st.image(image_url[12])
        st.text(book_author[12])
        st.text("Ratings:" + str(total_ratings[12]))
        st.text("Avg.Rating:" + str(round(avg_ratings[12],2)))
    with col4:
        st.image(image_url[13])
        st.text(book_author[13])
        st.text("Ratings:" + str(total_ratings[13]))
        st.text("Avg.Rating:" + str(round(avg_ratings[13],2)))
    with col5:
        st.image(image_url[14])
        st.text(book_author[14])
        st.text("Ratings:" + str(total_ratings[14]))
        st.text("Avg.Rating:" + str(round(avg_ratings[14],2)))  
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(image_url[15])
        st.text(book_author[15])
        st.text("Ratings:" + str(total_ratings[15]))
        st.text("Avg.Rating:" + str(round(avg_ratings[15],2)))
    with col2:
        st.image(image_url[16])
        st.text(book_author[16])
        st.text("Ratings:" + str(total_ratings[16]))
        st.text("Avg.Rating:" + str(round(avg_ratings[16],2)))
    with col3:
        st.image(image_url[17])
        st.text(book_author[17])
        st.text("Ratings:" + str(total_ratings[17]))
        st.text("Avg.Rating:" + str(round(avg_ratings[17],2)))
    with col4:
        st.image(image_url[18])
        st.text(book_author[18])
        st.text("Ratings:" + str(total_ratings[18]))
        st.text("Avg.Rating:" + str(round(avg_ratings[18],2)))
    with col5:
        st.image(image_url[19])
        st.text(book_author[19])
        st.text("Ratings:" + str(total_ratings[19]))
        st.text("Avg.Rating:" + str(round(avg_ratings[19],2))) 

st.sidebar.title("Recommend Books")
selected_book = st.sidebar.selectbox("Type or select a book from the dropdown", book_list)

if st.sidebar.button("Recommend Me"):
    moviee = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(moviee[0][2])
        st.text(moviee[0][0])
        st.text(moviee[0][1])  
    with col2:
        st.image(moviee[1][2])
        st.text(moviee[1][0])
        st.text(moviee[1][1])
    with col3:
        st.image(moviee[2][2])
        st.text(moviee[2][0])
        st.text(moviee[2][1])
    with col4:
        st.image(moviee[3][2])
        st.text(moviee[3][0])
        st.text(moviee[3][1])
    with col5:
        st.image(moviee[4][2])
        st.text(moviee[4][0])
        st.text(moviee[4][1])