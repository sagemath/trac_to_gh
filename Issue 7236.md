# Issue 7236: Partitions cleanup (box => cell + indentation fix)

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-10-17 20:38:04

Assignee: hivert

CC:  sage-combinat

Keywords: partitions cell

After a vote on `sage-combinat-devel`, see

```
http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/bd6dd9b316236f91
```

it was decided that in a partition diagramm a square should be called a cell. The following patch implement this choice.

I also take the occasion to fix an indentation problem which prevents some doc to be correctly typeset.

Cheers,

Florent


---

Comment by hivert created at 2009-10-17 20:40:54

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-10-18 07:32:05

Changing keywords from "partitions cell" to "partitions cell, leg, arm, hook".


---

Comment by nthiery created at 2009-10-18 07:32:05

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2009-10-18 07:32:05

I just reviewed your patch. Positive review up to the following points:

 - Specify in the definition of leg that this is in English notation
 - Add deprecation hooks for all renamed methods


---

Attachment


---

Comment by hivert created at 2009-10-18 15:23:03

I just uploaded a new patch with the required backward compatibility hooks and deprecation warnings. It is ready to review. 

Cheers,

Florent


---

Comment by hivert created at 2009-10-18 15:23:58

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2009-10-18 21:31:24

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2009-10-18 21:31:24

Thanks Florent. The test pass with 4.1.1 and a couple other patches applied. Positive review, assuming they pass smoothly on the current 4.2 ???

Florent: making a quick grep, I noticed that in sf/ns_macdonald.py, the LatticeDiagram uses the same old conventions as Partitions (box, leg, arm, ...). I let you decide if you want to fix this now as part of this ticket, or postpone to a later ticket.


---

Comment by mhansen created at 2009-10-19 05:44:55

I think it can be another ticket.  I'm going to write a "decorator" to make deprecated aliases easier.  So, we'd just do "boxes = deprecated_method_alias(cells)".


---

Comment by mhansen created at 2009-10-19 05:49:09

Resolution: fixed


---

Comment by nthiery created at 2009-10-19 09:21:17

Replying to [comment:6 mhansen]:
> I think it can be another ticket.

Ok. Thanks for merging it!

> I'm going to write a "decorator" to make deprecated aliases easier.  So, we'd just do "boxes = deprecated_method_alias(cells)".

+1!!!
