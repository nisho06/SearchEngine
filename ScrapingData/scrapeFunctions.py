from bs4 import BeautifulSoup

def paragraph(soup_new):
    para1 = None
    para2 = None

    try:
        parser_contents = soup_new.find('div', {"class": "mw-parser-output"}).contents
        for i in parser_contents:
            if i.name == 'p':
                if para1 == None:
                    para1 = i.text.strip()
                    continue
                if para2 == None:
                    para2 = i.text.strip()
                    break
        return (para1, para2)
    except AttributeError:
        return (para1, para2)

def birth(soup_new):
    birthdate = None
    birthplace = None
    try:
        info_box = soup_new.find('table', {'class': 'infobox'})
        table_row_list = info_box.findAll('tr')
    except TypeError or AttributeError:
        return (birthdate, birthplace)

    for tr in table_row_list:
        try:
            if ((tr.th.text).strip() == 'பிறப்பு'):
                if tr.td.findAll('span', {'class': 'bday'}):
                    birthdate = tr.td.find('span', {'class': 'bday'}).text
                if tr.td.findAll('span', {'class': 'birthplace'}):
                    birthplace = tr.td.find('span', {'class': 'birthplace'}).text
                else:
                    try:
                        string_br = str(tr.td)
                        if '<br/>' in string_br:
                            splitted_with_break = string_br.split('<br/>')
                            birthplace = (BeautifulSoup(splitted_with_break[-1], "html.parser").text.strip())
                            if birthplace == '':
                                birthplace = None
                    except AttributeError:
                        continue
        except AttributeError or TypeError:
            continue
    return (birthdate, birthplace)
