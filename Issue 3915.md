# Issue 3915: [with patch, needs review] PolyBoRi interface improvements

Issue created by migration from https://trac.sagemath.org/ticket/3915

Original creator: malb

Original creation time: 2008-08-20 20:02:48

Assignee: malb

CC:  burcin

Keywords: polybori

The attached patch
 * adds an `interpolation_polynomial` method to `BooleanPolynomialRing`
 * adds `reduce` methods to `BooleanPolynomial` and `BooleanPolynomialIdeal`
 * improves the documentation slightly
 * makes `f in I` work for f a `BooleanPolynomial`


---

Comment by malb created at 2008-08-20 20:03:43

oh, it also adds a `_latex_` method to `BooleanPolynomial`


---

Comment by PolyBoRi created at 2008-08-27 14:21:32

The line:

```
g.minimalizeAndTailReduce()
```

is nearly meaningless, as it ignores the result.
For having a reduced system set
the keyword
redsb=True
for the groebner_basis call.
Furthermore, your reduce implementation doesn't necessarily yield a unique (reduced) normal form.
For PolyBoRi >0.4 set
strat.optRedTail=True
for PolyBoRi <0.4
apply
p=red_tail(strat,p)
to a normal form.
Michael


---

Comment by malb created at 2008-08-27 16:30:48

Thanks for the review. The updated patch should address your comments.


---

Comment by PolyBoRi created at 2008-08-28 06:54:15

Looks good,
there is still some minor thing, I detected.
But this is nothing about the patch, as it was buggy before:

It is possible to pass a deg_bound to
groebner_basis
.
So the result is not garantied to be a GB.
In this case it looks strange to set

```
self.__gb = g
```


maybe you can check this
via

```
if kwds.get("deg_bound",False) is False:
  self.__gb = g
```


Then I'll give it a positive review.
Michael


---

Comment by PolyBoRi created at 2008-08-28 07:14:08

ups: still, comments regarding the patch:
These are optional, as they only concern performance:

pbori.pyxline 3144

```
            s = sum([prod([x[i] for i in xrange(n) if v[i]],  
	            B.one_element()) for v in s],  
                    B.zero_element()) 
            s = s.set()
```

should be faster with

```
            s=BooleSet(sum([prod([x[i] for i in xrange(n) if v[i]],  
	            B.one_element()) for v in s]
```

However, you will have to handle the case of the empty set seperately(when there are no monomials) to make sure, that it is the right ring.
I think, if we can make this easier upstream.

Furthermore, if you really want to be clever: The use of prod is quite unoptimal here.
If you really want get these multiplications for variables fast, you should
multiply them in this way:
x1*(x2*(x3*x4)))
So first use the indices behind. Note, that indices in PolyBoRi don't have to be identical to those in sage/Singular
lex, degree lex: identical
dp(dp_asc): reversed.
Blocks of degree lexicographical: identical
Blocks of degree reverse lex. : reversed in each block, so quite strange
(if it is correctly implemented in sage)


---

Attachment


---

Comment by malb created at 2008-08-28 10:36:46

Replying to [comment:4 PolyBoRi]:
> It is possible to pass a deg_bound to groebner_basis.

I check for `deg_bound` in the updated patch. Thanks a lot for your detailed criticism, it helps (me) a lot! I give the patch a positive review now, since you wrote:

> Then I'll give it a positive review. Michael


---

Comment by malb created at 2008-08-28 10:38:37

Replying to [comment:5 PolyBoRi]:
> ups: still, comments regarding the patch:
> These are optional, as they only concern performance:
> 
> pbori.pyxline 3144
> s=BooleSet(sum([prod([x[i] for i in xrange(n) if v[i]], B.one_element()) for v in s]

It seems we didn't implement BooleSet(BooleanPolynomial) in Sage. I'll check the upstream implementation and fix that.

> If you really want get these multiplications for variables fast, you should
> multiply them in this way:
> x1*(x2*(x3*x4)))

I don't do anything fancy for now, but I reversed the order of the product. This might be faster in the normal case which is lex if I understand your comment correctly.


---

Comment by PolyBoRi created at 2008-08-28 10:43:05

> 
> It seems we didn't implement BooleSet(BooleanPolynomial) in Sage. I'll check the upstream implementation and fix that.

sorry, the line was long, without the sum:
just

```
BooleSet([prod([x[i] for ...]
```


A BooleSet is a set of monomials.
It uses a more sophisticated addition.

> 
> > If you really want get these multiplications for variables fast, you should
> > multiply them in this way:
> > x1*(x2*(x3*x4)))
> 
> I don't do anything fancy for now, but I reversed the order of the product. This might be faster in the normal case which is lex if I understand your comment correctly.

yes, it is much faster in Lex, even from a Python interpreter with boost::python calling overhead (in large examples, high degree monomials)

You have my positive review :-).


---

Comment by mabshoff created at 2008-08-28 10:59:54

I am seeing slight merge issues with my current alpha2 tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/devel/sage$ patch -p1 < trac_3915_pbori_improvements.patch
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 FAILED at 391.
Hunk #2 succeeded at 1948 (offset 47 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
```

The failing hunk deletes `contains`, so this should be easy to rebase.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-28 22:30:44

Martin suggested in IRC just to delete the hunk that fails to apply manually. The reject is cause by some other code being applied in alpha2, so I will sort this out by posting an updated patch of Martin's patch and a second patch that deletes the hunk in question.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-29 01:42:44

rebased patch of malb's - all that needed fixing was plot's parameter list


---

Attachment

Merged trac_3915_pbori_improvements.patch in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-29 01:43:08

Resolution: fixed
