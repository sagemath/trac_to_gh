# Issue 9650: Adding support for differential forms

archive/issues_009650.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  mhampton @jasongrout @jdemeyer @qed777 @novoselt @nilesjohnson\n\nKeywords: forms, functions, symbolics\n\nImplements support for differential forms to Sage.  After applying the patch, three new classes are added to sage:\n\n1. `CoordinatePatch` -- an open subset of Rn on which differential forms can be defined\n2. `DifferentialForms` -- a differential forms parent\n3. `DifferentialForm` -- a differential forms class.\n\nPlease see the documentation in the `DifferentialForm` class for more information about syntax, available methods, etc.\n\nThis is a very basic implementation, providing support for exterior differentiation and wedge products of forms, but not much more.  The emphasis is on making sure that the framework is implemented correctly.\n\nSee discussion at\n\n1. http://wiki.sagemath.org/tensorcalc\n2. http://groups.google.be/group/sage-devel/browse_thread/thread/2feef1f0be557585/c2b7095747ebe34d\n\nIssue created by migration from https://trac.sagemath.org/ticket/9650\n\n",
    "created_at": "2010-07-31T11:48:00Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Adding support for differential forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9650",
    "user": "https://github.com/jvkersch"
}
```
Assignee: @burcin

CC:  mhampton @jasongrout @jdemeyer @qed777 @novoselt @nilesjohnson

Keywords: forms, functions, symbolics

Implements support for differential forms to Sage.  After applying the patch, three new classes are added to sage:

1. `CoordinatePatch` -- an open subset of Rn on which differential forms can be defined
2. `DifferentialForms` -- a differential forms parent
3. `DifferentialForm` -- a differential forms class.

Please see the documentation in the `DifferentialForm` class for more information about syntax, available methods, etc.

This is a very basic implementation, providing support for exterior differentiation and wedge products of forms, but not much more.  The emphasis is on making sure that the framework is implemented correctly.

See discussion at

1. http://wiki.sagemath.org/tensorcalc
2. http://groups.google.be/group/sage-devel/browse_thread/thread/2feef1f0be557585/c2b7095747ebe34d

Issue created by migration from https://trac.sagemath.org/ticket/9650





---

archive/issue_comments_093419.json:
```json
{
    "body": "Wow, thanks!  I'm not an expert in differential geometry, so I'm going to have to rely on someone else to vet the theoretical design at this level.  Here are a few python comments, though:\n\n* `all([is_SymbolicVariable(c) for c in coordinates])` should not construct a list, so that short-circuiting can occur: `all(is_SymbolicVariable(c) for c in coordinates)`\n\n* Checking for `None` should be done with is (it's a lot faster that way): `metric is not None`\n\nI also added mention of two other mma packages to the wiki page, one of which has a nice Integral command.  Do you see us getting a command that can integrate like the following commands indicate?\n\n\n```\nThe area of the unit square is calculated by:\t\nIntegral[ d[x,y] , Chain[ {x -> s, y -> t}, {s, 0, 1}, {t, 0, 1}]].\t\n\nThe area of the circle of radius R is calculated by:\nSetAttributes[R, Constant];\nIntegral[ d[x,y] , \tChain[ {x -> r Cos[theta], y -> r Sin[theta]}, \\\n{r, 0, R}, {theta, 0, 2Pi}]].\n\n\nStokes Theorem:\n\nIntegral[ d @ ((x/2) d[y] - (y/2) d[y]) , \tChain[ {x -> s, y -> t}, \\\n{s, 0, 1}, {t, 0, 1}]] ==\t\nIntegral[ ((x/2) d[y] - (y/2) d[y]) , \tBoundary @ Chain[ {x -> s, y -> \\\nt}, {s, 0, 1}, {t, 0, 1}]]\n```\n",
    "created_at": "2010-07-31T18:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93419",
    "user": "https://github.com/jasongrout"
}
```

Wow, thanks!  I'm not an expert in differential geometry, so I'm going to have to rely on someone else to vet the theoretical design at this level.  Here are a few python comments, though:

* `all([is_SymbolicVariable(c) for c in coordinates])` should not construct a list, so that short-circuiting can occur: `all(is_SymbolicVariable(c) for c in coordinates)`

* Checking for `None` should be done with is (it's a lot faster that way): `metric is not None`

I also added mention of two other mma packages to the wiki page, one of which has a nice Integral command.  Do you see us getting a command that can integrate like the following commands indicate?


```
The area of the unit square is calculated by:	
Integral[ d[x,y] , Chain[ {x -> s, y -> t}, {s, 0, 1}, {t, 0, 1}]].	

The area of the circle of radius R is calculated by:
SetAttributes[R, Constant];
Integral[ d[x,y] , 	Chain[ {x -> r Cos[theta], y -> r Sin[theta]}, \
{r, 0, R}, {theta, 0, 2Pi}]].


Stokes Theorem:

