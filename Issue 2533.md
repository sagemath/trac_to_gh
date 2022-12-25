# Issue 2533: add "-p" flag to $CP for make install

archive/issues_002533.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nOn Saturday 15 March 2008, Paul Zimmermann wrote:\n>        Hi,\n\n> I wonder why sage -br takes so much time after a fresh build from source\n> and make install. Normally, since everything was just compiled, it should\n> have nothing to do. I guess the reason lies in:\n\n>    bash-3.00$ make install DESTDIR=/usr/local/sage-2.10.3 -n\n>    ...\n>    cp -rv * /usr/local/sage-2.10.3/sage/\n>    ...\n\n> where 'cp' does not preserve the dates of the files, and thus the correct\n> dependencies are lost. Maybe \"mv * /usr/local/sage-2.10.3/sage/\" would\n> solve that problem?\n\nOr use\n    cp -prv * ...\nthe -p option preserve timestamps.\n\nBill\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2533\n\n",
    "created_at": "2008-03-15T22:15:35Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "add \"-p\" flag to $CP for make install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
On Saturday 15 March 2008, Paul Zimmermann wrote:
>        Hi,

> I wonder why sage -br takes so much time after a fresh build from source
> and make install. Normally, since everything was just compiled, it should
> have nothing to do. I guess the reason lies in:

>    bash-3.00$ make install DESTDIR=/usr/local/sage-2.10.3 -n
>    ...
>    cp -rv * /usr/local/sage-2.10.3/sage/
>    ...

> where 'cp' does not preserve the dates of the files, and thus the correct
> dependencies are lost. Maybe "mv * /usr/local/sage-2.10.3/sage/" would
> solve that problem?

Or use
    cp -prv * ...
the -p option preserve timestamps.

Bill
```


Issue created by migration from https://trac.sagemath.org/ticket/2533





---

archive/issue_comments_017234.json:
```json
{
    "body": "Attachment [trac_2533.patch](tarball://root/attachments/some-uuid/ticket2533/trac_2533.patch) by mabshoff created at 2008-03-15 22:19:16",
    "created_at": "2008-03-15T22:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2533#issuecomment-17234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2533.patch](tarball://root/attachments/some-uuid/ticket2533/trac_2533.patch) by mabshoff created at 2008-03-15 22:19:16



---

archive/issue_comments_017235.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-15T22:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2533#issuecomment-17235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017236.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-15T22:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2533#issuecomment-17236",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_017237.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T22:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2533#issuecomment-17237",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.rc0



---

archive/issue_events_002714.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T22:26:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2533",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2533#event-2714"
}
```



---

archive/issue_comments_017238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T22:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2533#issuecomment-17238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
