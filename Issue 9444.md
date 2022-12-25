# Issue 9444: Fix "rm: Cannot remove any directory in the path of the current working directory" on t2

archive/issues_009444.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirkby\n\nIn `/rootpool2/local/kirkby/sage-4.5.alpha1` on t2:\n\n```sh\n$ tail spkg/logs/rubiks-20070912.p11.log\nreal    2m30.575s\nuser    2m20.699s\nsys     0m5.083s\nSuccessfully installed rubiks-20070912.p11\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/rootpool2/local/kirkby/sage-4.5.alpha1/spkg/build/rubiks-20070912.p11\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing rubiks-20070912.p11.spkg\n```\n\nThis leaves an empty directory `SAGE_ROOT/spkg/build/rubiks-20070912.p11`.\n\nIt seems the problem is\n\n```sh\nrm -rf \"$SAGE_PACKAGES/build/$PKG_NAME\"\n```\n\nnear the end of `SAGE_LOCAL/bin/sage-spkg`.  What if we precede this with `cd ..`, say?\n\nIssue created by migration from https://trac.sagemath.org/ticket/9444\n\n",
    "created_at": "2010-07-07T05:29:55Z",
    "labels": [
        "component: porting: solaris",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Fix \"rm: Cannot remove any directory in the path of the current working directory\" on t2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9444",
    "user": "https://github.com/qed777"
}
```
Assignee: drkirkby

CC:  drkirkby

In `/rootpool2/local/kirkby/sage-4.5.alpha1` on t2:

```sh
$ tail spkg/logs/rubiks-20070912.p11.log
real    2m30.575s
user    2m20.699s
sys     0m5.083s
Successfully installed rubiks-20070912.p11
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/rootpool2/local/kirkby/sage-4.5.alpha1/spkg/build/rubiks-20070912.p11
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing rubiks-20070912.p11.spkg
```

This leaves an empty directory `SAGE_ROOT/spkg/build/rubiks-20070912.p11`.

It seems the problem is

```sh
rm -rf "$SAGE_PACKAGES/build/$PKG_NAME"
```

near the end of `SAGE_LOCAL/bin/sage-spkg`.  What if we precede this with `cd ..`, say?

Issue created by migration from https://trac.sagemath.org/ticket/9444





---

archive/issue_comments_090345.json:
```json
{
    "body": "Attachment [trac_9444-spkg_build_dir_t2.patch](tarball://root/attachments/some-uuid/ticket9444/trac_9444-spkg_build_dir_t2.patch) by @qed777 created at 2010-07-07 05:37:54\n\nStep out of spkg/build/foo-x.y.z before deleting it.",
    "created_at": "2010-07-07T05:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90345",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9444-spkg_build_dir_t2.patch](tarball://root/attachments/some-uuid/ticket9444/trac_9444-spkg_build_dir_t2.patch) by @qed777 created at 2010-07-07 05:37:54

Step out of spkg/build/foo-x.y.z before deleting it.



---

archive/issue_comments_090346.json:
```json
{
    "body": "I've attached a trial patch that uses `cd \"$SAGE_PACKAGES/build/\"`.",
    "created_at": "2010-07-07T05:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90346",
    "user": "https://github.com/qed777"
}
```

I've attached a trial patch that uses `cd "$SAGE_PACKAGES/build/"`.



---

archive/issue_comments_090347.json:
```json
{
    "body": "This looks good and I'm confident it would fix this rather annoying bug. \n\nMy only concern is whether fixing this bug will cause a problem for any code that might have relied on the old behavior. That will need testing. \n\nDave",
    "created_at": "2010-07-07T07:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90347",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This looks good and I'm confident it would fix this rather annoying bug. 

My only concern is whether fixing this bug will cause a problem for any code that might have relied on the old behavior. That will need testing. 

Dave



---

archive/issue_comments_090348.json:
```json
{
    "body": "I think that this message only appears on Solaris; at least, that's been my experience.  On sage.math, for example, I can do this:\n\n```\n$ cd /scratch/palmieri\n$ mkdir TEMP\n$ cd TEMP\n$ rm -rf /scratch/palmieri/TEMP\n```\n\nbut doing this on t2.math results in an error:\n\n```\nrm: Cannot remove any directory in the path of the current working directory\n```\n\nSo if it ever relied on this behavior, it didn't rely on it on sage.math.  (All of the linux machines I've used, and also Mac OS X, behave like sage.math in this regard.)\n\nI'm trying a build on sage.math with this patch, and I'll try it on t2 later.",
    "created_at": "2010-07-27T22:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90348",
    "user": "https://github.com/jhpalmieri"
}
```

I think that this message only appears on Solaris; at least, that's been my experience.  On sage.math, for example, I can do this:

```
$ cd /scratch/palmieri
$ mkdir TEMP
$ cd TEMP
$ rm -rf /scratch/palmieri/TEMP
```

but doing this on t2.math results in an error:

```
rm: Cannot remove any directory in the path of the current working directory
```

So if it ever relied on this behavior, it didn't rely on it on sage.math.  (All of the linux machines I've used, and also Mac OS X, behave like sage.math in this regard.)

