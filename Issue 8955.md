# Issue 8955: random_matrix(GF(2),2,1) always returns all 1 matrix

archive/issues_008955.json:
```json
{
    "body": "Assignee: jason, was\n\nReported by Roberto N\u00f3brega on [sage-devel]:\n\n```\nHello, all!\n\nAfter running\n\nrandom_matrix(GF(2), 2, 1)\n\nI always get the same matrix, [[1][1]].\n\nAlso, the following code\n\nfreq = {}\nfor _ in range(1000):\n    M = random_matrix(GF(2), 2, 2)\n    M.set_immutable()\n    if M not in freq:\n        freq[M] = 1\n    else:\n        freq[M] += 1\nshow(freq)\n\ngives a very different result from the uniform distribution that I was\nexpecting. For example, the all-ones 2x2 matrix is the more probable,\nand matrices with a full-zero-row does not appear, although matrices\nwith a full-zero-column does. In general, I noticed that the more\n\"1's\" the matrix has, the more probable it is.\n\nAm I missing something?\n\nRegards,\nRoberto.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8955\n\n",
    "created_at": "2010-05-12T10:44:22Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "random_matrix(GF(2),2,1) always returns all 1 matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8955",
    "user": "@malb"
}
```
Assignee: jason, was

Reported by Roberto Nóbrega on [sage-devel]:

```
Hello, all!

After running

random_matrix(GF(2), 2, 1)

I always get the same matrix, [[1][1]].

Also, the following code

freq = {}
for _ in range(1000):
    M = random_matrix(GF(2), 2, 2)
    M.set_immutable()
    if M not in freq:
        freq[M] = 1
    else:
        freq[M] += 1
show(freq)

gives a very different result from the uniform distribution that I was
expecting. For example, the all-ones 2x2 matrix is the more probable,
and matrices with a full-zero-row does not appear, although matrices
with a full-zero-column does. In general, I noticed that the more
"1's" the matrix has, the more probable it is.

Am I missing something?

Regards,
Roberto.
```


Issue created by migration from https://trac.sagemath.org/ticket/8955





---

archive/issue_comments_082532.json:
```json
{
    "body": "What is the status of this?",
    "created_at": "2010-08-15T20:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82532",
    "user": "ylchapuy"
}
```

What is the status of this?



---

archive/issue_comments_082533.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-15T20:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82533",
    "user": "@malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082534.json:
```json
{
    "body": "I always forget to toggle the right status.",
    "created_at": "2010-08-15T20:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82534",
    "user": "@malb"
}
```

I always forget to toggle the right status.



---

archive/issue_comments_082535.json:
```json
{
    "body": "I agree with the proposed solution, but I think there should be some explanations in the docstring about what `density` means exactly.\nSeeing \n\n```\ndef random_matrix(R, nrows, ncols=None, sparse=False, density=None, *args, **kwds):\n    ...\n    - ``density``: Integer (default: 1)\n    ...\n```\n\nseems strange to me.",
    "created_at": "2010-08-15T20:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82535",
    "user": "ylchapuy"
}
```

I agree with the proposed solution, but I think there should be some explanations in the docstring about what `density` means exactly.
Seeing 

```
def random_matrix(R, nrows, ncols=None, sparse=False, density=None, *args, **kwds):
    ...
    - ``density``: Integer (default: 1)
    ...
