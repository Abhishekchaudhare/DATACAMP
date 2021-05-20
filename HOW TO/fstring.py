#This technique helps in adding variables in our string
#This technique is advancement over .format method and it has made reading string easier

#Method 1 (.format)
for i in  range(0,100,3):
    print('I will add 3 after {0} and the number will become {1}'.format(i,i+3))

#Method 2 (f string)
for i in range(0,100,3):
    print(f'I will add 3 after number {i} and the number will become {i}')

#format date using fstring, we can add floats, add padding using this
from datetime import datetime
date=datetime(year=1995,month=12,day=28)
print(f'My birthdate is {date:%D}') 

#Extra fun using string from time (i.e strftime)
print(date.strftime('%D'))

