# Issue 3651: elliptic curves -- bug in L_ratio()

archive/issues_003651.json:
```json
{
    "body": "Assignee: was\n\nCC:  nbruin@cecm.sfu.ca\n\nNils Bruin reports:\n\n\"I ran into the following problem in sage, and I suspect it might be your code:\n\n```\nsage: EllipticCurve([0,0,0,-193^2,0]).sha().an()\n[...]\nNameError: global name 'misc' is not defined\n```\n\nWas this tested at all?\"\n\nIt's a problem in L_ratio().\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3651\n\n",
    "created_at": "2008-07-13T19:35:49Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "elliptic curves -- bug in L_ratio()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3651",
    "user": "cremona"
}
```
Assignee: was

CC:  nbruin@cecm.sfu.ca

Nils Bruin reports:

"I ran into the following problem in sage, and I suspect it might be your code:

```
sage: EllipticCurve([0,0,0,-193^2,0]).sha().an()
[...]
NameError: global name 'misc' is not defined
```

Was this tested at all?"

It's a problem in L_ratio().


Issue created by migration from https://trac.sagemath.org/ticket/3651





---

archive/issue_comments_025820.json:
```json
{
    "body": "Attachment [sage-trac3651.patch](tarball://root/attachments/some-uuid/ticket3651/sage-trac3651.patch) by cremona created at 2008-07-13 19:45:47\n\nAfter the attached patch (based on 3.0.4) it works fine:\n\n```\nsage: EllipticCurve([0,0,0,-193^2,0]).sha().an()\n4\n```\n",
    "created_at": "2008-07-13T19:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3651#issuecomment-25820",
    "user": "cremona"
}
```

Attachment [sage-trac3651.patch](tarball://root/attachments/some-uuid/ticket3651/sage-trac3651.patch) by cremona created at 2008-07-13 19:45:47

After the attached patch (based on 3.0.4) it works fine:

```
sage: EllipticCurve([0,0,0,-193^2,0]).sha().an()
4
```




---

archive/issue_comments_025821.json:
```json
{
    "body": "See http://groups.google.com/group/sage-devel/t/60a62f8337e4de3a for details.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-13T19:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3651#issuecomment-25821",
    "user": "mabshoff"
}
```

See http://groups.google.com/group/sage-devel/t/60a62f8337e4de3a for details.

Cheers,

Michael



---

archive/issue_comments_025822.json:
```json
{
    "body": "Does not work with me, did you mean \nimport sage.misc.misc as misc\n?",
    "created_at": "2008-07-14T10:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3651#issuecomment-25822",
    "user": "wuthrich"
}
```

Does not work with me, did you mean 
import sage.misc.misc as misc
?



---

archive/issue_comments_025823.json:
```json
{
    "body": "Sorry, my mistake; it works of course.",
    "created_at": "2008-07-14T12:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3651#issuecomment-25823",
    "user": "wuthrich"
}
```

Sorry, my mistake; it works of course.



---

archive/issue_comments_025824.json:
```json
{
    "body": "Taking Chris' remark into account I am giving this a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T04:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3651#issuecomment-25824",
    "user": "mabshoff"
}
```

Taking Chris' remark into account I am giving this a positive review.

Cheers,

Michael



---

archive/issue_comments_025825.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T04:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3651#issuecomment-25825",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.alpha0



---

archive/issue_comments_025826.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T04:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3651#issuecomment-25826",
    "user": "mabshoff"
}
```

Resolution: fixed
