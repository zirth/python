
choices = []

for x in range(0, 9) :
	choices.append(str(x + 1))

print choices[0]

def printBoard() :
	print '\n-------'
	print '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|'
	print '-------'
	print '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|'
	print '-------'
	print '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|'
	print '-------'

printBoard()
	
	