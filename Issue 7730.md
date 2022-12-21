# Issue 7730: hessenberg_form hangs (or is *very* slow)

Issue created by migration from Trac.

Original creator: spancratz

Original creation time: 2009-12-18 02:53:45

Assignee: AlexGhitza

Keywords: matrices, hessenberg form

I heard of the following bug report through William.

Bug report
----------

Simple 8X8 matrix determinant computation makes sage hang:


```
def genVar(i):
    return "x%i"%i

def matrix_from_hash(h):
    R=FractionField(PolynomialRing(GF(2),",".join(map(genVar,range(0,10)))))
    h2 = {}
    for p in h:
        x=R.zero_element()
        for v in h[p]:
            x=x+R.gens()[v]
        h2[p] = x
        h2[p[1],p[0]] = x
    return matrix(h2,sparse=False)

def test():
    m = matrix_from_hash({(0, 1): [0, 5], (1, 2): [0], (5, 6): [2], (6, 7): [1], (4, 5): [4], (0, 7): [1, 7], (0, 6): [2, 1], (0, 5): [4, 2], (0, 4): [3, 4], (2, 3): [6], (0, 3): [6, 3], (3, 4): [3], (0, 2): [0, 6]})
    print m
    m.charpoly()
```


On the other hand if m.det() is replaced m.inverse(), it runs through in no time.

The determinant of the matrix is a sum of two monomials: ``x1*x4*x5*x6 + x0*x2*x3*x7``, but even the most primitive implementation (summing all 8! permutations,most of them zero) should run through in much less than minute.

Notes
-----

I could only look at this briefly so far.  The problem is --- this is perhaps unexpected --- not with the more recent implementation of "_charpoly_df".  In fact, in the method "charpoly", the method selected is "_charpoly_hessenberg".  Both methods "hessenberg" and "hessenbergize" reveal this problem.


---

Comment by spancratz created at 2009-12-18 02:56:10

Changing assignee from AlexGhitza to spancratz.


---

Comment by spancratz created at 2009-12-27 23:22:40

Code demonstrating the problem


---

Attachment

I've come a little closer to isolating the problem.  Using the matrix from the code in the problem description and the notation from the method ``hessenbergize`` in file ``matrix2.pyx``, the first problematic case occurs when ``m = 4`` (in the outer loop) and ``j = 5`` (in the inner loop).  This is the point at which the size of the elements that are considered changes from a couple of lines to something filling more than one screen (at a little over 80 characters per line).

Then, in the call to ``add_multiple_of_row_c`` (in the file ``matrix0.pyx``) at the iteration ``c = 4`` in the inner loop an expression of the form `x + a*y` is formed.  The attached file ``x.sage`` contains that particular case as follows:

    sage: x, a, y = test_problem()

Now the easier expression ``a*y`` already causes Sage to hang.  I can't see an easy reason for why this computation shouldn't finish, I guess it's just that *fraction fields* of multivariate polynomial rings are very slow in the current implementation.  In any case, I'll run the code on an idle machine in a few minutes and post here again in the next few days.

Sebastian


---

Comment by was created at 2009-12-29 08:37:03

> Now the easier expression a*y already causes Sage to hang. 
> I can't see an easy reason for why this computation shouldn't 
> finish, I guess it's just that *fraction fields* of multivariate 
> polynomial rings are very slow in the current implementation. 
> In any case, I'll run the code on an idle machine in a few minutes 
> and post here again in the next few days. 

Unsubstantiated guess: Maybe Singular is taking a GCD, and GCD's in Singular suck?

We *really* need to write our own polynomial GCD, already...


---

Comment by spancratz created at 2010-01-04 10:53:58

I spent some more time on this.  The attached file `x2.sage` as before a method `test_problem()`.  To find out when things turn from acceptably slow to ridiculously slow, I added one term after the other to the numerator polynomial of ``a`` (in the notation as before).  I think the two elements ``b`` and ``c`` display the problem quite well, exhibiting vastly different timings despite ``c`` only including one additional monomial term:


```
    sage: x,a,b,c,y = test_problem()
    sage: timeit('_ = b*y', number=1, repeat=1)
    1 loops, best of 1: 1.5 s per loop
    sage: timeit('_ = c*y', number=1, repeat=1)
    1 loops, best of 1: 1.79e+13 ns per loop
```


By the way, the second timing is about 4.97 hours and the output ``1.79e+13 ns`` should perhaps be improved.  Is the ``timeit`` command something imported from an outside package (and thus _perhaps_ difficult to change), or something that can easily be changed within the Sage code?

Anyway, I am a little puzzled about this problem at the moment as I don't quite see how the implementation of this should be this sensitive to the input.  I'll try to break it down to the level of multiplications and GCDs next.

Finally, regarding the computation of ``a*y``, which I had started on another machine, well, I terminated it this morning after running for 180 hours and a peak memory usage of over 1.1GB.

Sebastian


---

Comment by spancratz created at 2010-01-04 10:55:33

Code exhibiting the problem more clearly (on the level of fraction fields)


---

Attachment

This is mostly just to confirm that the problem is indeed the multivariate polynomial GCD.  I don't know much about this at the moment, but I am writing an email to Martin Albrecht, who I think wrote the libSINGULAR interface, to ask whether he has any suggestions.

However, there is another possible improvement that here would push the problem a little further away (to instances of about twice the size, I guess), but I think it should also be done in general:

In the generic fraction field implementation, in order to compute the product a/b * c/d, we first compute a*c and b*d, then form their GCD and finally divide both the numerator and the denominator by this.  This could be computed much faster if we assumed (or even checked and ensured, if necessary!) that a/b and c/d are in lowest terms and then compute GCD(a,d) and GCD(b,c) instead.

I think this might affect the fraction field implementation a lot though, since it affects the assumptions about when elements are in lowest terms and when not.  I guess that this is something that ought to be discussed on sage-devel, right?

Sebastian


---

Comment by kedlaya created at 2016-08-16 23:40:58

Awakening a moribund ticket here...

I just reran the initial example in 7.3, and it still seems to hang; but Sebastian's example no longer exhibits the same behavior:

```
sage: x,a,b,c,y = test_problem()
sage: timeit('_ = b*y', number=1, repeat=1)
1 loops, best of 1: 15.4 ms per loop
sage: sage: timeit('_ = c*y', number=1, repeat=1)
1 loops, best of 1: 10.8 ms per loop
```

so maybe this problem hasn't been isolated after all.


---

Comment by kedlaya created at 2020-08-16 03:30:05

Updated the code fragment for Sage 9.2 (the method `zero_element` is gone, replaced by `zero`; and of course `print` needs parens now). The original issue stands.
