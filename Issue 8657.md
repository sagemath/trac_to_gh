# Issue 8657: libgcrypt spkg has incorrect DSO linking

archive/issues_008657.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  pjeremy drkirby was\n\nKeywords: DSO\n\nThe libgcrypt src/tests/ have a subtle linker bug which is exposed by the DSO linking changes for Fedora 13, see https://fedoraproject.org/wiki/UnderstandingDSOLinkChange. This version adds libgpg-error to the link command line.\n\nThe change is completely safe and is required to compile libgcrypt on Fedora 13 (beta).\n\nhttp://www.stp.dias.ie/~vbraun/Sage/spkg/libgcrypt-1.4.4.p3.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/8657\n\n",
    "created_at": "2010-04-07T21:54:40Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "libgcrypt spkg has incorrect DSO linking",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8657",
    "user": "vbraun"
}
```
Assignee: GeorgSWeber

CC:  pjeremy drkirby was

Keywords: DSO

The libgcrypt src/tests/ have a subtle linker bug which is exposed by the DSO linking changes for Fedora 13, see https://fedoraproject.org/wiki/UnderstandingDSOLinkChange. This version adds libgpg-error to the link command line.

The change is completely safe and is required to compile libgcrypt on Fedora 13 (beta).

http://www.stp.dias.ie/~vbraun/Sage/spkg/libgcrypt-1.4.4.p3.spkg

Issue created by migration from https://trac.sagemath.org/ticket/8657





---

archive/issue_comments_078556.json:
```json
{
    "body": "Duplicate of #9189.  I'm not sure why I didn't see this one before.",
    "created_at": "2010-06-09T17:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8657#issuecomment-78556",
    "user": "mhansen"
}
```

Duplicate of #9189.  I'm not sure why I didn't see this one before.



---

archive/issue_comments_078557.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-09T17:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8657#issuecomment-78557",
    "user": "mhansen"
}
```

Resolution: duplicate
