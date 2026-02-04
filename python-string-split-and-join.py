def split_and_join(line):
    # write your code here
    linelist=line.split(" ")
    st=linelist[0]
    for i in range(1,len(linelist)):
       st= st+"-"+linelist[i]
    return st

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
