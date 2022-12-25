# Issue 8191: Add iconv needed for Solaris, and possibly Cygwin too

archive/issues_008191.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @mwhansen @williamstein\n\nKeywords: iconv solaris cygwin\n\nThe latest version of R in Sage 2.10.1, needs a powerful version of iconv. The version of iconv in Solaris is not sufficiently powerful.  This is documented in the 'R Installation and Administration' manual under the *Solaris* section.\n\nhttp://cran.r-project.org/doc/manuals/R-admin.pdf\n\n\n#3381 added a command line option to the configure script to disable the use of iconv. \n\nFor a long time R has been reporting messages that this option would be removed, and it would be necessary to install iconv. Well that time has come.\n\n```\nchecking for cblas_cdotu_sub in vecLib framework... no\nchecking iconv.h usability... yes\nchecking iconv.h presence... yes\nchecking for iconv.h... yes\nchecking for iconv... yes\nchecking whether iconv accepts \"UTF-8\", \"latin1\" and \"UCS-*\"... no\nconfigure: error: a suitable iconv is essential\nError configuring R.\n\nreal    2m15.532s\nuser    0m47.020s\nsys    1m9.582s\nsage: An error occurred while installing r-2.10.1\n```\n\nSo we must have an inconv package. I will create one. \n\nIt looks as though this will be needed on Cygwin also - see #7319. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8191\n\n",
    "closed_at": "2010-03-02T22:38:46Z",
    "created_at": "2010-02-05T10:32:33Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Add iconv needed for Solaris, and possibly Cygwin too",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8191",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @mwhansen @williamstein

Keywords: iconv solaris cygwin

The latest version of R in Sage 2.10.1, needs a powerful version of iconv. The version of iconv in Solaris is not sufficiently powerful.  This is documented in the 'R Installation and Administration' manual under the *Solaris* section.

http://cran.r-project.org/doc/manuals/R-admin.pdf


#3381 added a command line option to the configure script to disable the use of iconv. 

For a long time R has been reporting messages that this option would be removed, and it would be necessary to install iconv. Well that time has come.

```
checking for cblas_cdotu_sub in vecLib framework... no
checking iconv.h usability... yes
checking iconv.h presence... yes
checking for iconv.h... yes
checking for iconv... yes
checking whether iconv accepts "UTF-8", "latin1" and "UCS-*"... no
configure: error: a suitable iconv is essential
Error configuring R.

real    2m15.532s
user    0m47.020s
sys    1m9.582s
sage: An error occurred while installing r-2.10.1
```

So we must have an inconv package. I will create one. 

It looks as though this will be needed on Cygwin also - see #7319. 


Issue created by migration from https://trac.sagemath.org/ticket/8191





---

