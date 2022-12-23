# Issue 8198: p-adic precision in vector multiplication

Issue created by migration from https://trac.sagemath.org/ticket/8198

Original creator: wuthrich

Original creation time: 2010-02-05 22:52:30

Assignee: roed

CC:  niles jpflori

Keywords: padics vector

Trying to resolve #4656, I found the following unpleasant bug.

this looks good :

```
sage: R = Qp(5,5)
sage: x = R(5).add_bigoh(1)
sage: x
O(5)
sage: x*R(1)
O(5)
```


But when multiplied with the identity matrix the precision is lost

```
sage: I = matrix(R, [[1,0],[0,1]])
sage: v = vector([R(1),x])
sage: v
(1 + O(5^5), O(5))
sage: v*I
(1 + O(5^5), 0)
sage: v[0]*I[1,0] + v[1]*I[1,1]
O(5)
```


This causes things like

```
sage: M = matrix(R,[[1,2],[3,4]])
sage: M*v
(1 + O(5^5), 3 + O(5^5))
sage: v[0]*M[0,0] + v[1]*M[0,1]
1 + O(5)
sage: v[0]*M[1,0] + v[1]*M[1,1]
3 + O(5)
```


This is an even worse example, which could be a different bug

```
sage: vv = vector(x)
sage: vv
(0)
sage: vv[0]
0
sage: x
O(5)
```



---

Comment by wuthrich created at 2010-02-05 22:53:50

I must admit that I have not searched through the tracs to see if this is a duplicate. Sorry.

Resolving the bug would result in the resolution of #4656, too, I believe.


---

Comment by niles created at 2010-08-03 23:24:26

I found this bug also, while working on #9457.  After a fair bit of struggling with elliptic curve code, I now think this is a significant part of the problem.

I noticed the following also; I can't tell if it's the same bug or not.

```
sage: R = QQ.completion(5,5)
sage: P.<T> = R[]
sage: Q.<T> = R[[]]
sage: P(R(0).add_bigoh(-1))
(O(5^-1))
sage: Q(R(0).add_bigoh(-1))
0
sage: P(R(0).add_bigoh(2))
(O(5^2))
sage: Q(R(0).add_bigoh(2))
0
sage: Q(R(1).add_bigoh(2))
1 + O(5^2)
sage: Q(R(1).add_bigoh(-1))
0
sage: Q(R(1/25).add_bigoh(-1))
5^-2 + O(5^-1)
```



---

Comment by niles created at 2010-08-03 23:36:56

Replying to [comment:2 niles]:
> I noticed the following also; I can't tell if it's the same bug or not.

oh, this seems to be the same as #4656


---

Comment by wuthrich created at 2011-01-27 11:32:36

I narrowed down the last issue above. (vector calls Sequence which calls list):


```
sage: R = Qp(5,5)
sage: x = R(5).add_bigoh(1)
sage: list(x)
[0]
```


again the element is set to zero. The problem here is different than the original case. In fact list(x) should raise an error, just like list(0) does. 


```
sage: list([x,x]) 
[O(5), O(5)]
```


works correctly. So this is really about matrix multiplication.


---

Comment by wuthrich created at 2014-02-02 15:06:16

Note the very last bug, is not longer a problem in 6.1 as `vv = vector(x)`
raises the error
 `TypeError: this local element is not iterable`
and that should be ok.


---

Comment by wuthrich created at 2014-02-02 15:39:10

I don't even understand where vector * matrix multiplication is implemented...


---

Comment by pbruin created at 2014-04-11 01:31:34

Replying to [comment:8 wuthrich]:
> I don't even understand where vector * matrix multiplication is implemented...
In `sage/matrix/matrix0.pyx` (I discovered this when working on #804).  It tries to be too smart for its own good and skips entries of the vector that are equal to 0...  I made a patch and am now testing it.


---

Comment by pbruin created at 2014-04-11 01:43:32

Changing status from new to needs_review.


---

Comment by pbruin created at 2014-04-11 01:43:32

Changing component from padics to linear algebra.


---

Comment by wuthrich created at 2014-04-11 16:23:04

Changing status from needs_review to positive_review.


---

Comment by wuthrich created at 2014-04-11 16:23:04

Good. All tests pass.

I was not certain about the changes as I am not completely fluent in cython. Having read documentations, I think they make sense. I tested the speed in a few very limited cases and it does not seem to me that the new code is slower or faster (except of course when the field is Qp). 

Thanks for the help.


---

Comment by pbruin created at 2014-04-11 17:03:55

Thanks; hopefully this goes some way towards being able to fix the related tickets #4656, #5075 and #9457...


---

Comment by vbraun created at 2014-04-13 19:33:32

Resolution: fixed
