# Issue 3632: [with patch,with positive review] small bug in p-adic heights

archive/issues_003632.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: E = EllipticCurve([37,0])\nsage: E.padic_regulator(5)\n```\n\ngives a Assertion Error.\n\nThe included patch corrects this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3632\n\n",
    "closed_at": "2008-07-16T01:33:52Z",
    "created_at": "2008-07-10T13:11:05Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with patch,with positive review] small bug in p-adic heights",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3632",
    "user": "https://github.com/categorie"
}
```
Assignee: @williamstein

```
sage: E = EllipticCurve([37,0])
sage: E.padic_regulator(5)
```

gives a Assertion Error.

The included patch corrects this.

Issue created by migration from https://trac.sagemath.org/ticket/3632





---

archive/issue_comments_025638.json:
```json
{
    "body": "Attachment [trac.3632.patch](tarball://root/attachments/some-uuid/ticket3632/trac.3632.patch) by @categorie created at 2008-07-10 13:11:54",
    "created_at": "2008-07-10T13:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25638",
    "user": "https://github.com/categorie"
}
```

Attachment [trac.3632.patch](tarball://root/attachments/some-uuid/ticket3632/trac.3632.patch) by @categorie created at 2008-07-10 13:11:54



---

archive/issue_events_008336.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-10T13:13:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "milestone": "sage-3.0.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3632#event-8336"
}
```



---

archive/issue_comments_025639.json:
```json
{
    "body": "I hate to do this.... it's obviously a perfectly good patch.... but the documentation needs to be updated too, and the loop in the doctests needs to test the m = 1 case, and somewhere you need to add a doctest showing the correct behaviour for the example you gave in the ticket description!",
    "created_at": "2008-07-10T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25639",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I hate to do this.... it's obviously a perfectly good patch.... but the documentation needs to be updated too, and the loop in the doctests needs to test the m = 1 case, and somewhere you need to add a doctest showing the correct behaviour for the example you gave in the ticket description!



---

archive/issue_comments_025640.json:
```json
{
    "body": "Attachment [trac.3632.extra1.patch](tarball://root/attachments/some-uuid/ticket3632/trac.3632.extra1.patch) by @categorie created at 2008-07-11 10:23:22\n\nOk. I added an additional patch (applied after the first) with some docstring. I hope that it is enough.",
    "created_at": "2008-07-11T10:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25640",
    "user": "https://github.com/categorie"
}
```

Attachment [trac.3632.extra1.patch](tarball://root/attachments/some-uuid/ticket3632/trac.3632.extra1.patch) by @categorie created at 2008-07-11 10:23:22

Ok. I added an additional patch (applied after the first) with some docstring. I hope that it is enough.



---

archive/issue_comments_025641.json:
```json
{
    "body": "Attachment [trac.3632.extra2.patch](tarball://root/attachments/some-uuid/ticket3632/trac.3632.extra2.patch) by dmharvey created at 2008-07-11 13:10:45\n\nhi, I've added yet a third patch, with minor changes to your patch, plus cleaning up some existing nearby doctests which didn't make sense to me. Assuming you are happy with these changes, I think this patch is good to go.\n\n(all three patches should be applied)",
    "created_at": "2008-07-11T13:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25641",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [trac.3632.extra2.patch](tarball://root/attachments/some-uuid/ticket3632/trac.3632.extra2.patch) by dmharvey created at 2008-07-11 13:10:45

hi, I've added yet a third patch, with minor changes to your patch, plus cleaning up some existing nearby doctests which didn't make sense to me. Assuming you are happy with these changes, I think this patch is good to go.

(all three patches should be applied)



---

archive/issue_comments_025642.json:
```json
{
    "body": "Yop, that is fine with me. I guess I am allowed to change the 'summary'.",
    "created_at": "2008-07-14T09:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25642",
    "user": "https://github.com/categorie"
}
```

Yop, that is fine with me. I guess I am allowed to change the 'summary'.



---

archive/issue_comments_025643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T01:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25643",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025644.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T01:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25644",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0



---

archive/issue_events_008337.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-16T01:33:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3632#event-8337"
}
```
