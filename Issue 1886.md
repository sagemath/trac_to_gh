# Issue 1886: [with patch - actually tuning tarball] add atlas pretuning for AMD Athlon MP processors

archive/issues_001886.json:
```json
{
    "body": "Assignee: @williamstein\n\nSo that building ATLAS on AMD Athlon doesn't take FIVE HOURS, I've recorded the tuning information and attached it to this ticket. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1886\n\n",
    "created_at": "2008-01-22T04:45:44Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch - actually tuning tarball] add atlas pretuning for AMD Athlon MP processors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1886",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

So that building ATLAS on AMD Athlon doesn't take FIVE HOURS, I've recorded the tuning information and attached it to this ticket. 

Issue created by migration from https://trac.sagemath.org/ticket/1886





---

archive/issue_comments_011917.json:
```json
{
    "body": "Attachment [K732SSE1.tgz](tarball://root/attachments/some-uuid/ticket1886/K732SSE1.tgz) by @williamstein created at 2008-01-22 04:48:14\n\nI followed the directions here:\n   http://math-atlas.sourceforge.net/devel/atlas_devel/atlas_devel.html#SECTION00070000000000000000\n\nIn particular, I did:\n\n```\n   1. sage -f -m atlas-3.8.p7\n   2. cd spkg/build/atlas-3.8.p7\n   3. cd ATLAS-build/ARCHS\n   4. make ArchNew\n   5. make tarfile\n```\n",
    "created_at": "2008-01-22T04:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1886#issuecomment-11917",
    "user": "https://github.com/williamstein"
}
```

Attachment [K732SSE1.tgz](tarball://root/attachments/some-uuid/ticket1886/K732SSE1.tgz) by @williamstein created at 2008-01-22 04:48:14

I followed the directions here:
   http://math-atlas.sourceforge.net/devel/atlas_devel/atlas_devel.html#SECTION00070000000000000000

In particular, I did:

```
   1. sage -f -m atlas-3.8.p7
   2. cd spkg/build/atlas-3.8.p7
   3. cd ATLAS-build/ARCHS
   4. make ArchNew
   5. make tarfile
```




---

archive/issue_comments_011918.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-02-02T09:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1886#issuecomment-11918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_011919.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-02T09:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1886#issuecomment-11919",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011920.json:
```json
{
    "body": "Look at #1547 for an spkg with the tuning information added.",
    "created_at": "2008-02-02T09:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1886#issuecomment-11920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Look at #1547 for an spkg with the tuning information added.



---

archive/issue_comments_011921.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T09:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1886#issuecomment-11921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc5



---

archive/issue_comments_011922.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T09:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1886#issuecomment-11922",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002044.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-02T09:58:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1886",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1886#event-2044"
}
```