```

seems strange to me.



---

archive/issue_comments_082536.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-15T20:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82536",
    "user": "ylchapuy"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082537.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-15T21:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82537",
    "user": "@malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082538.json:
```json
{
    "body": "I've updated the patch accordingly (and added the ticket number)",
    "created_at": "2010-08-15T21:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82538",
    "user": "@malb"
}
```

I've updated the patch accordingly (and added the ticket number)



---

archive/issue_comments_082539.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-15T21:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82539",
    "user": "ylchapuy"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082540.json:
```json
{
    "body": "Hum, I don't think it's ok now...\nMy understanding is that:\n\n* we should stare that default is None\n* we should explain that in this case each element is random and **can be 0**\n* if a density is given, it's the rate of **nonzero** element (thus for GF(2) a density of 1 means an all 1 matrix)\n* by the way, density should be float, not Integer, or?",
    "created_at": "2010-08-15T21:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82540",
    "user": "ylchapuy"
}
```

Hum, I don't think it's ok now...
My understanding is that:

* we should stare that default is None
* we should explain that in this case each element is random and **can be 0**
* if a density is given, it's the rate of **nonzero** element (thus for GF(2) a density of 1 means an all 1 matrix)
* by the way, density should be float, not Integer, or?



---

archive/issue_comments_082541.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-16T14:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82541",
    "user": "@malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082542.json:
```json
{
    "body": "I've updated the attached patch\n\n* fixed the docstring as requested\n* fixed the behaviour of randomize() for dense matrices over GF(2)\u00a0\n* fixed some docstrings on the way\n\nThe patch depends on#9475.",
    "created_at": "2010-08-16T14:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82542",
    "user": "@malb"
}
```

I've updated the attached patch

* fixed the docstring as requested
* fixed the behaviour of randomize() for dense matrices over GF(2) 
* fixed some docstrings on the way

The patch depends on#9475.



---

archive/issue_comments_082543.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-16T15:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82543",
    "user": "@malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082544.json:
```json
{
    "body": "There are some doctest failures due to changes of random matrix generation",
    "created_at": "2010-08-16T15:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82544",
    "user": "@malb"
}
```

There are some doctest failures due to changes of random matrix generation



---

archive/issue_comments_082545.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-16T15:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82545",
    "user": "@malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082546.json:
```json
{
    "body": "I fixed all known doctest failures. It would be good if this patch was reviewed & applied quickly since it is the kind of patch which will bitrot quickly since it touches quite a few files.",
    "created_at": "2010-08-16T15:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82546",
    "user": "@malb"
}
```

I fixed all known doctest failures. It would be good if this patch was reviewed & applied quickly since it is the kind of patch which will bitrot quickly since it touches quite a few files.



---

archive/issue_comments_082547.json:
```json
{
    "body": "I added a minimal reviewer's patch. Otherwise, everything is fine, applies with minimal fuzz to sage4.5.3.alpha1, all doctests pass. Ok for merging.",
    "created_at": "2010-08-18T11:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82547",
    "user": "ylchapuy"
}
```

I added a minimal reviewer's patch. Otherwise, everything is fine, applies with minimal fuzz to sage4.5.3.alpha1, all doctests pass. Ok for merging.



---

archive/issue_comments_082548.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-18T11:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82548",
    "user": "ylchapuy"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082549.json:
```json
{
    "body": "The reviewer patch is fine by me too.",
    "created_at": "2010-08-18T11:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82549",
    "user": "@malb"
}
```

The reviewer patch is fine by me too.



---

archive/issue_comments_082550.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-18T07:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82550",
    "user": "@qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082551.json:
```json
{
    "body": "Could someone rebase the patch(es) here against 4.6.alpha1 when it's released (soon) and restore the positive review?",
    "created_at": "2010-09-18T07:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82551",
    "user": "@qed777"
}
```

Could someone rebase the patch(es) here against 4.6.alpha1 when it's released (soon) and restore the positive review?



---

archive/issue_comments_082552.json:
```json
{
    "body": "Attachment [random_matrix.patch](tarball://root/attachments/some-uuid/ticket8955/random_matrix.patch) by @malb created at 2010-09-20 15:52:26",
    "created_at": "2010-09-20T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82552",
    "user": "@malb"
}
```

Attachment [random_matrix.patch](tarball://root/attachments/some-uuid/ticket8955/random_matrix.patch) by @malb created at 2010-09-20 15:52:26



---

archive/issue_comments_082553.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-20T15:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82553",
    "user": "@malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082554.json:
```json
{
    "body": "The updated patch is rebased to 4.6.alpha1. Apply `random_matrix.patch` only.",
    "created_at": "2010-09-20T15:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82554",
    "user": "@malb"
}
```

The updated patch is rebased to 4.6.alpha1. Apply `random_matrix.patch` only.



---

archive/issue_comments_082555.json:
```json
{
    "body": "malb: based on the comment above, should you restore the positive review?",
    "created_at": "2010-09-23T23:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82555",
    "user": "@jasongrout"
}
```

malb: based on the comment above, should you restore the positive review?



---

archive/issue_comments_082556.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-27T14:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82556",
    "user": "ylchapuy"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082557.json:
```json
{
    "body": "Attachment [8955_review.patch](tarball://root/attachments/some-uuid/ticket8955/8955_review.patch) by ylchapuy created at 2010-09-27 14:28:36\n\nReviewer's patch also updated ;)\nPositive review. (I'm quite sure malb will confirm)",
    "created_at": "2010-09-27T14:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82557",
    "user": "ylchapuy"
}
```

Attachment [8955_review.patch](tarball://root/attachments/some-uuid/ticket8955/8955_review.patch) by ylchapuy created at 2010-09-27 14:28:36

Reviewer's patch also updated ;)
Positive review. (I'm quite sure malb will confirm)



---

archive/issue_comments_082558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8955#issuecomment-82558",
    "user": "@qed777"
}
```

Resolution: fixed
