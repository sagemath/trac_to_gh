# Issue 632: bug in command line time function and something -- very weird

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-09 23:27:42

Assignee: somebody

Notice that the second timing below is "0 seconds", which is clearly completely wrong.
The notation "3r" means the unpreparsed 3, i.e., the Python *integer* 3.  There
is a *noticeable amount of time* that passes when the input is given.  So something
is very very wrong.  This happens on intel os x and on 64-bit opteron linux (and
probably all other os's). 


```
sage: time n=int(3)**int(999999)
CPU times: user 0.76 s, sys: 0.00 s, total: 0.76 s
Wall time: 0.76
sage: time n= 3r ** 999999r
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: preparse('time n= 3r ** 999999r')
'time n= 3 ** 999999'
sage: preparse('time n=int(3)**int(999999)')
'time n=int(Integer(3))**int(Integer(999999))'
```



---

Comment by cwitty created at 2007-10-07 17:36:49

The "time" IPython operator compiles the code, and then carefully times how long it takes to run the compiled code.

The Python compiler does some constant folding.  In this case, when IPython tries to compile "n = 3 ** 999999", the Python compiler evaluates the exponentiation (before IPython starts timing).

I can't think of a good way to fix this, if we even decide it's a bug.  Maybe one of the less-bad ways is to change the preprocessor, so that "3r" maps to "int(3)" instead of "3".


---

Comment by cwitty created at 2007-10-12 01:24:36

For the record:

William Stein, Fernando Perez, and I corresponded about this.  In the next version of IPython (0.8.2), the "time" command will time the compilation separately, and report this time if it's more than 0.1 seconds.

I suppose this bug should stay open until that version of IPython is included in SAGE; then it can be closed.


---

Comment by anakha created at 2008-10-23 23:33:41

This is fixed in 3.1.4 at least:


```
sage: time n= 3r ** 999999r
CPU times: user 0.17 s, sys: 0.01 s, total: 0.17 s
Wall time: 0.19 s
```


And we are already at 0.8.4 for IPython.


---

Comment by mabshoff created at 2008-10-24 10:35:10

Resolution: fixed


---

Comment by mabshoff created at 2008-10-24 10:35:10

Fixed.

Cheers,

Michael
