# Issue 8658: opencdk spkg has incorrect DSO linking

Issue created by migration from Trac.

Original creator: vbraun

Original creation time: 2010-04-07 22:24:48

Assignee: AlexGhitza

Keywords: DSO

opencdk fails to explicitly link against libgcrypt. This is exposed by the changed ld behavior in Fedora 13 (beta), see https://fedoraproject.org/wiki/UnderstandingDSOLinkChange

The new version fixes this and is necessary to compile on F13. You can get it at

http://www.stp.dias.ie/~vbraun/Sage/spkg/opencdk-0.6.6.p4.spkg


---

Comment by mhansen created at 2010-06-09 18:12:50

I'd like to get this in 4.4.4.  There are a couple of issues. `/bin/sh` on boxen doesn't like ` Makefile.{am,in} `.  Also, sed on Solaris doesn't support `-i`.  While the Makefiles don't need to be used on Solaris, it be nice to not have those fail.  Also, we should check the exit status to make sure the command successfully ran.


---

Comment by mhansen created at 2010-06-09 18:12:50

Changing status from new to needs_work.


---

Comment by vbraun created at 2010-06-09 19:29:13

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-06-09 19:29:13

Ok updated version now copies a suitable Makefile.in file from patches/ instead of the sed hack:

http://www.stp.dias.ie/~vbraun/Sage/spkg/opencdk-0.6.6.p4.spkg

The Makefile.am is not needed, so I did not change it. Hopefully upstream will make a new release before we have to edit this again. The Fedora people are trying to push these changes upstream.


---

Comment by mhansen created at 2010-06-11 18:23:04

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-11 18:24:17

I've merged http://sage.math.washington.edu/home/mhansen/opencdk-0.6.6.p4.spkg


---

Comment by mhansen created at 2010-06-11 18:24:17

Resolution: fixed
