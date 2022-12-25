# Issue 3653: Better random complex numbers

archive/issues_003653.json:
```json
{
    "body": "Assignee: somebody\n\nI have tried to generate some random complex numbers today and discovered that random_element behaves somewhat unexpected - without arguments it returns integer values between -2 and 2, with an optional argument n - integers between -n and n. That is exactly what is described in the documentation, but I would expect it to be a random complex number from the square [-1,1]x[-1,1] or unit disk and with an argument - a random value from the square or the disk of given size.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3653\n\n",
    "created_at": "2008-07-13T22:34:23Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Better random complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3653",
    "user": "https://github.com/novoselt"
}
```
Assignee: somebody

I have tried to generate some random complex numbers today and discovered that random_element behaves somewhat unexpected - without arguments it returns integer values between -2 and 2, with an optional argument n - integers between -n and n. That is exactly what is described in the documentation, but I would expect it to be a random complex number from the square [-1,1]x[-1,1] or unit disk and with an argument - a random value from the square or the disk of given size.

Issue created by migration from https://trac.sagemath.org/ticket/3653





---

archive/issue_comments_025776.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2008-08-02T13:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3653#issuecomment-25776",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_025777.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-02T13:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3653#issuecomment-25777",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025778.json:
```json
{
    "body": "Attachment [trac3653-complex-random_element.patch](tarball://root/attachments/some-uuid/ticket3653/trac3653-complex-random_element.patch) by cwitty created at 2008-08-23 17:29:52",
    "created_at": "2008-08-23T17:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3653#issuecomment-25778",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac3653-complex-random_element.patch](tarball://root/attachments/some-uuid/ticket3653/trac3653-complex-random_element.patch) by cwitty created at 2008-08-23 17:29:52



---

archive/issue_comments_025779.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-08-26T22:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3653#issuecomment-25779",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_003872.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-26T22:54:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3653",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3653#event-3872"
}
```



---

archive/issue_comments_025780.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-26T22:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3653#issuecomment-25780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_025781.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-26T22:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3653#issuecomment-25781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