Integral[ d @ ((x/2) d[y] - (y/2) d[y]) , 	Chain[ {x -> s, y -> t}, \
{s, 0, 1}, {t, 0, 1}]] ==	
Integral[ ((x/2) d[y] - (y/2) d[y]) , 	Boundary @ Chain[ {x -> s, y -> \
t}, {s, 0, 1}, {t, 0, 1}]]
```




---

archive/issue_comments_093420.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-31T18:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93420",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_093421.json:
```json
{
    "body": "Also, if you feel like the patch is to the point that it needs review, please change the status below to \"needs review\".",
    "created_at": "2010-07-31T18:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93421",
    "user": "https://github.com/jasongrout"
}
```

Also, if you feel like the patch is to the point that it needs review, please change the status below to "needs review".



---

archive/issue_comments_093422.json:
```json
{
    "body": "Thanks for the comments, which not only improved the patch but my Python knowledge as well!  I've updated the patch in the meantime.  Thanks also for guiding me through the sage patch process!\n\nSome quick comments and questions:\n\n1.  As for integration of forms, I think this is definitely doable and in fact should be dealt with before the other stuff (metric geometry, etc).\n\n2.  I'm very interesting in seeing how the authors of that mathematica package represented differential forms -- thanks for the link!\n\n3. Once I've taken a good look at the mathematica package, I'll set the patch to \"needs review\".",
    "created_at": "2010-08-01T16:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93422",
    "user": "https://github.com/jvkersch"
}
```

Thanks for the comments, which not only improved the patch but my Python knowledge as well!  I've updated the patch in the meantime.  Thanks also for guiding me through the sage patch process!

Some quick comments and questions:

1.  As for integration of forms, I think this is definitely doable and in fact should be dealt with before the other stuff (metric geometry, etc).

2.  I'm very interesting in seeing how the authors of that mathematica package represented differential forms -- thanks for the link!

3. Once I've taken a good look at the mathematica package, I'll set the patch to "needs review".



---

archive/issue_comments_093423.json:
```json
{
    "body": "I'm going to set the patch to \"needs review\", firstly since as burcin pointed out in a private email, the licensing situation of the mathematica package is somewhat unclear, and secondly the implementation of the differential forms class is sufficiently simple so that the issue won't be with the algorithms that I used but rather whether this is good sage programming.\n\nSome things to keep in mind: right now, the way to create a differential form is as follows: first you create a !``CoordinatePatch!`` on which forms can be defined, then you create a !``DifferentialForms!`` parent and then you can create forms.\u00a0 Explicitly, this looks like\n\n\n```\n\n\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 sage: x, y, z = var('x, y, z')\n\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 sage: U = !CoordinatePatch((x, y, z))\n\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 sage: F = !DifferentialForms(U)\n\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 sage: form = !DifferentialForm(F, 0, sin(x*y)); form\n\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 sin(x*y)\n\n```\n\n\nLet me know if this construction is confusing or can be simplified in any way.",
    "created_at": "2010-08-04T08:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93423",
    "user": "https://github.com/jvkersch"
}
```

I'm going to set the patch to "needs review", firstly since as burcin pointed out in a private email, the licensing situation of the mathematica package is somewhat unclear, and secondly the implementation of the differential forms class is sufficiently simple so that the issue won't be with the algorithms that I used but rather whether this is good sage programming.

Some things to keep in mind: right now, the way to create a differential form is as follows: first you create a !``CoordinatePatch!`` on which forms can be defined, then you create a !``DifferentialForms!`` parent and then you can create forms.  Explicitly, this looks like


```

        sage: x, y, z = var('x, y, z')
        sage: U = !CoordinatePatch((x, y, z))
        sage: F = !DifferentialForms(U)
        sage: form = !DifferentialForm(F, 0, sin(x*y)); form
        sin(x*y)

