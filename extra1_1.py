
# hyperscroll
# program to check if dot-plot sequence is valid

def check_dot(seq):
	wrong_stack = []
	openbracket_count, closedbracket_count = 0, 0
	openbracket_count = seq.count('(')
	closedbracket_count = seq.count(')')
	if openbracket_count == closedbracket_count:
		for char in seq:
			if char == '(' or char == ')' or char == '.':
				continue
			elif char != '(' or char != ')' or char != '.':
				wrong_stack.append(char)
		if wrong_stack:
			print("Wrong sequence - can't contain anything else but '(', ')', '.'. Delete: " + str(wrong_stack))
			return
	else:
		print("Wrong sequence - number of opening and closing brackets is not equal.")
		return
	openbracket_count, closedbracket_count = 0, 0
	for char in seq:
		if char == '(':
			openbracket_count = openbracket_count + 1
		if char == ')':
			closedbracket_count= closedbracket_count + 1
		if closedbracket_count > openbracket_count:
			print("Wrong sequence - incorrect order of the brackets or there are brackets that are not closed")
			return
	print("Good sequence!")

if __name__ == '__main__':
	seq = input()
	check_dot(seq)



