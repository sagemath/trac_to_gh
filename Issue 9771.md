# Issue 9771: unify doctest commands, especially for 'long' and 'parallel' options

Issue created by migration from https://trac.sagemath.org/ticket/9772

Original creator: niles

Original creation time: 2010-08-20 18:12:45

Assignee: mvngu

Make sure that the commands for doctesting the entire Sage library test the same files, in particular when including `long` and `parallel` options.


From William, at

http://ask.sagemath.org/question/35/does-sage-testall-test-long-doctests

Looking at `SAGE_ROOT/local/bin/sage-sage` we see that `sage -testall` calls the script `sage-maketest` which passes all of its options on to `sage -t`. [and thus cannot handle a parallel option]


If you look in `SAGEROOT/makefile` you'll see that `make test` just calls `sage-maketest`. Note that `make testlong` on the other hand has a specific list of directories it tests, defined in `SAGEROOT/makefile`. Right now they match the list in `SAGE_ROOT/local/bin/sage-maketest`. However, if these ever get out of sync, bad things will happen in that `make test` and `make testlong` would suddenly test different code.


---

Comment by kcrisman created at 2010-08-24 13:28:03

In fact, there should be a very easy way to to -ptestall or something.


---

Comment by jdemeyer created at 2013-02-28 16:11:06

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-02-28 16:11:06

Superseded by #12415.


---

Comment by jdemeyer created at 2013-02-28 16:11:16

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-07 08:18:49

Resolution: duplicate
