# Issue 6438: Upgrade to Cython 0.11.2

archive/issues_006438.json:
```json
{
    "body": "Assignee: mabshoff\n\nAt the very least, native complex support will be valuable. \n\nThe spkg at http://sage.math.washington.edu/home/robertwb/cython/ built and passed all doctests a couple of versions back. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6438\n\n",
    "created_at": "2009-06-28T09:03:55Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Upgrade to Cython 0.11.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6438",
    "user": "@robertwb"
}
```
Assignee: mabshoff

At the very least, native complex support will be valuable. 

The spkg at http://sage.math.washington.edu/home/robertwb/cython/ built and passed all doctests a couple of versions back. 

Issue created by migration from https://trac.sagemath.org/ticket/6438





---

archive/issue_comments_051681.json:
```json
{
    "body": "Here is a direct link: http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.spkg",
    "created_at": "2009-07-17T19:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51681",
    "user": "@mwhansen"
}
```

Here is a direct link: http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.spkg



---

archive/issue_comments_051682.json:
```json
{
    "body": "We should update to the latest tip to fix the numpy issue.",
    "created_at": "2009-07-17T21:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51682",
    "user": "@robertwb"
}
```

We should update to the latest tip to fix the numpy issue.



---

archive/issue_comments_051683.json:
```json
{
    "body": "Does your comment mean that we need a new spkg?  Is this a \"needs work\" ticket now?",
    "created_at": "2009-07-19T03:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51683",
    "user": "@jasongrout"
}
```

Does your comment mean that we need a new spkg?  Is this a "needs work" ticket now?



---

archive/issue_comments_051684.json:
```json
{
    "body": "On the other hand, the spkg seems fine, except that the SPKG.txt file does not include a changelog of any sort.  Shouldn't this be added?",
    "created_at": "2009-07-19T04:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51684",
    "user": "@jasongrout"
}
```

On the other hand, the spkg seems fine, except that the SPKG.txt file does not include a changelog of any sort.  Shouldn't this be added?



---

archive/issue_comments_051685.json:
```json
{
    "body": "http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.1.spkg\n\nI don't see anything in SPKG.txt that needs changing--the changelog would be pretty boring if it was there (\"Upgraded to version x.y.z\" * 100).",
    "created_at": "2009-07-21T19:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51685",
    "user": "@robertwb"
}
```

http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.1.spkg

I don't see anything in SPKG.txt that needs changing--the changelog would be pretty boring if it was there ("Upgraded to version x.y.z" * 100).



---

archive/issue_comments_051686.json:
```json
{
    "body": "Attachment [6438-cython.patch](tarball://root/attachments/some-uuid/ticket6438/6438-cython.patch) by @robertwb created at 2009-07-22 14:19:27\n\nAll tests pass with the above spkg and patch.",
    "created_at": "2009-07-22T14:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51686",
    "user": "@robertwb"
}
```

Attachment [6438-cython.patch](tarball://root/attachments/some-uuid/ticket6438/6438-cython.patch) by @robertwb created at 2009-07-22 14:19:27

All tests pass with the above spkg and patch.



---

archive/issue_comments_051687.json:
```json
{
    "body": "The SPKG at\n\nhttp://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.1.spkg\n\ndoesn't contain a file called `.hgignore` like the current version in Sage 4.1. So when one executes the command\n\n```\nhg status\n```\n\none sees a lot of source files. I've added a `.hgignore` file to the repository of that SPKG. The updated SPKG is up at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/cython-0.11.2.1.spkg\n\nAll doctests passed with the latter SPKG and `6438-cython.patch`.",
    "created_at": "2009-07-24T12:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51687",
    "user": "mvngu"
}
```

The SPKG at

http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.1.spkg

doesn't contain a file called `.hgignore` like the current version in Sage 4.1. So when one executes the command

```
hg status
```

one sees a lot of source files. I've added a `.hgignore` file to the repository of that SPKG. The updated SPKG is up at

http://sage.math.washington.edu/home/mvngu/patch/cython-0.11.2.1.spkg

All doctests passed with the latter SPKG and `6438-cython.patch`.



---

archive/issue_comments_051688.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T13:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6438#issuecomment-51688",
    "user": "mvngu"
}
```

Resolution: fixed
