def shuffleString(a, b, c):
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)


    if( len_c !=  len_a + len_b ):

        return False

    else:

        i = 0
        j = 0
        k = 0

        while k != len_c:
            if (i < len_a) and (a[i] == c[k]):
                i += 1
            elif (j < len_b) and (b[j] == c[k]):
                j += 1
            else:
                return False
            k += 1

        if (i < len_a) or (j < len_b):
            return False
        else:
            return True





if __name__ == '__main__':
    a = "AB"
    b = "CD"
    c = "ACGD"

    if shuffleString(sorted(a), sorted(b), sorted(c)) == True:
        print("Is valid suffle")
    else:
        print("Not Valid suffle")