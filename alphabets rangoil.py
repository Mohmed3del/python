from string import ascii_lowercase as alphabets
def print_rangoli(size):
    for i in range(1,2*size):
        m = alphabets[abs(size-i):size]
        m = m[-1:0:-1] + m
        print('-'.join(m).center(size*4-3,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n) 
