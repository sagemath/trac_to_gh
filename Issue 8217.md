# Issue 8217: make 4ti2 an optional package

archive/issues_008217.json:
```json
{
    "body": "Assignee: tbd\n\nThe 4ti2 package should be cleaned up and made into an optional package.\n\nI know of no build issues.  The .DS_Store files from OS X need to be removed, it needs to be under mercurial revision control, and the upstream project should be checked for updates.  After that I know of no reason why this shouldn't be an optional package.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8217\n\n",
    "created_at": "2010-02-08T20:28:50Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "make 4ti2 an optional package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: tbd

The 4ti2 package should be cleaned up and made into an optional package.

I know of no build issues.  The .DS_Store files from OS X need to be removed, it needs to be under mercurial revision control, and the upstream project should be checked for updates.  After that I know of no reason why this shouldn't be an optional package.

Issue created by migration from https://trac.sagemath.org/ticket/8217





---

archive/issue_comments_072349.json:
```json
{
    "body": "This seems reasonable. I think this is supposed to be voted on on sage-devel? Also, a link to the spkg would be helpful.",
    "created_at": "2010-02-09T18:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72349",
    "user": "https://github.com/wdjoyner"
}
```

This seems reasonable. I think this is supposed to be voted on on sage-devel? Also, a link to the spkg would be helpful.



---

archive/issue_comments_072350.json:
```json
{
    "body": "See also #5489.",
    "created_at": "2010-02-09T19:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72350",
    "user": "https://github.com/jhpalmieri"
}
```

See also #5489.



---

archive/issue_comments_072351.json:
```json
{
    "body": "Spkg at:\n[http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg)\naddresses all the points above.  Please add to optional packages and remove the 4ti2.p0 package from experimental.",
    "created_at": "2010-10-20T02:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72351",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Spkg at:
[http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg)
addresses all the points above.  Please add to optional packages and remove the 4ti2.p0 package from experimental.



---

archive/issue_comments_072352.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-20T02:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72352",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072353.json:
```json
{
    "body": "Oops, I reversed the version order, should be this:\n\n[http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg)",
    "created_at": "2011-01-04T21:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72353",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Oops, I reversed the version order, should be this:

[http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg)



---

archive/issue_comments_072354.json:
```json
{
    "body": "At the very least, this should replace the version currently posted, since Marshall's newest version at least installs fine (on 10.6.6 macs and on ubuntu linux), whereas \nthe older version posted on the sage website doesn't install at all.",
    "created_at": "2011-01-17T17:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72354",
    "user": "https://github.com/wdjoyner"
}
```

At the very least, this should replace the version currently posted, since Marshall's newest version at least installs fine (on 10.6.6 macs and on ubuntu linux), whereas 
the older version posted on the sage website doesn't install at all.



---

archive/issue_comments_072355.json:
```json
{
    "body": "I have tested this on OS X 10.5 and 10.6; 64-bit linux (Ubuntu 10.04), and solaris (the machine Mark on skynet).",
    "created_at": "2011-03-22T20:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I have tested this on OS X 10.5 and 10.6; 64-bit linux (Ubuntu 10.04), and solaris (the machine Mark on skynet).



---

archive/issue_comments_072356.json:
```json
{
    "body": "I just tested 4ti2-1.3.2.p1.spkg on Ubuntu 11.04 with sage-4.7.1 on a 64bit Dell Optiplex.  There were no problems with the installation, and it worked with several calculations involving sandpiles that require 4ti2.",
    "created_at": "2011-09-13T23:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72356",
    "user": "https://trac.sagemath.org/admin/accounts/users/dperkinson"
}
```

I just tested 4ti2-1.3.2.p1.spkg on Ubuntu 11.04 with sage-4.7.1 on a 64bit Dell Optiplex.  There were no problems with the installation, and it worked with several calculations involving sandpiles that require 4ti2.



---

archive/issue_comments_072357.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-13T23:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72357",
    "user": "https://trac.sagemath.org/admin/accounts/users/dperkinson"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072358.json:
```json
{
    "body": "Changing keywords from \"\" to \"sandpiles\".",
    "created_at": "2011-09-16T11:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72358",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "sandpiles".



---

archive/issue_comments_072359.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-17T04:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72359",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed



---

archive/issue_events_008419.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2011-09-17T04:31:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8217#event-8419"
}
```
