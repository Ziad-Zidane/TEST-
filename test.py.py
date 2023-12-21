
Z = int(input("enter the  first:"))
X = int(input(" the scend  number:"))
A = int(input("enter the  third:"))


def _myfunction(n1, n2, n3):
    if Z > A and Z > X:
        print(Z)
    elif X > Z and X > A:
        print(X)
    elif A > Z and A > X:
        print(A)


_myfunction(Z, X, A)