```


Let me know if this construction is confusing or can be simplified in any way.



---

archive/issue_comments_093424.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-04T08:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93424",
    "user": "https://github.com/jvkersch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093425.json:
```json
{
    "body": "Oops: inside of triple-braces, things are quoted literally:\n\n\n```\nsage: x, y, z = var('x, y, z')\nsage: U = CoordinatePatch((x, y, z))\nsage: F = DifferentialForms(U)\nsage: form = DifferentialForm(F, 0, sin(x*y)); form\nsin(x*y)\n```\n",
    "created_at": "2010-08-04T14:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93425",
    "user": "https://github.com/jasongrout"
}
```

Oops: inside of triple-braces, things are quoted literally:


```
sage: x, y, z = var('x, y, z')
sage: U = CoordinatePatch((x, y, z))
sage: F = DifferentialForms(U)
sage: form = DifferentialForm(F, 0, sin(x*y)); form
sin(x*y)
```




---

archive/issue_comments_093426.json:
```json
{
    "body": "To placate `./sage -b`, which now gives\n\n```\npackage init file 'sage/tensor/__init__.py' not found (or not a regular file)\n```\n\nmessages, could you add an empty `sage/tensor/__init__.py`.\n\nAlso, if you'd like to document your new modules in the reference manual, you can add `tensor` to\n\n```\nSAGE_ROOT/devel/sage/doc/en/reference/index.rst\n```\n\nand create `tensor.rst`, patterned after `graphs.rst` (say), in the same directory.  To rebuild the manual, run\n\n```sh\n$ cd SAGE_ROOT\n$ ./sage -b\n$ ./sage -docbuild reference html -j\n```\n\nSphinx should print warnings about any docstring formatting problems.  The results will be in\n\n```\nSAGE_ROOT/devel/sage/doc/output/html/en/reference/\n```\n",
    "created_at": "2010-08-23T01:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93426",
    "user": "https://github.com/qed777"
}
```

To placate `./sage -b`, which now gives

```
package init file 'sage/tensor/__init__.py' not found (or not a regular file)
```

messages, could you add an empty `sage/tensor/__init__.py`.

Also, if you'd like to document your new modules in the reference manual, you can add `tensor` to

```
SAGE_ROOT/devel/sage/doc/en/reference/index.rst
```

and create `tensor.rst`, patterned after `graphs.rst` (say), in the same directory.  To rebuild the manual, run

```sh
$ cd SAGE_ROOT
$ ./sage -b
$ ./sage -docbuild reference html -j
```

Sphinx should print warnings about any docstring formatting problems.  The results will be in

```
SAGE_ROOT/devel/sage/doc/output/html/en/reference/
```




---

archive/issue_comments_093427.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-23T16:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93427",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093428.json:
```json
{
    "body": "Hi Joris,\n\nI saw your e-mail to `sage-devel`, so here's my review :)  This looks like a nice patch, and it works nicely enough that I had to resist the temptation to ask for more functionality (which you are right to postpone, I think).\n\nI ran a complete doctest of the sage library, and tested building the documentation, as well as playing with a few examples.  Here are some notes\n\n* add empty file __init__.py (as mentioned above; this is required for doctesting and to build documentation)\n* add author to coordinate_patch.py\n* I believe it is usual for gens() to return a tuple (rather than a list); e.g.\n\n```\nsage: PolynomialRing(RR,3,'x,y,z').gens()\n(x, y, z)\n```\n\n\n* `make ptestlong` passes all tests!\n\n* Following the above suggestion, I added 'tensor' to `index.rst` and the following to a new file `tensor.rst`.  There are a few warnings when building the documentation that need to be fixed, but mostly it looks good.\n\n```\nDifferential Forms\n============\n\n.. toctree::\n   :maxdepth: 2\n\n   sage/tensor/coordinate_patch\n   sage/tensor/differential_forms\n   sage/tensor/differential_form_element\n```\n\n\n* Is there a reason you call the directory `tensor` instead of e.g. `diff_forms` or even `differential_forms`?  I'm not an expert on differential forms, so I defer to your judgment, but the latter seems more intuitive to me.",
    "created_at": "2010-08-23T16:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93428",
    "user": "https://github.com/nilesjohnson"
}
```

Hi Joris,

I saw your e-mail to `sage-devel`, so here's my review :)  This looks like a nice patch, and it works nicely enough that I had to resist the temptation to ask for more functionality (which you are right to postpone, I think).

I ran a complete doctest of the sage library, and tested building the documentation, as well as playing with a few examples.  Here are some notes

* add empty file __init__.py (as mentioned above; this is required for doctesting and to build documentation)
* add author to coordinate_patch.py
* I believe it is usual for gens() to return a tuple (rather than a list); e.g.

```
sage: PolynomialRing(RR,3,'x,y,z').gens()
(x, y, z)
```


* `make ptestlong` passes all tests!

* Following the above suggestion, I added 'tensor' to `index.rst` and the following to a new file `tensor.rst`.  There are a few warnings when building the documentation that need to be fixed, but mostly it looks good.

```
Differential Forms
============

.. toctree::
   :maxdepth: 2

   sage/tensor/coordinate_patch
   sage/tensor/differential_forms
   sage/tensor/differential_form_element
```


* Is there a reason you call the directory `tensor` instead of e.g. `diff_forms` or even `differential_forms`?  I'm not an expert on differential forms, so I defer to your judgment, but the latter seems more intuitive to me.



---

archive/issue_comments_093429.json:
```json
{
    "body": "the first point is about `__init__.py`; sorry for the misformatting!",
    "created_at": "2010-08-23T16:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93429",
    "user": "https://github.com/nilesjohnson"
}
```

the first point is about `__init__.py`; sorry for the misformatting!



---

archive/issue_comments_093430.json:
```json
{
    "body": "oh, and doctest coverage is at 100% for each of the 3 files!",
    "created_at": "2010-08-23T17:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93430",
    "user": "https://github.com/nilesjohnson"
}
```

oh, and doctest coverage is at 100% for each of the 3 files!



---

archive/issue_comments_093431.json:
```json
{
    "body": "Hi Niles and Mitesh,\n\nThank you for your instructive comments.  Niles, thanks also for agreeing to review my patch!  The suggestion to include this functionality to the reference manual was especially helpful -- it makes everything so much clearer to see the documentation in nice, crisp HTML form.\n\nI implemented the changes you suggested (adding to the reference manual, adding authors, making `gens()` return a tuple), but I have a few questions/comments that are more of a technical nature, revealing simultaneously my mercurial ineptitude:\n\n1.  I made a mess of the upload section -- could someone with admin privileges delete all but the most recent attachment?\n\n2.  Try as I might, I could not produce a patch which creates the file `__init__.py`.  I added that file to my sage tree as per the documentation, instructed hg to add it, confirmed with `hg status` that it was listed as added, but when I look at `hg diff` that file is nowhere to be found.  The other files are created/modified as expected.  The patch also does not create `__init__.py`, as you experienced.  Are these init files somehow special as far as hg is concerned?\n\n3.  I called the package `tensor` rather than anything more specific in order to accommodate future additions: it would be good to have support for generic tensors (not just differential forms) and common operations on them (e.g. covariant derivations), so that we could for instance do symbolic Riemannian geometry.  However, if you think we should stick to a more specific name for now, then that's fine with me too.",
    "created_at": "2010-08-24T12:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93431",
    "user": "https://github.com/jvkersch"
}
```

Hi Niles and Mitesh,

Thank you for your instructive comments.  Niles, thanks also for agreeing to review my patch!  The suggestion to include this functionality to the reference manual was especially helpful -- it makes everything so much clearer to see the documentation in nice, crisp HTML form.

I implemented the changes you suggested (adding to the reference manual, adding authors, making `gens()` return a tuple), but I have a few questions/comments that are more of a technical nature, revealing simultaneously my mercurial ineptitude:

1.  I made a mess of the upload section -- could someone with admin privileges delete all but the most recent attachment?

2.  Try as I might, I could not produce a patch which creates the file `__init__.py`.  I added that file to my sage tree as per the documentation, instructed hg to add it, confirmed with `hg status` that it was listed as added, but when I look at `hg diff` that file is nowhere to be found.  The other files are created/modified as expected.  The patch also does not create `__init__.py`, as you experienced.  Are these init files somehow special as far as hg is concerned?

3.  I called the package `tensor` rather than anything more specific in order to accommodate future additions: it would be good to have support for generic tensors (not just differential forms) and common operations on them (e.g. covariant derivations), so that we could for instance do symbolic Riemannian geometry.  However, if you think we should stick to a more specific name for now, then that's fine with me too.



---

archive/issue_comments_093432.json:
```json
{
    "body": "Replying to [comment:17 jvkersch]:\n> Hi Niles and Mitesh,\n> \n> Thank you for your instructive comments.  Niles, thanks also for agreeing to review my patch!  The suggestion to include this functionality to the reference manual was especially helpful -- it makes everything so much clearer to see the documentation in nice, crisp HTML form.\n> \n> I implemented the changes you suggested (adding to the reference manual, adding authors, making `gens()` return a tuple), but I have a few questions/comments that are more of a technical nature, revealing simultaneously my mercurial ineptitude:\n> \n> 1.  I made a mess of the upload section -- could someone with admin privileges delete all but the most recent attachment?\n\n\nDone.\n\n> \n> 2.  Try as I might, I could not produce a patch which creates the file `__init__.py`.  I added that file to my sage tree as per the documentation, instructed hg to add it, confirmed with `hg status` that it was listed as added, but when I look at `hg diff` that file is nowhere to be found.  The other files are created/modified as expected.  The patch also does not create `__init__.py`, as you experienced.  Are these init files somehow special as far as hg is concerned?\n> \n\n\nA peculiarity of Mercurial is that it can't check in empty files.  So usually we'll add either a space, or a comment like:\n\n\n```\n# This comment is here so the file is non-empty (so Mercurial will check it in).\n```\n\n\nor something like that.\n\n\n> 3.  I called the package `tensor` rather than anything more specific in order to accommodate future additions: it would be good to have support for generic tensors (not just differential forms) and common operations on them (e.g. covariant derivations), so that we could for instance do symbolic Riemannian geometry.  However, if you think we should stick to a more specific name for now, then that's fine with me too.\n\nPersonally, I'm okay with \"tensor\", since \"differential_forms\" would be equally confusing to my calc 3 students, so (a) there will be a learning curve anyway, and (b) most functions students would use are probably going to be imported into the top-level namespace anyway.",
    "created_at": "2010-08-24T14:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93432",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:17 jvkersch]:
