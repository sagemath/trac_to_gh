# Issue 3297: Make ccdlib produce a shared library

archive/issues_003297.json:
```json
{
    "body": "Assignee: mabshoff\n\nTim Abbott made a patch to get cddlib to use libtools and easily\nproduce a shared library. Packaging the change for sage means not \nonly patching several Makefile.am file but also adding a file \nltmain.sh and regenerating configure.in, configure, aclocal.m4\nand several Makefile.in.\nI attach a tarball containing an updated patch folder and also \na patch to spkg-install to use it. The new spkg-install only build\nshared libraries. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3297\n\n",
    "created_at": "2008-05-25T09:19:49Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make ccdlib produce a shared library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3297",
    "user": "https://github.com/kiwifb"
}
```
Assignee: mabshoff

Tim Abbott made a patch to get cddlib to use libtools and easily
produce a shared library. Packaging the change for sage means not 
only patching several Makefile.am file but also adding a file 
ltmain.sh and regenerating configure.in, configure, aclocal.m4
and several Makefile.in.
I attach a tarball containing an updated patch folder and also 
a patch to spkg-install to use it. The new spkg-install only build
shared libraries. 

Issue created by migration from https://trac.sagemath.org/ticket/3297





---

archive/issue_comments_022756.json:
```json
{
    "body": "new patch folder",
    "created_at": "2008-05-25T09:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22756",
    "user": "https://github.com/kiwifb"
}
```

new patch folder



---

archive/issue_comments_022757.json:
```json
{
    "body": "Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3297/spkg-install.patch) by @kiwifb created at 2008-05-25 09:21:53\n\npatch to spkg-install",
    "created_at": "2008-05-25T09:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22757",
    "user": "https://github.com/kiwifb"
}
```

Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3297/spkg-install.patch) by @kiwifb created at 2008-05-25 09:21:53

patch to spkg-install



---

