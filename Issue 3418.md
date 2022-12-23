# Issue 3418: added new combinatorial functions for tableaux and crystals

Issue created by migration from https://trac.sagemath.org/ticket/3418

Original creator: aschilling

Original creation time: 2008-06-13 18:30:06

Assignee: Mike Hansen

CC:  sage-combinat

Keywords: promotion; reflection

I added a two new functions 
promotion and promotion_inverse
for rectangular tableaux.

I also added a reflection operator
for the crystal library.


---

Attachment


---

Comment by mhansen created at 2008-06-13 18:50:38

Hi Anne,

The one thing I would change is that instead of returning the string "Tableaux is not rectangular" is raising a ValueError with that message.  Also, could you add a line before "EXAMPLES" in "def s("?

Other than that, it looks good to go in.

--Mike


---

Comment by mhansen created at 2008-06-13 18:59:00

Oh, the doctest for the ValueError would look something like this:


```
sage: t = Tableau([[1,2],[2]]) 
sage: t.promotion(3) 
Traceback (most recent call last):
...
ValueError: Tableaux is not recutangular

```



---

Comment by aschilling created at 2008-06-13 19:43:06

fixed the issues that Mike raised


---

Attachment


---

Comment by mabshoff created at 2008-06-15 22:27:13

Resolution: fixed


---

Comment by mabshoff created at 2008-06-15 22:27:13

Merged promotion_reflection-3418-submitted.patch in Sage 3.0.3.rc0
