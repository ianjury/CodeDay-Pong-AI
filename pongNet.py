import random
def neuralNetwork(input1, input2, input3, externLayer):	#externLayer is (presumably

	inputs = [1, 2, 3] #This is the inputs.
	layer1 = [3.01, 4.01, 5.01, 6.01]#Layer 1 of weights
	output = 4.01 #output. Defaults to
	x = 0 #x, is used for a variety of purposes like y
	y = 0

	buffer1 = [[0 for x in range(3)] for y in range(4)] #buffer1 is a 4x5 array. I've left extra space
	#just in case.

	inputs[0] = input1
	inputs[1] = input2
	inputs[2] = input3

	for x in range(0, 3):
		layer1[x] = externLayer[x]


	x = 0 #Reinitialize the x and y values.
	y = 0

	for x in range(0, 3):
	        buffer1[0][x] = inputs[x]
	        buffer1[1][x] = inputs[x]
	        buffer1[2][x] = inputs[x]
	        buffer1[3][x] = inputs[x]
	x = 0#Reinitalize the x and y values
	y = 0

	for x in range(0, 3):#Preform neural network arithmetic.
	        for y in range(0, 3):#Cycles through all of the values
	                buffer1[x][y] = buffer1[x][y] * layer1[x] # and multiplies it by the weight
	               # print buffer1[x][y] #Prints all of the output values. Used for troubleshooting.
	                #Comment out when not needed

	x = 0 #Reinitialize the x and y values
	y = 0

	for x in range(0, 3):
	        for y in range(0, 3):
	                output = buffer1[x][y] + output
	#print (output % 8) + 1
	return (output % 8) + 1

def evolv(e):

        y = 0
        x = 0
        #random.seed(a = None)
        y = random.randint(0, 4)
        x = random.randint(0, 1)
        change = 1.5
        if(y == 0):
                if(x == 1 and e[0] <= 7):
                        e[0] = e[0] + change
                elif(x == 0 and e[0] > 0):
                        e[0] = e[0] - change
        elif(y == 1):
                if(x == 1 and e[1] <= 7):
                        e[1] = e[1] + change
                elif(x == 0 and e[1] > 0):
                        e[1] = e[1] - change
        elif(y == 2):
                if(x == 1 and e[2] <= 7):
                        e[2] = e[2] + change
                elif(x == 0 and e[2] > 0):
                        e[2] = e[2] - change
        elif(y == 3):
                if(x == 1 and e[3] <= 7):
                        e[3] = e[3] - change
                elif(x == 0 and e[3] > 0):
                        e[3] = e[3] - change
