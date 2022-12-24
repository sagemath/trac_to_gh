# Issue 6112: Remove stale file sage/graphs/graph_isom.pyx

archive/issues_006112.json:
```json
{
    "body": "Assignee: rlm\n\nThis file has been superseded by those in `sage/groups/perm_gps/partn_ref`. I think its time has come.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6112\n\n",
    "created_at": "2009-05-21T15:03:48Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Remove stale file sage/graphs/graph_isom.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6112",
    "user": "rlm"
}
```
Assignee: rlm

This file has been superseded by those in `sage/groups/perm_gps/partn_ref`. I think its time has come.

Issue created by migration from https://trac.sagemath.org/ticket/6112





---

archive/issue_comments_048832.json:
```json
{
    "body": "Attachment [trac_6112.patch](tarball://root/attachments/some-uuid/ticket6112/trac_6112.patch) by ddrake created at 2009-06-16 02:23:37",
    "created_at": "2009-06-16T02:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48832",
    "user": "ddrake"
}
```

Attachment [trac_6112.patch](tarball://root/attachments/some-uuid/ticket6112/trac_6112.patch) by ddrake created at 2009-06-16 02:23:37



---

archive/issue_comments_048833.json:
```json
{
    "body": "Changing assignee from rlm to ddrake.",
    "created_at": "2009-06-16T02:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48833",
    "user": "ddrake"
}
```

Changing assignee from rlm to ddrake.



---

archive/issue_comments_048834.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-16T02:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48834",
    "user": "ddrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048835.json:
```json
{
    "body": "I don't know much about the graphs code, but I definitely can produce a patch which deletes a file. rlm, can you review?",
    "created_at": "2009-06-16T02:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48835",
    "user": "ddrake"
}
```

I don't know much about the graphs code, but I definitely can produce a patch which deletes a file. rlm, can you review?



---

archive/issue_comments_048836.json:
```json
{
    "body": "Wait, that was stupid...you can't just remove a file and expect things that use that file to figure out what to do...! Needs work.",
    "created_at": "2009-06-16T02:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48836",
    "user": "ddrake"
}
```

Wait, that was stupid...you can't just remove a file and expect things that use that file to figure out what to do...! Needs work.



---

archive/issue_comments_048837.json:
```json
{
    "body": "I'll take care of this -- I'm currently in the middle of overhauling graphs, and this is on my list.",
    "created_at": "2009-06-16T04:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48837",
    "user": "rlm"
}
```

I'll take care of this -- I'm currently in the middle of overhauling graphs, and this is on my list.



---

archive/issue_comments_048838.json:
```json
{
    "body": "Attachment [trac_6112-module_list.py](tarball://root/attachments/some-uuid/ticket6112/trac_6112-module_list.py) by rlm created at 2009-06-21 22:05:27",
    "created_at": "2009-06-21T22:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48838",
    "user": "rlm"
}
```

Attachment [trac_6112-module_list.py](tarball://root/attachments/some-uuid/ticket6112/trac_6112-module_list.py) by rlm created at 2009-06-21 22:05:27



---

archive/issue_comments_048839.json:
```json
{
    "body": "After deleting `graph_isom.so` and testing all of sage with `-long`, all is well.\n\nThe last test will be to actually roll an alpha and make sure everything still works, although I'm guessing all should be fine.",
    "created_at": "2009-06-21T22:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48839",
    "user": "rlm"
}
```

After deleting `graph_isom.so` and testing all of sage with `-long`, all is well.

The last test will be to actually roll an alpha and make sure everything still works, although I'm guessing all should be fine.



---

archive/issue_comments_048840.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6112#issuecomment-48840",
    "user": "rlm"
}
```

Resolution: fixed
