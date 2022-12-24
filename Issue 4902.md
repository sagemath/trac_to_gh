# Issue 4902: convert sage.algebras.* docstrings to Sphinx

archive/issues_004902.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4902\n\n",
    "created_at": "2009-01-01T22:45:35Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "convert sage.algebras.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4902",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4902





---

archive/issue_comments_037186.json:
```json
{
    "body": "Attachment [trac_4902.patch](tarball://root/attachments/some-uuid/ticket4902/trac_4902.patch) by mhansen created at 2009-01-02 03:00:24",
    "created_at": "2009-01-02T03:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37186",
    "user": "mhansen"
}
```

Attachment [trac_4902.patch](tarball://root/attachments/some-uuid/ticket4902/trac_4902.patch) by mhansen created at 2009-01-02 03:00:24



---

archive/issue_comments_037187.json:
```json
{
    "body": "Mostly looks good.  I have one major issue, and then some little things:\n\nOne major problem: I notice that methods starting with `_` seem to be missing from the html version of the documentation (e.g., `__cmp__` and `__init__`). These were present in the the old version; was there a reason for their omission? Because of this omission, I'm not going to be able to review the changes to the docstrings of such methods (because I'm not familiar enough with ReST, and so I'm using both the source code and the html to do the review).\n\nMinor things:\n\nfree_algebra.py, lines 165-167 (a blank line, then ::, then a blank line in the docstring for `FreeAlgebra_generic`): these can be deleted, I think, since they needlessly break the EXAMPLES into two sections.\n\nquaternion_algebra.py, line 134.  Why in the html version does the line\n\n```\ndef QuaternionAlgebra(K, a, b, names=['i','j','k'], denom=1): \n```\n\nend up showing a comma after the left bracket?  It looks like `names=[, 'i', 'j', 'k']`.\n\nquaternion_algebra.py, line 321: in the html, the string ``\\mathbb{Z}[i]`,` can allow a line break between Z[i] and the comma.  Can this be avoided?\n\nquaternion_algebra_element.py, line 219: need a line break and an empty line between \"Do we?\" and \"EXAMPLES::\"\n\nquaternion_algebra_element.py, line 234: need a line break and an empty line between \"scalar part...\" and \"EXAMPLES::\"\n\nsteenrod_algebra_bases.py, lines 121-122: I don't think that \"INTERNAL DOCUMENTATION\" needs to be a section heading, or whatever it is now.  Maybe change this to \"INTERNAL DOCUMENTATION::\" and delete the line of hyphens following it?\n\nsteenrod_algebra_bases.py, lines 128-149: each line starting with \"add\" is supposed to be an item in a list.\n\nsteenrod_algebra_bases.py, lines 1394-1395: ``t`th iterated commutator of consecutive  `\\text{Sq}<sup>{2</sup>i}` 's.` isn't being rendered properly.  Maybe change ``t`th` to ``t^{th}``?\n\nThe same thing happens on line 1417 with ``n`th`.\n\nsteenrod_algebra_bases.py, line 1462: the original text said `the cache _steenrod_bases is set to {} before doing the computations.`, but the {} disappeared in the new version.\n\nsteenrod_algebra_element.py, lines 11-12: `EXAMPLES` should have a double colon after it, and the line of hyphens below it should be deleted.\n\nsteenrod_algebra_element.py, lines 272-273: as above, perhaps `INTERNAL DOCUMENTATION` should have :: after it, and no line of hyphens below it.\n\nsteenrod_algebra_element.py, line 1518: change ``i`th` to ``i^{th}``\n\nsteenrod_algebra_element.py, line 1530: change ``k`th` to ``k^{th}``",
    "created_at": "2009-01-07T20:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37187",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_037188.json:
```json
{
    "body": "Attachment [trac_4902-2.patch](tarball://root/attachments/some-uuid/ticket4902/trac_4902-2.patch) by mhansen created at 2009-01-08 21:10:42",
    "created_at": "2009-01-08T21:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37188",
    "user": "mhansen"
}
```

Attachment [trac_4902-2.patch](tarball://root/attachments/some-uuid/ticket4902/trac_4902-2.patch) by mhansen created at 2009-01-08 21:10:42



---

archive/issue_comments_037189.json:
```json
{
    "body": "I've posted a patch which takes care of a number of the issues you noted.\n\nThe problem with \"def QuaternionAlgebra\" is internal to Sphinx.  I'll send a message to their mailing list.\n\nCurrently, the documentation for \"internal\" methods that start with \"_\" are not included in the reference manual by default.  In the future, I have some ideas for extending Sphinx's autodoc extension to be able to include things underscore methods without cluttering things up for users not interested in them.",
    "created_at": "2009-01-08T21:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37189",
    "user": "mhansen"
}
```

I've posted a patch which takes care of a number of the issues you noted.

The problem with "def QuaternionAlgebra" is internal to Sphinx.  I'll send a message to their mailing list.

Currently, the documentation for "internal" methods that start with "_" are not included in the reference manual by default.  In the future, I have some ideas for extending Sphinx's autodoc extension to be able to include things underscore methods without cluttering things up for users not interested in them.



---

archive/issue_comments_037190.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> I've posted a patch which takes care of a number of the issues you noted.\n\nGreat, I'll take a look soon.\n\n> Currently, the documentation for \"internal\" methods that start with \"_\" are not included in the reference manual by default.  In the future, I have some ideas for extending Sphinx's autodoc extension to be able to include things underscore methods without cluttering things up for users not interested in them.\n\nFrom Sage's point of view, various classes have a lot of documentation in the __init__ method, so unfortunately leaving them out means leaving out some important things.  Anyway...",
    "created_at": "2009-01-08T23:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37190",
    "user": "jhpalmieri"
}
```

Replying to [comment:3 mhansen]:
> I've posted a patch which takes care of a number of the issues you noted.

Great, I'll take a look soon.

> Currently, the documentation for "internal" methods that start with "_" are not included in the reference manual by default.  In the future, I have some ideas for extending Sphinx's autodoc extension to be able to include things underscore methods without cluttering things up for users not interested in them.

From Sage's point of view, various classes have a lot of documentation in the __init__ method, so unfortunately leaving them out means leaving out some important things.  Anyway...



---

archive/issue_comments_037191.json:
```json
{
    "body": "Looks good, positive review.  You also caught some things that I had missed, or maybe you were fixing typos in the original documentation.  Thanks.",
    "created_at": "2009-01-09T00:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37191",
    "user": "jhpalmieri"
}
```

Looks good, positive review.  You also caught some things that I had missed, or maybe you were fixing typos in the original documentation.  Thanks.



---

archive/issue_comments_037192.json:
```json
{
    "body": "Attachment [sage.algebras-final.patch](tarball://root/attachments/some-uuid/ticket4902/sage.algebras-final.patch) by mhansen created at 2009-02-21 19:14:47",
    "created_at": "2009-02-21T19:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37192",
    "user": "mhansen"
}
```

Attachment [sage.algebras-final.patch](tarball://root/attachments/some-uuid/ticket4902/sage.algebras-final.patch) by mhansen created at 2009-02-21 19:14:47



---

archive/issue_comments_037193.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37193",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_037194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4902#issuecomment-37194",
    "user": "mabshoff"
}
```

Resolution: fixed
