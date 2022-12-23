# Issue 9465: Update to FriCAS 1.1.0

archive/issues_009465.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  hemmecke rws\n\nThe earliear upgrade is in http://trac.sagemath.org/sage_trac/ticket/9354\nAlso look at http://trac.sagemath.org/sage_trac/ticket/6517\nfor more information.\n\nhttp://sage.math.washington.edu/home/hemmecke/pub/fricas-1.1.0.spkg\n\nhttp://sage.math.washington.edu/home/hemmecke/pub/fricasaldor-1.1.0.spkg\n\nfricasaldor might not properly work on 64 bit machines or might not work at all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9465\n\n",
    "created_at": "2010-07-09T12:39:04Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "Update to FriCAS 1.1.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9465",
    "user": "hemmecke"
}
```
Assignee: AlexGhitza

CC:  hemmecke rws

The earliear upgrade is in http://trac.sagemath.org/sage_trac/ticket/9354
Also look at http://trac.sagemath.org/sage_trac/ticket/6517
for more information.

http://sage.math.washington.edu/home/hemmecke/pub/fricas-1.1.0.spkg

http://sage.math.washington.edu/home/hemmecke/pub/fricasaldor-1.1.0.spkg

fricasaldor might not properly work on 64 bit machines or might not work at all.

Issue created by migration from https://trac.sagemath.org/ticket/9465





---

archive/issue_comments_090769.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-09T12:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90769",
    "user": "hemmecke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090770.json:
```json
{
    "body": "Changing component from algebra to packages.",
    "created_at": "2010-09-02T11:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90770",
    "user": "AlexGhitza"
}
```

Changing component from algebra to packages.



---

archive/issue_comments_090771.json:
```json
{
    "body": "Would you like to make an spkg with current Fricas?\nI'll make sure to review it, etc.\nThanks!",
    "created_at": "2012-01-23T05:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90771",
    "user": "dimpase"
}
```

Would you like to make an spkg with current Fricas?
I'll make sure to review it, etc.
Thanks!



---

archive/issue_comments_090772.json:
```json
{
    "body": "for the record, fricas-1.0.9 spkg fails to install in Sage 4.8 on x86_64 Linux (Debian).",
    "created_at": "2012-01-23T05:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90772",
    "user": "dimpase"
}
```

for the record, fricas-1.0.9 spkg fails to install in Sage 4.8 on x86_64 Linux (Debian).



---

archive/issue_comments_090773.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-23T05:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90773",
    "user": "dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090774.json:
```json
{
    "body": "Why are you considering 1.0.9? Above you find a link to 1.1.0. and\nFriCAS progressed to 1.1.5.\n\nHowever, in 1.1.5 the aldor-interface is broken. It's already fixed in trunk,\nbut I tend to wait till 1.1.6 is released in order to produce a new spkg.\n\nFurthermore, quickly browsing over my spkg generation scripts, tells me,\nthat I will have to fix some small issues.\n\nBTW, is it still required that FriCAS for Sage must use ECL and not SBCL?\n\nRalf",
    "created_at": "2012-01-26T23:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90774",
    "user": "hemmecke"
}
```

Why are you considering 1.0.9? Above you find a link to 1.1.0. and
FriCAS progressed to 1.1.5.

However, in 1.1.5 the aldor-interface is broken. It's already fixed in trunk,
but I tend to wait till 1.1.6 is released in order to produce a new spkg.

Furthermore, quickly browsing over my spkg generation scripts, tells me,
that I will have to fix some small issues.

BTW, is it still required that FriCAS for Sage must use ECL and not SBCL?

Ralf



---

archive/issue_comments_090775.json:
```json
{
    "body": "Replying to [comment:5 hemmecke]:\n> Why are you considering 1.0.9? Above you find a link to 1.1.0. and\n> FriCAS progressed to 1.1.5.\n\nI was just pointing out that an upgrade is needed badly.\n\n\n> \n> However, in 1.1.5 the aldor-interface is broken. It's already fixed in trunk,\n> but I tend to wait till 1.1.6 is released in order to produce a new spkg.\n> \n> Furthermore, quickly browsing over my spkg generation scripts, tells me,\n> that I will have to fix some small issues.\n> \n> BTW, is it still required that FriCAS for Sage must use ECL and not SBCL?\n\nWas it ever required? I guess it was never assumed that SBCL is installed on the system, so by default\nFriCAS can fall back on ECL provided by Sage.\n(This would need a trivial adjustment of the spkg-install, I suppose).\n\nOn the other hand a fast interface to FriCAS would need an embeddable Lisp, and ECL fits this bill.\n\nDima\n \n\n> \n> Ralf",
    "created_at": "2012-01-28T10:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90775",
    "user": "dimpase"
}
```

Replying to [comment:5 hemmecke]:
> Why are you considering 1.0.9? Above you find a link to 1.1.0. and
> FriCAS progressed to 1.1.5.

I was just pointing out that an upgrade is needed badly.


> 
> However, in 1.1.5 the aldor-interface is broken. It's already fixed in trunk,
> but I tend to wait till 1.1.6 is released in order to produce a new spkg.
> 
> Furthermore, quickly browsing over my spkg generation scripts, tells me,
> that I will have to fix some small issues.
> 
> BTW, is it still required that FriCAS for Sage must use ECL and not SBCL?

Was it ever required? I guess it was never assumed that SBCL is installed on the system, so by default
FriCAS can fall back on ECL provided by Sage.
(This would need a trivial adjustment of the spkg-install, I suppose).

On the other hand a fast interface to FriCAS would need an embeddable Lisp, and ECL fits this bill.

Dima
 

> 
> Ralf



---

archive/issue_comments_090776.json:
```json
{
    "body": "Changing component from packages: standard to packages: experimental.",
    "created_at": "2014-11-13T13:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90776",
    "user": "jdemeyer"
}
```

Changing component from packages: standard to packages: experimental.



---

archive/issue_comments_090777.json:
```json
{
    "body": "Changing keywords from \"\" to \"fricas\".",
    "created_at": "2014-12-06T15:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90777",
    "user": "chapoton"
}
```

Changing keywords from "" to "fricas".



---

archive/issue_comments_090778.json:
```json
{
    "body": "Hi,\n\nCould we ship the last version ?\n\n```\nNovember 24, 2014 -- FriCAS 1.2.4 released.\n```\n\n\nVincent",
    "created_at": "2014-12-06T15:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90778",
    "user": "vdelecroix"
}
```

Hi,

Could we ship the last version ?

```
November 24, 2014 -- FriCAS 1.2.4 released.
```


Vincent



---

archive/issue_comments_090779.json:
```json
{
    "body": "I wrote the spkg-install and it at least compile on my computer... If anybody want to test it\n- download the source tarball `fricas-1.2.4-full.tar.bz2`, move it to `$SAGE_ROOT/upstream` and rename it `fricas-1.2.4.tar.bz2`\n- switch to the git branch provided here\n- run `sage -i fricas` and then `make` (from `$SAGE_ROOT`)\n\nI am currently trying to see whether the interface is not broken...\n\nVincent",
    "created_at": "2014-12-06T15:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90779",
    "user": "vdelecroix"
}
```

I wrote the spkg-install and it at least compile on my computer... If anybody want to test it
- download the source tarball `fricas-1.2.4-full.tar.bz2`, move it to `$SAGE_ROOT/upstream` and rename it `fricas-1.2.4.tar.bz2`
- switch to the git branch provided here
- run `sage -i fricas` and then `make` (from `$SAGE_ROOT`)

I am currently trying to see whether the interface is not broken...

Vincent



---

archive/issue_comments_090780.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-06T15:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90780",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090781.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-06T15:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90781",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090782.json:
```json
{
    "body": "Looks like it work -> needs review.",
    "created_at": "2014-12-06T15:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90782",
    "user": "vdelecroix"
}
```

Looks like it work -> needs review.



---

archive/issue_comments_090783.json:
```json
{
    "body": "I have added a few '#optional - fricas' so that the tests pass both with '-optional=fricas' and without, in 'interfaces/fricas.py'\n----\nNew commits:",
    "created_at": "2014-12-06T16:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90783",
    "user": "chapoton"
}
```

I have added a few '#optional - fricas' so that the tests pass both with '-optional=fricas' and without, in 'interfaces/fricas.py'
----
New commits:



---

archive/issue_comments_090784.json:
```json
{
    "body": "Looks good to me. If somebody else can confirm, this seems to be good to go.",
    "created_at": "2014-12-06T16:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90784",
    "user": "chapoton"
}
```

Looks good to me. If somebody else can confirm, this seems to be good to go.



---

archive/issue_comments_090785.json:
```json
{
    "body": "Wow, fricas has Puiseux series. Builds fine. Passes all tests in `interfaces`, `rings`, and `structure`.",
    "created_at": "2014-12-06T16:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90785",
    "user": "rws"
}
```

Wow, fricas has Puiseux series. Builds fine. Passes all tests in `interfaces`, `rings`, and `structure`.



---

archive/issue_comments_090786.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-06T16:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90786",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090787.json:
```json
{
    "body": "1. See also http://fricas.github.io\n\n2. What exactly is the problem with fricas-aldor on 64bit machines?\n\n3. Meanwhile Aldor is under the Apache License 2.0. So fricas-aldor could even install Aldor. Or there should be another spkg that installs Aldor and fricas-aldor might trigger installation of Aldor, if it is not already there.",
    "created_at": "2014-12-06T17:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90787",
    "user": "hemmecke"
}
```

1. See also http://fricas.github.io

2. What exactly is the problem with fricas-aldor on 64bit machines?

3. Meanwhile Aldor is under the Apache License 2.0. So fricas-aldor could even install Aldor. Or there should be another spkg that installs Aldor and fricas-aldor might trigger installation of Aldor, if it is not already there.



---

archive/issue_comments_090788.json:
```json
{
    "body": "Replying to [comment:24 hemmecke]:\n> 1. See also http://fricas.github.io\n\nThe documentation is much nicer there... why the project is both on sourceforge and github ?\n\n> 2. What exactly is the problem with fricas-aldor on 64bit machines?\n\nNo idea... I have to try, where the source code is available ?\n\n> 3. Meanwhile Aldor is under the Apache License 2.0. So fricas-aldor could even install Aldor. Or there should be another spkg that installs Aldor and fricas-aldor might trigger installation of Aldor, if it is not already there.\n\nI guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.\n\nVincent",
    "created_at": "2014-12-06T17:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90788",
    "user": "vdelecroix"
}
```

Replying to [comment:24 hemmecke]:
> 1. See also http://fricas.github.io

The documentation is much nicer there... why the project is both on sourceforge and github ?

> 2. What exactly is the problem with fricas-aldor on 64bit machines?

No idea... I have to try, where the source code is available ?

> 3. Meanwhile Aldor is under the Apache License 2.0. So fricas-aldor could even install Aldor. Or there should be another spkg that installs Aldor and fricas-aldor might trigger installation of Aldor, if it is not already there.

I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.

Vincent



---

archive/issue_comments_090789.json:
```json
{
    "body": "Replying to [comment:25 vdelecroix]:\n> The documentation is much nicer there... why the project is both on sourceforge and github ?\n\nThe project is officially on sourceforge and still under SVN. :-( But since I think git is tremendously better, I created a life mirror at github.\nSee https://sites.google.com/site/hemmecke/fricas-svn#fricas-devel for details.\nI'd be happy if FriCAS switched completely to git, but that's not a big issue with mainly only Waldek and me commiting to the code base.\n \n> > 2. What exactly is the problem with fricas-aldor on 64bit machines?\n> \n> No idea... I have to try, where the source code is available ?\n\nSource code of what?\n\nAldor: https://github.com/pippijn/aldor\nfricas-aldor spkg: ummmm.... I used to have a hg repo somewhere on my sagemath account, but don't know what the computer is that I have to login. I would then try to convert it to git and put it to github.\n\n> I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.\n\nPlease do that and put me into the CC. I'm currently a little unfamiliar with Sage development.",
    "created_at": "2014-12-06T18:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90789",
    "user": "hemmecke"
}
```

Replying to [comment:25 vdelecroix]:
> The documentation is much nicer there... why the project is both on sourceforge and github ?

The project is officially on sourceforge and still under SVN. :-( But since I think git is tremendously better, I created a life mirror at github.
See https://sites.google.com/site/hemmecke/fricas-svn#fricas-devel for details.
I'd be happy if FriCAS switched completely to git, but that's not a big issue with mainly only Waldek and me commiting to the code base.
 
> > 2. What exactly is the problem with fricas-aldor on 64bit machines?
> 
> No idea... I have to try, where the source code is available ?

Source code of what?

Aldor: https://github.com/pippijn/aldor
fricas-aldor spkg: ummmm.... I used to have a hg repo somewhere on my sagemath account, but don't know what the computer is that I have to login. I would then try to convert it to git and put it to github.

> I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.

Please do that and put me into the CC. I'm currently a little unfamiliar with Sage development.



---

archive/issue_comments_090790.json:
```json
{
    "body": "Replying to [comment:26 hemmecke]:\n> Replying to [comment:25 vdelecroix]:\n>  \n> > > 2. What exactly is the problem with fricas-aldor on 64bit machines?\n> > \n> > No idea... I have to try, where the source code is available ?\n> \n> Source code of what?\n> \n> Aldor: https://github.com/pippijn/aldor\n> fricas-aldor spkg: ummmm.... I used to have a hg repo somewhere on my sagemath account, but don't know what the computer is that I have to login. I would then try to convert it to git and put it to github.\n\nIt would be better to have a link to a stable release with a version number (i.e. \"an official tarball\"). Otherwise we need to artificially create one.\n\n> > I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.\n> \n> Please do that and put me into the CC. I'm currently a little unfamiliar with Sage development.\n\nTo create packages the documentation is very well written: http://sagemath.org/doc/developer/packaging.html (I might help for that step). Then there is the second step of having an interface within sage (I have very little experience with that).\n\nVincent",
    "created_at": "2014-12-06T20:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90790",
    "user": "vdelecroix"
}
```

Replying to [comment:26 hemmecke]:
> Replying to [comment:25 vdelecroix]:
>  
> > > 2. What exactly is the problem with fricas-aldor on 64bit machines?
> > 
> > No idea... I have to try, where the source code is available ?
> 
> Source code of what?
> 
> Aldor: https://github.com/pippijn/aldor
> fricas-aldor spkg: ummmm.... I used to have a hg repo somewhere on my sagemath account, but don't know what the computer is that I have to login. I would then try to convert it to git and put it to github.

It would be better to have a link to a stable release with a version number (i.e. "an official tarball"). Otherwise we need to artificially create one.

> > I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.
> 
> Please do that and put me into the CC. I'm currently a little unfamiliar with Sage development.

To create packages the documentation is very well written: http://sagemath.org/doc/developer/packaging.html (I might help for that step). Then there is the second step of having an interface within sage (I have very little experience with that).

Vincent



---

archive/issue_comments_090791.json:
```json
{
    "body": "See #9427 for a follow-up ticket on integration.",
    "created_at": "2014-12-07T11:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90791",
    "user": "chapoton"
}
```

See #9427 for a follow-up ticket on integration.



---

archive/issue_comments_090792.json:
```json
{
    "body": "No $`@`#$ sourceforge links the next time, please.",
    "created_at": "2014-12-11T17:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90792",
    "user": "vbraun"
}
```

No $`@`#$ sourceforge links the next time, please.



---

archive/issue_comments_090793.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-12-12T12:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90793",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_090794.json:
```json
{
    "body": "FYI: optional doctests don't pass, so the package was moved to experimental.",
    "created_at": "2015-06-06T09:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9465#issuecomment-90794",
    "user": "jdemeyer"
}
```

FYI: optional doctests don't pass, so the package was moved to experimental.
