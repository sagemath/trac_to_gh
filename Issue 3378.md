# Issue 3378: [with patch, needs review] graphs.nauty_geng fails due to missing imports

archive/issues_003378.json:
```json
{
    "body": "Assignee: rlm\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3378\n\n",
    "created_at": "2008-06-06T17:55:56Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] graphs.nauty_geng fails due to missing imports",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3378",
    "user": "mhansen"
}
```
Assignee: rlm



Issue created by migration from https://trac.sagemath.org/ticket/3378





---

archive/issue_comments_023651.json:
```json
{
    "body": "Attachment [3378.patch](tarball://root/attachments/some-uuid/ticket3378/3378.patch) by rlm created at 2008-06-07 15:12:49\n\nI suppose this didn't get caught by doctests because nauty is an optional package. Is it possible to have doctests that actually get run?\n\nAlso, in installing the optional nauty spkg, I notice that there is an interactive do-you-accept-this-license step. This doesn't seem right at all... Mabshoff, thoughts?",
    "created_at": "2008-06-07T15:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3378#issuecomment-23651",
    "user": "rlm"
}
```

Attachment [3378.patch](tarball://root/attachments/some-uuid/ticket3378/3378.patch) by rlm created at 2008-06-07 15:12:49

I suppose this didn't get caught by doctests because nauty is an optional package. Is it possible to have doctests that actually get run?

Also, in installing the optional nauty spkg, I notice that there is an interactive do-you-accept-this-license step. This doesn't seem right at all... Mabshoff, thoughts?



---

archive/issue_comments_023652.json:
```json
{
    "body": "Re the license: This is on purpose since it isn't GPL compatible and I think it is fine. It has been proposed to create a non-free repo and then stick all non-GPL compatible spkgs in there.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-08T22:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3378#issuecomment-23652",
    "user": "mabshoff"
}
```

Re the license: This is on purpose since it isn't GPL compatible and I think it is fine. It has been proposed to create a non-free repo and then stick all non-GPL compatible spkgs in there.

Cheers,

Michael



---

archive/issue_comments_023653.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-08T22:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3378#issuecomment-23653",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023654.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha2",
    "created_at": "2008-06-08T22:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3378#issuecomment-23654",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha2