> Hi Niles and Mitesh,
> 
> Thank you for your instructive comments.  Niles, thanks also for agreeing to review my patch!  The suggestion to include this functionality to the reference manual was especially helpful -- it makes everything so much clearer to see the documentation in nice, crisp HTML form.
> 
> I implemented the changes you suggested (adding to the reference manual, adding authors, making `gens()` return a tuple), but I have a few questions/comments that are more of a technical nature, revealing simultaneously my mercurial ineptitude:
> 
> 1.  I made a mess of the upload section -- could someone with admin privileges delete all but the most recent attachment?


Done.

> 
> 2.  Try as I might, I could not produce a patch which creates the file `__init__.py`.  I added that file to my sage tree as per the documentation, instructed hg to add it, confirmed with `hg status` that it was listed as added, but when I look at `hg diff` that file is nowhere to be found.  The other files are created/modified as expected.  The patch also does not create `__init__.py`, as you experienced.  Are these init files somehow special as far as hg is concerned?
> 


A peculiarity of Mercurial is that it can't check in empty files.  So usually we'll add either a space, or a comment like:


```
# This comment is here so the file is non-empty (so Mercurial will check it in).
```


or something like that.


> 3.  I called the package `tensor` rather than anything more specific in order to accommodate future additions: it would be good to have support for generic tensors (not just differential forms) and common operations on them (e.g. covariant derivations), so that we could for instance do symbolic Riemannian geometry.  However, if you think we should stick to a more specific name for now, then that's fine with me too.

Personally, I'm okay with "tensor", since "differential_forms" would be equally confusing to my calc 3 students, so (a) there will be a learning curve anyway, and (b) most functions students would use are probably going to be imported into the top-level namespace anyway.



---

archive/issue_comments_093433.json:
```json
{
    "body": "Replying to [comment:18 jason]:\n\n> A peculiarity of Mercurial is that it can't check in empty files.  So usually we'll add either a space, or a comment like:\n> (...)\n\n\nThanks a lot for pointing that out -- this is really helpful!\n\nI've updated the patch with the `__init__.py`, verified that it passes all doctests, and added those files to the reference manual section.  So I'm changing the status back to `needs_review`.",
    "created_at": "2010-08-24T19:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93433",
    "user": "https://github.com/jvkersch"
}
```

Replying to [comment:18 jason]:

> A peculiarity of Mercurial is that it can't check in empty files.  So usually we'll add either a space, or a comment like:
> (...)


Thanks a lot for pointing that out -- this is really helpful!

I've updated the patch with the `__init__.py`, verified that it passes all doctests, and added those files to the reference manual section.  So I'm changing the status back to `needs_review`.



---

archive/issue_comments_093434.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-24T19:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93434",
    "user": "https://github.com/jvkersch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093435.json:
```json
{
    "body": "It looks like the top of coordinate_patch.py is repeated around line 232.  Was that intentional?",
    "created_at": "2010-08-24T21:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93435",
    "user": "https://github.com/jasongrout"
}
```

