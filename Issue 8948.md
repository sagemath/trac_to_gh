# Issue 8948: add thin space between vector entries

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-05-11 06:29:05

Assignee: jason, was

CC:  rbeezer

This patch adds a thin space between vector entries, which helps distinguish the entries from each other, especially when there are symbolic expressions, so the entries already may have thin spaces in them.


---

Attachment


---

Comment by jason created at 2011-01-18 17:02:33

Rob, you might be interested in this slight improvement to linear algebra latexing.

Maybe this ticket only needs a doctest to be ready for review?


---

Comment by jason created at 2011-01-18 17:02:33

Changing status from new to needs_work.


---

Comment by rbeezer created at 2011-01-21 05:10:51

Yep, code looks good.  I _always_ put a thin space into my vectors, so this will be nice to have automatically.  Doctests are updated, made two necessary fixes in the symbolic-callable tests.  Running tests right now and will report back.


---

Attachment

Attachment is totally doctests that needed fixing, plus one new one.  No change to the code.  I'm fine with a positive review on the code once somebody checks my doctest changes.


---

Comment by rbeezer created at 2011-01-23 04:37:45

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2011-01-23 05:56:53

Doctests changes looks good, I also think that it will be a nice improvement!


---

Comment by novoselt created at 2011-01-23 05:56:53

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-26 22:26:33

Resolution: fixed
