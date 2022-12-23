# Issue 6100: give a basis for homology and cohomology of chain complexes in terms of given generators

Issue created by migration from https://trac.sagemath.org/ticket/6100

Original creator: bantieau

Original creation time: 2009-05-21 03:41:24

Assignee: jhpalmieri

CC:  jhpalmieri bantieau

Add functionality so that we can compute a basis for (co)homology in dimension n of a chain complex C_* in terms of a given basis for C_n.

This will use the patch #5882 of William Stein.


---

Attachment

main patch, implementing generators


---

Comment by sault created at 2010-01-11 15:31:59

Doctest added


---

Comment by sault created at 2010-01-11 15:35:42

Changing status from new to needs_review.


---

Attachment

Generators of homology now computable via generators=true option in the homology() method of chain_complex.

Known issues:  If S is a simplicial complex, S.homology(generators=true) has not been directly implemented.  Furthermore, S.chain_complex().homology(generators=true) computes the generators based on the order in which simplices are chosen for computing S.chain_complex() -- which is not guaranteed to be the same order in which simplices are listed in S.


---

Comment by jhpalmieri created at 2010-02-03 18:23:47

Replying to [comment:2 sault]:

Thanks for working on this; I hope we can get it into shape soon, and then into Sage.

> Known issues:  If S is a simplicial complex, S.homology(generators=true) has not been directly implemented.  

I know a good way to deal with this, and I'll eventually submit a patch on another ticket that takes care of it (as part of an implementation of cubical complexes and Delta-complexes, among other things).

> Furthermore, S.chain_complex().homology(generators=true) computes the generators based on the order in which simplices are chosen for computing S.chain_complex() -- which is not guaranteed to be the same order in which simplices are listed in S.

I wonder what we can do to fix this.  It might be a lot of work; I'm not sure.  Maybe when we build the chain complex, modify the cached list of simplices of S?  This is something to think about for another ticket, not this one.

There are three problems with this patch: the main one is that it doesn't work with field coefficients:

```
sage: T = simplicial_complexes.Torus()
sage: C = T.chain_complex()
sage: C.homology(base_ring=QQ, generators=True)
{0: Vector space of dimension 1 over Rational Field, 1: Vector space of dimension 2 over Rational Field, 2: (Vector space of dimension 1 over Rational Field, [ 1 -1 -1 -1  1 -1 -1  1  1  1  1  1 -1 -1])}
```

It only returns generators in dimensions where there is no incoming differential. When you fix this, add a doctest like

```
sage: T = simplicial_complexes.Torus()
sage: C = T.chain_complex()
sage: C.homology(1, base_ring=QQ, generators=True)
???
```


The second problem is the documentation: you should explain (briefly) the format of the output when "generators" is True: it's giving a matrix, and you should say exactly what this matrix represents.

The third issue is minor: the indentation in the docstrings is important, but you changed it, so it gives errors when producing the reference manual.  The docstring itself also looks bad: from the notebook, define a chain complex C and evaluate "C.homology?" to see what the formatted docstring looks like.  Or do `browse_sage_doc(C.homology)` from the command line.


---

Comment by jhpalmieri created at 2010-02-03 18:23:47

Changing status from needs_review to needs_work.


---

Comment by sault created at 2010-02-26 20:35:14

Replying to [comment:3 jhpalmieri]:

Thanks John, for reviewing this patch and for spotting the bugs/omissions.  I'll be working on this today and I hope to get it up to speed soon.  

-S


> Replying to [comment:2 sault]:
> 
> Thanks for working on this; I hope we can get it into shape soon, and then into Sage.
> 
> > Known issues:  If S is a simplicial complex, S.homology(generators=true) has not been directly implemented.  
> 
> I know a good way to deal with this, and I'll eventually submit a patch on another ticket that takes care of it (as part of an implementation of cubical complexes and Delta-complexes, among other things).
> 
> > Furthermore, S.chain_complex().homology(generators=true) computes the generators based on the order in which simplices are chosen for computing S.chain_complex() -- which is not guaranteed to be the same order in which simplices are listed in S.
> 
> I wonder what we can do to fix this.  It might be a lot of work; I'm not sure.  Maybe when we build the chain complex, modify the cached list of simplices of S?  This is something to think about for another ticket, not this one.
> 
> There are three problems with this patch: the main one is that it doesn't work with field coefficients:
> {{{
> sage: T = simplicial_complexes.Torus()
> sage: C = T.chain_complex()
> sage: C.homology(base_ring=QQ, generators=True)
> {0: Vector space of dimension 1 over Rational Field, 1: Vector space of dimension 2 over Rational Field, 2: (Vector space of dimension 1 over Rational Field, [ 1 -1 -1 -1  1 -1 -1  1  1  1  1  1 -1 -1])}
> }}}
> It only returns generators in dimensions where there is no incoming differential. When you fix this, add a doctest like
> {{{
> sage: T = simplicial_complexes.Torus()
> sage: C = T.chain_complex()
> sage: C.homology(1, base_ring=QQ, generators=True)
> ???
> }}}
> 
> The second problem is the documentation: you should explain (briefly) the format of the output when "generators" is True: it's giving a matrix, and you should say exactly what this matrix represents.
> 
> The third issue is minor: the indentation in the docstrings is important, but you changed it, so it gives errors when producing the reference manual.  The docstring itself also looks bad: from the notebook, define a chain complex C and evaluate "C.homology?" to see what the formatted docstring looks like.  Or do `browse_sage_doc(C.homology)` from the command line.


---

Comment by jhpalmieri created at 2010-02-26 20:46:58

Hi Shaun,

You should also look at ticket #8302, which now has a positive review and so should be merged some time soon.  You might want to base your patches on that.  In particular, you should look at how keywords are passed between the various homology and chain complex methods, and you should look at how the Sage interface to CHomP returns generators.  Your patch should be consistent with that (and you could add to the file homology/tests.py -- added in #8302 -- to test that your patch and CHomP produce compatible results).

Since you're just dealing with generators for chain complexes, I don't know if it's worth putting a warning in the homology method for cell complexes, or at least in the docstring: if someone asks for generators and they don't have chomp installed, it will pass `generators=True` to the homology method for chain complexes, and therefore will produce something using your code, but it may not be what the user expects (since it will be in terms of the chain complex, not the simplicial complex).  Probably a warning in the docstring is appropriate now, and in another ticket, we can try to translate the chain complex information back to simplicial complex information somehow.


---

Attachment


---

Comment by tscrim created at 2013-04-03 21:07:45

I've uploaded a patch which combines the two previous patches and hopefully addresses the issues you've mentioned.

For patchbot:

Apply: trac_6100-basis_homology-ts.patch


---

Comment by tscrim created at 2013-04-03 21:07:45

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2013-05-29 09:28:06

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-05-29 09:28:06

Looks good to me.


---

Comment by jdemeyer created at 2013-06-06 12:30:21

Resolution: fixed


---

Comment by slelievre created at 2020-10-26 15:18:20

Follow-up question:

- [Ask Sage question 53129: Cohomology ring of a Lie algebra](https://ask.sagemath.org/question/53129)


---

Comment by jhpalmieri created at 2020-10-29 17:44:16

See #30838 for a followup (not related to the Lie algebra question).
