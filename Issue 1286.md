# Issue 1286: fix maxima floating point precision handling

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-27 00:35:16

Assignee: was

This sucks:

```
sage: SR(1.93902384092834082309480238482348293402384908) + SR(1)
2.939023840928341
```


It should do this:

```
sage: SR(1.93902384092834082309480238482348293402384908) + SR(1)
2.93902384092834082309480238482348293402384908
```


How to implement this?  Use bfloat in Maxima.  Here are some examples:

```
(%i41) block([fpprec:50], bfloat(%pi));
(%o41)       3.1415926535897932384626433832795028841971693993751b0
```

Have to do some weird crap to coerce in mpfr's:

```
(%i1) block([fpprec:50], bfloat(1.93902384092834082309480238482348293402384908));
Warning:  Float to bigfloat conversion of 1.939023840928341
(%o1)        1.9390238409283409299344632850674846197472777518007b0
(%i3) block([fpprec:50], bfloat(193902384092834082309480238482348293402384908)/10^44);
(%o3)          1.93902384092834082309480238482348293402384908b0
```


When simplifying an expression be sure to compute the prec of it as
the min of the precs of all the leaves; integers have infinite precision.





---

Comment by zimmerma created at 2007-11-27 17:31:53

I'm not sure you really want to implement that. Here you mix:

(1) the precision of a floating-point variable (the number of bits or digits used to store its significand)

(2) the accuracy of a given value (a bound on the error with respect to the exact value)

Your idea is that when the user enters 1.93902384092834082309480238482348293402384908, he/she tells you that there
are as many significant digits. But if you do this, this means that mathematically equivalent values such that
1.939 and 1.9390 would represent different values within SAGE. I don't like this. I much prefer that the user 
specifies the precision of the computation as in RealField(23)(1.9390), or that there is a default precision 
for all SAGE objects that are converted to floating-point.


---

Comment by mhansen created at 2007-12-02 02:38:02

This works for me in sage-2.8.15alpha1.


---

Comment by mhansen created at 2007-12-02 02:38:02

Resolution: worksforme


---

Comment by mabshoff created at 2007-12-02 02:43:39


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.15.alpha1, Release Date: 2007-12-01               |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: SR(1.93902384092834082309480238482348293402384908) + SR(1)
2.93902384092834082309480238482348293402384908
sage:
```

Cheers,

Michael
