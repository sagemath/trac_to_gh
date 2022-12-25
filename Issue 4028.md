# Issue 4028: doctest and improve sage/interfaces/axiom.py

archive/issues_004028.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4028\n\n",
    "created_at": "2008-09-01T02:40:26Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "doctest and improve sage/interfaces/axiom.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4028",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/4028





---

archive/issue_comments_028988.json:
```json
{
    "body": "Attachment [trac_4028.patch](tarball://root/attachments/some-uuid/ticket4028/trac_4028.patch) by mabshoff created at 2008-09-01 03:17:10\n\nOne spelling error: \"requires Axoim\" (which Mike corrected) - other than that is passes doctests with and without Axiom installed. Mike went with me over the patch and answered questions. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-28988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4028.patch](tarball://root/attachments/some-uuid/ticket4028/trac_4028.patch) by mabshoff created at 2008-09-01 03:17:10

One spelling error: "requires Axoim" (which Mike corrected) - other than that is passes doctests with and without Axiom installed. Mike went with me over the patch and answered questions. Positive review.

Cheers,

Michael



---

archive/issue_comments_028989.json:
```json
{
    "body": "Oops, with the original axiom running the doctest with -optional results in a fork bomb :(\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-28989",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, with the original axiom running the doctest with -optional results in a fork bomb :(

Cheers,

Michael



---

archive/issue_comments_028990.json:
```json
{
    "body": "Looks like somehow the following ends up getting called:\n\n```\nsage -axiom -nox -noclef\n```\nIf I run that from the command line it also starts a fork bomb.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-28990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks like somehow the following ends up getting called:

```
sage -axiom -nox -noclef
```
If I run that from the command line it also starts a fork bomb.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_028991.json:
```json
{
    "body": "It is all William's fault:\n\n```\nmabshoff@sage:/usr/local/bin$ pwd\n/usr/local/bin\nmabshoff@sage:/usr/local/bin$ cat axiom \n#!/bin/sh\nsage -axiom $*\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-28991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It is all William's fault:

```
mabshoff@sage:/usr/local/bin$ pwd
/usr/local/bin
mabshoff@sage:/usr/local/bin$ cat axiom 
#!/bin/sh
sage -axiom $*
```

Cheers,

Michael



---

archive/issue_comments_028992.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T04:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-28992",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_events_009202.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-01T04:13:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4028#event-9202"
}
```



---

archive/issue_comments_028993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T04:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-28993",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
