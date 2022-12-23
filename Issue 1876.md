# Issue 1876: minor typo in reference manual section 8.1.1.2

Issue created by migration from https://trac.sagemath.org/ticket/1876

Original creator: bober

Original creation time: 2008-01-21 06:22:45

Assignee: tba

The reference manual page at

http://www.sagemath.org/doc/html/ref/node44.html

says

*Note that the character is an escape character in Python, and also a character used by graph6 strings:*

and then later

*In Python, the escaped character is represented by*

Probably there should be a 'slash' and a 'slashslash' there somewhere.


---

Comment by mabshoff created at 2008-03-16 08:48:45

This seems to have gotten fixed. From http://www.sagemath.org/doc/html/ref/node44.html as of 2.10.3:


```
Note that the \ character is an escape character in Python, and also a character used by graph6 strings:
```

and then

```
In Python, the escaped character \ is represented by \\:
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 08:50:06

Resolution: fixed
