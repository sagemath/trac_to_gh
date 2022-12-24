# Issue 8676: document breadth-first and depth-first search methods of C graph

archive/issues_008676.json:
```json
{
    "body": "Assignee: mvngu\n\nAs the subject says. Also make sure to cross-reference the DFS and BFS of C graph and generic graph implementations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8676\n\n",
    "created_at": "2010-04-12T06:51:44Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "document breadth-first and depth-first search methods of C graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8676",
    "user": "mvngu"
}
```
Assignee: mvngu

As the subject says. Also make sure to cross-reference the DFS and BFS of C graph and generic graph implementations.

Issue created by migration from https://trac.sagemath.org/ticket/8676





---

archive/issue_comments_078953.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-12T06:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78953",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078954.json:
```json
{
    "body": "Hello !!!\n\nI'm halfway through the review of this patch, and I have two remarks :\n\n* It may be a mistale from my part, but even though I can see you added generic_graph to the .rst file, I do not see it in the reference manual even though I can see your updates to the c_graph documentation.\n\n* path #8513 already adds this line, so your patch may have to be rebased on this one. I do not know whether the other modifications of #8513 could create conflicts, by the way\n\nReviewing your patches remains my preferred way of learning how to use Sage/Sphinx ;-)\n\nNathann",
    "created_at": "2010-04-12T08:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78954",
    "user": "ncohen"
}
```

Hello !!!

I'm halfway through the review of this patch, and I have two remarks :

* It may be a mistale from my part, but even though I can see you added generic_graph to the .rst file, I do not see it in the reference manual even though I can see your updates to the c_graph documentation.

* path #8513 already adds this line, so your patch may have to be rebased on this one. I do not know whether the other modifications of #8513 could create conflicts, by the way

Reviewing your patches remains my preferred way of learning how to use Sage/Sphinx ;-)

Nathann



---

archive/issue_comments_078955.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-04-12T08:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78955",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_078956.json:
```json
{
    "body": "Attachment [trac_8676-document-cgraph.patch](tarball://root/attachments/some-uuid/ticket8676/trac_8676-document-cgraph.patch) by mvngu created at 2010-04-13 00:54:00\n\nbased on Sage 4.3.5; require #8513",
    "created_at": "2010-04-13T00:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78956",
    "user": "mvngu"
}
```

Attachment [trac_8676-document-cgraph.patch](tarball://root/attachments/some-uuid/ticket8676/trac_8676-document-cgraph.patch) by mvngu created at 2010-04-13 00:54:00

based on Sage 4.3.5; require #8513



---

archive/issue_comments_078957.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n>  * It may be a mistale from my part, but even though I can see you added generic_graph to the .rst file, I do not see it in the reference manual even though I can see your updates to the c_graph documentation.\n\nThis usually happens. What I would do is this. Take the latest Sage version, e.g. the binary version of Sage 4.3.5, and delete the `output` directory:\n\n```\nrm -rf SAGE_ROOT/devel/sage-main/doc/output/\n```\n\nThen apply necessary patches. When all such patches apply without problems, rebuild the reference manual, or indeed the whole Sage documentation.\n\n\n\n\n\n>  * path #8513 already adds this line, so your patch may have to be rebased on this one. I do not know whether the other modifications of #8513 could create conflicts, by the way\n\nI have rebased my patch on top of those at #8513. So now apply patches in this order:\n\n1. #8513\n2. [trac_8676-document-cgraph.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8676/trac_8676-document-cgraph.patch)",
    "created_at": "2010-04-13T01:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78957",
    "user": "mvngu"
}
```

Replying to [comment:2 ncohen]:
>  * It may be a mistale from my part, but even though I can see you added generic_graph to the .rst file, I do not see it in the reference manual even though I can see your updates to the c_graph documentation.

This usually happens. What I would do is this. Take the latest Sage version, e.g. the binary version of Sage 4.3.5, and delete the `output` directory:

```
rm -rf SAGE_ROOT/devel/sage-main/doc/output/
```

Then apply necessary patches. When all such patches apply without problems, rebuild the reference manual, or indeed the whole Sage documentation.





>  * path #8513 already adds this line, so your patch may have to be rebased on this one. I do not know whether the other modifications of #8513 could create conflicts, by the way

I have rebased my patch on top of those at #8513. So now apply patches in this order:

1. #8513
2. [trac_8676-document-cgraph.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8676/trac_8676-document-cgraph.patch)



---

archive/issue_comments_078958.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-04-13T01:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78958",
    "user": "mvngu"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_078959.json:
```json
{
    "body": "Yet another of Minh's patches. \n\nNo mistake that I could notice, the patches are nicely imported, no warning of any kind during the generation of the documentation, the touched files pass all tests, and I learned new ways to use Sphynx. Positive review, and thank you again for your work ! :-)\n\nNathann",
    "created_at": "2010-04-14T11:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78959",
    "user": "ncohen"
}
```

Yet another of Minh's patches. 

No mistake that I could notice, the patches are nicely imported, no warning of any kind during the generation of the documentation, the touched files pass all tests, and I learned new ways to use Sphynx. Positive review, and thank you again for your work ! :-)

Nathann



---

archive/issue_comments_078960.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-14T11:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78960",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078961.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78961",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_078962.json:
```json
{
    "body": "Merged \"trac_8676-document-cgraph.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8676#issuecomment-78962",
    "user": "jhpalmieri"
}
```

Merged "trac_8676-document-cgraph.patch" in 4.4.alpha0.
