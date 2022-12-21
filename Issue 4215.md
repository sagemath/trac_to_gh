# Issue 4215: [with patch, needs review] Bug in creating sparse vectors using a dictionary

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-09-29 02:35:44

Assignee: tbd


```
I suspect there is a bug in the implementation of the vector function.
It seems that when trying to construct a sparse vector by a dictionary
sage simply ignores the keys. for example:

sage: v = vector({3:1.1 , 5:3.14}); v
(1.10000000000000, 3.14000000000000)

where one would expect the behavior to be similar to matrix:

sage: m = matrix({(0,3):1.1 , (0,5):3.14}); m
[0.000000000000000 0.000000000000000 0.000000000000000
1.10000000000000 0.000000000000000  3.14000000000000]

it seems to me that the problem is in prepare_dict (in
free_module_element)
```



---

Attachment

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-29 04:15:14

Resolution: fixed


---

Comment by mabshoff created at 2008-09-29 04:15:14

Merged in Sage 3.1.3.alpha2
