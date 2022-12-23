# Issue 6095: implement sloane sequence: A060302 (digits of (pi^4+pi^5))^(1/6)

Issue created by migration from https://trac.sagemath.org/ticket/6095

Original creator: was

Original creation time: 2009-05-20 21:20:44

Assignee: mhansen

interesting because almost digits of e.


---

Attachment


---

Comment by robertwb created at 2009-05-20 21:50:00

The code looks good, but is this useful enough to have in Sage?


---

Comment by was created at 2009-05-21 06:13:52

cwitty and robertwb pointed out a BUG.  If there is a sequence of more than ten 9's in a row, then this code can give a wrong answer.   One has to specifically deal with the case of 9's and use that the number is transcendental.
