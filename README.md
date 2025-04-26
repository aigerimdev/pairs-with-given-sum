    Ask clarifiying question?
    1. What if the input is not intiger? It is gonna raise an error?
    2. what if nubers are negative? 
    3. what if the list is empty? It is going to return 0
    4. What if the list has only one number? One number can not make a pair return 0
    5. What if the target is negative number?
    6. If no pairs match? return 0
    7. What if number is 0 in a list?
    8. What if target is 0? 
    9. What if list has only one number and that number is equal to target? 



Your Question	Your Answer	Does it make sense?	Notes
1. Non-integer input?	Raise an error.	✅ Yes!	It's safer to expect clean input, or raise error if not.
2. Negative numbers?	Allow.	✅ Yes!	Negative numbers should be allowed unless the problem says not to.
3. Empty list?	Return 0.	✅ Yes!	No numbers → no pairs → return 0.
4. Only one number?	Return 0.	✅ Yes!	One number can't form a pair.
5. Negative target?	Allow.	✅ Yes!	Target can be any number (positive, negative, zero).
6. No matching pairs?	Return 0.	✅ Yes!	Correct — no pairs, return 0.
7. Number 0 in list?	Allow.	✅ Yes!	Zero is just another number, should be treated normally.
8. Target is 0?	Allow.	✅ Yes!	Should find pairs that add up to 0 (like 0+0 or -1+1).