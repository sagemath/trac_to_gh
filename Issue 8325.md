# Issue 8325: Sphinx warning: 'Could not parse cython argspec'

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-22 05:45:15

Assignee: mvngu

CC:  jhpalmieri

Sphinx warnings from building the HTML reference manual include:

```
matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL: Could not parse cython argspec
plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3d.export_jmol: Could not parse cython argspec
```


Related: #8244.


---

Comment by mpatel created at 2010-02-22 05:56:07

Alternate way to get Cython argspec.  sage repo.


---

Comment by mpatel created at 2010-02-22 05:58:34

Changing status from new to needs_review.


---

Attachment

The patch should work for the cases in the description.


---

Comment by jhpalmieri created at 2010-02-24 22:18:14

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-02-24 22:18:14

Should patches like this also come with a corresponding one to sagenb.misc.sageinspect, as in #8324?

Looks good, no warnings when building the reference manual for these two files, and the relevant pages look good.  Nice solution.


---

Comment by jhpalmieri created at 2010-02-24 22:26:28

(Is it dangerous to use "exec" here?  It looks okay to me, but I feel as though I should always be suspicious of using it.)


---

Comment by mpatel created at 2010-02-25 07:03:27

Replying to [comment:3 jhpalmieri]:
> (Is it dangerous to use "exec" here?  It looks okay to me, but I feel as though I should always be suspicious of using it.)
I think you're right.  The `exec`'d code could have bad side effects.  I'm about to attach a patch that uses [comment:ticket:8244:5 this AST code], instead.


---

Comment by mpatel created at 2010-02-25 07:03:34

Changing status from positive_review to needs_work.


---

Attachment

AST version.  sage repo.


---

Comment by mpatel created at 2010-02-25 07:39:52

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-25 07:39:52

I've attached the AST version, which seems to work for me, although I have no formal training in computer science.  If the patch looks good, I'll add a sagenb repository patch.


---

Comment by jhpalmieri created at 2010-03-04 05:49:49

On one hand, this seems to fix the two particular doctests in question.  On the other, it's not perfect. I can see two problems, one of which I know how to fix:

 - if the source has the (unlikely) form `def f({(1,2,3): True}): ...`, then this version (and all previous versions) will think that the arg spec ends after `(1,2,3):`.  The function `_sage_getargspec_from_ast` can actually handle this kind of thing, though, so I think we should pass the entire source code to it, rather than truncate at the first `):`.  That is, delete line 470 and change line 471 from

```
proxy = 'def dummy' + source[beg:end] + '\n    return' 
```

 to

```
proxy = 'def dummy' + source[beg:] + '\n    return' 
```


 - if the docstring has type information, it can't handle it.  I don't know what to do about this, or if it's worth it.

Should we fix the first problem and then go ahead with this?  I also notice that the methods for `SageArgSpecVisitor` don't have doctests.  Is that possible for these sorts of things?  I know nothing about ast.


---

Attachment

Another clause.  More doctests.  Apply only this patch.   sage repo.


---

Comment by mpatel created at 2010-03-04 09:26:15

V3:

 * Implements your idea to pass the entire source code.  I've included the previous version as a fallback, since `LLL` has a Cython-only construct:

```python
R = <Matrix_integer_dense>self.new_matrix(entries=map(ZZ,A.list()))
```


 * Has extra, more direct doctests of `SageArgSpecVisitor`'s methods.

I don't mind leaving the second problem for another day.


---

Comment by jhpalmieri created at 2010-03-04 20:00:31

Looks good.  All doctests pass, fixes the two problems.


---

Comment by jhpalmieri created at 2010-03-04 20:00:31

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-03-04 23:42:33

For SageNB's `sageinspect.py`.  sagenb repo.


---

Comment by mpatel created at 2010-03-04 23:46:46

Changing status from positive_review to needs_work.


---

Attachment

I've attached a version for SageNB.


---

Comment by mpatel created at 2010-03-04 23:46:53

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-05 01:11:30

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-03-05 01:11:30

Unless I'm misunderstanding, the sagenb patch needs work: all of the doctests in the patch import from `sage.misc.sageinspect` rather than from `sagenb...`.


---

Comment by mpatel created at 2010-03-05 01:25:44

Fix doctest imports.  Replaces previous sagenb patch.


---

Attachment

Oops.  Sorry about that.  V2 is up.


---

Comment by mpatel created at 2010-03-05 01:26:41

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-05 02:51:53

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 09:24:56

I've merged the Sage library patch.  When this is merged in the notebook, we can close this ticket.


---

Comment by mhansen created at 2010-03-06 09:24:56

Remove assignee mvngu.


---

Comment by mpatel created at 2010-03-09 05:00:49

Resolution: fixed


---

Comment by mpatel created at 2010-03-09 05:00:49

Merged sagenb patch V2 in sagenb-0.7.5.3, which will be at #8435.
