# Issue 3677: sage -t / sage -tp does not take into account the current directory

archive/issues_003677.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @mwhansen\n\nAt the end of testing when reporting the results, sage -t does not take into account the current directory.  It produces output like this:\n\n\n```\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/ambient_space.py\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py\n```\n\n\nwhen it should be giving output like \n\n\n```\n\tsage -t  ambient_space.py\n\tsage -t  root_lattice_realization.py\n\tsage -t  root_space.py\n\tsage -t  root_system.py\n\tsage -t  weight_space.py\n```\n\n\nif I am in $SAGE_ROOT/devel/sage-combinat/sage/combinat/root_system .\n\nIssue created by migration from https://trac.sagemath.org/ticket/3677\n\n",
    "created_at": "2008-07-19T01:48:02Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "sage -t / sage -tp does not take into account the current directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3677",
    "user": "@mwhansen"
}
```
Assignee: @garyfurnish

CC:  @mwhansen

At the end of testing when reporting the results, sage -t does not take into account the current directory.  It produces output like this:


```
	sage -t  devel/sage-combinat/sage/combinat/root_system/ambient_space.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py
```


when it should be giving output like 


```
	sage -t  ambient_space.py
	sage -t  root_lattice_realization.py
	sage -t  root_space.py
	sage -t  root_system.py
	sage -t  weight_space.py
```


if I am in $SAGE_ROOT/devel/sage-combinat/sage/combinat/root_system .

Issue created by migration from https://trac.sagemath.org/ticket/3677





---

archive/issue_comments_026038.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-11T15:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-26038",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026039.json:
```json
{
    "body": "Attachment [trac_3677_bin.patch](tarball://root/attachments/some-uuid/ticket3677/trac_3677_bin.patch) by @garyfurnish created at 2008-12-11 15:17:28\n\nThis fixes this issue for sage -tp but not for sage -t.",
    "created_at": "2008-12-11T15:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-26039",
    "user": "@garyfurnish"
}
```

Attachment [trac_3677_bin.patch](tarball://root/attachments/some-uuid/ticket3677/trac_3677_bin.patch) by @garyfurnish created at 2008-12-11 15:17:28

This fixes this issue for sage -tp but not for sage -t.



---

archive/issue_comments_026040.json:
```json
{
    "body": "Is it possible to get this reviewed for 3.2.2?",
    "created_at": "2008-12-14T01:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-26040",
    "user": "@garyfurnish"
}
```

Is it possible to get this reviewed for 3.2.2?



---

archive/issue_comments_026041.json:
```json
{
    "body": "The \"-t\" case of this has been split to #4790",
    "created_at": "2008-12-14T05:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-26041",
    "user": "@garyfurnish"
}
```

The "-t" case of this has been split to #4790



---

archive/issue_comments_026042.json:
```json
{
    "body": "Yep, this works Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T05:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-26042",
    "user": "mabshoff"
}
```

Yep, this works Positive review.

Cheers,

Michael



---

archive/issue_comments_026043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T05:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-26043",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026044.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T05:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3677#issuecomment-26044",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc0
