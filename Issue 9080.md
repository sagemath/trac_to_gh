# Issue 9080: add F-distribution support for RealDistribution

Issue created by migration from Trac.

Original creator: klee

Original creation time: 2010-05-29 03:54:56

Assignee: amhou

add the F-distribution to the supported distributions for RealDistribution


---

Attachment

The patch adds F-distribution.


---

Comment by klee created at 2010-05-29 03:59:00

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-09-21 20:08:49

You may want to rebase this against 4.6.alpha1 if necessary.  Also, the commit message should start with `Trac 9080` or something like that.  Finally, maybe the error message should say that this is not a supported distribution?  It's certainly conceivable that there would be one in the literature which isn't yet in Sage or GSL :)


---

Comment by kcrisman created at 2010-09-21 20:08:49

Changing status from needs_review to needs_work.


---

Comment by klee created at 2010-09-25 01:23:07

Changing status from needs_work to needs_review.


---

Comment by klee created at 2010-09-25 01:23:07

I rebased the patch to the latest release of Sage (4.5.3). It was fun (and sad...) to see all different flavors of the heads of the commit messages used by developers. I followed the one DEMANDED by the developer manual. I changed all the error message as suggested.


---

Comment by klee created at 2010-09-25 01:32:37

revised according to the reviewer's comments


---

Attachment

There is a slight inconsistency even in the developer manual. In the section "Producing Patches with Mercurial", "trac xxxx: ..." is suggested while "Trac xxxx: ..." seems to be the official standard.


---

Comment by kcrisman created at 2010-09-25 17:00:58

Replying to [comment:4 klee]:
> There is a slight inconsistency even in the developer manual. In the section "Producing Patches with Mercurial", "trac xxxx: ..." is suggested while "Trac xxxx: ..." seems to be the official standard.
You could ask on sage-devel about this - for me, it's not so crucial, but mvngu might have an informed opinion.


---

Attachment


---

Comment by kcrisman created at 2011-06-17 00:51:09

I've rebased this against 4.7.1.alpha2.


---

Comment by kcrisman created at 2011-06-17 00:58:20

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-06-17 00:58:20

Positive review.   Gives correct values, checked with Wolfram Alpha.  Not surprising, since GSL is a very stable library.

But we need a lot more doctests for just about all of these - see #11514.


---

Comment by jdemeyer created at 2011-07-22 12:49:00

Resolution: fixed
