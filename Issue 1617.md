# Issue 1617: speed problem when factoring polynoms

Issue created by migration from https://trac.sagemath.org/ticket/1617

Original creator: schilly

Original creation time: 2007-12-28 22:01:50

Assignee: was

There is a huge speed difference. Any special reasons? A novice user would possibly not understand why!




```
var('x,y')
time p1=factor(x^99+y^99)

Time: CPU 0.05 s, Wall: 58.43 s
```





```
R.<x,y> = QQ[]
time p2=factor(x^99+y^99)

Time: CPU 0.06 s, Wall: 0.06 s
```



---

Comment by mabshoff created at 2007-12-29 04:22:29

Changing assignee from was to malb.


---

Comment by mabshoff created at 2007-12-29 04:22:29

This is likely caused by using Maxima's factoring vs. Singular's libfactor. In the first case x and y are symbolic. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-29 04:22:29

Changing component from algebraic geometry to commutative algebra.


---

Comment by malb created at 2008-01-16 16:01:03

I vote for `wontfix` because I see no way of fixing this, this is a Maxima speed issue. The only fix I could think of is to add something about this in some documentation.


---

Comment by was created at 2008-01-16 16:13:03

Changing status from new to assigned.


---

Comment by was created at 2008-01-16 16:13:03

Changing assignee from malb to was.


---

Attachment


---

Comment by mabshoff created at 2008-01-16 17:16:51

At least one comment is wrong in the patch since the "-" no longer shows up:

```
2288	2288	        Notice that the -1 factor is separated out: 
2289	2289	            sage: f.factor_list() 
2290	 	            [(-1, 1), (y - x, 1), (y^2 + x*y + x^2, 1)] 
 	2290	            [(x - y, 1), (y^2 + x*y + x^2, 1)] 
```


Cheers,

Michael


---

Comment by ncalexan created at 2008-01-19 22:25:28

This patch could interact with #1391 (http://trac.sagemath.org/sage_trac/ticket/1391).  That one should be applied first, I think, and then this looked at again.


---

Comment by malb created at 2008-01-25 17:01:51

The patch applies to 2.10.1.alpha1 (hunks, but success). Afterwards, only the `toy_buchberger.py` tests fail which is unrelated. Thus, I say: apply.


---

Comment by was created at 2008-01-25 17:12:21

The mabshoff comment above about "At least one comment is wrong in the patch since the "-" no longer shows up" was caused by ncalexan's patch related to factorization.py, which was after #1617.


---

Comment by mabshoff created at 2008-01-25 17:32:11

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-25 17:32:11

Resolution: fixed