It looks like the top of coordinate_patch.py is repeated around line 232.  Was that intentional?



---

archive/issue_comments_093436.json:
```json
{
    "body": "In fact, it looks like the entire content of coordinate_patch.py is duplicated, starting around line 232 of that file.",
    "created_at": "2010-08-24T21:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93436",
    "user": "https://github.com/jasongrout"
}
```

In fact, it looks like the entire content of coordinate_patch.py is duplicated, starting around line 232 of that file.



---

archive/issue_comments_093437.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-25T15:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93437",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093438.json:
```json
{
    "body": "Hi Joris,\n\nThings are looking good, but the documentation produces some warnings related to formatting errors--please fix this in addition to deleting the duplicates from `coordinate_patch.py`.  There are also some formatting problems in the documentation which do not produce warnings, so please check the html documentation carefully.\n\nAlso, do you think the documentation files could have better names?  I find it funny that the documentation for \"`DifferentialForm`\" is titled \"Differential forms class\" and the documentation for \"`DifferentialForms`\" is titled something else. (But again I'll defer to you on this :)",
    "created_at": "2010-08-25T15:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93438",
    "user": "https://github.com/nilesjohnson"
}
```

Hi Joris,

Things are looking good, but the documentation produces some warnings related to formatting errors--please fix this in addition to deleting the duplicates from `coordinate_patch.py`.  There are also some formatting problems in the documentation which do not produce warnings, so please check the html documentation carefully.

Also, do you think the documentation files could have better names?  I find it funny that the documentation for "`DifferentialForm`" is titled "Differential forms class" and the documentation for "`DifferentialForms`" is titled something else. (But again I'll defer to you on this :)



---

archive/issue_comments_093439.json:
```json
{
    "body": "Hi Jason and Niles,\n\nThanks for your comments, in particular for catching that code duplication.  I've tried to address your suggestions as well as I could, and here are the changes in the most recent version of the patch:\n\n1.  I've fixed the documentation so that it generates the output without any warnings, and I've also addressed the formatting issues.  This proved to be really tricky...\n\n2.  I agree on the names of the documentation files.  In the current patch, the documentation now reads: \"Algebra of differential forms\" for `differential_forms.py` and \"Elements of the algebra of differential forms\" for `differential_form_element.py`.  I believe that this is both clearer and more in line with the rest of the Sage docs, but please feel free to correct me on this!\n\nThanks for all your time on the review!",
    "created_at": "2010-08-30T21:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93439",
    "user": "https://github.com/jvkersch"
}
```

Hi Jason and Niles,

Thanks for your comments, in particular for catching that code duplication.  I've tried to address your suggestions as well as I could, and here are the changes in the most recent version of the patch:

1.  I've fixed the documentation so that it generates the output without any warnings, and I've also addressed the formatting issues.  This proved to be really tricky...

2.  I agree on the names of the documentation files.  In the current patch, the documentation now reads: "Algebra of differential forms" for `differential_forms.py` and "Elements of the algebra of differential forms" for `differential_form_element.py`.  I believe that this is both clearer and more in line with the rest of the Sage docs, but please feel free to correct me on this!

Thanks for all your time on the review!



---

archive/issue_comments_093440.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-30T21:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93440",
    "user": "https://github.com/jvkersch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093441.json:
```json
{
    "body": "Joris, could you add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames), when it's convenient?",
    "created_at": "2010-08-30T21:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93441",
    "user": "https://github.com/qed777"
}
```

Joris, could you add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames), when it's convenient?



---

archive/issue_comments_093442.json:
```json
{
    "body": "The most recent patch looks good to me.  Doctests pass, playing around with some examples seems fine, and docs build.  However, as this is not my area, at least one other person should pass off on this (niles?).",
    "created_at": "2010-08-31T03:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93442",
    "user": "https://github.com/jasongrout"
}
```

The most recent patch looks good to me.  Doctests pass, playing around with some examples seems fine, and docs build.  However, as this is not my area, at least one other person should pass off on this (niles?).



---

archive/issue_comments_093443.json:
```json
{
    "body": "This looks good to me too, although I'm not sure if this is desired behavior:\n\n\n```\nU = CoordinatePatch((x,y))\nF2 = DifferentialForms(U)\nq = DifferentialForm(F2,1)\nq[0] = -y\nq[1] = x\ndiff(q,y)\n```\n\ngives\n\n```\n0\n```\n\nbut it seems like diff(q,y) should give dx/\\dy.  I'm pretty rusty with my differntial forms though, I'll try to brush up.",
    "created_at": "2010-08-31T15:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This looks good to me too, although I'm not sure if this is desired behavior:


```
U = CoordinatePatch((x,y))
F2 = DifferentialForms(U)
q = DifferentialForm(F2,1)
q[0] = -y
q[1] = x
diff(q,y)
```

gives

```
0
```

but it seems like diff(q,y) should give dx/\dy.  I'm pretty rusty with my differntial forms though, I'll try to brush up.



---

archive/issue_comments_093444.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-31T17:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93444",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093445.json:
```json
{
    "body": "I agree; documentation builds cleanly, looks good, and the code works nicely.  As Joris has said, this is intentionally a very basic implementation; I think later patches should add functionality and flexibility (e.g. differential forms over other rings, and coercion between forms over different sets of variables, as is done for multivariate polynomial rings)\n\n\nReplying to [comment:27 mhampton]:\n> This looks good to me too, although I'm not sure if this is desired behavior:\n> \n\n```\nU = CoordinatePatch((x,y))\nF2 = DifferentialForms(U)\nq = DifferentialForm(F2,1)\nq[0] = -y\nq[1] = x\ndiff(q,y)\n```\n\n> gives\n> \n\n```\n 0\n```\n\n> but it seems like diff(q,y) should give dx/\\dy.  I'm pretty rusty with my differntial forms though, I'll try to brush up.\n> \n\nThis problem is caused because `diff()` first tries to call `q.differentiate()` and, failing that, coerces `q` to the symbolic ring and differentiates it there.  Adding a `differentiate()` method which simply calls `q.diff()` would solve this problem.  Depending on what you think is best, you could silently ignore additional arguments to `diff`, or you could throw an error if additional arguments are present.",
    "created_at": "2010-08-31T17:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93445",
    "user": "https://github.com/nilesjohnson"
}
```

I agree; documentation builds cleanly, looks good, and the code works nicely.  As Joris has said, this is intentionally a very basic implementation; I think later patches should add functionality and flexibility (e.g. differential forms over other rings, and coercion between forms over different sets of variables, as is done for multivariate polynomial rings)


Replying to [comment:27 mhampton]:
> This looks good to me too, although I'm not sure if this is desired behavior:
> 

```
U = CoordinatePatch((x,y))
F2 = DifferentialForms(U)
q = DifferentialForm(F2,1)
q[0] = -y
q[1] = x
diff(q,y)
```

> gives
> 

```
 0
