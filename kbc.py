question_list = [
   "How many continents are there?",              # pehla question
   "What is the capital of India?",            # doosra question
   "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
   #pehle question ke liye options
   ["1.Four", "2.Nine", "3.Seven", "4.Eight"],
   #second question ke liye options
   ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
   #third question ke liye options
   ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
]
l5050 = [
   #pehle question ke liye options
   ["1.Four", " ", "3.Seven", " "],
   #second question ke liye options
   [" ", "2.Bhopal", " ", "4.Delhi"],
   #third question ke liye options
   ["1.Software Engineering", " ", "3.Tourism", " "]
]
b=0
solution_list = [3, 4, 1] 
for i in range(len(question_list)):
	print(question_list[i])
	print(options_list[i])
	x = int(input("Option No. "))
	if x == solution_list[i]:
		print("Congro")
	elif x == 5050:
		if b == 1:
			print("No life line")
			print(question_list[i])
			print(options_list[i])
			x = int(input("Option No. "))
			if x == solution_list[i]:
				print("Congro")
			else:
				print("Try Next Time")
				break
		else:
			print(l5050[i])
			x = int(input())
			if x == solution_list[i]:
				print("cong")
				b += 1
			else:
				print("Try Next Time")
				break
	else:
		print("agli baar try karna")
		break


