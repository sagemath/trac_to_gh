# Issue 1160: *major* bug in using the sage notebook as a maxima notebook

archive/issues_001160.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nOn Nov 12, 2007 10:20 PM, Moreira <fjm@fc.up.pt> wrote:\n> After changing system to Maxima in a worksheet, evaluations of cells\n> do not appear. If I write \"3+1\" in a cell and press SHIFT+ENTER the\n> green bar remains. If I interrupt the computation (option in drop down\n> menus) then,  the result appears immediately after I press the ok\n> button in the  alert message saying \"Unable to immediately interrupt\n> calculation\"\n> \n> The same happens if SAGE is chosen as the active system and I begin\n> the cell with %maxima.\n> \n> However,  writing \"maxima(3+1)\" the result  appears as expected.\n> \n> This happens to me running a vmware image of sage on windows XP and\n> accessing SAGE notebook with firefox 2.09. I also tried the notebook\n> interface at\n> https://sage.math.washington.edu:8103/\n> and I obtained the same \"behaviour\".\n> \n> If I  choose other systems (like sh, html,gp)  everything works fine..\n> \n> Is anybody experiencing this kind of  behaviour or is only a bug with\n> me?!\n\nYes, I see exactly the same bug.   This is a rather serious bug actually,\nand I'm really glad you reported it!  \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1160\n\n",
    "created_at": "2007-11-12T23:32:32Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "*major* bug in using the sage notebook as a maxima notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1160",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
On Nov 12, 2007 10:20 PM, Moreira <fjm@fc.up.pt> wrote:
> After changing system to Maxima in a worksheet, evaluations of cells
> do not appear. If I write "3+1" in a cell and press SHIFT+ENTER the
> green bar remains. If I interrupt the computation (option in drop down
> menus) then,  the result appears immediately after I press the ok
> button in the  alert message saying "Unable to immediately interrupt
> calculation"
> 
> The same happens if SAGE is chosen as the active system and I begin
> the cell with %maxima.
> 
> However,  writing "maxima(3+1)" the result  appears as expected.
> 
> This happens to me running a vmware image of sage on windows XP and
> accessing SAGE notebook with firefox 2.09. I also tried the notebook
> interface at
> https://sage.math.washington.edu:8103/
> and I obtained the same "behaviour".
> 
> If I  choose other systems (like sh, html,gp)  everything works fine..
> 
> Is anybody experiencing this kind of  behaviour or is only a bug with
> me?!

Yes, I see exactly the same bug.   This is a rather serious bug actually,
and I'm really glad you reported it!  
```


Issue created by migration from https://trac.sagemath.org/ticket/1160





---

archive/issue_comments_007071.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-02T03:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7071",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007072.json:
```json
{
    "body": "OK, a lead -- this is caused by line 254 of server/support.py, which calls\n\n```\n   maxima.chdir(...)\n```\n\nwhich hangs.",
    "created_at": "2007-12-02T04:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7072",
    "user": "https://github.com/williamstein"
}
```

OK, a lead -- this is caused by line 254 of server/support.py, which calls

```
   maxima.chdir(...)
```

which hangs.



---

archive/issue_comments_007073.json:
```json
{
    "body": "Attachment [trac-1160.patch](tarball://root/attachments/some-uuid/ticket1160/trac-1160.patch) by @williamstein created at 2007-12-02 05:28:10",
    "created_at": "2007-12-02T05:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7073",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1160.patch](tarball://root/attachments/some-uuid/ticket1160/trac-1160.patch) by @williamstein created at 2007-12-02 05:28:10



---

archive/issue_comments_007074.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T05:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007075.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T05:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7075",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha2.



---

archive/issue_comments_007076.json:
```json
{
    "body": "Attachment [trac1160-fix.patch](tarball://root/attachments/some-uuid/ticket1160/trac1160-fix.patch) by @williamstein created at 2007-12-02 07:03:51",
    "created_at": "2007-12-02T07:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7076",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1160-fix.patch](tarball://root/attachments/some-uuid/ticket1160/trac1160-fix.patch) by @williamstein created at 2007-12-02 07:03:51



---

archive/issue_comments_007077.json:
```json
{
    "body": "Attachment [trac1160-maxima-fix.patch](tarball://root/attachments/some-uuid/ticket1160/trac1160-maxima-fix.patch) by @williamstein created at 2007-12-02 18:49:47",
    "created_at": "2007-12-02T18:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7077",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1160-maxima-fix.patch](tarball://root/attachments/some-uuid/ticket1160/trac1160-maxima-fix.patch) by @williamstein created at 2007-12-02 18:49:47



---

archive/issue_comments_007078.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-02T18:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7078",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_007079.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-02T18:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7079",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007080.json:
```json
{
    "body": "Merged trac1160-maxima-fix.patch in 2.8.15.rc0.",
    "created_at": "2007-12-02T18:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac1160-maxima-fix.patch in 2.8.15.rc0.



---

archive/issue_comments_007081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T18:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1160#issuecomment-7081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
