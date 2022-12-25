# Issue 2050: disallow *generic* matrix eigenspaces for inexact fields (very easy to implement)

archive/issues_002050.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  ncalexander@gmail.com\n\nInstead of lying the following code should just raise a NotImplementedError.  Basically use the `is_exact()` method on rings to determine if the ring is not exact, and if so, raise an error on eigenspaces computation.  Some generic algorithms suck for inexact rings.   One thing, the error message for RR and CC could suggest using RDF or CDF... and maybe when prec <= 53, the code could use RDF or CDF (?). \n\n\n```\nsage: R=RealField(30)\nsage: M=matrix(R,2,[2,1,1,1])\nsage: M.eigenspaces()\n\n[\n(2.6180340, [\n\n]),\n(0.38196601, [\n\n])\n]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2050\n\n",
    "created_at": "2008-02-05T05:00:28Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "disallow *generic* matrix eigenspaces for inexact fields (very easy to implement)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2050",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  ncalexander@gmail.com

Instead of lying the following code should just raise a NotImplementedError.  Basically use the `is_exact()` method on rings to determine if the ring is not exact, and if so, raise an error on eigenspaces computation.  Some generic algorithms suck for inexact rings.   One thing, the error message for RR and CC could suggest using RDF or CDF... and maybe when prec <= 53, the code could use RDF or CDF (?). 


```
sage: R=RealField(30)
sage: M=matrix(R,2,[2,1,1,1])
sage: M.eigenspaces()

[
(2.6180340, [

]),
(0.38196601, [

])
]
```


Issue created by migration from https://trac.sagemath.org/ticket/2050





---

archive/issue_comments_013244.json:
```json
{
    "body": "See #1706 for a related ticket.",
    "created_at": "2008-02-05T05:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2050#issuecomment-13244",
    "user": "https://github.com/williamstein"
}
```

See #1706 for a related ticket.



---

archive/issue_comments_013245.json:
```json
{
    "body": "Attachment [2050-ncalexan-eigenspaces-1.patch](tarball://root/attachments/some-uuid/ticket2050/2050-ncalexan-eigenspaces-1.patch) by @ncalexan created at 2008-02-17 00:45:53",
    "created_at": "2008-02-17T00:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2050#issuecomment-13245",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2050-ncalexan-eigenspaces-1.patch](tarball://root/attachments/some-uuid/ticket2050/2050-ncalexan-eigenspaces-1.patch) by @ncalexan created at 2008-02-17 00:45:53



---

archive/issue_comments_013246.json:
```json
{
    "body": "I get the following against 2.10.3.alpha0:\n\n\n```\ncd \"/home/mhansen/sage-2.10.3.alpha0/devel/sage\" && hg status\ncd \"/home/mhansen/sage-2.10.3.alpha0/devel/sage\" && hg status\ncd \"/home/mhansen/sage-2.10.3.alpha0/devel/sage\" && hg import   \"/home/mhansen/.sage/temp/sage/15288/tmp_0.patch\"\napplying /home/mhansen/.sage/temp/sage/15288/tmp_0.patch\npatching file sage/matrix/matrix2.pyx\nHunk #4 succeeded at 2130 with fuzz 2 (offset 0 lines).\nHunk #5 FAILED at 2146\nHunk #6 FAILED at 2163\n2 out of 7 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-02-27T18:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2050#issuecomment-13246",
    "user": "https://github.com/mwhansen"
}
```

I get the following against 2.10.3.alpha0:


```
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg import   "/home/mhansen/.sage/temp/sage/15288/tmp_0.patch"
applying /home/mhansen/.sage/temp/sage/15288/tmp_0.patch
patching file sage/matrix/matrix2.pyx
Hunk #4 succeeded at 2130 with fuzz 2 (offset 0 lines).
Hunk #5 FAILED at 2146
Hunk #6 FAILED at 2163
2 out of 7 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_013247.json:
```json
{
    "body": "Attachment [2050.patch](tarball://root/attachments/some-uuid/ticket2050/2050.patch) by @mwhansen created at 2008-02-27 22:57:55",
    "created_at": "2008-02-27T22:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2050#issuecomment-13247",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2050.patch](tarball://root/attachments/some-uuid/ticket2050/2050.patch) by @mwhansen created at 2008-02-27 22:57:55



---

archive/issue_comments_013248.json:
```json
{
    "body": "I've made a patch 2050 which applies cleanly after #2299 .  All tests pass so things look good to me.",
    "created_at": "2008-02-27T22:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2050#issuecomment-13248",
    "user": "https://github.com/mwhansen"
}
```

I've made a patch 2050 which applies cleanly after #2299 .  All tests pass so things look good to me.



---

archive/issue_comments_013249.json:
```json
{
    "body": "Merged 2050.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2050#issuecomment-13249",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2050.patch in Sage 2.10.3.rc0



---

archive/issue_events_004932.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-28T00:57:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2050#event-4932"
}
```



---

archive/issue_comments_013250.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2050#issuecomment-13250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
