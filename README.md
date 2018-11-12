# Quiz-nov-12
Linked list: Implement a Linked List to store collection of Date objects. 
Date=(day, month, year)(insert, remove, reverse)

## Intro
Linked list is a data structure which has ordered elements in it.
We can describe it as a list/collection that contains elements that are not located in the memory one after another physically. 
Linked list has head which has a reference to the first element in the list. 
Each element in linked list is called a node and has 2 feature: reference to the next node and data/value. 

## Operations
There are several operations defined for linked list. Here they are
Insert- appends an element after the chosen element
Remove- removes an element from the list 
Display - prints the list
Reverse - reverses the whole list
Search - searches for the specific element in the list


## Complexity
Note that in linked list typed data structure for reaching every node it is needed to start from the very start(head of the list) and go one by one until the last element. This means that for accessing or searching for any element in the linked list time complexity will be the n, or O(n). n is the number of items in the list. While insert and deletion time complexity is not dependant from the number of elements in the list, so it is O(1). 

## description
the code is gaining dates, 
then it is showing the reserved version of the list, 
after it removes an element from the list,
then another item is added.
Note that all the operations described below are getting dates from main.

After the program asks in case user wants to add dates himself
then prints the dates plus the date that was added by the user.
