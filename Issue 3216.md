# Issue 3216: notebook -- doctests for user.py

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-05-16 04:34:16

Assignee: timothyclemans

Warning patch will depend on #3213 because user.py was modified for it.



---

Attachment


---

Comment by was created at 2008-05-19 04:55:35

REVIEW:

Even after the patch there is a nodoctest at the top of the file.  That turns off doctesting. 
I think this may have mislead you into thinking the doctests work.  Could you please delete
nodoctest from the file, then fix all the doctest failures.  Thanks!

```
teragon-2:notebook was$ sage -t user.py 
sage -t  devel/sage-bugday12/sage/server/notebook/user.py   **********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/user.py", line 72:
    sage: user.set_password(self, 'Crrc!')
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        user.set_password(self, 'Crrc!')###line 72:
    sage: user.set_password(self, 'Crrc!')
    NameError: name 'self' is not defined
**********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/user.py", line 73:
    sage: old != user.password()
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/user.py", line 85:
    sage: user.set_hashed_password(self, 'Crrc!')
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[3]>", line 1, in <module>
        user.set_hashed_password(self, 'Crrc!')###line 85:
    sage: user.set_hashed_password(self, 'Crrc!')
    NameError: name 'self' is not defined
**********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/user.py", line 86:
    sage: user.password()
Expected:
    'Crrc!'
Got:
    'aamxw5LCYcWY.'
**********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/user.py", line 104:
    sage: user.get_email()
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        user.get_email()###line 104:
    sage: user.get_email()
    AttributeError: UserConfiguration instance has no attribute 'get_email'
**********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/user.py", line 106:
    sage: user.set_email('bob`@`ilovepizza.gov')
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[4]>", line 1, in <module>
        user.set_email('bob`@`ilovepizza.gov')###line 106:
    sage: user.set_email('bob`@`ilovepizza.gov')
    AttributeError: UserConfiguration instance has no attribute 'set_email'
**********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/user.py", line 107:
    sage: user.get_email()
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[5]>", line 1, in <module>
        user.get_email()###line 107:
    sage: user.get_email()
    AttributeError: UserConfiguration instance has no attribute 'get_email'
**********************************************************************
3 items had failures:
   2 of   6 in __main__.example_4
   2 of   5 in __main__.example_5
   3 of   6 in __main__.example_7
***Test Failed*** 7 failures.
For whitespace errors, see the file /Users/was/build/build/sage-3.0.1/tmp/.doctest_user.py
	 [2.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage-bugday12/sage/server/notebook/user.py
Total time for all tests: 2.2 seconds
teragon-2:notebook was$ 
```



---

Attachment


---

Comment by craigcitro created at 2008-06-15 21:45:17

Changing keywords from "" to "editor_wstein".


---

Comment by was created at 2008-06-16 04:45:30

apply all three patches including this one, which makes things professional instead of "pizza"


---

Attachment


---

Comment by mabshoff created at 2008-06-23 12:56:40

Merged in Sage 3.0.4.alpha0


---

Comment by mabshoff created at 2008-06-23 12:56:40

Resolution: fixed
