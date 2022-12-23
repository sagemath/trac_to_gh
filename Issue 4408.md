# Issue 4408: magma interface -- change _magma_init_ to take non-optional magma argument

Issue created by migration from https://trac.sagemath.org/ticket/4408

Original creator: was

Original creation time: 2008-10-31 01:50:04

Assignee: was

This patch touches a lot of files in a trivial automatic way.  They main point is it changes the _magma_init_ signature from 

_magma_init_(self)

to 

_magma_init_(self, magma)

where magma is a magma interface.  Also, it introduces some caching for the magma interface itself.  This means that _magma_init_ has access to and can impact the full state of the magma interpreter.   This makes creating a string representation of an element valid for that interpreter dramatically more powerful and flexible, is conceptually very easy to understand, and works.  The caching helps mediate potential efficiency issues. 

Note, whether caching should be on or off by default is unclear, and I think can only be answered by implementing a lot more of this framework and doing some profiling. 


---

Attachment


---

Comment by was created at 2008-11-04 05:07:29

I've decided caching is not the default, since I don't want to blatantly introduce memory leaks. The second patch implements this change (one line change), plus changes all _magma_init_()'s to appropriate _magma_init_(magma).


---

Attachment


---

Attachment


---

Comment by was created at 2008-11-24 03:37:37

Resolution: invalid


---

Comment by was created at 2008-11-24 03:37:37

I've decided this approach with caching is the wrong design since it would introduce memory leaks.  I'm closing this ticket/approach as invalid, and opening a new one, which
implements related ideas and gets it right.  See #4601.
