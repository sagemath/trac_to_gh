# Issue 9171: cygwin: some test failures in sagedoc.py

Issue created by migration from https://trac.sagemath.org/ticket/9171

Original creator: was

Original creation time: 2010-06-07 04:36:13

Assignee: tbd

CC:  jpflori


```

sage -t  "devel/sage/sage/misc/sagedoc.py"                  
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py", line 891:
    sage: len(search_doc('tree', interact=False).splitlines()) > 2000
Expected:
    True
Got:
    False
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/sagedoc.py", line 496:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    False

```



---

Comment by kcrisman created at 2010-08-02 13:59:42

I usually get these errors if the documentation isn't built.  Is that's what's going on here?


---

Comment by kcrisman created at 2011-08-02 02:30:18

I get the second failure, but not the first one, on a recent build on XP.


---

Comment by kcrisman created at 2011-08-19 14:51:04

I'm getting these failures by hand, though.   And I checked - the documentation is not automatically built.  So let's change this title.


---

Comment by kcrisman created at 2013-01-15 15:22:28

JP says that the doc does now build (since Maxima now works with #9167).


---

Comment by jpflori created at 2013-01-15 18:07:20

Yup the doc built fine for me and the test passes.
If you can reproduce that, let's close this ticket.


---

Comment by kcrisman created at 2013-01-17 03:58:47

This is really frustrating for me - I simply cannot build the doc, or (once again) even start Sage, even though it *just was working a few days ago*.  All the usual can't map foo.dll to the same address stuff.  I've rebased several times, no luck, though sometimes different files that can't map...

I'd like to try this again, though - yet another build from scratch, hopefully.  There is no rush to close this, after all, as there is no patch or spkg required.


---

Comment by jpflori created at 2013-01-30 10:44:17

I once again built the doc succesfully, so let's close this one.
I doubt XP/7 32bits/64bits will make any difference.


---

Comment by jpflori created at 2013-01-30 10:44:17

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-01-30 13:06:20

No, I think you are right.  Assuming one can get Sage to start reliably, this should now be okay.


---

Comment by jpflori created at 2013-01-30 13:10:15

Ok, so I'm putting this as positive_review/wontfix


---

Comment by jpflori created at 2013-01-30 13:10:15

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-01-30 13:11:22

I guess it would be worth confirming this doctest passes :) though I'm sure it will now.


---

Comment by jpflori created at 2013-01-30 13:42:46

It passed on my 5.5.rc0 and 5.6.rc0 'make ptest' and just did so on my 5.7.beta1.


---

Comment by jdemeyer created at 2013-01-31 20:35:55

Resolution: worksforme
