Hashing technique is a way to reduce the complexity of searching down to a constant time complexity.

Linear search : O(n)
Binary search : O(log_2(n))
Hashing search : O(1)

There are 2 kinds of functional relationships in Hashing:
1) one to one : f(x) = x ---> uses too much space
2) many to one : f(n1,n2,...,n) = x ---> leads to collision

Couple of ways of dealing with collision:
1) Open Hashing: increase the space of the hash
   a) chaining :  
	- hash of linked-lists, each index of the hashing table is a linked-list of sorted values.
	- Complexity:
		- Time : lambda = (number of elements/size of hash) --> loading factor tells you how many elements are uniformly distributed to each index of the hashing table.
			- successful search = constant time of hashing + average elements at each index
					    = 1 + (lambda/2)
			- unsuccessful search = constant time of hashing + max elements at each index
					      = 1 + lambda

2) Closed Hashing: use the space given
   - Open Addressing :
	a) Linear Probing
	b) Quadratic Probing
	c) Double Hashing

When to use hashing ?
- when the keys are uniformly distributed