# author Zhijun
import re

with open('requirements.txt', 'r') as f:
    lines = f.readlines()
    get_off = re.compile(r'==\d.+\d')
    for i in lines:
        print('Before replace: {}'.format(i))
        i = get_off.sub('', i)
        print('After replace: {}'.format(i))
        with open('require_final.txt', 'a') as w:
            w.writelines(i)
            w.close()
    f.close()

if __name__ == '__main__':
    pass
