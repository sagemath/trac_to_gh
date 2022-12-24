# Issue 4590: sage/interfaces/phc.py writes tmp files into cwd

archive/issues_004590.json:
```json
{
    "body": "Assignee: mhampton\n\nFrom _output_from_command_list:\n\n```\n        EXAMPLES:\n            sage: from sage.interfaces.phc import *  #optional\n            sage: R2.<x,y> = PolynomialRing(QQ,2)    #optional\n            sage: start_sys = [(x-1)^2+(y-1)-1, x^2+y^2-1]  #optional\n            sage: a = phc._output_from_command_list(['phc -m','4','n','n','n'], start_sys)#optional\n            sage: os.unlink(a)#optional\n```\n\nThe Sage library might not be writable for the user who is running doctests, so the above doctest needs to be fixed.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4590\n\n",
    "created_at": "2008-11-23T04:16:14Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "sage/interfaces/phc.py writes tmp files into cwd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4590",
    "user": "mabshoff"
}
```
Assignee: mhampton

From _output_from_command_list:

```
        EXAMPLES:
            sage: from sage.interfaces.phc import *  #optional
            sage: R2.<x,y> = PolynomialRing(QQ,2)    #optional
            sage: start_sys = [(x-1)^2+(y-1)-1, x^2+y^2-1]  #optional
            sage: a = phc._output_from_command_list(['phc -m','4','n','n','n'], start_sys)#optional
            sage: os.unlink(a)#optional
```

The Sage library might not be writable for the user who is running doctests, so the above doctest needs to be fixed.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4590





---

archive/issue_comments_034424.json:
```json
{
    "body": "Attachment [trac_4590.patch](tarball://root/attachments/some-uuid/ticket4590/trac_4590.patch) by @mwhansen created at 2009-01-21 21:17:30",
    "created_at": "2009-01-21T21:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34424",
    "user": "@mwhansen"
}
```

Attachment [trac_4590.patch](tarball://root/attachments/some-uuid/ticket4590/trac_4590.patch) by @mwhansen created at 2009-01-21 21:17:30



---

archive/issue_comments_034425.json:
```json
{
    "body": "Actually, the only files that get used in that function are these:\n\n\n```\n        input_filename = sage.misc.misc.tmp_filename()\n        output_filename = sage.misc.misc.tmp_filename()\n```\n\n\nThe doctest may have been a little misleading.  The reviewer can decide if the patch should go in or the ticket should be marked as invalid.",
    "created_at": "2009-01-21T21:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34425",
    "user": "@mwhansen"
}
```

Actually, the only files that get used in that function are these:


```
        input_filename = sage.misc.misc.tmp_filename()
        output_filename = sage.misc.misc.tmp_filename()
```


The doctest may have been a little misleading.  The reviewer can decide if the patch should go in or the ticket should be marked as invalid.



---

archive/issue_comments_034426.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-21T21:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34426",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034427.json:
```json
{
    "body": "Changing assignee from mhampton to @mwhansen.",
    "created_at": "2009-01-21T21:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34427",
    "user": "@mwhansen"
}
```

Changing assignee from mhampton to @mwhansen.



---

archive/issue_comments_034428.json:
```json
{
    "body": "Either way is fine with me.  Looking at the code, it seems that mhansen is right.  I'd probably go with the patch so things are less confusing.",
    "created_at": "2009-01-22T15:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34428",
    "user": "@jasongrout"
}
```

Either way is fine with me.  Looking at the code, it seems that mhansen is right.  I'd probably go with the patch so things are less confusing.



---

archive/issue_comments_034429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T02:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34429",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034430.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T02:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34430",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1
