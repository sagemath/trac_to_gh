# Issue 4838: implement plotting of complex numbers

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-12-20 16:47:25

Assignee: was

Keywords: plot complex number

It would be nice to be able to do:


```
sage: CC(3-2*I).plot()
```


which would return a plot object of the point 3-2*I.  I guess it just needs to wrap the normal plot of a point.


---

Comment by vdelecroix created at 2010-01-29 22:30:27

Changing status from new to needs_review.


---

Attachment


---

Attachment

use only this one !


---

Comment by rossk created at 2010-01-31 10:47:33

This works (so patch does its job as designed)

```
CC(1+I).plot() 
```


This currently doesnt work (because not part of this ticket) 

```
[CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)].plot()
```

(its a natural extension of the idea in this ticket, but will have to be a new ticket if anyone thinks its worth implementing)


---

Comment by rossk created at 2010-01-31 10:47:33

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2010-01-31 11:44:59

> This currently doesnt work (because not part of this ticket) 
> {{{
> [CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)].plot()
> }}}
> (its a natural extension of the idea in this ticket, but will have to be a new ticket if anyone thinks its worth implementing)  

BEWARE: It's not a good idea to implement this (and not even possible). To be able to do this the .plot() method have to be coded inside the list object which is a python object.

But remains the question on how do the following work ?

```
sage: z0 = CC(2,3)
sage: plot(z0)   # works with this patch
sage: z1 = 2 + 3*I
sage: plot(z1)  # does not work because z1 is in SR and not in CC
```


Most of the time users have to think about using `point` more than `plot` for complex numbers... and I'm not sure about the usefulness of this ticket...


---

Comment by mpatel created at 2010-02-10 15:24:07

The patch commit string is insufficiently descriptive.  I've refreshed it to
`#4838: Implement plotting of complex numbers` in the queue for 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 14:57:13

Resolution: fixed
