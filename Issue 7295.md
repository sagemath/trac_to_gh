# Issue 7295: typo in ecm spkg-install

Issue created by migration from Trac.

Original creator: fbissey

Original creation time: 2009-10-25 09:35:57

Assignee: tbd

The removal of the old version of ecm in ecm-6.2.1_p0.spkg
is broken because of typo:


rm -f "$SAGE_LCOAL"/lib/libecm.*


should be:


rm -f "$SAGE_LOCAL"/lib/libecm.*

Notice LOCAL



---

Comment by fbissey created at 2009-10-26 01:01:43

patch to spkg-install


---

Attachment


---

Comment by fbissey created at 2009-10-26 01:02:32

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-10-28 14:00:11

The updated spkg can be found at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ecm/ecm-6.2.1.p1.spkg

All changes have been committed in fbissey's name.


---

Comment by mvngu created at 2009-10-28 14:00:11

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 16:47:35

Resolution: fixed
