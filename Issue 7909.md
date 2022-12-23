# Issue 7909: Replace $MKDIR with 'mkdir' in sage-spkg

Issue created by migration from https://trac.sagemath.org/ticket/7909

Original creator: drkirkby

Original creation time: 2010-01-12 16:15:32

Assignee: GeorgSWeber

CC:  jsp

sage-env has $MKDIR in one place, which will cause problems with an updated 'sage-env' which no longer defines MKDIR. 

I'm attaching a copy of the revised sage-env, and also a Mercurial patch.


---

Attachment

A complete copy of the revised sage-env


---

Comment by drkirkby created at 2010-01-12 16:21:53

Mercurial patch for sage-env


---

Attachment


---

Comment by drkirkby created at 2010-01-12 16:22:15

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-12 16:48:09

Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?

The patch is simple and looks good.


Jaap


---

Comment by jsp created at 2010-01-12 17:25:06

Replying to [comment:2 jsp]:
> Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?
> 
> The patch is simple and looks good.
> 
> 
> Jaap
> 

It is really in sage-spkg!!  I changed the description.

Waiting for the mercurial patch.

Jaap


---

Comment by jsp created at 2010-01-12 17:30:30

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-12 17:30:30

The "mercurial patch" is ok. sage-spkg looks good. So positive review.

Jaap


---

Comment by rlm created at 2010-01-14 03:03:07

Resolution: fixed
