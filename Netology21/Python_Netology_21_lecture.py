#%%

f1 = open('file1.txt', 'r')
print (f1.readline())

for line in f1:
    print (line)
f1.close()

l = [str(i)+str(i-1) for i in range(20)]

f2 = open ('file2.txt', 'w')
for index in l:
    f2.write(index + '\n')
f2.close()

f2 = open('file2.txt', 'r')
l = [line.strip() for line in f2]
f2.close()

#%%
f = open ('warandpeace1.txt', 'r')
count = 0
for index, line in enumerate (f):
    if 'Наташа' in line and 'Пьер' in line:
        count += 1
        print (index +1)
print ('Наташа и Пьер встретились в одной строке {} раз.'.format (count))
f.close()

#%%
with open ('file3.txt') as f:
    for line in f:
        line = line.strip()
        team1, score1, _, score2, team2 = line.split(' ')
        score1 = int (score1)
        score2 = int (score2)
        if score1 > score2:
            print ('{0} переиграл {1}'.format(team1, team2))
        elif score1 < score2:
            print ('{0} продул {1}'.format(team1, team2))
        else:
            print ('{0} сравнял счет с {1}'.format(team1, team2))

#%%

classname_max = None
classname_max_height = 0

with open ('file4.txt') as f:
    for _ in range (3):
        classname = f.readline()
        heights = f.readline()
        f.readline()

        heights = heights.split(',')
        int_heights = [int(i) for i in heights]
        print (classname, int_heights)

        avg_heights = sum (int_heights) / len (int_heights)

        if avg_heights > classname_max_height:
                classname_max = classname
                classname_max_height = avg_heights

        print (classname, int_heights, round(avg_heights,2))

print ('Самый высокий класс {0} с ростом {1} см'.format(classname_max, round (classname_max_height,2)))

#%%
import datetime

with open ('file5.txt', 'a') as f:
    f.write('Небольшой текст в {}\n'.format (datetime.datetime.now()))

#%%

with open ('file6.txt', 'w') as f:
    while True:
        print ('Input number: ')
        user_input = input ()

        if user_input == 'exit':
            break

        f.write('Вы ввели число {}\n'.format(user_input))
