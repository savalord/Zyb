import zipfile

def download(filename,fio_list):
    newzip = zipfile.ZipFile(r'Наряд-заказы.zip', 'w')  # создаем архив
    for i in range(0, len(fio_list)):
        newzip.write('./Exsel_Files/' + fio_list[i] + 'Макс.xlsx')
        newzip.write('./Exsel_Files/' + fio_list[i] + 'Мин.xlsx')
    newzip.write('./Exsel_Files/общая_сумма.xlsx')
    newzip.close()
