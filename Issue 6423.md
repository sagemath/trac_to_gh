# Issue 6423: Sage not always understanding i=sqrt(-1)  - Maxima bug proably

archive/issues_006423.json:
```json
{
    "body": "Assignee: tbd\n\nVladimir Bondarenko (a developer of software to test computer algebra systems - see [http://www.cas-testing.org/](http://www.cas-testing.org/) ), had been playing with [http://demo.sagenb.org/](http://demo.sagenb.org/) and noted the following:\n\n```\nexp(-x^i).integral(x,0,1)  returns\n\nTraceback (click to the left for traceback)\n...\nIs %i an integer?\n\nOuch! Any Sage comments?\n```\n\n\nWhen I reported his on sage-devel, William Stein said:\n\n''A large amount of the symbolic functionality that uses Maxima has\nissues like this, but unfortunately there is basically nothing we can do about it, except continue with projects to rewrite the parts of Sage that call Maxima so that they don't call Maxima.  So this class of bugs should be very good motivation to continue to work on\nimplementing symbolic integration ourselves (and/or further improving sympy!).''\n\nHe then went on to say he wanted it reported as a TRAC bug but was busy, so I have done it on his behalf. \n\nI don't feel able to comment much more on this, and personally don't intend trying to fix it (outside my knowledge), so I've just reported it. \n\nCan someone else add appropriate priority, milestones, keywords etc, as this is completely outside my *comfort zone*. \n\nDavid Kirkby\n\nIssue created by migration from https://trac.sagemath.org/ticket/6423\n\n",
    "created_at": "2009-06-26T14:54:37Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Sage not always understanding i=sqrt(-1)  - Maxima bug proably",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6423",
    "user": "drkirkby"
}
```
Assignee: tbd

Vladimir Bondarenko (a developer of software to test computer algebra systems - see [http://www.cas-testing.org/](http://www.cas-testing.org/) ), had been playing with [http://demo.sagenb.org/](http://demo.sagenb.org/) and noted the following:

```
exp(-x^i).integral(x,0,1)  returns

Traceback (click to the left for traceback)
...
Is %i an integer?

Ouch! Any Sage comments?
```


When I reported his on sage-devel, William Stein said:

''A large amount of the symbolic functionality that uses Maxima has
issues like this, but unfortunately there is basically nothing we can do about it, except continue with projects to rewrite the parts of Sage that call Maxima so that they don't call Maxima.  So this class of bugs should be very good motivation to continue to work on
implementing symbolic integration ourselves (and/or further improving sympy!).''

He then went on to say he wanted it reported as a TRAC bug but was busy, so I have done it on his behalf. 

I don't feel able to comment much more on this, and personally don't intend trying to fix it (outside my knowledge), so I've just reported it. 

Can someone else add appropriate priority, milestones, keywords etc, as this is completely outside my *comfort zone*. 

David Kirkby

Issue created by migration from https://trac.sagemath.org/ticket/6423





---

archive/issue_comments_051569.json:
```json
{
    "body": "Changing assignee from tbd to @burcin.",
    "created_at": "2009-07-05T05:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51569",
    "user": "@aghitza"
}
```

Changing assignee from tbd to @burcin.



---

archive/issue_comments_051570.json:
```json
{
    "body": "Changing component from algebra to calculus.",
    "created_at": "2009-07-05T05:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51570",
    "user": "@aghitza"
}
```

Changing component from algebra to calculus.



---

archive/issue_comments_051571.json:
```json
{
    "body": "This is fixed by the spkg and patch at #6699.  I will put up a patch with a doctest here when #6699 gets merged.",
    "created_at": "2009-08-24T09:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51571",
    "user": "@aghitza"
}
```

This is fixed by the spkg and patch at #6699.  I will put up a patch with a doctest here when #6699 gets merged.



---

archive/issue_comments_051572.json:
```json
{
    "body": "Changing assignee from @burcin to @aghitza.",
    "created_at": "2009-08-24T09:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51572",
    "user": "@aghitza"
}
```

Changing assignee from @burcin to @aghitza.



---

archive/issue_comments_051573.json:
```json
{
    "body": "Unfortunately, it seems not.  From uw.sagenb.org:\n\n\n```\nsage: exp(-x^i).integral(x,0,1)\nTraceback (most recent call last):\n...\nTypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(i>0)' before integral or limit evaluation, for example):\nIs %i an integer?\nsage: maxima.eval('integrate(exp(-x^%i),x,0,1);')\nTraceback (most recent call last):\n...\nValueError: Computation failed since Maxima requested additional constraints (try the command 'assume(i>0)' before integral or limit evaluation, for example):\nIs %i an integer?\n```\n\n\nThis also was verified on a local installation.",
    "created_at": "2009-09-29T14:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51573",
    "user": "@kcrisman"
}
```

Unfortunately, it seems not.  From uw.sagenb.org:


```
sage: exp(-x^i).integral(x,0,1)
Traceback (most recent call last):
...
TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(i>0)' before integral or limit evaluation, for example):
Is %i an integer?
sage: maxima.eval('integrate(exp(-x^%i),x,0,1);')
Traceback (most recent call last):
...
ValueError: Computation failed since Maxima requested additional constraints (try the command 'assume(i>0)' before integral or limit evaluation, for example):
Is %i an integer?
```


This also was verified on a local installation.



---

archive/issue_comments_051574.json:
```json
{
    "body": "Just FYI, this is now FIXED in the latest CVS of Maxima.  \n\n```\nMaxima 5.19post http://maxima.sourceforge.netusing Lisp SBCL 1.0.24\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) integrate(exp(-x^%i),x,0,1);\n                       %i gamma_incomplete(- %i, - log(x + 1))\n(%o1) %i (%i (limit   (---------------------------------------\n              x -> 0-                     2\n   %i gamma_incomplete(%i, - log(x + 1))    %i gamma_incomplete(%i, 1)\n - -------------------------------------) + --------------------------\n                     2                                  2\n   %i gamma_incomplete(- %i, 1)\n - ----------------------------)\n                2\n              gamma_incomplete(%i, - log(x + 1))\n + limit   (- ----------------------------------\n   x -> 0-                    2\n   gamma_incomplete(- %i, - log(x + 1))    gamma_incomplete(%i, 1)\n - ------------------------------------) + -----------------------\n                    2                                 2\n   gamma_incomplete(- %i, 1)\n + -------------------------)\n               2\n(%i2) \n```\n\nOf course, now we'll have to deal with nounforms and gamma_incomplete translation, but hopefully that won't be too big of a hurdle.",
    "created_at": "2009-10-23T23:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51574",
    "user": "@kcrisman"
}
```

Just FYI, this is now FIXED in the latest CVS of Maxima.  

```
Maxima 5.19post http://maxima.sourceforge.netusing Lisp SBCL 1.0.24
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) integrate(exp(-x^%i),x,0,1);
                       %i gamma_incomplete(- %i, - log(x + 1))
