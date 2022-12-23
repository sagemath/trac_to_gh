# Issue 6529: adding doctests to arith.py

Issue created by migration from https://trac.sagemath.org/ticket/6529

Original creator: mhampton

Original creation time: 2009-07-14 04:52:36

Assignee: somebody

arith.py currently has quite a few doctests missing.  I (Marshall Hampton) am planning on bringing this up to 100% coverage soon.


---

Comment by mhampton created at 2009-07-14 19:05:40

Brings arith.py coverage to 100%; includes functions from #6509


---

Comment by mhampton created at 2009-07-14 19:07:33

Changing type from defect to enhancement.


---

Attachment

Attached patch has functions from ticket #6509 in it as well.  

I deleted the optional argument "k=1" from Euler_Phi, since it didn't seem to be there for any reason.


---

Attachment


---

Comment by davidloeffler created at 2009-07-16 17:02:40

Good work: patch applies fine, and all doctests pass. But I noticed that several docstrings are mis-formatted, including the one for the new four_squares function. Then I had an attack of enthusiasm and decided to clean all that up. Hence the second patch above.

I'm happy with mhampton's changes; so if mhampton (or anyone someone else) could take a quick look at the second patch, then we can call this a positive review.

David


---

Comment by mvngu created at 2009-07-18 17:05:20

Resolution: fixed


---

Comment by mhampton created at 2009-07-19 13:51:30

Thanks David, that was a lot of cleanup work.
