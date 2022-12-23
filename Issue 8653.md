# Issue 8653: Command-line "advanced" help has wrong option name for randomized tests

Issue created by migration from https://trac.sagemath.org/ticket/8653

Original creator: rbeezer

Original creation time: 2010-04-06 05:58:27

Assignee: mvngu

`sage -h` says  `sage -t -randorder <files>` will do doctests in a random order and this is correct,

but `sage -advanced` says `sage -t -rand <files>` will do the job, and this is incorrect

Upcoming patch (to apply at the local/bin repo) corrects the advanced usage message.


---

Comment by rbeezer created at 2010-04-06 06:02:03

Changing status from new to needs_review.


---

Attachment


---

Comment by timdumol created at 2010-04-18 08:29:41

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-04-18 08:29:41

Works as advertised. Positive review.


---

Comment by jhpalmieri created at 2010-04-19 05:20:24

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-19 05:20:24

Merged into 4.4.alpha1.