(%o1) %i (%i (limit   (---------------------------------------
              x -> 0-                     2
   %i gamma_incomplete(%i, - log(x + 1))    %i gamma_incomplete(%i, 1)
 - -------------------------------------) + --------------------------
                     2                                  2
   %i gamma_incomplete(- %i, 1)
 - ----------------------------)
                2
              gamma_incomplete(%i, - log(x + 1))
 + limit   (- ----------------------------------
   x -> 0-                    2
   gamma_incomplete(- %i, - log(x + 1))    gamma_incomplete(%i, 1)
 - ------------------------------------) + -----------------------
                    2                                 2
   gamma_incomplete(- %i, 1)
 + -------------------------)
               2
(%i2) 
```

Of course, now we'll have to deal with nounforms and gamma_incomplete translation, but hopefully that won't be too big of a hurdle.



---

archive/issue_comments_051575.json:
```json
{
    "body": "Using Maxima 5.20.1 with Sage 4.3.alpha1:\n\n```\nsage: exp(-x*i).integral(x,0,1)\nI*e^(-I) - I\n```\n\nSo if that is mathematically correct, sounds like it's fixed.  The following link [http://www.wolframalpha.com/input/?i=integrate+e%5E%28-x*I%29+from+0+to+1](http://www.wolframalpha.com/input/?i=integrate+e%5E%28-x*I%29+from+0+to+1) indicates it is, as well as just using the FTC.  Now we just need the spkg and to put a doctest here.\n\nSee #7748 for getting a symbolic incomplete gamma, which we would also need regardless of that.",
    "created_at": "2009-12-22T17:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51575",
    "user": "@kcrisman"
}
```

Using Maxima 5.20.1 with Sage 4.3.alpha1:

```
sage: exp(-x*i).integral(x,0,1)
I*e^(-I) - I
```

So if that is mathematically correct, sounds like it's fixed.  The following link [http://www.wolframalpha.com/input/?i=integrate+e%5E%28-x*I%29+from+0+to+1](http://www.wolframalpha.com/input/?i=integrate+e%5E%28-x*I%29+from+0+to+1) indicates it is, as well as just using the FTC.  Now we just need the spkg and to put a doctest here.

See #7748 for getting a symbolic incomplete gamma, which we would also need regardless of that.



---

archive/issue_comments_051576.json:
```json
{
    "body": "This patch depends on the spkg at #7745, but should still apply (with fuzz) if one doesn't apply the patch there.",
    "created_at": "2009-12-22T21:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51576",
    "user": "@kcrisman"
}
```

This patch depends on the spkg at #7745, but should still apply (with fuzz) if one doesn't apply the patch there.



---

archive/issue_comments_051577.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-22T21:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51577",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051578.json:
```json
{
    "body": "Based on 4.3.alpha1",
    "created_at": "2009-12-22T21:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51578",
    "user": "@kcrisman"
}
```

Based on 4.3.alpha1



---

archive/issue_comments_051579.json:
```json
{
    "body": "Attachment [trac_6423-exp.patch](tarball://root/attachments/some-uuid/ticket6423/trac_6423-exp.patch) by @robert-marik created at 2009-12-23 08:38:28\n\nPositive review! Tested on 4.3.rc0 and got only errors which have been reported on sage-devel and are not relevent to this ticket. Tested together with #7745 and #4142.\n\nPositive review, thanks for upgrading.",
    "created_at": "2009-12-23T08:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51579",
    "user": "@robert-marik"
}
```

Attachment [trac_6423-exp.patch](tarball://root/attachments/some-uuid/ticket6423/trac_6423-exp.patch) by @robert-marik created at 2009-12-23 08:38:28

Positive review! Tested on 4.3.rc0 and got only errors which have been reported on sage-devel and are not relevent to this ticket. Tested together with #7745 and #4142.

Positive review, thanks for upgrading.



---

archive/issue_comments_051580.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-23T08:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51580",
    "user": "@robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051581.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T03:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6423#issuecomment-51581",
    "user": "@mwhansen"
}
```

Resolution: fixed