archive/issue_comments_022758.json:
```json
{
    "body": "We should update to the latest cddlib release while we are at it. I see no point in sticking all those files in patches into the mercurial repo since that means checking in 1.3MB of files that will be removed in the next upstream release anyway.\n\nPlease do not attach tar.gz archives to trac ticket since a bug prevents the download the easy way, i.e. just follow the link and you will see.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-25T13:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We should update to the latest cddlib release while we are at it. I see no point in sticking all those files in patches into the mercurial repo since that means checking in 1.3MB of files that will be removed in the next upstream release anyway.

Please do not attach tar.gz archives to trac ticket since a bug prevents the download the easy way, i.e. just follow the link and you will see.

Cheers,

Michael



---

archive/issue_comments_022759.json:
```json
{
    "body": "I just checked and there are other conflicting changes to cddlib-0.94f. So I would greatly prefer for this to go upstream before we merge it back into Sage. The author of cddlib seems to be quite responsive, so let's try that route first.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-25T13:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I just checked and there are other conflicting changes to cddlib-0.94f. So I would greatly prefer for this to go upstream before we merge it back into Sage. The author of cddlib seems to be quite responsive, so let's try that route first.

Cheers,

Michael



---

archive/issue_comments_022760.json:
```json
{
    "body": "OK I have a small patch against 0.94f somewhere, not a big change\ncompared to 0.94b but of course everything has to be regenerated\nwhich is upstream job anyway. I'll see what I can do.\n\nCheers,\nFrancois",
    "created_at": "2008-05-25T20:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22760",
    "user": "https://github.com/kiwifb"
}
```

OK I have a small patch against 0.94f somewhere, not a big change
compared to 0.94b but of course everything has to be regenerated
which is upstream job anyway. I'll see what I can do.

Cheers,
Francois



---

archive/issue_comments_022761.json:
```json
{
    "body": "Sent an email upstream with a libtool patch against 0.94f.\n\nFrancois",
    "created_at": "2008-05-25T22:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22761",
    "user": "https://github.com/kiwifb"
}
```

Sent an email upstream with a libtool patch against 0.94f.

Francois



---

archive/issue_comments_022762.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T22:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22762",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_022763.json:
```json
{
    "body": "Tim,\n\nthe latest upstream release is cddlib-094f - did those patches get merged?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T17:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Tim,

the latest upstream release is cddlib-094f - did those patches get merged?

Cheers,

Michael



---

archive/issue_comments_022764.json:
```json
{
    "body": "Hi Micheal,\n\nthe latest upstream release was already 094f when I filled the bug.\nI sent a patch against 094f upstream but never got an answer.\n\nFrancois",
    "created_at": "2008-08-26T23:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22764",
    "user": "https://github.com/kiwifb"
}
```

Hi Micheal,

the latest upstream release was already 094f when I filled the bug.
I sent a patch against 094f upstream but never got an answer.

Francois



---

archive/issue_comments_022765.json:
```json
{
    "body": "What's up with this?  It has been in limbo for 3 months!  Somebody do something.",
    "created_at": "2008-11-28T22:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22765",
    "user": "https://github.com/williamstein"
}
```

What's up with this?  It has been in limbo for 3 months!  Somebody do something.



---

archive/issue_comments_022766.json:
```json
{
    "body": "Replying to [comment:10 was]:\n> What's up with this?  It has been in limbo for 3 months!  Somebody do something. \n\nUpstream is unresponsive. I don't see the point to copy over a massive amount of changes making the spkg at least twice as large. This is also purely a Debian thing, but we could just ship in place modified sources with instructions on how to get from upstream to this. Once upstream updates (if ever) we could sync.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T22:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22766",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:10 was]:
> What's up with this?  It has been in limbo for 3 months!  Somebody do something. 

Upstream is unresponsive. I don't see the point to copy over a massive amount of changes making the spkg at least twice as large. This is also purely a Debian thing, but we could just ship in place modified sources with instructions on how to get from upstream to this. Once upstream updates (if ever) we could sync.

Cheers,

Michael



---

archive/issue_comments_022767.json:
```json
{
    "body": "> Upstream is unresponsive. I don't see the point to copy over a massive amount of \n> changes making the spkg at least twice as large. This is also purely a Debian \n> thing, but we could just ship in place modified sources with instructions on how \n> to get from upstream to this. Once upstream updates (if ever) we could sync. \n\nI don't get the sense of any precise plan here, and I'm tempted to close this as invalid?  Thoughts?",
    "created_at": "2008-12-06T21:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22767",
    "user": "https://github.com/williamstein"
}
```

> Upstream is unresponsive. I don't see the point to copy over a massive amount of 
> changes making the spkg at least twice as large. This is also purely a Debian 
> thing, but we could just ship in place modified sources with instructions on how 
> to get from upstream to this. Once upstream updates (if ever) we could sync. 

I don't get the sense of any precise plan here, and I'm tempted to close this as invalid?  Thoughts?



---

archive/issue_comments_022768.json:
```json
{
    "body": "Here  a [new cddlib spkg](http://perso.crans.org/barthelemy/cddlib-094f.spkg), based on the current 094b.p3\n\nI...\n* packaged upstream version 0.94f\n* removed some temporary files\n* adapted the allfaces.c patch\n* updated the SPKG changelog\n* did not update de dist/debian directory\n* did not integrate #3297 nor #3304\n* did not commit anything into the .hg repository",
    "created_at": "2009-01-27T14:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22768",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

Here  a [new cddlib spkg](http://perso.crans.org/barthelemy/cddlib-094f.spkg), based on the current 094b.p3

I...
* packaged upstream version 0.94f
* removed some temporary files
* adapted the allfaces.c patch
* updated the SPKG changelog
* did not update de dist/debian directory
* did not integrate #3297 nor #3304
* did not commit anything into the .hg repository



---

archive/issue_comments_022769.json:
```json
{
    "body": "Replying to [comment:13 sbarthelemy]:\n> Here  a [new cddlib spkg](http://perso.crans.org/barthelemy/cddlib-094f.spkg), based on the current 094b.p3\n\nI just discovered #1619 which is the proper place for my comment. I copied it there. Sorry for the noise.",
    "created_at": "2009-01-27T16:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22769",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

Replying to [comment:13 sbarthelemy]:
> Here  a [new cddlib spkg](http://perso.crans.org/barthelemy/cddlib-094f.spkg), based on the current 094b.p3

I just discovered #1619 which is the proper place for my comment. I copied it there. Sorry for the noise.



---

archive/issue_comments_022770.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-29T19:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22770",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_022771.json:
```json
{
    "body": "I think #1619 removes some of the issues here, and so these patches would need to be rebased at least.  Someone might want to revive working on converting this to a shared library, so I don't think it should be closed, but I am changing it to needs work.",
    "created_at": "2009-10-29T19:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22771",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I think #1619 removes some of the issues here, and so these patches would need to be rebased at least.  Someone might want to revive working on converting this to a shared library, so I don't think it should be closed, but I am changing it to needs work.



---

archive/issue_comments_022772.json:
```json
{
    "body": "Replying to [comment:15 mhampton]:\n> I think #1619 removes some of the issues here, and so these patches would need to be rebased at least.  Someone might want to revive working on converting this to a shared library, so I don't think it should be closed, but I am changing it to needs work.\n\nOK I had done some of the work against 0.94f already but I guess skpg-install at least\nwill need to be rebased. I will look at it later today.",
    "created_at": "2009-10-29T20:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22772",
    "user": "https://github.com/kiwifb"
}
```

Replying to [comment:15 mhampton]:
> I think #1619 removes some of the issues here, and so these patches would need to be rebased at least.  Someone might want to revive working on converting this to a shared library, so I don't think it should be closed, but I am changing it to needs work.

OK I had done some of the work against 0.94f already but I guess skpg-install at least
will need to be rebased. I will look at it later today.



---

archive/issue_comments_022773.json:
```json
{
    "body": "Took me longer than expected to get around this.\nIt is a big patch when you include all the necessary regenerated files.\nIs it OK to attach it compressed (241K compressed, 1.1M uncompressed).\nAlso do we disable the static library or do we build both?",
    "created_at": "2009-11-08T01:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22773",
    "user": "https://github.com/kiwifb"
}
```

Took me longer than expected to get around this.
It is a big patch when you include all the necessary regenerated files.
Is it OK to attach it compressed (241K compressed, 1.1M uncompressed).
Also do we disable the static library or do we build both?



---

archive/issue_comments_022774.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-02-21T10:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22774",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_022775.json:
```json
{
    "body": "Fran\u00e7ois Bissey wrote on sage-devel:\n\nJust looked at SPKG.txt. #3297 has been supplanted in many ways so it should\nbe closed.",
    "created_at": "2011-02-21T10:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22775",
    "user": "https://github.com/jdemeyer"
}
```

François Bissey wrote on sage-devel:

Just looked at SPKG.txt. #3297 has been supplanted in many ways so it should
be closed.



---

archive/issue_events_003516.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-02-24T10:02:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3297#event-3516"
}
```



---

archive/issue_comments_022776.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-02-24T10:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3297#issuecomment-22776",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
