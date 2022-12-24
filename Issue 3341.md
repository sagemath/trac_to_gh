# Issue 3341: fix minor issue with creating skew partitions by dividng partitions

archive/issues_003341.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n\n```\nsage: Partition([2,1])/Partition([1])\n/home/was/s/local/lib/python2.5/site-packages/sage/combinat/partition.py in __div__(self, p)\n    325             \n    326         \"\"\"\n--> 327         if not self.dominates(Partition_class(p)):\n    328             raise ValueError, \"the partition must dominate p\"\n    329 \n\n/home/was/s/local/lib/python2.5/site-packages/sage/combinat/combinat.py in __init__(self, l)\n    546         \"\"\"\n    547         if not isinstance(l, list):\n--> 548             raise ValueError, 'l must be a list'\n    549         self._list = l\n    550         self._hash = None\n\nValueError: l must be a list\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3341\n\n",
    "created_at": "2008-05-31T06:56:01Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "fix minor issue with creating skew partitions by dividng partitions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3341",
    "user": "mhansen"
}
```
Assignee: mhansen

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

archive/issue_comments_023199.json:
```json
{
    "body": "Attachment [3341.patch](tarball://root/attachments/some-uuid/ticket3341/3341.patch) by mhansen created at 2008-05-31 06:59:25",
    "created_at": "2008-05-31T06:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23199",
    "user": "mhansen"
}
```

Attachment [3341.patch](tarball://root/attachments/some-uuid/ticket3341/3341.patch) by mhansen created at 2008-05-31 06:59:25



---

archive/issue_comments_023200.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-31T06:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23200",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023201.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-15T22:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23201",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_023202.json:
```json
{
    "body": "good work.",
    "created_at": "2008-06-19T20:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23202",
    "user": "malb"
}
```

good work.



---

archive/issue_comments_023203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T07:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23203",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023204.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T07:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3341#issuecomment-23204",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha0
