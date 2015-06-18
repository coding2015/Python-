#!/usr/bin/python
'''
bubble algorithm:
	elements compared with it's next element from the tail to the start
	during the process, 
		bigger/smaller element is exchanged to a fronter position like bubble. 		
	time-complex: O(n^2)

KeyPoint:
	changable-obj's shallow copy

Problem-solved:
	use less codes to implement descending or ascending sort
Solving:
    reverse_sorting_list = sorted_list.reverse() or reversed(sorted_list)
    so in the end of Bubble(), add:
    if reverse:
    	a.revered()

Further Problem:
	deep-copy value to Bubble 
'''

def Bubble(a, reverse=False):
	n = len(a)
	for i in range(n):
		exchanged = False
		for j in range(n-1, i, -1):
			if a[j] < a[j-1]:
				temp = a[j]
				a[j] = a[j-1]
				a[j-1] = temp
				exchanged = True
		if exchanged == False:
			break
	if reverse:
		a.reverse()

def main():
	print Bubble.__doc__
	n = int(raw_input('how many elements?> '))
	a = []	
	#for i in n: #error: n is a number, it's not iterable 
	for i in range(n):
		a.append(int(raw_input('enter an integer> ')))
	prompt = '''
Which order do you want to sort?
	(A)scending (default)
	(D)escending	
Please enter choich> '''

	choice = raw_input(prompt)
	if choice and choice[0].lower() == 'd':
		reverse = True
	else:
		reverse = False
	print 'befor sort:'
	print a
	Bubble(a,reverse)
	print 'after sort:'
	print a

if __name__ == '__main__':
	main()
