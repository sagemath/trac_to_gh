# Issue 9897: Clean up and add functions to sage/libs/pari/decl.pxi

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-09-11 13:24:02

Assignee: was

CC:  leif

* Add a file `sage/libs/pari/declinl.pxi` for declarations of inline functions.
 * Some clean up of `sage/libs/pari/decl.pxi`, in particular removing duplicate functions


---

Comment by jdemeyer created at 2010-09-12 09:37:04

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-12 13:18:57

s/seperate/separate/

s/This files/This file/


---

Comment by jdemeyer created at 2010-09-16 17:13:19

Replying to [comment:3 leif]:
> s/seperate/separate/
> 
> s/This files/This file/

Done.


---

Comment by leif created at 2010-09-19 20:24:15

Did you upload the wrong patch?

I just noticed the typos are back...


---

Comment by leif created at 2010-09-19 20:44:11

The `global t0` in `gequal_long()` is superfluous.


---

Attachment

Done.


---

Comment by leif created at 2010-09-20 14:45:54

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-20 14:45:54

Ok, I've now also tested this with Sage 4.6.alpha1 and #9876 (PARI 2.4.3.svn-12577.p7) on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64 (both `ptestlong`).

Patch is up-to-date, so positive review.

I've (of course?) not checked if all functions really come from the PARI source files they're claimed to come from. ;-)

It's up to you to convince Mitesh to merge it into 4.6.alpha2. :)


---

Comment by leif created at 2010-09-26 14:35:03

Perhaps one should mention that `pari/declinl.pxi` gets included by `pari/decl.pxi`.

Add svn snapshot number?


---

Comment by jdemeyer created at 2010-09-26 17:05:44

Adds authors to files in sage/libs/pari, apply on top of 9898_pari_decl.patch


---

Attachment

Replying to [comment:10 leif]:
> Perhaps one should mention that `pari/declinl.pxi` gets included by `pari/decl.pxi`.
Done.

> Add svn snapshot number?
I don't think that is so relevant (those files would not look that much different for other SVN snapshot numbers). Besides, people can still look at the ticket #9343 for more information.


---

Comment by leif created at 2010-09-26 17:54:22

Replying to [comment:11 jdemeyer]:
> [...] people can still look at the ticket #9343 for more information.

:-)

Btw, is [08-15](http://en.wikipedia.org/wiki/08/15) a [_symbolic_](http://de.wikipedia.org/wiki/08/15_%28Redewendung%29) date?

Positive review for the second patch, too.


---

Comment by mpatel created at 2010-09-28 10:55:45

Resolution: fixed
