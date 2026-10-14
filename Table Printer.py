tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    # Step 1: Find max width of each column
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for item in table[i]:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)
    
    # Step 2: Print row by row
    num_rows = len(table[0])  # all inner lists same length
    for row in range(num_rows):
        for col in range(len(table)):
            print(table[col][row].rjust(colWidths[col]), end=' ')
        print()  # newline after each row

printTable(tableData)