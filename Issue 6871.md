# Issue 6871: temporary passwords aren't temporary

archive/issues_006871.json:
```json
{
    "body": "Assignee: boothby\n\nAs described in comment:27:ticket:4135, when #4135 is applied, the \"temporary\" password you get when resetting a user's password isn't temporary -- you can log in, log out, and then log in again with it.\n\nAlso, the page that tells you the new password has a title of \"Error\" even though no error has occurred.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6871\n\n",
    "created_at": "2009-09-03T03:19:25Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "temporary passwords aren't temporary",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6871",
    "user": "https://github.com/dandrake"
}
```
Assignee: boothby

As described in comment:27:ticket:4135, when #4135 is applied, the "temporary" password you get when resetting a user's password isn't temporary -- you can log in, log out, and then log in again with it.

Also, the page that tells you the new password has a title of "Error" even though no error has occurred.

Issue created by migration from https://trac.sagemath.org/ticket/6871





---

archive/issue_comments_056629.json:
```json
{
    "body": "This comment may be gratuitous, but the issue I'm having with the notebook running on Sage 5.3 is:\n\n1) I create a new user.\n\n2) I let the user know their temporary password.\n\n3) They log in successfully with their temporary password.\n\n4) They change their password.\n\n5) After automatic logout, neither password works, not the temporary nor the newly created password.  Screen reads \"wrong password\".\n\nThe weird thing is, when I do this with a longer than 4 letter name I don't get this problem...",
    "created_at": "2012-10-19T07:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6871#issuecomment-56629",
    "user": "https://trac.sagemath.org/admin/accounts/users/startakovsky"
}
```

This comment may be gratuitous, but the issue I'm having with the notebook running on Sage 5.3 is:

1) I create a new user.

2) I let the user know their temporary password.

3) They log in successfully with their temporary password.

4) They change their password.

5) After automatic logout, neither password works, not the temporary nor the newly created password.  Screen reads "wrong password".

The weird thing is, when I do this with a longer than 4 letter name I don't get this problem...



---

archive/issue_comments_056630.json:
```json
{
    "body": "The 'error' message is long since gone.\n\nI cannot replicate the issue in comment:1, though it is certainly not gratuitous.  Partly that is because we now say\n> The username must start with a letter and be between 4 and 32 characters long.\n\nSo the only remaining issue is, of course, the one actually mentioned.  The question is whether this is a problem...",
    "created_at": "2014-12-10T19:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6871#issuecomment-56630",
    "user": "https://github.com/kcrisman"
}
```

The 'error' message is long since gone.

I cannot replicate the issue in comment:1, though it is certainly not gratuitous.  Partly that is because we now say
> The username must start with a letter and be between 4 and 32 characters long.

So the only remaining issue is, of course, the one actually mentioned.  The question is whether this is a problem...



---

archive/issue_comments_056631.json:
```json
{
    "body": "https://github.com/sagemath/sagenb/issues/294",
    "created_at": "2014-12-10T19:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6871#issuecomment-56631",
    "user": "https://github.com/kcrisman"
}
```

https://github.com/sagemath/sagenb/issues/294



---

archive/issue_comments_056632.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6871#issuecomment-56632",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid



---

archive/issue_comments_056633.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6871",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6871#issuecomment-56633",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_events_007103.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2020-03-29T02:12:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6871",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6871#event-7103"
}
```
