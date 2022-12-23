# Issue 8209: make docstring processing available for introspection, and fix mathtt

Issue created by migration from https://trac.sagemath.org/ticket/8209

Original creator: jhpalmieri

Original creation time: 2010-02-07 17:56:20

Assignee: mvngu

CC:  mpatel

Two issues: several docstrings contain `\mathtt{self`}, and jsMath doesn't recognize this command, so it's not typeset correctly, either with introspection from the notebook or in the reference manual.  Do this in the notebook, for example:

```
sage: a = 5
sage: a.is_power_of?
```

Or look at the docstring for `is_power_of` in sage.rings.integer in the reference manual (assuming you've built the ref manual with the '--jsmath' option).

Second, several docstrings use dollar signs, and while these are processed correctly for the reference manual (turning `$x=y$` into ``x=y``), they are not dealt with in introspection in the notebook.  Evaluate `sage.categories.g_sets.GSets?`, for example: you'll see `$G$` rather than _G_.

The attached patch therefore does these things:

 - moves the function `process_dollars` from SAGE_ROOT/devel/sage/doc/common/conf.py to SAGE_ROOT/devel/sage/sage/misc/sagedoc.py, where it can be used to format each docstring before displaying it.

 - implements a similar function `process_mathtt` which converts `\mathtt{blah`} to `\verb|blah|`, which jsMath can handle.  Oh, except on the command line, it just turns `\mathtt{blah`} to `blah`, which I think is easier to read.


---

Attachment


---

Comment by jhpalmieri created at 2010-02-07 17:57:28

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-02-07 21:39:57

Note: this patch fixes the problem reported in #8196 with tty doc output, thus a (partial)
positive review for that issue.


---

Comment by mpatel created at 2010-02-09 04:16:44

Call `process_mathtt` with `embedded=True` in docbuild.  Apply only this patch.  sage repo.


---

Attachment

Should we call `process_mathtt` with `embedded=True` when building the reference manual?  V2 makes this change, but it's for both jsMath and PNG math modes.  Is that OK?


---

Comment by jhpalmieri created at 2010-02-09 07:07:16

Good catch about using `embedded=True`.  How about this version: it changes the first line of process_mathtt in conf.py from

```
if len(docstringlines) > 0:
```

to

```
if len(docstringlines) > 0 and 'SAGE_DOC_JSMATH' in os.environ:
```



---

Attachment

apply only this patch (sage repo)


---

Comment by mpatel created at 2010-02-10 14:08:17

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 14:08:17

Oops.  Of course, that's the right way.


---

Comment by mpatel created at 2010-02-10 15:49:18

For the record: Applying the patch 4.3.2 + [a long queue](http://trac.sagemath.org/sage_trac/ticket/8186#comment:6) gives

```
applying trac_8209-mathtt.3.patch
patching file sage/misc/sagedoc.py
Hunk #1 succeeded at 191 with fuzz 1 (offset 2 lines).
Hunk #2 succeeded at 396 with fuzz 2 (offset 2 lines).
```

possibly because I've haven't yet applied #8161.


---

Comment by mpatel created at 2010-02-10 23:15:23

Replying to [comment:6 mpatel]:
> [...]possibly because I've haven't yet applied #8161.
Yes.


---

Comment by mpatel created at 2010-02-11 14:54:04

Resolution: fixed
