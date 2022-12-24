# Issue 3006: missing elliptic integrals in special.py

archive/issues_003006.json:
```json
{
    "body": "Assignee: was\n\nThe following problem was reported by Dustin Vaselaar to sage-support:\n\n\nHello,\nI am looking to use a complete elliptic integral of the first kind in\nsage, however I'm not sure if this has been implemented.  The link\nhttp://www.sagemath.org/doc/html/ref/module-sage.functions.special.html\nmentions a function \"elliptic_kc\", but it doesn't seem to be\nimplemented in sage version 3.0, judging from the result of this\ncommand:\n\n\n```\nsage: elliptic_kc?\nObject `elliptic_kc` not found.\n```\n\n\nAny insights on using a a complete elliptic integral of the first kind\nin sage?\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3006\n\n",
    "created_at": "2008-04-23T14:27:55Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "missing elliptic integrals in special.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3006",
    "user": "wdj"
}
```
Assignee: was

The following problem was reported by Dustin Vaselaar to sage-support:


Hello,
I am looking to use a complete elliptic integral of the first kind in
sage, however I'm not sure if this has been implemented.  The link
http://www.sagemath.org/doc/html/ref/module-sage.functions.special.html
mentions a function "elliptic_kc", but it doesn't seem to be
implemented in sage version 3.0, judging from the result of this
command:


```
sage: elliptic_kc?
Object `elliptic_kc` not found.
```


Any insights on using a a complete elliptic integral of the first kind
in sage?



Issue created by migration from https://trac.sagemath.org/ticket/3006





---

archive/issue_comments_020673.json:
```json
{
    "body": "Clearly this is a problem with \"documentation\" but I filed it under \"calculus\" since that seemed closer. It is a matter of adding a wrapper to Maxima's function elliptic_kc.\n\n\n```\nsage: RR(maxima.eval(\"elliptic_kc (0.5)\"))\n1.85407467730137\n```\n\n\nI'll submit a patch soon.",
    "created_at": "2008-04-23T14:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3006#issuecomment-20673",
    "user": "wdj"
}
```

Clearly this is a problem with "documentation" but I filed it under "calculus" since that seemed closer. It is a matter of adding a wrapper to Maxima's function elliptic_kc.


```
sage: RR(maxima.eval("elliptic_kc (0.5)"))
1.85407467730137
```


I'll submit a patch soon.



---

archive/issue_comments_020674.json:
```json
{
    "body": "Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3006/9607.patch) by wdj created at 2008-04-23 22:15:38\n\nThinking about this problem more, I think it is my fault. In any case, a patch is attached.  It is based on 3.0 and passes sage -t but my (old) machine froze (as it very often does) during the sage -testall. No errors were reported before the freeze.",
    "created_at": "2008-04-23T22:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3006#issuecomment-20674",
    "user": "wdj"
}
```

Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3006/9607.patch) by wdj created at 2008-04-23 22:15:38

Thinking about this problem more, I think it is my fault. In any case, a patch is attached.  It is based on 3.0 and passes sage -t but my (old) machine froze (as it very often does) during the sage -testall. No errors were reported before the freeze.



---

archive/issue_comments_020675.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-04-24T03:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3006#issuecomment-20675",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_020676.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-24T04:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3006#issuecomment-20676",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0



---

archive/issue_comments_020677.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-24T04:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3006#issuecomment-20677",
    "user": "mabshoff"
}
```

Resolution: fixed
