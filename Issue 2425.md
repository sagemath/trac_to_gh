# Issue 2425: [with patch; needs review] In multipolynomials, the function jacob() should be called gradient()

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2008-03-07 23:08:54

Assignee: jbandlow@gmail.com

Keywords: jacob, gradient

On Fri, Feb 29, 2008 at 1:58 PM, Jason Bandlow <jbandlow`@`gmail.com> wrote:

Hi,

Currently, if f is a multi-polynomial, the call f.jacob() returns the
list of partial derivatives of f with respect to the ring generators:

```
  sage: R.<x,y,z> = PolynomialRing(QQ)
  sage: f = x^4 + y^3 + z^2 + x*y*z
  sage: f.jacob()
  [4*x^3 + y*z, 3*y^2 + x*z, x*y + 2*z]
```




I'd like to change the name to gradient. Another possibility is changing
the name to 'jacobian', but I think it's likely that more people (eg
calculus students) will recognize the term 'gradient' and not 'jacobian'
than vice-versa.  And who talks about the Jacobian of a single function
anyway? :)



---

Attachment


---

Comment by mabshoff created at 2008-03-08 00:12:59

Changing component from Cygwin to commutative algebra.


---

Comment by malb created at 2008-03-08 12:21:09

Review: If the submitter reports that `make test` passes with the patch applied, I'm happy to give it a positive review.


---

Comment by cremona created at 2008-03-08 16:41:04

I applied the patch successfully to 2.10.3.rc0 and the test passed ok.

I did a search_source to see if there were any other mentions of "jacob(" and found just one, in interfaces/singular.py.  Here I found the example

```
    sage: R = singular.ring(0, '(x,y,z)', 'dp')
    sage: f = singular('x3+y3+(x-y)*x2y2+z2')
    sage: f
    x^3*y^2-x^2*y^3+x^3+y^3+z^2
    sage: R1 = singular.ring(0, '(x,y,z)', 'ds')
    sage: f = R.fetch(f)
    sage: f
    z^2+x^3+y^3+x^3*y^2-x^2*y^3

We can calculate the Milnor number of $f$:
    sage: _=singular.LIB('sing.lib')     # assign to _ to suppress printing
    sage: f.milnor()
    4

The Jacobian applied twice yields the Hessian matrix of $f$,
with which we can compute.
    sage: H = f.jacob().jacob()
    sage: H
    6*x+6*x*y^2-2*y^3,6*x^2*y-6*x*y^2,  0,
    6*x^2*y-6*x*y^2,  6*y+2*x^3-6*x^2*y,0,
    0,                0,                2
```


which suggests that the name jacob() is standard in singular.  Should there be any sort of cross-reference between the new gradient() and the new jacob() ?


---

Comment by jbandlow created at 2008-03-08 18:56:35

So, if the current patch is applied, all tests seem to pass, and we'll have the following situation: If singular is called explicitly, jacob() will work and gradient() won't.  If singular is not called explicitly, gradient() will work and jacob() won't. 

Adding gradient() obviously doesn't hurt anybody, but for people used to singular, we are would be removing 'jacob()' which they may be used to.  Of course, it's trivial to put jacob() back in, and have it point to gradient(), but the cost is clutter when the user does `sage: f.<tab>`.  Is this clutter worth it to keep people who are used to singular happy?  I have no idea how to answer this question.


---

Comment by malb created at 2008-03-09 15:27:10

Generally speaking 'we' don't aim for this kind of compatibility with Singular, i.e. same names for methods etc.. Sage is object oriented, Singular is not, in Singular an ideal is equivalent with its list of generators, in Sage it is not, etc. So renaming `jacob()` to `gradient()` is fine in my books.


---

Comment by cremona created at 2008-03-09 17:12:17

I think the above counts as "positive review" so I am relabelling the ticket.


---

Comment by mabshoff created at 2008-03-09 19:11:46

I agree. Merged in Sage 2.10.3.rc4


---

Comment by mabshoff created at 2008-03-09 19:11:46

Resolution: fixed
