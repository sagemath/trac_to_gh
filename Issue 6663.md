# Issue 6663: add new 4ti2 and glpk experimental packages

archive/issues_006663.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: 4ti2, glpk, sandpile\n\nThe 4ti2 and glpk packages in experimental are very out of date.  Since there seems to be some growing interest in having them available in sage they should be updated.  If they can be made to work on more platforms they should be moved to optional.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6663\n\n",
    "created_at": "2009-07-31T20:14:51Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "add new 4ti2 and glpk experimental packages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6663",
    "user": "mhampton"
}
```
Assignee: tbd

Keywords: 4ti2, glpk, sandpile

The 4ti2 and glpk packages in experimental are very out of date.  Since there seems to be some growing interest in having them available in sage they should be updated.  If they can be made to work on more platforms they should be moved to optional.

Issue created by migration from https://trac.sagemath.org/ticket/6663





---

archive/issue_comments_054687.json:
```json
{
    "body": "My current package attempts are at:\n\nhttp://www.d.umn.edu/~mhampton/4ti2.p0.spkg\nhttp://www.d.umn.edu/~mhampton/glpk.p0.spkg \n\n-Marshall",
    "created_at": "2009-07-31T20:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54687",
    "user": "mhampton"
}
```

My current package attempts are at:

http://www.d.umn.edu/~mhampton/4ti2.p0.spkg
http://www.d.umn.edu/~mhampton/glpk.p0.spkg 

-Marshall



---

archive/issue_comments_054688.json:
```json
{
    "body": "I was unaware of the glpk package at:\nhttp://trac.sagemath.org/sage_trac/ticket/6602\n\nwhich has a more recent version of glpk.  That spkg should be used instead of mine.",
    "created_at": "2009-07-31T23:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54688",
    "user": "mhampton"
}
```

I was unaware of the glpk package at:
http://trac.sagemath.org/sage_trac/ticket/6602

which has a more recent version of glpk.  That spkg should be used instead of mine.



---

archive/issue_comments_054689.json:
```json
{
    "body": "This 4ti2 spkg installed fine with N Cohen's glpk (http://trac.sagemath.org/sage_trac/ticket/6602) on an amd64 ubuntu 9.04 machine.",
    "created_at": "2009-08-01T04:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54689",
    "user": "wdj"
}
```

This 4ti2 spkg installed fine with N Cohen's glpk (http://trac.sagemath.org/sage_trac/ticket/6602) on an amd64 ubuntu 9.04 machine.



---

archive/issue_comments_054690.json:
```json
{
    "body": "This installed fine and passed sage -testall (except for the known failures) on an intel macbook with 4.1.1.a0 running OS 10.4.11.\n\nThis gets a positive review from me. Are there more tests which should be run before \"needs review\" gets changed to \"positive review\"?",
    "created_at": "2009-08-01T20:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54690",
    "user": "wdj"
}
```

This installed fine and passed sage -testall (except for the known failures) on an intel macbook with 4.1.1.a0 running OS 10.4.11.

This gets a positive review from me. Are there more tests which should be run before "needs review" gets changed to "positive review"?



---

archive/issue_comments_054691.json:
```json
{
    "body": "Changing component from algebra to packages.",
    "created_at": "2009-08-16T05:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54691",
    "user": "AlexGhitza"
}
```

Changing component from algebra to packages.



---

archive/issue_comments_054692.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-08-16T05:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54692",
    "user": "AlexGhitza"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_054693.json:
```json
{
    "body": "I have downloaded the spkg to my home directory:\n\n\n\nhttp://sage.math.washington.edu/home/mvngu/patch/4ti2.p0.spkg\n\n\n\nIs there any special reason why the package is not under revision control?\n\n```\n[mvngu@mod mvngu]$ tar -jxf 4ti2.p0.spkg \n[mvngu@mod mvngu]$ cd 4ti2.p0/\n[mvngu@mod 4ti2.p0]$ hg st\nabort: There is no Mercurial repository here (.hg not found)!\n```\n",
    "created_at": "2009-09-02T08:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54693",
    "user": "mvngu"
}
```

I have downloaded the spkg to my home directory:



http://sage.math.washington.edu/home/mvngu/patch/4ti2.p0.spkg



Is there any special reason why the package is not under revision control?

```
[mvngu@mod mvngu]$ tar -jxf 4ti2.p0.spkg 
[mvngu@mod mvngu]$ cd 4ti2.p0/
[mvngu@mod 4ti2.p0]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
```




---

archive/issue_comments_054694.json:
```json
{
    "body": "Merged in the experimental packages repository at\n\nhttp://www.sagemath.org/packages/experimental/\n\nThe updated spkg is available at\n\nhttp://www.sagemath.org/packages/experimental/4ti2.p0.spkg",
    "created_at": "2009-09-11T18:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54694",
    "user": "mvngu"
}
```

Merged in the experimental packages repository at

http://www.sagemath.org/packages/experimental/

The updated spkg is available at

http://www.sagemath.org/packages/experimental/4ti2.p0.spkg



---

archive/issue_comments_054695.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-11T18:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54695",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054696.json:
```json
{
    "body": "Changing component from packages to experimental package.",
    "created_at": "2009-09-20T22:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6663#issuecomment-54696",
    "user": "mvngu"
}
```

Changing component from packages to experimental package.
