# Issue 7162: maybe remove linking xpm into gd

archive/issues_007162.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein drkirkby @jaapspies\n\nI'm trying to build sage-4.1.2 on disk.math.washington.edu (opensolaris x86) and had to change the spkg-install of gd-2.0.35.p2:\n\n```\n# We explicitly disable X support, since (1) X is not a SAGE dependency,\n# and (2) the gd build fails on a lot of OS X PPC machines when X is enabled.\n./configure --prefix=\"$SAGE_LOCAL\" --without-jpeg --without-x --without-xpm --with-zlib=\"$SAGE_LOCAL\" --with-freetype=\"$SAGE_LOCAL\"\n```\n\nI added `--without-xpm`.\n\nMaybe we should make this standard?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7162\n\n",
    "created_at": "2009-10-08T20:07:15Z",
    "labels": [
        "component: porting: solaris",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "maybe remove linking xpm into gd",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7162",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @williamstein drkirkby @jaapspies

I'm trying to build sage-4.1.2 on disk.math.washington.edu (opensolaris x86) and had to change the spkg-install of gd-2.0.35.p2:

```
# We explicitly disable X support, since (1) X is not a SAGE dependency,
# and (2) the gd build fails on a lot of OS X PPC machines when X is enabled.
./configure --prefix="$SAGE_LOCAL" --without-jpeg --without-x --without-xpm --with-zlib="$SAGE_LOCAL" --with-freetype="$SAGE_LOCAL"
```

I added `--without-xpm`.

Maybe we should make this standard?


Issue created by migration from https://trac.sagemath.org/ticket/7162





---

archive/issue_comments_059263.json:
```json
{
    "body": "It seems sensible to make it standard to me. \n\nIf you want to post a package, I'll review it.",
    "created_at": "2009-11-04T04:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59263",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It seems sensible to make it standard to me. 

If you want to post a package, I'll review it.



---

archive/issue_comments_059264.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T18:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59264",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059265.json:
```json
{
    "body": "Attachment [7162.patch](tarball://root/attachments/some-uuid/ticket7162/7162.patch) by drkirkby created at 2010-01-02 18:49:34\n\nA revised .spkg can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg",
    "created_at": "2010-01-02T18:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59265",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [7162.patch](tarball://root/attachments/some-uuid/ticket7162/7162.patch) by drkirkby created at 2010-01-02 18:49:34

A revised .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg



---

archive/issue_comments_059266.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> A revised .spkg can be found at \n> \n> http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg\n\n\nThis change make the build depend on setting export CFLAGS=-m64\n\nIs this a good thing to  do?\n\nJaap",
    "created_at": "2010-01-02T21:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59266",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:2 drkirkby]:
> A revised .spkg can be found at 
> 
> http://boxen.math.washington.edu/home/kirkby/portability/gd-2.0.35.p3/gd-2.0.35.p3.spkg


This change make the build depend on setting export CFLAGS=-m64

Is this a good thing to  do?

Jaap



---

archive/issue_comments_059267.json:
```json
{
    "body": "Hi, \nyou have a point, but there was some logic to this. \n\nThe purpose of the ticket which William opened was to add \n\n```\n--without-xpm\n```\n\nto the line where the configure script it invoked. The ticket had nothing to to with SAGE64.\n\nI think whilst trying to build on Solaris in 64-bit mode, you should set CFLAGS and CXXFLAGS to include -m64, as that will allow **some** packages to build without making changes to their spkg-install files. This is one such package. \n\nI've written two scripts (#7505) which check what the compiler is (GCC, Sun Studio, HP, IBM etc). That ticket already has positive review. \n\nI've written an updated version of sage-env, #7818 which is awaiting review. That will uses those two script, determine the right compiler flag, then automatically export the right compiler flag to CFLAGS. \n\nAs such, I believe making only the change William suggested is sufficient in this case. Just export CFLAGS and CXXFLAGS to include -m64, and expect that in the next release or two, that will happen automatically for you. Doing this, will reduce somewhat the number of spkg-install files that need editing. \n\nDave",
    "created_at": "2010-01-02T22:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59267",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi, 
you have a point, but there was some logic to this. 

The purpose of the ticket which William opened was to add 

```
--without-xpm
```

to the line where the configure script it invoked. The ticket had nothing to to with SAGE64.

I think whilst trying to build on Solaris in 64-bit mode, you should set CFLAGS and CXXFLAGS to include -m64, as that will allow **some** packages to build without making changes to their spkg-install files. This is one such package. 

I've written two scripts (#7505) which check what the compiler is (GCC, Sun Studio, HP, IBM etc). That ticket already has positive review. 

I've written an updated version of sage-env, #7818 which is awaiting review. That will uses those two script, determine the right compiler flag, then automatically export the right compiler flag to CFLAGS. 

As such, I believe making only the change William suggested is sufficient in this case. Just export CFLAGS and CXXFLAGS to include -m64, and expect that in the next release or two, that will happen automatically for you. Doing this, will reduce somewhat the number of spkg-install files that need editing. 

Dave



---

archive/issue_comments_059268.json:
```json
{
    "body": "Ok, nobody is hurt here. People who are porting should know this.\n\nSo I give it a positive review.\n\nJaap",
    "created_at": "2010-01-02T23:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59268",
    "user": "https://github.com/jaapspies"
}
```

Ok, nobody is hurt here. People who are porting should know this.

So I give it a positive review.

Jaap



---

archive/issue_comments_059269.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-02T23:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59269",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7162#issuecomment-59270",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_016930.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-03T22:07:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7162",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7162#event-16930"
}
```
