# Issue 9186: Update R's spkg-install for building multiple spkgs in parallel

archive/issues_009186.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby @jhpalmieri @nexttime\n\nTo build R with `SAGE_PARALLEL_SPKG_BUILD=\"yes\"` on Mac OS X, we need to add, e.g.,\n\n```sh\nMAKEFLAGS=\nexport MAKEFLAGS\n```\n\nto the \"make install\" part of the package's `spkg-install`.\n\nPlease see #8306 about building spkgs in parallel.  For `MAKEFLAGS`, see [the GNU Make manual](http://www.gnu.org/software/make/manual/html_node/Options_002fRecursion.html).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9186\n\n",
    "created_at": "2010-06-08T08:42:08Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Update R's spkg-install for building multiple spkgs in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9186",
    "user": "@qed777"
}
```
Assignee: tbd

CC:  drkirkby @jhpalmieri @nexttime

To build R with `SAGE_PARALLEL_SPKG_BUILD="yes"` on Mac OS X, we need to add, e.g.,

```sh
MAKEFLAGS=
export MAKEFLAGS
```

to the "make install" part of the package's `spkg-install`.

Please see #8306 about building spkgs in parallel.  For `MAKEFLAGS`, see [the GNU Make manual](http://www.gnu.org/software/make/manual/html_node/Options_002fRecursion.html).

Issue created by migration from https://trac.sagemath.org/ticket/9186





---

archive/issue_comments_085927.json:
```json
{
    "body": "spkg patch.  Set empty `MAKEFLAGS` for installation.",
    "created_at": "2010-06-09T02:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9186#issuecomment-85927",
    "user": "@qed777"
}
```

spkg patch.  Set empty `MAKEFLAGS` for installation.



---

archive/issue_comments_085928.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-09T02:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9186#issuecomment-85928",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085929.json:
```json
{
    "body": "Attachment [trac_9186-r_makeflags.patch](tarball://root/attachments/some-uuid/ticket9186/trac_9186-r_makeflags.patch) by @qed777 created at 2010-06-09 02:25:21\n\nI've put a new spkg at\n\n* http://sage.math.washington.edu/home/mpatel/trac/9186/r-2.10.1.p2.spkg",
    "created_at": "2010-06-09T02:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9186#issuecomment-85929",
    "user": "@qed777"
}
```

Attachment [trac_9186-r_makeflags.patch](tarball://root/attachments/some-uuid/ticket9186/trac_9186-r_makeflags.patch) by @qed777 created at 2010-06-09 02:25:21

I've put a new spkg at

* http://sage.math.washington.edu/home/mpatel/trac/9186/r-2.10.1.p2.spkg



---

archive/issue_comments_085930.json:
```json
{
    "body": "Positive review. It is extreamly simple, looks good and I've tested it on Solaris 10 on an old Sun Blade 2000 SPARC. \n\n\n```\nreal    21m53.863s\nuser    17m29.388s\nsys     3m22.428s\nSuccessfully installed r-2.10.1.p2\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.4/spkg/build/r-2.10.1.p2\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing r-2.10.1.p2.spkg\n```\n\n\n**I really hope your code for building packages in parallel gets into Sage asap. It could make a huge difference to build times. I'll see if I can get some interest in pushing this up the priority list!**",
    "created_at": "2010-06-24T17:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9186#issuecomment-85930",
    "user": "drkirkby"
}
```

Positive review. It is extreamly simple, looks good and I've tested it on Solaris 10 on an old Sun Blade 2000 SPARC. 


```
real    21m53.863s
user    17m29.388s
sys     3m22.428s
Successfully installed r-2.10.1.p2
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4/spkg/build/r-2.10.1.p2
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing r-2.10.1.p2.spkg
```


**I really hope your code for building packages in parallel gets into Sage asap. It could make a huge difference to build times. I'll see if I can get some interest in pushing this up the priority list!**



---

archive/issue_comments_085931.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T17:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9186#issuecomment-85931",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085932.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9186#issuecomment-85932",
    "user": "@rlmill"
}
```

Resolution: fixed