archive/issue_comments_072068.json:
```json
{
    "body": "I'm cc'in Mike on this ticket, as I believe it has implications for his ticket #7319\n\nDave",
    "created_at": "2010-02-05T10:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72068",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm cc'in Mike on this ticket, as I believe it has implications for his ticket #7319

Dave



---

archive/issue_comments_072069.json:
```json
{
    "body": "I've created iconv-1.13.1.spkg which is the latest release. \n\nI have **not** added the Mercurial repository, as I was not exactly sure how to do it. This will need to go as a standard package, and another part of Sage will need to ensure that inconv gets built. \n\nI've marked it as 'needs info' rather than for review, as at this stage there is no Mercurial repository. But perhaps people can test it out. \n\nhttp://boxen.math.washington.edu/home/kirkby/new-packages/iconv\n\nI've personally tested it on the following. If the self-tests are uncommented, (see spkg-install), then all tests do pass except on Solaris 10 (SPARC), where ./check-subst dumps core in both 32-bit and 64-bit mode on two separate machines. \n\n* sage.math Linux (defaults to 64-bit) \n* bsd.math OS X (defaults to 64-bit)\n* OpenSolaris 06/2009 on a Sun Ultra 27 (Intel Xeon processor) - 32-bit\n* OpenSolaris 06/2009 on a Sun Ultra 27 (Intel Xeon processor) - 64-bit. \n* Solaris 10 03/2005 on a Sun Blade 1000 (UltraSPARC III+ processor) - 32-bit \n* Solaris 10 03/2005 on a Sun Blade 1000 (UltraSPARC III+ processor) - 64-bit \n\nThere is still an issue with R 2.10.1 building on Solaris (SPARC), but it gets a lot further with this iconv package built. We can sort out the problems with R later. There are tons of options given to the R configure script, at least one of which is not valid. I suspect by changing the options and removing the invalid code in R's spkg-install file, then R can be made to build on Solaris. \n\nDave",
    "created_at": "2010-02-14T04:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72069",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've created iconv-1.13.1.spkg which is the latest release. 

I have **not** added the Mercurial repository, as I was not exactly sure how to do it. This will need to go as a standard package, and another part of Sage will need to ensure that inconv gets built. 

I've marked it as 'needs info' rather than for review, as at this stage there is no Mercurial repository. But perhaps people can test it out. 

http://boxen.math.washington.edu/home/kirkby/new-packages/iconv

I've personally tested it on the following. If the self-tests are uncommented, (see spkg-install), then all tests do pass except on Solaris 10 (SPARC), where ./check-subst dumps core in both 32-bit and 64-bit mode on two separate machines. 

* sage.math Linux (defaults to 64-bit) 
* bsd.math OS X (defaults to 64-bit)
* OpenSolaris 06/2009 on a Sun Ultra 27 (Intel Xeon processor) - 32-bit
* OpenSolaris 06/2009 on a Sun Ultra 27 (Intel Xeon processor) - 64-bit. 
* Solaris 10 03/2005 on a Sun Blade 1000 (UltraSPARC III+ processor) - 32-bit 
* Solaris 10 03/2005 on a Sun Blade 1000 (UltraSPARC III+ processor) - 64-bit 

There is still an issue with R 2.10.1 building on Solaris (SPARC), but it gets a lot further with this iconv package built. We can sort out the problems with R later. There are tons of options given to the R configure script, at least one of which is not valid. I suspect by changing the options and removing the invalid code in R's spkg-install file, then R can be made to build on Solaris. 

Dave



---

archive/issue_comments_072070.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-02-14T04:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72070",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_072071.json:
```json
{
    "body": "I believe the iconv package is now ready for review. \n\n* spkg-check has been added. \n* The Mercurial repository has been added. \n* As shown below, iconv is tested by R and found to be suitable. \n\n```\nDisabling libiconv support on Solaris\nchecking iconv.h usability... yes\nchecking iconv.h presence... yes\nchecking for iconv.h... yes\nchecking for iconv... in libiconv\nchecking whether iconv accepts \"UTF-8\", \"latin1\" and \"UCS-*\"... yes\nchecking for iconvlist... yes\nchecking for iconv... yes\n```\n\nThe message \n\n```\nDisabling libiconv support on Solaris\n```\nis from R's spkg-install, so needs to be removed. That is ticket #8272\n\nIt should be noted that.  \n* The test failure seen on Solaris 10 (SPARC) but not on OS X, Linux or OpenSolaris has a trac item for it. #8271\n* The failure of iconv's 'make check' to actually exit with a non-zero exit code when it encounters a failure has a trac ticket for it #8270.",
    "created_at": "2010-02-15T11:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72071",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I believe the iconv package is now ready for review. 

* spkg-check has been added. 
* The Mercurial repository has been added. 
* As shown below, iconv is tested by R and found to be suitable. 

```
Disabling libiconv support on Solaris
checking iconv.h usability... yes
checking iconv.h presence... yes
checking for iconv.h... yes
checking for iconv... in libiconv
checking whether iconv accepts "UTF-8", "latin1" and "UCS-*"... yes
checking for iconvlist... yes
checking for iconv... yes
```

The message 

```
Disabling libiconv support on Solaris
```
is from R's spkg-install, so needs to be removed. That is ticket #8272

It should be noted that.  
* The test failure seen on Solaris 10 (SPARC) but not on OS X, Linux or OpenSolaris has a trac item for it. #8271
* The failure of iconv's 'make check' to actually exit with a non-zero exit code when it encounters a failure has a trac ticket for it #8270.



---

archive/issue_comments_072072.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-15T11:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72072",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_072073.json:
```json
{
    "body": "Changing component from solaris to packages.",
    "created_at": "2010-02-15T11:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72073",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from solaris to packages.



---

archive/issue_comments_072074.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-15T11:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72074",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072075.json:
```json
{
    "body": "Oops, I forget to attach the revised spkg/install and spkg/standard/deps. I'll do that in a minute.",
    "created_at": "2010-02-15T11:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72075",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Oops, I forget to attach the revised spkg/install and spkg/standard/deps. I'll do that in a minute.



---

archive/issue_comments_072076.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket8191/install) by drkirkby created at 2010-02-15 11:51:27\n\nNew $SAGE_ROOT/spkg/install to add support for the new iconv package",
    "created_at": "2010-02-15T11:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72076",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket8191/install) by drkirkby created at 2010-02-15 11:51:27

