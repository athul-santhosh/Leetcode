# Appraoch :

# Traverse the list  
# use four variables so as to keep clean track of all the list and avoid confusions
# if cur.data < x => smaller list
# else cur.data => larger_list
# if small list is empty , return large head
# else small_tail.next = large_head
# return small head
 


def partition(head, x):
	small_head = None
	small_tail = None
	large_head = None
	large_tail = None
	cur = head
	while cur:
		if cur.data < x:
			if small_head is None:
				small_head = cur
				small_tail = small_head
			else:
				small_tail.next =  cur
				small_tail = cur
		else:
			if large_head is None:
				large_head = cur
				large_tail = large_head
			else:	
				large_tail.next = cur
				large_tail = cur
				
	cur = cur.next
	# if there is no lesser element in the list => important corner case
	if small_tail is None:
		return large_head
	small_tail.next = large_head
	return small_head
