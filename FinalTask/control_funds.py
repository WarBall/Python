dirfile = "D:\\testCSV\\"
filename = dirfile + "purchases.csv"
title = ["Category", "Prodyct", "Cost", "Date"]
job_status = True


def menu() : 
    print ('Hello!\n')
    print ('1.Add')
    print ('2.Show all')
    print ('3.Show for date')
    print ('4.Show by category')
    print ('5.Show by min->max')
    print ('6.Delete')
    print ('0.Exit')

def menu_manager() : 
    global job_status
    while job_status :
        operation_entry = input('\nWhat would you like to do? ')

        if operation_entry.isnumeric() and 0 <= int(operation_entry) <= 6 :
            job_status = False
        else :
            print ('\nAn error occurred while typing. Please try again. (Ps: numbers from 0 to 6)')

    options(operation_entry)

def options (n) : 
    global job_status
    if n == '0': #Выход
        job_status = False
        print ('\nAll the best') 
    elif n == '1': #Добавить данные
        add()
        job_status = True
        menu_manager()
    elif n == '2': #Показать данные
        show_all(reading_file())
        job_status = True
        menu_manager()
    elif n == '3': #Запрос по дате
        show_date(reading_file())
        job_status = True
        menu_manager()
    elif n == '4': #Запрос по категории
        show_category(reading_file())
        job_status = True
        menu_manager()
    elif n == '5': #Вывод данных с сортировкой
        show_ascending(reading_file())
        job_status = True
        menu_manager()
    elif n == '6': #Удаление данных
        delet()
        job_status = True
        menu_manager()

#Создать файл
def create_file() :
    import os.path
    if not os.path.isfile(filename) :
        import csv
        with open(filename, "w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
            writer.writerow(title)

#Прочитать данные
def reading_file() :
    import os.path
    
    if os.path.isfile(filename) :
        import csv
        try :
            rows = []
            with open(filename, "r", encoding="utf-8") as fh:
                reader = csv.reader(fh)
                rows = list(reader)
            return rows
        except OSError as ex:
            return "OSError: {}".format(ex)
    else :
        print("File not found! A new file has been created.")
        create_file()
    

        
#Добавить данные           
def add() :
    import csv
    from datetime import datetime

    category = input("Category: ")
    prodyct = input("Prodyct: ")
    cost = input("Cost: ")
    date = str(datetime.now().date())

    with open(filename, "a", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
        writer.writerow([category, prodyct, cost, date])  

#Показать данные
def show_all(rows) :
    for row in rows:
        print("{:13} {:13} {:13} {:13}".format(*row))
    print("\n")

#Запрос по дате
def show_date(rows) :
    import time

    print("\nChoose date")
    date = set()
    for row in rows:
        if row[3] == 'Date':
            continue
        date.add(row[3])
    print(date)

    while True : 
        operation_entry = input('Date(yyyy-m-dd): ')
        try :
            input_date = time.strptime(operation_entry, '%Y-%m-%d')
            for row in rows:
                if row[3] == 'Date' or row[3] != operation_entry :
                    continue
                print(row)
            break
        except ValueError: 
            print('Incorrect data! Try again.') 
            continue 

#Запрос по категории
def show_category(rows):
    categories = set()
    for row in rows:
        if row[0] == 'Category':
            continue
        categories.add(row[0])
    print(categories)

    while True : 
        operation_entry = input('Category: ')
        if operation_entry.isalpha() :
            for row in rows:
                if row[0] == 'Category' or row[0] != operation_entry :
                    continue
                print(row)
                break 
        else :
            print('Incorrect data! Try again.') 
            continue


#Вывод данных с сортировкой
def show_ascending(rows) :
    list_item=rows.pop(0)
    rows.sort(key=lambda x: int(x[2]))
    rows.insert(0,list_item) 

    for row in rows:
        print("{:13} {:13} {:13} {:13}".format(*row))
            
    print("\n")

#Удаление данных
def delet() :
    import os.path
    if os.path.isfile(filename) :
        import csv
        with open(filename, "w", encoding="utf-8", newline="") as fh:
            fh.truncate()
            writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
            writer.writerow(title)
        print("All entries deleted!\n")
    else :
        print("File not found")

