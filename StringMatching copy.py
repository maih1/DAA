import time

# Hàm kiểm tra chuỗi có khớp với một mẫu hay không
def isMatch(str, i, pattern, j, dict):
 
    n = len(str)
    m = len(pattern)
 
    # base condition
    if n < m:
        return False
 
    # nếu cả mẫu và chuỗi đều đến cuối
    if i == n and j == m:
        return True
 
    # nếu một trong hai chuỗi hoặc mẫu đến cuối
    if i == n or j == m:
        return False
 
    # ký tự mẫu thứ j
    current = pattern[j]
 
    # nếu ký tự mẫu có trong dict map ánh xạ mẫu và chuỗi
    if current in dict:
 
        s = dict[current]
        k = len(s)
 
        # kiểm tra ký tự tiếp theo của chuỗi từ vị trí chuỗi mẫu trong chuỗi gốc
        if i + k < len(str):
            ss = str[i:i + k]
        else:
            ss = str[i:]
 
        # sai nếu ký tự tiếp theo không khớp với mẫu
        if ss != s:
            return False
 
        # Lặp lại ký tự còn lại nếu ký tự tiếp theo đã khớp với mẫu
        return isMatch(str, i + k, pattern, j + 1, dict)
 
    #kiểm tra các ký tư tiếp theo trong chuỗi 
    for k in range(1, n - i + 1):
 
        # Thêm ký tự tiếp theo vào chuỗi mẫu hiện tại
        dict[current] = str[i:i + k]
 
        # Kiểm tra sự khớp
        if isMatch(str, i + k, pattern, j + 1, dict):
            return True
 
        #Nếu không khớp với ký tự mẫu, xóa khỏi chuỗi mẫu hiện tại
        dict.pop(current)
 
    return False
 
 
if __name__ == '__main__':
 
    str = "stringteststring"
    pattern = "XYX"

    dict = {}

    timeStart = time.time() 

    if isMatch(str, 0, pattern, 0, dict):
        print(dict)
    else:
        print("Khong co chuoi khop")

    timeEnd = time.time()

    time = timeEnd - timeStart

    print("Thoi gian:", time, 's')