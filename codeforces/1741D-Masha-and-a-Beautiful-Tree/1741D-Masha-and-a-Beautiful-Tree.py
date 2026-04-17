def divide(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr)//2

        l_arr, l_count = divide(arr[:mid])
        r_arr, r_count = divide(arr[mid:])

        if l_count == -1 or r_count == -1:
            return [], -1

        return compare(l_arr, r_arr, l_count + r_count)


    def compare(l, r, c):
        if max(l) < min(r):
            return l + r, c 

        elif max(r) < min(l):
            return r + l, c + 1 
        else:
            return [], -1

    print(divide(arr)[1])