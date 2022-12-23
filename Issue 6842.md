# Issue 6842: [with patch, needs review] ordinal_str giving wrong answers for 111, 112, 113

Issue created by migration from https://trac.sagemath.org/ticket/6842

Original creator: SimonKing

Original creation time: 2009-08-29 11:29:59

Assignee: somebody

Keywords: ordinals

The following is incorrect, if I am not mistaken (but I am not a native speaker):

```
sage: n = 113
sage: n.ordinal_str()
'113rd'
sage: n = 112
sage: n.ordinal_str()
'112nd'
sage: n = 111
sage: n.ordinal_str()
'111st'
```


With my patch, one gets

```
sage: n = 111
sage: n.ordinal_str()
'111th'
sage: n = 112
sage: n.ordinal_str()
'112th'
sage: n = 113
sage: n.ordinal_str()
'113th'
```

while one still has

```
sage: n = 121
sage: n.ordinal_str()
'121st'
sage: n = 122
sage: n.ordinal_str()
'122nd'
sage: n = 123
sage: n.ordinal_str()
'123rd'
```



---

Comment by SimonKing created at 2009-08-29 11:30:50

Fixing ordinal_str for numbers of the form n*100+11, n*100+12, n*100+13


---

Attachment

Looks good to me. It passes unit tests and the documentation builds correctly. 

Adam


---

Comment by mvngu created at 2009-08-30 07:09:42

Resolution: fixed


---

Comment by cremona created at 2009-08-30 10:32:57

I came along to review this only to find that I was too late.  Thanks for fixing the bug (which was mine).
