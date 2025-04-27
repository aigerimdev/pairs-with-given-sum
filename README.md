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



1. If the numbers is empty:
   if yes then return 0
2. Check if all numbers a integers and chek target as well. If not then raise an value error
3. if lenght of number == 1 then return 0 because we dont have peer.
4. create hash table to store seen numbers
5. create a counter to count peers
6. itiRATE trough each number:
      1. find a complement
      2. if colplements is found in our hash_table:
         1. increment our counter by 1
      3. Seen number insert to hashtable as a key and value is True
7. return counter