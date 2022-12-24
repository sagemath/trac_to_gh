# Issue 3055: creating subgraph does not delete _pos entries

archive/issues_003055.json:
```json
{
    "body": "Assignee: rlm\n\nThis means that later, a call to relabel fails.  This affects, for example, the graph isomorphism code (which was how the error was originally found).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3055\n\n",
    "created_at": "2008-04-29T20:42:56Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "creating subgraph does not delete _pos entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3055",
    "user": "jason"
}
```
Assignee: rlm

This means that later, a call to relabel fails.  This affects, for example, the graph isomorphism code (which was how the error was originally found).


Issue created by migration from https://trac.sagemath.org/ticket/3055





---

archive/issue_comments_021090.json:
```json
{
    "body": "Attachment [trac-3055-subgraph-del-pos.patch](tarball://root/attachments/some-uuid/ticket3055/trac-3055-subgraph-del-pos.patch) by jason created at 2008-04-29 21:09:18\n\nWith #3054 and #3055 applied, doctests pass in the graphs/ directory.",
    "created_at": "2008-04-29T21:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3055#issuecomment-21090",
    "user": "jason"
}
```

Attachment [trac-3055-subgraph-del-pos.patch](tarball://root/attachments/some-uuid/ticket3055/trac-3055-subgraph-del-pos.patch) by jason created at 2008-04-29 21:09:18

With #3054 and #3055 applied, doctests pass in the graphs/ directory.



---

archive/issue_comments_021091.json:
```json
{
    "body": "Have not run doctests, but I support this fix.",
    "created_at": "2008-04-29T21:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3055#issuecomment-21091",
    "user": "rlm"
}
```

Have not run doctests, but I support this fix.



---

archive/issue_comments_021092.json:
```json
{
    "body": "#3054 and #3055 applied to my current merge tree doctest clean. So I am considering this a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T02:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3055#issuecomment-21092",
    "user": "mabshoff"
}
```

#3054 and #3055 applied to my current merge tree doctest clean. So I am considering this a positive review.

Cheers,

Michael



---

archive/issue_comments_021093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-30T02:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3055#issuecomment-21093",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021094.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-30T02:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3055#issuecomment-21094",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_comments_021095.json:
```json
{
    "body": "Tracy McKay and Laura DeLoss should also get credit for exposing this bug.",
    "created_at": "2008-05-02T22:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3055#issuecomment-21095",
    "user": "jason"
}
```

Tracy McKay and Laura DeLoss should also get credit for exposing this bug.



---

archive/issue_comments_021096.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Tracy McKay and Laura DeLoss should also get credit for exposing this bug.\n\nWell, did they fix the bug? So far we only give credit for doing that. People who find bugs are not credited and while we could add a \"reported by FOO\" byline I am not sure those people will get added to the credit list.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T03:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3055#issuecomment-21096",
    "user": "mabshoff"
}
```

Replying to [comment:5 jason]:
> Tracy McKay and Laura DeLoss should also get credit for exposing this bug.

Well, did they fix the bug? So far we only give credit for doing that. People who find bugs are not credited and while we could add a "reported by FOO" byline I am not sure those people will get added to the credit list.

Cheers,

Michael
