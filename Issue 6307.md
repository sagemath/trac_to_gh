# Issue 6307: Move javascript out of python-land

archive/issues_006307.json:
```json
{
    "body": "Assignee: tbd\n\nAs Mike Hansen noted in #5564, the javascript shouldn't be in a python file in triple-quoted strings.  Unfortunately, the patch he submitted to do this bitrotted. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6307\n\n",
    "created_at": "2009-06-16T05:42:28Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Move javascript out of python-land",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6307",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tbd

As Mike Hansen noted in #5564, the javascript shouldn't be in a python file in triple-quoted strings.  Unfortunately, the patch he submitted to do this bitrotted. 

Issue created by migration from https://trac.sagemath.org/ticket/6307





---

archive/issue_comments_050234.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-06-16T05:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50234",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_050235.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2009-06-16T05:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50235",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_050236.json:
```json
{
    "body": "In #5564, mhansen mentioned that this patch breaks history; if anyone really cares about preserving history, it's easy enough with `hg cp`. I made a version of this patch which does exactly the same thing with respect to file contents, but also tells Mercurial about the history: http://sage.math.washington.edu/home/drake/6307bis.patch\n\n(It's rather bigger than the patch on this ticket because it's diffing the new .js files against js.py, instead of /dev/null.)",
    "created_at": "2009-06-18T00:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50236",
    "user": "https://github.com/dandrake"
}
```

In #5564, mhansen mentioned that this patch breaks history; if anyone really cares about preserving history, it's easy enough with `hg cp`. I made a version of this patch which does exactly the same thing with respect to file contents, but also tells Mercurial about the history: http://sage.math.washington.edu/home/drake/6307bis.patch

(It's rather bigger than the patch on this ticket because it's diffing the new .js files against js.py, instead of /dev/null.)



---

archive/issue_comments_050237.json:
```json
{
    "body": "Attachment [6307bis.patch](tarball://root/attachments/some-uuid/ticket6307/6307bis.patch) by boothby created at 2009-06-18 02:33:15\n\nVery nice, I didn't know that functionality existed.",
    "created_at": "2009-06-18T02:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50237",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [6307bis.patch](tarball://root/attachments/some-uuid/ticket6307/6307bis.patch) by boothby created at 2009-06-18 02:33:15

Very nice, I didn't know that functionality existed.



---

archive/issue_comments_050238.json:
```json
{
    "body": "doctest failure in psage.py",
    "created_at": "2009-06-20T18:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50238",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

doctest failure in psage.py



---

archive/issue_comments_050239.json:
```json
{
    "body": "I can't reproduce the error in psage.py... I'm re-marking this as a positive review.",
    "created_at": "2009-07-09T19:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50239",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I can't reproduce the error in psage.py... I'm re-marking this as a positive review.



---

archive/issue_comments_050240.json:
```json
{
    "body": "reviewer patch; fixes typos",
    "created_at": "2009-07-16T11:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch; fixes typos



---

archive/issue_comments_050241.json:
```json
{
    "body": "Attachment [trac_6307-reviewer.patch](tarball://root/attachments/some-uuid/ticket6307/trac_6307-reviewer.patch) by mvngu created at 2009-07-16 11:32:48",
    "created_at": "2009-07-16T11:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6307-reviewer.patch](tarball://root/attachments/some-uuid/ticket6307/trac_6307-reviewer.patch) by mvngu created at 2009-07-16 11:32:48



---

archive/issue_comments_050242.json:
```json
{
    "body": "Once this ticket is closed, ticket #5564 should also be closed as a consequence of the patches on this ticket. Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T11:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Once this ticket is closed, ticket #5564 should also be closed as a consequence of the patches on this ticket. Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_050243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050244.json:
```json
{
    "body": "This ticket results in a corrupt repository. After merging this ticket in Sage 4.1.1.alpha0, I created a source distribution with `sage -sdist 4.1.1.alpha0`. Now compile that source distribution, then cd to `SAGE_ROOT/devel/sage-main` and do:\n\n```\n[mvngu@sage sage-main]$ hg st\n! sage/server/notebook/templates/async_lib.js\n! sage/server/notebook/templates/jmol_lib.js\n! sage/server/notebook/templates/notebook_lib.js\n```\n\nI'm marking this ticket as \"needs work\" and reverting it in my merge tree.",
    "created_at": "2009-07-22T17:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This ticket results in a corrupt repository. After merging this ticket in Sage 4.1.1.alpha0, I created a source distribution with `sage -sdist 4.1.1.alpha0`. Now compile that source distribution, then cd to `SAGE_ROOT/devel/sage-main` and do:

```
[mvngu@sage sage-main]$ hg st
! sage/server/notebook/templates/async_lib.js
! sage/server/notebook/templates/jmol_lib.js
! sage/server/notebook/templates/notebook_lib.js
```

I'm marking this ticket as "needs work" and reverting it in my merge tree.



---

archive/issue_comments_050245.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-22T17:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_050246.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-22T17:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_050247.json:
```json
{
    "body": "Working on a fix for this right now...",
    "created_at": "2009-07-22T17:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50247",
    "user": "https://github.com/rlmill"
}
```

Working on a fix for this right now...



---

archive/issue_comments_050248.json:
```json
{
    "body": "Rather, I have a fix, but the sdist command is taking a long time. Once that is done I can confirm that it worked.",
    "created_at": "2009-07-22T17:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50248",
    "user": "https://github.com/rlmill"
}
```

Rather, I have a fix, but the sdist command is taking a long time. Once that is done I can confirm that it worked.



---

archive/issue_comments_050249.json:
```json
{
    "body": "Attachment [trac_6307-manifest.in.patch](tarball://root/attachments/some-uuid/ticket6307/trac_6307-manifest.in.patch) by @rlmill created at 2009-07-22 18:08:58\n\nIt works!\n\n\n```\n[rlm-book templates]$ pwd\n/Users/rlmill/sage-4.1.1.alpha0.6307/dist/sage-4.1.1.alpha0.fix.test/spkg/standard/sage-4.1.1.alpha0.fix.test/sage/server/notebook/templates\n[rlm-book templates]$ ls\ntotal 208K\n-rw-r--r-- 1 rlmill  786 2009-07-22 10:23 account_recovery.html\n-rw-r--r-- 1 rlmill 1.5K 2009-07-22 10:23 account_settings.html\n-rw-r--r-- 1 rlmill  729 2009-07-22 10:23 async_lib.js\n-rw-r--r-- 1 rlmill  448 2009-07-22 10:23 banner.html\n-rw-r--r-- 1 rlmill  467 2009-07-22 10:23 base.html\n-rw-r--r-- 1 rlmill  440 2009-07-22 10:23 base_authenticated.html\n-rw-r--r-- 1 rlmill 2.8K 2009-07-22 10:23 docs.html\n-rw-r--r-- 1 rlmill  324 2009-07-22 10:23 error_message.html\n-rw-r--r-- 1 rlmill  534 2009-07-22 10:23 history.html\n-rw-r--r-- 1 rlmill 1.2K 2009-07-22 10:23 jmol_lib.js\n-rw-r--r-- 1 rlmill  385 2009-07-22 10:23 list_top.html\n-rw-r--r-- 1 rlmill 2.8K 2009-07-22 10:23 login.html\n-rw-r--r-- 1 rlmill 117K 2009-07-22 10:23 notebook_lib.js\n-rw-r--r-- 1 rlmill 2.3K 2009-07-22 10:23 registration.html\n-rw-r--r-- 1 rlmill  284 2009-07-22 10:23 search.html\n-rw-r--r-- 1 rlmill  780 2009-07-22 10:23 source_code.html\n-rw-r--r-- 1 rlmill  220 2009-07-22 10:23 template_error.html\n-rw-r--r-- 1 rlmill 1.3K 2009-07-22 10:23 top_bar.html\n-rw-r--r-- 1 rlmill 1.2K 2009-07-22 10:23 upload.html\n-rw-r--r-- 1 rlmill  324 2009-07-22 10:23 user_management.html\n-rw-r--r-- 1 rlmill 6.7K 2009-07-22 10:23 worksheet_listing.html\n-rw-r--r-- 1 rlmill  280 2009-07-22 10:23 yes_no.html\n```\n",
    "created_at": "2009-07-22T18:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50249",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6307-manifest.in.patch](tarball://root/attachments/some-uuid/ticket6307/trac_6307-manifest.in.patch) by @rlmill created at 2009-07-22 18:08:58

It works!


```
[rlm-book templates]$ pwd
/Users/rlmill/sage-4.1.1.alpha0.6307/dist/sage-4.1.1.alpha0.fix.test/spkg/standard/sage-4.1.1.alpha0.fix.test/sage/server/notebook/templates
[rlm-book templates]$ ls
total 208K
-rw-r--r-- 1 rlmill  786 2009-07-22 10:23 account_recovery.html
-rw-r--r-- 1 rlmill 1.5K 2009-07-22 10:23 account_settings.html
-rw-r--r-- 1 rlmill  729 2009-07-22 10:23 async_lib.js
-rw-r--r-- 1 rlmill  448 2009-07-22 10:23 banner.html
-rw-r--r-- 1 rlmill  467 2009-07-22 10:23 base.html
-rw-r--r-- 1 rlmill  440 2009-07-22 10:23 base_authenticated.html
-rw-r--r-- 1 rlmill 2.8K 2009-07-22 10:23 docs.html
-rw-r--r-- 1 rlmill  324 2009-07-22 10:23 error_message.html
-rw-r--r-- 1 rlmill  534 2009-07-22 10:23 history.html
-rw-r--r-- 1 rlmill 1.2K 2009-07-22 10:23 jmol_lib.js
-rw-r--r-- 1 rlmill  385 2009-07-22 10:23 list_top.html
-rw-r--r-- 1 rlmill 2.8K 2009-07-22 10:23 login.html
-rw-r--r-- 1 rlmill 117K 2009-07-22 10:23 notebook_lib.js
-rw-r--r-- 1 rlmill 2.3K 2009-07-22 10:23 registration.html
-rw-r--r-- 1 rlmill  284 2009-07-22 10:23 search.html
-rw-r--r-- 1 rlmill  780 2009-07-22 10:23 source_code.html
-rw-r--r-- 1 rlmill  220 2009-07-22 10:23 template_error.html
-rw-r--r-- 1 rlmill 1.3K 2009-07-22 10:23 top_bar.html
-rw-r--r-- 1 rlmill 1.2K 2009-07-22 10:23 upload.html
-rw-r--r-- 1 rlmill  324 2009-07-22 10:23 user_management.html
-rw-r--r-- 1 rlmill 6.7K 2009-07-22 10:23 worksheet_listing.html
-rw-r--r-- 1 rlmill  280 2009-07-22 10:23 yes_no.html
```




---

archive/issue_comments_050250.json:
```json
{
    "body": "The new patch should fix the repository issues.",
    "created_at": "2009-07-22T18:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50250",
    "user": "https://github.com/jhpalmieri"
}
```

The new patch should fix the repository issues.



---

archive/issue_comments_050251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T09:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6307#issuecomment-50251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
