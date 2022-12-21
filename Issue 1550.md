# Issue 1550: use libecm instead of pexpect+ecm binary

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-12-17 13:46:48

Assignee: was

I noticed the GMP-ECM interface currently calls the ecm binary through a text interface, with command line 
parameters, and gets results by parsing the output of ecm.

It would be much better and more efficient to use the C interface libecm (see the ecm.h header file, and the
ecmfactor.c file distributed without GMP-ECM). Note that the C interface already returns information about the
found factor and the cofactor (prime, composite). Also, the libecm.a file is already compiled by SAGE.


---

Comment by was created at 2008-01-21 11:41:31

This is a great idea.  I thought that Yi Qiang already implemented something like this though, but evidently not (or it didn't get into sage).  I'll ping him again about this.


---

Comment by rlm created at 2008-01-21 20:55:04

Needs serious improvement- just a minimal implementation, probably in the wrong directory...


---

Attachment


---

Comment by rlm created at 2008-01-22 01:22:31

Patch on top of libecm.patch


---

Attachment

Review: This is a great patch, which could in addition serve as example of how to interface a C
library with SAGE. Just a minor comment: the example ecmfactor(999, 0.0) always outputs (True, 27):
factors 2 and 3 are special within ECM. I would suggest a more difficult example, for instance
ecmfactor(1022117, 10.0) which sometimes outputs (True, 1013), sometimes (True, 1009),
sometimes (True, 1022117), or (False, None). However this might cause problems with the doctests:
how to check functions with non-deterministic output?


---

Comment by rlm created at 2008-01-22 17:09:34

Here's an example (whenever 'random' occurs, the output is not checked against the expected output):


```
sage: ecmfactor(1022117, 10.0) # random output
(True, 1022117)
```



---

Comment by mabshoff created at 2008-01-23 04:20:03

Resolution: fixed


---

Comment by mabshoff created at 2008-01-23 04:20:03

Merged in Sage 2.10.1.alpha2
