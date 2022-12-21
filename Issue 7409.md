# Issue 7409: Partitions(n).random_element() is extremely slow

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-08 10:33:58

Assignee: mhansen

CC:  sage-combinat

Keywords: random integer partition, placherel measure

It is currently implemented by building the list !
Here are some suggestions: Look at 

```
http://www.site.uottawa.ca/~ivan/F49-int-part.pdf
```

Thanks to #7408 we have a fast algorithm for generating partitions with Plancherel measure. So I suggest the following interface:

```
Paritions(n).random_element()
```

default to

```
Partitions(n).random_element_uniform()
```

and to implement

```
Partitions(n).random_element_Plancherel()
```

Any comment about the interface ? 

Cheers,

Florent


---

Comment by mhansen created at 2009-11-08 14:05:11

I would think something like 


```
Partitions(n).random_element(distribution='uniform') #default
Partitions(n).random_element(distribution='plancherel')
```



---

Comment by hivert created at 2009-11-13 15:00:46

Changing assignee from mhansen to hivert.


---

Attachment

I implemented an algorithm from "Nijenhuis, Wilf, Combinatorial Algorithms" which looks reasonably fast. There is certainly room for improvement. However, It will be done later if needed.


---

Comment by hivert created at 2009-11-24 12:50:27

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-01 04:56:43

Looks good.


---

Comment by mhansen created at 2009-12-01 04:56:43

Resolution: fixed
