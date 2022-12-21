# Issue 706: irange --- also add range that includes the endpoints by default

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-20 14:33:20

Assignee: somebody

From Jaap Spies (see attached):

```
Forgot to add a few examples:

sage: v = irange(0,5); v
[0, 1, 2, 3, 4, 5]
sage: v = irange(1,10); v
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: v = irange(10,-1,-1); v
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
sage: v = irange(1,8, 1/2); v
[1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7, 15/2, 8]
sage: v = irange(1,2, 0.4); v
[1, 1.40000000000000, 1.80000000000000]
sage: v = irange(1, 2, 0.5); v
[1, 1.50000000000000, 2]
sage: v = irange(1, 2, -0.5); v
[]
sage: v = irange(2, -2, -0.5); v
[2, 1.50000000000000, 1.00000000000000, 0.500000000000000, 0.000000000000000, -0.500000000000000, -1.00000000000000, -1.50000000000000, -2]
sage: v = irange(10,1); v
[]
sage: v = irange(10,10); v
[10]
sage: v = irange(10); v
Traceback (most recent call last):
...
TypeError: irange() takes at least 2 arguments (1 given)
sage: v = irange(0.5, 2.5, 0.5); v
[0.500000000000000, 1.00000000000000, 1.50000000000000, 2.00000000000000, 2.50000000000000]
sage: [n^2 for n in irange(-1, 10)]
[1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

And this one from the calculus thread!
> --  I think that the Python convention of not including the upper bound
>> > in a sum is a real problem.
>> >
>> > sage: sum(i for i in range(1,10))
>> > 45
>> >
>> > I understand this is a fundamental convention in Python, and that it is
>> > very
>> > natural for people used to malloc(), but I worry that this will be a
>> > constant
>> > headache for students (and professors!).


sage: sum(i for i in irange(1, 10))
55
```


I think including this is a good idea, modulo serious optimization issues.


---

Attachment


---

Comment by was created at 2007-09-20 15:14:11

Changing assignee from somebody to jaap spies.


---

Attachment

Replying to [ticket:706 was]:
> From Jaap Spies (see attached):
> {{{
> 
> sage: v = irange(0,5); v
> [0, 1, 2, 3, 4, 5]
> sage: v = irange(1,10); v
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
> sage: v = irange(10,-1,-1); v
> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
> sage: v = irange(1,8, 1/2); v
> [1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7, 15/2, 8]
> sage: v = irange(1,2, 0.4); v
> [1, 1.40000000000000, 1.80000000000000]
> sage: v = irange(1, 2, 0.5); v
> [1, 1.50000000000000, 2]
> sage: v = irange(1, 2, -0.5); v
> []
> sage: v = irange(2, -2, -0.5); v
> [2, 1.50000000000000, 1.00000000000000, 0.500000000000000, 0.000000000000000, -0.500000000000000, -1.00000000000000, -1.50000000000000, -2]
> sage: v = irange(10,1); v
> []
> sage: v = irange(10,10); v
> [10]
> sage: v = irange(10); v
> Traceback (most recent call last):
> ...
> TypeError: irange() takes at least 2 arguments (1 given)
> sage: v = irange(0.5, 2.5, 0.5); v
> [0.500000000000000, 1.00000000000000, 1.50000000000000, 2.00000000000000, 2.50000000000000]
> sage: [n^2 for n in irange(-1, 10)]
> [1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
> 
> And this one from the calculus thread!
> > --  I think that the Python convention of not including the upper bound
> >> > in a sum is a real problem.
> >> >
> >> > sage: sum(i for i in range(1,10))
> >> > 45
> >> >
> >> > I understand this is a fundamental convention in Python, and that it is
> >> > very
> >> > natural for people used to malloc(), but I worry that this will be a
> >> > constant
> >> > headache for students (and professors!).
> 
> 
> sage: sum(i for i in irange(1, 10))
> 55
> }}}
> 
> I think including this is a good idea, modulo serious optimization issues. 

irange now only depends on srange. So ticket #701 will solve this issue.

patch 'irange_improved.hg' is relative to 'irange.hg'


---

Comment by was created at 2007-09-21 07:32:08

I think http://trac.sagemath.org/sage_trac/ticket/702 is actually much nicer to use, so for now I think
irange isn't needed.


---

Comment by was created at 2007-09-21 07:32:08

Resolution: wontfix
