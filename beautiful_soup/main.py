from bs4 import BeautifulSoup
with open('html-code.html','r') as html_file:
    content =html_file.read()

soup =BeautifulSoup(content,'lxml')
tags =soup.find_all('p')

List_styles=soup.find_all('li')

for list in List_styles:
    list_name = list.text
    list_price = list.class('price').text

    print(list_name)
    print(list_price)
 


