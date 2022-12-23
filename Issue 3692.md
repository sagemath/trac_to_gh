# Issue 3692: notebook -- issue with quotes

Issue created by migration from https://trac.sagemath.org/ticket/3692

Original creator: was

Original creation time: 2008-07-21 07:07:29

Assignee: boothby

Using notebook mode.


```
Problem:
cell input: '\''
output: '\\u0027'
expected output: '\u0027'
```


Sincerely,
Mats


---

Comment by was created at 2008-07-21 20:01:55

Tom Boothby:

```

Either this is a python bug, "user error", or a feature request.  I don't think this is a problem with the notebook.

boothby@eight:~$ sage -python
Python 2.5.1 (r251:54863, Nov  9 2007, 07:54:29)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> x = '\u0027'
>>> x
'\\u0027'
>>>

The default behavior is to call repr on the return value of the last line (if not None), yes?  If so, this is consistent.  If not, what?  Should we call print instead of repr? (then, I believe it's a feature request)
```



---

Comment by was created at 2008-07-21 20:01:55

Resolution: invalid
