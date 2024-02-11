def diamondpattern(rows):
    
    for i in range(1, rows + 1):                    #upper half diamond shape
        print(" " * (rows - i) + "* " * i)
    
    
    for i in range(rows - 1, 0, -1):                #lower half diamond shape
        print(" " * (rows - i) + "* " * i)


rowno = 5
diamondpattern(rowno)
