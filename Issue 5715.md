# Issue 5715: [with patch, needs review] show subdivisions for matrices over GF(2)

archive/issues_005715.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nSince `matrix_mod2_dense` defines its own `str` function, it overrides the function for general matrices, so for dense matrices over GF(2), subdivisions are not printed.  (See [this discussion](http://groups.google.com/group/sage-support/browse_frm/thread/a08df4717024f9c0).)\n\nThis patch deletes the `str` method for dense matrices over GF(2).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5715\n\n",
    "created_at": "2009-04-08T19:17:10Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] show subdivisions for matrices over GF(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5715",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Since `matrix_mod2_dense` defines its own `str` function, it overrides the function for general matrices, so for dense matrices over GF(2), subdivisions are not printed.  (See [this discussion](http://groups.google.com/group/sage-support/browse_frm/thread/a08df4717024f9c0).)

This patch deletes the `str` method for dense matrices over GF(2).

Issue created by migration from https://trac.sagemath.org/ticket/5715





---

archive/issue_events_005957.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2009-04-08T19:24:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5715#event-5957"
}
```



---

archive/issue_comments_044573.json:
```json
{
    "body": "Attachment [5715-subdivisions.patch](tarball://root/attachments/some-uuid/ticket5715/5715-subdivisions.patch) by @jhpalmieri created at 2009-04-08 19:24:40\n\nThis is a duplicate of #5714.",
    "created_at": "2009-04-08T19:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44573",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5715-subdivisions.patch](tarball://root/attachments/some-uuid/ticket5715/5715-subdivisions.patch) by @jhpalmieri created at 2009-04-08 19:24:40

This is a duplicate of #5714.



---

archive/issue_comments_044574.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-08T19:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44574",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: duplicate



---

archive/issue_comments_044575.json:
```json
{
    "body": "Needs work.  There is a *very good* reason that there is a str method for GF(2) -- it's for speed!  Check this out:\n\n```\nBEFORE YOUR PATCH:\nsage: a = random_matrix(GF(2),1000)\nsage: time b = a.str()\nCPU times: user 0.41 s, sys: 0.01 s, total: 0.42 s\nWall time: 0.42 s\n```\n\n\n```\nAFTER YOUR PATCH:\nsage: a = random_matrix(GF(2),1000)\nsage: time b = a.str()\nCPU times: user 5.02 s, sys: 0.86 s, total: 5.88 s\nWall time: 5.89 s\n```\n",
    "created_at": "2009-04-08T19:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44575",
    "user": "https://github.com/williamstein"
}
```

Needs work.  There is a *very good* reason that there is a str method for GF(2) -- it's for speed!  Check this out:

```
BEFORE YOUR PATCH:
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 0.41 s, sys: 0.01 s, total: 0.42 s
Wall time: 0.42 s
```


```
AFTER YOUR PATCH:
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 5.02 s, sys: 0.86 s, total: 5.88 s
Wall time: 5.89 s
```




---

archive/issue_comments_044576.json:
```json
{
    "body": "Attachment [5715-mat2-subdiv.patch](tarball://root/attachments/some-uuid/ticket5715/5715-mat2-subdiv.patch) by @robertwb created at 2009-04-09 07:21:46\n\napply only this patch",
    "created_at": "2009-04-09T07:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44576",
    "user": "https://github.com/robertwb"
}
```

Attachment [5715-mat2-subdiv.patch](tarball://root/attachments/some-uuid/ticket5715/5715-mat2-subdiv.patch) by @robertwb created at 2009-04-09 07:21:46

apply only this patch



---

archive/issue_comments_044577.json:
```json
{
    "body": "I posted a new patch that handles subdivisions. I went ahead and sped up the str method while I was there too. \n\nBefore\n\n```\nsage: a = random_matrix(GF(2),1000)\nsage: time b = a.str()\nCPU times: user 0.48 s, sys: 0.01 s, total: 0.49 s\nWall time: 0.50 s\n```\n\n\nAfter\n\n```\nsage: a = random_matrix(GF(2),1000)\nsage: time b = a.str()\nCPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s\nWall time: 0.02 s\n```\n",
    "created_at": "2009-04-09T07:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44577",
    "user": "https://github.com/robertwb"
}
```

I posted a new patch that handles subdivisions. I went ahead and sped up the str method while I was there too. 

Before

```
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 0.48 s, sys: 0.01 s, total: 0.49 s
Wall time: 0.50 s
```


After

```
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s
Wall time: 0.02 s
```




---

archive/issue_comments_044578.json:
```json
{
    "body": "Hmm, shouldn't this patch be reopened or maybe go to another ticket? We need to do one thing since this patch is currently closed as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T09:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, shouldn't this patch be reopened or maybe go to another ticket? We need to do one thing since this patch is currently closed as a dupe.

Cheers,

Michael



---

archive/issue_comments_044579.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2009-04-09T10:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44579",
    "user": "https://github.com/robertwb"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_044580.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-04-09T10:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44580",
    "user": "https://github.com/robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_events_005958.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2009-04-09T10:40:29Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5715#event-5958"
}
```



---

archive/issue_comments_044581.json:
```json
{
    "body": "I just reopened this ticket, as it seems to have the most activity.",
    "created_at": "2009-04-09T10:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44581",
    "user": "https://github.com/robertwb"
}
```

I just reopened this ticket, as it seems to have the most activity.



---

archive/issue_comments_044582.json:
```json
{
    "body": "Looks good, passes all tests when applied to 3.4.1.rc2.  Also fast, as robertwb pointed out above.\n\nA question: how do you tell if a sparse matrix is too big to be converted to a dense one?  If we have a sparse mod 2 matrix, should we consider printing it by converting to a dense one and using this routine?  For a 1000x1000 random matrix, converting and using this one was about 5 times faster than just printing it.  (If this is a good idea, then it belongs in a different ticket, but I don't know if this is a good idea...)",
    "created_at": "2009-04-13T00:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44582",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good, passes all tests when applied to 3.4.1.rc2.  Also fast, as robertwb pointed out above.

A question: how do you tell if a sparse matrix is too big to be converted to a dense one?  If we have a sparse mod 2 matrix, should we consider printing it by converting to a dense one and using this routine?  For a 1000x1000 random matrix, converting and using this one was about 5 times faster than just printing it.  (If this is a good idea, then it belongs in a different ticket, but I don't know if this is a good idea...)



---

archive/issue_comments_044583.json:
```json
{
    "body": "Merged 5715-mat2-subdiv.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T09:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44583",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 5715-mat2-subdiv.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_events_005959.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-13T09:13:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5715#event-5959"
}
```



---

archive/issue_comments_044584.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T09:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44584",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044585.json:
```json
{
    "body": "How big is too big is an interesting question, but too big to convert > to big to print. Probably should be a separate ticket, but the optimizer in me sees an even easier way: create the zero matrix doing \"[0 0 ... 0]\" * nrows, then set the 1 entries. This wouldn't of course handle subdivisons though, but could be easily adapted to do so the same way as this code.",
    "created_at": "2009-04-14T02:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5715#issuecomment-44585",
    "user": "https://github.com/robertwb"
}
```

How big is too big is an interesting question, but too big to convert > to big to print. Probably should be a separate ticket, but the optimizer in me sees an even easier way: create the zero matrix doing "[0 0 ... 0]" * nrows, then set the 1 entries. This wouldn't of course handle subdivisons though, but could be easily adapted to do so the same way as this code.
