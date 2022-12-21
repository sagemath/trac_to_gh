# Issue 9650: Adding support for differential forms

Issue created by migration from Trac.

Original creator: jvkersch

Original creation time: 2010-07-31 11:48:00

Assignee: burcin

CC:  mhampton jason jdemeyer mpatel novoselt niles

Keywords: forms, functions, symbolics

Implements support for differential forms to Sage.  After applying the patch, three new classes are added to sage:

 1. `CoordinatePatch` -- an open subset of Rn on which differential forms can be defined
 1. `DifferentialForms` -- a differential forms parent
 1. `DifferentialForm` -- a differential forms class.

Please see the documentation in the `DifferentialForm` class for more information about syntax, available methods, etc.

This is a very basic implementation, providing support for exterior differentiation and wedge products of forms, but not much more.  The emphasis is on making sure that the framework is implemented correctly.

See discussion at

 1. http://wiki.sagemath.org/tensorcalc
 1. http://groups.google.be/group/sage-devel/browse_thread/thread/2feef1f0be557585/c2b7095747ebe34d


---

Comment by jason created at 2010-07-31 18:30:05

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

Integral[ d `@` ((x/2) d[y] - (y/2) d[y]) , 	Chain[ {x -> s, y -> t}, \
{s, 0, 1}, {t, 0, 1}]] ==	
Integral[ ((x/2) d[y] - (y/2) d[y]) , 	Boundary `@` Chain[ {x -> s, y -> \
t}, {s, 0, 1}, {t, 0, 1}]]
```



---

Comment by jason created at 2010-07-31 18:30:05

Changing status from new to needs_work.


---

Comment by jason created at 2010-07-31 18:30:37

Also, if you feel like the patch is to the point that it needs review, please change the status below to "needs review".


---

Comment by jvkersch created at 2010-08-01 16:55:11

Thanks for the comments, which not only improved the patch but my Python knowledge as well!  I've updated the patch in the meantime.  Thanks also for guiding me through the sage patch process!

Some quick comments and questions:

1.  As for integration of forms, I think this is definitely doable and in fact should be dealt with before the other stuff (metric geometry, etc).

2.  I'm very interesting in seeing how the authors of that mathematica package represented differential forms -- thanks for the link!

3. Once I've taken a good look at the mathematica package, I'll set the patch to "needs review".


---

Comment by jvkersch created at 2010-08-04 08:52:36

I'm going to set the patch to "needs review", firstly since as burcin pointed out in a private email, the licensing situation of the mathematica package is somewhat unclear, and secondly the implementation of the differential forms class is sufficiently simple so that the issue won't be with the algorithms that I used but rather whether this is good sage programming.

Some things to keep in mind: right now, the way to create a differential form is as follows: first you create a !``CoordinatePatch!`` on which forms can be defined, then you create a !``DifferentialForms!`` parent and then you can create forms.  Explicitly, this looks like


```

        sage: x, y, z = var('x, y, z')
        sage: U = CoordinatePatch((x, y, z))
        sage: F = DifferentialForms(U)
        sage: form = DifferentialForm(F, 0, sin(x*y)); form
        sin(x*y)

