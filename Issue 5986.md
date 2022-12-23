# Issue 5986: [with patch, needs review] Workaround mishandled nested classes in Python and cPickle

Issue created by migration from https://trac.sagemath.org/ticket/5986

Original creator: nthiery

Original creation time: 2009-05-05 07:14:13

Assignee: nthiery

CC:  sage-combinat cwitty

Keywords: pickling, nested classes

With the python code below::
    class A:
        class B:
            pass
Python 2.6 erroneously set the B.__name__ to "B" instead of "A.B".

Furthermore, upon pickling (here in save_global)
*and* unpickling (in load_global) a class
with name "A.B" in a module mod, the standard
cPickle module searches for "A.B" in mod.__dict__
instead of looking up "A" and then "B" in the result.

This patch works around this by a patch to cPickle.c which fixes the
name for B to its appropriate value A.B, and inserts 'A.B' = A.B in
mod.__dict__ (hacky, but seems to work) the first time A.B is pickled,
and fixes load_global to implement a proper lookup upon unpickling.

It also ensures that sage/interfaces/sage0.py uses loads/dumps from
sage_object rather than calling directly cPickle.loads/dumps
(+1 by cwitty on this change)

Depends on #5483 and #5985


---

Attachment


---

Comment by nthiery created at 2009-05-18 03:10:18

Changing status from new to assigned.


---

Comment by robertwb created at 2009-05-22 23:06:51

This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121.


---

Comment by jason created at 2009-09-22 17:09:12

Replying to [comment:4 robertwb]:
> This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121. 

Does that mean that this ticket can be closed?


---

Comment by nthiery created at 2009-09-22 20:06:20

Replying to [comment:5 jason]:
> Replying to [comment:4 robertwb]:
> > This workaround it a bit to hackish for my taste, but it's been implemented and tested. Followup at #6121. 
> 
> Does that mean that this ticket can be closed?

Not before Robert or someone else writes a proof of concept patch upon the category code proving that #6121 is a usable replacement for this one to get pickling to work for parents and categories.
See discussion on Sage devel.


---

Attachment

Apply only this one


---

Comment by nthiery created at 2009-10-11 08:50:46

The newly attached patch implements a completely different fix, using #6110 and #6121.

William is ok integrating this in 4.1.2 if it's ready on time (see IRC).

Robert: please review! (unless you feel you should be an author, and get someone else to review it :-))


---

Comment by robertwb created at 2009-10-11 08:56:50

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-10-11 08:56:50

Much less intrusive--too bad we didn't pursue this just a bit more back in June.


---

Comment by mhansen created at 2009-10-15 07:05:19

Resolution: fixed
