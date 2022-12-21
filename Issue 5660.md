# Issue 5660: count_points(1) for elliptic curves over finite fields is stupid

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-01 17:27:14

Assignee: was

CC:  jcooley

There is one special case of count_points that could be massively faster.  This should definitely be optimized!


```
sage: E = EllipticCurve(GF(97),[1,2])
sage: time E.count_points(1)
[104]
Time: CPU 1.91 s, Wall: 1.93 s
sage: time E.cardinality()
104
Time: CPU 0.00 s, Wall: 0.18 s
```



---

Comment by cremona created at 2009-04-16 20:51:02

I think that count_points is some general scheme thing.  All that needs doing is overriding that for elliptic curves I think.


---

Comment by davidloeffler created at 2009-07-21 08:14:26

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-21 08:14:26

Changing component from number theory to elliptic curves.


---

Comment by cremona created at 2009-07-21 08:54:40

All that is needed is to add a count_points(n) method for elliptic curves over finite fields which returns self.cardinality(extension_degree=n).  An easy job for someone!


---

Comment by cremona created at 2009-08-18 10:37:26

Applies to 4.1.1


---

Attachment

The patch follows the above suggestion, and also overwrites the rational_points() function for elliptic curves over finite fields to be synonymous to points().


---

Comment by cremona created at 2009-08-19 09:26:48

Apply after previous


---

Attachment

Looks good and passes tests.


---

Comment by mvngu created at 2009-08-23 00:44:54

I'm getting the following doctest failure with the above two patches applied to Sage 4.1.1:

```
sage -t -long devel/sage-main/sage/schemes/generic/algebraic_scheme.py
**********************************************************************
File "/scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/devel/sage-main/sage/schemes/generic/algebraic_scheme.py", line 794:
    sage: Etilde.rational_points()
Expected:
    [(0 : 0 : 1), (1 : 0 : 1), (2 : 0 : 1), (0 : 2 : 1), (1 : 2 : 1), (2 : 2 : 1), (0 : 1 : 0)]
Got:
    [(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_28
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/tmp/.doctest_algebraic_scheme.py
	 [4.4 s]
```



---

Comment by AlexGhitza created at 2009-08-23 02:00:47

This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.

I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.


---

Comment by AlexGhitza created at 2009-08-23 02:01:16

add after previous two


---

Comment by mvngu created at 2009-08-23 10:09:56

Resolution: fixed


---

Attachment


---

Comment by cremona created at 2009-08-23 11:39:26

Replying to [comment:7 AlexGhitza]:
> This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.
> 
> I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.
> 

Thanks, Alex, you are quite right -- and it is my fault for not testing more before posting the patch.
