def check(str):

    stack = []
    closing = ["}", ")", "]"]
    opening = ["{", "(", "["]

    for i in str:
        if i in opening:
            stack.append(i)
        elif i in closing:
            if stack == []:
                print("Unbalanced")
                return 0
            else:
                stack.pop()

    if stack == []:
        print("baclanced")
    else:
        print("Unbalacned")


if __name__ == '__main__':
    a = "{8)*{9)"
    check(a)


