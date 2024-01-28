import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import pickle
import requests

books_dict= pickle.load(open('popular.pkl','rb'))
books=pd.DataFrame(books_dict)
similar= pickle.load(open('similarity_score.pkl','rb'))

def fetch_poster(books_id):
    url= 'https://covers.openlibrary.org/b/id/'+str(books_id)+'-M.jpg' # url for the book covers
    try:
        data=requests.get(url) # getting the data from the url
        data.raise_for_status() # checking  for the status 
        data=data.json() # converting the data into json format
        poster_path=data['poster_path'] # getting the poster path
        def fetch_poster(books_id):
            url = 'https://covers.openlibrary.org/b/id/' + str(books_id) + '-M.jpg'  # url for the book covers
            try:
                data = requests.get(url)  # getting the data from the url
                data.raise_for_status()  # checking for the status
                data = data.json()  # converting the data.json format
                poster_path = data['poster_path']# getting the poster path
                full_path = 'https://covers.openlibrary.org' + poster_path  # get the full path for the book
                return full_path
            except requests.exceptions.HTTPError as err:
                print(f"HTTP Error: {err}")
            except requests.exceptions.RequestException as err:
                print(f"Request Exception: {err}")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")

def recommend(book):
    try:
      index=books[books['title']==book].index[0]
      distances=similar[index]# get the distances of the book
      books_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11] # getting the top 10 books.
      recommended_books=[]
      recommended_books_posters=[]
      for i in books_list:
          books_id=books.iloc[i][0].split('-')[1] # getting the books id
          recommended_books.append(books.iloc[i][0]) # getting the name of the book.
          poster_path=fetch_poster(books_id)
          if poster_path:
              recommended_books_posters.append(poster_path)

          return recommended_books,recommended_books_posters
      
    except:
         st.write("Sorry,the book which you are looking for is not present")


# Streamlit Layout 
st.title("Book Recommender System") 
option=st.selectbox("Select a book",books['Book-Title'].values) #

if st.button('Recommend'):
    if(option is not None):
        names,posters=recommend(option)
    else:
        st.write("Please select a book")

# Displaying the selected book information
    selected_book=books[books['Book-Title']==option].iloc[0]
    st.write(f"**Selected Book: {selected_book['Book-Title']} **" )
    column1,column2,column3,column4,column5,column6,column7,column8,column9,column10=st.columns(10)
    with column1:
        st.text(names[0])
        st.image(posters[0],use_column_width=True)
    with column2:
        st.text(names[1])
        st.image(posters[1],use_column_width=True)
    with column3:
        st.text(names[2])
        st.image(posters[2],use_column_width=True)
    with column4:
        st.text(names[3])
        st.image(posters[3],use_column_width=True)
    with column5:
        st.text(names[4])
        st.image(posters[4],use_column_width=True)
    with column6:
        st.text(names[5])
        st.image(posters[5],use_column_width=True)
    with column7:
        st.text(names[6])
        st.image(posters[6],use_column_width=True)
    with column8:
        st.text(names[7])
        st.image(posters[7],use_column_width=True)
    with column9:
        st.text(names[8])
        st.image(posters[8],use_column_width=True)
    with column10:
        st.text(names[9])
        st.image(posters[9],use_column_width=True)
    
    
            
