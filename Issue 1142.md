# Issue 1142: oddity with regular expressions and ipython

Issue created by migration from https://trac.sagemath.org/ticket/1142

Original creator: mabshoff

Original creation time: 2007-11-10 23:28:15

Assignee: was

Reported by wjp: The following is an example from the python regular expression howto. It seems that ipython's preprocessing somehow gets in the way. This works perfectly fine with regular python:

```
[wjp@issa sage-2.8.12]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.12, Release Date: 2007-11-06                      |
| Type notebook() for the GUI, and license() for information.        |
sage: import re
sage: >>> p = re.compile('(a(b)c)d')
sage: >>> m = p.match('abcd')
sage: >>> m.group(0)
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/data/sage/sage-2.8.12/<ipython console> in <module>()

<type 'exceptions.IndexError'>: no such group
sage: type(m)
<type '_sre.SRE_Match'>
sage: m.groups()
('abc', 'b')
sage: 
```


Cheers,

Michael


---

Comment by malb created at 2007-11-11 13:12:28

re cannot handle Sage Integers, but it should because they implement `__index__`

```
sage: import re
sage: p = re.compile('(a(b)c)d')
sage: m = p.match('abcd')
sage: m.group(0)
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/home/malb/<ipython console> in <module>()

<type 'exceptions.IndexError'>: no such group
sage: m.group(int(0))
'abcd'
```



---

Comment by mabshoff created at 2007-11-25 18:11:24

The problem is that the preparser turn 0 into an Integer. So using a python int fixes the problem.

Ergo: Invalid.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-25 18:11:24

Resolution: invalid
