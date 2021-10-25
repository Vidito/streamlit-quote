from bs4 import BeautifulSoup
import streamlit as st
import requests

col1,col2 = st.columns([6,1])
with col1:
    topic = st.selectbox('',['Adversity', 'Beauty', 'Beer','Christmas','Coffee','Dreams','Education','God', 'Good-Life'])
with col2:
    st.write('          ')
    st.write('          ')
    btn = st.button('Search')
if btn:
    re = requests.get(f'https://quoterati.com/topics/{topic.lower()}')
    soup = BeautifulSoup(re.content, 'html.parser')

    lists = soup.find('ul', class_="page-section__list")
    lis = lists.find_all('li', class_='quote')
    num = 0
    for i in lis:
        quote = i.find('blockquote', class_="quote__text").text
        author = i.find('a', class_="quote__link").text
        num+=1
        st.markdown(f'''<div class='q' style='color:#2B393C; background-color:#F4F4F1; padding:60px; margin:10px; border-radius:8px; text-align:center; line-height:2;'> <span style='border:1px solid #2B393C; padding:10px;'  > {num}</span> <br> <p style='margin:20px; font-size:30px'  >{quote} </p>
        <span style='color:#E16927'> {author} </span> </div>
        ''', unsafe_allow_html=True)
        # st.caption(author)

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# local_css('style.css')