```

> but it seems like diff(q,y) should give dx/\dy.  I'm pretty rusty with my differntial forms though, I'll try to brush up.
> 

This problem is caused because `diff()` first tries to call `q.differentiate()` and, failing that, coerces `q` to the symbolic ring and differentiates it there.  Adding a `differentiate()` method which simply calls `q.diff()` would solve this problem.  Depending on what you think is best, you could silently ignore additional arguments to `diff`, or you could throw an error if additional arguments are present.



---

archive/issue_comments_093446.json:
```json
{
    "body": "Hi Marshall and Niles,\n\nThanks for testing the patch.  I never would have expected this behavior, so I'm glad it comes out now, thanks!!  I followed Niles' suggestion and added a `derivative` member function which calls `diff`.  If any additional arguments are specified, it throws an exception since I want to avoid situations like these where one tries to take the derivative of a form with respect to a coordinate.  This isn't an intrinsic (coordinate-independent) notion, so it would be better to enforce that in the code as well.\n\nMore generally, Marshall's issue uncovers something strange having to do with coercion into the symbolic ring: \n\n\n```\nsage: x, y = var('x, y')\nsage: U = CoordinatePatch((x, y)) \nsage: F = DifferentialForms(U)\nsage: q = DifferentialForm(F, 2)\nsage: q[0, 1] = sin(x*y); q\nsin(x*y)*dx/\\dy\nsage: SR(q)\nsin(x*y)*dx/\\dy\nsage: q.parent()\nAlgebra of differential forms in the variables x, y\nsage: SR(q).parent()\nSymbolic Ring\n```\n\n\nI.e, if I coerce `q` into the symbolic ring, it still looks like a differential form but its parent is `SR` and the behavior is completely wrong (wedge and diff members give the wrong results).  Shouldn't this kind of coercion raise an error, since this could never be the intended behavior?\n\nLet me know what you guys think -- for now I'll leave this as needs_work.",
    "created_at": "2010-09-02T05:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93446",
    "user": "https://github.com/jvkersch"
}
```

Hi Marshall and Niles,

Thanks for testing the patch.  I never would have expected this behavior, so I'm glad it comes out now, thanks!!  I followed Niles' suggestion and added a `derivative` member function which calls `diff`.  If any additional arguments are specified, it throws an exception since I want to avoid situations like these where one tries to take the derivative of a form with respect to a coordinate.  This isn't an intrinsic (coordinate-independent) notion, so it would be better to enforce that in the code as well.

More generally, Marshall's issue uncovers something strange having to do with coercion into the symbolic ring: 


```
sage: x, y = var('x, y')
sage: U = CoordinatePatch((x, y)) 
sage: F = DifferentialForms(U)
sage: q = DifferentialForm(F, 2)
sage: q[0, 1] = sin(x*y); q
sin(x*y)*dx/\dy
sage: SR(q)
sin(x*y)*dx/\dy
sage: q.parent()
Algebra of differential forms in the variables x, y
sage: SR(q).parent()
Symbolic Ring
```


I.e, if I coerce `q` into the symbolic ring, it still looks like a differential form but its parent is `SR` and the behavior is completely wrong (wedge and diff members give the wrong results).  Shouldn't this kind of coercion raise an error, since this could never be the intended behavior?

Let me know what you guys think -- for now I'll leave this as needs_work.



---

archive/issue_comments_093447.json:
```json
{
    "body": "Think of SR as a wrapper around any python object.  For example, continuing from your example above\n\n\n```\nsage: p=SR(q)\nsage: p.pyobject().parent()\nAlgebra of differential forms in the variables x, y\n```\n\n\nI think it's fine to let the explicit conversion SR(q) work---by default, explicitly converting to SR just wraps the object as above, and I think is supported for every Sage object, whether or not it makes \"sense\".  Do you see someplace that the conversion to an SR object is implicit?  That would be a problem.",
    "created_at": "2010-09-02T06:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93447",
    "user": "https://github.com/jasongrout"
}
```

Think of SR as a wrapper around any python object.  For example, continuing from your example above


```
sage: p=SR(q)
sage: p.pyobject().parent()
Algebra of differential forms in the variables x, y
```


I think it's fine to let the explicit conversion SR(q) work---by default, explicitly converting to SR just wraps the object as above, and I think is supported for every Sage object, whether or not it makes "sense".  Do you see someplace that the conversion to an SR object is implicit?  That would be a problem.



---

archive/issue_comments_093448.json:
```json
{
    "body": "By the way, I notice a lot of methods that have AttributeErrors.  For example, `q.trailing_coefficient()` appears in the tab completion, but gives an error on invocation.  Is filling out these methods that you've inherited (do \"q.\" and then press the tab key to see the methods available/inherited) a planned feature for the future?",
    "created_at": "2010-09-02T06:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93448",
    "user": "https://github.com/jasongrout"
}
```

By the way, I notice a lot of methods that have AttributeErrors.  For example, `q.trailing_coefficient()` appears in the tab completion, but gives an error on invocation.  Is filling out these methods that you've inherited (do "q." and then press the tab key to see the methods available/inherited) a planned feature for the future?



---

archive/issue_comments_093449.json:
```json
{
    "body": "Replying to [comment:30 jason]:\n\n> I think it's fine to let the explicit conversion SR(q) work---by default, explicitly converting to SR just wraps the object as above, and I think is supported for every Sage object, whether or not it makes \"sense\".  Do you see someplace that the conversion to an SR object is implicit?  That would be a problem.\n> \n\nI agree with Jason; I usually think of `SR` as \"the nothing ring\", or \"the everything ring\", depending on your point of view.  The problem with `diff(q)` previously returning 0 has to do with `SR(q).vars()` being empty.  That is, when converting to `SR`, the variables of `q` are not noticed.  If you wanted to be overly fancy, you could try to implement something so that the variables of `q` are created and recognized when one does `SR(q)`, but this seems pretty pointless to me.\n\nAlso, Joris, I completely agree on your decision to raise an error for additional arguments to `diff`.\n\nAs for the method inheritance problem, I'm of two minds.  This problem has come up for me (and probably others) too, and stems from wanting to inherit most of the functionality of another class, but not all of the methods.  The technically correct thing to do is write a new master class, inherit from that, and rewrite the other class also inheriting from the new master class -- this will probably take a while, and has the potential to raise subtle bugs.  The laziest thing to do is ignore the problem -- this will probably be fine for most users, and confusing for some.  A middle road is to go through all of the inherited methods and make sense out of the ones you can.  For those you can't, override the method to raise `NotImplementedError` or something similar, with a nice message about how this doesn't make sense for your class.\n\nFor this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.",
    "created_at": "2010-09-02T20:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93449",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:30 jason]:

