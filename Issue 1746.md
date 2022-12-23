# Issue 1746: add p-norm as a method to vectors (probably very easy)

Issue created by migration from https://trac.sagemath.org/ticket/1746

Original creator: was

Original creation time: 2008-01-10 10:44:22

Assignee: was


```


On Jan 10, 2008 12:17 AM, vgermrk <vgermrk@googlemail.com> wrote:
> 
> [Sorry for asking so much "Is there a ... function in Sage?" -
> Questions.]
> 
> But: Is there a native way to compute the p-Norm (e.g. euclidean oder
> maximum norm) of a vector?
> 

There is no built in function, but we can write one easily:

def pnorm(v, p):
      return sum([a^p for a in v])^(1/p)


Then:

sage: pnorm(vector([1,2,3]), 5)
276^(1/5)
sage: pnorm(vector(RDF, [1,2,3]), 5)
3.07738488539
sage: var('a b c d p')
sage: pnorm(vector([a, b, c, d]), p)
(d^p + c^p + b^p + a^p)^(1/p)

 -- William
```



---

Comment by was created at 2008-01-10 10:44:45

Changing type from defect to enhancement.


---

Comment by jkantor created at 2008-01-10 10:55:07

for RDF and CDF vectors

```
from numpy import linalg
v=vector(RDF,[1,2,3])
linalg.norm(v,5)
```

3.0773848853940629


---

Comment by jkantor created at 2008-01-10 10:57:16

In the above example it should be 

`linalg.norm(v.numpy(),5)`


---

Attachment


---

Comment by schilly created at 2008-01-11 21:34:05

does this also work for matrices? matrix norms are at least equally important!


---

Comment by was created at 2008-01-11 21:37:31

What is the defn of matrix p-norms?  Is it the same?


---

Comment by AlexGhitza created at 2008-01-12 09:36:19

I agree that matrix norms are important.  However, unlike the case of vectors, where the p-norm is rather universally agreed upon, there are a bunch of different definitions for norms on matrices, see
http://en.wikipedia.org/wiki/Matrix_norm
There are at least 3 different things denoted as p-norm there.

I think it's important for us to do this, but trickier than the vector case, so I've made it into track #1763.

In the meantime, it would be great if someone reviewed the current patch.


---

Comment by mabshoff created at 2008-01-20 00:51:53

Merged in Sage 2.10.1.alpha0


---

Comment by mabshoff created at 2008-01-20 00:51:53

Resolution: fixed
