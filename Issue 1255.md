# Issue 1255: bug in permutation_automorphism_group

archive/issues_001255.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nI have found a code C which crashes C.permutation_automorphism_group().\nThis function basically is a wrapper for GAP's `MatrixAutomorphisms` \nfunction. The code that causes it to fail is [20,14] in\nhttp://sage.math.washington.edu/home/wdj/research/coding-theory/sd_codes.sage\n\nIssue created by migration from https://trac.sagemath.org/ticket/1255\n\n",
    "created_at": "2007-11-24T19:33:26Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in permutation_automorphism_group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1255",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @wdjoyner

I have found a code C which crashes C.permutation_automorphism_group().
This function basically is a wrapper for GAP's `MatrixAutomorphisms` 
function. The code that causes it to fail is [20,14] in
http://sage.math.washington.edu/home/wdj/research/coding-theory/sd_codes.sage

Issue created by migration from https://trac.sagemath.org/ticket/1255





---

archive/issue_comments_007822.json:
```json
{
    "body": "Is this a bug in gap?  If so, make a Gap-only session that replicates it and report it to the Gap list asap.",
    "created_at": "2007-11-25T18:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1255#issuecomment-7822",
    "user": "https://github.com/williamstein"
}
```

Is this a bug in gap?  If so, make a Gap-only session that replicates it and report it to the Gap list asap.



---

archive/issue_comments_007823.json:
```json
{
    "body": "We are having trouble replicating this -- what hardware / os are you using?",
    "created_at": "2007-11-25T18:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1255#issuecomment-7823",
    "user": "https://github.com/williamstein"
}
```

We are having trouble replicating this -- what hardware / os are you using?



---

archive/issue_comments_007824.json:
```json
{
    "body": "This definitely doesn't seem valid anymore:\n\n```\nsage: load /Users/rlmill/Desktop/sd_codes.sage\nsage: time L = self_dual_codes(20)\nCPU times: user 2.09 s, sys: 0.83 s, total: 2.92 s\nWall time: 3.10\nsage: C = L[14][0]; C\nLinear code of length 19, dimension 10 over Finite Field of size 2\nsage: C.permutation_automorphism_group()\nPermutation Group with generators [(10,19), (9,15)(16,17), (9,16)(15,17), (8,9)(17,18), (7,8)(16,17), (4,5)(13,14), (4,13)(5,14), (3,4)(12,14), (1,2)(5,13), (1,3)(2,12)]\n```\n",
    "created_at": "2008-05-10T21:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1255#issuecomment-7824",
    "user": "https://github.com/rlmill"
}
```

This definitely doesn't seem valid anymore:

```
sage: load /Users/rlmill/Desktop/sd_codes.sage
sage: time L = self_dual_codes(20)
CPU times: user 2.09 s, sys: 0.83 s, total: 2.92 s
Wall time: 3.10
sage: C = L[14][0]; C
Linear code of length 19, dimension 10 over Finite Field of size 2
sage: C.permutation_automorphism_group()
Permutation Group with generators [(10,19), (9,15)(16,17), (9,16)(15,17), (8,9)(17,18), (7,8)(16,17), (4,5)(13,14), (4,13)(5,14), (3,4)(12,14), (1,2)(5,13), (1,3)(2,12)]
```




---

archive/issue_comments_007825.json:
```json
{
    "body": "In fact, none of the codes from that function cause a \"crash\":\n\n```\nsage: for n in range(24):\n....:     for C in self_dual_codes(n):\n....:         G = C[0].permutation_automorphism_group()\n....:         \nsage: \n```\n",
    "created_at": "2008-05-10T21:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1255#issuecomment-7825",
    "user": "https://github.com/rlmill"
}
```

In fact, none of the codes from that function cause a "crash":

```
sage: for n in range(24):
....:     for C in self_dual_codes(n):
....:         G = C[0].permutation_automorphism_group()
....:         
sage: 
```




---

archive/issue_comments_007826.json:
```json
{
    "body": "David also says that he cannot reproduce the crash.",
    "created_at": "2008-05-11T02:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1255#issuecomment-7826",
    "user": "https://github.com/rlmill"
}
```

David also says that he cannot reproduce the crash.



---

archive/issue_events_001397.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-31T04:25:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1255#event-1397"
}
```



---

archive/issue_comments_007827.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-31T04:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1255#issuecomment-7827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_007828.json:
```json
{
    "body": "Invalid.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-31T04:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1255#issuecomment-7828",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Invalid.

Cheers,

Michael
