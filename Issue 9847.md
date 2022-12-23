# Issue 9847: 'sage -advanced' does not mention the '-R' flag, which starts the R interpreter

Issue created by migration from https://trac.sagemath.org/ticket/9848

Original creator: mpatel

Original creation time: 2010-09-01 09:51:49

Assignee: was

CC:  kcrisman

To run the copy of R bundled with Sage, we can use `sage -R`, but this option is not documented in the help message returned by `sage -advanced`.

The relevant file is `SAGE_ROOT/local/bin/sage-sage`.


---

Comment by kcrisman created at 2010-09-01 12:56:22

Are there any other programs we can run in this way which are not on that list?  Gap, Pari, Maxima are all there...


---

Comment by kcrisman created at 2011-08-19 13:31:48

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-08-19 13:31:48

Huh, this was fixed at some point in the recent past.   At any rate, it is in the released 4.7.1.

```
  -maxima [...]       -- run Sage's Maxima with given arguments
  -mwrank [...]       -- run Sage's mwrank with given arguments
  -python [...]       -- run the Python interpreter
  -R [...]            -- run Sage's R with given arguments
  -scons [...]        -- run Sage's scons
```

In fact, it even shows up in `./sage -help`.


---

Comment by kcrisman created at 2011-08-19 13:34:50

This, along with a lot of other stuff, was added in #10326.


---

Comment by kcrisman created at 2011-08-19 13:34:50

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-08-22 08:08:30

Resolution: duplicate
