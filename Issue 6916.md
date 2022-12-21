# Issue 6916: follow-up to #6749: fix warnings when building reference manual

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-10 11:59:26

Assignee: tbd

CC:  ncohen

As the subject says. This is a follow-up to ticket #6749.


---

Comment by mvngu created at 2009-09-10 17:44:04

Changing component from algebra to documentation.


---

Comment by mvngu created at 2009-09-10 17:44:04

Changing assignee from tbd to tba.


---

Comment by jhpalmieri created at 2009-09-29 21:55:43

I give it a positive review, too, but if you want to change the lines

```
    - ``seq`` -- Two different possible types: 
      - A sequence of pairs (weight, value). 
      - A sequence of reals (a value of 1 is assumed). 
```

by adding a blank line after the first one, it looks a little better (to me) when typeset.  I'll give that a positive review in advance, so if you want to make the change, no need for more review.


---

Attachment

based on Sage 4.1.2.alpha4


---

Comment by mvngu created at 2009-09-30 02:55:45

Replying to [comment:3 jhpalmieri]:
> I give it a positive review, too, but if you want to change the lines

```
    - ``seq`` -- Two different possible types: 
      - A sequence of pairs (weight, value). 
      - A sequence of reals (a value of 1 is assumed). 
```

> by adding a blank line after the first one, it looks a little better (to me) when typeset.
Done.


---

Comment by mvngu created at 2009-09-30 03:53:59

Resolution: fixed
