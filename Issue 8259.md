# Issue 8259: Conversion from symmetric polynomials to basis of monomial symmetric functions

Issue created by migration from https://trac.sagemath.org/ticket/8259

Original creator: aschilling

Original creation time: 2010-02-14 00:22:35

Assignee: sage-combinat

CC:  jbandlow sage-combinat

Keywords: symmetric functions

Currently a function that converts a symmetric polynomial into the monomial basis is missing in sage. Jason Bandlow wrote a first version which should be integrated into sage:

def toSF(f):
    """ Input is a symmetric polynomial in a polynomial ring in finitely
    many variables.  Output is a symmetric function in the monomial
    basis of the ring of symmetric functions over the same base ring.
    """
    X = f.parent().gens()
    n = f.parent().ngens()
    SF = SymmetricFunctions(f.base_ring())
    m = SF.monomial()
    out = m(0)
    while f != 0:
        lt = f.lt()
        c = lt.monomial_coefficient(lt)
        p = Partition(lt.exponents()[0])
        f += -c*m(p).expand(n,X)
        out += c*m(p)
    return out


---

Comment by aschilling created at 2010-02-20 05:30:58

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-02-21 23:44:39

Has this been checked on Solaris?

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by aschilling created at 2010-02-22 02:54:03

Dave,

Are you sure you posted this comment to the correct ticket?

If so, could you please comment on the relevance of Solaris to 
the code?

Thanks,

Anne

Replying to [comment:4 drkirkby]:
> Has this been checked on Solaris?
> 
> There's general information about building on Solaris at
> 
>  http://wiki.sagemath.org/solaris
> 
> Information specifically for 't2' at
> 
>  http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2
> 
> Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html
> 
> Dave


---

Comment by jbandlow created at 2010-02-22 20:38:43

Hi Anne,

The fix to crystals.py doesn't apply to either sage 4.3.2 or sage 4.3.3.  Can it be removed from this patch?

Thanks,
Jason


---

Comment by jbandlow created at 2010-02-22 21:05:43

One more thing.  I would really like to have an option to verify that the input actually is a symmetric function.  In fact I think this should be true by default.  So the key function would look something like this:


```
def from_polynomial(self, f, check=True):        
    assert(self.base_ring() == f.base_ring()
    d = dict([(e,c) for e,c in f.dict().iteritems() if tuple(sorted(e)) == tuple(reversed(e))]) 
    if not check:
        return self.sum(d[la]*self(Partition(la)) for la in d.keys())
    out = self.sum(d[la]*self(Partition(la)) for la in d.keys())
    assert( out.expand(f.parent().ngens(),f.parent().gens()) == f )
    return out
```



---

Comment by aschilling created at 2010-02-23 02:42:02

Hi Jason,

I attached a revised patch which includes your suggestion to add the option to test
whether the polynomial is symmetric.

For me the patch applied to sage-4.3.3. It depends on trac tickets #7978 and #8154
which have been merged in sage-4.3.3. Hence it might not apply cleanly to sage-4.3.2.

Anne


---

Attachment


---

Comment by aschilling created at 2010-02-23 18:51:35

Hi Jason,

As we just discussed on the phone, I did revert the indentation of class Element
in /combinat/sf/monomial.py back to the same level as
class SymmetricFunctionAlgebra_monomial

However, I did change the indentation to be multiples of 4 rather than multiples 
of 3. I sent an e-mail to sage-combinat-devel to ask about the indentation issues
in sf.

Anne


---

Comment by jbandlow created at 2010-02-23 21:54:55

Changing status from needs_review to positive_review.


---

Comment by jbandlow created at 2010-02-23 21:54:55

Thanks Anne! This looks good to me.  Positive review.

-Jason


---

Comment by nthiery created at 2010-02-25 08:43:09

Just two tiny remarks:

 - One can write `assert a==b` instead of `assert(a==b)`
 - One could be a bit more specific:  `assert a==b, "not a symmetric polynomial"
 - Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).
   So I am not sure it is the appropriate idiom here.

That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.

Thanks!


---

Attachment

Replying to [comment:11 nthiery]:
> Just two tiny remarks:
> 
>  - One can write `assert a==b` instead of `assert(a==b)`
>  - One could be a bit more specific:  `assert a==b, "not a symmetric polynomial"
>  - Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).
>    So I am not sure it is the appropriate idiom here.
> 
> That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.
> 
> Thanks!

Done! Please review the review of the review of the review ... oops! Infinite loop!


---

Comment by nthiery created at 2010-02-25 18:14:40

Replying to [comment:12 aschilling]:
> Replying to [comment:11 nthiery]:
> > Just two tiny remarks:
> > 
> >  - One can write `assert a==b` instead of `assert(a==b)`
> >  - One could be a bit more specific:  `assert a==b, "not a symmetric polynomial"
> >  - Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).
> >    So I am not sure it is the appropriate idiom here.
> > 
> > That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.
> > 
> > Thanks!
> 
> Done! Please review the review of the review of the review ... oops! Infinite loop!

Thanks! I haven't rerun the tests, but the review patch looks good to me.


---

Comment by mvngu created at 2010-03-02 21:27:28

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 21:27:28

Merged in this order:

 1. [trac_8259-from_poly_to_sym-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8259/trac_8259-from_poly_to_sym-as.patch)
 1. [trac_8259-from_poly_to_sym-review-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8259/trac_8259-from_poly_to_sym-review-as.patch)
