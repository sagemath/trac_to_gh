# Issue 8956: Fix notebook help on auto-evaluation

Issue created by migration from https://trac.sagemath.org/ticket/8956

Original creator: kcrisman

Original creation time: 2010-05-12 15:45:09

Assignee: jason, was

CC:  jdemeyer

Keywords: autoevaluate, auto-evaluate

Apparently, #auto should be %auto now.  But the help page for the notebook doesn't say so.  As far as I can tell, both work?


---

Comment by mhansen created at 2010-05-12 16:13:19

Yes, there is code in the notebook to explicitly allow #auto, but %auto is preferred since it matches up with the other cell directives.


---

Comment by jason created at 2010-05-12 16:57:18

See #7002 for a fix that you made 8 months ago :).


---

Comment by kcrisman created at 2010-05-12 17:04:10

Annoying.  Would it be pretty easy for someone with access to the notebook code (i.e. not me) to just rebase that patch to SageNB?  Aargh.


---

Comment by kcrisman created at 2011-06-20 15:43:09

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-20 15:43:09

Okay, it turns out that this was finally merged in #7002 very recently.  Hooray!

To release manager: this can be closed.


---

Comment by kcrisman created at 2011-06-20 15:43:18

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-20 18:53:53

Resolution: duplicate
