# Issue 9940: faster multinomial_coefficients

Issue created by migration from Trac.

Original creator: pernici

Original creation time: 2010-09-18 15:43:36

Assignee: AlexGhitza

With the attached patch multinomial_coefficients(m,n) becomes faster
than the unpatched version as m increases

Sage-4.5.1
sage: %timeit w = multinomial_coefficients(int(20),int(5))
5 loops, best of 3: 4.91 s per loop

with patch:
sage: %timeit w = multinomial_coefficients(int(20),int(5))
5 loops, best of 3: 1.05 s per loop




---

Attachment

I think I got an even faster implementation.
I'm sorry but I don't have a development Sage handy for the next days, so I just put the code here.
If you want to make a clean patch with this, go ahead; otherwise, I will do it in some days when I'm back home.


```
def multinomial_coefficients(m, n):
    if m == 2:
        return binomial_coefficients(n)
    t = [n] + [0] * (m - 1)
    r = {tuple(t): 1}
    if n:
        p0 = 0 # leftmost nonzero position
    else:
        p0 = m
    # enumerate tuples in co-lex order
    while p0 < m - 1:
        # compute next tuple
        j = p0
        tj = t[j]
        t[j+1] += 1
        if j:
            t[0] = tj
            t[j] = 0
        if tj > 1:
            p0 = 0
            start = 1
        else:
            p0 += 1
            start = p0
        # compute the value
        v = 0
        for k in xrange(start, m):
            if t[k]:
                t[k] -= 1
                v += r[tuple(t)]
                t[k] += 1
        t[0] -= 1
        r[tuple(t)] = (v * tj) // (n - t[0])
    return r
```



---

Attachment


---

Comment by ylchapuy created at 2010-09-22 14:39:31

Apply only http://trac.sagemath.org/sage_trac/attachment/ticket/9941/trac9941-even_faster_multinomial_coefficients.patch .
With it applied, I got `260 ms` for the same test on my computer.


---

Comment by ylchapuy created at 2010-09-22 14:39:31

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2010-10-11 06:33:15

up... any chance someone review this ticket?


---

Comment by fwclarke created at 2010-11-14 11:52:58

Changing status from needs_review to needs_work.


---

Comment by fwclarke created at 2010-11-14 11:52:58

I've tested this, and confirmed that the "even_faster" patch is indeed significantly faster and delivers correct results.  It's _almost_ a positive review, except for two minor things:

1. Erroneous results are returned if `m` is zero. E.g.,

 * 

```
sage: multinomial_coefficients(0, 3)
{(3,): 1}
```


To be consistent with `multinomial([])`, which returns `1`, `multinomial_coefficients(0, n)` should return `{(), 1)}` if `n` is zero, and `{}` otherwise.

2. I don't understand the comment "`the very first step was mixed above"`, the word _mixed_ in particular.

One other thing that might be worth changing would be to allow `multinomial` to take a tuple as its argument.  Then `multinomial_coefficients` could have a doctest like


```
sage: r = multinomial_coefficients(4, 3)
sage: all(multinomial(k) == v for k, v in r.items())
True
```



---

Attachment

I attached a patch to be applied after the 'even_faster' one.

It corrects the behavior for `m=0`. It also change the comment.
I just wanted to say that the initialization of v (which is part of the computation of the value) is done within the code for enumerating the tuples.

Regarding the modification of `multinomial`, I leave this for another ticket.


---

Comment by fwclarke created at 2010-11-15 07:54:39

Changing status from needs_work to positive_review.


---

Comment by fwclarke created at 2010-11-15 07:54:39

Fine now with these two patches.  Positive review.


---

Comment by jdemeyer created at 2010-12-02 14:39:31

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-12-02 14:39:31

You should add an example/test for the last patch, i.e. for the case m = 0.


---

Attachment


---

Comment by ylchapuy created at 2010-12-02 19:47:44

Here it is. Apply in order:

 * trac9941-even_faster_multinomial_coefficients.patch
 * trac9941-corrections.patch
 * trac9941_second_review.patch


---

Comment by ylchapuy created at 2010-12-02 19:47:44

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2010-12-02 21:22:18

The new patch does the job.


---

Comment by fwclarke created at 2010-12-02 21:22:18

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-12 06:33:15

Resolution: fixed
