# Issue 3341: fix minor issue with creating skew partitions by dividng partitions

archive/issues_003341.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n```\nsage: Partition([2,1])/Partition([1])\n/home/was/s/local/lib/python2.5/site-packages/sage/combinat/partition.py in __div__(self, p)\n    325             \n    326         \"\"\"\n--> 327         if not self.dominates(Partition_class(p)):\n    328             raise ValueError, \"the partition must dominate p\"\n    329 \n\n/home/was/s/local/lib/python2.5/site-packages/sage/combinat/combinat.py in __init__(self, l)\n    546         \"\"\"\n    547         if not isinstance(l, list):\n--> 548             raise ValueError, 'l must be a list'\n    549         self._list = l\n    550         self._hash = None\n\nValueError: l must be a list\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3341\n\n",
    "created_at": "2008-05-31T06:56:01Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "fix minor issue with creating skew partitions by dividng partitions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3341",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat


```
sage: Partition([2,1])/Partition([1])
/home/was/s/local/lib/python2.5/site-packages/sage/combinat/partition.py in __div__(self, p)
    325             
    326         """
--> 327         if not self.dominates(Partition_class(p)):
    328             raise ValueError, "the partition must dominate p"
    329 

/home/was/s/local/lib/python2.5/site-packages/sage/combinat/combinat.py in __init__(self, l)
    546         """
    547         if not isinstance(l, list):
--> 548             raise ValueError, 'l must be a list'
    549         self._list = l
    550         self._hash = None

ValueError: l must be a list
```




Issue created by migration from https://trac.sagemath.org/ticket/3341





---

archive/issue_comments_023151.json:
```json
{
    "body": "Attachment [3341.patch](tarball://root/attachments/some-uuid/ticket3341/3341.patch) by @mwhansen created at 2008-05-31 06:59:25",
    "created_at": "2008-05-31T06:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23151",
    "user": "https://github.com/mwhansen"
}
```

Attachment [3341.patch](tarball://root/attachments/some-uuid/ticket3341/3341.patch) by @mwhansen created at 2008-05-31 06:59:25



---

archive/issue_comments_023152.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-31T06:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23152",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023153.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-15T22:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23153",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_023154.json:
```json
{
    "body": "good work.",
    "created_at": "2008-06-19T20:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23154",
    "user": "https://github.com/malb"
}
```

good work.



---

archive/issue_comments_023155.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T07:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023156.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T07:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha0
