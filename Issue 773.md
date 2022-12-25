# Issue 773: SAGE drops . from path

archive/issues_000773.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nwas@ubuntu:~/sd5/ant$ export PATH=.:$PATH\nwas@ubuntu:~/sd5/ant$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.5.1, Release Date: 2007-09-26                     |\n| Type notebook() for the GUI, and license() for information.        |\nos.ensage: os.environ['PATH']\n'/home/was/s/local/polymake/bin/:/home/was/s:/home/was/s/local/bin:/home/was/s.dev:/usr/local/bin/:/home/was/bin:/home/was/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/773\n\n",
    "created_at": "2007-10-01T19:05:57Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "SAGE drops . from path",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/773",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
was@ubuntu:~/sd5/ant$ export PATH=.:$PATH
was@ubuntu:~/sd5/ant$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.5.1, Release Date: 2007-09-26                     |
| Type notebook() for the GUI, and license() for information.        |
os.ensage: os.environ['PATH']
'/home/was/s/local/polymake/bin/:/home/was/s:/home/was/s/local/bin:/home/was/s.dev:/usr/local/bin/:/home/was/bin:/home/was/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games'
```


Issue created by migration from https://trac.sagemath.org/ticket/773





---

archive/issue_comments_004600.json:
```json
{
    "body": "I'm guessing this is caused by the following lines from expect.py...\n\n```\n# . in user's path causes *HUGE* trouble, e.g., pexpect will try to\n# run a directory name!\np = os.environ['PATH'].split(':')\nos.environ['PATH'] = ':'.join([v for v in p if v.strip() != '.'])\n```\n\n\nThese lines were added by William Stein:\n\n```\nchangeset:   2329:cccccf17fcd6\nuser:        William Stein <wstein@gmail.com>\ndate:        Thu Jan 11 14:10:46 2007 -0800\nsummary:     Make sure . is not in user's path.\n```\n",
    "created_at": "2007-12-11T02:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/773#issuecomment-4600",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I'm guessing this is caused by the following lines from expect.py...

```
# . in user's path causes *HUGE* trouble, e.g., pexpect will try to
# run a directory name!
p = os.environ['PATH'].split(':')
os.environ['PATH'] = ':'.join([v for v in p if v.strip() != '.'])
```


These lines were added by William Stein:

```
changeset:   2329:cccccf17fcd6
user:        William Stein <wstein@gmail.com>
date:        Thu Jan 11 14:10:46 2007 -0800
summary:     Make sure . is not in user's path.
```




---

archive/issue_comments_004601.json:
```json
{
    "body": "Attachment [trac_773-sage.patch](tarball://root/attachments/some-uuid/ticket773/trac_773-sage.patch) by @williamstein created at 2009-01-23 10:13:44",
    "created_at": "2009-01-23T10:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/773#issuecomment-4601",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_773-sage.patch](tarball://root/attachments/some-uuid/ticket773/trac_773-sage.patch) by @williamstein created at 2009-01-23 10:13:44



---

archive/issue_comments_004602.json:
```json
{
    "body": "The attached new spkg and deleting the code cwitty pointed out completely fixes this problem.",
    "created_at": "2009-01-23T10:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/773#issuecomment-4602",
    "user": "https://github.com/williamstein"
}
```

The attached new spkg and deleting the code cwitty pointed out completely fixes this problem.



---

archive/issue_comments_004603.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-24T14:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/773#issuecomment-4603",
    "user": "https://github.com/rlmill"
}
```

Looks good.



---

archive/issue_comments_004604.json:
```json
{
    "body": "I did some further cleanups in SPKG.txt and also add .hgignore. The result is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/pexpect-2.0.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T17:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/773#issuecomment-4604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I did some further cleanups in SPKG.txt and also add .hgignore. The result is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/pexpect-2.0.p3.spkg

Cheers,

Michael



---

archive/issue_comments_004605.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T18:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/773#issuecomment-4605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_004606.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T18:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/773#issuecomment-4606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
