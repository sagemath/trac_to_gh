# Issue 3797: [with patch, needs review] several improvements to graph generation

archive/issues_003797.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ekirkman\n\nThis patch:\n\n1. Fixes a bug in sparse6 strings for n=0.\n2. Implements generation of graphs with loops.\n3. Implements generation of graphs with specified degree sequence.\n\nThe last two have been verified to some extent using Sloane's tables. It's all in the documentation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3797\n\n",
    "created_at": "2008-08-09T22:25:31Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] several improvements to graph generation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3797",
    "user": "rlm"
}
```
Assignee: rlm

CC:  ekirkman

This patch:

1. Fixes a bug in sparse6 strings for n=0.
2. Implements generation of graphs with loops.
3. Implements generation of graphs with specified degree sequence.

The last two have been verified to some extent using Sloane's tables. It's all in the documentation.

Issue created by migration from https://trac.sagemath.org/ticket/3797





---

archive/issue_comments_026999.json:
```json
{
    "body": "Attachment [trac3797-graph_generator_improvements.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-graph_generator_improvements.patch) by rlm created at 2008-08-09 23:15:47",
    "created_at": "2008-08-09T23:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-26999",
    "user": "rlm"
}
```

Attachment [trac3797-graph_generator_improvements.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-graph_generator_improvements.patch) by rlm created at 2008-08-09 23:15:47



---

archive/issue_comments_027000.json:
```json
{
    "body": "Depends on #3789.",
    "created_at": "2008-08-10T03:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-27000",
    "user": "rlm"
}
```

Depends on #3789.



---

archive/issue_comments_027001.json:
```json
{
    "body": "Attachment [trac3797-augment_by_verts.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-augment_by_verts.patch) by rlm created at 2008-08-10 03:22:38",
    "created_at": "2008-08-10T03:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-27001",
    "user": "rlm"
}
```

Attachment [trac3797-augment_by_verts.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-augment_by_verts.patch) by rlm created at 2008-08-10 03:22:38



---

archive/issue_comments_027002.json:
```json
{
    "body": "From the submission:\n\n\n```\nThis patch:\n\n   1. Fixes a bug in sparse6 strings for n=0.\n```\n\n\nI think this bugfix looks good.\n\n\n```\n   2. Implements generation of graphs with loops.\n```\n\n\nThis looks good -- I can't guarantee that it works, but it looks fine.\n\n\n```\n   3. Implements generation of graphs with specified degree sequence.\n```\n\n\nIt's not clear what degree sequence means.  I can derive it from the code, but maybe change\n\n```\n \t241\t        deg_seq -- a sequence of degrees for the graph to have. If specified, \n \t242\t            augment, property and size are all ignored. \n```\n\nto something like\n\n```\n \t241\t        deg_seq -- a sequence of non-negative integers.  The degrees of the vertices of the generated graph will be the specified integers, in some order.  If specified, \n \t242\t            augment, property and size are all ignored. \n```\n\n\nIs that even clearer?",
    "created_at": "2008-08-10T06:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-27002",
    "user": "ncalexan"
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

archive/issue_comments_027003.json:
```json
{
    "body": "Attachment [trac3797-docs.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-docs.patch) by ncalexan created at 2008-08-10 06:20:13\n\nLooks good!",
    "created_at": "2008-08-10T06:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-27003",
    "user": "ncalexan"
}
```

Attachment [trac3797-docs.patch](tarball://root/attachments/some-uuid/ticket3797/trac3797-docs.patch) by ncalexan created at 2008-08-10 06:20:13

Looks good!



---

archive/issue_comments_027004.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.alpha1",
    "created_at": "2008-08-10T06:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-27004",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.1.alpha1



---

archive/issue_comments_027005.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T06:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3797#issuecomment-27005",
    "user": "mabshoff"
}
```

Resolution: fixed
