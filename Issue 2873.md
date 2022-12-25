# Issue 2873: [with patch and spkg, positive review] Customize JMOL menu

archive/issues_002873.json:
```json
{
    "body": "Assignee: @jasongrout\n\nIt would be nice to shorten the menu quite a bit and pick the options that make sense to us.\n\nSee http://chemapps.stolaf.edu/jmol/docs/examples-11/new4.htm point 13 for how to do this.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2873\n\n",
    "closed_at": "2009-02-14T14:51:03Z",
    "created_at": "2008-04-10T22:42:45Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch and spkg, positive review] Customize JMOL menu",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2873",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @jasongrout

It would be nice to shorten the menu quite a bit and pick the options that make sense to us.

See http://chemapps.stolaf.edu/jmol/docs/examples-11/new4.htm point 13 for how to do this.



Issue created by migration from https://trac.sagemath.org/ticket/2873





---

archive/issue_comments_019692.json:
```json
{
    "body": "See also the very nice writeup at http://wiki.jmol.org:81/index.php/Custom_Menus",
    "created_at": "2009-02-13T21:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19692",
    "user": "https://github.com/jasongrout"
}
```

See also the very nice writeup at http://wiki.jmol.org:81/index.php/Custom_Menus



---

archive/issue_comments_019693.json:
```json
{
    "body": "Whoever fixes this, please make sure that #1777 is taken care of (which can be fixed by this ticket, I believe).",
    "created_at": "2009-02-13T21:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19693",
    "user": "https://github.com/jasongrout"
}
```

Whoever fixes this, please make sure that #1777 is taken care of (which can be fixed by this ticket, I believe).



---

archive/issue_comments_019694.json:
```json
{
    "body": "Attachment [jmol-custom-menu.patch](tarball://root/attachments/some-uuid/ticket2873/jmol-custom-menu.patch) by @jasongrout created at 2009-02-14 09:48:17",
    "created_at": "2009-02-14T09:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19694",
    "user": "https://github.com/jasongrout"
}
```

Attachment [jmol-custom-menu.patch](tarball://root/attachments/some-uuid/ticket2873/jmol-custom-menu.patch) by @jasongrout created at 2009-02-14 09:48:17



---

archive/issue_comments_019695.json:
```json
{
    "body": "We need both a patch and a new spkg (which contains the custom menu file).  The spkg is up at http://sage.math.washington.edu/home/jason/jmol-11.6.16.spkg (I took the opportunity to update to the latest jmol stable version).",
    "created_at": "2009-02-14T09:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19695",
    "user": "https://github.com/jasongrout"
}
```

We need both a patch and a new spkg (which contains the custom menu file).  The spkg is up at http://sage.math.washington.edu/home/jason/jmol-11.6.16.spkg (I took the opportunity to update to the latest jmol stable version).



---

archive/issue_comments_019696.json:
```json
{
    "body": "This patch and spkg take care of #1777 too.",
    "created_at": "2009-02-14T10:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19696",
    "user": "https://github.com/jasongrout"
}
```

This patch and spkg take care of #1777 too.



---

archive/issue_comments_019697.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-02-14T10:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19697",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_019698.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T10:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19698",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_events_006567.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-14T13:57:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2873#event-6567"
}
```



---

archive/issue_comments_019699.json:
```json
{
    "body": "The spkg is **not** based in the latest jmol.spkg in tree and is missing fixes to spkg-install. Bad Jason :)\n\nTimothy: **always** check the repo and verify that it is based on the previous spkg.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T13:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19699",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg is **not** based in the latest jmol.spkg in tree and is missing fixes to spkg-install. Bad Jason :)

Timothy: **always** check the repo and verify that it is based on the previous spkg.

Cheers,

Michael



---

archive/issue_comments_019700.json:
```json
{
    "body": "I will put up a new jmol spkg at #5271.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T14:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19700",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will put up a new jmol spkg at #5271.

Cheers,

Michael



---

archive/issue_comments_019701.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T14:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19701",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006568.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-14T14:51:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2873#event-6568"
}
```



---

archive/issue_comments_019702.json:
```json
{
    "body": "Merged jmol-custom-menu.patch in Sage 3.3.rc1. \n\nNote that the spkg above was **not** merged, but the one at #5271.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T14:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19702",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged jmol-custom-menu.patch in Sage 3.3.rc1. 

Note that the spkg above was **not** merged, but the one at #5271.

Cheers,

Michael
