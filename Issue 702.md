# Issue 702: Ellipsis range notation

Issue created by migration from https://trac.sagemath.org/ticket/702

Original creator: robertwb

Original creation time: 2007-09-20 11:00:18

Assignee: was

There have been proposal to add syntax to SAGE similar to magma/mathmatica/etc 1..n for ranges. See the mailing list for much discusssion. 


---

Attachment


---

Comment by robertwb created at 2007-09-20 11:14:26

The above patches are one such proposal. NOTE: it has not been decided whether or not to include this feature. However, I like it. 


```
sage: [1..10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: n = 5
sage: [1..n]
[1, 2, 3, 4, 5]
sage: [0,2,..,10]
[0, 2, 4, 6, 8, 10]
sage: [0,2,..,10,20..30]
[0, 2, 4, 6, 8, 10, 20, 22, 24, 26, 28, 30]

sage: (0,2,..,10)       
<generator object at 0xc57cd78>
sage: A = (5,7,..)
sage: [A.next() for _ in range(20)]
[5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

```


And a non-trivial example


```
sage: L = [1..5]
sage: [L[4], .., next_prime(10), 3, 2, 1]
[5, 6, 7, 8, 9, 10, 11, 3, 2, 1]
```



---

Comment by robertwb created at 2007-09-20 11:14:26

Changing status from new to assigned.


---

Comment by robertwb created at 2007-09-20 11:14:26

Changing assignee from was to robertwb.


---

Attachment


---

Comment by robertwb created at 2007-09-20 11:22:36

Fixed:


```
sage: A = (5,7,..)
sage: [A.next() for _ in range(10)]
[5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
```



---

Attachment


---

Comment by robertwb created at 2007-09-20 19:07:53

Fixed an issue with double quotes, and now this works as well 


```
sage: list(1..5)
[1, 2, 3, 4, 5]
```



---

Attachment

Applied.  (And I fixed a few bugs.)


---

Comment by was created at 2007-09-20 20:11:03

Resolution: fixed


---

Comment by robertwb created at 2007-09-21 22:58:38

Resolution changed from fixed to 


---

Comment by robertwb created at 2007-09-21 22:58:38

Changing status from closed to reopened.


---

Comment by robertwb created at 2007-09-21 22:58:38

[1,2,..,-10] should return the empty list.


---

Attachment


---

Comment by robertwb created at 2007-09-21 23:01:12

Fixed. 


```
sage: [1,2..-1]
[]
sage: [10..1]
[]
sage: [1..10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: [1..10,step=2] # no extra preparsing needed
[1, 3, 5, 7, 9]
```



---

Comment by jason created at 2007-09-22 00:05:19

Why doesn't [10..1] return [10,9,8,7,6,5,4,3,2,1]?


---

Comment by was created at 2007-09-23 21:35:33

I don't think this should be an error:


```
sage: [1..5, step=0.5]
<type 'exceptions.TypeError'>: unable to coerce element to an integer
```


i.e., the universe stuff should take into account the step if given.


---

Comment by was created at 2007-09-25 05:32:12

Fixed now by Robert...


---

Comment by was created at 2007-09-25 05:32:12

Resolution: fixed
