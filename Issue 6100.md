# Issue 6100: give a basis for homology and cohomology of chain complexes in terms of given generators

archive/issues_006100.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nCC:  jhpalmieri bantieau\n\nAdd functionality so that we can compute a basis for (co)homology in dimension n of a chain complex C_* in terms of a given basis for C_n.\n\nThis will use the patch #5882 of William Stein.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6100\n\n",
    "created_at": "2009-05-21T03:41:24Z",
    "labels": [
        "algebraic topology",
        "minor",
        "enhancement"
    ],
    "title": "give a basis for homology and cohomology of chain complexes in terms of given generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6100",
    "user": "bantieau"
}
```
Assignee: jhpalmieri

CC:  jhpalmieri bantieau

Add functionality so that we can compute a basis for (co)homology in dimension n of a chain complex C_* in terms of a given basis for C_n.

This will use the patch #5882 of William Stein.

Issue created by migration from https://trac.sagemath.org/ticket/6100





---

archive/issue_comments_048665.json:
```json
{
    "body": "Attachment [13222.patch](tarball://root/attachments/some-uuid/ticket6100/13222.patch) by sault created at 2010-01-11 15:31:47\n\nmain patch, implementing generators",
    "created_at": "2010-01-11T15:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48665",
    "user": "sault"
}
```

Attachment [13222.patch](tarball://root/attachments/some-uuid/ticket6100/13222.patch) by sault created at 2010-01-11 15:31:47

main patch, implementing generators



---

archive/issue_comments_048666.json:
```json
{
    "body": "Doctest added",
    "created_at": "2010-01-11T15:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48666",
    "user": "sault"
}
```

Doctest added



---

archive/issue_comments_048667.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-11T15:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48667",
    "user": "sault"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_048668.json:
```json
{
    "body": "Attachment [13223.patch](tarball://root/attachments/some-uuid/ticket6100/13223.patch) by sault created at 2010-01-11 15:35:42\n\nGenerators of homology now computable via generators=true option in the homology() method of chain_complex.\n\nKnown issues:  If S is a simplicial complex, S.homology(generators=true) has not been directly implemented.  Furthermore, S.chain_complex().homology(generators=true) computes the generators based on the order in which simplices are chosen for computing S.chain_complex() -- which is not guaranteed to be the same order in which simplices are listed in S.",
    "created_at": "2010-01-11T15:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48668",
    "user": "sault"
}
```

Attachment [13223.patch](tarball://root/attachments/some-uuid/ticket6100/13223.patch) by sault created at 2010-01-11 15:35:42

Generators of homology now computable via generators=true option in the homology() method of chain_complex.

Known issues:  If S is a simplicial complex, S.homology(generators=true) has not been directly implemented.  Furthermore, S.chain_complex().homology(generators=true) computes the generators based on the order in which simplices are chosen for computing S.chain_complex() -- which is not guaranteed to be the same order in which simplices are listed in S.



---

archive/issue_comments_048669.json:
```json
{
    "body": "Replying to [comment:2 sault]:\n\nThanks for working on this; I hope we can get it into shape soon, and then into Sage.\n\n> Known issues:  If S is a simplicial complex, S.homology(generators=true) has not been directly implemented.  \n\nI know a good way to deal with this, and I'll eventually submit a patch on another ticket that takes care of it (as part of an implementation of cubical complexes and Delta-complexes, among other things).\n\n> Furthermore, S.chain_complex().homology(generators=true) computes the generators based on the order in which simplices are chosen for computing S.chain_complex() -- which is not guaranteed to be the same order in which simplices are listed in S.\n\nI wonder what we can do to fix this.  It might be a lot of work; I'm not sure.  Maybe when we build the chain complex, modify the cached list of simplices of S?  This is something to think about for another ticket, not this one.\n\nThere are three problems with this patch: the main one is that it doesn't work with field coefficients:\n\n```\nsage: T = simplicial_complexes.Torus()\nsage: C = T.chain_complex()\nsage: C.homology(base_ring=QQ, generators=True)\n{0: Vector space of dimension 1 over Rational Field, 1: Vector space of dimension 2 over Rational Field, 2: (Vector space of dimension 1 over Rational Field, [ 1 -1 -1 -1  1 -1 -1  1  1  1  1  1 -1 -1])}\n```\n\nIt only returns generators in dimensions where there is no incoming differential. When you fix this, add a doctest like\n\n```\nsage: T = simplicial_complexes.Torus()\nsage: C = T.chain_complex()\nsage: C.homology(1, base_ring=QQ, generators=True)\n???\n```\n\n\nThe second problem is the documentation: you should explain (briefly) the format of the output when \"generators\" is True: it's giving a matrix, and you should say exactly what this matrix represents.\n\nThe third issue is minor: the indentation in the docstrings is important, but you changed it, so it gives errors when producing the reference manual.  The docstring itself also looks bad: from the notebook, define a chain complex C and evaluate \"C.homology?\" to see what the formatted docstring looks like.  Or do `browse_sage_doc(C.homology)` from the command line.",
    "created_at": "2010-02-03T18:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48669",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_048670.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-03T18:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48670",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_048671.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n\nThanks John, for reviewing this patch and for spotting the bugs/omissions.  I'll be working on this today and I hope to get it up to speed soon.  \n\n-S\n\n\n> Replying to [comment:2 sault]:\n> \n> Thanks for working on this; I hope we can get it into shape soon, and then into Sage.\n> \n> > Known issues:  If S is a simplicial complex, S.homology(generators=true) has not been directly implemented.  \n> \n> I know a good way to deal with this, and I'll eventually submit a patch on another ticket that takes care of it (as part of an implementation of cubical complexes and Delta-complexes, among other things).\n> \n> > Furthermore, S.chain_complex().homology(generators=true) computes the generators based on the order in which simplices are chosen for computing S.chain_complex() -- which is not guaranteed to be the same order in which simplices are listed in S.\n> \n> I wonder what we can do to fix this.  It might be a lot of work; I'm not sure.  Maybe when we build the chain complex, modify the cached list of simplices of S?  This is something to think about for another ticket, not this one.\n> \n> There are three problems with this patch: the main one is that it doesn't work with field coefficients:\n> {{{\n> sage: T = simplicial_complexes.Torus()\n> sage: C = T.chain_complex()\n> sage: C.homology(base_ring=QQ, generators=True)\n> {0: Vector space of dimension 1 over Rational Field, 1: Vector space of dimension 2 over Rational Field, 2: (Vector space of dimension 1 over Rational Field, [ 1 -1 -1 -1  1 -1 -1  1  1  1  1  1 -1 -1])}\n> }}}\n> It only returns generators in dimensions where there is no incoming differential. When you fix this, add a doctest like\n> {{{\n> sage: T = simplicial_complexes.Torus()\n> sage: C = T.chain_complex()\n> sage: C.homology(1, base_ring=QQ, generators=True)\n> ???\n> }}}\n> \n> The second problem is the documentation: you should explain (briefly) the format of the output when \"generators\" is True: it's giving a matrix, and you should say exactly what this matrix represents.\n> \n> The third issue is minor: the indentation in the docstrings is important, but you changed it, so it gives errors when producing the reference manual.  The docstring itself also looks bad: from the notebook, define a chain complex C and evaluate \"C.homology?\" to see what the formatted docstring looks like.  Or do `browse_sage_doc(C.homology)` from the command line.",
    "created_at": "2010-02-26T20:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48671",
    "user": "sault"
}
```

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

archive/issue_comments_048672.json:
```json
{
    "body": "Hi Shaun,\n\nYou should also look at ticket #8302, which now has a positive review and so should be merged some time soon.  You might want to base your patches on that.  In particular, you should look at how keywords are passed between the various homology and chain complex methods, and you should look at how the Sage interface to CHomP returns generators.  Your patch should be consistent with that (and you could add to the file homology/tests.py -- added in #8302 -- to test that your patch and CHomP produce compatible results).\n\nSince you're just dealing with generators for chain complexes, I don't know if it's worth putting a warning in the homology method for cell complexes, or at least in the docstring: if someone asks for generators and they don't have chomp installed, it will pass `generators=True` to the homology method for chain complexes, and therefore will produce something using your code, but it may not be what the user expects (since it will be in terms of the chain complex, not the simplicial complex).  Probably a warning in the docstring is appropriate now, and in another ticket, we can try to translate the chain complex information back to simplicial complex information somehow.",
    "created_at": "2010-02-26T20:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48672",
    "user": "jhpalmieri"
}
```

Hi Shaun,

You should also look at ticket #8302, which now has a positive review and so should be merged some time soon.  You might want to base your patches on that.  In particular, you should look at how keywords are passed between the various homology and chain complex methods, and you should look at how the Sage interface to CHomP returns generators.  Your patch should be consistent with that (and you could add to the file homology/tests.py -- added in #8302 -- to test that your patch and CHomP produce compatible results).

Since you're just dealing with generators for chain complexes, I don't know if it's worth putting a warning in the homology method for cell complexes, or at least in the docstring: if someone asks for generators and they don't have chomp installed, it will pass `generators=True` to the homology method for chain complexes, and therefore will produce something using your code, but it may not be what the user expects (since it will be in terms of the chain complex, not the simplicial complex).  Probably a warning in the docstring is appropriate now, and in another ticket, we can try to translate the chain complex information back to simplicial complex information somehow.



---

archive/issue_comments_048673.json:
```json
{
    "body": "Attachment [trac_6100-basis_homology-ts.patch](tarball://root/attachments/some-uuid/ticket6100/trac_6100-basis_homology-ts.patch) by tscrim created at 2013-04-03 21:04:06",
    "created_at": "2013-04-03T21:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48673",
    "user": "tscrim"
}
```

Attachment [trac_6100-basis_homology-ts.patch](tarball://root/attachments/some-uuid/ticket6100/trac_6100-basis_homology-ts.patch) by tscrim created at 2013-04-03 21:04:06



---

archive/issue_comments_048674.json:
```json
{
    "body": "I've uploaded a patch which combines the two previous patches and hopefully addresses the issues you've mentioned.\n\nFor patchbot:\n\nApply: trac_6100-basis_homology-ts.patch",
    "created_at": "2013-04-03T21:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48674",
    "user": "tscrim"
}
```

I've uploaded a patch which combines the two previous patches and hopefully addresses the issues you've mentioned.

For patchbot:

Apply: trac_6100-basis_homology-ts.patch



---

archive/issue_comments_048675.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-04-03T21:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48675",
    "user": "tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_048676.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-29T09:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48676",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048677.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2013-05-29T09:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48677",
    "user": "vbraun"
}
```

Looks good to me.



---

archive/issue_comments_048678.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-06T12:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48678",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_048679.json:
```json
{
    "body": "Follow-up question:\n\n- [Ask Sage question 53129: Cohomology ring of a Lie algebra](https://ask.sagemath.org/question/53129)",
    "created_at": "2020-10-26T15:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48679",
    "user": "slelievre"
}
```

Follow-up question:

- [Ask Sage question 53129: Cohomology ring of a Lie algebra](https://ask.sagemath.org/question/53129)



---

archive/issue_comments_048680.json:
```json
{
    "body": "See #30838 for a followup (not related to the Lie algebra question).",
    "created_at": "2020-10-29T17:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6100#issuecomment-48680",
    "user": "jhpalmieri"
}
```

See #30838 for a followup (not related to the Lie algebra question).
