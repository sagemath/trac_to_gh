# Issue 486: [with patch] number_of_partitions() could be faster.

archive/issues_000486.json:
```json
{
    "body": "Assignee: bober\n\nCC:  sage-combinat\n\nKeywords: partitions, number_of_partitions, partitions_c.cc\n\nThe implementation of `number_of_partitions()` in `partition_c.cc` should use `quaddoubles `and `doubledoubles`, and should also select the necessary precision more carefully.\n\nAlso, number_of_partitions() should have more tests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/486\n\n",
    "closed_at": "2007-10-13T07:47:59Z",
    "created_at": "2007-08-24T01:37:08Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "[with patch] number_of_partitions() could be faster.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/486",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```
Assignee: bober

CC:  sage-combinat

Keywords: partitions, number_of_partitions, partitions_c.cc

The implementation of `number_of_partitions()` in `partition_c.cc` should use `quaddoubles `and `doubledoubles`, and should also select the necessary precision more carefully.

Also, number_of_partitions() should have more tests.

Issue created by migration from https://trac.sagemath.org/ticket/486





---

archive/issue_comments_002415.json:
```json
{
    "body": "Attachment [5835-number_of_partitions-improvement.patch](tarball://root/attachments/some-uuid/ticket486/5835-number_of_partitions-improvement.patch) by bober created at 2007-08-29 15:56:05\n\nPatch for the improvements described in this ticket. Touches files setup.py, combinat.py, and partitions_c.cc",
    "created_at": "2007-08-29T15:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2415",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Attachment [5835-number_of_partitions-improvement.patch](tarball://root/attachments/some-uuid/ticket486/5835-number_of_partitions-improvement.patch) by bober created at 2007-08-29 15:56:05

Patch for the improvements described in this ticket. Touches files setup.py, combinat.py, and partitions_c.cc



---

archive/issue_comments_002416.json:
```json
{
    "body": "NOTE: The attached patch depends on the patch attached to ticket #468 being applied (or on that bug being fixed in some other way, of course).\n\nSome more notes on the attached file:\nMany changes were made to partitions_c.cc to do some code cleanup, templatize some code, attempt to make the use of long doubles behave nicely across different platforms, to use qd_real and dd_real types, and to select the precision much more carefully.\n\nThe changes to combinat.py are just some doctest additions.\n\nThe change to setup.py is just to link partitions_c.cc with the qd library when it builds. (I think that it adds 5 characters to setup.py.)\n\nSome timing results on a core duo T2400 (1.83 ghz):\n\nbefore patch:\n\n```\nsage: time a = number_of_partitions(100000000)\nCPU times: user 7.50 s, sys: 0.00 s, total: 7.50 s\nWall time: 7.50\nsage: time a = number_of_partitions(1000000000)\nCPU times: user 102.16 s, sys: 0.12 s, total: 102.28 s\nWall time: 102.94\n```\nafter patch:\n\n```\nsage: time a = number_of_partitions(100000000)\nCPU times: user 4.00 s, sys: 0.01 s, total: 4.01 s\nWall time: 4.11\nsage: time a = number_of_partitions(1000000000)\nCPU times: user 38.08 s, sys: 0.06 s, total: 38.14 s\nWall time: 39.24\n```",
    "created_at": "2007-08-29T16:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2416",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
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

archive/issue_events_001244.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/bober",
    "created_at": "2007-08-29T16:14:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/486#event-1244"
}
```



---

archive/issue_events_001245.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-10-12T23:16:05Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/486#event-1245"
}
```



---

archive/issue_events_001246.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-10-12T23:16:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/486#event-1246"
}
```



---

archive/issue_comments_002417.json:
```json
{
    "body": "bundle with both the patches for 468 and 486",
    "created_at": "2007-10-13T02:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2417",
    "user": "https://github.com/mwhansen"
}
```

bundle with both the patches for 468 and 486



---

archive/issue_comments_002418.json:
```json
{
    "body": "Attachment [partition_updates.hg](tarball://root/attachments/some-uuid/ticket486/partition_updates.hg) by @williamstein created at 2007-10-13 07:47:59",
    "created_at": "2007-10-13T07:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2418",
    "user": "https://github.com/williamstein"
}
```

Attachment [partition_updates.hg](tarball://root/attachments/some-uuid/ticket486/partition_updates.hg) by @williamstein created at 2007-10-13 07:47:59



---

archive/issue_events_001247.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T07:47:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/486#event-1247"
}
```



---

archive/issue_comments_002419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/486#issuecomment-2419",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
