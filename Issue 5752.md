# Issue 5752: Bring doctests of sage/games/sudoku.py to 100%

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-04-11 15:47:56

Assignee: mabshoff




---

Comment by rbeezer created at 2009-04-11 19:28:46

Coverage is now 100%, Several additional examples, including a minimal-hint, uniquely-solvable puzzle.  Some minor code and comment clean-ups.


---

Attachment


---

Comment by was created at 2009-04-12 05:26:49

Cool example in the docstring, though of course that the sudoku command at the top level takes forever on this hard one is a bummer.  I wish there were a better solver in sage..


```
sage: B = matrix(ZZ, 9, 9, [ [0,0,0,0,1,0,9,0,0], [8,0,0,4,0,0,0,0,0], [2,0,0,0,0,0,0,0,0], [0,7,0,0,3,0,0,0,0], [0,0,0,0,0,0,2,0,4], [0,0,0,0,0,0,0,5,8], [0,6,0,0,0,0,1,3,0], [7,0,0,2,0,0,0,0,0], [0,0,0,8,0,0,0,0,0] ])
sage: sudoku(B)
[wait forever...]
```


Very nice job adding doctests!!


---

Comment by rbeezer created at 2009-04-12 06:00:21

Replying to [comment:2 was]:
> I wish there were a better solver in sage..

I did have some thoughts about that while working through this...

> ` [wait forever...] `

I did eventually get a solution on that one, but didn't go back to do a timing on it!


---

Comment by mabshoff created at 2009-04-12 21:05:21

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-12 21:05:21

Resolution: fixed
