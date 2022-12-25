# Issue 3298: Cython warnings for PolyBoRi

archive/issues_003298.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @robertwb @burcin\n\nKeywords: polybori, cython\n\n```\npython2.5 `which cython` --embed-positions --incref-local-binop -I/usr/local/sage-3.0/devel/sage-main -opbori.pyx\nwarning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:40:56: Function signature does not match previous declaration\nwarning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:41:59: Function signature does not match previous declaration\nwarning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:200:10: Function signature does not match previous declaration\nFinished updating Cython code (time = 2.520616 seconds)\n```\n\nI couldn't figure out what is wrong. Maybe a false positive?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3298\n\n",
    "created_at": "2008-05-25T13:41:31Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Cython warnings for PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3298",
    "user": "https://github.com/malb"
}
```
Assignee: cwitty

CC:  @robertwb @burcin

Keywords: polybori, cython

```
python2.5 `which cython` --embed-positions --incref-local-binop -I/usr/local/sage-3.0/devel/sage-main -opbori.pyx
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:40:56: Function signature does not match previous declaration
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:41:59: Function signature does not match previous declaration
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:200:10: Function signature does not match previous declaration
Finished updating Cython code (time = 2.520616 seconds)
```

I couldn't figure out what is wrong. Maybe a false positive?

Issue created by migration from https://trac.sagemath.org/ticket/3298





---

archive/issue_comments_022777.json:
```json
{
    "body": "fix cython warnings for pbori.pyx",
    "created_at": "2009-01-24T19:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22777",
    "user": "https://github.com/burcin"
}
```

fix cython warnings for pbori.pyx



---

archive/issue_comments_022778.json:
```json
{
    "body": "Changing assignee from cwitty to @burcin.",
    "created_at": "2009-01-24T19:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22778",
    "user": "https://github.com/burcin"
}
```

Changing assignee from cwitty to @burcin.



---

archive/issue_comments_022779.json:
```json
{
    "body": "Attachment [trac_3298-pbori_cython_warnings.patch](tarball://root/attachments/some-uuid/ticket3298/trac_3298-pbori_cython_warnings.patch) by @burcin created at 2009-01-24 19:07:29\n\nThrough a chain of typedefs the parameter expected by these functions was defined to be int, not the enum declared in the .pxi file. With the attached patch, the warnings go away. :)",
    "created_at": "2009-01-24T19:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22779",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_3298-pbori_cython_warnings.patch](tarball://root/attachments/some-uuid/ticket3298/trac_3298-pbori_cython_warnings.patch) by @burcin created at 2009-01-24 19:07:29

Through a chain of typedefs the parameter expected by these functions was defined to be int, not the enum declared in the .pxi file. With the attached patch, the warnings go away. :)



---

archive/issue_events_007409.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2009-01-24T19:07:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3298#event-7409"
}
```



---

archive/issue_comments_022780.json:
```json
{
    "body": "Looks good.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good.

Cheers,

Michael



---

archive/issue_events_007410.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T19:13:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3298#event-7410"
}
```



---

archive/issue_comments_022781.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022782.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T19:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3298#issuecomment-22782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2