> I think it's fine to let the explicit conversion SR(q) work---by default, explicitly converting to SR just wraps the object as above, and I think is supported for every Sage object, whether or not it makes "sense".  Do you see someplace that the conversion to an SR object is implicit?  That would be a problem.
> 

I agree with Jason; I usually think of `SR` as "the nothing ring", or "the everything ring", depending on your point of view.  The problem with `diff(q)` previously returning 0 has to do with `SR(q).vars()` being empty.  That is, when converting to `SR`, the variables of `q` are not noticed.  If you wanted to be overly fancy, you could try to implement something so that the variables of `q` are created and recognized when one does `SR(q)`, but this seems pretty pointless to me.

Also, Joris, I completely agree on your decision to raise an error for additional arguments to `diff`.

As for the method inheritance problem, I'm of two minds.  This problem has come up for me (and probably others) too, and stems from wanting to inherit most of the functionality of another class, but not all of the methods.  The technically correct thing to do is write a new master class, inherit from that, and rewrite the other class also inheriting from the new master class -- this will probably take a while, and has the potential to raise subtle bugs.  The laziest thing to do is ignore the problem -- this will probably be fine for most users, and confusing for some.  A middle road is to go through all of the inherited methods and make sense out of the ones you can.  For those you can't, override the method to raise `NotImplementedError` or something similar, with a nice message about how this doesn't make sense for your class.

For this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.



---

archive/issue_comments_093450.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-04T21:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93450",
    "user": "https://github.com/jvkersch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093451.json:
```json
{
    "body": "Thanks for elucidating the role of `SR`.  I don't think there is any implicit coercion anywhere of forms into `SR`, so this probably won't give any problems.\n\nReplying to [comment:32 niles]:\n\n> \n> For this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.\n\nOK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.",
    "created_at": "2010-09-04T21:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93451",
    "user": "https://github.com/jvkersch"
}
```

Thanks for elucidating the role of `SR`.  I don't think there is any implicit coercion anywhere of forms into `SR`, so this probably won't give any problems.

Replying to [comment:32 niles]:

> 
> For this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.

OK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.



---

