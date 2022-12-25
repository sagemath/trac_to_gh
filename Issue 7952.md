# Issue 7952: broken binomial sum (fixed in maxima)

archive/issues_007952.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  jpflori @orlitzky\n\nKeywords: maxima\n\nFrom the following sage-devel thread:\n\nhttp://groups.google.com/group/sage-devel/t/c7a742292f424b04\n\n\n```\nOn Jan 10, 6:15\u00a0pm, Harald Schilly <harald.schi...@gmail.com> wrote:\n> Hi, I got this from the report a problem link:\n>\n> Typing (in the inotebook)\n>\n> var('t,k,i')\n> sum(binomial(i+t,t),i,0,k)\n>\n> results in\n>\n> binomial(k + t + 1, t + 1) - 1\n>\n> which is false, the well-known answer is binomial(k + t + 1, t + 1)  \n\nThere is a fix for this bug in maxima cvs. If you don't want to wait\nfor the next release I can provide a patch.\n\nAndrej\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7952\n\n",
    "created_at": "2010-01-16T18:08:01Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "broken binomial sum (fixed in maxima)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7952",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  jpflori @orlitzky

Keywords: maxima

From the following sage-devel thread:

http://groups.google.com/group/sage-devel/t/c7a742292f424b04


```
On Jan 10, 6:15 pm, Harald Schilly <harald.schi...@gmail.com> wrote:
> Hi, I got this from the report a problem link:
>
> Typing (in the inotebook)
>
> var('t,k,i')
> sum(binomial(i+t,t),i,0,k)
>
> results in
>
> binomial(k + t + 1, t + 1) - 1
>
> which is false, the well-known answer is binomial(k + t + 1, t + 1)  

There is a fix for this bug in maxima cvs. If you don't want to wait
for the next release I can provide a patch.

Andrej
```


Issue created by migration from https://trac.sagemath.org/ticket/7952





---

archive/issue_comments_069267.json:
```json
{
    "body": "Here is the patch, we should add this to our package:\n\nhttp://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/src/combin.lisp?r1=1.39&r2=1.40&view=patch",
    "created_at": "2010-01-17T08:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69267",
    "user": "https://github.com/burcin"
}
```

Here is the patch, we should add this to our package:

http://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/src/combin.lisp?r1=1.39&r2=1.40&view=patch



---

archive/issue_comments_069268.json:
```json
{
    "body": "jpflori reports this is fixed in #10187's package.  Maybe s/he will contribute a patch :)",
    "created_at": "2010-11-16T14:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69268",
    "user": "https://github.com/kcrisman"
}
```

jpflori reports this is fixed in #10187's package.  Maybe s/he will contribute a patch :)



---

archive/issue_comments_069269.json:
```json
{
    "body": "Attachment [sage-trac_7952.patch](tarball://root/attachments/some-uuid/ticket7952/sage-trac_7952.patch) by @orlitzky created at 2011-12-14 00:29:37\n\nAdd a doctest for the correct behavior.",
    "created_at": "2011-12-14T00:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69269",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_7952.patch](tarball://root/attachments/some-uuid/ticket7952/sage-trac_7952.patch) by @orlitzky created at 2011-12-14 00:29:37

Add a doctest for the correct behavior.



---

archive/issue_comments_069270.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-14T00:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69270",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069271.json:
```json
{
    "body": "This is fixed in sage-4.8.alpha4, so I've added a doctest.",
    "created_at": "2011-12-14T00:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69271",
    "user": "https://github.com/orlitzky"
}
```

This is fixed in sage-4.8.alpha4, so I've added a doctest.



---

archive/issue_comments_069272.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-28T02:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69272",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069273.json:
```json
{
    "body": "Positive review.",
    "created_at": "2012-01-28T02:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69273",
    "user": "https://github.com/kcrisman"
}
```

Positive review.



---

archive/issue_comments_069274.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-02T12:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7952#issuecomment-69274",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
