# Issue 3052: mercurial --> plain text --> mercurial

archive/issues_003052.json:
```json
{
    "body": "Assignee: mabshoff\n\nRobert Bradshaw has mostly solved this:\n\n```\nI've looked into this some more and it looks like we can completely\nreconstruct a repository from the export of all its keywords. The\ntrick is to use the --exact keyword when importing. This forces it to\napply the given patch to the correct parent (sometimes creating a new\nhead) and will also correctly import merge patches (removing heads).\nSome scripts to do this are up at\n\nhttp://sage.math.washington.edu/home/robertwb/hg/\n\nI've successfully exported and re-created simple repositories (with\nbranching) with these scripts, and it works great and preserves all\nthe history. The only issue is that I can't seem to get it to work\nwith any repositories older than a certain date. I think the issue is\nthat mercurial changed the way nodeid's are calculated (and I keep\ngetting an error \"abort: patch is damaged or loses information\" which\nis thrown when the newly computed nodeid does not match the one in\nthe patch (command.py:1632 in 0.9.5)). Matt Mackall, any suggestions\non how to cleanly get around this/get the old node-id numbers instead?\n\n- Robert Bradshaw\n```\n\nBut there are issues.  See the complete thread here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/79da4852b8e20851/c4b8e87260f08f96?#c4b8e87260f08f96\n\n---\n\nApply [attachment:trac_3052-makefile.patch] or [attachment:trac_3052-makefile-rebased.patch] to the **Sage root** repository (in `$SAGE_ROOT/`).\n\nApply [attachment:trac_3052-textify.patch] to the **base repository** (in `$SAGE_ROOT/spkg/base/`).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3052\n\n",
    "closed_at": "2011-09-27T17:40:17Z",
    "created_at": "2008-04-29T05:18:58Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "mercurial --> plain text --> mercurial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3052",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Robert Bradshaw has mostly solved this:

```
I've looked into this some more and it looks like we can completely
reconstruct a repository from the export of all its keywords. The
trick is to use the --exact keyword when importing. This forces it to
apply the given patch to the correct parent (sometimes creating a new
head) and will also correctly import merge patches (removing heads).
Some scripts to do this are up at

http://sage.math.washington.edu/home/robertwb/hg/

I've successfully exported and re-created simple repositories (with
branching) with these scripts, and it works great and preserves all
the history. The only issue is that I can't seem to get it to work
with any repositories older than a certain date. I think the issue is
that mercurial changed the way nodeid's are calculated (and I keep
getting an error "abort: patch is damaged or loses information" which
is thrown when the newly computed nodeid does not match the one in
the patch (command.py:1632 in 0.9.5)). Matt Mackall, any suggestions
on how to cleanly get around this/get the old node-id numbers instead?

- Robert Bradshaw
```

But there are issues.  See the complete thread here:

http://groups.google.com/group/sage-devel/browse_thread/thread/79da4852b8e20851/c4b8e87260f08f96?#c4b8e87260f08f96

---

Apply [attachment:trac_3052-makefile.patch] or [attachment:trac_3052-makefile-rebased.patch] to the **Sage root** repository (in `$SAGE_ROOT/`).

Apply [attachment:trac_3052-textify.patch] to the **base repository** (in `$SAGE_ROOT/spkg/base/`).


Issue created by migration from https://trac.sagemath.org/ticket/3052





---

archive/issue_comments_021020.json:
```json
{
    "body": "Is this ticket still valid? I'm not sure I understand what exactly needs to be done with this, but it seems to apply to ancient mercurial versions and sage 2.x...",
    "created_at": "2011-04-04T17:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21020",
    "user": "https://github.com/kini"
}
```

Is this ticket still valid? I'm not sure I understand what exactly needs to be done with this, but it seems to apply to ancient mercurial versions and sage 2.x...



---

archive/issue_comments_021021.json:
```json
{
    "body": "OK, William explained it to me simply - some users (especially, say, corporate environments) might be afraid of viruses in Mercurial's binary history data. This ticket is looking for a way to make our source distribution consist **entirely** of text files only.",
    "created_at": "2011-08-06T07:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21021",
    "user": "https://github.com/kini"
}
```

OK, William explained it to me simply - some users (especially, say, corporate environments) might be afraid of viruses in Mercurial's binary history data. This ticket is looking for a way to make our source distribution consist **entirely** of text files only.



---

archive/issue_comments_021022.json:
```json
{
    "body": "I've written a python program that converts Mercurial 1.0+ bundles to a JSON representation and back. This doesn't produce a series of patch files, but it is a fully 7-bit-clean text format which is human-readable (though not as easy to grasp as a git diff or unified diff). It is also a bit-identically reversible computation and preserves all node IDs. The transformation from repository to bundle is also fully reversible as it is what Mercurial itself uses for pushes and pulls.",
    "created_at": "2011-08-10T08:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21022",
    "user": "https://github.com/kini"
}
```

I've written a python program that converts Mercurial 1.0+ bundles to a JSON representation and back. This doesn't produce a series of patch files, but it is a fully 7-bit-clean text format which is human-readable (though not as easy to grasp as a git diff or unified diff). It is also a bit-identically reversible computation and preserves all node IDs. The transformation from repository to bundle is also fully reversible as it is what Mercurial itself uses for pushes and pulls.



---

archive/issue_comments_021023.json:
```json
{
    "body": "apply to $SAGE_ROOT",
    "created_at": "2011-08-11T05:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21023",
    "user": "https://github.com/kini"
}
```

apply to $SAGE_ROOT



---

archive/issue_comments_021024.json:
```json
{
    "body": "Attachment [trac_3052-textify.patch](tarball://root/attachments/some-uuid/ticket3052/trac_3052-textify.patch) by @kini created at 2011-08-11 05:11:41\n\napply to $SAGE_ROOT/spkg/base",
    "created_at": "2011-08-11T05:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21024",
    "user": "https://github.com/kini"
}
```

Attachment [trac_3052-textify.patch](tarball://root/attachments/some-uuid/ticket3052/trac_3052-textify.patch) by @kini created at 2011-08-11 05:11:41

apply to $SAGE_ROOT/spkg/base



---

archive/issue_comments_021025.json:
```json
{
    "body": "So here are a couple of patches. Apply as indicated. The python file is not doctested, but most of the functions are pretty side-effectful so I don't see how exactly to do this. It at least does fail the doctester if it can't find the correct things to import, so that much is at least safeguarded (in case Mercurial is too old or too new, for example). Speaking of which, this patch depends on #10594 (merged in 4.7.2.alpha0).\n\nTest this patch by unpacking a source distro tarball, doing `make text-expand`, `make text-collapse`, `make`, and `make ptestlong` (in that order, of course). Works for me on sage.math.washington.edu .",
    "created_at": "2011-08-11T05:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21025",
    "user": "https://github.com/kini"
}
```

So here are a couple of patches. Apply as indicated. The python file is not doctested, but most of the functions are pretty side-effectful so I don't see how exactly to do this. It at least does fail the doctester if it can't find the correct things to import, so that much is at least safeguarded (in case Mercurial is too old or too new, for example). Speaking of which, this patch depends on #10594 (merged in 4.7.2.alpha0).

Test this patch by unpacking a source distro tarball, doing `make text-expand`, `make text-collapse`, `make`, and `make ptestlong` (in that order, of course). Works for me on sage.math.washington.edu .



---

archive/issue_comments_021026.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-11T05:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21026",
    "user": "https://github.com/kini"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_021027.json:
```json
{
    "body": "Sounds good, positive review. \n\nOf course there is still a 35MB spkg containing various OSX Fortran compilers, thats a lot of binary code ;) Hopefully apple will fix their toolchain at one point...",
    "created_at": "2011-09-18T12:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21027",
    "user": "https://github.com/vbraun"
}
```

Sounds good, positive review. 

Of course there is still a 35MB spkg containing various OSX Fortran compilers, thats a lot of binary code ;) Hopefully apple will fix their toolchain at one point...



---

archive/issue_comments_021028.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-18T12:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21028",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021029.json:
```json
{
    "body": "Thanks for the review! :)",
    "created_at": "2011-09-21T04:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21029",
    "user": "https://github.com/kini"
}
```

Thanks for the review! :)



