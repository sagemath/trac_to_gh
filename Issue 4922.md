# Issue 4922: convert sage.monoids.* docstrings to Sphinx

archive/issues_004922.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4922\n\n",
    "created_at": "2009-01-01T22:54:39Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.monoids.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4922",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4922





---

archive/issue_comments_037353.json:
```json
{
    "body": "Attachment [trac_4922.patch](tarball://root/attachments/some-uuid/ticket4922/trac_4922.patch) by mhansen created at 2009-01-02 02:20:14",
    "created_at": "2009-01-02T02:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4922#issuecomment-37353",
    "user": "mhansen"
}
```

Attachment [trac_4922.patch](tarball://root/attachments/some-uuid/ticket4922/trac_4922.patch) by mhansen created at 2009-01-02 02:20:14



---

archive/issue_comments_037354.json:
```json
{
    "body": "Looks good.  One tiny change: \n\nsage/monoids/free_monoid.py, line 156: change ``i`th` to ``i`-th`.\n\n(This is in a function whose name starts with double underscores, so it isn't even in the reference manual.  Just in case we add such things to the reference manual eventually, though...)\n\nAfter this change, positive review.",
    "created_at": "2009-02-09T21:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4922#issuecomment-37354",
    "user": "jhpalmieri"
}
```

Looks good.  One tiny change: 

sage/monoids/free_monoid.py, line 156: change ``i`th` to ``i`-th`.

(This is in a function whose name starts with double underscores, so it isn't even in the reference manual.  Just in case we add such things to the reference manual eventually, though...)

After this change, positive review.



---

archive/issue_comments_037355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4922#issuecomment-37355",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037356.json:
```json
{
    "body": "Attachment [sage.monoids-final.patch](tarball://root/attachments/some-uuid/ticket4922/sage.monoids-final.patch) by mabshoff created at 2009-02-24 18:45:38\n\nMerged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4922#issuecomment-37356",
    "user": "mabshoff"
}
```

Attachment [sage.monoids-final.patch](tarball://root/attachments/some-uuid/ticket4922/sage.monoids-final.patch) by mabshoff created at 2009-02-24 18:45:38

Merged in Sage 3.4.alpha0.

Cheers,

Michael
