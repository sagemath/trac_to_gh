# Issue 5962: Comparison in the Gap interface raises an error

Issue created by migration from https://trac.sagemath.org/ticket/5962

Original creator: SimonKing

Original creation time: 2009-05-02 17:31:46

Assignee: was

CC:  wdj

Keywords: gap comparison

On sage.math with sage-3.4.1, one has

```
sage: gap('DihedralGroup(8)')==gap('DihedralGroup(8)')
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...
RuntimeError: Gap produced error output
Error, no 1st choice method found for `LT' on 2 arguments

   executing $sage1 < $sage2;
```


The problem seems to be that Gap is unable to compare:

```
sage: gap('DihedralGroup(8)=DihedralGroup(8)')
false
```


Perhaps it would make sense to try and implement a `__cmp__` method that is more sophisticated than what is done in Gap? 

At least it should be made sure that the `__cmp__` method of the Gap interface does not raise an error.



---

Comment by SimonKing created at 2010-07-05 12:10:46

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-07-05 12:10:46

I see no way for a really satisfying solution, as long as GAP can not even compare two objects whose definitions are identical.

However, the errors being raised by GAP when comparing elements are now caught in a try-except clause. We have, as doc tests:

```
sage: gap('DihedralGroup(8)')==gap('DihedralGroup(8)')
False    # sorry, this is what GAP claims.
sage: gap('SymmetricGroup(8)')<gap('AlternatingGroup(8)')
True
sage: gap('SymmetricGroup(8)')>gap('AlternatingGroup(8)')
False
sage: gap('SymmetricGroup(8)')==gap('SymmetricGroup(8)')
True
```


All but the first of these examples worked before. But the first resulted in an error, which is now fixed.


---

Comment by SimonKing created at 2011-03-08 12:12:19

I just found that this ticket needs review since 8 months. Fortunately the patch still works fine. So, any volunteer?


---

Comment by wdj created at 2011-03-08 13:53:08

Replying to [comment:2 SimonKing]:
> I just found that this ticket needs review since 8 months. 
> Fortunately the patch still works fine. So, any volunteer?

I have spring break coming up and can try to review it then if no one beats me to it.


---

Comment by wdj created at 2011-03-12 22:56:24

This patch applies to 4.7.a1 and passes sage -testall. The patch does as claimed (adding some try-except statements) and contains the proper additional examples in the docstrings. Positive review from me.

Thanks Simon!


---

Comment by wdj created at 2011-03-12 22:56:24

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-27 13:52:32

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-03-27 13:52:32

Please change the commit message (using hg qrefresh -e) such that the ticket number appears on the first line.


---

Attachment

Avoid an error being raised when comparing GAP elements. Add doctest.


---

Comment by SimonKing created at 2011-03-27 14:01:51

Changing status from needs_work to positive_review.


---

Comment by SimonKing created at 2011-03-27 14:01:51

Replying to [comment:5 jdemeyer]:
> Please change the commit message (using hg qrefresh -e) such that the ticket number appears on the first line. 

Done.


---

Comment by jdemeyer created at 2011-03-27 14:25:37

Replying to [comment:6 SimonKing]:
> Done.

Thanks!


---

Comment by jdemeyer created at 2011-03-28 07:18:01

Resolution: fixed
