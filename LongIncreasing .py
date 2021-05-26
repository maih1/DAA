
def lengthOfLIS(nums):
    tails =[0 for i in range(len(nums))]
    size = 0
    for x in nums:
        i=0
        j=size
        while i!=j:
            mid = i + (j-i)//2
            if tails[mid]< x:
                i= mid+1
            else:
                j = mid
        tails[i] = x
        size = max(i+1,size)

    return size

if __name__ == '__main__':
    lists = [10, 3, 9, 5, 1, 20, 41, 2]
    res = lengthOfLIS(lists)
    print("Day con don dieu tang dai nhat:", res)