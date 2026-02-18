def gray_code(n):
    if n == 0:
        return [""]
    
    smaller_gray_code = gray_code(n-1)

    first_half = ["0" + code for code in smaller_gray_code]
    second_half = ["1" + code for code in reversed(smaller_gray_code)]

    return first_half + second_half

if __name__ == "__main__":
    n = int(input())
    result = gray_code(n)

    for code in result:
        print(code)