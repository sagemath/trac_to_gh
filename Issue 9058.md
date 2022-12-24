# Issue 9058: Compute cores to improve subgraph_search

archive/issues_009058.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  mvngu\n\nIf one is looking for H in G, then we may assume the minimum degree of G is larger than the minimum degree of H. We can assume the same for the complement when computing an induced subgraph. Take care of directed graphs.\n\nrequires #8922\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9058\n\n",
    "created_at": "2010-05-26T22:30:27Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Compute cores to improve subgraph_search",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9058",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  mvngu

If one is looking for H in G, then we may assume the minimum degree of G is larger than the minimum degree of H. We can assume the same for the complement when computing an induced subgraph. Take care of directed graphs.

requires #8922

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9058





---

archive/issue_comments_084046.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84046",
    "user": "ncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084047.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-02T15:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84047",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084048.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-06T12:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84048",
    "user": "lsampaio"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084049.json:
```json
{
    "body": "Attachment [trac_9058.patch](tarball://root/attachments/some-uuid/ticket9058/trac_9058.patch) by lsampaio created at 2010-10-06 12:48:59\n\nI verified the patch and I believe it is ok to be merged.",
    "created_at": "2010-10-06T12:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84049",
    "user": "lsampaio"
}
```

Attachment [trac_9058.patch](tarball://root/attachments/some-uuid/ticket9058/trac_9058.patch) by lsampaio created at 2010-10-06 12:48:59

I verified the patch and I believe it is ok to be merged.



---

archive/issue_comments_084050.json:
```json
{
    "body": "cool ! Thanks `;-)`\n\nNathann",
    "created_at": "2010-10-06T12:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84050",
    "user": "ncohen"
}
```

cool ! Thanks `;-)`

Nathann



---

archive/issue_comments_084051.json:
```json
{
    "body": "Don't forget to update the author and reviewer fields.  lsampaio, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?",
    "created_at": "2010-10-08T21:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84051",
    "user": "mpatel"
}
```

Don't forget to update the author and reviewer fields.  lsampaio, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?



---

archive/issue_comments_084052.json:
```json
{
    "body": "ok, I did it =)\nthank you for pointing this!",
    "created_at": "2010-10-08T21:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84052",
    "user": "lsampaio"
}
```

ok, I did it =)
thank you for pointing this!



---

archive/issue_comments_084053.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-08T22:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-84053",
    "user": "mpatel"
}
```

Resolution: fixed
