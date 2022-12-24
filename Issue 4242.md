# Issue 4242: Bugfix for dominates() method of partition.py (with patch; needs review)

archive/issues_004242.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\np.dominates(q) would give the wrong answer (True) if q had more boxes than p, but the first (length of p) parts of q were dominated by p.  Attached patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4242\n\n",
    "created_at": "2008-10-04T14:06:47Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Bugfix for dominates() method of partition.py (with patch; needs review)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4242",
    "user": "jbandlow"
}
```
Assignee: mhansen

CC:  sage-combinat

p.dominates(q) would give the wrong answer (True) if q had more boxes than p, but the first (length of p) parts of q were dominated by p.  Attached patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/4242





---

archive/issue_comments_030832.json:
```json
{
    "body": "Attachment [4242.patch](tarball://root/attachments/some-uuid/ticket4242/4242.patch) by jbandlow created at 2008-10-04 14:07:50",
    "created_at": "2008-10-04T14:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30832",
    "user": "jbandlow"
}
```

Attachment [4242.patch](tarball://root/attachments/some-uuid/ticket4242/4242.patch) by jbandlow created at 2008-10-04 14:07:50



---

archive/issue_comments_030833.json:
```json
{
    "body": "Thanks Jason!  Looks good to me.",
    "created_at": "2008-10-04T14:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30833",
    "user": "mhansen"
}
```

Thanks Jason!  Looks good to me.



---

archive/issue_comments_030834.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-07T17:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30834",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030835.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-07T17:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30835",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha3



---

archive/issue_comments_030836.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-10-07T17:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30836",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_030837.json:
```json
{
    "body": "With the patch applied I get\n\n```\nsage -t  devel/sage/sage/combinat/partition.py              \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/partition.py\", line 604:\n    sage: Partition([]).dominates([1])\nExpected:\n    False\nGot:\n    True\n**********************************************************************\n```\n\n\nI assumed that at least the patched file would be doctested :(\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T17:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30837",
    "user": "mabshoff"
}
```

With the patch applied I get

```
sage -t  devel/sage/sage/combinat/partition.py              
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/partition.py", line 604:
    sage: Partition([]).dominates([1])
Expected:
    False
Got:
    True
**********************************************************************
```


I assumed that at least the patched file would be doctested :(

Cheers,

Michael



---

archive/issue_comments_030838.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-10-07T17:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30838",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_030839.json:
```json
{
    "body": "Attachment [trac_4242.patch](tarball://root/attachments/some-uuid/ticket4242/trac_4242.patch) by mabshoff created at 2008-10-12 19:46:34\n\nLooks good to me. Thanks Mike.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-12T19:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30839",
    "user": "mabshoff"
}
```

Attachment [trac_4242.patch](tarball://root/attachments/some-uuid/ticket4242/trac_4242.patch) by mabshoff created at 2008-10-12 19:46:34

Looks good to me. Thanks Mike.

Cheers,

Michael



---

archive/issue_comments_030840.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-12T19:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30840",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.rc0



---

archive/issue_comments_030841.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-12T19:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4242#issuecomment-30841",
    "user": "mabshoff"
}
```

Resolution: fixed
