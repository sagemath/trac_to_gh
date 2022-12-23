# Issue 2135: [with patch, needs easy review] allow for specifying initial position in spring layout

archive/issues_002135.json:
```json
{
    "body": "Assignee: rlm\n\nsuggested by Peter Jipsen (does he have a track account yet?)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2135\n\n",
    "created_at": "2008-02-10T01:06:42Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs easy review] allow for specifying initial position in spring layout",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2135",
    "user": "rlm"
}
```
Assignee: rlm

suggested by Peter Jipsen (does he have a track account yet?)

Issue created by migration from https://trac.sagemath.org/ticket/2135





---

archive/issue_comments_014004.json:
```json
{
    "body": "Attachment\n\nApply.  There are no doctests, but how would one doctest this?  There is a small typo in the docstring, I think -- a missing apostrophe.",
    "created_at": "2008-02-15T03:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-14004",
    "user": "ncalexan"
}
```

Attachment

Apply.  There are no doctests, but how would one doctest this?  There is a small typo in the docstring, I think -- a missing apostrophe.



---

archive/issue_comments_014005.json:
```json
{
    "body": "Actually, maybe one could test it by giving it a stable initial configuration, and then \"...\"-ing out most of the output.",
    "created_at": "2008-02-19T22:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-14005",
    "user": "rlm"
}
```

Actually, maybe one could test it by giving it a stable initial configuration, and then "..."-ing out most of the output.



---

archive/issue_comments_014006.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T01:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-14006",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014007.json:
```json
{
    "body": "Attachment\n\nMerged both patches in Sage 2.10.3.alpha0. I fixed the missing apostrophe in plot_positions_with_spring-graphs.patch.\n\nCheeers,\n\nMichael",
    "created_at": "2008-02-25T01:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-14007",
    "user": "mabshoff"
}
```

Attachment

Merged both patches in Sage 2.10.3.alpha0. I fixed the missing apostrophe in plot_positions_with_spring-graphs.patch.

Cheeers,

Michael
