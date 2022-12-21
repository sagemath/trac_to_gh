# Issue 9910: Changing the LP formulation of feedback vertex/arc set to improve the speed

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-09-14 20:59:42

Assignee: jason, ncohen, rlm

CC:  abmasse mvngu

A friend of mine had the good idea to think about the MFAS problem one evening, and told me that the LP formulation given in GLPK's examples was able to return the optimal value of a particular problem in 8ms. It took more (I did not wait) than 2 minutes for Sage.

I looked at the two formulations, and they were so clode that I still do not understand why the second one is faster. I will think about it for a while, though I can already write the corresponding patch `:-)`

Nathann


---

Comment by ncohen created at 2010-09-15 17:09:42

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-10-23 16:21:51

Patch rebased on top of #10151

Nathann


---

Comment by abmasse created at 2010-11-14 03:40:57

Hi Nathann !

A question and a remark:

  1. If I understand correctly, your ticket is improving the speed of the minimum feedback vertex/arc set problems by providing another LP formulation. Could you detail where you took the first formulation (I assume you're the one who coded it) and where you got the new one? This could help in the review process to compare and make sure the two methods are equivalent.
  1. I a bunch of lines where lists are created without being used, such as in:

```
[p.add_constraint(d[v],min=n) for v in self]
```

  Wouldn't it be better to replace it with a loop?

```
for v in self: p.add_constraint(d[v], min=n)
```

  I think it's useless to create a list that will be thrown to the garbage collector right away :) Moreover, the number of characters is exactly the same, so it's not a waste of space :)


---

Comment by abmasse created at 2010-11-14 03:40:57

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2010-11-16 07:10:31

Hello !!!

You are totally right about these lists.. That's just how I coded LP at first, but it wasn't a good idea after all. You will find the "modern LP code" easier to read `:-D`

About the formulations... Well, the first one was just the one I came up with when I first wanted to solve MFAS problems, and the other one was given to me by a friend who was reading glpk's examples. You will find this file there :

http://stuff.mit.edu/afs/athena/software/glpk/examples/mfasp.mod

Note that even though the speed improvement is great, I wrote #9923 some time later and wondered whether I should remove this patch because of it : there is no comparison possible between this LP formulation and #9923, which will be (when it will be merged) the default way to solve MFAS problems. This formulation will just stay as a backup, or to check both algorithms' correctness (unless people do not want it of course, but that's what I had in mind when writing #9923)...

(patch updated)

Nathann


---

Comment by ncohen created at 2010-11-16 07:10:31

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2011-01-12 01:42:33

Changing status from needs_review to needs_work.


---

Attachment

You're still using the list syntax for constraint addition loops at the end of the patch:

```
[p.add_constraint(d[u]-d[v]+n*(b[u]+b[v]),min=1) for (u,v) in self.edges(labels=None)] 
[p.add_constraint(d[u],max=n) for u in self]
```


Other than that, this patch looks good. All long tests pass against sage-4.6.1.rc1 and I'm otherwise happy. Fix the one issue, ping me and I'll set this to positive review.


---

Comment by gbe created at 2011-01-12 01:56:32

Added a small patch fixing the last two list comprehension liness.


---

Attachment


---

Comment by rlm created at 2011-01-12 03:01:36

Thank you!


---

Comment by rlm created at 2011-01-12 03:01:36

Changing status from needs_work to positive_review.


---

Comment by ncohen created at 2011-01-12 08:44:29

Thanksssssss !! `:-)`


---

Comment by jdemeyer created at 2011-01-19 22:21:56

Resolution: fixed
