# Issue 978: bug in Sequence __str__ method

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-24 02:27:44

Assignee: somebody


```
Andrey Novoseltsev 	 
Dear William,

I have printing issues with sequences, cr parameter is not processed correctly
when it is False:

sage: s = Sequence([1,2,3], cr=False)
sage: s
[1, 2, 3]
sage: print s, str(s), repr(s)
[
1,
2,
3
] [
1,
2,
3
] [1, 2, 3]
sage: s = Sequence([1,2,3], cr=True)
sage: s
[
1,
2,
3
]
sage: print s, str(s), repr(s)
[
1,
2,
3
] [
1,
2,
3
] [
1,
2,
3
]

I get this both under notebook and command line and it is somewhat unpleasant.

Thank you,
```



---

Attachment


---

Comment by malb created at 2007-10-24 19:18:02

Resolution: fixed


---

Comment by malb created at 2007-10-24 19:18:02

applied to 2.8.9.alpha1
