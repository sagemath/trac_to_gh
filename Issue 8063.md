# Issue 8063: New gsl-1.10.p2.spkg works with Open Solaris 64 bit

archive/issues_008063.json:
```json
{
    "body": "Assignee: drkirkby\n\nSetting SAGE64=yes not only works on OSX, but also with Open Solaris 64 bit.\n\nThe package can be found here:\n[http://boxen.math.washington.edu/home/jsp/ports/gsl-1.10.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/gsl-1.10.p2.spkg)\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/8063\n\n",
    "created_at": "2010-01-25T21:49:41Z",
    "labels": [
        "porting",
        "major",
        "enhancement"
    ],
    "title": "New gsl-1.10.p2.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8063",
    "user": "jsp"
}
```
Assignee: drkirkby

Setting SAGE64=yes not only works on OSX, but also with Open Solaris 64 bit.

The package can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/gsl-1.10.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/gsl-1.10.p2.spkg)

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/8063





---

archive/issue_comments_070672.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T21:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8063#issuecomment-70672",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070673.json:
```json
{
    "body": "Attachment [gsl-1.10.p2.patch](tarball://root/attachments/some-uuid/ticket8063/gsl-1.10.p2.patch) by drkirkby created at 2010-01-27 13:43:57\n\nI'm not sure I'd personally bother sorting out SAGE64 issues in packages unless they are building 32-bit, which this one is not. \n\nBut you have also removed Michael Abshoff as a maintainer, and also removed the \n\n\n```\necho \"64 bit MacIntel\"\n```\n\n\nso I would agree the fixes are desirable. \n\nI would search for packages which are building 32-bit. \n\n\n```\n$ file local/lib/* | grep 32-bit\n$ file local/lib/* | grep 32-bit\n```\n\n\nand only bother fixing them. \n\nDave",
    "created_at": "2010-01-27T13:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8063#issuecomment-70673",
    "user": "drkirkby"
}
```

Attachment [gsl-1.10.p2.patch](tarball://root/attachments/some-uuid/ticket8063/gsl-1.10.p2.patch) by drkirkby created at 2010-01-27 13:43:57

I'm not sure I'd personally bother sorting out SAGE64 issues in packages unless they are building 32-bit, which this one is not. 

But you have also removed Michael Abshoff as a maintainer, and also removed the 


```
echo "64 bit MacIntel"
```


so I would agree the fixes are desirable. 

I would search for packages which are building 32-bit. 


```
$ file local/lib/* | grep 32-bit
$ file local/lib/* | grep 32-bit
```


and only bother fixing them. 

Dave



---

archive/issue_comments_070674.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n\n> \n> so I would agree the fixes are desirable. \n> \n\nSo positive review?\n\nJaap",
    "created_at": "2010-01-27T13:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8063#issuecomment-70674",
    "user": "jsp"
}
```

Replying to [comment:2 drkirkby]:

> 
> so I would agree the fixes are desirable. 
> 

So positive review?

Jaap



---

archive/issue_comments_070675.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T14:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8063#issuecomment-70675",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8063#issuecomment-70676",
    "user": "mpatel"
}
```

Resolution: fixed
