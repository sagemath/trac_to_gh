# Issue 7803: DeprecationWarning: the sets module is deprecated

Issue created by migration from Trac.

Original creator: cschwan

Original creation time: 2010-01-01 12:24:11

Assignee: GeorgSWeber

CC:  sage-combinat

Keywords: warnings

I read this warning everytime I start Sage, so I have prepared a simple patch which replaces "Set" with the built-in type set. The patch must be applied inside sage-4.3.spkg and changes the file sage/combinat/matrices/latin.py.

I should mention that I did not built Sage from Sage's makefile alone but from a gentoo ebuild written by myself - using upstream Sage does not yield this warning. Anyway, since "sets" was deprecated since Python 2.6 this should be fixed.


---

Attachment


---

Comment by nthiery created at 2010-02-16 16:20:08

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-02-16 16:20:08

The patch looks good to me. I'll try to launch the doctests shortly, but if someone beats me to it, and finds no issue, feel free to put a positive review.


---

Comment by novoselt created at 2010-04-17 23:43:07

I cannot apply this patch, I get the following:


```
novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7803/sage-4.3-fix-deprecation-warning.patch
adding sage-4.3-fix-deprecation-warning.patch to series file
novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qpush
applying sage-4.3-fix-deprecation-warning.patch
unable to find 'combinat/matrices/latin.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file combinat/matrices/latin.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh sage-4.3-fix-deprecation-warning.patch

```


I checked that the file is actually still there (and the above commands work fine for other patches).

Also, it seems that there is no user information and commit message with the ticket number in the patch file.


---

Comment by novoselt created at 2010-04-17 23:43:07

Changing status from needs_review to needs_work.


---

Comment by cschwan created at 2010-04-18 09:17:04

Replying to [comment:3 novoselt]:
> I cannot apply this patch, I get the following:
> 
> {{{
> novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7803/sage-4.3-fix-deprecation-warning.patch
> adding sage-4.3-fix-deprecation-warning.patch to series file
> novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qpush
> applying sage-4.3-fix-deprecation-warning.patch
> unable to find 'combinat/matrices/latin.py' for patching
> 3 out of 3 hunks FAILED -- saving rejects to file combinat/matrices/latin.py.rej
> patch failed, unable to continue (try -v)
> patch failed, rejects left in working dir
> errors during apply, please fix and refresh sage-4.3-fix-deprecation-warning.patch
> 
> }}}
> 
> I checked that the file is actually still there (and the above commands work fine for other patches).

The command fails because the patch was not generated with mercurials diff command (at the time I reported I did not know that you had to use mercurial for generating patches). So the command works if you use the standard patch command: patch < patchfile.patch - which course overwrites the original files. I will upload an hg-ified patch later.

I can also clarify the need of this patch: If one updates ipython and runs testcases without this patch a lot of testcases will fail because python now prints deprecation warnings.

> 
> Also, it seems that there is no user information and commit message with the ticket number in the patch file.


---

Comment by novoselt created at 2010-05-21 16:44:15

Changing status from needs_work to needs_review.


---

Attachment

Making new attachments does not create "ticket update" messages, so I didn't know that a new version is added. As I understand, this is now ready for review, so I'll go ahead and change the status.


---

Comment by novoselt created at 2010-05-21 16:47:04

While I do not see waring messages anyway, the changes are transparent and are for the good. All doctests pass with 4.4.2.


---

Comment by novoselt created at 2010-05-21 16:47:04

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 08:33:46

Resolution: fixed
