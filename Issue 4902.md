# Issue 4902: convert sage.algebras.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4902

Original creator: mhansen

Original creation time: 2009-01-01 22:45:35

Assignee: tba




---

Attachment


---

Comment by jhpalmieri created at 2009-01-07 20:22:25

Mostly looks good.  I have one major issue, and then some little things:

One major problem: I notice that methods starting with `_` seem to be missing from the html version of the documentation (e.g., `__cmp__` and `__init__`). These were present in the the old version; was there a reason for their omission? Because of this omission, I'm not going to be able to review the changes to the docstrings of such methods (because I'm not familiar enough with ReST, and so I'm using both the source code and the html to do the review).

Minor things:

free_algebra.py, lines 165-167 (a blank line, then ::, then a blank line in the docstring for `FreeAlgebra_generic`): these can be deleted, I think, since they needlessly break the EXAMPLES into two sections.

quaternion_algebra.py, line 134.  Why in the html version does the line

```
def QuaternionAlgebra(K, a, b, names=['i','j','k'], denom=1): 
```

end up showing a comma after the left bracket?  It looks like `names=[, 'i', 'j', 'k']`.

quaternion_algebra.py, line 321: in the html, the string ``\mathbb{Z}[i]`,` can allow a line break between Z[i] and the comma.  Can this be avoided?

quaternion_algebra_element.py, line 219: need a line break and an empty line between "Do we?" and "EXAMPLES::"

quaternion_algebra_element.py, line 234: need a line break and an empty line between "scalar part..." and "EXAMPLES::"

steenrod_algebra_bases.py, lines 121-122: I don't think that "INTERNAL DOCUMENTATION" needs to be a section heading, or whatever it is now.  Maybe change this to "INTERNAL DOCUMENTATION::" and delete the line of hyphens following it?

steenrod_algebra_bases.py, lines 128-149: each line starting with "add" is supposed to be an item in a list.

steenrod_algebra_bases.py, lines 1394-1395: ``t`th iterated commutator of consecutive  `\text{Sq}<sup>{2</sup>i}` 's.` isn't being rendered properly.  Maybe change ``t`th` to ``t^{th}``?

The same thing happens on line 1417 with ``n`th`.

steenrod_algebra_bases.py, line 1462: the original text said `the cache _steenrod_bases is set to {} before doing the computations.`, but the {} disappeared in the new version.

steenrod_algebra_element.py, lines 11-12: `EXAMPLES` should have a double colon after it, and the line of hyphens below it should be deleted.

steenrod_algebra_element.py, lines 272-273: as above, perhaps `INTERNAL DOCUMENTATION` should have :: after it, and no line of hyphens below it.

steenrod_algebra_element.py, line 1518: change ``i`th` to ``i^{th}``

steenrod_algebra_element.py, line 1530: change ``k`th` to ``k^{th}``


---

Attachment


---

Comment by mhansen created at 2009-01-08 21:13:04

I've posted a patch which takes care of a number of the issues you noted.

The problem with "def QuaternionAlgebra" is internal to Sphinx.  I'll send a message to their mailing list.

Currently, the documentation for "internal" methods that start with "_" are not included in the reference manual by default.  In the future, I have some ideas for extending Sphinx's autodoc extension to be able to include things underscore methods without cluttering things up for users not interested in them.


---

Comment by jhpalmieri created at 2009-01-08 23:33:08

Replying to [comment:3 mhansen]:
> I've posted a patch which takes care of a number of the issues you noted.

Great, I'll take a look soon.

> Currently, the documentation for "internal" methods that start with "_" are not included in the reference manual by default.  In the future, I have some ideas for extending Sphinx's autodoc extension to be able to include things underscore methods without cluttering things up for users not interested in them.

From Sage's point of view, various classes have a lot of documentation in the __init__ method, so unfortunately leaving them out means leaving out some important things.  Anyway...


---

Comment by jhpalmieri created at 2009-01-09 00:14:27

Looks good, positive review.  You also caught some things that I had missed, or maybe you were fixing typos in the original documentation.  Thanks.


---

Attachment


---

Comment by mabshoff created at 2009-02-24 18:48:47

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 18:48:47

Resolution: fixed
