# Beat

'''
    dd.mm.yyyy
    1.0 (20.6.2021) - a
    '''

# TODO:
# 1. more complex conversion to raw (for nested 111/1001)? like "1 101","111 111 101"


'''
	1 [arg] - push arg onto the stack as decimal
	10 - pop
	11 - get input as decimal number, and push
	100 - get input as char, get its decimal <not ASCII> (my own code thing) value and push
	101 - output as decimal + pop
	110 - output as <not ASCII> + pop
	111 [func] - while top value ≠ 0 (if its = 0, immediately break), execute the function (it can have [arg])
	1000 - execute top value (converted to binary) as a function + pop, value below is [arg] (you can also do like 111 [func] [arg])
	1001 [func] - skips the function if top value is 0
	1010 - duplicates top value of the stack
	1011 - flips stack
	1100 - if top two values on the stack are equal, pushes 1, otherwise pushes a 0
	1101 - 101 but w/o pop
	1110 - 110 but w/o pop
	1111 - ends the program
	'''
con = ['\n',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.',',','!','?',':',';',"'",'"','(',')','[',']','{','}','<','>','_','@','#','$','&','%','^','/','\\','+','-','*','=','|','~','`','°','	'] # con=convert

'''epic ascii bootleg
	1  -       1 - \n
	2  -      10 - space
	3  -      11 - A
	...
	28 -   11100 - Z
	29 -   11101 - a
	...
	54 -  110110 - z
	55 -  110111 - 0
	56 -  111000 - 1
	57 -  111001 - 2
	58 -  111010 - 3
	59 -  111011 - 4
	60 -  111100 - 5
	61 -  111101 - 6
	62 -  111110 - 7
	63 -  111111 - 8
	64 - 1000000 - 9
	65 - 1000001 - .
	66 - 1000010 - ,
	67 - 1000011 - !
	68 - 1000100 - ?
	69 - 1000101 - :
	70 - 1000110 - ;
	71 - 1000111 - '
	72 - 1001000 - "
	73 - 1001001 - (
	74 - 1001010 - )
	75 - 1001011 - [
	76 - 1001100 - ]
	77 - 1001101 - {
	78 - 1001110 - }
	79 - 1001111 - <
	80 - 1010000 - >
	81 - 1010001 - _
	82 - 1010010 - @
	83 - 1010011 - #
	84 - 1010100 - $
	85 - 1010101 - &
	86 - 1010110 - %
	87 - 1010111 - ^
	88 - 1011000 - /
	89 - 1011001 - \
	90 - 1011010 - +
	91 - 1011011 - -
	92 - 1011100 - *
	93 - 1011101 - =
	94 - 1011110 - |
	95 - 1011111 - ~
	96 - 1100000 - `
	97 - 1100001 - °
	98 - 1100010 - tab
	'''


print('Welcome to the Beat interpreter')

def tochar(n):
	# n is decimal
	return con[n-1]

def tonum(c):
	return con.index(c)+1

def tobin(n):
	return str(bin(n))[2:]

def todec(n):
	return int(n,2)


starts = ['@','#','?','%']
# shoutout to Tobias SN
left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

stack = []
startpos = ''
starttype = ''
cdir = (0,0)
pointer = (0,0)
current = ''
bc = '' # bc=binary code

def reset():
    global stack,startpos,starttype,cdir,pointer,current,bc
    stack = []
    startpos = ''
    starttype = ''
    cdir = 0
    pointer = (0,0)
    current = ''
    bc = ''


def raw(ss):
	global stack
	ssl = ss.split('\n')
	ssl.append(' ')
	skip = 'none'
	min = 0
	nskip = 0
	for m in ssl:
		#print(1,stack)
		if m != '0':
			ssl[min] = m.lstrip('0')
		if nskip != 0:
			min += 1
			nskip -= 1
			if nskip < 0:
				nskip = 0
			continue
		if skip == 'none' or (skip == '1001' and stack[-1] != 0):
			# push
			if m == '1':
				skip = '1'
			# pop
			elif m == '10':
				stack.pop()
			# input dec
			elif m == '11':
				stack.append(int(input('11>')))
			# input char
			elif m == '100':
				stack.append(tonum(input('100>')[0]))
			# out dec + pop
			elif m == '101':
				print(stack.pop(),end='')
			# out char + pop
			elif m == '110':
				print(tochar(stack.pop()),end='')
			# while not eq 0
			elif m == '111':
				skip = '111'
			# exec
			elif m == '1000':
				sm1 = tobin(stack[-1])
				if len(stack) >= 2:
					sm2 = tobin(stack[-2])
				stack.pop()
				if sm1 == '1':
					stack.pop()
					raw('1\n'+sm2)
				else:
					raw(sm1)
			# skip if top = 0
			elif m == '1001':
				skip = '1001'
			# duplicate
			elif m == '1010':
				stack.append(stack[-1])
			# flip
			elif m == '1011':
				stack = list(reversed(stack))
			# top two equal
			elif m == '1100':
				if stack[-1] == stack[-2]:
					stack.append(1)
				else:
					stack.append(0)
			# out dec
			elif m == '1101':
				print(stack[-1],end='')
			# out char
			elif m == '1110':
				print(tochar(stack[-1]),end='')
			# stop
			elif m == '1111':
				break
				
			if skip == '1001':
				skip = 'none'
		elif skip == '1':
			stack.append(todec(m))
			skip = 'none'
		elif skip == '111':
			while 1:
				if stack[-1] == 0:
					break
				if m == '1':
					raw('1\n'+ssl[min+1])
				else:
					raw(m)
			skip = 'none'
		elif skip == '1001' and stack[-1] == 0:
			if m == '1':
				nskip = 1
			elif m == '111' or m == '1001':
				skip = m
			else:
				skip = 'none'
		min += 1
		nskip -= 1
		if nskip < 0:
			nskip = 0
		#print(2,stack)


def beat(bb):
    global stack,startpos,starttype,cdir,pointer,current,bc
    # 1 find starting point (@ right, # down, ? left, % up)
    # 2 convert to raw beat
    # 3 execute
    bbl = bb.split('\n')
    length = len(max(bbl, key=len))
    bbl.insert(0,length*' ')
    bbl.append(length*' ')

    kkin = 0
    for kk in bbl:
        bbl[kkin] = ' ' + bbl[kkin] + (length-len(kk)+1)*' '
        kkin += 1
    iin = 0
    subin = 0
    # i = row, sub = column
    for i in bbl:
        for sub in i:
            if sub in starts:
                starttype = sub
                startpos = str(iin)+':'+str(subin)
                pointer = (iin,subin)
                current = sub
                if sub == '@':
                    cdir = right
                elif sub == '#':
                    cdir = down
                elif sub == '?':
                    cdir = left
                elif sub == '%':
                    cdir = up
                break
            subin += 1
        iin += 1
        subin = 0
    while current != ' ':
        if current == '^':
            if cdir != up:
            	bc = bc + '\n'
            cdir = up
        elif current == '>':
            if cdir != right:
            	bc = bc + '\n'
            cdir = right
        elif current == 'v':
            if cdir != down:
            	bc = bc + '\n'
            cdir = down
        elif current == '<':
            if cdir != left:
            	bc = bc + '\n'
            cdir = left
        elif current == '+':
            if cdir == left or cdir == right:
                if bbl[pointer[0]+1][pointer[1]] == '+' or bbl[pointer[0]-1][pointer[1]] == '+':
                    bc = bc+'1'
                else:
                    bc = bc+'0'
            elif cdir == down or cdir == up:
                if bbl[pointer[0]][pointer[1]+1] == '+' or bbl[pointer[0]][pointer[1]-1] == '+':
                    bc = bc+'1'
                else:
                    bc = bc+'0'
    
        pointer = (pointer[0] + cdir[0], pointer[1] + cdir[1])
        current = bbl[pointer[0]][pointer[1]]
    
    raw(bc)


while 1:
    print('Type "c" to code - use \\n for newlines (then type c again to exit); "o" to open a file')
    og = input()
    if og == 'c':
        cinp = input()
        while cinp != 'c':
            beat(cinp.replace('\\n','\n'))
            print('/---\\')
            reset()
            cinp = input()
    elif og == 'o':
        print('Enter file path')
        oinp = input()
        oopen = open(oinp,'r')
        oread = oopen.read()
        oopen.close()
        beat(oread)
        print('/---\\')
        reset()