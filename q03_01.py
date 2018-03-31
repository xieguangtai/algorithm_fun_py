import sys
def main():
    lst = [False for _ in range(100)]
    for i in range(2, 100):
        j = i-1
        while j < 100:
            lst[j] = not lst[j]
            j += i
        tmp_lst = [i+1 if v else '' for i, v in enumerate(lst)]
        print(tmp_lst)
        if i == 99:
            sys.exit(0)
        
    for i, j in enumerate(lst):
        if j:
            print(i)

if __name__ == '__main__':
    main()