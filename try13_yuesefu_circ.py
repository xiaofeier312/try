



def get_live(lens=10, k=1):
    """k is step"""
    flag = 0
    if k == 1:
        return lens
    else:
        people = [ x for x in range(1, (lens + 1 )) ]
        print(people)
        while True:
            if flag == 0:
                mod = k  % lens #deal with step > len(people)
                flag = k
            #print(people)
            if mod == 0:
                mod = lens
            people.pop(mod-1)
            lens = lens -1
            if lens == 0:
                break
            flag = (flag + k - 1 ) % lens

            mod = flag
            print(people)





if __name__ == '__main__':
    get_live(7, 3)