# Issue 9912: n() returns symbolic expression

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-09-16 01:57:27

Assignee: AlexGhitza

CC:  cwitty

from sage-support:
http://groups.google.com/group/sage-support/browse_thread/thread/b36c90f1490eac19#

```
sage: a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5) 
sage: a.imag().n()
0.939469338708203*sin(0.500000000000000*pi)
```



---

Comment by jason created at 2010-09-16 23:50:52

Even simpler:


```
sage: n(arctan2(0,-log(2)))
pi
```



---

Comment by zimmerma created at 2010-09-16 23:57:13

Note also the strange tty output (look in the 2nd argument of `arctan2`):

```
sage: a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5)
sage: a.imag()
sin(1/2*arctan2(0, -88* + 48))*sqrt(abs(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48))/(sqrt(3) + 5)
```


Should I open a separate ticket for that?
Paul


---

Comment by burcin created at 2010-09-18 21:44:26

Changing component from basic arithmetic to symbolics.


---

Comment by burcin created at 2010-09-18 21:44:26

I'm changing the component to `symbolics`, since this is probably a bug in pynac.

Regarding the problem with the output Carl mentions in comment:2: This is also present in GiNaC, but the printing is better:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.7)
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5);
(sqrt(48+4*(5+sqrt(3))*(-5+sqrt(3)))+4*sqrt(3))*(5+sqrt(3))^(-1)
> imag_part(a);
(5+sqrt(3))^(-1)*sqrt(abs(48+4*(5+sqrt(3))*(-5+sqrt(3))))*sin(1/2*atan2(0,48+4*(-22)))
```


Note the term `4*(-22)` at the end of the last line.

We should open a new ticket for this and report it on the GiNaC list. I'm not sure if this has anything to do with this ticket ATM. Numeric evaluation seems to work fine in GiNaC:


```
> evalf(imag_part(a));
0.9394693387082032295
```



---

Comment by burcin created at 2010-09-18 21:44:26

Changing assignee from AlexGhitza to burcin.


---

Comment by zimmerma created at 2010-09-19 08:27:19

Burcin,

> We should open a new ticket for this and report it on the GiNaC list. 

I've reported a new ticket (#9947). I let you report it on the GiNaC list.

Paul


---

Comment by burcin created at 2010-09-24 11:14:50

Changing keywords from "" to "pynac".


---

Comment by burcin created at 2010-09-24 11:14:50

Replying to [comment:4 zimmerma]:
> Burcin,
> 
> > We should open a new ticket for this and report it on the GiNaC list. 
> 
> I've reported a new ticket (#9947). I let you report it on the GiNaC list.

This issue was fixed upstream by Richard Kreckel.

While the fix makes the original example on this ticket work, Jason's example from comment:1 or the one reported by Tian Wei on sage-support (below) still don't work.


```
sage: b = sqrt(-log(2))
sage: print b.imag().n()
0.832554611157698*sin(0.500000000000000*pi)
```



---

Attachment


---

Comment by burcin created at 2010-10-10 19:55:47

I uploaded a patch to fix this. The problem wasn't in pynac after all, it was the numeric approximation function for `arctan2()`.


---

Comment by burcin created at 2010-10-10 19:55:47

Changing keywords from "pynac" to "".


---

Comment by burcin created at 2010-10-10 19:55:47

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-10-11 07:17:41

positive review, good work Burcin!

Paul


---

Comment by zimmerma created at 2010-10-11 07:17:41

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-01 10:12:30

Resolution: fixed
