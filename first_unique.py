def find_first_unique_num_1(q):
    start = 0
    duplicate_index = []
    while start < len(q):
        if start+1 < len(q):
            for i in range(start+1, len(q)):
                if q[start] != 0 and q[i] != 0 and q[start] == q[i]:
                    duplicate_index.append(start)
                    q[i] = 0
        while start < len(q)-1:
            start += 1
            if q[start] != 0:
                break
        if start == len(q) - 1:
            break
    print(duplicate_index)
    for i in duplicate_index:
        q[i] = 0
    print(q)
    return_val = 0
    for i in q:
        if i != 0:
            return_val = i
            break
    print("final_answer: ", return_val)
    return return_val

def find_first_unique_num(q):
    find_first_unique_num_1(q)
    # if len(q) == 1:
    #     return q[0]
    # if len(set(q)) == 1:
    #     return 0
    # unique = 0
    # for i in range(0, len(q)):
    #     unique = q[i]
    #     found_any = False
    #     for j in range(0, len(q)):
    #         if i != j and unique == q[j]:
    #             found_any = True
    #             unique = 0
    #             break
    #     if not found_any:
    #         return unique
    #     else:
    #         unique = 0
    # return unique


print(find_first_unique_num([1,5,1,3,4,3]))
print(find_first_unique_num([1,1,1]))
print(find_first_unique_num([1, 1, 10]))
print(find_first_unique_num([10]))
print(find_first_unique_num([7, 1, 1, 7]))
print(find_first_unique_num([7, 1, 1, 7, 17]))



