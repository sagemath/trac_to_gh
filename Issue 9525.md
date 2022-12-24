# Issue 9525: Installation of cvxopt will always report succesful, even if it fails.

archive/issues_009525.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jdemeyer\n\nWhilst trying to locate a bug causing a 64-bit build of Sage on Solaris to be unstable, I found that cvxopt will always report it has successfully installed, even if it does not. The last line in `spkg-install` is\n\n\n```\npython setup.py install\n```\n\n\nwith no error checking. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9525\n\n",
    "created_at": "2010-07-17T08:32:55Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Installation of cvxopt will always report succesful, even if it fails.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9525",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jdemeyer

Whilst trying to locate a bug causing a 64-bit build of Sage on Solaris to be unstable, I found that cvxopt will always report it has successfully installed, even if it does not. The last line in `spkg-install` is


```
python setup.py install
```


with no error checking. 



Issue created by migration from https://trac.sagemath.org/ticket/9525





---

archive/issue_comments_091642.json:
```json
{
    "body": "This needs to be coordinated with #6456",
    "created_at": "2010-07-17T18:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9525#issuecomment-91642",
    "user": "@mwhansen"
}
```

This needs to be coordinated with #6456



---

archive/issue_comments_091643.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-26T15:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9525#issuecomment-91643",
    "user": "@dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091644.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> This needs to be coordinated with #6456\n\nthis is done in my latest update just submitted on #6456",
    "created_at": "2010-07-26T15:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9525#issuecomment-91644",
    "user": "@dimpase"
}
```

Replying to [comment:1 mhansen]:
> This needs to be coordinated with #6456

this is done in my latest update just submitted on #6456



---

archive/issue_comments_091645.json:
```json
{
    "body": "Note that #6456 has been merged; can this be closed (i.e., was it in fact fixed in that spkg) once that receives positive review?",
    "created_at": "2010-12-02T16:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9525#issuecomment-91645",
    "user": "@kcrisman"
}
```

Note that #6456 has been merged; can this be closed (i.e., was it in fact fixed in that spkg) once that receives positive review?



---

archive/issue_comments_091646.json:
```json
{
    "body": "To release manager: this one should be closed, as far as all the information suggests.",
    "created_at": "2011-01-19T21:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9525#issuecomment-91646",
    "user": "@kcrisman"
}
```

To release manager: this one should be closed, as far as all the information suggests.



---

archive/issue_comments_091647.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-01-19T22:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9525#issuecomment-91647",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
