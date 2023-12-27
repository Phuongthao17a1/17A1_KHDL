while True:
    try:
        x=int(input("Nhap X:"))
        break
    except ValueError:
        print("bi loi, moi nhap lai")
print("X=",x)