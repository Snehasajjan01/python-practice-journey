#Write program to merge two dictionaries
student = {1:'Veena',
           2:'Rounak',
           3:'Naveen',
           4:'Sarvesh'}
print(student)
teachers = {11:'Shivu',
            12:'Sagar'}
print(teachers)
total ={**student,**teachers}
print(total)