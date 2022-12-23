# Issue 2356: Bug in discrete_log_generic

Issue created by migration from https://trac.sagemath.org/ticket/2356

Original creator: cremona

Original creation time: 2008-02-29 21:41:10

Assignee: joyner

CC:  marshbuck@gmail.com

Marshall Buck reports (email to sage-support 2008-02-29):

Problem 1.  Fails because the list sizes in the baby step giant step
method are too small.

Example. [NB This particular example does *not* fail with 2.10.2]


```
F.<w> = GF(121)
v = w^120
v.log(w)
```

bombs with:

```
File "/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/
arith.py", line 2164, in discrete_log_generic
   raise ValueError, "Log of %s to the base %s does not exist."%(a,b)
ValueError: Log of 2*w + 10 to the base w does not exist.
```

This can be fixed by changing the append loop to make "g"  to {{{range(m
+1)}}} instead of `range(m)`.  This makes g m+2 long and S2 m-long.  Then {{{(m
+2)*m >= ord}}}.


```
   m = ord.isqrt()
   g = [a]
   c = b**(-m)
   S2 = [1]
   for i in range(m+1):  # suggested line change   ---  was range(m)
       g.append(g[i]*c)
       if i < m-1:
           S2.append(S2[i]*b)
   for y in g:
       if y in S2:
           x = S2.index(y)
           return Z(m*(g.index(y)) + x)
```


2. The other problem is the inefficiency in the lookup " {{{for y in g:
if y in S2:}}} ".  The work is proportional to  "ord", insead of
proportional to  "m" as intended by BSGS method.  It is quicker to do
a set lookup:


```
 S2set = set(S2)
 for y in g:
     if y in S2set:
         x = S2.index(y)...
```


----

Coments by John Cremona:

1. Note that this is related to #277

2. I already suggested using a dict for the lookup instead of using lists or sets

I will post a patch.



---

Attachment

Attached patch 8682 fixes both issues:  increases m by 1 and uses a dict() for fast lookup of the table.


---

Comment by cremona created at 2008-03-02 17:35:26

Changing status from new to assigned.


---

Comment by cremona created at 2008-03-02 17:35:26

Changing assignee from joyner to cremona.


---

Comment by wdj created at 2008-03-02 19:07:05

Applied cleanly to 2.10.3.rc0 and passed sage -testall. Also,


```
sage: F.<w> = GF(121)
sage: v = w^120
sage: v.log(w)
0
```

works as it should. Recommend acceptance.


---

Comment by cremona created at 2008-03-04 18:04:02

The two new patches to #2356 -- which have a positive review! -- need to be applied after this one.  They do in fact supercede this one, there therefore this one gets another positive review by default.  I'm sure I am breaking protocol by adding that myself but seriously!


---

Comment by mabshoff created at 2008-03-04 18:24:47

Replying to [comment:4 cremona]:
> The two new patches to #2356 -- which have a positive review! -- need to be applied after this one.  They do in fact supercede this one, there therefore this one gets another positive review by default.  I'm sure I am breaking protocol by adding that myself but seriously!

Hi John,

I assume you refer to the two patches at #277 instead of "The two new patches to #2356 -- which have a positive review!". The positive review is fine in this case and not a breaking of protocol - we shouldn't and don't enforce rules for the sake of rules :) 

I will merge both patches shortly and close the tickets assuming the patches apply.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-05 00:19:50

Merged both in Sage 2.10.3.rc2


---

Comment by mabshoff created at 2008-03-05 00:19:50

Resolution: fixed


---

Comment by mabshoff created at 2008-03-05 00:21:28

Merged the *only* patch in Sage 2.10.3.rc2 - sorry for the confusion - I meant ticket #277.
