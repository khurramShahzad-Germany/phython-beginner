GPA = input('enter your GPA: ')
GPA = float(GPA)
if GPA < 0 :
    print('error: please enter the correct GPA, i.e from 0.01 to 4.0')
elif GPA < 2.0 :
    print('GRADE: F')
elif GPA < 2.5 : 
    print('GRADE: D')
elif GPA < 3.0 :
    print('GRADE: C')
elif GPA < 3.5 : 
    print('GRADE: B')
elif GPA <= 4:
    print('GRADE: A')
elif GPA > 4 :
    print('error: please enter the correct GPA, i.e from 0.01 to 4.0')
else:
    print('error: please enter the correct GPA, i.e from 0.01 to 4.0') 
