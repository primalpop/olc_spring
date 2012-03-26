##Localization Program - 2D

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

def count():
	return len(colors), len(colors[0])

def sense(p, Z):
    row, column = count() 
    q = [[0.0] * column for i in xrange(row)]	
    for i in range(row):
        for j in range(column):
            hit = (Z == colors[i][j])
            q[i][j] = p[i][j] *(hit * sensor_right + (1-hit) * (1-sensor_right))
    
	s = sum([sum(q[k]) for k in range(len(q))])
   	
    for i in range(len(q)):
        for j in range(column):
            q[i][j] /= s
    return q

def move(p, U):
    row, column = count() 
    q = [[0.0] * column for i in xrange(row)]	
    first, second = U[0], U[1]
    for i in range(row):
        for j in range(column):
            s = p_move * p[(i-first) % row][(j-second) % column]
            s = s + (1 - p_move) * p[i % row][j % column]
            q[i][j] = s  
    return q

def calculate():
	row, column = count() 
	p = [[1.0/(row+column)] * column for i in xrange(row)]	#Creating the Uniform Distribution
	for k in range(len(measurements)):
	    p = move(p, motions[k])
	    p = sense(p, measurements[k])
	return p
 
p = calculate()

#Your probability array must be printed 
#with the following code.
show(p)





