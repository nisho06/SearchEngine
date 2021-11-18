import requests
from bs4 import BeautifulSoup

def paragraph(soup_new):
    para1 = '-'
    para2 = '-'

    try:
        parser_contents = soup_new.find('div',{"class":"mw-parser-output"}).contents
        for i in parser_contents:
            if i.name == 'p':
                if para1 == '-':
                    para1 = i.text.strip()
                    continue
                if para2 == '-':
                    para2 = i.text.strip()
                    break
        # for para_index in range(len(list_para)):
        #     if para_index == 0:
        #         para1 = list_para[para_index].text.strip()
        #     else:
        #         para_last+=(list_para[para_index].text.strip()+ str('\n'))
        # para2 = para_last
        return (para1, para2)

    except AttributeError:
        return (para1, para2)

def birth(soup_new):
    birthdate = '-'
    birthplace = '-'
    try:
        info_box = soup_new.find('table',{'class':'infobox'})
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
                            if birthplace == '':
                                birthplace = '-'
                    except AttributeError:
                        continue
        except AttributeError or TypeError:
            continue
    return (birthdate, birthplace)


    # if ((tr.th.text == 'பிறப்பு')):
    #     print(tr.td.text)

link_final = 'https://ta.wikipedia.org/wiki/%E0%AE%9C%E0%AF%86._%E0%AE%9C%E0%AF%86%E0%AE%AF%E0%AE%B2%E0%AE%B2%E0%AE%BF%E0%AE%A4%E0%AE%BE'

response_new = requests.get(
    url=link_final)

soup_new = BeautifulSoup(response_new.content, 'html.parser')


(para1, para2) = paragraph(soup_new)

print(para1)
print (para2)

# print (birthdate)
# print (birthplace)