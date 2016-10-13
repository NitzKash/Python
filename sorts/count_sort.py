from __future__ import print_function


def count_sort(a):
    aux=[]
    max1=max(a)
    for i in range(0,max1+1):
        aux.append(0)
    for x in a:
        aux[x]+=1
    for i in range(1,max1+1):
        aux[i]=aux[i]+aux[i-1]
    op=[]
    for i in range(0,len(a)):
        op.append(0)
    for i in range(len(a)-1,-1,-1):
        op[aux[a[i]]-1]=a[i]
        aux[a[i]]=aux[a[i]]-1
    return op


if __name__ == '__main__':
    import sys
    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma (no negative numbers):\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(count_sort(unsorted))
