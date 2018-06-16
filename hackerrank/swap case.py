def swap_case(s): 
    for i in(len(s)): 
        if(i.isupper()): 
            i.lower()
    return s
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
