# Issue 9784: Simple Server API - wrong cell results

Issue created by migration from https://trac.sagemath.org/ticket/9785

Original creator: dpoetzsch

Original creation time: 2010-08-23 10:45:49

Assignee: jason, was

CC:  jason

Using the Simple Server API I tried the following (after logging in of course):

At first I sent the code "`sleep(10);5`" to the server using the following URL:
`http://localhost:port/simple/compute?session=theID&code=sleep(10)%3B5`

Then, immediatly afterwards (this means command one was still computing) I sent the code "`4+5`" to the server using the URL
`http://localhost:port/simple/compute?session=theID&code=4%2B5`

Then, after 10 seconds, I looked at the results of both commands using
`http://localhost:port/simple/status?session=theID&cell=2`
and
`http://localhost:port/simple/status?session=theID&cell=3`

Both cells had `5` as result, which should be only the result of the first
cell.


---

Attachment

This fixes the problem for me.


---

Comment by kcrisman created at 2013-06-14 17:10:34

Sadly, the simple server does not work with the current notebook, and the [Sage cell server](https://github.com/sagemath/sagecell) has more or less superseded it.


---

Comment by kcrisman created at 2013-06-14 17:10:34

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-06-14 17:11:06

Although we'll close this, I hope the code here will someday prove useful, though!


---

Comment by kcrisman created at 2013-06-14 17:11:06

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-06-14 18:36:45

Changing status from positive_review to needs_info.


---

Comment by kcrisman created at 2013-06-14 18:36:45

Note that #11409 would remove this completely.


---

Comment by kcrisman created at 2014-09-17 02:26:00

This has now been removed.


---

Comment by kcrisman created at 2014-09-17 02:26:00

Changing status from needs_info to positive_review.


---

Comment by vbraun created at 2014-09-18 17:59:16

Resolution: wontfix
