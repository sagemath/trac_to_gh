# Issue 8719: convert RDF/CDF matrices to numpy

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-04-20 00:07:17

Assignee: jason, was

CC:  rbeezer

This patch makes the following work:


```
            sage: import numpy
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)                  
            array([[ 0.,  1.,  2.],
            [ 3.,  4.,  5.]])
            sage: numpy.array(m).dtype            
            dtype('float64')
            sage: m = matrix(CDF, 2, range(6)); m
            [  0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)                  
            array([[ 0.+0.j,  1.+0.j,  2.+0.j],
            [ 3.+0.j,  4.+0.j,  5.+0.j]])
            sage: numpy.array(m).dtype            
            dtype('complex128')
```



---

Comment by jason created at 2010-04-20 00:11:50

Changing status from new to needs_review.


---

Comment by jason created at 2010-05-03 19:01:08

Changing assignee from jason, was to jason.


---

Comment by jason created at 2010-05-03 19:01:50

rbeezer: it seems like you could naturally review this.  It just adds a numpy-specific magic method for conversion.


---

Comment by rbeezer created at 2010-05-04 04:16:53

Hi Jason,

So you have defined a new method "`__array__`" for a Sage matrix object.  When somebody calls numpy.array(a) for a Sage matrix  a  then this `__array__` method gets called (and this is in effect just the numpy() method of a Sage matrix)?  In other words, the numpy.array() method has an expanded reportoire and now "knows" how to deal with a Sage matrix object?

If so, could you say so?  The line  `__array__=numpy` all by itself looks really mysterious with no documentation.  And the new doctests say "you could use numpy" - when Sage is really doing the heavy-lifting?  It sounds like numpy is doing the work, when this is not a standard behavior of numpy.

So I'm suggesting maybe this seemingly circular arrrangement (modify Sage matrices, so numpy can deal with them, using a Sage function to convert to a numpy array) could be better explained so nobody messes it up or gets too confused.  With the added code and the added doctests all together, I think I was able to figure this out - otherwise it would have been a head-scratcher.

Rob


---

Attachment


---

Comment by jason created at 2010-05-04 05:11:47

I updated the docs.


---

Comment by rbeezer created at 2010-05-04 06:27:03

Replying to [comment:7 jason]:
> I updated the docs.

Looks good!  I'll finish this tomorrow night.


---

Comment by rbeezer created at 2010-05-05 06:10:27

Looks good, builds and passes all tests, documentation builds without warnings.

The added documentation looks great.

Positive review.


---

Comment by rbeezer created at 2010-05-05 06:10:27

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 22:03:13

Resolution: fixed
