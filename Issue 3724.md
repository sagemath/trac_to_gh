# Issue 3724: [with patch, depends on other ticket] faster hashs for Matrix_mod2_dense

archive/issues_003724.json:
```json
{
    "body": "Assignee: malb\n\nCC:  simonking\n\nKeywords: m4ri, hash, matrix\n\nSimon King requested faster hashing for matrices over GF(2). This patch implements it, but depends on #3324 and an updated M4RI.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3724\n\n",
    "created_at": "2008-07-25T12:08:04Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, depends on other ticket] faster hashs for Matrix_mod2_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3724",
    "user": "malb"
}
```
Assignee: malb

CC:  simonking

Keywords: m4ri, hash, matrix

Simon King requested faster hashing for matrices over GF(2). This patch implements it, but depends on #3324 and an updated M4RI.

Issue created by migration from https://trac.sagemath.org/ticket/3724





---

archive/issue_comments_026412.json:
```json
{
    "body": "implements faster hashing",
    "created_at": "2008-07-25T12:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26412",
    "user": "malb"
}
```

implements faster hashing



---

archive/issue_comments_026413.json:
```json
{
    "body": "Attachment [m4ri_hash.patch](tarball://root/attachments/some-uuid/ticket3724/m4ri_hash.patch) by malb created at 2008-08-06 16:32:32\n\nit seems, the patch is independent of the PNG fix.",
    "created_at": "2008-08-06T16:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26413",
    "user": "malb"
}
```

