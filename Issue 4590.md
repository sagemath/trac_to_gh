# Issue 4590: sage/interfaces/phc.py writes tmp files into cwd

archive/issues_004590.json:
```json
{
    "body": "Assignee: mhampton\n\nFrom _output_from_command_list:\n\n```\n        EXAMPLES:\n            sage: from sage.interfaces.phc import *  #optional\n            sage: R2.<x,y> = PolynomialRing(QQ,2)    #optional\n            sage: start_sys = [(x-1)^2+(y-1)-1, x^2+y^2-1]  #optional\n            sage: a = phc._output_from_command_list(['phc -m','4','n','n','n'], start_sys)#optional\n            sage: os.unlink(a)#optional\n```\nThe Sage library might not be writable for the user who is running doctests, so the above doctest needs to be fixed.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4590\n\n",
    "created_at": "2008-11-23T04:16:14Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "sage/interfaces/phc.py writes tmp files into cwd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4590",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_034357.json:
```json
{
    "body": "Attachment [trac_4590.patch](tarball://root/attachments/some-uuid/ticket4590/trac_4590.patch) by @mwhansen created at 2009-01-21 21:17:30",
    "created_at": "2009-01-21T21:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34357",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4590.patch](tarball://root/attachments/some-uuid/ticket4590/trac_4590.patch) by @mwhansen created at 2009-01-21 21:17:30



---

archive/issue_comments_034358.json:
```json
{
    "body": "Actually, the only files that get used in that function are these:\n\n```\n        input_filename = sage.misc.misc.tmp_filename()\n        output_filename = sage.misc.misc.tmp_filename()\n```\n\nThe doctest may have been a little misleading.  The reviewer can decide if the patch should go in or the ticket should be marked as invalid.",
    "created_at": "2009-01-21T21:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34358",
    "user": "https://github.com/mwhansen"
}
```

Actually, the only files that get used in that function are these:

```
        input_filename = sage.misc.misc.tmp_filename()
        output_filename = sage.misc.misc.tmp_filename()
```

The doctest may have been a little misleading.  The reviewer can decide if the patch should go in or the ticket should be marked as invalid.



---

archive/issue_comments_034359.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-21T21:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34359",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034360.json:
```json
{
    "body": "Changing assignee from mhampton to @mwhansen.",
    "created_at": "2009-01-21T21:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34360",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mhampton to @mwhansen.



---

archive/issue_comments_034361.json:
```json
{
    "body": "Either way is fine with me.  Looking at the code, it seems that mhansen is right.  I'd probably go with the patch so things are less confusing.",
    "created_at": "2009-01-22T15:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34361",
    "user": "https://github.com/jasongrout"
}
```

Either way is fine with me.  Looking at the code, it seems that mhansen is right.  I'd probably go with the patch so things are less confusing.



---

archive/issue_events_010440.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T02:35:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4590#event-10440"
}
```



---

archive/issue_comments_034362.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T02:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034363.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T02:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4590#issuecomment-34363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_events_010441.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T02:35:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4590",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4590#event-10441"
}
```
