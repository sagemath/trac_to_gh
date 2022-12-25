# Issue 3882: explain in the programming guide why spkg source patches should be applied by copying entire files

archive/issues_003882.json:
```json
{
    "body": "Assignee: tba\n\nIn the sage programming guide (and maybe on the wiki too), it should be explained how to distribute a patch to the source of an spkg.  The way I think about it (thanks to wstein and mabshoff!) is that the end result of the patches should be cached in whole files, which are then copied over the sources at install time.  Thus, at spkg-install time, there should be no reliance on patch and friends; only files copied over onto the sources.\n\nSo one way to do it would be to maintain a set of patches to the sources.  When the spkg is created, apply all the patches and copy the affected files to a patches-cached (or patches-applied or something) directory.  When the spkg is installed, just copy the affected files over the source files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3882\n\n",
    "closed_at": "2010-02-14T14:39:26Z",
    "created_at": "2008-08-17T03:13:45Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "explain in the programming guide why spkg source patches should be applied by copying entire files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3882",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tba

In the sage programming guide (and maybe on the wiki too), it should be explained how to distribute a patch to the source of an spkg.  The way I think about it (thanks to wstein and mabshoff!) is that the end result of the patches should be cached in whole files, which are then copied over the sources at install time.  Thus, at spkg-install time, there should be no reliance on patch and friends; only files copied over onto the sources.

So one way to do it would be to maintain a set of patches to the sources.  When the spkg is created, apply all the patches and copy the affected files to a patches-cached (or patches-applied or something) directory.  When the spkg is installed, just copy the affected files over the source files.

Issue created by migration from https://trac.sagemath.org/ticket/3882





---

archive/issue_comments_027633.json:
```json
{
    "body": "I'm working on editing the programming guide, but I don't understand what you mean. Can you explain it again, or give an example?\n\n(Probably part of the issue is that I haven't really worked with spkg's, just the core sage library.)",
    "created_at": "2008-08-19T01:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27633",
    "user": "https://github.com/jhpalmieri"
}
```

I'm working on editing the programming guide, but I don't understand what you mean. Can you explain it again, or give an example?

(Probably part of the issue is that I haven't really worked with spkg's, just the core sage library.)



---

archive/issue_comments_027634.json:
```json
{
    "body": "I'm not understanding why one would want to do it this way, rather than just patch the source. It makes it much clearer what's going on. Also, we can assume something like patch is available as we are using it for mercurial (or do we need it later on?)\n\nIf not, I think it would be very good to make it clear with an (automated) patches-applied directory, so someone could update an spkg without having to manually figure out all the diffs and re-apply them.",
    "created_at": "2008-08-19T03:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27634",
    "user": "https://github.com/robertwb"
}
```

I'm not understanding why one would want to do it this way, rather than just patch the source. It makes it much clearer what's going on. Also, we can assume something like patch is available as we are using it for mercurial (or do we need it later on?)

If not, I think it would be very good to make it clear with an (automated) patches-applied directory, so someone could update an spkg without having to manually figure out all the diffs and re-apply them.



---

archive/issue_comments_027635.json:
```json
{
    "body": "A couple reasons *not* to use patch:\n\n* GNU patch that can apply unified diffs does not exist on some platforms per default, i.e. Solaris\n* the number of changes to the sources in the src directory are usually small and should be pushed upstream anyway\n* copying patches is dead simple and very KISS\n* hg's patch requires the sources to be under revision control, doubling the size of a Sage tarball\n* hg is only available late in the build process, so it is a chicken and egg problem\n* some changes are conditional on the platform we are building on\n\nWilliam and I discussed this with Jason in IRC for an hour. As an opinion from the trenches: patch has no advantage over copying. Most spkgs have the new files and their diff in the patches directory. Upgrading spkgs will not be any easier by applying some patches to the source since it requires some understanding what is being changed. And those reasons should be documented in SPKG.txt.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T03:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27635",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A couple reasons *not* to use patch:

* GNU patch that can apply unified diffs does not exist on some platforms per default, i.e. Solaris
* the number of changes to the sources in the src directory are usually small and should be pushed upstream anyway
* copying patches is dead simple and very KISS
* hg's patch requires the sources to be under revision control, doubling the size of a Sage tarball
* hg is only available late in the build process, so it is a chicken and egg problem
* some changes are conditional on the platform we are building on

William and I discussed this with Jason in IRC for an hour. As an opinion from the trenches: patch has no advantage over copying. Most spkgs have the new files and their diff in the patches directory. Upgrading spkgs will not be any easier by applying some patches to the source since it requires some understanding what is being changed. And those reasons should be documented in SPKG.txt.

Cheers,

Michael



---

archive/issue_comments_027636.json:
```json
{
    "body": "Yes, those seem like good enough reasons.",
    "created_at": "2008-08-19T04:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27636",
    "user": "https://github.com/robertwb"
}
```

Yes, those seem like good enough reasons.



---

archive/issue_comments_027637.json:
```json
{
    "body": "I just posted lots of revisions to the programming guide in #3905, but I have not dealt with the issue raised here.  I would suggest, if anyone feels inspired to work on this one, wait until #3905 makes it through the review process so we don't get conflicts -- both in the technical sense of being unable to apply one patch or the other, and also stylistically and content-wise: if the changes in #3905 go through, any changes for this ticket should be based on the new version.",
    "created_at": "2008-08-20T00:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27637",
    "user": "https://github.com/jhpalmieri"
}
```

I just posted lots of revisions to the programming guide in #3905, but I have not dealt with the issue raised here.  I would suggest, if anyone feels inspired to work on this one, wait until #3905 makes it through the review process so we don't get conflicts -- both in the technical sense of being unable to apply one patch or the other, and also stylistically and content-wise: if the changes in #3905 go through, any changes for this ticket should be based on the new version.



---

archive/issue_comments_027638.json:
```json
{
    "body": "A patch to revise the Developer's Guide is up at #8079.",
    "created_at": "2010-02-09T12:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

A patch to revise the Developer's Guide is up at #8079.



---

archive/issue_comments_027639.json:
```json
{
    "body": "Close as fixed by #8079.",
    "created_at": "2010-02-14T14:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27639",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #8079.



---

archive/issue_events_008901.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-14T14:39:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3882#event-8901"
}
```



---

archive/issue_comments_027640.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-14T14:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3882#issuecomment-27640",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
