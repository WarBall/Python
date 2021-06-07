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

    #Создать файл
    def create_file() :
        import os.path

        if not os.path.isfile(filename) :
            import csv
            with open(filename, "w", encoding="utf-8", newline="") as fh:
                writer = csv.writer(fh, quoting=csv.QUOTE_ALL)

    #Прочитать данные
    def reading_file() :
        import os.path

        rows = []
        if os.path.isfile(filename) :
            import csv
            try :
                with open(filename, "r", encoding="utf-8") as fh:
                    reader = csv.reader(fh)
                    rows = list(reader)
                return rows
            except OSError as ex:
                print("OSError: ",ex)
        else :
            print("File not found! A new file has been created.")
            create_file()
            reading_file()
        
    #Добавить данные           
    def add() :
        import csv
        import os.path
        from datetime import datetime

        category = input("Category: ")
        prodyct = input("Prodyct: ")
        date = str(datetime.now().date())
        while True :       
            try:
                cost = int(input("Cost: "))
            except ValueError as ex :
                print("ValueError: ",ex)
                continue
            else :
                break
        with open(filename, "a", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
            writer.writerow([category, prodyct, cost, date])  

    #Показать данные
    def show_all(data_list) :
        print("{:15} {:15} {:15} {:15}".format(*title))
        for row in data_list:
            print("{:15} {:15} {:15} {:15}".format(*row))
        print("\n")

    #Запрос по столбцам
    def show_date(column) :
        import time
        from datetime import datetime

        rows = reading_file()

        print("\n{:15}".format(title[column]))
        dates = set()
        for row in rows:
            dates.add(row[column])
        dates = list(dates)
        for date in enumerate(dates):
            print("{:<7} {:13} ".format(date[0]+1,date[1]))

        while True : 
            try :
                operation_entry = int(input('To complete, enter 0 or the number of\n the parameter you are interested in: '))
            except ValueError as ex: 
                print('ValueError: ',ex) 
                continue
            if operation_entry in range(1,len(dates)+1):
                print("{:15} {:15} {:15} {:15}".format(*title))
                for row in rows:
                    if row[column] == dates[operation_entry-1] :
                        print("{:15} {:15} {:15} {:15}".format(*row))
                break
            elif operation_entry == 0 :
                break
            else :
                print("Please enter a number from 1 to ",len(dates))

    #Вывод данных с сортировкой
    def show_ascending(data_list) :
        print("{:15} {:15} {:15} {:15}".format(*title))

        data_list.sort(key=lambda x: int(x[2]))
        for row in data_list:
            print("{:15} {:15} {:15} {:15}".format(*row))
            
        print("\n")

    #Удаление данных
    def delet() :
        import os.path
        if os.path.isfile(filename) :
            import csv
            with open(filename, "w", encoding="utf-8", newline="") as fh:
                fh.truncate()
            print("All entries deleted!\n")
        else :
            print("File not found")
    
    def menu_manager() : 
        global job_status
        while job_status :
            try:
                operation_entry = int(input('\nWhat would you like to do? '))
            except ValueError as ex :
                print("ValueError: ",ex)
                continue
            if 0 <= operation_entry <= 6 :
                job_status = False
            else :
                print ('\nAn error occurred while typing. Please try again. (Ps: numbers from 0 to 6)')
        options(operation_entry)

    def options (n) : 
        global job_status
        if n == 0 : #Выход
            job_status = False
            print ('\nAll the best') 
        elif n == 1 : #Добавить данные
            add()
            job_status = True
            menu_manager()
        elif n == 2 : #Показать данные
            show_all(reading_file())
            job_status = True
            menu_manager()
        elif n == 3 : #Запрос по дате
            show_date(3)
            job_status = True
            menu_manager()
        elif n == 4 : #Запрос по категории
            show_date(0)
            job_status = True
            menu_manager()
        elif n == 5 : #Вывод данных с сортировкой
            show_ascending(reading_file())
            job_status = True
            menu_manager()
        elif n == 6 : #Удаление данных
            delet()
            job_status = True
            menu_manager()

    menu_manager()