```


Let me know if this construction is confusing or can be simplified in any way.


---

Comment by jvkersch created at 2010-08-04 08:52:36

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-08-04 14:42:40

Oops: inside of triple-braces, things are quoted literally:


```
sage: x, y, z = var('x, y, z')
sage: U = CoordinatePatch((x, y, z))
sage: F = DifferentialForms(U)
sage: form = DifferentialForm(F, 0, sin(x*y)); form
sin(x*y)
```



---

Comment by mpatel created at 2010-08-23 01:19:32

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

Comment by niles created at 2010-08-23 16:53:10

Changing status from needs_review to needs_work.


---

Comment by niles created at 2010-08-23 16:53:10

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

Comment by niles created at 2010-08-23 16:54:55

the first point is about `__init__.py`; sorry for the misformatting!


---

Comment by niles created at 2010-08-23 17:08:17

oh, and doctest coverage is at 100% for each of the 3 files!


---

Comment by jvkersch created at 2010-08-24 12:44:39

Hi Niles and Mitesh,

Thank you for your instructive comments.  Niles, thanks also for agreeing to review my patch!  The suggestion to include this functionality to the reference manual was especially helpful -- it makes everything so much clearer to see the documentation in nice, crisp HTML form.

I implemented the changes you suggested (adding to the reference manual, adding authors, making `gens()` return a tuple), but I have a few questions/comments that are more of a technical nature, revealing simultaneously my mercurial ineptitude:

1.  I made a mess of the upload section -- could someone with admin privileges delete all but the most recent attachment?

2.  Try as I might, I could not produce a patch which creates the file `__init__.py`.  I added that file to my sage tree as per the documentation, instructed hg to add it, confirmed with `hg status` that it was listed as added, but when I look at `hg diff` that file is nowhere to be found.  The other files are created/modified as expected.  The patch also does not create `__init__.py`, as you experienced.  Are these init files somehow special as far as hg is concerned?

3.  I called the package `tensor` rather than anything more specific in order to accommodate future additions: it would be good to have support for generic tensors (not just differential forms) and common operations on them (e.g. covariant derivations), so that we could for instance do symbolic Riemannian geometry.  However, if you think we should stick to a more specific name for now, then that's fine with me too.


---

Comment by jason created at 2010-08-24 14:23:26

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

Comment by jvkersch created at 2010-08-24 19:47:06

Replying to [comment:18 jason]:

> A peculiarity of Mercurial is that it can't check in empty files.  So usually we'll add either a space, or a comment like:
> (...)


Thanks a lot for pointing that out -- this is really helpful!

I've updated the patch with the `__init__.py`, verified that it passes all doctests, and added those files to the reference manual section.  So I'm changing the status back to `needs_review`.


---

Comment by jvkersch created at 2010-08-24 19:47:06

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-08-24 21:27:14

It looks like the top of coordinate_patch.py is repeated around line 232.  Was that intentional?


---

Comment by jason created at 2010-08-24 21:28:55

In fact, it looks like the entire content of coordinate_patch.py is duplicated, starting around line 232 of that file.


---

Comment by niles created at 2010-08-25 15:00:57

Changing status from needs_review to needs_work.


---

Comment by niles created at 2010-08-25 15:00:57

Hi Joris,

Things are looking good, but the documentation produces some warnings related to formatting errors--please fix this in addition to deleting the duplicates from `coordinate_patch.py`.  There are also some formatting problems in the documentation which do not produce warnings, so please check the html documentation carefully.

Also, do you think the documentation files could have better names?  I find it funny that the documentation for "`DifferentialForm`" is titled "Differential forms class" and the documentation for "`DifferentialForms`" is titled something else. (But again I'll defer to you on this :)


---

Comment by jvkersch created at 2010-08-30 21:52:58

Hi Jason and Niles,

Thanks for your comments, in particular for catching that code duplication.  I've tried to address your suggestions as well as I could, and here are the changes in the most recent version of the patch:

1.  I've fixed the documentation so that it generates the output without any warnings, and I've also addressed the formatting issues.  This proved to be really tricky...

2.  I agree on the names of the documentation files.  In the current patch, the documentation now reads: "Algebra of differential forms" for `differential_forms.py` and "Elements of the algebra of differential forms" for `differential_form_element.py`.  I believe that this is both clearer and more in line with the rest of the Sage docs, but please feel free to correct me on this!

Thanks for all your time on the review!


---

Comment by jvkersch created at 2010-08-30 21:55:22

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-08-30 21:58:16

Joris, could you add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames), when it's convenient?


---

Comment by jason created at 2010-08-31 03:30:18

The most recent patch looks good to me.  Doctests pass, playing around with some examples seems fine, and docs build.  However, as this is not my area, at least one other person should pass off on this (niles?).


---

Comment by mhampton created at 2010-08-31 15:02:29

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

Comment by niles created at 2010-08-31 17:07:31

Changing status from needs_review to needs_work.


---

Comment by niles created at 2010-08-31 17:07:31

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

Comment by jvkersch created at 2010-09-02 05:37:39

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

Comment by jason created at 2010-09-02 06:32:04

Think of SR as a wrapper around any python object.  For example, continuing from your example above


```
sage: p=SR(q)
sage: p.pyobject().parent()
Algebra of differential forms in the variables x, y
```


I think it's fine to let the explicit conversion SR(q) work---by default, explicitly converting to SR just wraps the object as above, and I think is supported for every Sage object, whether or not it makes "sense".  Do you see someplace that the conversion to an SR object is implicit?  That would be a problem.


---

Comment by jason created at 2010-09-02 06:34:16

By the way, I notice a lot of methods that have AttributeErrors.  For example, `q.trailing_coefficient()` appears in the tab completion, but gives an error on invocation.  Is filling out these methods that you've inherited (do "q." and then press the tab key to see the methods available/inherited) a planned feature for the future?


---

Comment by niles created at 2010-09-02 20:58:52

Replying to [comment:30 jason]:

> I think it's fine to let the explicit conversion SR(q) work---by default, explicitly converting to SR just wraps the object as above, and I think is supported for every Sage object, whether or not it makes "sense".  Do you see someplace that the conversion to an SR object is implicit?  That would be a problem.
> 

I agree with Jason; I usually think of `SR` as "the nothing ring", or "the everything ring", depending on your point of view.  The problem with `diff(q)` previously returning 0 has to do with `SR(q).vars()` being empty.  That is, when converting to `SR`, the variables of `q` are not noticed.  If you wanted to be overly fancy, you could try to implement something so that the variables of `q` are created and recognized when one does `SR(q)`, but this seems pretty pointless to me.

Also, Joris, I completely agree on your decision to raise an error for additional arguments to `diff`.

As for the method inheritance problem, I'm of two minds.  This problem has come up for me (and probably others) too, and stems from wanting to inherit most of the functionality of another class, but not all of the methods.  The technically correct thing to do is write a new master class, inherit from that, and rewrite the other class also inheriting from the new master class -- this will probably take a while, and has the potential to raise subtle bugs.  The laziest thing to do is ignore the problem -- this will probably be fine for most users, and confusing for some.  A middle road is to go through all of the inherited methods and make sense out of the ones you can.  For those you can't, override the method to raise `NotImplementedError` or something similar, with a nice message about how this doesn't make sense for your class.

For this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.


---

Comment by jvkersch created at 2010-09-04 21:28:03

Changing status from needs_work to needs_review.


---

Comment by jvkersch created at 2010-09-04 21:28:03

Thanks for elucidating the role of `SR`.  I don't think there is any implicit coercion anywhere of forms into `SR`, so this probably won't give any problems.

Replying to [comment:32 niles]:

> 
> For this ticket, I'd be in support of raising `NotImplementedError`s for all of the broken inherited methods, and writing a new ticket to implement those that can be.

OK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.


---

Comment by jason created at 2010-09-04 21:51:56

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

Comment by mhampton created at 2010-09-05 03:13:49

Jason, I agree, I think this is in good enough shape for inclusion.  I think its important to get this sort of new functionality in as soon as possible as long as the design looks reasonable, which it does.  

I think this is very exciting, its the sort of functionality that Sage is meant for, and I'm very happy to see this addition.


---

Comment by mhampton created at 2010-09-05 03:13:49

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-05 03:57:55

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-05 03:57:55

Could someone please update [attachment:trac9650_differential_forms_v2.patch] with a more descriptive commit string that includes the ticket number?  For example: `#9650: Add support for differential forms`.


