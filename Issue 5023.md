# Issue 5023: typo in calculus.py

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2009-01-19 10:34:11

Assignee: tba

at line 1372, algorithim should be algorithm



---

Attachment


---

Comment by zimmerma created at 2009-01-19 21:01:22

The attachment fixes the above typo and two more. However for the last one (tahn -> tanh) I am
concerned about the fact that there was no doctest for the corresponding function.

```
sage: a=tanh(2)
sage: a._algebraic_(QQbar)
...
TypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational
```

Did I something wrong? If not, a new ticket should be opened.


---

Comment by jsp created at 2009-02-05 15:29:15

The patch corrected the typos, so a positive review.

But still


```
[jaap`@`paix sage-3.3.alpha4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.3.alpha5, Release Date: 2009-02-03                  |
| Type notebook() for the GUI, and license() for information.        |
sage: a=tanh(2)

sage: a._algebraic_(QQbar)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

[...]
TypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational
```


Someone more knowledgeable should decide to open a new ticket or not.

Jaap


---

Comment by mabshoff created at 2009-02-06 00:20:49

I have moved the issue Paul pointed out to #5191 so we can merge the spelling fixes.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 22:28:10

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 22:28:10

Resolution: fixed
