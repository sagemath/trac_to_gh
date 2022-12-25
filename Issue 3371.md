# Issue 3371: bug in uniformiSer for p-adic rings

archive/issues_003371.json:
```json
{
    "body": "Assignee: @malb\n\n\nUniformi Z er\n\n\n```\nsage : A = Zp(7,10)\nsage : B.<t> = A.ext(x^2+7)\nsage : B.uniformizer()\nt + O(t^21)\n```\n\n\nversus Uniformi S er\n\n\n```\nsage : B.uniformiser()\n6*t^2 + t^4 + O(t^22)\n```\n\n\nwhich is NOT a uniformiser.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3371\n\n",
    "created_at": "2008-06-05T14:01:32Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "bug in uniformiSer for p-adic rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3371",
    "user": "https://github.com/categorie"
}
```
Assignee: @malb


Uniformi Z er


```
sage : A = Zp(7,10)
sage : B.<t> = A.ext(x^2+7)
sage : B.uniformizer()
t + O(t^21)
```


versus Uniformi S er


```
sage : B.uniformiser()
6*t^2 + t^4 + O(t^22)
```


which is NOT a uniformiser.


Issue created by migration from https://trac.sagemath.org/ticket/3371





---

archive/issue_comments_023536.json:
```json
{
    "body": "Attachment [sage-3371.patch](tarball://root/attachments/some-uuid/ticket3371/sage-3371.patch) by fwclarke created at 2008-06-05 17:09:07",
    "created_at": "2008-06-05T17:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23536",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [sage-3371.patch](tarball://root/attachments/some-uuid/ticket3371/sage-3371.patch) by fwclarke created at 2008-06-05 17:09:07



---

archive/issue_comments_023537.json:
```json
{
    "body": "The attached patch solves the problem [and also eliminates a stray tab].",
    "created_at": "2008-06-05T17:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23537",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The attached patch solves the problem [and also eliminates a stray tab].



---

archive/issue_events_007599.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-05T19:19:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3371#event-7599"
}
```



---

archive/issue_comments_023538.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23538",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_023539.json:
```json
{
    "body": "extra touch-ups",
    "created_at": "2008-06-18T08:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23539",
    "user": "https://github.com/craigcitro"
}
```

extra touch-ups



---

archive/issue_comments_023540.json:
```json
{
    "body": "Attachment [trac-3371.patch](tarball://root/attachments/some-uuid/ticket3371/trac-3371.patch) by @roed314 created at 2008-06-18 09:05:14\n\nI approve of the changes in this ticket.",
    "created_at": "2008-06-18T09:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23540",
    "user": "https://github.com/roed314"
}
```

Attachment [trac-3371.patch](tarball://root/attachments/some-uuid/ticket3371/trac-3371.patch) by @roed314 created at 2008-06-18 09:05:14

I approve of the changes in this ticket.



---

archive/issue_comments_023541.json:
```json
{
    "body": "Attachment [trac-3371-doctest.patch](tarball://root/attachments/some-uuid/ticket3371/trac-3371-doctest.patch) by @craigcitro created at 2008-06-18 09:05:31\n\nadd a doctest",
    "created_at": "2008-06-18T09:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23541",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3371-doctest.patch](tarball://root/attachments/some-uuid/ticket3371/trac-3371-doctest.patch) by @craigcitro created at 2008-06-18 09:05:31

add a doctest



---

archive/issue_comments_023542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T07:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23542",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023543.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T07:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3371#issuecomment-23543",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.0.4.alpha0



---

archive/issue_events_007600.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T07:06:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3371#event-7600"
}
```



---

archive/issue_events_007601.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T07:06:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3371#event-7601"
}
```



---

archive/issue_events_007602.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T07:06:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3371",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3371#event-7602"
}
```
