# Issue 5393: pycrypto 2.0.1: integrate fix for http://www.securityfocus.com/bid/33674/info (security)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-27 16:38:36

Assignee: mabshoff


```
PyCrypto ARC2 Module Buffer Overflow Vulnerability

PyCrypto (Python Cryptography Toolkit) is prone to a buffer-overflow vulnerability because it fails to adequately verify user-supplied input.

Successful exploits may allow attackers to execute arbitrary code in the context of applications using the vulnerable module. Failed attempts may lead to a denial-of-service condition.
```



---

Comment by mabshoff created at 2009-02-27 16:38:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-27 16:39:58

The commit to be applied can be found at 

http://gitweb.pycrypto.org/?p=crypto/pycrypto-2.x.git;a=commitdiff;h=d1c4875e1f220652fe7ff8358f56dee3b2aba31b

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-03 00:12:43

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/rc0/pycrypto-2.0.1.p3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-03 00:17:38

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-03 00:17:38

Resolution: fixed
