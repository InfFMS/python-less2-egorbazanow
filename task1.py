# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
  #  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
h = int(input('Введите  час начала уроков:'))
m = int(input('Введите минуты начала уроков:'))
n = int(input('Введите номер урока:'))
t = h * 60 + m
br = 10
timeb = t + (n-1)*45 + br * (n-1)
timee = t + n*45  + br*(n-1)
fullb = timeb // 60
minb = timeb % 60
fulle = timee // 60
minte = timee % 60
print('Начало урока', fullb, minb,  sep = ':')
print('Конец урока', fulle, minte,  sep = ':')
while n == 5:
    br = 45


