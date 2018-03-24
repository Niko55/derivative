import numpy as np


matrix=[] #define empty matrix
row=[] #define empty row
for i in range(3): #total row is 3
    for j in range(3): #total column is 3
        row.append(np.random.randint(0, 10)) #adding 0 value for each column for this row
    matrix.append(row) #add fully defined column into the row
#print(matrix)
m = np.asmatrix(matrix)
#print(m)

one_hot = [0, 0, 1]
b = np.asmatrix(one_hot)

xi = np.dot(b, m)
#print(xi)

def softmax(x_arr):
    for i in x_arr:
        return np.exp(i)/(np.sum(np.exp(i)))
    
if __name__ == "__main__":
    l = softmax(xi)
    print(l)