# Issue 1188: unexpected results after LLL?

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-16 21:48:40

Assignee: was

Consider this example from the Magma handbook:

```
# n integers which's GCD we are interested in
sage: Q = [ 67015143, 248934363018, 109210, 25590011055, 74631449, 10230248, 709487, 68965012139, 972065, 864972271 ]
sage: n = len(Q)
sage: S = 100 
sage: X = Matrix(IntegerRing(), n, n + 1)
sage: for i in xrange(n):
...     X[i,i + 1] = 1
sage: for i in xrange(n): 
...     X[i,0] = S*Q[i]
sage: L = X.LLL()
sage: show(L)
sage: M = L[n-1].list()[1:]
sage: add([Q[i]*M[i] for i in range(n)])
864972271
```


which isn't quite right, we expect:

```
# n integers which's GCD we are interested in
sage: Q = [ 67015143, 248934363018, 109210, 25590011055, 74631449, 10230248, 709487, 68965012139, 972065, 864972271 ]
sage: n = len(Q)
sage: S = 100 
sage: X = Matrix(IntegerRing(), n, n + 1)
sage: for i in xrange(n):
...     X[i,i + 1] = 1
sage: for i in xrange(n): 
...     X[i,0] = S*Q[i]
sage: L = X.LLL(algorithm='NTL:LLL')
sage: show(L)
sage: M = L[n-1].list()[1:]
sage: add([Q[i]*M[i] for i in range(n)])
-1
```


Is this my lack of understanding of LLL reduction or is this a bug?


---

Comment by zimmerma created at 2007-11-16 22:50:29

I get -1 with both X.LLL() and X.LLL(algorithm='NTL:LLL') on a Pentium M with sage-2.8.12.
Maybe a processor-specific problem?


---

Comment by malb created at 2007-11-17 13:23:07

My processor is a Core2Duo which I use in 64-bit mode (Debian/testing AMD64). I can also reproduce this bug on sage.math (64-bit Opteron). So I assume this is an issue with 64-bit architectures.


---

Comment by malb created at 2007-11-17 14:26:07

Changing status from new to assigned.


---

Comment by malb created at 2007-11-17 14:26:07

Changing priority from major to blocker.


---

Comment by malb created at 2007-11-17 14:26:07

Changing assignee from was to malb.


---

Comment by malb created at 2007-11-17 14:26:07

I upgraded this bug to a blocker as it is a bug which leads to wrong results without raising an error.


---

Comment by was created at 2007-11-18 20:28:40

One quick point is at least the result is still a basis for the correct lattice:


```
A = X.row_module()
B = L.row_module()
A == B
///
True
```


so it's returning something that is a basis for the correct lattice.  But maybe it's not LLL reduced. 

We should write a function to determine whether or not a matrix is LLL reduced, i.e., use the LLL criterion, as described in Section 2.6 of Cohen's book. 

If the output isn't LLL reduced, then there is definitely a bug.  

Anyway, I am going to attempt to implement this criterion right now, and see what
happens.


---

Comment by was created at 2007-11-18 21:51:09

OK, I wrote a program to compute Gramm-schmidt form, in order to check the LLL criterion.  I tried it on the above output L (I will post this elsewhere when I finish documenting it: http://trac.sagemath.org/sage_trac/ticket/1201).  It is DEFINITELY THE CASE THAT NTL is getting things *wrong* here.  When transforming the rows of L into orthogonal form using LLL a coefficient mu_ij of 68719476736.0213 appears, which is > 1/2, so the resulting matrix is not LLL reduced.  This this is still thus a major blocker.  

One "fix" would be to have it print a big warning no matter what on 64-bit, which
would at least allow us to release.  But this really needs to get fixed / understood.


---

Comment by wjp created at 2007-11-19 00:42:23

Correction to the above comment: fpLLL gets things wrong, not NTL.

Currently Sage doesn't check the return value of the LLL() calls in fplll.pyx (zero = ok, non-zero = error). When adding that, it turns out that for this example fpLLL itself detects something is wrong.


---

Comment by wjp created at 2007-11-19 02:35:00

In at least two places, fpLLL was assuming longs and ints were the same size. The patch I'm attaching should fix those. I already e-mailed Damien Stehle about this, too.


---

Comment by wjp created at 2007-11-19 02:35:47

fpLLL-2.1.3 64-bit patch


---

Attachment

A new spkg is available at:

http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.4-20071119.spkg

malb will add a doctest to verify this issue has really been fixed. Once that is merged we can hopefully close this ticket.

Cheers,

Michael


---

Comment by malb created at 2007-11-19 10:52:31

doctests + documentation update


---

Attachment

malb: The error codes from LLL() are positive when an error occurs. Attaching an updated (non-hg) patch that replaces the ret < 0 checks by ret != 0.


---

Attachment

updated fplll.patch


---

Comment by malb created at 2007-11-19 11:53:21

On IRC:

```
[11:46] <wjp> malb: I slightly updated your fplll patch replacing ret < 0 by ret != 0 since fpLLL returns positive values on error
[11:46] <malb> I disagree
[11:46] <malb> are you sure it has to be an error if !=0 ?
[11:47] <malb> it just returns kappa, doesn't it?
[11:47] <wjp> only in error case, as far as I can tell
[11:47] <malb> the example will not work if you test for ret != 0
[11:47] <malb> i.e. the doctest I just added
[11:48] <wjp> that's strange; I'll look through the fplll sources again then
[11:48] <malb> also heuristic may return kappa != 0 because it is not guaranteed to be LLL reduced anyway
[11:48] <malb> I only superficially scanned the source though
[11:48] <wjp> hm, so it might not be usable as an error code
[11:49] <malb> yes, but I am not sure, we could ask Damien?
```



---

Comment by was created at 2007-11-20 15:38:17

#1188 looks good -- make sure to only apply fplll2.patch instead of fplll.patch.

And wow or wow wjp did a great job on that one in multiple ways!


---

Comment by mabshoff created at 2007-11-20 15:55:11

Merged in 2.8.13.rc1. - see #1217 for followup.

I would like to close this ticket. I did apply the doctest.patch and updated to the latest upstream libfplll.spkg that malb provided.


---

Comment by mabshoff created at 2007-11-20 15:55:11

Resolution: fixed
