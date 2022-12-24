# Issue 2479: RDF polynomial factoring bug

archive/issues_002479.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: x = polygen(RDF,'x')\nsage: (-2*x^2 - 1).factor()\n[]\n```\n\n\ndegree 4?\n\nIssue created by migration from https://trac.sagemath.org/ticket/2479\n\n",
    "created_at": "2008-03-12T00:49:24Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "RDF polynomial factoring bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2479",
    "user": "@williamstein"
}
```
Assignee: somebody


```
sage: x = polygen(RDF,'x')
sage: (-2*x^2 - 1).factor()
[]
```


degree 4?

Issue created by migration from https://trac.sagemath.org/ticket/2479





---

archive/issue_comments_016799.json:
```json
{
    "body": "Attachment [sage-2479.patch](tarball://root/attachments/some-uuid/ticket2479/sage-2479.patch) by @williamstein created at 2008-03-12 00:55:17\n\nAttached patch fixes this problem.",
    "created_at": "2008-03-12T00:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2479#issuecomment-16799",
    "user": "@williamstein"
}
```

Attachment [sage-2479.patch](tarball://root/attachments/some-uuid/ticket2479/sage-2479.patch) by @williamstein created at 2008-03-12 00:55:17

Attached patch fixes this problem.



---

archive/issue_comments_016800.json:
```json
{
    "body": "Yep, looks good. \n\nI'm giving this a positive review, even though I had trouble applying this patch on my home machine. I think something got screwed up with my home machine's install, because it was an upgrade from 2.10.1 to 2.10.2 to 2.10.3. I tested, and the patch applies just fine against the copy of 2.10.3.rc1 I have on sage.math, so I'm pretty sure this is a local problem with my setup. Maybe it's an issue with upgrades from 2.10.2 to 2.10.3? In any event, it shouldn't be a problem for whoever is rolling 2.10.3.1 or whatnot.",
    "created_at": "2008-03-12T01:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2479#issuecomment-16800",
    "user": "@craigcitro"
}
```

Yep, looks good. 

I'm giving this a positive review, even though I had trouble applying this patch on my home machine. I think something got screwed up with my home machine's install, because it was an upgrade from 2.10.1 to 2.10.2 to 2.10.3. I tested, and the patch applies just fine against the copy of 2.10.3.rc1 I have on sage.math, so I'm pretty sure this is a local problem with my setup. Maybe it's an issue with upgrades from 2.10.2 to 2.10.3? In any event, it shouldn't be a problem for whoever is rolling 2.10.3.1 or whatnot.



---

archive/issue_comments_016801.json:
```json
{
    "body": "Actually, I take it back. I think that the version that William made this patch against isn't 2.10.3, because the same hunk that failed for me will fail on sage.math and another upgrade that just finished for me. I'm going to submit a second patch in about 30 seconds; one of the two should work.",
    "created_at": "2008-03-12T01:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2479#issuecomment-16801",
    "user": "@craigcitro"
}
```

Actually, I take it back. I think that the version that William made this patch against isn't 2.10.3, because the same hunk that failed for me will fail on sage.math and another upgrade that just finished for me. I'm going to submit a second patch in about 30 seconds; one of the two should work.



---

archive/issue_comments_016802.json:
```json
{
    "body": "Ok, re-based the patch. The name on the commit should get changed to William, since it's really his patch.",
    "created_at": "2008-03-12T01:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2479#issuecomment-16802",
    "user": "@craigcitro"
}
```

Ok, re-based the patch. The name on the commit should get changed to William, since it's really his patch.



---

archive/issue_comments_016803.json:
```json
{
    "body": "Attachment [trac-2479-v2.patch](tarball://root/attachments/some-uuid/ticket2479/trac-2479-v2.patch) by @craigcitro created at 2008-03-12 01:51:46\n\nsame patch as above, but applies clean against 2.10.3",
    "created_at": "2008-03-12T01:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2479#issuecomment-16803",
    "user": "@craigcitro"
}
```

Attachment [trac-2479-v2.patch](tarball://root/attachments/some-uuid/ticket2479/trac-2479-v2.patch) by @craigcitro created at 2008-03-12 01:51:46

same patch as above, but applies clean against 2.10.3



---

archive/issue_comments_016804.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-12T19:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2479#issuecomment-16804",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016805.json:
```json
{
    "body": "Merged trac-2479-v2.patch in Sage 2.10.4.alpha0",
    "created_at": "2008-03-12T19:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2479#issuecomment-16805",
    "user": "mabshoff"
}
```

Merged trac-2479-v2.patch in Sage 2.10.4.alpha0
