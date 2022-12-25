# Issue 9420: SubgraphSearch class instead of a method, digraphs fixed

archive/issues_009420.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @rlmill\n\nHello !!\n\nThis patch implements the class SubgraphSearch, which enables one to look for copies of a small graph in a larger one, which is exactly what the method subgraph_search previously did (#8922).\n\nThe code is simply inserted inside a new class, with a few other methods to iterate over the occurences, or to count them !\n\nThis could have been done with a simple \"yield\" in Cython, though we may not want to wait until they are implemented ;-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9420\n\n",
    "created_at": "2010-07-03T11:52:09Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "SubgraphSearch class instead of a method, digraphs fixed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9420",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  @rlmill

Hello !!

This patch implements the class SubgraphSearch, which enables one to look for copies of a small graph in a larger one, which is exactly what the method subgraph_search previously did (#8922).

The code is simply inserted inside a new class, with a few other methods to iterate over the occurences, or to count them !

This could have been done with a simple "yield" in Cython, though we may not want to wait until they are implemented ;-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9420





---

archive/issue_comments_089704.json:
```json
{
    "body": "Attachment [trac_9420.patch](tarball://root/attachments/some-uuid/ticket9420/trac_9420.patch) by @nathanncohen created at 2010-07-03 11:53:09",
    "created_at": "2010-07-03T11:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89704",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9420.patch](tarball://root/attachments/some-uuid/ticket9420/trac_9420.patch) by @nathanncohen created at 2010-07-03 11:53:09



---

archive/issue_comments_089705.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-03T11:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89705",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089706.json:
```json
{
    "body": "OK, tested on Debian Linux amd64, and on MacOSX PPC with gcc4.2.\nThe change seems to be more ideological than adding more functionality/bugfixing.\nIt would be nice if someone more versed in Sage had a look, whether this is not something \nalien ideologically...",
    "created_at": "2010-09-19T06:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89706",
    "user": "https://github.com/dimpase"
}
```

OK, tested on Debian Linux amd64, and on MacOSX PPC with gcc4.2.
The change seems to be more ideological than adding more functionality/bugfixing.
It would be nice if someone more versed in Sage had a look, whether this is not something 
alien ideologically...



---

archive/issue_comments_089707.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T06:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89707",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089708.json:
```json
{
    "body": "indeed... and most importantly, it may have consisted in replacing \"return\" by \"yield\", if only those were available in Cython `:-p`\n\nNathann",
    "created_at": "2010-09-19T08:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89708",
    "user": "https://github.com/nathanncohen"
}
```

indeed... and most importantly, it may have consisted in replacing "return" by "yield", if only those were available in Cython `:-p`

Nathann



---

archive/issue_events_009575.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-29T08:39:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9420#event-9575"
}
```



---

archive/issue_comments_089709.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89709",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
