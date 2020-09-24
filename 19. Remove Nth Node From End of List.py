Approach:

#locate the previous node to the node to be deleted

#use two pointers runner and striker

#striker will point => previous node to the node to be deleted

#runner makes n moves first

#then runnner and striker moves equal , when runner reaches 

#striker will point =>  node to the node to be deleted



def removeNode(head,n):
	# corner case
	if head is None or Head.next is None:
		return None
	runner = head
	striker = head
	for _ in range(n):
		runner = runner.next
	# the node to be deleted is first element
	if runner is None:
		head = striker.next
		return head
		
		
	while runner.next:
		runner = runner.next 
		striker = striker.next
	striker.next = striker.next.next
	return head 

