# Issue 8161: use Sphinx to produce docstrings from the command line

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-02-03 02:34:04

Assignee: mvngu

The attached patch uses Sphinx to produce docstrings from the command line.  The docstrings are still plain text, but among other things, all double colons should be turned into single colons.  The patch also (by hand) changes ```text``` to `"text"`, which I think looks better and conveys the same information.

It also no longer replaces `\\` with `\\\\` for docstrings in the notebook, since there is a line in sphinxify that just undoes this.

This depends on #8160.



---

Comment by jhpalmieri created at 2010-02-03 02:35:03

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-02-03 03:47:08

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-02-03 03:47:08

I think the idea is good, but this needs work; I'm getting some doctest failures with this patch:

```
The following tests failed:

	sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/structure/element.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 6 doctests failed
	sage -t -long devel/sage/sage/structure/element_wrapper.py # Segfault
	sage -t -long devel/sage/sage/misc/sageinspect.py # 4 doctests failed
	sage -t -long devel/sage/sage/structure/dynamic_class.py # 1 doctests failed
```

I'll try to work on them, and anyone else who is interested can do the same.


---

Attachment


---

Comment by jhpalmieri created at 2010-02-03 04:41:24

With this patch, all tests pass on boxen.


---

Comment by jhpalmieri created at 2010-02-03 04:41:24

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-04 06:34:08

This looks good.  I noticed an existing problem with Unicode docstrings.  With #8051 and with or without #8167,

```python
sage: sagenb.notebook.worksheet.Worksheet.name?
sage: sagenb.misc.misc.unicode_str?
```

have `'<no docstring>'`.  V2 should fix this.


---

Attachment

Handle Unicode docstrings.  Replaces previous.  *sage* repo.


---

Comment by mpatel created at 2010-02-04 06:54:33

Update `sagenb.misc.sageinspect` doctests.  *sagenb* repo.


---

Attachment

V2 replaces `return str(r)` with

```python
    from sagenb.misc.misc import encoded_str
    return encoded_str(r)
```

in `sage.misc.sageinspect._sage_getdoc_unformatted`.

The sagenb patch depends on #8051 + #8167 + #8102 + #8160.


---

Comment by jhpalmieri created at 2010-02-05 03:55:50

On further reflection, I've decided that replacing ```` with `"` is a bad idea.  It's complicated, and it can make some docstrings less clear.  For example, should ```"text"``` be turned into `"text"` or `"'text'"`?  What about ```algorithm="gap"```: turn it into `"algorithm='gap'"`?  What about (from sage.interfaces.sage0.Sage) the beautiful ```s('"x"')```?

If we eventually decide this is a good idea, we can do it in another ticket (or submit it as a possible customization for text output in Sphinx), but I'm taking it out for now.

A few doctests in sage and sagenb need to be changed as a consequence; see the new patches.


---

Comment by jhpalmieri created at 2010-02-05 03:56:19

for sage repo


---

Attachment

for sagenb repo


---

Comment by mpatel created at 2010-02-05 07:02:43

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 14:53:50

Resolution: fixed