---

archive/issue_comments_021030.json:
```json
{
    "body": "Looks like Jeroen's merger doesn't yet support the base repository... :(",
    "created_at": "2011-09-23T11:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21030",
    "user": "https://github.com/nexttime"
}
```

Looks like Jeroen's merger doesn't yet support the base repository... :(



---

archive/issue_comments_021031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-27T17:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21031",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed



---

archive/issue_events_006916.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2011-09-27T17:40:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3052#event-6916"
}
```



---

archive/issue_comments_021032.json:
```json
{
    "body": "Attachment [trac_3052-makefile-rebased.patch](tarball://root/attachments/some-uuid/ticket3052/trac_3052-makefile-rebased.patch) by @jdemeyer created at 2011-10-06 11:38:40",
    "created_at": "2011-10-06T11:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21032",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_3052-makefile-rebased.patch](tarball://root/attachments/some-uuid/ticket3052/trac_3052-makefile-rebased.patch) by @jdemeyer created at 2011-10-06 11:38:40



---

archive/issue_comments_021033.json:
```json
{
    "body": "I rebased all patches with fuzz 2, but didn't bother about this one because it was so trivial (or obvious). ;-)",
    "created_at": "2011-10-06T11:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21033",
    "user": "https://github.com/nexttime"
}
```

I rebased all patches with fuzz 2, but didn't bother about this one because it was so trivial (or obvious). ;-)



---

archive/issue_comments_021034.json:
```json
{
    "body": "BTW this code imports stuff from Mercurial internals so it may need to be updated when we next upgrade Mercurial. Any ideas on how to make a doctest that will break when Mercurial is upgraded so that this will be noticed when the time comes? I guess there's always the trivial\n\n```rst\n>>> import mercurial.__version__.version\n>>> mercurial.__version__.version\n'1.8.4'\n```\n\nBut even if we use this silly doctest, where should it go? `$SAGE_ROOT/spkg/base` is not doctested by `make ptestlong`.",
    "created_at": "2011-10-31T08:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21034",
    "user": "https://github.com/kini"
}
```

BTW this code imports stuff from Mercurial internals so it may need to be updated when we next upgrade Mercurial. Any ideas on how to make a doctest that will break when Mercurial is upgraded so that this will be noticed when the time comes? I guess there's always the trivial

```rst
>>> import mercurial.__version__.version
>>> mercurial.__version__.version
'1.8.4'
```

But even if we use this silly doctest, where should it go? `$SAGE_ROOT/spkg/base` is not doctested by `make ptestlong`.



---

archive/issue_comments_021035.json:
```json
{
    "body": "Odd tests go in `SAGE_ROOT/devel/sage/sage/tests`.",
    "created_at": "2011-10-31T16:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21035",
    "user": "https://github.com/williamstein"
}
```

Odd tests go in `SAGE_ROOT/devel/sage/sage/tests`.



---

archive/issue_comments_021036.json:
```json
{
    "body": "Perhaps we could tag such tests `# optional - release` such they get only run by developers and the release manager(s) or release scripts.  Then we could really test whether `text-expand` and `text-collapse` are still functional (and not just test for a Mercurial version, which is a bit odd).",
    "created_at": "2011-10-31T21:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3052#issuecomment-21036",
    "user": "https://github.com/nexttime"
}
```

Perhaps we could tag such tests `# optional - release` such they get only run by developers and the release manager(s) or release scripts.  Then we could really test whether `text-expand` and `text-collapse` are still functional (and not just test for a Mercurial version, which is a bit odd).
