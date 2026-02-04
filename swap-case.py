def swap_case(s):
    st=""
    for i in s:
        if i.islower():
           st = st+i.upper()
        elif i.isupper():
            st=st+i.lower()
        else:
            st=st+i
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)