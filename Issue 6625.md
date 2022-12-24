# Issue 6625: manually removing executable bits doesn't work

archive/issues_006625.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is a follow up to #3687. Apparently, the issue of executable bits pop up again after they had been manually removed. That is, manually remove the executable bits of sage-banner, sage-gdb-commands, sage-maxima.lisp, and sage-verify-pyc. Then create a source distribution and you see those executable bits restored:\n\n```\n[mvngu@sage bin]$ pwd\n/home/mvngu/release/sage-4.1.1.alpha1/local/bin\n[mvngu@sage bin]$ hg st\nM sage-README-osx.txt\nM sage-banner\nM sage-gdb-commands\nM sage-maxima.lisp\nM sage-verify-pyc\n```\n\nSomewhere a script called by the command\n\n```\nsage -sdist <version-number>\n```\n\nis restoring those executable bits.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6625\n\n",
    "created_at": "2009-07-26T06:50:31Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "manually removing executable bits doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6625",
    "user": "mvngu"
}
```
Assignee: cwitty

This is a follow up to #3687. Apparently, the issue of executable bits pop up again after they had been manually removed. That is, manually remove the executable bits of sage-banner, sage-gdb-commands, sage-maxima.lisp, and sage-verify-pyc. Then create a source distribution and you see those executable bits restored:

```
[mvngu@sage bin]$ pwd
/home/mvngu/release/sage-4.1.1.alpha1/local/bin
[mvngu@sage bin]$ hg st
M sage-README-osx.txt
M sage-banner
M sage-gdb-commands
M sage-maxima.lisp
M sage-verify-pyc
```

Somewhere a script called by the command

```
sage -sdist <version-number>
```

is restoring those executable bits.

Issue created by migration from https://trac.sagemath.org/ticket/6625





---

archive/issue_comments_054277.json:
```json
{
    "body": "Attachment [scripts_6625_no_x_bit.patch](tarball://root/attachments/some-uuid/ticket6625/scripts_6625_no_x_bit.patch) by wjp created at 2010-01-19 02:18:05\n\nThe `sage-make_devel_packages` explicitly set the x bit on all `sage-*` files.",
    "created_at": "2010-01-19T02:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54277",
    "user": "wjp"
}
```

Attachment [scripts_6625_no_x_bit.patch](tarball://root/attachments/some-uuid/ticket6625/scripts_6625_no_x_bit.patch) by wjp created at 2010-01-19 02:18:05

The `sage-make_devel_packages` explicitly set the x bit on all `sage-*` files.



---

archive/issue_comments_054278.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T02:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54278",
    "user": "wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054279.json:
```json
{
    "body": "Attachment [trac_6625-no-x-bit.patch](tarball://root/attachments/some-uuid/ticket6625/trac_6625-no-x-bit.patch) by mvngu created at 2010-01-19 17:26:07\n\nrebased against Sage 4.3.1.rc1; apply to SAGE_LOCAL/bin",
    "created_at": "2010-01-19T17:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54279",
    "user": "mvngu"
}
```

Attachment [trac_6625-no-x-bit.patch](tarball://root/attachments/some-uuid/ticket6625/trac_6625-no-x-bit.patch) by mvngu created at 2010-01-19 17:26:07

rebased against Sage 4.3.1.rc1; apply to SAGE_LOCAL/bin



---

archive/issue_comments_054280.json:
```json
{
    "body": "The attachment [scripts_6625_no_x_bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/scripts_6625_no_x_bit.patch) fails to apply against Sage 4.3.1.rc1:\n\n```\n[mvngu@mod bin]$ pwd\n/dev/shm/mvngu/sage-4.3.1.rc1/local/bin\n[mvngu@mod bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6625/scripts_6625_no_x_bit.patch\nadding scripts_6625_no_x_bit.patch to series file\n[mvngu@mod bin]$ hg qpush\napplying scripts_6625_no_x_bit.patch\npatching file sage-make_devel_packages\nHunk #1 FAILED at 135\n1 out of 1 hunks FAILED -- saving rejects to file sage-make_devel_packages.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh scripts_6625_no_x_bit.patch\n[mvngu@mod bin]$ cat sage-make_devel_packages.rej \n--- sage-make_devel_packages\n+++ sage-make_devel_packages\n@@ -136,6 +136,8 @@\n rm -rf $SCRIPTS\n mkdir $SCRIPTS\n chmod +x sage-*\n+chmod -x sage-README-osx.txt sage-banner sage-gdb-commands\n+chmod -x sage-maxima.lisp sage-verify-pyc\n chmod +x dsage_*\n rm sage-*~\n```\n\nThe failure results from #7975, which removes dsage from Sage and the patches on #7975 have been merged in Sage 4.3.1.rc1. The guilty line from [scripts_6625_no_x_bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/scripts_6625_no_x_bit.patch) is:\n\n```\n139\t141\tchmod +x dsage_*\n```\n\nEssentially the patch looks good. I have rebased it against Sage 4.3.1.rc1, so only my rebase [trac_6625-no-x-bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/trac_6625-no-x-bit.patch) needs reviewing.",
    "created_at": "2010-01-19T17:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54280",
    "user": "mvngu"
}
```

The attachment [scripts_6625_no_x_bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/scripts_6625_no_x_bit.patch) fails to apply against Sage 4.3.1.rc1:

```
[mvngu@mod bin]$ pwd
/dev/shm/mvngu/sage-4.3.1.rc1/local/bin
[mvngu@mod bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6625/scripts_6625_no_x_bit.patch
adding scripts_6625_no_x_bit.patch to series file
[mvngu@mod bin]$ hg qpush
applying scripts_6625_no_x_bit.patch
patching file sage-make_devel_packages
Hunk #1 FAILED at 135
1 out of 1 hunks FAILED -- saving rejects to file sage-make_devel_packages.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh scripts_6625_no_x_bit.patch
[mvngu@mod bin]$ cat sage-make_devel_packages.rej 
--- sage-make_devel_packages
+++ sage-make_devel_packages
@@ -136,6 +136,8 @@
 rm -rf $SCRIPTS
 mkdir $SCRIPTS
 chmod +x sage-*
+chmod -x sage-README-osx.txt sage-banner sage-gdb-commands
+chmod -x sage-maxima.lisp sage-verify-pyc
 chmod +x dsage_*
 rm sage-*~
```

The failure results from #7975, which removes dsage from Sage and the patches on #7975 have been merged in Sage 4.3.1.rc1. The guilty line from [scripts_6625_no_x_bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/scripts_6625_no_x_bit.patch) is:

```
139	141	chmod +x dsage_*
```

Essentially the patch looks good. I have rebased it against Sage 4.3.1.rc1, so only my rebase [trac_6625-no-x-bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/trac_6625-no-x-bit.patch) needs reviewing.



---

archive/issue_comments_054281.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T17:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54281",
    "user": "wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054282.json:
```json
{
    "body": "Thanks. The rebase looks good to me.",
    "created_at": "2010-01-19T17:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54282",
    "user": "wjp"
}
```

Thanks. The rebase looks good to me.



---

archive/issue_comments_054283.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T02:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54283",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054284.json:
```json
{
    "body": "Merged [trac_6625-no-x-bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/trac_6625-no-x-bit.patch) in the script repository.",
    "created_at": "2010-01-24T02:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6625#issuecomment-54284",
    "user": "mvngu"
}
```

Merged [trac_6625-no-x-bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/trac_6625-no-x-bit.patch) in the script repository.
