# Issue 5009: elementary_divisors for integer matrices: fix doc string

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-01-18 06:32:17

Assignee: was

Keywords: elementary divisor

The doc string for the `elementary_divisors` method in matrix_integer_dense.pyx says

```
The elementary divisors are the invariants of the finite
abelian group that is the cokernel of this matrix. 
```

The word "cokernel" needs to be expanded upon.  I think, from trial and error, that this is computing the cokernel of left multiplication by the matrix, and this needs to be *clearly stated*, especially given other left/right issues with matrices in Sage.  (See #1587, for example.)

Furthermore, give at least one example where the matrix _isn't square_ so we can see a bit more clearly on which side the matrix is acting, say a simple matrix like [[3, 0, 0], [0, 0, 0]].  Maybe even include both this and its transpose.

(As an editorial comment, I find it really annoying that methods like this are for left multiplication, while methods like `restrict_codomain` are for right multiplication, so if I want to use them both, I have to take transposes way too many times.)


---

Attachment


---

Comment by mhansen created at 2009-01-24 15:29:54

Looks good to me.


---

Comment by mabshoff created at 2009-01-28 13:03:03

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 13:03:03

Merged in Sage 3.3.alpha3.

Cheers,

Michael