New $SAGE_ROOT/spkg/install to add support for the new iconv package



---

archive/issue_comments_072077.json:
```json
{
    "body": "Attachment [install.diff](tarball://root/attachments/some-uuid/ticket8191/install.diff) by drkirkby created at 2010-02-15 11:52:02\n\nDiff for for $SAGE_ROOT/spkg/install",
    "created_at": "2010-02-15T11:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72077",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [install.diff](tarball://root/attachments/some-uuid/ticket8191/install.diff) by drkirkby created at 2010-02-15 11:52:02

Diff for for $SAGE_ROOT/spkg/install



---

archive/issue_comments_072078.json:
```json
{
    "body": "New $SAGE_ROOT/spkg/standard/deps",
    "created_at": "2010-02-15T11:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72078",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

New $SAGE_ROOT/spkg/standard/deps



---

archive/issue_comments_072079.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket8191/deps) by drkirkby created at 2010-02-15 11:54:31\n\nDiff file for $SAGE_ROOT/spkg/standard/deps",
    "created_at": "2010-02-15T11:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72079",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket8191/deps) by drkirkby created at 2010-02-15 11:54:31

Diff file for $SAGE_ROOT/spkg/standard/deps



---

archive/issue_comments_072080.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8191/deps.diff) by drkirkby created at 2010-02-15 11:59:02\n\nI've attached the following two files, in addition to diffs to their originals. Neither file appear to be are under revision control, so I assume these two files will have to be manually integrated.  \n\n```\n$SAGE_ROOT/spkg/standard/deps \n$SAGE_ROOT/spkg/install \n```\n\nI've made gdmodule, Python and R all depend on iconv, as all of them check for iconv. \n\n**This is now ready for review!!!**\n\nDave",
    "created_at": "2010-02-15T11:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72080",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8191/deps.diff) by drkirkby created at 2010-02-15 11:59:02

I've attached the following two files, in addition to diffs to their originals. Neither file appear to be are under revision control, so I assume these two files will have to be manually integrated.  

```
$SAGE_ROOT/spkg/standard/deps 
$SAGE_ROOT/spkg/install 
```

I've made gdmodule, Python and R all depend on iconv, as all of them check for iconv. 

**This is now ready for review!!!**

Dave



---

