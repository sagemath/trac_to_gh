# Issue 9950: Missing package init file 'sage/tests/french_book/__init__.py'

archive/issues_009950.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  ylchapuy @zimmermann6\n\nRunning `sage -b` with 4.6.alpha1 gives:\n\n```\n[...]\nrunning build_py\npackage init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)\npackage init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)\nrunning build_ext\n[...]\n```\n\nThe solution is to add an \"empty\" `__init__.py` file.  Mercurial may complain if the file is truly empty.  We can use \n\n # This comment is here so the file is non-empty (so Mercurial will check it in).\n\nsay, instead.\n\nThis is a follow-up to #9395.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9951\n\n",
    "created_at": "2010-09-19T21:36:49Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Missing package init file 'sage/tests/french_book/__init__.py'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9950",
    "user": "https://github.com/qed777"
}
```
Assignee: @jasongrout

CC:  ylchapuy @zimmermann6

Running `sage -b` with 4.6.alpha1 gives:

```
[...]
running build_py
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
running build_ext
[...]
```

The solution is to add an "empty" `__init__.py` file.  Mercurial may complain if the file is truly empty.  We can use 

 # This comment is here so the file is non-empty (so Mercurial will check it in).

say, instead.

This is a follow-up to #9395.

Issue created by migration from https://trac.sagemath.org/ticket/9951





---

archive/issue_comments_099075.json:
```json
{
    "body": "I made the mistake the other day of creating an empty file. Mercruial checked it in OK.",
    "created_at": "2010-09-19T21:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99075",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I made the mistake the other day of creating an empty file. Mercruial checked it in OK.



---

archive/issue_comments_099076.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> I made the mistake the other day of creating an empty file. Mercruial checked it in OK. \n\nYeah, it is properly checked it, but exporting it gives\n\n```\n# HG changeset patch\n# User Leif Leonhardy <not.really@online.de>\n# Date 1284952693 -7200\n# Node ID eb739c32247985cc9923bb8dbdebf1f7eb404666\n# Parent  81b3de2e81408620d6d68f022cd7d834880fa029\n#9951 Add (empty) sage/tests/french_book/__init__.py file to avoid warnings.\n\n# HG changeset patch\n# User Leif Leonhardy <not.really@online.de>\n# Date 1284953161 -7200\n# Node ID 87a65b1dbf4f7fc9dd0e468724924363e0d9072c\n# Parent  eb739c32247985cc9923bb8dbdebf1f7eb404666\n#9951 ... and fill it such that Mercurial will produce a proper patch :/\n\ndiff -r eb739c322479 -r 87a65b1dbf4f sage/tests/french_book/__init__.py\n--- a/sage/tests/french_book/__init__.py\tMon Sep 20 05:18:13 2010 +0200\n+++ b/sage/tests/french_book/__init__.py\tMon Sep 20 05:26:01 2010 +0200\n@@ -0,0 +1,1 @@\n+# This comment is here so the file is non-empty (so Mercurial will check it in).\n```\n\n(I.e., the patch(es) won't apply properly.) :/",
    "created_at": "2010-09-20T03:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99076",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:2 drkirkby]:
> I made the mistake the other day of creating an empty file. Mercruial checked it in OK. 

Yeah, it is properly checked it, but exporting it gives

```
# HG changeset patch
# User Leif Leonhardy <not.really@online.de>
# Date 1284952693 -7200
# Node ID eb739c32247985cc9923bb8dbdebf1f7eb404666
# Parent  81b3de2e81408620d6d68f022cd7d834880fa029
#9951 Add (empty) sage/tests/french_book/__init__.py file to avoid warnings.

# HG changeset patch
# User Leif Leonhardy <not.really@online.de>
# Date 1284953161 -7200
# Node ID 87a65b1dbf4f7fc9dd0e468724924363e0d9072c
# Parent  eb739c32247985cc9923bb8dbdebf1f7eb404666
#9951 ... and fill it such that Mercurial will produce a proper patch :/

diff -r eb739c322479 -r 87a65b1dbf4f sage/tests/french_book/__init__.py
--- a/sage/tests/french_book/__init__.py	Mon Sep 20 05:18:13 2010 +0200
+++ b/sage/tests/french_book/__init__.py	Mon Sep 20 05:26:01 2010 +0200
@@ -0,0 +1,1 @@
+# This comment is here so the file is non-empty (so Mercurial will check it in).
```

(I.e., the patch(es) won't apply properly.) :/



---

archive/issue_comments_099077.json:
```json
{
    "body": "Apply to Sage library",
    "created_at": "2010-09-20T03:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99077",
    "user": "https://github.com/nexttime"
}
```

Apply to Sage library



---

archive/issue_comments_099078.json:
```json
{
    "body": "Attachment [trac_9951-add_non-empty_fake_init_file_to_tests_french_book.patch](tarball://root/attachments/some-uuid/ticket9951/trac_9951-add_non-empty_fake_init_file_to_tests_french_book.patch) by @nexttime created at 2010-09-20 03:44:02\n\n*Non-empty* patch is up.",
    "created_at": "2010-09-20T03:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99078",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_9951-add_non-empty_fake_init_file_to_tests_french_book.patch](tarball://root/attachments/some-uuid/ticket9951/trac_9951-add_non-empty_fake_init_file_to_tests_french_book.patch) by @nexttime created at 2010-09-20 03:44:02

*Non-empty* patch is up.



---

archive/issue_comments_099079.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-20T03:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99079",
    "user": "https://github.com/nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099080.json:
```json
{
    "body": "sorry, I don't know how to review this patch. On my side, `sage -b` works with the vanilla\nsage-4.6.alpha1.",
    "created_at": "2010-09-20T07:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99080",
    "user": "https://github.com/zimmermann6"
}
```

sorry, I don't know how to review this patch. On my side, `sage -b` works with the vanilla
sage-4.6.alpha1.



---

archive/issue_comments_099081.json:
```json
{
    "body": "Replying to [comment:5 zimmerma]:\n> sorry, I don't know how to review this patch. On my side, `sage -b` works with the vanilla\n> sage-4.6.alpha1.\n\nIf it wouldn't **work**, the priority of this ticket would be *blocker* rather than *minor*. ;-)\n\nThe patch just avoids potentially annoying or confusing warning messages.\n \nTo see the difference, do for example:\n\n```sh\n~/Sage/sage-4.6.alpha1/devel/sage-main$ touch sage/tests/french_book/numbertheory.py \n~/Sage/sage-4.6.alpha1/devel/sage-main$ ../../sage -b     \n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nExecute 0 commands (using 0 threads)\nTime to execute 0 commands: 0.0640869140625 seconds\nFinished compiling Cython code (time = 0.421274900436 seconds)\nrunning install\nrunning build\nrunning build_py\npackage init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)\ncopying sage/tests/french_book/numbertheory.py -> build/lib.linux-x86_64-2.6/sage/tests/french_book\npackage init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.0187819004059 seconds.\nrunning install_lib\ncopying build/lib.linux-x86_64-2.6/sage/tests/french_book/numbertheory.py -> /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book\nbyte-compiling /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book/numbertheory.py to numbertheory.pyc\nrunning install_egg_info\nRemoving /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n\nreal\t0m1.590s\nuser\t0m1.110s\nsys\t0m0.300s\n```\n\n\nThen apply the patch and retry it. (In fact, you should not even have to touch the file, the messages should be there regardless of files being modified or not.)",
    "created_at": "2010-09-20T12:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99081",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 zimmerma]:
> sorry, I don't know how to review this patch. On my side, `sage -b` works with the vanilla
> sage-4.6.alpha1.

If it wouldn't **work**, the priority of this ticket would be *blocker* rather than *minor*. ;-)

The patch just avoids potentially annoying or confusing warning messages.
 
To see the difference, do for example:

```sh
~/Sage/sage-4.6.alpha1/devel/sage-main$ touch sage/tests/french_book/numbertheory.py 
~/Sage/sage-4.6.alpha1/devel/sage-main$ ../../sage -b     
----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Execute 0 commands (using 0 threads)
Time to execute 0 commands: 0.0640869140625 seconds
Finished compiling Cython code (time = 0.421274900436 seconds)
running install
running build
running build_py
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
copying sage/tests/french_book/numbertheory.py -> build/lib.linux-x86_64-2.6/sage/tests/french_book
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
running build_ext
Total time spent compiling C/C++ extensions:  0.0187819004059 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/tests/french_book/numbertheory.py -> /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book
byte-compiling /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book/numbertheory.py to numbertheory.pyc
running install_egg_info
Removing /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m1.590s
user	0m1.110s
sys	0m0.300s
```


Then apply the patch and retry it. (In fact, you should not even have to touch the file, the messages should be there regardless of files being modified or not.)



---

archive/issue_comments_099082.json:
```json
{
    "body": "with the patch, I get:\n\n```\ntarte% ../../sage -b\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTime to execute 0 commands: 1.09672546387e-05 seconds\nFinished compiling Cython code (time = 0.345225095749 seconds)\nrunning install\nrunning build\nrunning build_py\ncopying sage/tests/french_book/__init__.py -> build/lib.linux-x86_64-2.6/sage/tests/french_book\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.017902135849 seconds.\nrunning install_lib\ncopying build/lib.linux-x86_64-2.6/sage/tests/french_book/__init__.py -> /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book\nbyte-compiling /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book/__init__.py to __init__.pyc\nrunning install_egg_info\nRemoving /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n\nreal    0m1.459s\nuser    0m1.145s\nsys     0m0.233s\n```\n\nthus a positive review.\n\nPaul",
    "created_at": "2010-09-21T07:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99082",
    "user": "https://github.com/zimmermann6"
}
```

with the patch, I get:

```
tarte% ../../sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 1.09672546387e-05 seconds
Finished compiling Cython code (time = 0.345225095749 seconds)
running install
running build
running build_py
copying sage/tests/french_book/__init__.py -> build/lib.linux-x86_64-2.6/sage/tests/french_book
running build_ext
Total time spent compiling C/C++ extensions:  0.017902135849 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/tests/french_book/__init__.py -> /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book
byte-compiling /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book/__init__.py to __init__.pyc
running install_egg_info
Removing /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real    0m1.459s
user    0m1.145s
sys     0m0.233s
```

thus a positive review.

Paul



---

archive/issue_comments_099083.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-21T07:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99083",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099084.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9950#issuecomment-99084",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_010079.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T09:11:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9950",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9950#event-10079"
}
```
