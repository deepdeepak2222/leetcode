def fun():
    try:
        n = int(input())
        a = map(int, input().split())
        m = min(a)
        print(-1, [2 * sum(a)])
    except Exception as e:
        print(e)



def all_sub_strings(s):
    for start in range(len(s) - 1):
        for end in range(start + 1, len(s)):
            sub_string = s[start:(end-start)+2]
            print(sub_string)



def replace_dup(arr):
    total_unique = 1
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            arr[total_unique] = arr[i]
            total_unique += 1

# def check_in_list():
#     from core.models import CardDetail
#     import time
#     start = time.time()
#     print("5fe37e9c" in CardDetail.objects.all().values_list("pk", flat=True))
#     print("Done in %s" % (time.time()-start))
#
# def check_by_filter():
#     from core.models import CardDetail
#     import time
#     start = time.time()
#     print(CardDetail.objects.filter(pk="5fe37e9c").exists())
#     print("Done in %s" % (time.time()-start))































'''
Given arrival and departure times of all trains that reach a railway station, 
the task is to find the minimum number of platforms required for the railway station so that no train waits.

Input: arr[] = {900, 940, 9:50, 11:00, 15:00, 18:00} 
dep[] = {910, 1200, 1120, 11:30, 19:00, 20:00} 
Output: 3 
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)

Input: arr[] = {9:00, 9:40} 
dep[] = {9:10, 12:00} 
Output: 1 
Explanation: Only one platform is needed. 

==============
write a function that takes in an array of positive intigers and returns the maximum sum of non-adjacent elements in the array.

if the inout array is empty, the function should return 0.

Sample input:

array =[75, 105, 120, 75, 90, 135]

sample output
330 //75 + 120 + 135

{
    0: 75,
    1: 105,
    2: 120,
    3: 75,
    4:90,
    5: 135
}

'''
total_plat = 0


def total_pat(arr, dep):
    total_plat = 1
    waiting = 0
    for index, train_arr in enumerate(arr):
        if train_arr < waiting:
            total_plat += 1
            waiting = max(waiting, dep[index])
    print(total_plat)
    return(total_plat)

total_pat([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])
