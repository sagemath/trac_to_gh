# Issue 4437: Sage 3.2.a2: numerical noise in sage/graphs/graph.py

archive/issues_004437.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn an x86:\n\n```\nsage -t  devel/sage/sage/graphs/graph.py                    **********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/graph.py\", line 5802:\n    sage: P.spectrum(laplacian=True)\nExpected:\n    [...e-16, 2.0, 2.0, 2.0, 2.0, 2.0, 5.0, 5.0, 5.0, 5.0]\nGot:\n    [4.89153937105e-17, 2.0, 2.0, 2.0, 2.0, 2.0, 5.0, 5.0, 5.0, 5.0]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4437\n\n",
    "created_at": "2008-11-04T13:53:58Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.a2: numerical noise in sage/graphs/graph.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4437",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On an x86:

```
sage -t  devel/sage/sage/graphs/graph.py                    **********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/graph.py", line 5802:
    sage: P.spectrum(laplacian=True)
Expected:
    [...e-16, 2.0, 2.0, 2.0, 2.0, 2.0, 5.0, 5.0, 5.0, 5.0]
Got:
    [4.89153937105e-17, 2.0, 2.0, 2.0, 2.0, 2.0, 5.0, 5.0, 5.0, 5.0]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4437





---

archive/issue_comments_032622.json:
```json
{
    "body": "Attachment [trac_4437.patch](tarball://root/attachments/some-uuid/ticket4437/trac_4437.patch) by mabshoff created at 2008-11-05 21:52:06",
    "created_at": "2008-11-05T21:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4437#issuecomment-32622",
    "user": "mabshoff"
}
```

Attachment [trac_4437.patch](tarball://root/attachments/some-uuid/ticket4437/trac_4437.patch) by mabshoff created at 2008-11-05 21:52:06



---

archive/issue_comments_032623.json:
```json
{
    "body": "I'm okay with this.",
    "created_at": "2008-11-05T22:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4437#issuecomment-32623",
    "user": "@mwhansen"
}
```

I'm okay with this.



---

archive/issue_comments_032624.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-05T23:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4437#issuecomment-32624",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032625.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-05T23:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4437#issuecomment-32625",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha3
