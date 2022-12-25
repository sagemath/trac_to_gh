# Issue 7552: Update the Twisted package to 9.0

archive/issues_007552.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen @jaapspies\n\n[Twisted http://twistedmatrix.com] has just recently released a new version, 9.0. This update includes several major changes, the most significant to Sage development being support for WSGI in the Twisted.web framework (rather than the Twisted.web2 framework).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7552\n\n",
    "created_at": "2009-11-29T08:12:32Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Update the Twisted package to 9.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7552",
    "user": "https://github.com/TimDumol"
}
```
Assignee: tbd

CC:  @mwhansen @jaapspies

[Twisted http://twistedmatrix.com] has just recently released a new version, 9.0. This update includes several major changes, the most significant to Sage development being support for WSGI in the Twisted.web framework (rather than the Twisted.web2 framework).

Issue created by migration from https://trac.sagemath.org/ticket/7552





---

archive/issue_comments_064058.json:
```json
{
    "body": "Markup change.",
    "created_at": "2009-11-29T08:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64058",
    "user": "https://github.com/TimDumol"
}
```

Markup change.



---

archive/issue_comments_064059.json:
```json
{
    "body": "New package up at http://sage.math.washington.edu/home/timdumol/twisted-9.0.p0.spkg. I've tried it on a few worksheets, and things seem to be working well. The notebook tests pass as well.",
    "created_at": "2009-11-29T08:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64059",
    "user": "https://github.com/TimDumol"
}
```

New package up at http://sage.math.washington.edu/home/timdumol/twisted-9.0.p0.spkg. I've tried it on a few worksheets, and things seem to be working well. The notebook tests pass as well.



---

archive/issue_comments_064060.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-29T08:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64060",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064061.json:
```json
{
    "body": "Added package link to description.",
    "created_at": "2009-11-29T08:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64061",
    "user": "https://github.com/TimDumol"
}
```

Added package link to description.



---

archive/issue_comments_064062.json:
```json
{
    "body": "Added release notes.",
    "created_at": "2009-11-29T08:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64062",
    "user": "https://github.com/TimDumol"
}
```

Added release notes.



---

archive/issue_comments_064063.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-21T22:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64063",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064064.json:
```json
{
    "body": "1. Typing \"hg status\" gives:\n\n```\nwstein@sage:~/build/referee/sage-4.3.rc0/twisted-9.0.p0$ hg status\n! patches/keys.py\n! patches/sob.py\n```\n\nThis is because you just deleted those files instead of doing \"hg rm\".  To fix, put them back, then do \"hg rm\". \n\n2. You forgot to remove patches/filepath.py, but aren't using it anymore:\n\n```\n-cp patches/filepath.py src/twisted/python/\n```\n",
    "created_at": "2009-12-21T22:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64064",
    "user": "https://github.com/williamstein"
}
```

1. Typing "hg status" gives:

```
wstein@sage:~/build/referee/sage-4.3.rc0/twisted-9.0.p0$ hg status
! patches/keys.py
! patches/sob.py
```

This is because you just deleted those files instead of doing "hg rm".  To fix, put them back, then do "hg rm". 

2. You forgot to remove patches/filepath.py, but aren't using it anymore:

```
-cp patches/filepath.py src/twisted/python/
```




---

archive/issue_comments_064065.json:
```json
{
    "body": "New version with the fixes at http://sage.math.washington.edu/home/timdumol/twisted-9.0.p0.spkg. I neglected changing the version number.",
    "created_at": "2009-12-22T04:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64065",
    "user": "https://github.com/TimDumol"
}
```

New version with the fixes at http://sage.math.washington.edu/home/timdumol/twisted-9.0.p0.spkg. I neglected changing the version number.



---

archive/issue_comments_064066.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-22T04:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64066",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064067.json:
```json
{
    "body": "Should we add\n\n```sh\nrm -rf \"$SAGE_LOCAL\"/lib/python/site-packages/twisted\n```\n\nto\n\n```sh\n# Deleting the old version is *very* important with this package.\nrm -rf \"$SAGE_LOCAL\"/lib/python/site-packages/Twisted*\n```\n\nin `spkg-install`?",
    "created_at": "2010-01-15T20:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64067",
    "user": "https://github.com/qed777"
}
```

Should we add

```sh
rm -rf "$SAGE_LOCAL"/lib/python/site-packages/twisted
```

to

```sh
# Deleting the old version is *very* important with this package.
rm -rf "$SAGE_LOCAL"/lib/python/site-packages/Twisted*
```

in `spkg-install`?



---

archive/issue_comments_064068.json:
```json
{
    "body": "Also, `hg ci`.",
    "created_at": "2010-01-15T20:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64068",
    "user": "https://github.com/qed777"
}
```

Also, `hg ci`.



---

archive/issue_comments_064069.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> Also, `hg ci`.\nOops.  I mean that `hg stat` gives\n\n```\n! patches/filepath.py\n! patches/filepath.py.patch\n! patches/keys.py\n! patches/keys.py.patch\n! patches/sob.py\n! patches/sob.py.patch\n```\n",
    "created_at": "2010-01-15T20:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64069",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:8 mpatel]:
> Also, `hg ci`.
Oops.  I mean that `hg stat` gives

```
! patches/filepath.py
! patches/filepath.py.patch
! patches/keys.py
! patches/keys.py.patch
! patches/sob.py
! patches/sob.py.patch
```




---

archive/issue_comments_064070.json:
```json
{
    "body": "I've put these changes and added a description to `SPKG.txt` in\n\n* http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p1.spkg\n\nI didn't upgrade `zope.interface` to 3.5.3, since `sagenb-*.spkg` includes it.\n\nThe Se and doc tests pass for me.  Positive review, but someone should review my changes.",
    "created_at": "2010-01-15T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64070",
    "user": "https://github.com/qed777"
}
```

I've put these changes and added a description to `SPKG.txt` in

* http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p1.spkg

I didn't upgrade `zope.interface` to 3.5.3, since `sagenb-*.spkg` includes it.

The Se and doc tests pass for me.  Positive review, but someone should review my changes.



---

archive/issue_comments_064071.json:
```json
{
    "body": "I've not checked it for functionality, but this does at least build on Solaris. \n\nDave",
    "created_at": "2010-02-22T00:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64071",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've not checked it for functionality, but this does at least build on Solaris. 

Dave



---

archive/issue_comments_064072.json:
```json
{
    "body": "Requesting an assist, whenever it's convenient.",
    "created_at": "2010-02-22T21:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64072",
    "user": "https://github.com/qed777"
}
```

Requesting an assist, whenever it's convenient.



---

archive/issue_comments_064073.json:
```json
{
    "body": "Also see #8352, which makes a very small change to twisted's spkg-install file, so the previous version of twisted builds on any platform as 64-bit, not just OS X. \n\nBasically changing \n\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n   echo \"64 bit MacIntel\"\n   CFLAGS=\"-O2 -g -m64 \"; export CFLAGS\n   LDFLAGS=\"-m64 \"; export LDFLAGS\nfi\n\n```\n\n\nto\n\n\n```\nif [\"x$SAGE64\" = xyes ]; then\n   echo \"64 bit build\"\n   CFLAGS=\"-O2 -g -m64 \"; export CFLAGS\n   LDFLAGS=\"-m64 \"; export LDFLAGS\nfi\n```\n\n\nI'm happy to give the other ticket positive review, but are not going to just now, until I find the best way of handling this. \n\n\nDave",
    "created_at": "2010-02-24T21:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64073",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Also see #8352, which makes a very small change to twisted's spkg-install file, so the previous version of twisted builds on any platform as 64-bit, not just OS X. 

Basically changing 


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="-O2 -g -m64 "; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
fi

```


to


```
if ["x$SAGE64" = xyes ]; then
   echo "64 bit build"
   CFLAGS="-O2 -g -m64 "; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
fi
```


I'm happy to give the other ticket positive review, but are not going to just now, until I find the best way of handling this. 


Dave



---

archive/issue_comments_064074.json:
```json
{
    "body": "I got no feedback from sage-devel on the best way to handle this, so I've give #8352 positive review. \n\nI'm not marking it as 'needs work', as that might not be the right thing to do, it might be best if you incorporate the changes from that ticket too.",
    "created_at": "2010-02-25T03:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64074",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I got no feedback from sage-devel on the best way to handle this, so I've give #8352 positive review. 

I'm not marking it as 'needs work', as that might not be the right thing to do, it might be best if you incorporate the changes from that ticket too.



---

archive/issue_comments_064075.json:
```json
{
    "body": "I've added #8352's patch to\n\n* http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p2.spkg\n\nLet me know if there are any problems.",
    "created_at": "2010-02-25T08:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64075",
    "user": "https://github.com/qed777"
}
```

I've added #8352's patch to

* http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p2.spkg

Let me know if there are any problems.



---

archive/issue_comments_064076.json:
```json
{
    "body": "I think the first release of this in SPKG.txt should have been simply twisted-9.0 and not twisted-9.0.p0. The p's are only added after patches are applied at a later date. But it is pretty clear from the message that this was the first time version 9.0 was used, so I'm going to overlook that. \n\nI've added Jaap Spies as an author, as his changes are incorporated too. \n\n**Note to the release manager. When this ticket is merged, #8352 can be closed.**",
    "created_at": "2010-02-25T13:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64076",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I think the first release of this in SPKG.txt should have been simply twisted-9.0 and not twisted-9.0.p0. The p's are only added after patches are applied at a later date. But it is pretty clear from the message that this was the first time version 9.0 was used, so I'm going to overlook that. 

I've added Jaap Spies as an author, as his changes are incorporated too. 

**Note to the release manager. When this ticket is merged, #8352 can be closed.**



---

archive/issue_comments_064077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T13:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64077",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64078",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007782.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T22:45:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7552#event-7782"
}
```



---

archive/issue_comments_064079.json:
```json
{
    "body": "Merged [twisted-9.0.p2.spkg](http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p2.spkg) in the standard spkg repository.",
    "created_at": "2010-03-02T22:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7552#issuecomment-64079",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [twisted-9.0.p2.spkg](http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p2.spkg) in the standard spkg repository.
