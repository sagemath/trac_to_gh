# Issue 1539: bdist of sage should include devel/doc

Issue created by migration from https://trac.sagemath.org/ticket/1539

Original creator: was

Original creation time: 2007-12-16 16:35:16

Assignee: mabshoff


```
wstein: note-to-self devel/doc is missing from the bdist.
[08:33am] wstein: maybe it shouldn't be.
[08:33am] wstein: I don't know.
[08:33am] wstein: I think bdist should have it...
[08:33am] wstein: trac ticket
```



---

Comment by was created at 2008-02-12 16:16:24

#1708 duplicated this

Also, here is a comment from Kate Minola, which is the same problem.  I've thus
promoted this to a blocker:

```
For sage-2.10.1, if I compile from source and run
'make check' - all is fine.  If I then build a binary
distribution (using -bdist), and then inside the binary
distribution run 'make check' I get the following errors.

Kate

Testing SAGE tutorial
/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/
local/bin/sage-maketest: line 18: cd: /home/kate/sage/sage-2.10.1-
x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/tut: No such file
or directory
ERROR: File ./tut.tex is missing
exit code: 1

----------------------------------------------------------------------
The following tests failed:


       ./tut.tex
Total time for all tests: 0.0 seconds
Testing SAGE programming guide
/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/
local/bin/sage-maketest: line 22: cd: /home/kate/sage/sage-2.10.1-
x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/prog: No such
file or directory
ERROR: File ./prog.tex is missing
exit code: 1

----------------------------------------------------------------------
The following tests failed:


       ./prog.tex
Total time for all tests: 0.0 seconds
Testing SAGE constructions guide
/home/kate/sage/sage-2.10.1-x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/
local/bin/sage-maketest: line 26: cd: /home/kate/sage/sage-2.10.1-
x86_64-Linux/dist/sage-2.10.1-x86_64-Linux/devel/doc/const: No such
file or directory
ERROR: File ./const.tex is missing
exit code: 1

----------------------------------------------------------------------
The following tests failed:


       ./const.tex
Total time for all tests: 0.0 seconds
```



---

Comment by was created at 2008-02-12 16:16:24

Changing priority from major to blocker.


---

Attachment


---

Comment by mabshoff created at 2008-08-26 09:27:30

Patch is good. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 09:31:33

Resolution: fixed


---

Comment by mabshoff created at 2008-08-26 09:31:33

Merged in Sage 3.1.2.alpha1
