
def main():
    num = 11
    format_lst = ['{:d}', '{:o}', '{:b}']
    while True:
        if all([x.format(num) == x.format(num)[::-1] for x in format_lst]):
            print(num)
        num += 2

if __name__ == '__main__':
    main()