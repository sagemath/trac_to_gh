# Issue 9642: sage-maketest and sage-test-new should be able to run tests in parallel

Issue created by migration from https://trac.sagemath.org/ticket/9642

Original creator: mpatel

Original creation time: 2010-07-29 22:46:39

Assignee: mvngu

CC:  kcrisman

Reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/efae2db905b3ee8f/1a2312f22bc40d9a#1a2312f22bc40d9a) by K.-D. Crisman:

```
Subject: can sage -testall use threads?

That is, without setting NUM_THREADS or something.  I tried

./sage -testall -p 8

but I just get lots of error messages in addition to my test output.
I guess I have the same question about sage -tnew as well.
```


Somewhat related: #279


---

Comment by mpatel created at 2010-07-29 22:49:44

It seems the `sage -testall` and `sage -tnew` operators invoke `SAGE_LOCAL/bin/sage-maketest` and `sage-test-new`, respectively.  To run the tests, both scripts use `sage -t`, which calls the serial doctest runner `sage-test`.  Moreover, `sage-test-new` does not pass along command-line arguments.


---

Comment by roed created at 2013-03-14 20:39:39

This is resolved by #12415.


---

Comment by roed created at 2013-03-14 20:39:39

Changing status from new to needs_review.


---

Comment by roed created at 2013-03-14 20:39:53

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-15 13:00:58

Resolution: duplicate
