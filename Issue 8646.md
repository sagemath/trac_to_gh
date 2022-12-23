# Issue 8646: Windows 7 Virtual Box Install Fails

Issue created by migration from https://trac.sagemath.org/ticket/8646

Original creator: SevenThunders

Original creation time: 2010-04-03 01:54:07

Assignee: GeorgSWeber

I am running windows 7 64 bit, and have installed 
virtualbox 3.1.6.  Sage 4.3 does not import into virtualbox   right near the end of the import process it fails with the following error

Runtime error: -35 (Unresolved (unknown) host platform error.).

The error occurs on line 3325 of the source file VirtualBoxImpl.cpp .

This may be a virtualbox issue,  but it does mean that perhaps a lot of windows users can't get the default sage virtual environment to run.  I have not seen this issue reported elsewhere.


---

Comment by was created at 2010-04-05 03:01:24

The VirtualBox machine will be replaced by a VMware machine for the next release.  When that happens this ticket can be closed.


---

Comment by aapitzsch created at 2014-03-08 21:54:44

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-03-08 21:54:44

Running Windows 7 (64bit), too. Using the recent version of Virtualbox (4.3.8) importing and starting Sage 5.13 work without errors.


---

Comment by rws created at 2014-05-12 15:15:05

Appears to no longer be an issue.


---

Comment by rws created at 2014-05-12 15:15:05

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-05-12 20:18:09

Resolution: fixed
