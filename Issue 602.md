# Issue 602: sage: (1/2)^(2^100)
serious powering bug / overflow

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-06 19:24:35

Assignee: boothby


```
sage: (1/2)^(2^100)
1
```


Ouch!


---

Comment by mhansen created at 2007-09-06 21:30:10

The cutoff for the exponent looks to be 2^32.

```
sage: x = 2^(2^32-1)
sage: x == 1
False
sage: x = 2^(2^32)
sage: x == 1
True
sage: 
```



---

Comment by boothby created at 2007-09-06 22:24:11

fixed by patch:

[http://sage.math.washington.edu/home/boothby/my_patches/rationals602.hg](http://sage.math.washington.edu/home/boothby/my_patches/rationals602.hg)


---

Comment by was created at 2007-09-07 01:53:24

Resolution: fixed
