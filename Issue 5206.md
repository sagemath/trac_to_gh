# Issue 5206: attach command doesn't handle carriage returns correctly

Issue created by migration from https://trac.sagemath.org/ticket/5206

Original creator: mhampton

Original creation time: 2009-02-08 08:18:24

Assignee: boothby

Keywords: attach

This problem is specific to attaching files ending with ".py" in the notebook.  It does not seem to affect the command-line, or files ending with ".sage".  Some files that are moved around from different filesystems and editors end up having end-of-line commands that look like: "\r\n".  These raise a syntax error when attached.  Here is an example (of course you need to change the path):


```
testfile = file('/home/marshall/Desktop/misc/testrn.py','w')
testfile.write('my_var = 2\r\n')
testfile.close()
attach /home/marshall/Desktop/misc/testrn.py

    Syntax Error:
        attach /home/marshall/Desktop/misc/testrn.py
```



---

Comment by mabshoff created at 2009-02-08 08:23:15

No ticket without patches that aren't blockers should be assigned to 3.3 or 3.4 at this stage.

Cheers,

Michael


---

Comment by timdumol created at 2010-01-17 10:20:55

This seems to be fixed already (probably by #7514).


---

Comment by timdumol created at 2010-01-19 02:59:21

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 03:38:28

Resolution changed from duplicate to fixed
