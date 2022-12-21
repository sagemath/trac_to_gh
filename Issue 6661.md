# Issue 6661: Misleading warning message of  _expect_expr() at KeyboardInterrupt

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-07-31 13:32:17

Assignee: was

Keywords: KeyboardInterrupt

When there is a `KeyboardInterrupt` while `_expect_expr` talks with some interface, there is _always_ the warning message

```
Control-C pressed.  Interrupting R. Please wait a few seconds...
```

before the `KeyboardInterrupt` is re-raised -- regardless whether the interface is R or anything else!

The patch that I am about to post would instead print 

```
"Control-C pressed.  Interrupting %s. Please wait a few seconds..."%self
```

where `self` is the interface.

I know that all bug fixes should be doc tested. But can someone explain to me how one can produce a `KeyboardInterrupt` while `_expect_expr()` is running?


---

Comment by SimonKing created at 2009-07-31 13:34:30

Changing assignee from was to SimonKing.


---

Comment by SimonKing created at 2009-07-31 13:34:30

Changing status from new to assigned.


---

Comment by SimonKing created at 2009-07-31 19:13:55

Fixing a misleading warning message in _expect_expr, with doc test included


---

Attachment

Meanwhile there also is a doc test (thank you for pointing me to the "alarm" function, William!), so, I think the patch is ready for review!

Now, we have a better warning message:

```
sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Control-C pressed.  Interrupting Singular. Please wait a few seconds...
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/king/.sage/temp/gauss/29173/_home_king__sage_init_sage_0.py in <module>()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
    838                 else:
    839                     break
--> 840             raise KeyboardInterrupt, msg
    841
    842     def _sendstr(self, str):

KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
sage: print sage0.eval("alarm(1); gap._expect_expr('1')")
Control-C pressed.  Interrupting Gap. Please wait a few seconds...
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/king/.sage/temp/gauss/29173/_home_king__sage_init_sage_0.py in <module>()

/home/king/SAGE/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
    838                 else:
    839                     break
--> 840             raise KeyboardInterrupt, msg
    841
    842     def _sendstr(self, str):

KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
```


Note that it correctly says "Interrupting Singular" or "Interrupting Gap".


---

Comment by mvngu created at 2009-08-03 01:15:12

Before patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Control-C pressed.  Interrupting R. Please wait a few seconds...
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/.sage/temp/sage.math.washington.edu/23333/_home_mvngu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
    830                 else:
    831                     break
--> 832             raise KeyboardInterrupt, msg
    833 
    834     def _sendstr(self, str):

KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
sage: print sage0.eval("alarm(1); gap._expect_expr('1')")
Control-C pressed.  Interrupting R. Please wait a few seconds...
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/23333/_home_mvngu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
    830                 else:
    831                     break
--> 832             raise KeyboardInterrupt, msg
    833 
    834     def _sendstr(self, str):

KeyboardInterrupt: computation timed out because alarm was set for 1 seconds

```

The error message should say that it's interrupting Singular or GAP, not R. Now after the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Control-C pressed.  Interrupting Singular. Please wait a few seconds...
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/.sage/temp/sage.math.washington.edu/23479/_home_mvngu__sage_init_sage_0.py in <module>()

/scratch/mvngu/release/sage-4.1.1.rc0/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
    838                 else:
    839                     break
--> 840             raise KeyboardInterrupt, msg
    841 
    842     def _sendstr(self, str):

KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
sage: print sage0.eval("alarm(1); gap._expect_expr('1')")
Control-C pressed.  Interrupting Gap. Please wait a few seconds...
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/23479/_home_mvngu__sage_init_sage_0.py in <module>()

/scratch/mvngu/release/sage-4.1.1.rc0/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
    838                 else:
    839                     break
--> 840             raise KeyboardInterrupt, msg
    841 
    842     def _sendstr(self, str):

KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
```

The error message now correctly says that it's interrupting Singular or GAP. So positive review.


---

Comment by mvngu created at 2009-08-03 01:15:12

Resolution: fixed
