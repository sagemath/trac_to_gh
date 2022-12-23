# Issue 8217: make 4ti2 an optional package

archive/issues_008217.json:
```json
{
    "body": "Assignee: tbd\n\nThe 4ti2 package should be cleaned up and made into an optional package.\n\nI know of no build issues.  The .DS_Store files from OS X need to be removed, it needs to be under mercurial revision control, and the upstream project should be checked for updates.  After that I know of no reason why this shouldn't be an optional package.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8217\n\n",
    "created_at": "2010-02-08T20:28:50Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "title": "make 4ti2 an optional package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8217",
    "user": "mhampton"
}
```
Assignee: tbd

The 4ti2 package should be cleaned up and made into an optional package.

I know of no build issues.  The .DS_Store files from OS X need to be removed, it needs to be under mercurial revision control, and the upstream project should be checked for updates.  After that I know of no reason why this shouldn't be an optional package.

Issue created by migration from https://trac.sagemath.org/ticket/8217





---

archive/issue_comments_072471.json:
```json
{
    "body": "This seems reasonable. I think this is supposed to be voted on on sage-devel? Also, a link to the spkg would be helpful.",
    "created_at": "2010-02-09T18:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72471",
    "user": "wdj"
}
```

This seems reasonable. I think this is supposed to be voted on on sage-devel? Also, a link to the spkg would be helpful.



---

archive/issue_comments_072472.json:
```json
{
    "body": "See also #5489.",
    "created_at": "2010-02-09T19:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72472",
    "user": "jhpalmieri"
}
```

See also #5489.



---

archive/issue_comments_072473.json:
```json
{
    "body": "Spkg at:\n[http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg)\naddresses all the points above.  Please add to optional packages and remove the 4ti2.p0 package from experimental.",
    "created_at": "2010-10-20T02:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72473",
    "user": "mhampton"
}
```

Spkg at:
[http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg)
addresses all the points above.  Please add to optional packages and remove the 4ti2.p0 package from experimental.



---

archive/issue_comments_072474.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-20T02:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72474",
    "user": "mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072475.json:
```json
{
    "body": "Oops, I reversed the version order, should be this:\n\n[http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg)",
    "created_at": "2011-01-04T21:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72475",
    "user": "mhampton"
}
```

Oops, I reversed the version order, should be this:

[http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg)



---

archive/issue_comments_072476.json:
```json
{
    "body": "At the very least, this should replace the version currently posted, since Marshall's newest version at least installs fine (on 10.6.6 macs and on ubuntu linux), whereas \nthe older version posted on the sage website doesn't install at all.",
    "created_at": "2011-01-17T17:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72476",
    "user": "wdj"
}
```

At the very least, this should replace the version currently posted, since Marshall's newest version at least installs fine (on 10.6.6 macs and on ubuntu linux), whereas 
the older version posted on the sage website doesn't install at all.



---

archive/issue_comments_072477.json:
```json
{
    "body": "I have tested this on OS X 10.5 and 10.6; 64-bit linux (Ubuntu 10.04), and solaris (the machine Mark on skynet).",
    "created_at": "2011-03-22T20:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72477",
    "user": "mhampton"
}
```

I have tested this on OS X 10.5 and 10.6; 64-bit linux (Ubuntu 10.04), and solaris (the machine Mark on skynet).



---

archive/issue_comments_072478.json:
```json
{
    "body": "I just tested 4ti2-1.3.2.p1.spkg on Ubuntu 11.04 with sage-4.7.1 on a 64bit Dell Optiplex.  There were no problems with the installation, and it worked with several calculations involving sandpiles that require 4ti2.",
    "created_at": "2011-09-13T23:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72478",
    "user": "dperkinson"
}
```

I just tested 4ti2-1.3.2.p1.spkg on Ubuntu 11.04 with sage-4.7.1 on a 64bit Dell Optiplex.  There were no problems with the installation, and it worked with several calculations involving sandpiles that require 4ti2.



---

archive/issue_comments_072479.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-13T23:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72479",
    "user": "dperkinson"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072480.json:
```json
{
    "body": "Changing keywords from \"\" to \"sandpiles\".",
    "created_at": "2011-09-16T11:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72480",
    "user": "leif"
}
```

Changing keywords from "" to "sandpiles".



---

archive/issue_comments_072481.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-17T04:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8217#issuecomment-72481",
    "user": "leif"
}
```

Resolution: fixed
