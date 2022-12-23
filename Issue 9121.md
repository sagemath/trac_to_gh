# Issue 9121: sage-4.4.3.alpha1: set.py doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/9121

Original creator: was

Original creation time: 2010-06-03 03:23:06

Assignee: tbd

This test now fails, since it really just compares types and as sage grows types get loaded into different places in memory:

```
            sage: Primes() < Set(QQ)
            True
```



---

Comment by was created at 2010-06-03 03:26:56

I noticed a bug while looking at the relevant code in __cmp__:

```
        if not isinstance(right, Set_object):
            return cmp(type(right), type(Set_object))
        return cmp(self.__object, right.__object)
```

Notice that the first compare is totally backwards!   Interestingly, fixing this does fix the above bug.  Patch attached.


---

Comment by was created at 2010-06-03 03:26:56

Changing status from new to needs_review.


---

Attachment


---

Comment by fbissey created at 2010-06-03 09:25:13

I actually reported [http://trac.sagemath.org/sage_trac/ticket/9004](http://trac.sagemath.org/sage_trac/ticket/9004)
on that expression - the test has failed for a long time on sage-on-gentoo.
I didn't notice the backwardness and did something slightly different,
but the backwardness explain a lot of things.
I think you should have a look at it and mark one of them a duplicate.


---

Attachment


---

Comment by was created at 2010-06-03 16:00:28

fbissey -- you're right.  Both of our patches are wrong, but together they are right.  

Note that I'm marking this test random, since it is a comparison of types, which is architecture and sage-version dependent.


---

Comment by hivert created at 2010-06-03 16:46:52

Replying to [comment:4 was]:
> fbissey -- you're right.  Both of our patches are wrong, but together they are right.  
> 
> Note that I'm marking this test random, since it is a comparison of types, which is architecture and sage-version dependent. 

Note : trac_9121.patch was already merged in sage-4.4.3.alpha1 only trac_9121-part2.patch needs to be merged... The patch looks good to me I'm waiting for the tests to finish.


---

Comment by hivert created at 2010-06-03 17:04:03

Changing keywords from "" to "Sets comparison".


---

Comment by hivert created at 2010-06-03 17:04:03

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-06-03 17:04:03

All tests passed!


---

Comment by was created at 2010-06-04 15:18:19

Resolution: fixed
