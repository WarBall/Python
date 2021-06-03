#Работа со строками
string1 = "This is string. "
string2 = " This is another string."
print(string1+string2)
print(len(string1))
print(string1.title())
print(string2.lower())
print(string1.upper())
print(string2.rsplit())
print(string1.lstrip())
print(string2.strip())
print(string1.split("This"))
print("-----------------------------")

#Извлечение символов и подстрок
d = "qwerty"
ch = d[2]
chm = d[1:3]
print(chm)
chm = d[1:]
print(chm)
chm = d[:3]
print(chm)
chm = d[:]
print(chm)
chm = d[1:5:2]
print(chm)
print("-----------------------------")

#Работа с числами
int1 = 6
int2 = 25
print(int2/int1)
print(int2%2)
print(int1**2)
param = "string" + str(15)
print(param)
print("-----------------------------")

#Преобразование данных
param = "string" + str(15)
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)
print("-----------------------------")

#Форматирование строк
a = 1/3
print("{:7.3f}".format(a))
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print("{0} plus {1} = {2:2.3f}".format(n1,n2,n3))
print("-----------------------------")

#Списки
list1 = [82,8,23,97,92,44,17,39,11,12]
#print(dir(list))
#help(list.insert)
#help(list.append)
#help(list.sort)
#help(list.remove)
#help(list.reverse)

list1[0] = 76
list1.append(88)
list1.insert(-2,10)
del list1[0]
list1.pop()
print(list1)
print("-----------------------------")

#Сортировка элементов списка
list1.sort(reverse = True)
print(list1)
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(lis)
print("-----------------------------")

#Кортежи
#print(dir(tuple))
#help(tuple.index)
#help(tuple.count)

seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8)) #Сколько раз число 8 встречается в кортеже
print(seq.index(44)) #Позиция чмсла 44 в кортеже

listseq = list(seq)
print(type(listseq))
print(listseq.sort)
print("-----------------------------")

#Словари
D = {'food':'Cheese','quantity':3,'color':'Yellow'}
print(D['food'])
D['quantity'] += 2
print(D['quantity'])
dp = {}
Age = input("Введите возраст: ")
Name = input("Введите имя: ")
dp['age'] = Age
dp['name'] = Name
print(dp)
print("-----------------------------")

#Вложенность хранения данных
rec = {'name': {'firsname':'Bob','lastname':'Smit'},
       'job':['dev','mgr'],
       'age':25}
print(rec["name"])
print("firstname: ",rec["name"]["firsname"])
print("jobs: ",rec["job"])
newJob=input("Enter new job: ")
rec["job"].append(newJob)
print(rec)