# Issue 1914: incorrect string escaping in preparser

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-01-24 16:55:08

Assignee: was

This works in python:

```
>>> print "abc \"def\""
abc "def"
```


but it's broken in sage:

```
sage: print "abc \"def\""
------------------------------------------------------------
   File "<ipython console>", line 1
     print "abc \"def._backslash_()""
                                    ^
<type 'exceptions.SyntaxError'>: EOL while scanning single-quoted string
```




---

Comment by mabshoff created at 2008-01-24 20:37:14

This might be related to #1781.

Cheers,

Michael


---

Comment by burcin created at 2008-05-24 09:40:37

Resolution: fixed


---

Comment by burcin created at 2008-05-24 09:40:37

This works for me on 3.0.2-rc2. There is also the following doctest in sage/misc/preparser.py around line 40 to cover this:


```
A string with escaped quotes in it (the point here is that the
preparser doesn't get confused by the internal quotes):
    sage: "\"Yes,\" he said."
    '"Yes," he said.'
    sage: s = "\\"; s
    '\\'
```


I think this bug can safely be resolved as worksforme.
