# Issue 8077: New python_gnutls-1.1.4.p7.spkg works with Open Solaris 64 bit

archive/issues_008077.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirby was\n\nNow SAGE64=\"yes\" works for Open Solaris too.\n\nThe package can de found here:\n[http://boxen.math.washington.edu/home/jsp/ports/python_gnutls-1.1.4.p7.spkg](http://boxen.math.washington.edu/home/jsp/ports/python_gnutls-1.1.4.p7.spkg)\n\n\n\n```\nWriting /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/python_gnutls-1.1.4-py2.6.egg-info\n\nreal\t0m6.243s\nuser\t0m0.188s\nsys\t0m0.245s\nSuccessfully installed python_gnutls-1.1.4.p7\nYou can safely delete the temporary build directory\n/export/home/jaap/Downloads/sage-4.3.1/spkg/build/python_gnutls-1.1.4.p7\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing python_gnutls-1.1.4.p7.spkg\njaap@opensolaris:~/Downloads/sage-4.3.1$ touch spkg/installed/gnutls-1.1.4.p6\n\n```\n\n\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/8077\n\n",
    "created_at": "2010-01-26T12:25:32Z",
    "labels": [
        "porting",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "New python_gnutls-1.1.4.p7.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8077",
    "user": "jsp"
}
```
Assignee: drkirkby

CC:  drkirby was

Now SAGE64="yes" works for Open Solaris too.

The package can de found here:
[http://boxen.math.washington.edu/home/jsp/ports/python_gnutls-1.1.4.p7.spkg](http://boxen.math.washington.edu/home/jsp/ports/python_gnutls-1.1.4.p7.spkg)



```
Writing /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/python_gnutls-1.1.4-py2.6.egg-info

real	0m6.243s
user	0m0.188s
sys	0m0.245s
Successfully installed python_gnutls-1.1.4.p7
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1/spkg/build/python_gnutls-1.1.4.p7
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python_gnutls-1.1.4.p7.spkg
jaap@opensolaris:~/Downloads/sage-4.3.1$ touch spkg/installed/gnutls-1.1.4.p6

```



Jaap

Issue created by migration from https://trac.sagemath.org/ticket/8077





---

archive/issue_comments_070791.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T12:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8077#issuecomment-70791",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070792.json:
```json
{
    "body": "Attachment [python_gnutls-1.1.4.p7.patch](tarball://root/attachments/some-uuid/ticket8077/python_gnutls-1.1.4.p7.patch) by jsp created at 2010-01-26 18:37:38",
    "created_at": "2010-01-26T18:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8077#issuecomment-70792",
    "user": "jsp"
}
```

Attachment [python_gnutls-1.1.4.p7.patch](tarball://root/attachments/some-uuid/ticket8077/python_gnutls-1.1.4.p7.patch) by jsp created at 2010-01-26 18:37:38



---

archive/issue_comments_070793.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T12:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8077#issuecomment-70793",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070794.json:
```json
{
    "body": "Works fine. Positive review.",
    "created_at": "2010-01-27T12:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8077#issuecomment-70794",
    "user": "drkirkby"
}
```

Works fine. Positive review.



---

archive/issue_comments_070795.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8077#issuecomment-70795",
    "user": "mpatel"
}
```

Resolution: fixed
