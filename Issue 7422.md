# Issue 7422: New Incidence Structure and Block Design constructions

Issue created by migration from https://trac.sagemath.org/ticket/7422

Original creator: brett

Original creation time: 2009-11-10 02:09:23

Assignee: mhansen

CC:  rbeezer wdj

Keywords: Block Design, Incidence Structure, Residual, Derived, Complement, Supplement, Point Deletion

I have added two references; fixed the points() method to return points in lexicographic order so __eq__ works properly; made is_simple() its own standalone method and call it from block_design_checker and added the following constructions: Derived at a Point, Residual at a Point, Derived at a Block, Residual at a Block, Complementary, Supplementary, Point Deletion and Extraction of Blocks by size.

Some relevant discussion is here:

http://groups.google.com/group/sage-devel/browse_thread/thread/305158ab5d3181bc

Reviewers:

- Please think about my first item on the TODO list; is that a better way to proceed with derived_blck and residual_blck?

-I do not know whether this is "Minor" or "Major" (I am pretty sure it is not the others) so I have put "Major".  Please tell me if I was wrong.

- I have no idea what to put in Milestone so I have left it blank.


---

Comment by brett created at 2009-11-10 02:20:56

Changing status from new to needs_review.


---

Comment by jason created at 2009-11-10 15:09:24

Just a python and Sage style note: unless there is a huge significant reason, things in function names should be spelled out.  So, for example, residual_pt should be residual_point, blck should be "block", etc.  This makes a huge difference in readability for someone that is using the module, reading code written by others, etc.


---

Comment by brett created at 2009-11-10 17:04:46

Replying to [comment:2 jason]:
> Just a python and Sage style note: unless there is a huge significant reason, things in function names should be spelled out.  So, for example, residual_pt should be residual_point, blck should be "block", etc.  This makes a huge difference in readability for someone that is using the module, reading code written by others, etc.


OK, I will make this change, thanks.


---

Attachment

Patch with new constructions


---

Comment by brett created at 2009-11-14 18:45:58

I have changed the function names so they are all fully descriptive of what they do.

I also have a question.  When I run:

sage -coverage Projects/SAGE/sage-source/devel/sage/sage/combinat/designs/incidence_structures.py

I do get 100% coverage but I also get:

ERROR: Please add a `TestSuite(s).run()` doctest.

I have looked in the sage reference manual and the developers guide to see what this is and how I add such a thing, but to no avail.  If someone knows what this is please tell me or send a link to a page that describes it.  When I know what to do, I will add one of these.


---

Comment by jason created at 2009-11-14 19:02:39

Here is the patch for adding such a thing to matrices in Sage.  You might find the code useful as an example.

#6936

Here is the ticket that introduced the framework:

#6343

I don't know where this is documented, but there probably is a mailing list message or two about it.


---

Comment by drkirkby created at 2010-02-21 23:39:49

Remove assignee mhansen.


---

Comment by drkirkby created at 2010-02-21 23:39:49

Has this been checked on Solaris?

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by ncohen created at 2010-05-16 16:55:37

I do not know if this patch is still necessary, but if it is it needs to be rebased.


```
12 out of 12 hunks FAILED -- saving rejects to file sage/combinat/designs/incidence_structures.py.rej
```


Nathann


---

Comment by ncohen created at 2010-05-16 16:55:37

Changing status from needs_review to needs_work.


---

Comment by brett created at 2015-03-10 02:33:07

Set assignee to brett.


---

Comment by ncohen created at 2015-03-10 15:17:32

`@`brett: here is [1] the procedure to follow if you want to close this ticket. Note that while the doc says that you should switch it to 'needs review'first, we usually directly change the status to 'positive review' in this specific case.

Nathann

[1] http://www.sagemath.org/doc/developer/trac.html#reviewing-and-closing-tickets


---

Comment by brett created at 2015-03-10 15:20:26

This ticket should be closed.  It has been superseded by ticket #16534


---

Comment by brett created at 2015-03-10 15:20:48

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2015-03-12 23:51:41

you should also set the milestone to duplicate...


---

Comment by vbraun created at 2015-03-12 23:51:52

Resolution: duplicate


---

Comment by brett created at 2015-03-13 03:49:35

thanks
