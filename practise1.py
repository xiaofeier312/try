print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# http://www.runoob.com/python/python-100-examples.html
# example 1
# give 1,2,3,4 ,assemble 3 bit number

numlist = [1, 2, 3, 4]
flag = 0
for i in numlist:
    for j in numlist:
        for k in numlist:
            if i != j and i != k and j != k:
                str_num = str(i) + str(j) + str(k)
                flag += 1
                print str_num
print 'sum: {} numbers'.format(flag)
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# example 5

list_exam = []
# for i in range(0,3):
#     list.append(int(raw_input('Please input the {} number: '.format(i))))
# list.sort()
# print list

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# example 7

list_exam = ['a', 'z', 1, 3]
copy_list = list_exam[:]
print 'Copy_list: {}'.format(copy_list)
rever_list = list_exam[::-1]
print 'Rever_list: {}'.format(rever_list)

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# example 8
list_numbers = range(1, 10)
print 'talbe_list: ', list_numbers
for i in list_numbers:
    for j in list_numbers:
        if j <= i:
            print '{}*{}={}'.format(i, j, i * j),
    print
num_int = 200
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

# example 14

def decompose(num):
    get_list = []
    for x in range(2, num + 1):
        if num % x == 0:
            while num % x == 0:
                get_list.append(x)
                num /= x
    return get_list


print('Get_list: {}'.format(decompose(271)))
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# example 100
dict1 = {'a': 1, 'b': [{'aa': 11}, {'bb': 22}]}

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

# example 14
import os
import sys
cur = os.getcwd()
tree_list = []
def get_all(cur):

    if os.path.isfile(cur):
        print('Given is a file: {}'.format(cur))
        tree_list.append({cur: '_file_'})
    elif os.path.isdir(cur):
        print('Get folder~ {}'.format(cur))
        cur_ = os.listdir(cur)
        print('~~get cur_: {}'.format(cur_))
        for i in cur_:
            i_dir = cur+'/'+i
            get_all(i_dir)
        tree_list.append({cur: os.listdir(cur)})
    else:
        print('Given is not file or folder: {}'.format(cur))
get_all(cur)
print('@@@')
print(tree_list)

print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
from try3 import Person