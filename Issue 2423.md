# Issue 2423: notebook() opens up to the entire world by default

archive/issues_002423.json:
```json
{
    "body": "Assignee: boothby\n\nSee http://groups.google.com/group/sage-support/browse_thread/thread/3aeb27037554491b\n\nThe meat of the issue is that notebook() by default allows connections from anyone to the local computer.  This patch fixes it by calling the \"interface\" option of twisted to only allow connections from a specific interface.\n\nQuoting Yi Qiang in the email discussion:\n\n```\nThe problem is that the notebook is never launched to bound to a specific\ninterface. Could you please file a trac# against this?\n\nThe specific issue is that in twistedconf.tac, we start the server like so:\n\nstrports.service('tls:8000:privateKey=/Users/yqiang/.sage/notebook/private.pem:certKey=/Users/yqiang/.sage/notebook/public.pem',\nfactory)\n\nIt should read something like\n\nstrports.service('tls:8000:interface=\n127.0.0.1:privateKey=/Users/yqiang/.sage/notebook/private.pem:certKey=/Users/yqiang/.sage/notebook/public.pem',\nfactory)\n\nto only listen on localhost.\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2423\n\n",
    "created_at": "2008-03-07T22:41:35Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "notebook() opens up to the entire world by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2423",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

See http://groups.google.com/group/sage-support/browse_thread/thread/3aeb27037554491b

The meat of the issue is that notebook() by default allows connections from anyone to the local computer.  This patch fixes it by calling the "interface" option of twisted to only allow connections from a specific interface.

Quoting Yi Qiang in the email discussion:

```
The problem is that the notebook is never launched to bound to a specific
interface. Could you please file a trac# against this?

The specific issue is that in twistedconf.tac, we start the server like so:

strports.service('tls:8000:privateKey=/Users/yqiang/.sage/notebook/private.pem:certKey=/Users/yqiang/.sage/notebook/public.pem',
factory)

It should read something like

strports.service('tls:8000:interface=
127.0.0.1:privateKey=/Users/yqiang/.sage/notebook/private.pem:certKey=/Users/yqiang/.sage/notebook/public.pem',
factory)

to only listen on localhost.

```

Issue created by migration from https://trac.sagemath.org/ticket/2423





---

archive/issue_comments_016360.json:
```json
{
    "body": "Attachment [notebook-interface.patch](tarball://root/attachments/some-uuid/ticket2423/notebook-interface.patch) by @jasongrout created at 2008-03-07 22:41:54",
    "created_at": "2008-03-07T22:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2423#issuecomment-16360",
    "user": "https://github.com/jasongrout"
}
```

Attachment [notebook-interface.patch](tarball://root/attachments/some-uuid/ticket2423/notebook-interface.patch) by @jasongrout created at 2008-03-07 22:41:54



---

archive/issue_comments_016361.json:
```json
{
    "body": "This patch looks good to me. \n\nThe only question I have is what happens when a user specifies an invalid address, but this was not handled previously so it's not a regression.\n\n+1",
    "created_at": "2008-03-07T23:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2423#issuecomment-16361",
    "user": "https://github.com/yqiang"
}
```

This patch looks good to me. 

The only question I have is what happens when a user specifies an invalid address, but this was not handled previously so it's not a regression.

+1



---

archive/issue_comments_016362.json:
```json
{
    "body": "Looks good to me.  Thanks!",
    "created_at": "2008-03-07T23:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2423#issuecomment-16362",
    "user": "https://github.com/williamstein"
}
```

Looks good to me.  Thanks!



---

archive/issue_events_005725.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-07T23:22:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2423",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2423#event-5725"
}
```



---

archive/issue_comments_016363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-07T23:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2423#issuecomment-16363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016364.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc3",
    "created_at": "2008-03-07T23:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2423#issuecomment-16364",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc3
