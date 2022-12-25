# Issue 2279: numerical noise? doctest failure in sage.rings.number_field.totallyreal.__selberg_zograf_bound with 2.10.2

archive/issues_002279.json:
```json
{
    "body": "Assignee: @williamstein\n\nA fresh 64-bit install of 2.10.2 gives this (and only this) error with\n\"make check\":\n\n\n```\nsage -t  devel/sage-main/sage/rings/number_field/totallyreal.py**********************************************************************\nFile \"totallyreal.py\", line 410:\n   sage: sage.rings.number_field.totallyreal.__selberg_zograf_bound(8,7)\nExpected:\n   15.851871776151311\nGot:\n   15.851871776151313\n**********************************************************************\n1 items had failures:\n  1 of   1 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_totallyreal.py\n        [1.7 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n       sage -t  devel/sage-main/sage/rings/number_field/totallyreal.py\n```\n\n\nOS info:\n\n```\njec@host-57-71%uname -a\nLinux host-57-71 2.6.18.8-0.3-default #1 SMP Tue Apr 17 08:42:35 UTC 2007 x86_64 x86_64 x86_64 GNU/Linux\n```\n\n\n```\ngcc version 4.1.2 20061115 (prerelease) (SUSE Linux)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2279\n\n",
    "created_at": "2008-02-23T20:25:21Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "numerical noise? doctest failure in sage.rings.number_field.totallyreal.__selberg_zograf_bound with 2.10.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2279",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

A fresh 64-bit install of 2.10.2 gives this (and only this) error with
"make check":


```
sage -t  devel/sage-main/sage/rings/number_field/totallyreal.py**********************************************************************
File "totallyreal.py", line 410:
   sage: sage.rings.number_field.totallyreal.__selberg_zograf_bound(8,7)
Expected:
   15.851871776151311
Got:
   15.851871776151313
**********************************************************************
1 items had failures:
  1 of   1 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_totallyreal.py
        [1.7 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


       sage -t  devel/sage-main/sage/rings/number_field/totallyreal.py
```


OS info:

```
jec@host-57-71%uname -a
Linux host-57-71 2.6.18.8-0.3-default #1 SMP Tue Apr 17 08:42:35 UTC 2007 x86_64 x86_64 x86_64 GNU/Linux
```


```
gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)
```



Issue created by migration from https://trac.sagemath.org/ticket/2279





---

archive/issue_comments_015081.json:
```json
{
    "body": "Deleted the function __selberg_zograf_bound.  Patch attached.  JV",
    "created_at": "2008-02-28T02:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15081",
    "user": "https://github.com/jvoight"
}
```

Deleted the function __selberg_zograf_bound.  Patch attached.  JV



---

archive/issue_comments_015082.json:
```json
{
    "body": "Attachment [8682.patch](tarball://root/attachments/some-uuid/ticket2279/8682.patch) by @williamstein created at 2008-02-28 06:28:20",
    "created_at": "2008-02-28T06:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15082",
    "user": "https://github.com/williamstein"
}
```

Attachment [8682.patch](tarball://root/attachments/some-uuid/ticket2279/8682.patch) by @williamstein created at 2008-02-28 06:28:20



---

archive/issue_comments_015083.json:
```json
{
    "body": "Attachment [trac-2279.patch](tarball://root/attachments/some-uuid/ticket2279/trac-2279.patch) by @craigcitro created at 2008-02-28 06:53:08\n\nSame patch as the above, but it's a patch against 2.10.2, as opposed to the current working version of the code John and I are using (which is what the other patch above is against. ;) )",
    "created_at": "2008-02-28T06:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15083",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2279.patch](tarball://root/attachments/some-uuid/ticket2279/trac-2279.patch) by @craigcitro created at 2008-02-28 06:53:08

Same patch as the above, but it's a patch against 2.10.2, as opposed to the current working version of the code John and I are using (which is what the other patch above is against. ;) )



---

archive/issue_events_002450.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-28T06:54:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2279#event-2450"
}
```



---

archive/issue_comments_015084.json:
```json
{
    "body": "Merged trac-2279.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T06:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-2279.patch in Sage 2.10.3.rc0



---

archive/issue_comments_015085.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T06:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015086.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-02-28T22:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15086",
    "user": "https://github.com/craigcitro"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002451.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2008-02-28T22:47:45Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2279#event-2451"
}
```



---

archive/issue_comments_015087.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-02-28T22:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15087",
    "user": "https://github.com/craigcitro"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_015088.json:
```json
{
    "body": "In the fix posted above, I did two things:\n\n* removed `selberg_zograf_bound`, because it was causing numerical issues here \n and there, and wasn't actually used anywhere.\n\n* changed the default choice of totally real field of discriminant 5 (which gets\n added to the list by hand), because John had done that in his patch. Unfortunately,\n I switched a `-` for a `+` when doing it, and added a non-totally-real field.\n\nThe new patch I've attached fixes the second of these.",
    "created_at": "2008-02-28T22:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15088",
    "user": "https://github.com/craigcitro"
}
```

In the fix posted above, I did two things:

* removed `selberg_zograf_bound`, because it was causing numerical issues here 
 and there, and wasn't actually used anywhere.

* changed the default choice of totally real field of discriminant 5 (which gets
 added to the list by hand), because John had done that in his patch. Unfortunately,
 I switched a `-` for a `+` when doing it, and added a non-totally-real field.

The new patch I've attached fixes the second of these.



---

archive/issue_comments_015089.json:
```json
{
    "body": "I don't see the new patch.  In fact the patches listed seem to be the same!",
    "created_at": "2008-02-28T22:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15089",
    "user": "https://github.com/JohnCremona"
}
```

I don't see the new patch.  In fact the patches listed seem to be the same!



---

archive/issue_comments_015090.json:
```json
{
    "body": "Yep, I'm still waiting for my copy of rc0 to finish its `sage -clone` on sage.math. I was guessing it would finish before anyone looked at this ticket. ;)",
    "created_at": "2008-02-28T23:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15090",
    "user": "https://github.com/craigcitro"
}
```

Yep, I'm still waiting for my copy of rc0 to finish its `sage -clone` on sage.math. I was guessing it would finish before anyone looked at this ticket. ;)



---

archive/issue_comments_015091.json:
```json
{
    "body": "Attachment [trac-2279.pt2.patch](tarball://root/attachments/some-uuid/ticket2279/trac-2279.pt2.patch) by @craigcitro created at 2008-02-28 23:05:12",
    "created_at": "2008-02-28T23:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15091",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2279.pt2.patch](tarball://root/attachments/some-uuid/ticket2279/trac-2279.pt2.patch) by @craigcitro created at 2008-02-28 23:05:12



---

archive/issue_comments_015092.json:
```json
{
    "body": "Combined patches are fine.  Note that 8682.patch is the same as trac-2279.patch, so may be ignored, but that trac-2279.pt2.patch needs to be applied after trac-2279.patch.",
    "created_at": "2008-02-29T09:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15092",
    "user": "https://github.com/JohnCremona"
}
```

Combined patches are fine.  Note that 8682.patch is the same as trac-2279.patch, so may be ignored, but that trac-2279.pt2.patch needs to be applied after trac-2279.patch.



---

archive/issue_events_002452.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-29T18:53:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2279#event-2452"
}
```



---

archive/issue_comments_015093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-29T18:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015094.json:
```json
{
    "body": "Merged trac-2279.pt2.patch in Sage 2.10.3.rc1",
    "created_at": "2008-02-29T18:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2279#issuecomment-15094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-2279.pt2.patch in Sage 2.10.3.rc1
