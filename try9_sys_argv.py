import os
import random
import string
import sys


def gen_psd(length=10):
    letters = string.ascii_lowercase+string.digits
    letter_len = len(letters)
    times = 1 + int(length/letter_len)
    res = ''.join([random.choice(letters*times) for x in range(length)])
    return res


if __name__ == '__main__':
    print(gen_psd(int(sys.argv[1])))
    string = gen_psd(int(sys.argv[1]))
    if not os.path.isfile(os.path.join(os.getcwd(),'text1')):
        tmp = os.popen('touch text1')
    f = open(os.path.join(os.getcwd(),'text1'),'a')
    f.writelines(string)
    f.writelines('\n')
    f.close()
