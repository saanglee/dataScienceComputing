import random
import time

random.seed(100)

def QSort1(arr):
    start = time.time()
    
    ### Edit Here ###
    
    # Quick Sort with pivot in index 0
    
    
    #################

    #### Do not edit here ####
    
    end = time.time()    
    print("QSort1 time:", end - start)
    
    return arr

def QSort2(arr):
    start = time.time() 
    
    ### Edit Here ###
    
    # Quick Sort with pivot in random index


    
    #################



    #### Do not edit here ####
    
    end = time.time()    
    print("QSort2 time:", end - start)
    
    return arr

def QSort3(arr):
    start = time.time()
    
    ### Edit Here ###
    
    # Quick Sort with early stopping

        
    #################



    end = time.time()    
    print("QSort3 time:", end - start)
    
    return arr

def main():
    ### Edit Here ###
    
    # get number list


    
    #################

    result1 = QSort1(arr)
    result2 = QSort2(arr)
    result3 = QSort3(arr)
    
    print("QSort1 result:", result1)
    print("QSort2 result:", result2)
    print("QSort3 result:", result3)

if __name__ == "__main__":
    main()