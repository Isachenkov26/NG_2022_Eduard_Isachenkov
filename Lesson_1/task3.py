second = int(input("Enter number of seconds - "))
print(int(second / 86400), ":", int((second % 86400) / 3600), ":",
      int(((second % 86400) / 60) % 60), ":", (((second % 1440)) % 60))

