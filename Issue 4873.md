# Issue 4873: sage -optional should not require write access to sage repo; e.g., people may want to check on what packages are installed system-wide

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 18:36:36

Assignee: mabshoff


```
wstein`@`sage:~$ /usr/local/bin/sage -optional
Using SAGE Server http://www.sagemath.org//packages
http://www.sagemath.org//packages/optional/list --> /usr/local/sage/tmp/list
[Errno 13] Permission denied: '/usr/local/sage/tmp/list'



********************************************************************************



Error contacting http://www.sagemath.org//packages/optional/list. Try using an alternative server.
For example, from the bash prompt try typing

   export SAGE_SERVER=http://sage.scipy.org/sage/

then try again.



********************************************************************************



```



---

Comment by mabshoff created at 2008-12-24 21:36:45

Resolution: duplicate


---

Comment by mabshoff created at 2008-12-24 21:36:45

This is a dupe of #961

Cheers,

Michael
