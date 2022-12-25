# Issue 9122: conversions between simplicial and cubical complexes

archive/issues_009122.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  mhampton\n\nThis patch implements conversions between simplicial and cubical complexes.  It also implements the following: if you call\n\n```\nsage: SimplicialComplex(X)\n```\n\nit tests to see if X has a `_simplicial_` method, and if it does, it calls that and returns the answer.  So if anyone wants to convert their favorite Sage object to a simplicial complex, they just have to write a `_simplicial_` method for it; then `SimplicialComplex(blah)` will work.  Same for a `_cubical_` method and cubical complexes.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9122\n\n",
    "created_at": "2010-06-03T04:08:25Z",
    "labels": [
        "component: algebraic topology",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "conversions between simplicial and cubical complexes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9122",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  mhampton

This patch implements conversions between simplicial and cubical complexes.  It also implements the following: if you call

```
sage: SimplicialComplex(X)
```

it tests to see if X has a `_simplicial_` method, and if it does, it calls that and returns the answer.  So if anyone wants to convert their favorite Sage object to a simplicial complex, they just have to write a `_simplicial_` method for it; then `SimplicialComplex(blah)` will work.  Same for a `_cubical_` method and cubical complexes.


Issue created by migration from https://trac.sagemath.org/ticket/9122





---

archive/issue_comments_084705.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T04:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84705",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084706.json:
```json
{
    "body": "Maybe I am building the docs incorrectly, but it seems kind of sad that the documentation for _simplicial_ and _cubical_ does not show up in the reference manual, and if you look at it in the notebook it is not currently rendered correctly.\n\nOtherwise the functionality appears to be correctly implemented (although I have very little expertise in this area).  The flaws in rendering are probably the fault of the notebook code rather than this patch.",
    "created_at": "2011-03-29T03:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Maybe I am building the docs incorrectly, but it seems kind of sad that the documentation for _simplicial_ and _cubical_ does not show up in the reference manual, and if you look at it in the notebook it is not currently rendered correctly.

Otherwise the functionality appears to be correctly implemented (although I have very little expertise in this area).  The flaws in rendering are probably the fault of the notebook code rather than this patch.



---

archive/issue_comments_084707.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-03-29T03:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_084708.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-03-29T03:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84708",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_084709.json:
```json
{
    "body": "Oh, I think it's partly the fault of the patch: the docstrings should start with `r\"\"\"`, not just `\"\"\"`.  Try this new patch.",
    "created_at": "2011-03-29T03:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84709",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, I think it's partly the fault of the patch: the docstrings should start with `r"""`, not just `"""`.  Try this new patch.



---

archive/issue_comments_084710.json:
```json
{
    "body": "Attachment [trac_9122-cubical-simplicial.patch](tarball://root/attachments/some-uuid/ticket9122/trac_9122-cubical-simplicial.patch) by @jhpalmieri created at 2011-03-29 03:56:45",
    "created_at": "2011-03-29T03:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84710",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9122-cubical-simplicial.patch](tarball://root/attachments/some-uuid/ticket9122/trac_9122-cubical-simplicial.patch) by @jhpalmieri created at 2011-03-29 03:56:45



---

archive/issue_comments_084711.json:
```json
{
    "body": "All homology tests passed and the documentation looks fixed, so I think this is OK now.",
    "created_at": "2011-04-27T21:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84711",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

All homology tests passed and the documentation looks fixed, so I think this is OK now.



---

archive/issue_comments_084712.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-27T21:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022391.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-29T13:25:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9122#event-22391"
}
```



---

archive/issue_events_022392.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-07T08:34:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9122#event-22392"
}
```



---

archive/issue_comments_084713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-07T08:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9122#issuecomment-84713",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
