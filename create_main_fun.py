#function with main
def getInteger():
	result=int(input("Enter integer: "))
	return result

def Main():
	print("Started")
	output = getInteger()
	print(output)
if __name__=="__main__":
	Main()
