import requests
from bs4 import BeautifulSoup
import csv

from sample import birth, paragraph

response = requests.get(
    url="https://ta.wikipedia.org/wiki/%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D%E0%AE%A4%E0%AF%8D_%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AF%88%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%9F_%E0%AE%A8%E0%AE%9F%E0%AE%BF%E0%AE%95%E0%AF%88%E0%AE%95%E0%AE%B3%E0%AE%BF%E0%AE%A9%E0%AF%8D_%E0%AE%AA%E0%AE%9F%E0%AF%8D%E0%AE%9F%E0%AE%BF%E0%AE%AF%E0%AE%B2%E0%AF%8D")

soup = BeautifulSoup(response.content, 'html.parser')

csv_columns = ['இலக்கம்','பெயர்','அறிமுக வருடம்','அறிமுக படம்','பிறந்த திகதி','பிறந்த வருடம்','அறிமுகம்','உள்ளடக்கம்']

heroines = soup.findAll('tr')
heroines = heroines[1:]
links = []
dict_data= []

number = 1
for row in heroines :
    dict = {}
    dict[csv_columns[0]] = number
    if (row.td.find('a',{"class": "new"}) != None):
        continue
    data_row = row.findAll('td')
    dict[csv_columns[1]]=data_row[0].a.text

    link = data_row[0].a['href']
    link_final = f'https://ta.wikipedia.org/{link}'

    response_new = requests.get(
        url=link_final)

    soup_new = BeautifulSoup(response_new.content, 'html.parser')

    try:
        bday,birthplace = birth(soup_new)
        para1,para2 = paragraph(soup_new)

    except AttributeError or TypeError:
        bday = '-'
        birthplace = '-'


    dict[csv_columns[4]] = bday
    dict[csv_columns[5]] = birthplace
    dict[csv_columns[6]] = para1
    dict[csv_columns[7]] = para2
    # links.append(f'https://ta.wikipedia.org/{link}')

    if (data_row[1].text.strip().isnumeric() == True):
        dict[csv_columns[2]]=int(data_row[1].text.strip())
    else:
        dict[csv_columns[2]] = '-'

    if (data_row[2].text.strip() == "---") or (len(data_row[2].text.strip())==0):
        dict[csv_columns[3]]= '-'
    else:
        dict[csv_columns[3]] = data_row[2].text.strip()

    dict_data.append(dict)
    number+=1


csv_file = 'data.csv'

try:
    with open(csv_file,'w') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)

except IOError:
    print("I/O error")











    # if (row.td.find('a',{"class": "new"} == 1)):
    #     print(row.td.a.text)

    # print(row.td.a.text)

#     if (row.td.a)
#     names.append(row.td.a.text)
#
# print(names)

# print(body.prettify())

# allLinks = soup.find(id="mw-content-text").find_all("a")
# print(allLinks[1])