archive/issue_comments_093452.json:
```json
{
    "body": "Replying to [comment:33 jvkersch]:\n> Thanks for elucidating the role of `SR`.  I don't think there is any implicit coercion anywhere of forms into `SR`, so this probably won't give any problems.\n> \n> Replying to [comment:32 niles]:\n> \n> > \n> > For this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.\n> \n> OK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.\n\nI think you've gone above and beyond the requirement with this last one.  Thanks!  Again, I think the code looks good.  If someone else wants to give a final positive review on the mathematical foundation, let's mark this positive review and get it in.",
    "created_at": "2010-09-04T21:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93452",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:33 jvkersch]:
> Thanks for elucidating the role of `SR`.  I don't think there is any implicit coercion anywhere of forms into `SR`, so this probably won't give any problems.
> 
> Replying to [comment:32 niles]:
> 
> > 
> > For this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.
> 
> OK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.

I think you've gone above and beyond the requirement with this last one.  Thanks!  Again, I think the code looks good.  If someone else wants to give a final positive review on the mathematical foundation, let's mark this positive review and get it in.



---

archive/issue_comments_093453.json:
```json
{
    "body": "Jason, I agree, I think this is in good enough shape for inclusion.  I think its important to get this sort of new functionality in as soon as possible as long as the design looks reasonable, which it does.  \n\nI think this is very exciting, its the sort of functionality that Sage is meant for, and I'm very happy to see this addition.",
    "created_at": "2010-09-05T03:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93453",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Jason, I agree, I think this is in good enough shape for inclusion.  I think its important to get this sort of new functionality in as soon as possible as long as the design looks reasonable, which it does.  

I think this is very exciting, its the sort of functionality that Sage is meant for, and I'm very happy to see this addition.



---

archive/issue_comments_093454.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-05T03:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93454",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093455.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-05T03:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93455",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093456.json:
```json
{
    "body": "Could someone please update [attachment:trac9650_differential_forms_v2.patch] with a more descriptive commit string that includes the ticket number?  For example: `#9650: Add support for differential forms`.",
    "created_at": "2010-09-05T03:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93456",
    "user": "https://github.com/qed777"
}
```

Could someone please update [attachment:trac9650_differential_forms_v2.patch] with a more descriptive commit string that includes the ticket number?  For example: `#9650: Add support for differential forms`.



---

archive/issue_comments_093457.json:
```json
{
    "body": "Attachment [trac9650_differential_forms_v2.patch](tarball://root/attachments/some-uuid/ticket9650/trac9650_differential_forms_v2.patch) by @jvkersch created at 2010-09-05 07:53:00\n\nReplying to [comment:37 mpatel]:\n> Could someone please update [attachment:trac9650_differential_forms_v2.patch] with a more descriptive commit string that includes the ticket number?  For example: `#9650: Add support for differential forms`.\n\nDone -- thanks for pointing that out.",
    "created_at": "2010-09-05T07:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93457",
    "user": "https://github.com/jvkersch"
}
```

Attachment [trac9650_differential_forms_v2.patch](tarball://root/attachments/some-uuid/ticket9650/trac9650_differential_forms_v2.patch) by @jvkersch created at 2010-09-05 07:53:00

Replying to [comment:37 mpatel]:
> Could someone please update [attachment:trac9650_differential_forms_v2.patch] with a more descriptive commit string that includes the ticket number?  For example: `#9650: Add support for differential forms`.

Done -- thanks for pointing that out.



---

archive/issue_comments_093458.json:
```json
{
    "body": "Hi Jason and Marshall,\n\nThanks a lot for the final positive review and thanks all for the many comments along the way -- I can honestly say that I've learned more about Sage (and even Python) in the last few weeks than ever before!  Hopefully I can keep contributing in the future.\n\nBest wishes,\nJoris",
    "created_at": "2010-09-05T07:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93458",
    "user": "https://github.com/jvkersch"
}
```

Hi Jason and Marshall,

Thanks a lot for the final positive review and thanks all for the many comments along the way -- I can honestly say that I've learned more about Sage (and even Python) in the last few weeks than ever before!  Hopefully I can keep contributing in the future.

Best wishes,
Joris



---

archive/issue_comments_093459.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-05T07:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93459",
    "user": "https://github.com/jvkersch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093460.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-05T08:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93460",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093461.json:
```json
{
    "body": "corrected formatting for NotImplemented methods",
    "created_at": "2010-09-05T17:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93461",
    "user": "https://github.com/nilesjohnson"
}
```

corrected formatting for NotImplemented methods



---

archive/issue_comments_093462.json:
```json
{
    "body": "Attachment [trac9650_differential_forms_v2-reviewer.patch](tarball://root/attachments/some-uuid/ticket9650/trac9650_differential_forms_v2-reviewer.patch) by @nilesjohnson created at 2010-09-05 17:26:05\n\nReplying to [comment:33 jvkersch]:\n\n> OK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.\n\nThis looks great, and I agree with others on getting it included into sage soon.  There were some formatting errors in the new docstrings (need newline between `EXAMPLES::` and indented code block), and since someone else gave the positive review I just uploaded a corrected version (apply only [attachment:trac9650_differential_forms_v2-reviewer.patch]).",
    "created_at": "2010-09-05T17:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93462",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac9650_differential_forms_v2-reviewer.patch](tarball://root/attachments/some-uuid/ticket9650/trac9650_differential_forms_v2-reviewer.patch) by @nilesjohnson created at 2010-09-05 17:26:05

Replying to [comment:33 jvkersch]:

> OK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.

This looks great, and I agree with others on getting it included into sage soon.  There were some formatting errors in the new docstrings (need newline between `EXAMPLES::` and indented code block), and since someone else gave the positive review I just uploaded a corrected version (apply only [attachment:trac9650_differential_forms_v2-reviewer.patch]).



---

archive/issue_comments_093463.json:
```json
{
    "body": "Hi Niles,\n\nSorry for the formatting error and thanks for catching it so soon.  I will go over everything again soon, and if I find any more inconsistencies which crept in during my last round of implementations, I will post a new patch.",
    "created_at": "2010-09-07T09:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93463",
    "user": "https://github.com/jvkersch"
}
```

Hi Niles,

Sorry for the formatting error and thanks for catching it so soon.  I will go over everything again soon, and if I find any more inconsistencies which crept in during my last round of implementations, I will post a new patch.



---

archive/issue_comments_093464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9650#issuecomment-93464",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009786.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-15T10:39:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9650",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9650#event-9786"
}
```
