# Issue 9420: SubgraphSearch class instead of a method, digraphs fixed

archive/issues_009420.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  rlm\n\nHello !!\n\nThis patch implements the class SubgraphSearch, which enables one to look for copies of a small graph in a larger one, which is exactly what the method subgraph_search previously did (#8922).\n\nThe code is simply inserted inside a new class, with a few other methods to iterate over the occurences, or to count them !\n\nThis could have been done with a simple \"yield\" in Cython, though we may not want to wait until they are implemented ;-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9420\n\n",
    "created_at": "2010-07-03T11:52:09Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "SubgraphSearch class instead of a method, digraphs fixed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9420",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  rlm

Hello !!

This patch implements the class SubgraphSearch, which enables one to look for copies of a small graph in a larger one, which is exactly what the method subgraph_search previously did (#8922).

The code is simply inserted inside a new class, with a few other methods to iterate over the occurences, or to count them !

This could have been done with a simple "yield" in Cython, though we may not want to wait until they are implemented ;-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9420





---

archive/issue_comments_089848.json:
```json
{
    "body": "Attachment [trac_9420.patch](tarball://root/attachments/some-uuid/ticket9420/trac_9420.patch) by ncohen created at 2010-07-03 11:53:09",
    "created_at": "2010-07-03T11:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89848",
    "user": "ncohen"
}
```

Attachment [trac_9420.patch](tarball://root/attachments/some-uuid/ticket9420/trac_9420.patch) by ncohen created at 2010-07-03 11:53:09



---

archive/issue_comments_089849.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-03T11:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89849",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089850.json:
```json
{
    "body": "OK, tested on Debian Linux amd64, and on MacOSX PPC with gcc4.2.\nThe change seems to be more ideological than adding more functionality/bugfixing.\nIt would be nice if someone more versed in Sage had a look, whether this is not something \nalien ideologically...",
    "created_at": "2010-09-19T06:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89850",
    "user": "dimpase"
}
```

OK, tested on Debian Linux amd64, and on MacOSX PPC with gcc4.2.
The change seems to be more ideological than adding more functionality/bugfixing.
It would be nice if someone more versed in Sage had a look, whether this is not something 
alien ideologically...



---

archive/issue_comments_089851.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T06:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89851",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089852.json:
```json
{
    "body": "indeed... and most importantly, it may have consisted in replacing \"return\" by \"yield\", if only those were available in Cython `:-p`\n\nNathann",
    "created_at": "2010-09-19T08:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89852",
    "user": "ncohen"
}
```

indeed... and most importantly, it may have consisted in replacing "return" by "yield", if only those were available in Cython `:-p`

Nathann



---

archive/issue_comments_089853.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9420#issuecomment-89853",
    "user": "mpatel"
}
```

Resolution: fixed