archive/issue_comments_072081.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-15T11:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72081",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072082.json:
```json
{
    "body": "I'm attaching a Mercurial patch too",
    "created_at": "2010-02-17T00:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72082",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm attaching a Mercurial patch too



---

archive/issue_comments_072083.json:
```json
{
    "body": "Mercurial patch",
    "created_at": "2010-02-17T00:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72083",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch



---

archive/issue_comments_072084.json:
```json
{
    "body": "Attachment [R.patch](tarball://root/attachments/some-uuid/ticket8191/R.patch) by drkirkby created at 2010-02-17 00:21:38\n\nI called the Mercurial patch \"R.patch\", which was probably not a very sensible name. It is for the iconv package.",
    "created_at": "2010-02-17T00:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72084",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [R.patch](tarball://root/attachments/some-uuid/ticket8191/R.patch) by drkirkby created at 2010-02-17 00:21:38

I called the Mercurial patch "R.patch", which was probably not a very sensible name. It is for the iconv package.



---

archive/issue_comments_072085.json:
```json
{
    "body": "The new iconv package builds on sage.math, bsd.math, rosemary.math, t2.math, Skynet machines (cleo and iras), and Cygwin (winxp1 on boxen.math). \n\n\n\n\n**Note to release manager:** Replace the current file `spkg/install` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/install). Also replace the current file `spkg/standard/deps` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/deps). Both `install` and `deps` are not under revision control, so one has to replace them with updated versions. Make sure to turn on the executable bits of `install`.",
    "created_at": "2010-02-21T21:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The new iconv package builds on sage.math, bsd.math, rosemary.math, t2.math, Skynet machines (cleo and iras), and Cygwin (winxp1 on boxen.math). 




**Note to release manager:** Replace the current file `spkg/install` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/install). Also replace the current file `spkg/standard/deps` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/deps). Both `install` and `deps` are not under revision control, so one has to replace them with updated versions. Make sure to turn on the executable bits of `install`.



---

archive/issue_comments_072086.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T21:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072087.json:
```json
{
    "body": "At #8306, I've added iconv to gd's dependencies to keep make from building gd too early.  Should we do that here?",
    "created_at": "2010-02-27T07:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72087",
    "user": "https://github.com/qed777"
}
```

At #8306, I've added iconv to gd's dependencies to keep make from building gd too early.  Should we do that here?



---

