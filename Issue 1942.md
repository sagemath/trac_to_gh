# Issue 1942: Sage 2.10.1.rc0: sage0.cputime()  broken on 32 bit FC7/8

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-26 23:10:50

Assignee: mabshoff

Jaap reports the following on 32 bit FC7/8 with Sage 2.10.1.rc0:

```
[jaap`@`paix sage-2.10.1.rc0]$ ./sage -t  devel/sage-main/sage/interfaces/sage0.py
sage -t  devel/sage-main/sage/interfaces/sage0.py           **********************************************************************
File "sage0.py", line 143:
     sage: _= sage0.cputime()     # random output
Exception raised:
     Traceback (most recent call last):
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
         compileflags, 1) in test.globs
       File "<doctest __main__.example_2[0]>", line 1, in <module>
         _= sage0.cputime()     # random output###line 143:
     sage: _= sage0.cputime()     # random output
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 150, in cputime
         return eval(self.eval('cputime(%s)'%t))
       File "<string>", line 1
           1.3517939999999999
          ^
      SyntaxError: invalid syntax
**********************************************************************
File "sage0.py", line 147:
     sage: _= sage0.cputime()     # random output
Exception raised:
     Traceback (most recent call last):
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
         compileflags, 1) in test.globs
       File "<doctest __main__.example_2[2]>", line 1, in <module>
         _= sage0.cputime()     # random output###line 147:
     sage: _= sage0.cputime()     # random output
       File "/home/jaap/downloads/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 150, in cputime
         return eval(self.eval('cputime(%s)'%t))
       File "<string>", line 1
           1.726736
          ^
      SyntaxError: invalid syntax
**********************************************************************
1 items had failures:
    2 of   3 in __main__.example_2
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_sage0.py
          [6.9 s]
exit code: 256 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 23:15:54

It doesn't happen on FC8 :)

Cheers,

Michael


---

Comment by jsp created at 2008-01-26 23:51:42

This is ./sage -t -verbose of .../sage0.py on Fedora7


---

Attachment


```
> > Also, could you try replacing the line 150 by
> >           s = self.eval('cputime(%s)'%t)
> >           print "'%s'"%s
> >           return 0
> > in case my above suggestion doesn't work, and report what gets printed.
> > 

Exiting SAGE (CPU time 0m0.00s, Wall time 0m8.03s).
[jaap`@`paix sage-2.10.1.rc0]$ ./sage -t  devel/sage-main/sage/interfaces/sage0.py 2>&1 | tee -a test_sage0.log
sage -t  devel/sage-main/sage/interfaces/sage0.py           **********************************************************************
File "sage0.py", line 143:
     sage: _= sage0.cputime()     # random output
Expected nothing
Got:
     ' 1.360792
     '
**********************************************************************
File "sage0.py", line 147:
     sage: _= sage0.cputime()     # random output
Expected nothing
Got:
     ' 1.7347349999999999
     '
**********************************************************************
1 items had failures:
    2 of   3 in __main__.example_2
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_sage0.py
          [7.0 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


         sage -t  devel/sage-main/sage/interfaces/sage0.py
Total time for all tests: 7.0 seconds
[jaap`@`paix sage-2.10.1.rc0]$

```



---

Comment by mabshoff created at 2008-01-27 14:48:58

As William suspected there are some control characters in there, which Jaap confirmed:

```
> I have to say -- I just don't get why this doesn't work on your FC7 machine.
> All that it is doing is eval'ing a correct float constant...  I wonder if there
> are weird hidden invisible control codes in the output or something.
> 

This is from the log file:
     ValueError: invalid literal for float(): ^[[0;31m ^[[0m1.8237209999999999
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-28 06:37:04

Craig opened another ticket for the same issue: #1958. Since we have a patch over there close this as a duplicate.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-28 06:37:04

Resolution: duplicate
