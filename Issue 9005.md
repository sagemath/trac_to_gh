# Issue 9005: Derangements

Issue created by migration from Trac.

Original creator: amca01

Original creation time: 2010-05-21 10:20:57

Assignee: sage-combinat

CC:  ncohen ppurka

Keywords: derangements

The current implementation in Sage for derangements is a wrapper for the GAP "derangements" and "number_of_derangements" which is very restrictive.  For example, it doesn't allow derangements of arbitrary lists or strings.  The documentation observes 

"Warning - Wraps GAP - hence mset must be a list of objects that have string representations that can be interpreted by the GAP interpreter. If mset consists of at all complicated Sage objects, this function does not do what you expect. A proper function should be written! (TODO!)" 

This file is an attempt to provide that.


---

Attachment


---

Comment by tscrim created at 2013-04-01 19:40:04

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-04-01 19:40:04

Converted the sage file into a patch and brought it up to our current standards. Ready for review.


---

Comment by bsalisbury1 created at 2013-04-18 17:36:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-23 13:18:32

The patch is not a proper patch file, patches should be generated using `hg export tip`.


---

Comment by jdemeyer created at 2013-04-23 13:18:32

Changing status from positive_review to needs_work.


---

Comment by tscrim created at 2013-04-23 15:16:47

Changing status from needs_work to positive_review.


---

Attachment

Sorry about that. Fixed.


---

Comment by jdemeyer created at 2013-04-28 10:32:09

Resolution: fixed
