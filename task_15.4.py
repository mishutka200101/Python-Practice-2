def med(arr):
    arr.sort()
    return arr[len(arr) // 2]


def mod(arr):
    return max(arr, key=arr.count)


def fun():
    n = int(input())
    medi = []
    modi = []
    nums = []
    for _ in range(n):
        num = list(map(int, input().split()))
        nums.extend(num)
        medi.append(med(num))
        modi.append(mod(num))
    print(*medi)
    print(*modi)
    print(med(medi))
    print(mod(modi))
    print(med(nums))
    print(mod(nums))


fun()
