# Issue 555: c_lib SConscript doesn't always copy new libcsage.dylib on a sage -b

archive/issues_000555.json:
```json
{
    "body": "Assignee: @craigcitro\n\nIf you have two branches, and you edit libcsage.dylib in one, then sage -b to the other, it doesn't (always? ever?) copy over the appropriate libcsage.dylib to /sage/local/lib.\n\nIssue created by migration from https://trac.sagemath.org/ticket/555\n\n",
    "created_at": "2007-09-01T18:18:47Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "c_lib SConscript doesn't always copy new libcsage.dylib on a sage -b",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/555",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

If you have two branches, and you edit libcsage.dylib in one, then sage -b to the other, it doesn't (always? ever?) copy over the appropriate libcsage.dylib to /sage/local/lib.

Issue created by migration from https://trac.sagemath.org/ticket/555





---

archive/issue_comments_002857.json:
```json
{
    "body": "I'm pretty sure this is fixed. Basically, the problem is that scons doesn't want to look at a remote file (in our case $SAGE_ROOT/local/lib/libcsage.dylib) and see if it's up to date. The fix: just force it to copy the file over every time. Not the most elegant, but it works.\n\nhg bundle is attached.",
    "created_at": "2007-09-02T17:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2857",
    "user": "https://github.com/craigcitro"
}
```

I'm pretty sure this is fixed. Basically, the problem is that scons doesn't want to look at a remote file (in our case $SAGE_ROOT/local/lib/libcsage.dylib) and see if it's up to date. The fix: just force it to copy the file over every time. Not the most elegant, but it works.

hg bundle is attached.



---

archive/issue_comments_002858.json:
```json
{
    "body": "I can't apply this patch no matter what I try...",
    "created_at": "2007-09-03T03:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2858",
    "user": "https://github.com/williamstein"
}
```

I can't apply this patch no matter what I try...



---

archive/issue_comments_002859.json:
```json
{
    "body": "Attachment [trac_555.hg](tarball://root/attachments/some-uuid/ticket555/trac_555.hg) by @craigcitro created at 2007-09-03 03:11:18",
    "created_at": "2007-09-03T03:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2859",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_555.hg](tarball://root/attachments/some-uuid/ticket555/trac_555.hg) by @craigcitro created at 2007-09-03 03:11:18



---

archive/issue_comments_002860.json:
```json
{
    "body": "Attachment [ticket_555.patch](tarball://root/attachments/some-uuid/ticket555/ticket_555.patch) by @craigcitro created at 2007-09-03 03:17:24\n\npatch for same hg bundle below",
    "created_at": "2007-09-03T03:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2860",
    "user": "https://github.com/craigcitro"
}
```

Attachment [ticket_555.patch](tarball://root/attachments/some-uuid/ticket555/ticket_555.patch) by @craigcitro created at 2007-09-03 03:17:24

patch for same hg bundle below



---

archive/issue_comments_002861.json:
```json
{
    "body": "Attachment [total_trac_555_localbin.hg](tarball://root/attachments/some-uuid/ticket555/total_trac_555_localbin.hg) by @craigcitro created at 2007-09-03 06:43:34",
    "created_at": "2007-09-03T06:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2861",
    "user": "https://github.com/craigcitro"
}
```

Attachment [total_trac_555_localbin.hg](tarball://root/attachments/some-uuid/ticket555/total_trac_555_localbin.hg) by @craigcitro created at 2007-09-03 06:43:34



---

archive/issue_comments_002862.json:
```json
{
    "body": "Attachment [total_trac_555.hg](tarball://root/attachments/some-uuid/ticket555/total_trac_555.hg) by @craigcitro created at 2007-09-03 07:02:01\n\nAttached two new bundles, total_trac_555.hg and total_trac_555_localbin.hg. The first is against the main sage repo, and the second is for $SAGE_ROOT/local/bin, as you might guess from the name. These take you from a clean 2.8.3 install to a version with a fully working c_lib recompilation on branch switch setup, with very few spurious copies. \n\nLet me know if people run into trouble; if you want to test it, do the following: make a new branch (called, say, foo) and apply the hg bundle, and then clone that (maybe call that bar). Then switch back and forth between foo and bar, and make sure that you see libcsage.dylib getting copied (along with a bunch of include files) every time you switch branches.",
    "created_at": "2007-09-03T07:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2862",
    "user": "https://github.com/craigcitro"
}
```

Attachment [total_trac_555.hg](tarball://root/attachments/some-uuid/ticket555/total_trac_555.hg) by @craigcitro created at 2007-09-03 07:02:01

Attached two new bundles, total_trac_555.hg and total_trac_555_localbin.hg. The first is against the main sage repo, and the second is for $SAGE_ROOT/local/bin, as you might guess from the name. These take you from a clean 2.8.3 install to a version with a fully working c_lib recompilation on branch switch setup, with very few spurious copies. 

Let me know if people run into trouble; if you want to test it, do the following: make a new branch (called, say, foo) and apply the hg bundle, and then clone that (maybe call that bar). Then switch back and forth between foo and bar, and make sure that you see libcsage.dylib getting copied (along with a bunch of include files) every time you switch branches.



---

archive/issue_comments_002863.json:
```json
{
    "body": "I've pushed this all into the official repo.",
    "created_at": "2007-09-03T21:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2863",
    "user": "https://github.com/williamstein"
}
```

I've pushed this all into the official repo.



---

archive/issue_comments_002864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-03T21:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/555#issuecomment-2864",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000598.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-03T21:15:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/555",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/555#event-598"
}
```
