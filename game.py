import random
import time

def tit():
	print("#########################################################")
	print("#  _______  __    __         ________   _____     __    #  ")
	print("# /__  __/ /-/   / /_       /___  __/  /__   /   / /__  #  ")
	print("#   / /    __   / ___/ ____    / /     ___\  \  / ___/  #   ")
	print("#  / /    / /  /  \   /___/   / /     /  o  /  /  \     #")
	print("# /_/    /_/  /_/\_\         /_/     /_____/  /_/\_\    # ")
	print("#########################################################")
	print("\n..........................................DEVELOPER:t3j")	
def toss():
	print("\nTossing a coin",end="")
	time.sleep(1)
	print(".",end="")
	time.sleep(1)
	print(".",end="")
	time.sleep(1)
	print(".")
	outcome=random.randint(0,1)
	return outcome
	
def whofirst(out):
	if out==1:
		print("\nYOU WON THE TOSS")
		
		time.sleep(1)
	elif out==0 :
		print("\nCPU WON THE TOSS")
		time.sleep(1)
	else :
		print("")	
		


def cpufill(li):
	 
	 
	 while(True):
	 	inp=random.randint(0,8)
	 
	 	if li[inp]==' ':
	 		break
	 	
	 return inp
	 
def userfill(li):
	
	while(True):
		inp=int(input("\nYour Turn(choos place number): "))
		if li[inp]==' ':
			break
		else:
			print("ALDREDY FILLED,Choose different place\n")		
	return inp

def graphics(li):
	time.sleep(1)
	print(" ",li[0]," | ",li[1]," | ",li[2],end="")  
	print("\t\t          0 | 1 | 2 ")
	print("-----------------\t\t-------------")
	print(" ",li[3]," | ",li[4]," | ",li[5],end="")
	print("\t\t          3 | 4 | 5 ")
	print("-----------------\t\t-------------")
	print(" ",li[6]," | ",li[7]," | ",li[8],end="")                                    
	print("\t\t          6 | 7 | 8 ")
	print("\n\n")
	

def hint():
	print("\n__________________________________________________")
	print("\nINSTRUCTIONS : ")
	print("\t-->There are 0-8 places.You have to choose any one of them when it your turn.")
	print("\n")
	graphics(li)
	print("\n\n")
	
def win(li):
	
			
		if(li[0]==li[1]==li[2]!=' '):
			print("Tried:[0,1,3]")
			return li[0]
		elif(li[3]==li[4]==li[5]!=' '):
			print("Tried:[3,4,5]")
			return li[3]
		elif(li[6]==li[7]==li[8]!=' '):
			print("Tried:[6,7,8]")
			return li[6]
		elif(li[0]==li[4]==li[8]!=' '):
			print("Tried:[0,4,8]")
			return li[0]
		elif(li[2]==li[4]==li[6]!=' '):
			print("Tried:[2,4,6]")
			return li[2]
		else:
			return ' '

def check(ret,li,t):
	if(ret=='X'):
		print("\nYOU WON !!!")
		return 0
	elif(ret=='O'):
		print("\nCPU WON !!!")
		return 0
	elif(t==1):
		print("Match Draw !!!")
		return 0
##########################################################

li=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
tit()
out=toss()	
whofirst(out)
hint()
print("Print 'C' to continue: ",end=" " )
input()
t=9
while(t>0):	 
	
	

	if out%2==0:
		inp=cpufill(li)
		li[inp]='O'
		time.sleep(1)
		print("CPU Input : ",inp)
	else :
		inp=userfill(li)
		li[inp]='X'	
	out=out+1
	t=t-1
	
	graphics(li)	
	ret=win(li)
	action=check(ret,li,t)		
	
	if(action==0):	
		exit()






