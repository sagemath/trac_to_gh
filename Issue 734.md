# Issue 734: combinatorics problems on fedora core 7 with sage-2.8.5

archive/issues_000734.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  sage-combinat\n\n\n```\n> >\n> > NOTE: Since this is such a major release, there will likely be problems\n> > and a 2.8.5.1 release shortly to fix them.  Please report!\n> >\n> \n> Builds on Fedora 7,\n> \n> ----------------------------------------------------------------------\n> The following tests failed:\n> \n> \n>          sage -t  devel/sage-main/sage/combinat/skew_tableau.py\n>          sage -t  devel/sage-main/sage/combinat/ribbon.py\n> Total time for all tests: 1838.3 seconds\n> [jaap@paix sage-2.8.5]$\n\nThis is from mike Hansen's new combinatorics code, I think.\nI *am* able to replicate this on my Fedora Core machine,\nand on none of my other 10 or so machines.  Mike, any\ncomments -- I can give you an account on the machine if\nnecessary.\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/734\n\n",
    "created_at": "2007-09-21T21:09:48Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5.1",
    "title": "combinatorics problems on fedora core 7 with sage-2.8.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/734",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  sage-combinat


```
> >
> > NOTE: Since this is such a major release, there will likely be problems
> > and a 2.8.5.1 release shortly to fix them.  Please report!
> >
> 
> Builds on Fedora 7,
> 
> ----------------------------------------------------------------------
> The following tests failed:
> 
> 
>          sage -t  devel/sage-main/sage/combinat/skew_tableau.py
>          sage -t  devel/sage-main/sage/combinat/ribbon.py
> Total time for all tests: 1838.3 seconds
> [jaap@paix sage-2.8.5]$

This is from mike Hansen's new combinatorics code, I think.
I *am* able to replicate this on my Fedora Core machine,
and on none of my other 10 or so machines.  Mike, any
comments -- I can give you an account on the machine if
necessary.

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/734





---

archive/issue_comments_004289.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-09-21T21:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/734#issuecomment-4289",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_004290.json:
```json
{
    "body": "Attachment [734.patch](tarball://root/attachments/some-uuid/ticket734/734.patch) by @mwhansen created at 2007-09-23 18:38:06",
    "created_at": "2007-09-23T18:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/734#issuecomment-4290",
    "user": "https://github.com/mwhansen"
}
```

Attachment [734.patch](tarball://root/attachments/some-uuid/ticket734/734.patch) by @mwhansen created at 2007-09-23 18:38:06



---

archive/issue_comments_004291.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-23T19:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/734#issuecomment-4291",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004292.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-23T21:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/734#issuecomment-4292",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_004293.json:
```json
{
    "body": "The problem turned out to be comparing Integer and None. \n\nI had to fix another related problem: \n    http://sage.math.washington.edu/tmp/fc734.hg",
    "created_at": "2007-09-23T21:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/734#issuecomment-4293",
    "user": "https://github.com/williamstein"
}
```

The problem turned out to be comparing Integer and None. 

I had to fix another related problem: 
    http://sage.math.washington.edu/tmp/fc734.hg
