## Computer Process Organization
### lab1 - data structure
#### basic info
* **laboratory work number** : PLMM 5 
* **variant description** :  Hash-map (collision resolution: open addressing)
* **list of group members** : Liu Jun ; Wang Xin Yue
* **synopsis**:

#### contribution
* contribution summary for each group member (should be checkable by git log and git blame);
    - Liu Jun Complete the writing and testing of Muatable Code 
    - Wang Xin Yue Complete the writing and testing of Immutable Code
    - Together to  Complete readme.md
#### explanation 
hash map(open address)
1. we use the list to storage MapEntry(Node) which have k, v;
2. eg: [{k, v}, {k,v}] ---the position of the node storage by the hashvalue
3. we compute the hash use key % size rehash use the key + 1 % size it's mean we use the open address--linear probing
#### work demonstration 
first, we design the 
* work demonstration (how to use developed software, how to test it), should be repeatable by an instructor by given command-line
examples;
#### conclusion
* Mutable objects are nice because you can make changes in-place, without allocating a new object. 
But be careful—whenever you make an in-place change to an object, all references to that object will now reflect the change.    

* Imutable objects are more easy to implement the thread safety. because it will not be change.but  However, whenever you do need a modified object of that new type you must suffer the overhead of a new object creation, as well as potentially causing more frequent garbage collections. 

* in our implementation:
    1.there are something to improve, the map is fix size, we can make the capcity more large when the capcity is not enough. 
    2.the linear probing so make the data is unevenly distributed in the list, we can use We can use square probing or other methods to try to avoid this problem
    
    find possible implementation errors, which can pass some property-based tests.
