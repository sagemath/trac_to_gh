# Issue 7080: include new separated sage notebook in Sage

archive/issues_007080.json:
```json
{
    "body": "Assignee: boothby\n\nFirst we will just include this in a way that still technically allows one to use the old notebook.  In a future version of sage we'll remove support for the old version of the notebook.  \n\nNote that the new notebook spkg includes jmol and jquery in it's sagenb/data directory (it's distutils package data).   But we'll do things in two phases:\n\n  (1) include new notebook, but leave all the old stuff there, which is redundant but safe,\n\n  (2) delete old stuff in a future version of sage\n\nThis ticket has an spkg and a patch to the core Sage library (to change the notebook(...) command).\n\n* http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.2.spkg\n\n* the patches are attached as patches. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7080\n\n",
    "created_at": "2009-09-30T08:44:26Z",
    "labels": [
        "component: notebook",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "include new separated sage notebook in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7080",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

First we will just include this in a way that still technically allows one to use the old notebook.  In a future version of sage we'll remove support for the old version of the notebook.  

Note that the new notebook spkg includes jmol and jquery in it's sagenb/data directory (it's distutils package data).   But we'll do things in two phases:

  (1) include new notebook, but leave all the old stuff there, which is redundant but safe,

  (2) delete old stuff in a future version of sage

This ticket has an spkg and a patch to the core Sage library (to change the notebook(...) command).

* http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.2.spkg

* the patches are attached as patches. 



Issue created by migration from https://trac.sagemath.org/ticket/7080





---

archive/issue_comments_058430.json:
```json
{
    "body": "Attachment [trac_7080.patch](tarball://root/attachments/some-uuid/ticket7080/trac_7080.patch) by @williamstein created at 2009-09-30 09:21:47",
    "created_at": "2009-09-30T09:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7080#issuecomment-58430",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7080.patch](tarball://root/attachments/some-uuid/ticket7080/trac_7080.patch) by @williamstein created at 2009-09-30 09:21:47



---

archive/issue_comments_058431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-14T16:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7080#issuecomment-58431",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_007302.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-14T16:11:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7080",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7080#event-7302"
}
```
