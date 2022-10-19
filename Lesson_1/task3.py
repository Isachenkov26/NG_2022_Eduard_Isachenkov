second = int(input("Enter number of seconds - "))
if(second > 60):
    if((second / 60) > 60):
        if((second / 3600) > 24):
            print(int(second / 86400), ":", int((second % 86400) / 3600), ":", int((second % 86400) % 120), ":", (second % 86400) % 60)
        else:
            print("00 : ", int(second / 3600), ":", (int(second / 60) - ((int(second / 3600)) * 60)), ":", second % 120)
    else:
        print("00 : 00 : ", int(second / 60), ":", second % 60)
else:
    print("00 : 00 : 00 : ", second)
input("Click enter to exit")