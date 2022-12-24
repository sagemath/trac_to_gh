# Issue 4142: limit bug: should be -Infinity, but gives +Infinity

archive/issues_004142.json:
```json
{
    "body": "Assignee: burcin\n\nAs discussed in http://groups.google.com/group/sage-devel/browse_thread/thread/7afc9f414413906 , some limits are not evaluated correctly:\n\n\n```\nsage: f = sqrt(1-x^2)\nsage: g = diff(f, x); g\n-x/sqrt(1 - x^2)\nsage: limit(g, x=1, dir='below')\n+Infinity\n```\n\n\nThe last command should give -Infinity, of course, since `f` is a semicircle. At the other endpoint, the limit is correct (+Infinity). \n\nIssue created by migration from https://trac.sagemath.org/ticket/4142\n\n",
    "created_at": "2008-09-18T06:14:18Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "limit bug: should be -Infinity, but gives +Infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4142",
    "user": "ddrake"
}
```
Assignee: burcin

As discussed in http://groups.google.com/group/sage-devel/browse_thread/thread/7afc9f414413906 , some limits are not evaluated correctly:


```
sage: f = sqrt(1-x^2)
sage: g = diff(f, x); g
-x/sqrt(1 - x^2)
sage: limit(g, x=1, dir='below')
+Infinity
```


The last command should give -Infinity, of course, since `f` is a semicircle. At the other endpoint, the limit is correct (+Infinity). 

Issue created by migration from https://trac.sagemath.org/ticket/4142





---

archive/issue_comments_030073.json:
```json
{
    "body": "As it happens, this is still a problem in Sage 4.1.x - but the problem is somewhat more subtle than just some Maxima bug, or Sage incorrectly parsing Maxima output:\n\n```\n(%i1) limit(-x/sqrt(1-x^2),x,1,minus);\n(%o1)                                            infinity\n```\n\nBUT Maxima's infinity is not Sage's infinity; it is the complex infinity!  If the answer is +infinity, Maxima would return 'inf'.   I've asked the Maxima list about this, so we'll see what happens.",
    "created_at": "2009-09-29T16:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30073",
    "user": "kcrisman"
}
```

As it happens, this is still a problem in Sage 4.1.x - but the problem is somewhat more subtle than just some Maxima bug, or Sage incorrectly parsing Maxima output:

```
(%i1) limit(-x/sqrt(1-x^2),x,1,minus);
(%o1)                                            infinity
```

BUT Maxima's infinity is not Sage's infinity; it is the complex infinity!  If the answer is +infinity, Maxima would return 'inf'.   I've asked the Maxima list about this, so we'll see what happens.



---

archive/issue_comments_030074.json:
```json
{
    "body": "This is fixed in the latest Maxima CVS version, so whenever we upgrade again, this one will hopefully be closed.\n\n```\nMaxima 5.19post http://maxima.sourceforge.net\nusing Lisp SBCL 1.0.24\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) limit(-x/sqrt(1-x^2),x,1,minus);\n(%o1)                                minf\n```\n",
    "created_at": "2009-10-05T18:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30074",
    "user": "kcrisman"
}
```

This is fixed in the latest Maxima CVS version, so whenever we upgrade again, this one will hopefully be closed.

```
Maxima 5.19post http://maxima.sourceforge.net
using Lisp SBCL 1.0.24
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) limit(-x/sqrt(1-x^2),x,1,minus);
(%o1)                                minf
```




---

archive/issue_comments_030075.json:
```json
{
    "body": "This is now correct in Maxima 5.20.1, so it just needs a doctest once the new spkg is merged.",
    "created_at": "2009-12-22T17:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30075",
    "user": "kcrisman"
}
```

This is now correct in Maxima 5.20.1, so it just needs a doctest once the new spkg is merged.



---

archive/issue_comments_030076.json:
```json
{
    "body": "The patch here depends on the spkg at #7745 to work properly.  It also depends on the patch there, and at #6423, but will probably still apply if someone forgot to apply them first.",
    "created_at": "2009-12-22T21:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30076",
    "user": "kcrisman"
}
```

The patch here depends on the spkg at #7745 to work properly.  It also depends on the patch there, and at #6423, but will probably still apply if someone forgot to apply them first.



---

archive/issue_comments_030077.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-22T21:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30077",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030078.json:
```json
{
    "body": "Based on 4.3.alpha1",
    "created_at": "2009-12-22T21:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30078",
    "user": "kcrisman"
}
```

Based on 4.3.alpha1



---

archive/issue_comments_030079.json:
```json
{
    "body": "Attachment [trac_4142-limit-sqrt.patch](tarball://root/attachments/some-uuid/ticket4142/trac_4142-limit-sqrt.patch) by ddrake created at 2009-12-23 08:12:20\n\nThe spkg and patch at #7745 fix this problem, and the doctest passes. Positive review; this can be merged as soon as #7745 is in.",
    "created_at": "2009-12-23T08:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30079",
    "user": "ddrake"
}
```

Attachment [trac_4142-limit-sqrt.patch](tarball://root/attachments/some-uuid/ticket4142/trac_4142-limit-sqrt.patch) by ddrake created at 2009-12-23 08:12:20

The spkg and patch at #7745 fix this problem, and the doctest passes. Positive review; this can be merged as soon as #7745 is in.



---

archive/issue_comments_030080.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-23T08:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30080",
    "user": "ddrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_030081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T03:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4142#issuecomment-30081",
    "user": "mhansen"
}
```

Resolution: fixed
