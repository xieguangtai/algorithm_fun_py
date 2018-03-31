#from operator import add, sub, mul, truediv
import itertools

def change_09_2_9(eval_str):
    lst = [('0{}'.format(i), str(i)) for i in range(10)]
    state = True
    for s0, s1 in lst:
        if eval_str.find(s0) >= 0:
            state = False
            eval_str = eval_str.replace(s0, s1)
      #     print(s0, s1, eval_str)
    if state:
        return eval_str
    else:
#   print('after else:')
        return change_09_2_9(eval_str)

# python: In Python 3, leading zeros are not allowed on numbers. E.g:
def main():
#    ops = itertools.combinations_with_replacement([add, sub, mul, truediv, ''], 3)
    op_lsts = itertools.combinations_with_replacement(['+', '-', '*', '/', ''], 3)
    op_lsts = itertools.combinations_with_replacement(['*', ''], 3)
    nums = range(1000, 10000)
    products = itertools.product(op_lsts, nums)
    for op_lst, num in products:
        s_lst = list(str(num))
        eval_str = ''.join(''.join(x) for x in itertools.zip_longest(s_lst, op_lst, fillvalue=''))
        if len(eval_str) <= 4:
            continue
        eval_str = change_09_2_9(eval_str)
        try:
            if eval(eval_str) == int(''.join(list(str(num))[::-1])):
#           if eval(''.join(''.join(x) for x in itertools.zip_longest(s_lst, op_lst, fillvalue=''))) == num:
                print(num)
        except Exception as e:
         #  print(''.join(''.join(x) for x in itertools.zip_longest(s_lst, op_lst, fillvalue='')))
         #  print(num, op_lst)
         #  print(eval_str)
            pass

if __name__ == '__main__':
####ss = change_09_2_9('100302030500010203050203040')
#   print('ss:', ss)
    main()