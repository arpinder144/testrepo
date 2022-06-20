from random import *
alpha='abcdefghijklmnopqrstvwxyz'
digits='0123456789'
city=['delhi','toronto','york']

def e_name():
        name=choice(alpha).upper()
        n=randint(0,9)
        for i in range(n):
            name=name+choice(alpha)
        return name   
          
def e_salary():
         salary=uniform(5000,10000)
         return salary 

def e_mob():
          number='789'
          mobil=choice(number)
          for i in range(9):
             mobil=mobil+choice(digits)
          return mobil

def e_city():
          c= choice(city)
          return c


def e_data(n):
    for i in range(n):
       print('name:',e_name(),end=('     '))
       print('Salary:',e_salary(),end=('    '))
       print('Mobile:',e_mob(),end=('      '))
       print('City:',e_city())
       

n=int(input('Enter number of employess:'))
print(e_data(n))
