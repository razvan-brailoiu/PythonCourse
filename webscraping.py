from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

array_of_dates = [20, 21, 23, 24, 25, 26, 27]
header_initial = ['Nr. crt.', 'Județ', 'Număr de cazuri confirmate(total)', 'Număr de cazuri nou confirmate', 'Incidența  înregistrată la 14 zile']

dictionar_mare = {i: [] for i in header_initial}
dictionar = {}
for day in array_of_dates:
    # if day == 21:
    #     break
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/")
    table = browser.find_element(by=By.XPATH, value='//table')
    lista = table.text.split('\n')

    header_final = []
    for i in range(5):
        header_name = browser.find_element(by=By.XPATH, value=f'//table//td[{i+1}]').text
        header_final.append(header_name)

    print(header_final)
    # //dictionar = {i: [] for i in header_final}
    for i in range(1, len(lista)-1):
        lista_mod = (lista[i].split(' '))
        # print(lista_mod)
        if lista_mod[1] == "Satu" or lista_mod[1] == "Mun.":
            dictionar_mare[header_initial[0]].append(lista_mod[0])
            dictionar_mare[header_initial[1]].append(lista_mod[1]+lista_mod[2])
            dictionar_mare[header_initial[2]].append(lista_mod[3])
            dictionar_mare[header_initial[3]].append(lista_mod[4])
            dictionar_mare[header_initial[4]].append(lista_mod[5])
        elif lista_mod[1] == "Cazuri":
            dictionar_mare[header_initial[0]].append(lista_mod[0])
            dictionar_mare[header_initial[1]].append(lista_mod[1] + lista_mod[2]+lista_mod[3]+lista_mod[4]+lista_mod[5])
            dictionar_mare[header_initial[2]].append(lista_mod[6])
            dictionar_mare[header_initial[3]].append(lista_mod[7])
            dictionar_mare[header_initial[4]].append('')
        else:
            dictionar_mare[header_initial[0]].append(lista_mod[0])
            dictionar_mare[header_initial[1]].append(lista_mod[1])
            dictionar_mare[header_initial[2]].append(lista_mod[2])
            dictionar_mare[header_initial[3]].append(lista_mod[3])
            dictionar_mare[header_initial[4]].append(lista_mod[4])
    # dictionar_mare[


print(dictionar_mare)
df = pd.DataFrame(dictionar_mare)
df.to_csv('Covid21.xls')