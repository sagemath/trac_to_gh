# Issue 2470: dsage docs in tutorial -- can't tex them

archive/issues_002470.json:
```json
{
    "body": "Assignee: yi\n\nI can't tex tut.tex unless the dsage section is commented out.  Also there is some \"to be written...\" section in there -- this is not appropriate for the tutorial, which is meant to be a very very polished documented. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2470\n\n",
    "created_at": "2008-03-11T07:59:09Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "dsage docs in tutorial -- can't tex them",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2470",
    "user": "was"
}
```
Assignee: yi

I can't tex tut.tex unless the dsage section is commented out.  Also there is some "to be written..." section in there -- this is not appropriate for the tutorial, which is meant to be a very very polished documented. 

Issue created by migration from https://trac.sagemath.org/ticket/2470





---

archive/issue_comments_016728.json:
```json
{
    "body": "Thanks for catching that. I will attempt to fix it and post a patch. Is David Joyner the right person to ask about TeX related questions pertaining to the tutorial? I remember that I had problems putting in indexes.",
    "created_at": "2008-03-11T20:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16728",
    "user": "yi"
}
```

Thanks for catching that. I will attempt to fix it and post a patch. Is David Joyner the right person to ask about TeX related questions pertaining to the tutorial? I remember that I had problems putting in indexes.



---

archive/issue_comments_016729.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-11T20:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16729",
    "user": "yi"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016730.json:
```json
{
    "body": "Attachment [tut.patch](tarball://root/attachments/some-uuid/ticket2470/tut.patch) by yi created at 2008-03-22 00:00:22",
    "created_at": "2008-03-22T00:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16730",
    "user": "yi"
}
```

Attachment [tut.patch](tarball://root/attachments/some-uuid/ticket2470/tut.patch) by yi created at 2008-03-22 00:00:22



---

archive/issue_comments_016731.json:
```json
{
    "body": "Patch looks good to me. Constructs like ``foo'` will likely cause trouble while TeXing, but we can deal with that once we get closer to release. Yi, feel free to post a followup patch to resolve those issues and I will merge it.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-24T16:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16731",
    "user": "mabshoff"
}
```

Patch looks good to me. Constructs like ``foo'` will likely cause trouble while TeXing, but we can deal with that once we get closer to release. Yi, feel free to post a followup patch to resolve those issues and I will merge it.

Cheers,

Michael



---

archive/issue_comments_016732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-24T16:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16732",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016733.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-24T16:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16733",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2
