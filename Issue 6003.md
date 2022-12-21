# Issue 6003: Additions to Cholesky decomposition

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-05-07 19:07:39

Assignee: rbeezer

CC:  ncalexan

These are enhancements to #5554, which have been split off here.  Numbering is the same.  See #5554 for more details

2.  Make a positive-definite check the default, with a keyword to turn it off.

3.  Minor improvements to the docstrings.

4.  Warnings about accuracy for generic algorithm.


---

Comment by dsm created at 2012-05-27 23:12:16

Is this still valid given the positively reviewed #13035 and the pending #11274?


---

Comment by rbeezer created at 2012-08-21 17:55:08

Changing status from new to needs_review.


---

Comment by rbeezer created at 2012-08-21 17:55:08

Thanks, Doug.  Yes I think this has exceeded its shelf-life.  The referenced tickets (and maybe one or two others) basically put Cholesky decomposition on a firm footing again.

I'll try to put this into the right status to get Jeroen's attention.

*Release Manager*

This can be safely marked "wontfix" or made obsolete in some other way.  Thanks.


---

Comment by rbeezer created at 2012-08-21 17:55:53

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-22 09:48:08

Replying to [comment:2 rbeezer]:
> Thanks, Doug.  Yes I think this has exceeded its shelf-life.  The referenced tickets (and maybe one or two others) basically put Cholesky decomposition on a firm footing again.
> 
> I'll try to put this into the right status to get Jeroen's attention.
Just for your information: it's better to also change the milestone the sage-duplicate/invalid/wontfix.


---

Comment by jdemeyer created at 2012-09-05 09:39:38

Resolution: worksforme
