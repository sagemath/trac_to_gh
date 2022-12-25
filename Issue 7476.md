# Issue 7476: Edge-disjoint spanning trees

archive/issues_007476.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\nThe theorem from Nash-Williams on the existence of k edge-disjoint spanning trees in a graph is both important, useful, and polynomial to compute. This could be implemented using the short proof described in the following article :\n\nhttp://arxiv.org/abs/0911.2809\n\nOr, if we achieve to eventually define in Sage a class Matroid, this could be done through the Matroid Union Theorem as presented in Schrijver's book.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7476\n\n",
    "created_at": "2009-11-17T06:11:37Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Edge-disjoint spanning trees",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7476",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  @jasongrout

The theorem from Nash-Williams on the existence of k edge-disjoint spanning trees in a graph is both important, useful, and polynomial to compute. This could be implemented using the short proof described in the following article :

http://arxiv.org/abs/0911.2809

Or, if we achieve to eventually define in Sage a class Matroid, this could be done through the Matroid Union Theorem as presented in Schrijver's book.

Issue created by migration from https://trac.sagemath.org/ticket/7476





---

archive/issue_comments_062892.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T10:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62892",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062893.json:
```json
{
    "body": "Finally, it was pretty quick to do it through LP :-)\n\nNathann",
    "created_at": "2010-02-23T10:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62893",
    "user": "https://github.com/nathanncohen"
}
```

Finally, it was pretty quick to do it through LP :-)

Nathann



---

archive/issue_comments_062894.json:
```json
{
    "body": "For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/\n\nNathann",
    "created_at": "2010-04-08T21:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62894",
    "user": "https://github.com/nathanncohen"
}
```

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann



---

archive/issue_comments_062895.json:
```json
{
    "body": "Patch rebased on top of #7608 !",
    "created_at": "2010-04-23T11:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62895",
    "user": "https://github.com/nathanncohen"
}
```

Patch rebased on top of #7608 !



---

archive/issue_comments_062896.json:
```json
{
    "body": "I'd much rather see the algorithm in the paper implemented, especially if it's polynomial time.",
    "created_at": "2010-06-17T21:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62896",
    "user": "https://github.com/rlmill"
}
```

I'd much rather see the algorithm in the paper implemented, especially if it's polynomial time.



---

archive/issue_comments_062897.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-17T21:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62897",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062898.json:
```json
{
    "body": "What would you think of still putting this into Sage ? It would take much more time to write the other algorithm, and nothing says that LP would not be faster anyway...\n\nNathann",
    "created_at": "2010-06-18T11:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62898",
    "user": "https://github.com/nathanncohen"
}
```

What would you think of still putting this into Sage ? It would take much more time to write the other algorithm, and nothing says that LP would not be faster anyway...

Nathann



---

archive/issue_comments_062899.json:
```json
{
    "body": "If you indicate in the `ALGORITHM` section where the papers are regarding the poly-time algorithm, I'm fine with including this.",
    "created_at": "2010-06-18T14:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62899",
    "user": "https://github.com/rlmill"
}
```

If you indicate in the `ALGORITHM` section where the papers are regarding the poly-time algorithm, I'm fine with including this.



---

archive/issue_comments_062900.json:
```json
{
    "body": "Updated !",
    "created_at": "2010-06-20T17:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62900",
    "user": "https://github.com/nathanncohen"
}
```

Updated !



---

archive/issue_comments_062901.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-20T17:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62901",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062902.json:
```json
{
    "body": "Revised version of Nathann's patch using the proper # optional syntax",
    "created_at": "2010-06-21T17:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62902",
    "user": "https://github.com/rlmill"
}
```

Revised version of Nathann's patch using the proper # optional syntax



---

archive/issue_comments_062903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T17:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62903",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062904.json:
```json
{
    "body": "Attachment [trac_7476.patch](tarball://root/attachments/some-uuid/ticket7476/trac_7476.patch) by @rlmill created at 2010-06-21 17:49:43\n\nLooks good to me.",
    "created_at": "2010-06-21T17:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62904",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7476.patch](tarball://root/attachments/some-uuid/ticket7476/trac_7476.patch) by @rlmill created at 2010-06-21 17:49:43

Looks good to me.



---

archive/issue_events_007704.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-29T16:43:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7476#event-7704"
}
```



---

archive/issue_comments_062905.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7476#issuecomment-62905",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
