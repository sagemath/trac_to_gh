# Issue 5859: sage -coverageall fails on directories with zero tests

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-22 23:31:00

Assignee: mabshoff

CC:  mjo


```
./sage -coverageall devel/sage/sage/catalogue/
```

results in

```
Traceback (most recent call last):
  File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/sage-coverageall", line 44, in <module>
    coverage_all(sys.argv[1])
  File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/sage-coverageall", line 28, in coverage_all
    score = (float(scr) / total)
ZeroDivisionError: float division
```



---

Comment by mjo created at 2012-01-09 05:00:53

Default to 100% coverage when there are no tests.


---

Comment by mjo created at 2012-01-09 05:03:05

Changing status from new to needs_review.


---

Attachment

This was a pretty small fix, so there it is.

The coverage score would naturally be undefined, but saying it's 100% of zero is a useful fiction in this case.


---

Comment by aapitzsch created at 2012-04-29 17:12:45

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-01 05:07:45

Resolution: fixed
