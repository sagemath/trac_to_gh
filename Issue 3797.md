# Issue 3797: [with patch, with positive review] several improvements to graph generation

archive/issues_003797.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  ekirkman\n\nThis patch:\n\n1. Fixes a bug in sparse6 strings for n=0.\n2. Implements generation of graphs with loops.\n3. Implements generation of graphs with specified degree sequence.\n\nThe last two have been verified to some extent using Sloane's tables. It's all in the documentation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3797\n\n",
    "closed_at": "2008-08-10T06:53:45Z",
    "created_at": "2008-08-09T22:25:31Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, with positive review] several improvements to graph generation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3797",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

CC:  ekirkman

This patch:

1. Fixes a bug in sparse6 strings for n=0.
2. Implements generation of graphs with loops.
3. Implements generation of graphs with specified degree sequence.

The last two have been verified to some extent using Sloane's tables. It's all in the documentation.

Issue created by migration from https://trac.sagemath.org/ticket/3797





---

archive/issue_comments_026941.json:
```json
{
    "body": "Attachment [trac3797-graph_generator_improvements.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-graph_generator_improvements.patch) by @rlmill created at 2008-08-09 23:15:47",
    "created_at": "2008-08-09T23:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26941",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac3797-graph_generator_improvements.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-graph_generator_improvements.patch) by @rlmill created at 2008-08-09 23:15:47



---

archive/issue_comments_026942.json:
```json
{
    "body": "Depends on #3789.",
    "created_at": "2008-08-10T03:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26942",
    "user": "https://github.com/rlmill"
}
```

Depends on #3789.



---

archive/issue_comments_026943.json:
```json
{
    "body": "Attachment [trac3797-augment_by_verts.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-augment_by_verts.patch) by @rlmill created at 2008-08-10 03:22:38",
    "created_at": "2008-08-10T03:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26943",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac3797-augment_by_verts.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-augment_by_verts.patch) by @rlmill created at 2008-08-10 03:22:38



---

archive/issue_comments_026944.json:
```json
{
    "body": "From the submission:\n\n```\nThis patch:\n\n   1. Fixes a bug in sparse6 strings for n=0.\n```\n\nI think this bugfix looks good.\n\n```\n   2. Implements generation of graphs with loops.\n```\n\nThis looks good -- I can't guarantee that it works, but it looks fine.\n\n```\n   3. Implements generation of graphs with specified degree sequence.\n```\n\nIt's not clear what degree sequence means.  I can derive it from the code, but maybe change\n\n```\n \t241\t        deg_seq -- a sequence of degrees for the graph to have. If specified, \n \t242\t            augment, property and size are all ignored. \n```\nto something like\n\n```\n \t241\t        deg_seq -- a sequence of non-negative integers.  The degrees of the vertices of the generated graph will be the specified integers, in some order.  If specified, \n \t242\t            augment, property and size are all ignored. \n```\n\nIs that even clearer?",
    "created_at": "2008-08-10T06:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26944",
    "user": "https://github.com/ncalexan"
}
```

From the submission:

```
This patch:

   1. Fixes a bug in sparse6 strings for n=0.
```

I think this bugfix looks good.

```
   2. Implements generation of graphs with loops.
```

This looks good -- I can't guarantee that it works, but it looks fine.

```
   3. Implements generation of graphs with specified degree sequence.
```

It's not clear what degree sequence means.  I can derive it from the code, but maybe change

```
 	241	        deg_seq -- a sequence of degrees for the graph to have. If specified, 
 	242	            augment, property and size are all ignored. 
```
to something like

```
 	241	        deg_seq -- a sequence of non-negative integers.  The degrees of the vertices of the generated graph will be the specified integers, in some order.  If specified, 
 	242	            augment, property and size are all ignored. 
```

Is that even clearer?



---

archive/issue_comments_026945.json:
```json
{
    "body": "Attachment [trac3797-docs.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-docs.patch) by @ncalexan created at 2008-08-10 06:20:13\n\nLooks good!",
    "created_at": "2008-08-10T06:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26945",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac3797-docs.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-docs.patch) by @ncalexan created at 2008-08-10 06:20:13

Looks good!



---

archive/issue_comments_026946.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.alpha1",
    "created_at": "2008-08-10T06:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26946",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.1.alpha1



---

archive/issue_events_008727.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-10T06:53:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3797#event-8727"
}
```



---

archive/issue_comments_026947.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T06:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26947",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
