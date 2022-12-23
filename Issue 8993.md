# Issue 8993: Representation of polynomial quotient rings in Singular

Issue created by migration from https://trac.sagemath.org/ticket/8993

Original creator: SimonKing

Original creation time: 2010-05-19 16:48:31

Assignee: was

Keywords: polynomial quotient ring, singular

Currently there is no representation of univariate polynomial quotient rings in the Singular interface; it was only implemented for the multivariate case.

The attached patch implements it:

```
sage: P.<x> = QQ[]
sage: Q.<xi> = P.quo([(x^2+1)])
sage: singular(xi)
xi
sage: singular(Q)
//   characteristic : 0
//   number of vars : 1
//        block   1 : ordering lp
//                  : names    xi
//        block   2 : ordering C
// quotient ring from ideal
_[1]=xi^2+1
sage: (singular(xi)*singular(xi)).NF('std(0)')
-1
```




---

Comment by SimonKing created at 2010-05-19 16:50:38

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-05-25 01:19:29

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-05-25 01:19:29

Mostly looks good, the only issue is that you should never "import sage" (or sage.all) from within the sage library.


---

Comment by SimonKing created at 2010-05-25 07:30:08

Replying to [comment:2 robertwb]:
> Mostly looks good, the only issue is that you should never "import sage" (or sage.all) from within the sage library. 

Do I understand correctly:

It is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?

I'll submit a correction soon.

Cheers,

Simon


---

Comment by robertwb created at 2010-05-25 07:38:42

Yes.


---

Comment by SimonKing created at 2010-05-25 08:01:47

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-05-25 08:01:47

Replying to [comment:3 SimonKing]:
> ...
> It is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?
> 
> I'll submit a correction soon.

Done!


---

Comment by malb created at 2010-07-21 15:51:51

Patch looks okay, doctests pass.


---

Comment by malb created at 2010-07-21 15:51:51

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 02:25:29

Changing status from positive_review to needs_work.


---

Comment by ddrake created at 2010-07-22 02:25:29

Please include the ticket number in the commit messages for your patches!


---

Attachment

Implement polynomial quotient rings in singular interface


---

Attachment

Avoid "import sage" according to the reviewer's request - apply after first patch


---

Comment by SimonKing created at 2010-07-22 08:13:39

Replying to [comment:7 ddrake]:
> Please include the ticket number in the commit messages for your patches!

I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to "positive review".


---

Comment by SimonKing created at 2010-07-22 08:13:39

Changing status from needs_work to positive_review.


---

Comment by ddrake created at 2010-07-22 09:11:29

Replying to [comment:8 SimonKing]:
> I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to "positive review".

It certainly does. Thanks for fixing this! It should get merged in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-22 23:51:19

Merged both patches in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-22 23:51:19

Resolution: fixed
