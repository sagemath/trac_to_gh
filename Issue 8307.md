# Issue 8307: gfan-0.4plu keeps getting upgraded

archive/issues_008307.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  mvngu\n\nI think this happens because we misuse [rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip) in `SAGE_LOCAL/bin/sage-update`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8307\n\n",
    "created_at": "2010-02-19T12:36:24Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "gfan-0.4plu keeps getting upgraded",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8307",
    "user": "https://github.com/qed777"
}
```
Assignee: GeorgSWeber

CC:  mvngu

I think this happens because we misuse [rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip) in `SAGE_LOCAL/bin/sage-update`.

Issue created by migration from https://trac.sagemath.org/ticket/8307





---

archive/issue_comments_073568.json:
```json
{
    "body": "Fix rstrip problems.  Various cleanups.  scripts repo.",
    "created_at": "2010-02-19T14:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8307#issuecomment-73568",
    "user": "https://github.com/qed777"
}
```

Fix rstrip problems.  Various cleanups.  scripts repo.



---

archive/issue_comments_073569.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-19T14:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8307#issuecomment-73569",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073570.json:
```json
{
    "body": "Attachment [trac_8307-update_sage-update.patch](tarball://root/attachments/some-uuid/ticket8307/trac_8307-update_sage-update.patch) by @qed777 created at 2010-02-19 14:30:01\n\nThe patch\n\n* Fixes `rstrip` problems.\n* Includes pep8-related cleanup and cosmetic changes.\n* Uses [textwrap](http://docs.python.org/library/textwrap.html).\n\nFeel free to make further improvements, or to undo mine!",
    "created_at": "2010-02-19T14:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8307#issuecomment-73570",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8307-update_sage-update.patch](tarball://root/attachments/some-uuid/ticket8307/trac_8307-update_sage-update.patch) by @qed777 created at 2010-02-19 14:30:01

The patch

* Fixes `rstrip` problems.
* Includes pep8-related cleanup and cosmetic changes.
* Uses [textwrap](http://docs.python.org/library/textwrap.html).

Feel free to make further improvements, or to undo mine!



---

archive/issue_comments_073571.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-20T10:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8307#issuecomment-73571",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073572.json:
```json
{
    "body": "Based on a freshly compiled Sage 4.3.3.alpha1, I made a source distribution called sage-4.3.3.alpha1.1, which is essentially the same as Sage 4.3.3.alpha1. From a Sage 4.3.3.alpha1 binary, I upgraded it to sage-4.3.3.alpha1.1 and received the following upgrade message:\n\n```\nThe following packages will be upgraded:\n  examples-4.3.3.alpha1.1 extcode-4.3.3.alpha1.1 gfan-0.4plu sage-4.3.3.alpha1.1 sage_scripts-4.3.3.alpha1.1\n```\n\nI didn't make any changes to the gfan spkg and yet it is slated for upgrading. After upgrading the Sage library, I received the following message about upgrading gfan:\n\n```\nDone\nThe following packages will be upgraded:\n  gfan-0.4plu\n```\n\nAnswering yes to the upgrade, the install log shows this line:\n\n```\ngfan-0.4plus.spkg already present\n```\n\nYep, it's redudant and annoying that gfan is upgraded everytime one does a source upgrade.\n\n\n\n\nHere's another try. With a freshly compiled Sage 4.3.3.alpha1, I applied [trac_8307-update_sage-update.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8307/trac_8307-update_sage-update.patch) to the scripts repository and produced a source distribution sage-4.3.3.alpha1.1. I then applied that same patch on top of a binary version of Sage 4.3.3.alpha1 and upgraded that binary distribution to sage-4.3.3.alpha1.1. This time the upgrade message reads:\n\n```\nThe following packages will be upgraded:\n\n    examples-4.3.3.alpha1.1 extcode-4.3.3.alpha1.1 sage-4.3.3.alpha1.1\n    sage_scripts-4.3.3.alpha1.1\n```\n\nwith no gfan within sight. The upgrade process didn't upgrade gfan.\n\n\n\n\nThe patch moves some code to the following conditional at the end of `sage-update`:\n\n```\nif __name__ == '__main__':\n   <SNIP>\n```\n\nThere are some clean up of docstrings and clean up conforming to PEP8. The real change is in adding the new function `chop()` and using it as follows:\n\n```\n-    installed = set(os.listdir(\"%s/installed/\"%SPKG_ROOT))\n-    to_download = [x for x in packages if not x.rstrip('.spkg') in installed]\n+    installed = set(os.listdir(\"%s/installed/\" % SPKG_ROOT))\n+    to_download = [x for x in packages if not chop(x, '.spkg') in installed]\n\n```\n\nPreviously, the script `sage-update` used `rstrip()` for finding a list of spkg's to upgrade. This function won't work as intended for spkg's that has an \"s\" at the end of their names just before the extension \".spkg\". The new function `chop()` does this better by testing that the name of an spkg actually ends in \".spkg\". That's why the update script wants to upgrade \"gfan-0.4plu\" when the gfan spkg is named \"gfan-0.4plus\".",
    "created_at": "2010-02-20T10:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8307#issuecomment-73572",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Based on a freshly compiled Sage 4.3.3.alpha1, I made a source distribution called sage-4.3.3.alpha1.1, which is essentially the same as Sage 4.3.3.alpha1. From a Sage 4.3.3.alpha1 binary, I upgraded it to sage-4.3.3.alpha1.1 and received the following upgrade message:

```
The following packages will be upgraded:
  examples-4.3.3.alpha1.1 extcode-4.3.3.alpha1.1 gfan-0.4plu sage-4.3.3.alpha1.1 sage_scripts-4.3.3.alpha1.1
```

I didn't make any changes to the gfan spkg and yet it is slated for upgrading. After upgrading the Sage library, I received the following message about upgrading gfan:

```
Done
The following packages will be upgraded:
  gfan-0.4plu
```

Answering yes to the upgrade, the install log shows this line:

```
gfan-0.4plus.spkg already present
```

Yep, it's redudant and annoying that gfan is upgraded everytime one does a source upgrade.




Here's another try. With a freshly compiled Sage 4.3.3.alpha1, I applied [trac_8307-update_sage-update.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8307/trac_8307-update_sage-update.patch) to the scripts repository and produced a source distribution sage-4.3.3.alpha1.1. I then applied that same patch on top of a binary version of Sage 4.3.3.alpha1 and upgraded that binary distribution to sage-4.3.3.alpha1.1. This time the upgrade message reads:

```
The following packages will be upgraded:

    examples-4.3.3.alpha1.1 extcode-4.3.3.alpha1.1 sage-4.3.3.alpha1.1
    sage_scripts-4.3.3.alpha1.1
```

with no gfan within sight. The upgrade process didn't upgrade gfan.




The patch moves some code to the following conditional at the end of `sage-update`:

```
if __name__ == '__main__':
   <SNIP>
```

There are some clean up of docstrings and clean up conforming to PEP8. The real change is in adding the new function `chop()` and using it as follows:

```
-    installed = set(os.listdir("%s/installed/"%SPKG_ROOT))
-    to_download = [x for x in packages if not x.rstrip('.spkg') in installed]
+    installed = set(os.listdir("%s/installed/" % SPKG_ROOT))
+    to_download = [x for x in packages if not chop(x, '.spkg') in installed]

```

Previously, the script `sage-update` used `rstrip()` for finding a list of spkg's to upgrade. This function won't work as intended for spkg's that has an "s" at the end of their names just before the extension ".spkg". The new function `chop()` does this better by testing that the name of an spkg actually ends in ".spkg". That's why the update script wants to upgrade "gfan-0.4plu" when the gfan spkg is named "gfan-0.4plus".



---

archive/issue_comments_073573.json:
```json
{
    "body": "Merged [trac_8307-update_sage-update.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8307/trac_8307-update_sage-update.patch) in the script repository.",
    "created_at": "2010-03-02T21:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8307#issuecomment-73573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8307-update_sage-update.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8307/trac_8307-update_sage-update.patch) in the script repository.



---

archive/issue_events_008504.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T21:13:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8307#event-8504"
}
```



---

archive/issue_comments_073574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8307#issuecomment-73574",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
