# Issue 1746: add p-norm as a method to vectors (probably very easy)

archive/issues_001746.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n\n\nOn Jan 10, 2008 12:17 AM, vgermrk <vgermrk@googlemail.com> wrote:\n> \n> [Sorry for asking so much \"Is there a ... function in Sage?\" -\n> Questions.]\n> \n> But: Is there a native way to compute the p-Norm (e.g. euclidean oder\n> maximum norm) of a vector?\n> \n\nThere is no built in function, but we can write one easily:\n\ndef pnorm(v, p):\n      return sum([a^p for a in v])^(1/p)\n\n\nThen:\n\nsage: pnorm(vector([1,2,3]), 5)\n276^(1/5)\nsage: pnorm(vector(RDF, [1,2,3]), 5)\n3.07738488539\nsage: var('a b c d p')\nsage: pnorm(vector([a, b, c, d]), p)\n(d^p + c^p + b^p + a^p)^(1/p)\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1746\n\n",
    "created_at": "2008-01-10T10:44:22Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "add p-norm as a method to vectors (probably very easy)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1746",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```


On Jan 10, 2008 12:17 AM, vgermrk <vgermrk@googlemail.com> wrote:
> 
> [Sorry for asking so much "Is there a ... function in Sage?" -
> Questions.]
> 
> But: Is there a native way to compute the p-Norm (e.g. euclidean oder
> maximum norm) of a vector?
> 

There is no built in function, but we can write one easily:

def pnorm(v, p):
      return sum([a^p for a in v])^(1/p)


Then:

sage: pnorm(vector([1,2,3]), 5)
276^(1/5)
sage: pnorm(vector(RDF, [1,2,3]), 5)
3.07738488539
sage: var('a b c d p')
sage: pnorm(vector([a, b, c, d]), p)
(d^p + c^p + b^p + a^p)^(1/p)

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/1746





---

archive/issue_comments_010997.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-01-10T10:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-10997",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_010998.json:
```json
{
    "body": "for RDF and CDF vectors\n\n```\nfrom numpy import linalg\nv=vector(RDF,[1,2,3])\nlinalg.norm(v,5)\n```\n\n3.0773848853940629",
    "created_at": "2008-01-10T10:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-10998",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

for RDF and CDF vectors

```
from numpy import linalg
v=vector(RDF,[1,2,3])
linalg.norm(v,5)
```

3.0773848853940629



---

archive/issue_comments_010999.json:
```json
{
    "body": "In the above example it should be \n\n`linalg.norm(v.numpy(),5)`",
    "created_at": "2008-01-10T10:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-10999",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

In the above example it should be 

`linalg.norm(v.numpy(),5)`



---

archive/issue_events_004225.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2008-01-10T15:05:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1746#event-4225"
}
```



---

archive/issue_comments_011000.json:
```json
{
    "body": "Attachment [1746.patch](tarball://root/attachments/some-uuid/ticket1746/1746.patch) by @aghitza created at 2008-01-10 15:05:33",
    "created_at": "2008-01-10T15:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-11000",
    "user": "https://github.com/aghitza"
}
```

Attachment [1746.patch](tarball://root/attachments/some-uuid/ticket1746/1746.patch) by @aghitza created at 2008-01-10 15:05:33



---

archive/issue_comments_011001.json:
```json
{
    "body": "does this also work for matrices? matrix norms are at least equally important!",
    "created_at": "2008-01-11T21:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-11001",
    "user": "https://github.com/haraldschilly"
}
```

does this also work for matrices? matrix norms are at least equally important!



---

archive/issue_comments_011002.json:
```json
{
    "body": "What is the defn of matrix p-norms?  Is it the same?",
    "created_at": "2008-01-11T21:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-11002",
    "user": "https://github.com/williamstein"
}
```

What is the defn of matrix p-norms?  Is it the same?



---

archive/issue_comments_011003.json:
```json
{
    "body": "I agree that matrix norms are important.  However, unlike the case of vectors, where the p-norm is rather universally agreed upon, there are a bunch of different definitions for norms on matrices, see\nhttp://en.wikipedia.org/wiki/Matrix_norm\nThere are at least 3 different things denoted as p-norm there.\n\nI think it's important for us to do this, but trickier than the vector case, so I've made it into track #1763.\n\nIn the meantime, it would be great if someone reviewed the current patch.",
    "created_at": "2008-01-12T09:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-11003",
    "user": "https://github.com/aghitza"
}
```

I agree that matrix norms are important.  However, unlike the case of vectors, where the p-norm is rather universally agreed upon, there are a bunch of different definitions for norms on matrices, see
http://en.wikipedia.org/wiki/Matrix_norm
There are at least 3 different things denoted as p-norm there.

I think it's important for us to do this, but trickier than the vector case, so I've made it into track #1763.

In the meantime, it would be great if someone reviewed the current patch.



---

archive/issue_comments_011004.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T00:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-11004",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_comments_011005.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T00:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1746#issuecomment-11005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004226.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-20T00:51:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1746",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1746#event-4226"
}
```
