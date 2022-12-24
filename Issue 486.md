# Issue 486: number_of_partitions() could be faster.

archive/issues_000486.json:
```json
{
    "body": "Assignee: bober\n\nCC:  sage-combinat\n\nKeywords: partitions, number_of_partitions, partitions_c.cc\n\nThe implementation of `number_of_partitions()` in `partition_c.cc` should use `quaddoubles `and `doubledoubles`, and should also select the necessary precision more carefully.\n\nAlso, number_of_partitions() should have more tests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/486\n\n",
    "created_at": "2007-08-24T01:37:08Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "number_of_partitions() could be faster.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/486",
    "user": "bober"
}
```
Assignee: bober

CC:  sage-combinat

Keywords: partitions, number_of_partitions, partitions_c.cc

The implementation of `number_of_partitions()` in `partition_c.cc` should use `quaddoubles `and `doubledoubles`, and should also select the necessary precision more carefully.

Also, number_of_partitions() should have more tests.

Issue created by migration from https://trac.sagemath.org/ticket/486





---

archive/issue_comments_002425.json:
```json
{
    "body": "Attachment [5835-number_of_partitions-improvement.patch](tarball://root/attachments/some-uuid/ticket486/5835-number_of_partitions-improvement.patch) by bober created at 2007-08-29 15:56:05\n\nPatch for the improvements described in this ticket. Touches files setup.py, combinat.py, and partitions_c.cc",
    "created_at": "2007-08-29T15:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2425",
    "user": "bober"
}
```

Attachment [5835-number_of_partitions-improvement.patch](tarball://root/attachments/some-uuid/ticket486/5835-number_of_partitions-improvement.patch) by bober created at 2007-08-29 15:56:05

Patch for the improvements described in this ticket. Touches files setup.py, combinat.py, and partitions_c.cc



---

archive/issue_comments_002426.json:
```json
{
    "body": "NOTE: The attached patch depends on the patch attached to ticket #468 being applied (or on that bug being fixed in some other way, of course).\n\nSome more notes on the attached file:\nMany changes were made to partitions_c.cc to do some code cleanup, templatize some code, attempt to make the use of long doubles behave nicely across different platforms, to use qd_real and dd_real types, and to select the precision much more carefully.\n\nThe changes to combinat.py are just some doctest additions.\n\nThe change to setup.py is just to link partitions_c.cc with the qd library when it builds. (I think that it adds 5 characters to setup.py.)\n\nSome timing results on a core duo T2400 (1.83 ghz):\n\nbefore patch:\n\n```\nsage: time a = number_of_partitions(100000000)\nCPU times: user 7.50 s, sys: 0.00 s, total: 7.50 s\nWall time: 7.50\nsage: time a = number_of_partitions(1000000000)\nCPU times: user 102.16 s, sys: 0.12 s, total: 102.28 s\nWall time: 102.94\n```\n\nafter patch:\n\n```\nsage: time a = number_of_partitions(100000000)\nCPU times: user 4.00 s, sys: 0.01 s, total: 4.01 s\nWall time: 4.11\nsage: time a = number_of_partitions(1000000000)\nCPU times: user 38.08 s, sys: 0.06 s, total: 38.14 s\nWall time: 39.24\n```\n",
    "created_at": "2007-08-29T16:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2426",
    "user": "bober"
}
```

NOTE: The attached patch depends on the patch attached to ticket #468 being applied (or on that bug being fixed in some other way, of course).

Some more notes on the attached file:
Many changes were made to partitions_c.cc to do some code cleanup, templatize some code, attempt to make the use of long doubles behave nicely across different platforms, to use qd_real and dd_real types, and to select the precision much more carefully.

The changes to combinat.py are just some doctest additions.

The change to setup.py is just to link partitions_c.cc with the qd library when it builds. (I think that it adds 5 characters to setup.py.)

Some timing results on a core duo T2400 (1.83 ghz):

before patch:

```
sage: time a = number_of_partitions(100000000)
CPU times: user 7.50 s, sys: 0.00 s, total: 7.50 s
Wall time: 7.50
sage: time a = number_of_partitions(1000000000)
CPU times: user 102.16 s, sys: 0.12 s, total: 102.28 s
Wall time: 102.94
```

after patch:

```
sage: time a = number_of_partitions(100000000)
CPU times: user 4.00 s, sys: 0.01 s, total: 4.01 s
Wall time: 4.11
sage: time a = number_of_partitions(1000000000)
CPU times: user 38.08 s, sys: 0.06 s, total: 38.14 s
Wall time: 39.24
```




---

archive/issue_comments_002427.json:
```json
{
    "body": "bundle with both the patches for 468 and 486",
    "created_at": "2007-10-13T02:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2427",
    "user": "@mwhansen"
}
```

bundle with both the patches for 468 and 486



---

archive/issue_comments_002428.json:
```json
{
    "body": "Attachment [partition_updates.hg](tarball://root/attachments/some-uuid/ticket486/partition_updates.hg) by @williamstein created at 2007-10-13 07:47:59",
    "created_at": "2007-10-13T07:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2428",
    "user": "@williamstein"
}
```

Attachment [partition_updates.hg](tarball://root/attachments/some-uuid/ticket486/partition_updates.hg) by @williamstein created at 2007-10-13 07:47:59



---

archive/issue_comments_002429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2429",
    "user": "@williamstein"
}
```

Resolution: fixed
