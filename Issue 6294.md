# Issue 6294: lisp command in sage is now totally broken (because of ecl switch)

Issue created by migration from https://trac.sagemath.org/ticket/6294

Original creator: was

Original creation time: 2009-06-15 09:21:19

Assignee: was

CC:  awebb


```
wstein@bsd:~/build/sage-4.0.2.alpha3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: lisp.eval('(+ 2 3)')
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.0.2.alpha3, Release Date: 2009-06-13                |
| Type notebook() for the GUI, and license() for information.        |
/Users/was/.sage/temp/bsd.local/80207/_Users_was__sage_init_sage_0.py in <module>()

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in eval(self, code, strip, **kwds)
    116         """
    117         with gc_disabled():
--> 118             self._synchronize()
    119             code = str(code)
    120             code = code.strip()

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in _synchronize(self)
    192         E = self._expect
    193         if E is None:
--> 194             self._start()
    195             E = self._expect
    196         r = random.randrange(2147483647)

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.pyc in _start(self, *args, **kwds)
    186             True
    187         """
--> 188         Expect._start(self, *args, **kwds)
    189         self.__in_seq = 1
    190 

/Users/was/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)
    457             failed_to_start.append(self.__name)
    458             raise RuntimeError, "Unable to start %s because the command '%s' failed.\n%s"%(
--> 459                 self.__name, cmd, self._install_hints())
    460 
    461         os.chdir(current_path)

RuntimeError: Unable to start Lisp because the command 'clisp-noreadline --silent -on-error abort' failed.

sage: 
```



---

Attachment

All I did was change the clisp command to ecl and the tests passed. The exception is version and I could not find an equivalent for ecl in the manual. For now I just put a string to refer to the console which does print the version number. I did not attempt to fill in any of the "NotImplemented" methods.

Adam


---

Comment by timdumol created at 2009-08-30 09:40:28

I applied the patch on Sage 4.1.1. Lisp interface seems to work properly, code seems clean, and the doctests passed.


---

Comment by mvngu created at 2009-08-30 12:23:26

Resolution: fixed