---

Attachment

Replying to [comment:37 mpatel]:
> Could someone please update [attachment:trac9650_differential_forms_v2.patch] with a more descriptive commit string that includes the ticket number?  For example: `#9650: Add support for differential forms`.

Done -- thanks for pointing that out.


---

Comment by jvkersch created at 2010-09-05 07:59:33

Hi Jason and Marshall,

Thanks a lot for the final positive review and thanks all for the many comments along the way -- I can honestly say that I've learned more about Sage (and even Python) in the last few weeks than ever before!  Hopefully I can keep contributing in the future.

Best wishes,
Joris


---

Comment by jvkersch created at 2010-09-05 07:59:49

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-09-05 08:02:25

Changing status from needs_review to positive_review.


---

Comment by niles created at 2010-09-05 17:18:49

corrected formatting for NotImplemented methods


---

Attachment

Replying to [comment:33 jvkersch]:

> OK, I've updated the patch so that the methods which are not applicable raise `NotImplementedError`.  I don't know if I've done this properly though, since including all the doctests this amounts to quite a bit of additional code.

This looks great, and I agree with others on getting it included into sage soon.  There were some formatting errors in the new docstrings (need newline between `EXAMPLES::` and indented code block), and since someone else gave the positive review I just uploaded a corrected version (apply only [attachment:trac9650_differential_forms_v2-reviewer.patch]).


---

Comment by jvkersch created at 2010-09-07 09:33:23

Hi Niles,

Sorry for the formatting error and thanks for catching it so soon.  I will go over everything again soon, and if I find any more inconsistencies which crept in during my last round of implementations, I will post a new patch.


---

Comment by mpatel created at 2010-09-15 10:39:29

Resolution: fixed
