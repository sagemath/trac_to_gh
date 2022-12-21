# Issue 5092: Primes()?? gets hung in len call

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-25 02:11:19

Assignee: was




---

Comment by saliola created at 2009-01-25 02:29:39

You don't need the first two lines below in __cmp__ anymore.

```
        if isinstance(right, Primes_class):
            return 0
        return cmp(type(self), type(right))
```


Otherwise, it's a positive review.


---

Comment by mabshoff created at 2009-02-02 18:19:54

This patch causes one doctest failure:

```
sage -t -long "devel/sage/sage/sets/set.py"                 
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/sets/set.py", line 278:
    sage: Primes() < Set(QQ)
Expected:
    True
Got:
    False
**********************************************************************
```


Cheers,

Michael


---

Comment by saliola created at 2009-02-02 21:45:12

Replying to [comment:5 mabshoff]:
> This patch causes one doctest failure:

This is a weird test. I'm not even sure that it says anything meaningful. In fact, according to the documentation of __cmp__ for Set, it doesn't:

```
        \note{If $X < Y$ is true this does \emph{not} necessarily mean
        that $X$ is a subset of $Y$.  Also, any two sets can be
        compared, which is a general Python philosophy.}
```



---

Comment by AlexGhitza created at 2009-04-30 12:42:29

See #5933, which brings the coverage to 100% and was merged in 3.4.2.rc0.


---

Comment by mabshoff created at 2009-05-12 07:01:05

Well, there is still a potential bug fix in here, so can someone take a look and extra a potential fix?

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-10-19 19:26:45

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-10-19 19:26:45

I've rebased the patch of #5933.


---

Comment by mhansen created at 2009-10-19 19:46:49

err, on top of #5933


---

Comment by kcrisman created at 2009-10-20 07:02:53

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-10-20 07:02:53

Positive review. Unless you can provide an easily accessible example of where Primes(False) isn't Primes(True), but perhaps the first place that happens is waaay down the road...


---

Comment by mhansen created at 2009-10-21 04:00:22

Resolution: fixed
