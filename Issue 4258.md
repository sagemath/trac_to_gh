# Issue 4258: switch multiplication of dense matrices over finite prime fields to LinBox

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-10-10 08:50:02

Assignee: malb

CC:  cpernet burcin jason simonking

Keywords: linbox, linear algebra


```
sage: A = random_matrix(GF(3),2000,2000)
sage: %time A*A
2000 x 2000 dense matrix over Finite Field of size 3
CPU time: 14.69 s,  Wall time: 15.08 s
```



```
sage: %time A._multiply_linbox(A)
2000 x 2000 dense matrix over Finite Field of size 3
CPU time: 2.47 s,  Wall time: 2.55 s
```



---

Comment by malb created at 2009-08-25 19:23:42

Just for the record: Burcin came pretty far during SD16 and IIRC Clément then too over?


---

Comment by burcin created at 2011-08-02 16:22:56

Changing component from linear algebra to linbox.


---

Comment by burcin created at 2011-08-02 16:22:56

see #4260 for ongoing work. Shall we close this as a duplicate?


---

Comment by malb created at 2011-08-30 15:57:53

This is a duplicate of #4260 and should be closed.


---

Comment by SimonKing created at 2012-03-02 09:57:55

Changing status from new to needs_review.


---

Comment by SimonKing created at 2012-03-02 09:59:29

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2012-03-02 09:59:29

Martin suggested to close this ticket as a duplicate of #4260, and I agree. So, I'm inserting Martin as a reviewer and change it into a positive review (with the suggested resolution "duplicate").


---

Comment by jdemeyer created at 2012-03-02 13:55:20

Resolution: duplicate
