import datetime
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm


start_time_doc_1 = datetime.datetime.now()
def get_context(auto_comp, modl, volm, pr_auto):
    return {
        'brend': auto_comp,
        'model': modl,
        'vol': volm,
        'price': pr_auto,
    }

def from_template(auto_comp, modl, volm, pr_auto, template, signature):
    template = DocxTemplate(template)
    context = get_context(auto_comp, modl, volm, pr_auto)

    img_size = Cm(15)
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc
    template.render(context)

    template.save(auto_comp + '_' + str(datetime.datetime.now().date())+'report.docx')

def generate_report(auto_comp, modl, volm, pr_auto):
        template = 'report.docx'
        signature = 'volvo.jpg'
        document = from_template(auto_comp, modl, volm, pr_auto, template, signature)

generate_report('Volvo','XC60','10','2500000')
stop_time_doc_1 = datetime.datetime.now()
print(f'Время затраченное на создание отчета в формате doc 1 способ: {start_time_doc_1 - stop_time_doc_1}')

#----------Второй способ создания отчета в формате doc
start_time_doc_2 = datetime.datetime.now()
doc = DocxTemplate('report.docx')
context = {'brend':'Volvo', 'model':'XC60','vol':'10','price':'2500000'}
img_size = Cm(15)
signature = 'volvo.jpg'
acc = InlineImage(doc, signature, img_size)
context['acc'] = acc
doc.render(context)
doc.save('Авто-финал.docx')
stop_time_doc_2 = datetime.datetime.now()
print(f'Время затраченное на создание отчета в формате doc 2 способ: {start_time_doc_2 - stop_time_doc_2}')

#CSV-----------------------------------------------------------------------------
import csv

# Создание файлов в  формате csv из списка и словаря и их время создания
#csv.writer
start_csv = datetime.datetime.now()
car_data = [[' brend ', ' model ', ' volume ', '  price  '],[' Volvo ', ' XC60 ', 10 , 2500000],[' TOYOTA ', ' Camry ', 8, 2000000]]
with open('data_auto.csv', 'w') as f:
    writer = csv.writer(f,)
    writer.writerows(car_data)
# print('Writing complete.')
stop_csv = datetime.datetime.now()
time_csv = stop_csv - start_csv
print(f'Время создания файла из списка data_auto_csv - {time_csv}')



## csv.Dictwriter
start_csv_d = datetime.datetime.now()
dict_auto = [
    {'brend': 'Volvo', 'model': 'XC60', 'volume': 10, 'price': 2500000},
    {'brend': 'TOYOTA', 'model': 'Camry', 'volume': 8, 'price': 2000000}
]

filednames = ['brend', 'model', 'volume', 'price']

with open('dict_auto_ex.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=filednames)
    writer.writeheader()
    for i in range(len(dict_auto)):
        writer.writerow(dict_auto[i])
stop_csv_d = datetime.datetime.now()
time_csv_d = stop_csv_d - start_csv_d
print(f'Время создания файла из словаря dict_auto_csv - {time_csv_d}')






# Создание файла в формате json_и его время создания_----------------------------------------------------------------
import json
start_json = datetime.datetime.now()
dict_auto = [{
    'brend': 'Volvo', 'model': 'XC60', 'volume': 10, 'price': 2500000},
    {'brend': 'TOYOTA', 'model': 'Camry', 'volume': 8, 'price': 2000000}]
with open('json_dict_auto.json', 'w') as f:
    json.dump(dict_auto, f)

stop_json = datetime.datetime.now()
time_json = stop_json - start_json
print(f'Время создания файла json - {str(time_json)}')

# Проверял все-ли записалось в файл
# with open('json_dict_auto.json') as f:
#     data_for_auto = json.load(f)
# print(data_for_auto)