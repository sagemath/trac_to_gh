# Issue 5452: Graph broken on a input of type dict of dicts

archive/issues_005452.json:
```json
{
    "body": "Assignee: slabbe\n\nIn sage-3.2.3 the code below was fine, but it is broken in sage-3.3 and sage-3.4.rc0 :\n\n\n```\nsage: a,b,c,d,e,f=sorted(SymmetricGroup(3))\nsage: Graph({b:{d:'c',e:'p'}, c:{d:'p',e:'c'}})\n\n...\n\n/sage/graphs/graph.pyc in __init__(self, data, pos, loops, format, boundary, weighted, implementation, sparse, vertex_labels, **kwds)\n   8261                     if v not in verts: verts.append(v)\n   8262                     if hash(u) > hash(v):\n-> 8263                         if u in data[v]:\n   8264                             if data[u][v] != data[v][u]:\n   8265                                 raise ValueError(\"Dict does not agree on edge (%s,%s)\"%(u,v))\n\nKeyError: (1,2,3)\n```\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5452\n\n",
    "created_at": "2009-03-07T17:15:45Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Graph broken on a input of type dict of dicts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5452",
    "user": "slabbe"
}
```
Assignee: slabbe

In sage-3.2.3 the code below was fine, but it is broken in sage-3.3 and sage-3.4.rc0 :


```
sage: a,b,c,d,e,f=sorted(SymmetricGroup(3))
sage: Graph({b:{d:'c',e:'p'}, c:{d:'p',e:'c'}})

...

/sage/graphs/graph.pyc in __init__(self, data, pos, loops, format, boundary, weighted, implementation, sparse, vertex_labels, **kwds)
   8261                     if v not in verts: verts.append(v)
   8262                     if hash(u) > hash(v):
-> 8263                         if u in data[v]:
   8264                             if data[u][v] != data[v][u]:
   8265                                 raise ValueError("Dict does not agree on edge (%s,%s)"%(u,v))

KeyError: (1,2,3)
```





Issue created by migration from https://trac.sagemath.org/ticket/5452





---

archive/issue_comments_042217.json:
```json
{
    "body": "Against sage-3.4.rc0",
    "created_at": "2009-03-07T17:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5452#issuecomment-42217",
    "user": "slabbe"
}
```

Against sage-3.4.rc0



---

archive/issue_comments_042218.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-07T17:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5452#issuecomment-42218",
    "user": "slabbe"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042219.json:
```json
{
    "body": "Attachment [trac_5452.patch](tarball://root/attachments/some-uuid/ticket5452/trac_5452.patch) by slabbe created at 2009-03-07 17:18:36",
    "created_at": "2009-03-07T17:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5452#issuecomment-42219",
    "user": "slabbe"
}
```

Attachment [trac_5452.patch](tarball://root/attachments/some-uuid/ticket5452/trac_5452.patch) by slabbe created at 2009-03-07 17:18:36



---

archive/issue_comments_042220.json:
```json
{
    "body": "Must apply trac_5452.patch first.",
    "created_at": "2009-03-07T17:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5452#issuecomment-42220",
    "user": "slabbe"
}
```

Must apply trac_5452.patch first.



---

archive/issue_comments_042221.json:
```json
{
    "body": "Attachment [trac_5452_space_fix.patch](tarball://root/attachments/some-uuid/ticket5452/trac_5452_space_fix.patch) by rlm created at 2009-03-16 13:55:43\n\nHaven't tried testing since I'm about to get on a plane, but this patch looks straightforward enough to me.\n\n+1",
    "created_at": "2009-03-16T13:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5452#issuecomment-42221",
    "user": "rlm"
}
```

Attachment [trac_5452_space_fix.patch](tarball://root/attachments/some-uuid/ticket5452/trac_5452_space_fix.patch) by rlm created at 2009-03-16 13:55:43

Haven't tried testing since I'm about to get on a plane, but this patch looks straightforward enough to me.

+1



---

archive/issue_comments_042222.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.alpha0. Doctests do pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T20:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5452#issuecomment-42222",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.alpha0. Doctests do pass.

Cheers,

Michael



---

archive/issue_comments_042223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T20:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5452#issuecomment-42223",
    "user": "mabshoff"
}
```

Resolution: fixed
