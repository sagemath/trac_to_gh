# Issue 9352: givaro spkg: trivial typo in spkg-check

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-06-27 17:18:32

Assignee: tbd

CC:  drkirkby

The file spkg-check in the givaro spkg prints the following if testing fails: "Error while running the R testsuite ... exiting".  The new spkg changes "R" to "Givaro".



---

Attachment


---

Comment by jhpalmieri created at 2010-06-27 17:22:22

I've attaching the output from "hg diff".  The new spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg).


---

Comment by jhpalmieri created at 2010-06-27 17:22:22

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-06-27 17:43:26

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-27 17:43:26

Positive review of course. 

Dave


---

Comment by mpatel created at 2010-08-09 09:35:55

Resolution: fixed


---

Comment by jdemeyer created at 2011-12-12 09:16:08

Could it be that the version number really should have been

```
givaro-3.2.13rc1.p2.spkg
```

instead of

```
givaro-3.2.13rc2.p2.spkg
}}}?
