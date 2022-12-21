# Issue 8764: the full Data Encryption Standard (DES)

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-25 08:05:20

Assignee: mvngu

CC:  amca01@gmail.com

An implementation of the Data Encryption Standard (DES) for educational purposes.


---

Attachment

original Sage script by Alasdair McAndrew


---

Comment by mvngu created at 2010-04-25 08:08:57

Changing status from new to needs_work.


---

Comment by mvngu created at 2010-04-25 09:10:48

des.sage as a patch against Sage 4.4.rc0


---

Attachment

The patch [trac_8764-original-des.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8764/trac_8764-original-des.patch) contains essentially the same code as in [des.sage](http://trac.sagemath.org/sage_trac/attachment/ticket/8764/des.sage), but as a patch against the Sage library. The next task is to clean up that patch and organize the cryptography section of the reference manual in light of this implementation of DES.


---

Comment by chapoton created at 2013-08-25 09:27:52

I have cleaned up the patch a little bit.

There remains one doctest failing, and missing doctests.

apply trac_8764-original-des_v2.patch


---

Comment by chapoton created at 2013-08-25 11:30:41

apply only trac_8764-original-des_v2.patch


---

Attachment

clean version


---

Comment by chapoton created at 2013-08-25 12:44:26

apply only trac_8764-original-des_v2.patch


---

Comment by chapoton created at 2013-08-25 20:06:05

Changing keywords from "" to "data encryption standard".


---

Comment by chapoton created at 2014-01-05 12:56:26

New commits:


---

Comment by git created at 2016-05-19 12:30:08

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @yhxnf created at 2019-05-03 20:40:19

Changing status from needs_work to needs_review.


---

Comment by @yhxnf created at 2019-05-03 20:40:19

this seems outdated and inactive and now there is ticket:27761


---

Comment by roed created at 2021-04-28 05:55:15

Agreed: this can be closed.


---

Comment by roed created at 2021-04-28 05:55:15

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2021-04-30 18:21:32

Resolution: duplicate
