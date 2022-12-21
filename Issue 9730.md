# Issue 9730: A simple RC4 cipher implementation for Sage

Issue created by migration from Trac.

Original creator: sg.sourav

Original creation time: 2010-08-11 21:55:35

Assignee: mvngu

Keywords: RC4, Cryptosystem, Cipher

This is a standard RC4 implementation in the Cryptography directory for Sage. We do not consider advanced criteria to initialize the state bytearray, and hence this system may be prone to attacks (refer to relevant literature).

Though this is not fully secure (upto industry standard), this is a full-version implementation of the cipher, and can be used for educational purpose as well as for small-scale encryptions.


---

Comment by sg.sourav created at 2010-08-11 21:56:22

A patch to incorporate an implementation of RC4 in Sage


---

Comment by sg.sourav created at 2010-08-12 19:12:08

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-08-14 12:08:40

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-08-14 12:08:40

Running doctests over `rc4.py` fails with message:

```sh
[mvngu`@`sage sage-4.5.3.alpha0]$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py 
sage -t -long "devel/sage-main/sage/crypto/rc4.py"          
**********************************************************************
Error: TAB character found.

	 [1.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/crypto/rc4.py"
Total time for all tests: 1.9 seconds
```

This patch needs a lot of work.


---

Comment by sg.sourav created at 2010-08-16 08:22:58

Attaching a modified patch which passed all doctests successfully. Also added some sanity checks for types of inputs. 

Apply rc4_mod1.patch directly (not over rc4.patch).



```
sourav`@`ssg:~/sage4.5$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py
sage -t -long "devel/sage-main/sage/crypto/rc4.py"          
	 [6.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.7 seconds
sourav`@`ssg:~/sage4.5$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py
sage -t -long "devel/sage-main/sage/crypto/rc4.py"          
	 [6.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.7 seconds
```



---

Comment by sg.sourav created at 2010-08-16 08:23:52

Modified version of rc4.patch including sanity checks (passed doctests)


---

Attachment

apply rc4_mod1.patch


---

Comment by chapoton created at 2013-08-22 17:20:01

apply only rc4_mod1.patch


---

Attachment


---

Comment by chapoton created at 2014-01-06 20:03:34

New commits:
