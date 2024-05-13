def OPCount(num: int) -> int:
    ### Edit Here ###
    # calculate minimum operation count
    if num % 3 == 0:
        return num // 3
    if num % 2 == 0:
        return num // 2
    return num - 1
    #################

def main():
    ### Edit Here ###
    x = input(x)
    #################

    count = OPCount(x)
    print("result:", count)
  
if __name__ == "__main__":
    main()