I'm trying a build on sage.math with this patch, and I'll try it on t2 later.



---

archive/issue_comments_090349.json:
```json
{
    "body": "mpatel: I assume this is ready for review?",
    "created_at": "2010-07-27T22:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90349",
    "user": "https://github.com/jhpalmieri"
}
```

mpatel: I assume this is ready for review?



---

archive/issue_comments_090350.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-27T22:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90350",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090351.json:
```json
{
    "body": "I'm ok with the patch, though we could replicate\n\n```sh\n   # Make triply sure that we are in the build directory before doing \n    # a scary \"rm -rf\".\n    cd \"$SAGE_PACKAGES/build\"\n    if [ $? -ne 0 ]; then\n        echo \"Unable to find build directory.\"\n    else\n        rm -rf \"$PKG_BASE-\"*\n    fi\n```\n\nwhich is what is done some lines above.\n\nThere are many other things to fix or improve in `sage-spkg`, but I'll leave those for further tickets (something like work in progress) since hopefully this one gets merged soon.\n\nIf anyone feels Mitesh's solution is not sufficient, feel free to revert it to \"needs review\" or \"needs work\".\n\n-Leif",
    "created_at": "2010-07-27T23:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90351",
    "user": "https://github.com/nexttime"
}
```

I'm ok with the patch, though we could replicate

```sh
   # Make triply sure that we are in the build directory before doing 
    # a scary "rm -rf".
    cd "$SAGE_PACKAGES/build"
    if [ $? -ne 0 ]; then
        echo "Unable to find build directory."
    else
        rm -rf "$PKG_BASE-"*
    fi
```

which is what is done some lines above.

There are many other things to fix or improve in `sage-spkg`, but I'll leave those for further tickets (something like work in progress) since hopefully this one gets merged soon.

If anyone feels Mitesh's solution is not sufficient, feel free to revert it to "needs review" or "needs work".

-Leif



---

archive/issue_comments_090352.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-27T23:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90352",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090353.json:
```json
{
    "body": "I'm happy too. My initial concern was that the directory was not getting deleted on any operating system, in which case deleting it could be dangerous. But now I realise it gets deleted on Linux, then clearly there is no risk. \n\nI'm 100% happy with this. \n\nDave",
    "created_at": "2010-07-27T23:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90353",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm happy too. My initial concern was that the directory was not getting deleted on any operating system, in which case deleting it could be dangerous. But now I realise it gets deleted on Linux, then clearly there is no risk. 

I'm 100% happy with this. 

Dave



---

archive/issue_comments_090354.json:
```json
{
    "body": "Just for the record: Besides other things, I'd like to have something like `$SAGE_SPKG_KEEP_SRC` (or `SAGE_KEEP_BUILT_SPKGS`) for developers, because `-s` is not available for whole builds (with `make`).",
    "created_at": "2010-07-27T23:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90354",
    "user": "https://github.com/nexttime"
}
```

Just for the record: Besides other things, I'd like to have something like `$SAGE_SPKG_KEEP_SRC` (or `SAGE_KEEP_BUILT_SPKGS`) for developers, because `-s` is not available for whole builds (with `make`).



---

archive/issue_comments_090355.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> mpatel: I assume this is ready for review?\n\nYes.  I didn't change the status field because I had tested the patch only with `sage -f` on sage.math and t2.\n\nWere there any problems with your builds?",
    "created_at": "2010-07-28T05:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90355",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 jhpalmieri]:
> mpatel: I assume this is ready for review?

Yes.  I didn't change the status field because I had tested the patch only with `sage -f` on sage.math and t2.

Were there any problems with your builds?



---

archive/issue_comments_090356.json:
```json
{
    "body": "No, everything has worked fine.",
    "created_at": "2010-07-28T05:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90356",
    "user": "https://github.com/jhpalmieri"
}
```

No, everything has worked fine.



---

archive/issue_comments_090357.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> Just for the record: Besides other things, I'd like to have something like `$SAGE_SPKG_KEEP_SRC` (or `SAGE_KEEP_BUILT_SPKGS`) for developers, because `-s` is not available for whole builds (with `make`).\n\nSee #4949.",
    "created_at": "2010-08-06T21:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90357",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:7 leif]:
> Just for the record: Besides other things, I'd like to have something like `$SAGE_SPKG_KEEP_SRC` (or `SAGE_KEEP_BUILT_SPKGS`) for developers, because `-s` is not available for whole builds (with `make`).

See #4949.



---

archive/issue_comments_090358.json:
```json
{
    "body": "Why is the milestone for this set to 5.0? Do we really need to wait that long to fix this bug, given it already has positive review and is one of the simplest possible bug fixes. \n\nDave",
    "created_at": "2010-08-08T09:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90358",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Why is the milestone for this set to 5.0? Do we really need to wait that long to fix this bug, given it already has positive review and is one of the simplest possible bug fixes. 

Dave



---

archive/issue_events_009601.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:39:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9444#event-9601"
}
```



---

archive/issue_comments_090359.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9444#issuecomment-90359",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
