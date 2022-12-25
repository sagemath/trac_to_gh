# Issue 6997: minor typo in Constructions documentation

archive/issues_006997.json:
```json
{
    "body": "Assignee: tba\n\nCC:  mariah.lenox@gmail.com @wdjoyner\n\nMariah Lenox reports a typo in the Construction Guide at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b370c14dea509a7c) thread:\n\n```\nA minor typo in the Constructions documentation.  The\nConstructions documentation says to send corrections\nto sage-devel.\n\n# HG changeset patch\n# User Mariah Lenox <mariah.le...@gmail.com>\n# Date 1253652415 14400\n# Node ID bd65499b09ca9c88108908a609648850433dda8a\n# Parent  40fe66e6c2b07677706fd983a6be6f3eb86060c5\nuser: Mariah Lenox <mariah.le...@gmail.com>\nbranch 'default'\nchanged doc/en/constructions/interface_issues.rst\n\ndiff -r 40fe66e6c2b0 -r bd65499b09ca doc/en/constructions/\ninterface_issues.rst\n--- a/doc/en/constructions/interface_issues.rst Mon Sep 21 09:59:54\n2009 -0400\n+++ b/doc/en/constructions/interface_issues.rst Tue Sep 22 16:46:55\n2009 -0400\n@@ -549,7 +549,7 @@\n some of the GAP databases have to be added separately, and\n Singular. Adding Singular was not easy, due to the difficulty of\n compiling Singular from source. Version 0.9 was released in\n-November. This version when through 34 releases! As of version\n+November. This version went through 34 releases! As of version\n 0.9.34 (definitely by version 0.10.0), Maxima and clisp were\n included with Sage. Version 0.10.0 was released January 12, 2006.\n The release of Sage 1.0 was made early February, 2006. As of\n@@ -559,4 +559,4 @@\n such as assistance in compiling on various OS's. Generally code\n authors are acknowledged in the AUTHOR section of the Python\n docstring of their file and the credits section of the Sage\n-website.\n\\ No newline at end of file\n+website. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6997\n\n",
    "created_at": "2009-09-22T22:22:55Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "minor typo in Constructions documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

CC:  mariah.lenox@gmail.com @wdjoyner

Mariah Lenox reports a typo in the Construction Guide at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b370c14dea509a7c) thread:

```
A minor typo in the Constructions documentation.  The
Constructions documentation says to send corrections
to sage-devel.

# HG changeset patch
# User Mariah Lenox <mariah.le...@gmail.com>
# Date 1253652415 14400
# Node ID bd65499b09ca9c88108908a609648850433dda8a
# Parent  40fe66e6c2b07677706fd983a6be6f3eb86060c5
user: Mariah Lenox <mariah.le...@gmail.com>
branch 'default'
changed doc/en/constructions/interface_issues.rst

diff -r 40fe66e6c2b0 -r bd65499b09ca doc/en/constructions/
interface_issues.rst
--- a/doc/en/constructions/interface_issues.rst Mon Sep 21 09:59:54
2009 -0400
+++ b/doc/en/constructions/interface_issues.rst Tue Sep 22 16:46:55
2009 -0400
@@ -549,7 +549,7 @@
 some of the GAP databases have to be added separately, and
 Singular. Adding Singular was not easy, due to the difficulty of
 compiling Singular from source. Version 0.9 was released in
-November. This version when through 34 releases! As of version
+November. This version went through 34 releases! As of version
 0.9.34 (definitely by version 0.10.0), Maxima and clisp were
 included with Sage. Version 0.10.0 was released January 12, 2006.
 The release of Sage 1.0 was made early February, 2006. As of
@@ -559,4 +559,4 @@
 such as assistance in compiling on various OS's. Generally code
 authors are acknowledged in the AUTHOR section of the Python
 docstring of their file and the credits section of the Sage
-website.
\ No newline at end of file
+website. 
```


Issue created by migration from https://trac.sagemath.org/ticket/6997





---

archive/issue_comments_057758.json:
```json
{
    "body": "Attachment [trac_6997-minor-typo.patch](tarball://root/attachments/some-uuid/ticket6997/trac_6997-minor-typo.patch) by mvngu created at 2009-09-22 22:35:08",
    "created_at": "2009-09-22T22:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6997#issuecomment-57758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6997-minor-typo.patch](tarball://root/attachments/some-uuid/ticket6997/trac_6997-minor-typo.patch) by mvngu created at 2009-09-22 22:35:08



---

archive/issue_comments_057759.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T00:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6997#issuecomment-57759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016422.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-23T00:20:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6997",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6997#event-16422"
}
```



---

archive/issue_comments_057760.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6997#issuecomment-57760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
