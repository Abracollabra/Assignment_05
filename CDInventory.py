#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DeborahC, 2022-Nov-11, Modified File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
# Replace list of lists with list of dicts
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('\n\nThe Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] eXit')
    strChoice = input('\n\nl, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Add the functionality of loading existing data [from the .txt file]
        objFile = open(strFileName,'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID':lstRow[0], 'CD Title':lstRow[1], 'Artist':lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
      
    elif strChoice == 'a': 
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID':strID, 'CD Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dicRow)          
      
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')        
                  
    elif strChoice == 'd':
        delCD = int(input('Please input the index number of the CD you\'d like to delete.'))
        print(delCD)  #for testing only
        del lstTbl[delCD]        
               
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1]  + '\n'
            objFile.write(strRow)
        objFile.close()     
      
    else:
        print('Please choose either l, a, i, d, s or x!')

    
    