archive/issue_comments_072088.json:
```json
{
    "body": "Yes, well spotted. You were right to add it to #8036. \n\nIn practice however it will make no difference on Linux, Solaris or OS X as they all come with a version of iconv suitable for gd. It is only R on Solaris which needs this iconv package built, as the iconv shipped with Solaris is not suitable for building the latest versions of R. \n\nSince Minh has already tested this on multiple machines and given it positive review, I'm reluctant to change anything now, which might delay the package getting into Sage, as it would then need reviewing again. \n\nDelaying this getting into Sage will stop Sage working on Solaris. Whether iconv gets built before or after gd will make no difference on any supported platform. \n\nSince #8306 will have a dependancy on this, you have already taken care of the gd dependancy, so again I think that points to the fact there is no need to change this. \n\nDave",
    "created_at": "2010-02-27T14:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72088",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Yes, well spotted. You were right to add it to #8036. 

In practice however it will make no difference on Linux, Solaris or OS X as they all come with a version of iconv suitable for gd. It is only R on Solaris which needs this iconv package built, as the iconv shipped with Solaris is not suitable for building the latest versions of R. 

Since Minh has already tested this on multiple machines and given it positive review, I'm reluctant to change anything now, which might delay the package getting into Sage, as it would then need reviewing again. 

Delaying this getting into Sage will stop Sage working on Solaris. Whether iconv gets built before or after gd will make no difference on any supported platform. 

Since #8306 will have a dependancy on this, you have already taken care of the gd dependancy, so again I think that points to the fact there is no need to change this. 

Dave



---

archive/issue_comments_072089.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> Yes, well spotted. You were right to add it to #8036. \n\n\nOops, you were right to add it to #8306 was what I meant to write.",
    "created_at": "2010-02-27T14:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72089",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:11 drkirkby]:
> Yes, well spotted. You were right to add it to #8036. 


Oops, you were right to add it to #8306 was what I meant to write.



---

archive/issue_comments_072090.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-01T16:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72090",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_072091.json:
```json
{
    "body": "apply to script repository; depends on #8307",
    "created_at": "2010-03-02T19:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72091",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

apply to script repository; depends on #8307



---

archive/issue_comments_072092.json:
```json
{
    "body": "Attachment [trac_8191-reviewer.patch](tarball://root/attachments/some-uuid/ticket8191/trac_8191-reviewer.patch) by mvngu created at 2010-03-02 19:27:57\n\nThe iconv spkg installs a binary called \"iconv\" to `SAGE_LOCAL/bin`, a directory which is under revision control. Usually, we don't put executable binaries under revision control. After installing the iconv spkg, I get this:\n\n```\n[mvngu@sage bin]$ hg st\n? iconv\n```\nThe file `.hgignore` needs to be configured to ignore this file. I have attached [trac_8191-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/trac_8191-reviewer.patch) which does this. Apply that patch to the script repository. It depends on the patch at #8307. Only my patch needs review by anyone but me.",
    "created_at": "2010-03-02T19:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8191-reviewer.patch](tarball://root/attachments/some-uuid/ticket8191/trac_8191-reviewer.patch) by mvngu created at 2010-03-02 19:27:57

The iconv spkg installs a binary called "iconv" to `SAGE_LOCAL/bin`, a directory which is under revision control. Usually, we don't put executable binaries under revision control. After installing the iconv spkg, I get this:

```
[mvngu@sage bin]$ hg st
? iconv
```
The file `.hgignore` needs to be configured to ignore this file. I have attached [trac_8191-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/trac_8191-reviewer.patch) which does this. Apply that patch to the script repository. It depends on the patch at #8307. Only my patch needs review by anyone but me.



---

archive/issue_comments_072093.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-02T19:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072094.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-02T19:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072095.json:
```json
{
    "body": "Thanks Minh. Yes, that makes perfect sense. Positive review from me.",
    "created_at": "2010-03-02T20:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72095",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thanks Minh. Yes, that makes perfect sense. Positive review from me.



---

archive/issue_comments_072096.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-02T20:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72096",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019598.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T22:38:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8191#event-19598"
}
```



---

archive/issue_comments_072097.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72097",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_072098.json:
```json
{
    "body": "Merged in this order:\n\n1. Replace current \"install\" under `SAGE_ROOT/spkg` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/install).\n2. Replace current \"deps\" under `SAGE_ROOT/spkg/standard` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/deps).\n3. Merged [iconv-1.13.1.spkg](http://boxen.math.washington.edu/home/kirkby/new-packages/iconv/iconv-1.13.1.spkg) in the standard spkg repository.\n4. Merged [trac_8191-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/trac_8191-reviewer.patch) in the script repository.",
    "created_at": "2010-03-02T22:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72098",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. Replace current "install" under `SAGE_ROOT/spkg` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/install).
2. Replace current "deps" under `SAGE_ROOT/spkg/standard` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/deps).
3. Merged [iconv-1.13.1.spkg](http://boxen.math.washington.edu/home/kirkby/new-packages/iconv/iconv-1.13.1.spkg) in the standard spkg repository.
4. Merged [trac_8191-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/trac_8191-reviewer.patch) in the script repository.



---

archive/issue_comments_072099.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> In practice however it will make no difference on Linux, Solaris or OS X as they all come with a version of iconv suitable for gd.\n\n\nSage 4.3.4.alpha0 fails to build on a Fedora Linux system because iconv is not yet part of the dependency rule for building gd. This issue is now tracked at #8432.",
    "created_at": "2010-03-04T03:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8191#issuecomment-72099",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:11 drkirkby]:
> In practice however it will make no difference on Linux, Solaris or OS X as they all come with a version of iconv suitable for gd.


Sage 4.3.4.alpha0 fails to build on a Fedora Linux system because iconv is not yet part of the dependency rule for building gd. This issue is now tracked at #8432.
