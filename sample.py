import requests
from bs4 import BeautifulSoup, NavigableString, Tag

def birth(link):
    response = requests.get(
        url=link)

    soup = BeautifulSoup(response.content, 'html.parser')
    birthdate = '-'
    birthplace = '-'
    try:
        info_box = soup.find('table',{'class':'infobox'})
        table_row_list = info_box.findAll('tr')
    except TypeError or AttributeError :
        return(birthdate, birthplace)

    for tr in table_row_list:
        try:
            if ((tr.th.text).strip() == 'பிறப்பு'):
                if tr.td.findAll('span',{'class':'bday'}):
                    birthdate = tr.td.find('span',{'class':'bday'}).text
                if  tr.td.findAll('span',{'class':'birthplace'}):
                    birthplace = tr.td.find('span',{'class':'birthplace'}).text
                else:
                    try:
                        string_br= str(tr.td)
                        if '<br/>' in string_br:
                            splitted_with_break = string_br.split('<br/>')
                            birthplace = (BeautifulSoup(splitted_with_break[-1],"html.parser").text.strip())
                    except AttributeError:
                        continue
        except AttributeError or TypeError:
            continue
    return (birthdate, birthplace)


    # if ((tr.th.text == 'பிறப்பு')):
    #     print(tr.td.text)

(birthdate, birthplace) = birth('https://ta.wikipedia.org/wiki/%E0%AE%85%E0%AE%AE%E0%AE%B2%E0%AE%BE_(%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88)')
print (birthdate)
print(birthplace)
# print (birthdate)
# print (birthplace)