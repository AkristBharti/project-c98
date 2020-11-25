def fileswapper():
    #file1loc = input("Please Type File 1's Location: ")
    #file2loc = input("Please Type File 2's Location: ")
    
    file1loc = "sample1.txt"
    file2loc = "sample2.txt"
    
    
    file1data = open(file1loc, "r+")
    file2data = open(file2loc, "r+")
    
    file1words = file1data.read()
    file2words = file2data.read()
    
    print(file1words)
    print(file2words)
    
    file1data.write('\n'+file2words)
    file2data.write('\n'+file1words)
    
    print(file1words)
    print(file2words)
    
fileswapper()
