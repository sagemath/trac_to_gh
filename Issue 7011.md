# Issue 7011: fiddle with the number of threads automatically used for parallel testing

archive/issues_007011.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu drkirkby @jhpalmieri\n\nAt #6283, we changed the parallel testing framework so that it automatically uses all the cores/threads available, but perhaps this is not the best solution.\n\nDave says ([comment:9:ticket:6283]) \"I would have personally not allowed the default to exceed 8\", so maybe we can incorporate his limit in a way that still lets ordinary multicore computers be well-used:\n\n* NUM_THREADS defaults to 0, which is now interpreted in the sage-ptest script as min(cpu_count(), 8) -- so the default doesn't exceed 8, as Dave suggested.\n* if NUM_THREADS is -1, it just uses cpu_count().\n\nOn sage-devel, I suggested that a solution that works really well for 99+% of people is a good one -- and since most \"regular\" machines on which Sage is doctested have 8 or fewer cores, this still works fine for them, and with the above suggestion, people won't bring sage.math or t2.math to their knees.\n\nThoughts?\n\nIssue created by migration from https://trac.sagemath.org/ticket/7011\n\n",
    "created_at": "2009-09-25T07:39:05Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "fiddle with the number of threads automatically used for parallel testing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7011",
    "user": "https://github.com/dandrake"
}
```
Assignee: tbd

CC:  mvngu drkirkby @jhpalmieri

At #6283, we changed the parallel testing framework so that it automatically uses all the cores/threads available, but perhaps this is not the best solution.

Dave says ([comment:9:ticket:6283]) "I would have personally not allowed the default to exceed 8", so maybe we can incorporate his limit in a way that still lets ordinary multicore computers be well-used:

* NUM_THREADS defaults to 0, which is now interpreted in the sage-ptest script as min(cpu_count(), 8) -- so the default doesn't exceed 8, as Dave suggested.
* if NUM_THREADS is -1, it just uses cpu_count().

On sage-devel, I suggested that a solution that works really well for 99+% of people is a good one -- and since most "regular" machines on which Sage is doctested have 8 or fewer cores, this still works fine for them, and with the above suggestion, people won't bring sage.math or t2.math to their knees.

Thoughts?

Issue created by migration from https://trac.sagemath.org/ticket/7011





---

archive/issue_comments_057859.json:
```json
{
    "body": "On second thought, scratch the -1 idea. We can just make one change to sage-ptest: line 267 could be\n\n```\nnumthreads = min(8, multiprocessing.cpu_count())\n```\n\nAnyone who is desperate to saturate a machine with more than 8 cores can just specify it on the command line.",
    "created_at": "2009-09-25T08:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57859",
    "user": "https://github.com/dandrake"
}
```

On second thought, scratch the -1 idea. We can just make one change to sage-ptest: line 267 could be

```
numthreads = min(8, multiprocessing.cpu_count())
```

Anyone who is desperate to saturate a machine with more than 8 cores can just specify it on the command line.



---

archive/issue_comments_057860.json:
```json
{
    "body": "add in default maximum of 8 threads",
    "created_at": "2009-09-29T08:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57860",
    "user": "https://github.com/dandrake"
}
```

add in default maximum of 8 threads



---

archive/issue_comments_057861.json:
```json
{
    "body": "Attachment [trac_7011.patch](tarball://root/attachments/some-uuid/ticket7011/trac_7011.patch) by @dandrake created at 2009-09-29 08:32:58\n\npatch for $SAGE_ROOT/makefile",
    "created_at": "2009-09-29T08:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57861",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_7011.patch](tarball://root/attachments/some-uuid/ticket7011/trac_7011.patch) by @dandrake created at 2009-09-29 08:32:58

patch for $SAGE_ROOT/makefile



---

archive/issue_comments_057862.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-29T08:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57862",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057863.json:
```json
{
    "body": "Changing assignee from tbd to @dandrake.",
    "created_at": "2009-09-29T08:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57863",
    "user": "https://github.com/dandrake"
}
```

Changing assignee from tbd to @dandrake.



---

archive/issue_comments_057864.json:
```json
{
    "body": "Attachment [trac_7011-sage-root-makefile.patch](tarball://root/attachments/some-uuid/ticket7011/trac_7011-sage-root-makefile.patch) by @dandrake created at 2009-09-29 08:36:53\n\nI've uploaded patches for the sage_scripts repo, and for the root makefile. The second attachment is an ordinary unified diff.",
    "created_at": "2009-09-29T08:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57864",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_7011-sage-root-makefile.patch](tarball://root/attachments/some-uuid/ticket7011/trac_7011-sage-root-makefile.patch) by @dandrake created at 2009-09-29 08:36:53

I've uploaded patches for the sage_scripts repo, and for the root makefile. The second attachment is an ordinary unified diff.



---

archive/issue_comments_057865.json:
```json
{
    "body": "Looks good to me. Very helpful comments, too.",
    "created_at": "2009-09-30T20:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57865",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me. Very helpful comments, too.



---

archive/issue_comments_057866.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-14T01:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57866",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_057867.json:
```json
{
    "body": "merged into sage-4.1.2",
    "created_at": "2009-10-14T01:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7011#issuecomment-57867",
    "user": "https://github.com/williamstein"
}
```

merged into sage-4.1.2