Attachment [m4ri_hash.patch](tarball://root/attachments/some-uuid/ticket3724/m4ri_hash.patch) by malb created at 2008-08-06 16:32:32

it seems, the patch is independent of the PNG fix.



---

archive/issue_comments_026414.json:
```json
{
    "body": "Simon, can you review my patch?",
    "created_at": "2008-08-24T12:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26414",
    "user": "malb"
}
```

Simon, can you review my patch?



---

archive/issue_comments_026415.json:
```json
{
    "body": "The patch applies to sage-3.1.1\n\nConsider a little test:\n\n```\nsage: M=MatrixSpace(GF(2),10000,10000).random_element()\nsage: M.set_immutable()\nsage: time M.__hash__()\n```\n\nWithout the patch, i had to interrupt sage after few *__minutes__* since it ate pretty much of my computer's memory. \n\nWith the patch, we get\n\n```\nsage: time M.__hash__()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n-2570088162955604276\n```\n\n\nWell done, Martin! I give a positive review.\n\nThe patch contains a doc-test. One problem for me: Typing `M.__hash__?`, i don't see them. What is the user supposed to do in order to see the doc-string of the respective hash method?\n\nI know that the following should be another ticket. But here are two items on my wish list:\n1. Can similar things be done with the hash of matrices over GF(p), p>2?\n2. Please also improve pickling of matrices! Example:\n {{{\nsage: M=MatrixSpace(GF(2),1000,1000).random_element()\nsage: timeit('x=loads(dumps(M))')\n5 loops, best of 3: 2.33 s per loop\n }}}\n which is somehow slowish.",
    "created_at": "2008-08-26T09:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26415",
    "user": "SimonKing"
}
```

The patch applies to sage-3.1.1

Consider a little test:

```
sage: M=MatrixSpace(GF(2),10000,10000).random_element()
sage: M.set_immutable()
sage: time M.__hash__()
```

Without the patch, i had to interrupt sage after few *__minutes__* since it ate pretty much of my computer's memory. 

With the patch, we get

```
sage: time M.__hash__()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
-2570088162955604276
```


Well done, Martin! I give a positive review.

The patch contains a doc-test. One problem for me: Typing `M.__hash__?`, i don't see them. What is the user supposed to do in order to see the doc-string of the respective hash method?

I know that the following should be another ticket. But here are two items on my wish list:
1. Can similar things be done with the hash of matrices over GF(p), p>2?
2. Please also improve pickling of matrices! Example:
 {{{
sage: M=MatrixSpace(GF(2),1000,1000).random_element()
sage: timeit('x=loads(dumps(M))')
5 loops, best of 3: 2.33 s per loop
 }}}
 which is somehow slowish.



---

archive/issue_comments_026416.json:
```json
{
    "body": "Simon,\n\nplease open a thread on sage-devel. I assume the discussion will conclude that speed up is warranted and then we can open tickets for the new issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T09:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26416",
    "user": "mabshoff"
}
```

Simon,

please open a thread on sage-devel. I assume the discussion will conclude that speed up is warranted and then we can open tickets for the new issues.

Cheers,

Michael



---

archive/issue_comments_026417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-26T09:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26417",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026418.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-26T09:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26418",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_026419.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n\n\n> The patch contains a doc-test. One problem for me: Typing `M.__hash__?`, i don't see them. What is the user supposed to do in order to see the doc-string of the respective hash method?\n\nThat could be a bug for introspection (or however that thingy is called). Could you open a ticket?\n \n>  1. Can similar things be done with the hash of matrices over GF(p), p>2?\n\nYes it can, please open a Trac ticket and I'll do it as soon as I find some time. \n\n>  2. Please also improve pickling of matrices! Example:\n>  {{{\n> sage: M=MatrixSpace(GF(2),1000,1000).random_element()\n> sage: timeit('x=loads(dumps(M))')\n> 5 loops, best of 3: 2.33 s per loop\n>  }}}\n>  which is somehow slowish.\n\nThat is #3324 which is blocked by a problem on OSX 10.4 and libpng.",
    "created_at": "2008-08-26T10:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26419",
    "user": "malb"
}
```

Replying to [comment:3 SimonKing]:


> The patch contains a doc-test. One problem for me: Typing `M.__hash__?`, i don't see them. What is the user supposed to do in order to see the doc-string of the respective hash method?

That could be a bug for introspection (or however that thingy is called). Could you open a ticket?
 
>  1. Can similar things be done with the hash of matrices over GF(p), p>2?

Yes it can, please open a Trac ticket and I'll do it as soon as I find some time. 

>  2. Please also improve pickling of matrices! Example:
>  {{{
> sage: M=MatrixSpace(GF(2),1000,1000).random_element()
> sage: timeit('x=loads(dumps(M))')
> 5 loops, best of 3: 2.33 s per loop
>  }}}
>  which is somehow slowish.

That is #3324 which is blocked by a problem on OSX 10.4 and libpng.



---

archive/issue_comments_026420.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-08-26T13:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26420",
    "user": "SimonKing"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_026421.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-08-26T13:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26421",
    "user": "SimonKing"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_026422.json:
```json
{
    "body": "Sorry, but i think i should re-open the ticket:\n\n```\nsage: M = MatrixSpace(GF(2),10000,10000).random_element()\nsage: M.is_mutable()\nTrue\nsage: M.__hash__()\n354973654957594997\n```\n\n\nA mutable object is not allowed to have a hash, AFAIK. \nOn the other hand, the hash-value seems not to be cached:\n\n```\nsage: M[0,0]\n1\nsage: M[0,0]=0\nsage: M.__hash__()\n-8868398381897180811\n```\n\n\nSo, the hash value has changed (i.e., was re-computed) by changing the matrix...\n\n```\nsage: N=copy(M)\nsage: N.__hash__()\n-8868398381897180811\n```\n\n... and has not changed by copying the matrix.\n\nBy consequence, it may be that everything is alright.\n\nHowever, I re-open the ticket, because I think this should be addressed -- either by a new patch raising an exception when `M` is mutable, or by the assertion that \"mutable objects have no hash\" is a rule but no law, and that it is fine since the hash is not cached.\n\nCheers\n     Simon",
    "created_at": "2008-08-26T13:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26422",
    "user": "SimonKing"
}
```

Sorry, but i think i should re-open the ticket:

```
sage: M = MatrixSpace(GF(2),10000,10000).random_element()
sage: M.is_mutable()
True
sage: M.__hash__()
354973654957594997
```


A mutable object is not allowed to have a hash, AFAIK. 
On the other hand, the hash-value seems not to be cached:

```
sage: M[0,0]
1
sage: M[0,0]=0
sage: M.__hash__()
-8868398381897180811
```


So, the hash value has changed (i.e., was re-computed) by changing the matrix...

```
sage: N=copy(M)
sage: N.__hash__()
-8868398381897180811
```

... and has not changed by copying the matrix.

By consequence, it may be that everything is alright.

However, I re-open the ticket, because I think this should be addressed -- either by a new patch raising an exception when `M` is mutable, or by the assertion that "mutable objects have no hash" is a rule but no law, and that it is fine since the hash is not cached.

Cheers
     Simon



---

archive/issue_comments_026423.json:
```json
{
    "body": "address review",
    "created_at": "2008-08-26T13:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26423",
    "user": "malb"
}
```

address review



---

archive/issue_comments_026424.json:
```json
{
    "body": "Attachment [m4ri_hash2.patch](tarball://root/attachments/some-uuid/ticket3724/m4ri_hash2.patch) by malb created at 2008-08-26 13:25:29\n\nYou're right, good catch. The attached patch addresses that issue.",
    "created_at": "2008-08-26T13:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26424",
    "user": "malb"
}
```

Attachment [m4ri_hash2.patch](tarball://root/attachments/some-uuid/ticket3724/m4ri_hash2.patch) by malb created at 2008-08-26 13:25:29

You're right, good catch. The attached patch addresses that issue.



---

archive/issue_comments_026425.json:
```json
{
    "body": "m4ri_hash2.patch looks good to me. Positive review.",
    "created_at": "2008-08-26T16:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26425",
    "user": "mabshoff"
}
```

m4ri_hash2.patch looks good to me. Positive review.



---

archive/issue_comments_026426.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-26T21:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26426",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026427.json:
```json
{
    "body": "Merged m4ri_hash2.patch in Sage 3.1.2.alpha1",
    "created_at": "2008-08-26T21:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26427",
    "user": "mabshoff"
}
```

Merged m4ri_hash2.patch in Sage 3.1.2.alpha1



---

archive/issue_comments_026428.json:
```json
{
    "body": "The new hash-ing method does not obey Sage's hashing rules. See Robert's comment at #3956. Obeying this rule however would come with a considerable speed penalty compared to `m4ri_hash.patch`.",
    "created_at": "2008-08-27T16:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26428",
    "user": "malb"
}
```

The new hash-ing method does not obey Sage's hashing rules. See Robert's comment at #3956. Obeying this rule however would come with a considerable speed penalty compared to `m4ri_hash.patch`.



---

archive/issue_comments_026429.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-08-27T16:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26429",
    "user": "malb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_026430.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-08-27T16:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26430",
    "user": "malb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_026431.json:
```json
{
    "body": "Martin,\n\ncan we move the latest issue to a new ticket? As is this ticket is getting rather messy, i.e. in HISTORY.txt as well as here.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T19:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26431",
    "user": "mabshoff"
}
```

Martin,

can we move the latest issue to a new ticket? As is this ticket is getting rather messy, i.e. in HISTORY.txt as well as here.

Cheers,

Michael



---

archive/issue_comments_026432.json:
```json
{
    "body": "your wish is my command.",
    "created_at": "2008-08-27T19:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26432",
    "user": "malb"
}
```

your wish is my command.



---

archive/issue_comments_026433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T19:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3724#issuecomment-26433",
    "user": "malb"
}
```

Resolution: fixed
