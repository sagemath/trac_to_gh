# Issue 277: Add generic_discrete_logarithm and order computation using Pollard's rho algorithm

Issue created by migration from https://trac.sagemath.org/ticket/277

Original creator: ncalexan

Original creation time: 2007-02-22 23:53:02

Assignee: was

Keywords: discrete log shanks pollard rho order group structure

The computational cost of Shanks' Baby-Step Giant-Step algorithm and Pollard's rho and lambda algorithms are more or less the same, but the memory costs is much worse for Shanks' algorithm.  It would be nice to have better discrete log algos and group structure computations, ala E. Teske, A Space Efficient Algorithm for Group Structure Computation (1998).


---

Comment by was created at 2007-02-24 03:04:40

Remove assignee was.


---

Comment by dmharvey created at 2007-08-29 18:48:56

See also Sutherland's thesis

http://theory.lcs.mit.edu/~cis/theses/sutherland-phd.pdf

which gives a better algorithm for computing group orders


---

Attachment

patch applies to 2.10.3.rc0 after 8682.patch in #2356


---

Comment by cremona created at 2008-03-02 22:37:40

The attached patch (8758.patch) is a first stab at doing these things more generically.  For any multiplicative or additive situation the new version of discrete_log_generic() now works, using a baby-step-giant-step approach.  For example (see doctest) this gives a BSGS implementation of DLOGS for elliptic curves.

If people think this is a reasonable way to go (and it is certainly a simple interface) then there is more which can be added very easily:  a more general BSGS function (solve `a=b^n` with `n` in some specified interval) which would be called by discrete_log() and also allow for computation of orders of elements in any group, etc.

Then one could have other algorithms implemented in the same framework such as Pollard Rho or the more sophisticated ones mentioned in earlier comments.

More comments please!


---

Comment by cremona created at 2008-03-02 22:37:40

Changing component from number theory to group_theory.


---

Comment by robertwb created at 2008-03-04 06:16:24

I like it. 

One comment I have is that you might want to look at the python `operator` module rather than using lambda functions. 


```
sage: _ = var('x,y')
sage: operator.neg(x)
-x
sage: operator.add(x,y) # the order is actually respected, this is just a maxima thing
y + x
sage: operator.invert(x)
1/x
sage: operator.mul(x,y)
x*y
```



---

Comment by cremona created at 2008-03-04 09:22:41

apply after 8758.patch


---

Attachment

I liked the suggestion of using operators: 8759.patch does that (needs to be applied after 8758.patch).  At the same time it adds some more doctests, and makes a couple of minor efficiency savings.

If there are going to be more generic functions like this (and I hope there are) we need a better place for them than rings/arith.py.  I see that in structure/element.pyx there are also some generic things, including generic powering.  Perhaps this function should be moved to a new .py file under structures?  Or at least renamed generic.py.


---

Comment by robertwb created at 2008-03-04 11:30:54

Looks and works great. 

As far as your comments of a new .py file for generic functions, most of them will make sense in a category and will go there (in which case they will be automatically attached to every element and/or object of that category).


---

Comment by cremona created at 2008-03-04 18:01:22

Thanks for the positive review.

Note that these patches do not fulfill all the wish-list requirements, so while I hope they can be merged as soon as possible, the ticket should be be closed.  If that is possible!


---

Comment by mabshoff created at 2008-03-05 00:21:40

Resolution: fixed


---

Comment by mabshoff created at 2008-03-05 00:21:40

Merged both patches in Sage 2.10.3.rc2
