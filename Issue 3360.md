# Issue 3360: Upgarde sympow to the 1.019 release

archive/issues_003360.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  slelievre @timokau saraedum isuruf arojas mjo embray dimpase tscrim\n\nSympow 1.019 is already upstream in Debian, so let's upgrade.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3360\n\n",
    "created_at": "2008-06-04T15:51:07Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Upgarde sympow to the 1.019 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3360",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  slelievre @timokau saraedum isuruf arojas mjo embray dimpase tscrim

Sympow 1.019 is already upstream in Debian, so let's upgrade.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3360





---

archive/issue_comments_023392.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-02T04:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23392",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023393.json:
```json
{
    "body": "The latest release is 1.023 at\n\n http://magma.maths.usyd.edu.au/~watkins/sympow.tar.bz2\n http://magma.maths.usyd.edu.au/~watkins/sympow.src.tar.bz2\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T04:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23393",
    "user": "mabshoff"
}
```

The latest release is 1.023 at

 http://magma.maths.usyd.edu.au/~watkins/sympow.tar.bz2
 http://magma.maths.usyd.edu.au/~watkins/sympow.src.tar.bz2

Cheers,

Michael



---

archive/issue_comments_023394.json:
```json
{
    "body": "Changing keywords from \"\" to \"upgrade, sympow\".",
    "created_at": "2018-04-20T20:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23394",
    "user": "slelievre"
}
```

Changing keywords from "" to "upgrade, sympow".



---

archive/issue_comments_023395.json:
```json
{
    "body": "Didn't realise there was a newer version. Considering sympow's code, an upgrade can only be an improvement.",
    "created_at": "2018-04-20T22:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23395",
    "user": "fbissey"
}
```

Didn't realise there was a newer version. Considering sympow's code, an upgrade can only be an improvement.



---

archive/issue_comments_023396.json:
```json
{
    "body": "See also #25099 \"Add DESTDIR support for sympow\".",
    "created_at": "2018-06-02T09:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23396",
    "user": "slelievre"
}
```

See also #25099 "Add DESTDIR support for sympow".



---

archive/issue_comments_023397.json:
```json
{
    "body": "sympow 1.023 segfaults (in Debian) on some inputs that used to work with 1.018\n\n```\n$ sympow -analrank -curve \"[0,1,1,-2,0]\"\nsympow 1.023 RELEASE (Debian 1.023-8)  (c) Mark Watkins --- see README and COPYING for details\nMinimal model of curve  is [0,1,1,-2,0]\nAt 389: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nConductor is 389\nsp 1: Conductor at 389 is 1+0, root number is -1\nsp 1: Euler factor at 389 is 1-1*x\n1st sym power conductor is 389, global root number is 1\nNT 1d0: 43\nMaximal number of terms is 43\n0.0E+00\nDone with small primes 1049\nSegmentation fault (core dumped)\n```\n",
    "created_at": "2018-06-14T10:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23397",
    "user": "saraedum"
}
```

sympow 1.023 segfaults (in Debian) on some inputs that used to work with 1.018

```
$ sympow -analrank -curve "[0,1,1,-2,0]"
sympow 1.023 RELEASE (Debian 1.023-8)  (c) Mark Watkins --- see README and COPYING for details
Minimal model of curve  is [0,1,1,-2,0]
At 389: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
Conductor is 389
sp 1: Conductor at 389 is 1+0, root number is -1
sp 1: Euler factor at 389 is 1-1*x
1st sym power conductor is 389, global root number is 1
NT 1d0: 43
Maximal number of terms is 43
0.0E+00
Done with small primes 1049
Segmentation fault (core dumped)
```




---

archive/issue_comments_023398.json:
```json
{
    "body": "This is essentially a known bug: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863919. I submitted a patch for it on salsa: https://salsa.debian.org/science-team/sympow/merge_requests/1.",
    "created_at": "2018-06-14T12:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23398",
    "user": "saraedum"
}
```

This is essentially a known bug: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863919. I submitted a patch for it on salsa: https://salsa.debian.org/science-team/sympow/merge_requests/1.



---

archive/issue_comments_023399.json:
```json
{
    "body": "In an effort to update the sympow package in nix, I contacted the debian maintainer (Jerome Benoit).\n\nHe told me that he really did receive their tarball in a private email (how did you guys manage to find that file on his homepage?). He also told me that \"the upstream author is responsive (and he did not have a GIT because the code was written before the GIT revolution)\".\n\nDebian adds sage's patches and some more[1], as for example the bug fix saraedum mentions. It seems like Debian effectively became the new upstream of this package. I asked the maintainer if he had considered making it official and forking it, which he declined.\n\n[1] https://salsa.debian.org/science-team/sympow/tree/master/debian/patches",
    "created_at": "2018-07-13T19:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23399",
    "user": "@timokau"
}
```

In an effort to update the sympow package in nix, I contacted the debian maintainer (Jerome Benoit).

He told me that he really did receive their tarball in a private email (how did you guys manage to find that file on his homepage?). He also told me that "the upstream author is responsive (and he did not have a GIT because the code was written before the GIT revolution)".

Debian adds sage's patches and some more[1], as for example the bug fix saraedum mentions. It seems like Debian effectively became the new upstream of this package. I asked the maintainer if he had considered making it official and forking it, which he declined.

[1] https://salsa.debian.org/science-team/sympow/tree/master/debian/patches



---

archive/issue_comments_023400.json:
```json
{
    "body": "Replying to [comment:12 gh-timokau]:\n> He told me that he really did receive their tarball in a private email (how did you guys manage to find that file on his homepage?).\nIn my case: I wrote a private email to the sympow author and he told me about the URL.\n\n> He also told me that \"the upstream author is responsive (and he did not have a GIT because the code was written before the GIT revolution)\".\n> Debian adds sage's patches and some more[1], as for example the bug fix saraedum mentions. It seems like Debian effectively became the new upstream of this package. I asked the maintainer if he had considered making it official and forking it, which he declined.\n> \n> [1] https://salsa.debian.org/science-team/sympow/tree/master/debian/patches\nI was in correspondence with the sympow author about the recent segfault patch. Afterwards I proposed to move the project to github and basically take over maintenance but I have not heard back for a while since then.",
    "created_at": "2018-07-13T19:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23400",
    "user": "saraedum"
}
```

Replying to [comment:12 gh-timokau]:
> He told me that he really did receive their tarball in a private email (how did you guys manage to find that file on his homepage?).
In my case: I wrote a private email to the sympow author and he told me about the URL.

> He also told me that "the upstream author is responsive (and he did not have a GIT because the code was written before the GIT revolution)".
> Debian adds sage's patches and some more[1], as for example the bug fix saraedum mentions. It seems like Debian effectively became the new upstream of this package. I asked the maintainer if he had considered making it official and forking it, which he declined.
> 
> [1] https://salsa.debian.org/science-team/sympow/tree/master/debian/patches
I was in correspondence with the sympow author about the recent segfault patch. Afterwards I proposed to move the project to github and basically take over maintenance but I have not heard back for a while since then.



---

archive/issue_comments_023401.json:
```json
{
    "body": "Is the URL still valid ?\nOtherwise, after all, I may also consider to maintain a fork of sympow.",
    "created_at": "2018-07-13T19:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23401",
    "user": "@jgmbenoit"
}
```

Is the URL still valid ?
Otherwise, after all, I may also consider to maintain a fork of sympow.



---

archive/issue_comments_023402.json:
```json
{
    "body": "sympow still seems to be hosted at that URL. Its just not advertised anywhere. But there are still all those semi-mandatory patches flying around that should probably be upstreamed. Having the project in some public version control would be great.",
    "created_at": "2018-07-13T21:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23402",
    "user": "@timokau"
}
```

sympow still seems to be hosted at that URL. Its just not advertised anywhere. But there are still all those semi-mandatory patches flying around that should probably be upstreamed. Having the project in some public version control would be great.



---

archive/issue_comments_023403.json:
```json
{
    "body": "My notes about the url at\nhttps://trac.sagemath.org/ticket/25099#comment:13\nstill hold. Public version control of the original code\nand the existing extra patches would definitely help,\nas well as a home page for the project.",
    "created_at": "2018-07-14T03:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23403",
    "user": "slelievre"
}
```

My notes about the url at
https://trac.sagemath.org/ticket/25099#comment:13
still hold. Public version control of the original code
and the existing extra patches would definitely help,
as well as a home page for the project.



---

archive/issue_comments_023404.json:
```json
{
    "body": "I am on my way to fork sympow on gitlab. My concern will be only the unix part (read not the mathematical part) in view to harmonize related patches and integration in unix systems.\nNotes: My time being counted and limited, it would be question of weekends, rather of days.",
    "created_at": "2018-07-15T04:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23404",
    "user": "@jgmbenoit"
}
```

I am on my way to fork sympow on gitlab. My concern will be only the unix part (read not the mathematical part) in view to harmonize related patches and integration in unix systems.
Notes: My time being counted and limited, it would be question of weekends, rather of days.



---

archive/issue_comments_023405.json:
```json
{
    "body": "Great! Thank you for doing that.",
    "created_at": "2018-07-15T09:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23405",
    "user": "@timokau"
}
```

Great! Thank you for doing that.



---

archive/issue_comments_023406.json:
```json
{
    "body": "I have just rendered public my fork at [GitLab](GitLab): https://gitlab.com/rezozer/forks/sympow\nPlease test and report !",
    "created_at": "2018-07-21T06:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23406",
    "user": "@jgmbenoit"
}
```

I have just rendered public my fork at [GitLab](GitLab): https://gitlab.com/rezozer/forks/sympow
Please test and report !



---

archive/issue_comments_023407.json:
```json
{
    "body": "Updating from 1.018.1, this breaks the sage testsuite (looks like pretty much all the sympow interaction is broken):\n\n\n```\nsage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/lfunctions/sympow.py  # 13 doctests failed\nsage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/modular/abvar/abvar.py  # 1 doctest failed\nsage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/modular/hecke/submodule.py  # 1 doctest failed\nsage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/schemes/elliptic_curves/ell_rational_field.py  # 17 doctests failed\n```\n\n\nProbably just some minor change in output formatting that breaks the parser. Before I investigate further, this is presumably already fixed on Debian? Julian do you know the cause?",
    "created_at": "2018-07-23T13:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23407",
    "user": "@timokau"
}
```

Updating from 1.018.1, this breaks the sage testsuite (looks like pretty much all the sympow interaction is broken):


```
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/lfunctions/sympow.py  # 13 doctests failed
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/modular/abvar/abvar.py  # 1 doctest failed
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/modular/hecke/submodule.py  # 1 doctest failed
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/schemes/elliptic_curves/ell_rational_field.py  # 17 doctests failed
```


Probably just some minor change in output formatting that breaks the parser. Before I investigate further, this is presumably already fixed on Debian? Julian do you know the cause?



---

archive/issue_comments_023408.json:
```json
{
    "body": "`@`gh-jgmbenoit does the original author know about the fork? Has he said anything about it?",
    "created_at": "2018-07-23T13:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23408",
    "user": "@timokau"
}
```

`@`gh-jgmbenoit does the original author know about the fork? Has he said anything about it?



---

archive/issue_comments_023409.json:
```json
{
    "body": "`@`saraedum I am not surprised that it breaks the sage testsuite because the patched version runs more like any regular program. In fact it must break the sage related code itself: see the section [SYMPOW Data set](https://gitlab.com/rezozer/forks/sympow#sympow-data-setup) up for details.\nOtherwise, since it works on Debian, I guess it was fixed there. But I am not the one who did the fix.\nSo you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you.",
    "created_at": "2018-07-23T13:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23409",
    "user": "@jgmbenoit"
}
```

`@`saraedum I am not surprised that it breaks the sage testsuite because the patched version runs more like any regular program. In fact it must break the sage related code itself: see the section [SYMPOW Data set](https://gitlab.com/rezozer/forks/sympow#sympow-data-setup) up for details.
Otherwise, since it works on Debian, I guess it was fixed there. But I am not the one who did the fix.
So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you.



---

archive/issue_comments_023410.json:
```json
{
    "body": "Replying to [comment:21 gh-timokau]:\n> `@`gh-jgmbenoit does the original author know about the fork? Has he said anything about it?\n\nI sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back.",
    "created_at": "2018-07-23T13:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23410",
    "user": "@jgmbenoit"
}
```

Replying to [comment:21 gh-timokau]:
> `@`gh-jgmbenoit does the original author know about the fork? Has he said anything about it?

I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back.



---

archive/issue_comments_023411.json:
```json
{
    "body": "> So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you. \n\nThat's why I added saraedum (Julian R\u00fcdth). I was under the impression that he is the Debian maintainer. Is he not?\n\n> I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back. \n\nGreat. Please keep me posted (for example by posting here) in case you get feedback. It would be nice to be able to add that note to the update.",
    "created_at": "2018-07-23T14:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23411",
    "user": "@timokau"
}
```

> So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you. 

That's why I added saraedum (Julian Rüdth). I was under the impression that he is the Debian maintainer. Is he not?

> I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back. 

Great. Please keep me posted (for example by posting here) in case you get feedback. It would be nice to be able to add that note to the update.



---

archive/issue_comments_023412.json:
```json
{
    "body": "Replying to [comment:24 gh-timokau]:\n> > So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you. \n> \n> That's why I added saraedum (Julian R\u00fcdth). I was under the impression that he is the Debian maintainer. Is he not?\n> \n> > I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back. \n> \n> Great. Please keep me posted (for example by posting here) in case you get feedback. It would be nice to be able to add that note to the update.\n\nIt is a team work. To my knowledge, Julian is a new comer. Whatever, it was certainly fix a long time given that I wrote the Debian patches a long time ago, at least before that Stretch was frozen.\nConcerning Sage on Debian, the best is to send an email to the dedicated list:\n\ndebian-science-sagemath _at_ alioth-lists.debian.net",
    "created_at": "2018-07-23T14:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23412",
    "user": "@jgmbenoit"
}
```

Replying to [comment:24 gh-timokau]:
> > So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you. 
> 
> That's why I added saraedum (Julian Rüdth). I was under the impression that he is the Debian maintainer. Is he not?
> 
> > I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back. 
> 
> Great. Please keep me posted (for example by posting here) in case you get feedback. It would be nice to be able to add that note to the update.

It is a team work. To my knowledge, Julian is a new comer. Whatever, it was certainly fix a long time given that I wrote the Debian patches a long time ago, at least before that Stretch was frozen.
Concerning Sage on Debian, the best is to send an email to the dedicated list:

debian-science-sagemath _at_ alioth-lists.debian.net



---

archive/issue_comments_023413.json:
```json
{
    "body": "I cross-posted to that mailing list and sage-packaging: https://groups.google.com/forum/#!topic/sage-packaging/B3yTZ8eIbwM",
    "created_at": "2018-07-23T15:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23413",
    "user": "@timokau"
}
```

I cross-posted to that mailing list and sage-packaging: https://groups.google.com/forum/#!topic/sage-packaging/B3yTZ8eIbwM



---

archive/issue_comments_023414.json:
```json
{
    "body": "By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.",
    "created_at": "2018-07-23T15:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23414",
    "user": "@timokau"
}
```

By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.



---

archive/issue_comments_023415.json:
```json
{
    "body": "Replying to [comment:27 gh-timokau]:\n> By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.\n\nGitLab allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit",
    "created_at": "2018-07-23T16:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23415",
    "user": "@jgmbenoit"
}
```

Replying to [comment:27 gh-timokau]:
> By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.

GitLab allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit



---

archive/issue_comments_023416.json:
```json
{
    "body": "Replying to [comment:26 gh-timokau]:\n> I cross-posted to that mailing list and sage-packaging: https://groups.google.com/forum/#!topic/sage-packaging/B3yTZ8eIbwM\n\nThanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware.",
    "created_at": "2018-07-23T16:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23416",
    "user": "@jgmbenoit"
}
```

Replying to [comment:26 gh-timokau]:
> I cross-posted to that mailing list and sage-packaging: https://groups.google.com/forum/#!topic/sage-packaging/B3yTZ8eIbwM

Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware.



---

archive/issue_comments_023417.json:
```json
{
    "body": "Replying to [comment:28 gh-jgmbenoit]:\n> Replying to [comment:27 gh-timokau]:\n> > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.\n> \n> [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit\n\nCan that be nested further or is subgroup the limit?\n\n> Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. \n\nWere they? I haven't received a reply yet (besides that my post is awaiting approval).",
    "created_at": "2018-07-23T16:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23417",
    "user": "@timokau"
}
```

Replying to [comment:28 gh-jgmbenoit]:
> Replying to [comment:27 gh-timokau]:
> > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.
> 
> [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit

Can that be nested further or is subgroup the limit?

> Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. 

Were they? I haven't received a reply yet (besides that my post is awaiting approval).



---

archive/issue_comments_023418.json:
```json
{
    "body": "Replying to [comment:30 gh-timokau]:\n> Replying to [comment:28 gh-jgmbenoit]:\n> > Replying to [comment:27 gh-timokau]:\n> > > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.\n> > \n> > [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit\n> \n> Can that be nested further or is subgroup the limit?\n\nit can be nested further. I do not know the limit.\n\n> \n> > Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. \n> \n> Were they? \n\nat least, I am :-)\n\n I haven't received a reply yet (besides that my post is awaiting approval).\n\nBe patient, it is summer time.",
    "created_at": "2018-07-23T16:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23418",
    "user": "@jgmbenoit"
}
```

Replying to [comment:30 gh-timokau]:
> Replying to [comment:28 gh-jgmbenoit]:
> > Replying to [comment:27 gh-timokau]:
> > > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.
> > 
> > [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit
> 
> Can that be nested further or is subgroup the limit?

it can be nested further. I do not know the limit.

> 
> > Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. 
> 
> Were they? 

at least, I am :-)

 I haven't received a reply yet (besides that my post is awaiting approval).

Be patient, it is summer time.



---

archive/issue_comments_023419.json:
```json
{
    "body": "Replying to [comment:31 gh-jgmbenoit]:\n> Replying to [comment:30 gh-timokau]:\n> > Replying to [comment:28 gh-jgmbenoit]:\n> > > Replying to [comment:27 gh-timokau]:\n> > > > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.\n> > > \n> > > [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit\n> > \n> > Can that be nested further or is subgroup the limit?\n> \n> it can be nested further. I do not know the limit.\n\nAlright, thanks.\n\n\n> \n> > \n> > > Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. \n> > \n> > Were they? \n> \n> at least, I am :-)\n> \n>  I haven't received a reply yet (besides that my post is awaiting approval).\n> \n> Be patient, it is summer time.\n\nOf course :) I must've misunderstood your message, I thought you were referring to a reply to that email.",
    "created_at": "2018-07-23T16:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23419",
    "user": "@timokau"
}
```

Replying to [comment:31 gh-jgmbenoit]:
> Replying to [comment:30 gh-timokau]:
> > Replying to [comment:28 gh-jgmbenoit]:
> > > Replying to [comment:27 gh-timokau]:
> > > > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.
> > > 
> > > [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit
> > 
> > Can that be nested further or is subgroup the limit?
> 
> it can be nested further. I do not know the limit.

Alright, thanks.


> 
> > 
> > > Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. 
> > 
> > Were they? 
> 
> at least, I am :-)
> 
>  I haven't received a reply yet (besides that my post is awaiting approval).
> 
> Be patient, it is summer time.

Of course :) I must've misunderstood your message, I thought you were referring to a reply to that email.



---

archive/issue_comments_023420.json:
```json
{
    "body": "Okay turns out I just messed up packaging. Its not strictly relevant for this ticket and I thought about just emailing you, but maybe the sage package upgrade will run into the same problems.\n\nSo nix installs every package in its own prefix. That means sympow would go into `/nix/store/some-sympow-specific-folder-name/`. Only the sympow files would be in that folder.\n\nI'm currently achieving that by setting the install flag `DESTDIR=$out` ($out pointing to that sympow directory). However when launching an example from the README, it fails because it looks for the `new_data` script in `/usr/local/lib/sympow`. That script is in `$out/usr/local/lib/sympow`. Here's the error:\n\n\n```\n$ result/bin/sympow -sp 2p16 -curve \"[1,2,3,4,5]\"\nsympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details\n**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\nMinimal model of curve  is [1,-1,0,4,3]\nAt 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nAt 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nConductor is 10351\nP02L not found in param_data file\nWill compute data mesh file for `2'\nMake data for  symmetric power 2\n/bin/sh: /usr/local/lib/sympow/new_data: No such file or directory\n**ERROR** [FAILED]\nMay be tried with 'sympow -new_data `2'\n```\n\n\nIn the README I see that I can set the `SYMPOW_PKGLIBDIR` environment variable (although that shouldn't be necessary). After doing that, I get\n\n\n```\n$ result/bin/sympow -sp 2p16 -curve \"[1,2,3,4,5]\"\n**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\nRunning the new_data script for -sp 2\nMaking the datafiles for -sp 2\n\n**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\nRewarping param_data file /home/timo/.sympow/datafiles/param_data\nLeft with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data\n**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\nRemoving any old data files\nremoved '/home/timo/.sympow/datafiles/P02HM.txt'\nremoved '/home/timo/.sympow/datafiles/P02HS.txt'\nremoved '/home/timo/.sympow/datafiles/P02LM.txt'\nremoved '/home/timo/.sympow/datafiles/P02LS.txt'\nRunning the gp script\n\n**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n***   error opening input file: `/usr/local/share/sympow/standard1.gp'.\n***   error opening input file: `/usr/local/share/sympow/standard2.gp'.\n***   error opening input file: `/usr/local/share/sympow/standard3.gp'.\n***   at top-level: coeffs(0)\n***                 ^---------\n***   not a function in function call\n***   at top-level: coeffE(1)\n***                 ^---------\n***   not a function in function call\n***   error opening input file: `/usr/local/share/sympow/standard1.gp'.\n***   error opening input file: `/usr/local/share/sympow/standard2.gp'.\n***   error opening input file: `/usr/local/share/sympow/standard3.gp'.\n***   at top-level: coeffs(0)\n***                 ^---------\n***   not a function in function call\n***   at top-level: coeffO(1)\n***                 ^---------\n***   not a function in function call\n\n**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\nTrimming the data files\ntrimmed `/home/timo/.sympow/datafiles/P02HM.txt'\ntrimmed `/home/timo/.sympow/datafiles/P02HS.txt'\ntrimmed `/home/timo/.sympow/datafiles/P02LM.txt'\ntrimmed `/home/timo/.sympow/datafiles/P02LS.txt'\n**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\nRewarping param_data file /home/timo/.sympow/datafiles/param_data\nLeft with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data\nFinished with -sp 2\n**ERROR** P02L not found in param_data file in second round\nsympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details\nMinimal model of curve  is [1,-1,0,4,3]\nAt 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nAt 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nConductor is 10351\nP02L not found in param_data file\nWill compute data mesh file for `2'\nHas computed data mesh file for `2'\n```\n\n\nAm I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters. pari is included in the build dependencies.\n\nAlso in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package. Otherwilse I'll just take some from the README, but having them included in the package is better of course.",
    "created_at": "2018-07-27T14:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23420",
    "user": "@timokau"
}
```

Okay turns out I just messed up packaging. Its not strictly relevant for this ticket and I thought about just emailing you, but maybe the sage package upgrade will run into the same problems.

So nix installs every package in its own prefix. That means sympow would go into `/nix/store/some-sympow-specific-folder-name/`. Only the sympow files would be in that folder.

I'm currently achieving that by setting the install flag `DESTDIR=$out` ($out pointing to that sympow directory). However when launching an example from the README, it fails because it looks for the `new_data` script in `/usr/local/lib/sympow`. That script is in `$out/usr/local/lib/sympow`. Here's the error:


```
$ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Minimal model of curve  is [1,-1,0,4,3]
At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
Conductor is 10351
P02L not found in param_data file
Will compute data mesh file for `2'
Make data for  symmetric power 2
/bin/sh: /usr/local/lib/sympow/new_data: No such file or directory
**ERROR** [FAILED]
May be tried with 'sympow -new_data `2'
```


In the README I see that I can set the `SYMPOW_PKGLIBDIR` environment variable (although that shouldn't be necessary). After doing that, I get


```
$ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Running the new_data script for -sp 2
Making the datafiles for -sp 2

**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Rewarping param_data file /home/timo/.sympow/datafiles/param_data
Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Removing any old data files
removed '/home/timo/.sympow/datafiles/P02HM.txt'
removed '/home/timo/.sympow/datafiles/P02HS.txt'
removed '/home/timo/.sympow/datafiles/P02LM.txt'
removed '/home/timo/.sympow/datafiles/P02LS.txt'
Running the gp script

**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
***   at top-level: coeffs(0)
***                 ^---------
***   not a function in function call
***   at top-level: coeffE(1)
***                 ^---------
***   not a function in function call
***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
***   at top-level: coeffs(0)
***                 ^---------
***   not a function in function call
***   at top-level: coeffO(1)
***                 ^---------
***   not a function in function call

**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Trimming the data files
trimmed `/home/timo/.sympow/datafiles/P02HM.txt'
trimmed `/home/timo/.sympow/datafiles/P02HS.txt'
trimmed `/home/timo/.sympow/datafiles/P02LM.txt'
trimmed `/home/timo/.sympow/datafiles/P02LS.txt'
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Rewarping param_data file /home/timo/.sympow/datafiles/param_data
Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
Finished with -sp 2
**ERROR** P02L not found in param_data file in second round
sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
Minimal model of curve  is [1,-1,0,4,3]
At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
Conductor is 10351
P02L not found in param_data file
Will compute data mesh file for `2'
Has computed data mesh file for `2'
```


Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters. pari is included in the build dependencies.

Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package. Otherwilse I'll just take some from the README, but having them included in the package is better of course.



---

archive/issue_comments_023421.json:
```json
{
    "body": "Replying to [comment:33 gh-timokau]:\n> Okay turns out I just messed up packaging. Its not strictly relevant for this ticket\n\nI guess it would be a relevant ticket for the fork.\n\n and I thought about just emailing you, but maybe the sage package upgrade will run into the same problems.\n> \n> So nix installs every package in its own prefix. That means sympow would go into `/nix/store/some-sympow-specific-folder-name/`. Only the sympow files would be in that folder.\n> \n> I'm currently achieving that by setting the install flag `DESTDIR=$out` ($out pointing to that sympow directory). However when launching an example from the README, it fails because it looks for the `new_data` script in `/usr/local/lib/sympow`. That script is in `$out/usr/local/lib/sympow`. Here's the error:\n> \n> {{{\n> $ result/bin/sympow -sp 2p16 -curve \"[1,2,3,4,5]\"\n> sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details\n> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n> Minimal model of curve  is [1,-1,0,4,3]\n> At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\n> At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\n> Conductor is 10351\n> P02L not found in param_data file\n> Will compute data mesh file for `2'\n> Make data for  symmetric power 2\n> /bin/sh: /usr/local/lib/sympow/new_data: No such file or directory\n> **ERROR** [FAILED]\n> May be tried with 'sympow -new_data `2'\n> }}}\n> \n> In the README I see that I can set the `SYMPOW_PKGLIBDIR` environment variable (although that shouldn't be necessary\n\nit is why it is written that they are meant mainly for development and debugging purpose\n\nHere you are misusing PREFIX, VARPREFIX, and DESTDIR (see below)\n\n). After doing that, I get\n> \n> {{{\n> $ result/bin/sympow -sp 2p16 -curve \"[1,2,3,4,5]\"\n> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n> Running the new_data script for -sp 2\n> Making the datafiles for -sp 2\n> \n> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n> Rewarping param_data file /home/timo/.sympow/datafiles/param_data\n> Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data\n> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n> Removing any old data files\n> removed '/home/timo/.sympow/datafiles/P02HM.txt'\n> removed '/home/timo/.sympow/datafiles/P02HS.txt'\n> removed '/home/timo/.sympow/datafiles/P02LM.txt'\n> removed '/home/timo/.sympow/datafiles/P02LS.txt'\n> Running the gp script\n> \n> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n> ***   error opening input file: `/usr/local/share/sympow/standard1.gp'.\n> ***   error opening input file: `/usr/local/share/sympow/standard2.gp'.\n> ***   error opening input file: `/usr/local/share/sympow/standard3.gp'.\n> ***   at top-level: coeffs(0)\n> ***                 ^---------\n> ***   not a function in function call\n> ***   at top-level: coeffE(1)\n> ***                 ^---------\n> ***   not a function in function call\n> ***   error opening input file: `/usr/local/share/sympow/standard1.gp'.\n> ***   error opening input file: `/usr/local/share/sympow/standard2.gp'.\n> ***   error opening input file: `/usr/local/share/sympow/standard3.gp'.\n> ***   at top-level: coeffs(0)\n> ***                 ^---------\n> ***   not a function in function call\n> ***   at top-level: coeffO(1)\n> ***                 ^---------\n> ***   not a function in function call\n> \n> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n> Trimming the data files\n> trimmed `/home/timo/.sympow/datafiles/P02HM.txt'\n> trimmed `/home/timo/.sympow/datafiles/P02HS.txt'\n> trimmed `/home/timo/.sympow/datafiles/P02LM.txt'\n> trimmed `/home/timo/.sympow/datafiles/P02LS.txt'\n> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64\n> Rewarping param_data file /home/timo/.sympow/datafiles/param_data\n> Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data\n> Finished with -sp 2\n> **ERROR** P02L not found in param_data file in second round\n> sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details\n> Minimal model of curve  is [1,-1,0,4,3]\n> At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\n> At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\n> Conductor is 10351\n> P02L not found in param_data file\n> Will compute data mesh file for `2'\n> Has computed data mesh file for `2'\n> }}}\n> \n> Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.\n\nDESTDIR is mainly meant for packaging in custom Makefile (not for testing)\n\nTo do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.\n\nThe patches I brought from Debian are meant to ease integration in Unix for maintainers and users (compare to the original version): DESTDIR, PREFIX, and VARPREFIX have the customary meaning.\n\nBasically you cannot test in DESTDIR unless you set correctly the environment variables because\nPREFIXed  paths are hard coded.\n\n pari is included in the build dependencies.\n> \n> Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.\n\nThe test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.\n\n\n> Otherwilse I'll just take some from the README, but having them included in the package is better of course.",
    "created_at": "2018-07-27T18:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23421",
    "user": "@jgmbenoit"
}
```

Replying to [comment:33 gh-timokau]:
> Okay turns out I just messed up packaging. Its not strictly relevant for this ticket

I guess it would be a relevant ticket for the fork.

 and I thought about just emailing you, but maybe the sage package upgrade will run into the same problems.
> 
> So nix installs every package in its own prefix. That means sympow would go into `/nix/store/some-sympow-specific-folder-name/`. Only the sympow files would be in that folder.
> 
> I'm currently achieving that by setting the install flag `DESTDIR=$out` ($out pointing to that sympow directory). However when launching an example from the README, it fails because it looks for the `new_data` script in `/usr/local/lib/sympow`. That script is in `$out/usr/local/lib/sympow`. Here's the error:
> 
> {{{
> $ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
> sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Minimal model of curve  is [1,-1,0,4,3]
> At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> Conductor is 10351
> P02L not found in param_data file
> Will compute data mesh file for `2'
> Make data for  symmetric power 2
> /bin/sh: /usr/local/lib/sympow/new_data: No such file or directory
> **ERROR** [FAILED]
> May be tried with 'sympow -new_data `2'
> }}}
> 
> In the README I see that I can set the `SYMPOW_PKGLIBDIR` environment variable (although that shouldn't be necessary

it is why it is written that they are meant mainly for development and debugging purpose

Here you are misusing PREFIX, VARPREFIX, and DESTDIR (see below)

). After doing that, I get
> 
> {{{
> $ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Running the new_data script for -sp 2
> Making the datafiles for -sp 2
> 
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Rewarping param_data file /home/timo/.sympow/datafiles/param_data
> Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Removing any old data files
> removed '/home/timo/.sympow/datafiles/P02HM.txt'
> removed '/home/timo/.sympow/datafiles/P02HS.txt'
> removed '/home/timo/.sympow/datafiles/P02LM.txt'
> removed '/home/timo/.sympow/datafiles/P02LS.txt'
> Running the gp script
> 
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> ***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
> ***   at top-level: coeffs(0)
> ***                 ^---------
> ***   not a function in function call
> ***   at top-level: coeffE(1)
> ***                 ^---------
> ***   not a function in function call
> ***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
> ***   at top-level: coeffs(0)
> ***                 ^---------
> ***   not a function in function call
> ***   at top-level: coeffO(1)
> ***                 ^---------
> ***   not a function in function call
> 
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Trimming the data files
> trimmed `/home/timo/.sympow/datafiles/P02HM.txt'
> trimmed `/home/timo/.sympow/datafiles/P02HS.txt'
> trimmed `/home/timo/.sympow/datafiles/P02LM.txt'
> trimmed `/home/timo/.sympow/datafiles/P02LS.txt'
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Rewarping param_data file /home/timo/.sympow/datafiles/param_data
> Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
> Finished with -sp 2
> **ERROR** P02L not found in param_data file in second round
> sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
> Minimal model of curve  is [1,-1,0,4,3]
> At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> Conductor is 10351
> P02L not found in param_data file
> Will compute data mesh file for `2'
> Has computed data mesh file for `2'
> }}}
> 
> Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.

DESTDIR is mainly meant for packaging in custom Makefile (not for testing)

To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.

The patches I brought from Debian are meant to ease integration in Unix for maintainers and users (compare to the original version): DESTDIR, PREFIX, and VARPREFIX have the customary meaning.

Basically you cannot test in DESTDIR unless you set correctly the environment variables because
PREFIXed  paths are hard coded.

 pari is included in the build dependencies.
> 
> Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.

The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.


> Otherwilse I'll just take some from the README, but having them included in the package is better of course.



---

archive/issue_comments_023422.json:
```json
{
    "body": "Replying to [comment:34 gh-jgmbenoit]:\n> Replying to [comment:33 gh-timokau]:\n> > ...\n> > Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.\n> \n> DESTDIR is mainly meant for packaging in custom Makefile (not for testing)\n> \n> To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.\n\nRight, `DESTDIR` was a leftover from the old way to package sympow. Using `PREFIX` instead fixes the issue.\n\nThank you.\n\n> > Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.\n> \n> The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.\n\nYes, install checks is exactly what I'd want. To catch issues like this early. I assumed the sage interface was at fault, even though it was just faulty packaging. So after installation (which at least for nix is the same as packaging; the installation result can just be put in an archive and distributed), something like autotools `make installcheck` would be what I want.\n\n\nWhat is the difference between `/var/cache/sympow` and `~/.sympow`? When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about \"precomputed\" for `/var` and \"user computed\" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?",
    "created_at": "2018-07-28T12:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23422",
    "user": "@timokau"
}
```

Replying to [comment:34 gh-jgmbenoit]:
> Replying to [comment:33 gh-timokau]:
> > ...
> > Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.
> 
> DESTDIR is mainly meant for packaging in custom Makefile (not for testing)
> 
> To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.

Right, `DESTDIR` was a leftover from the old way to package sympow. Using `PREFIX` instead fixes the issue.

Thank you.

> > Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.
> 
> The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.

Yes, install checks is exactly what I'd want. To catch issues like this early. I assumed the sage interface was at fault, even though it was just faulty packaging. So after installation (which at least for nix is the same as packaging; the installation result can just be put in an archive and distributed), something like autotools `make installcheck` would be what I want.


What is the difference between `/var/cache/sympow` and `~/.sympow`? When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?



---

archive/issue_comments_023423.json:
```json
{
    "body": "Replying to [comment:35 gh-timokau]:\n> Replying to [comment:34 gh-jgmbenoit]:\n> > Replying to [comment:33 gh-timokau]:\n> > > ...\n> > > Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.\n> > \n> > DESTDIR is mainly meant for packaging in custom Makefile (not for testing)\n> > \n> > To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.\n> \n> Right, `DESTDIR` was a leftover from the old way to package sympow. Using `PREFIX` instead fixes the issue.\n> \n> Thank you.\n> \n> > > Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.\n> > \n> > The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.\n> \n> Yes, install checks is exactly what I'd want. To catch issues like this early. I assumed the sage interface was at fault, even though it was just faulty packaging. So after installation (which at least for nix is the same as packaging; the installation result can just be put in an archive and distributed), something like autotools `make installcheck` would be what I want.\n> \n> \n> What is the difference between `/var/cache/sympow` and `~/.sympow`?\n\n/var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :\n1] /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);\n2] /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.\n\n\n~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER when the clear version whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .\nBehind this, there is a community policy: we can reuse data computed by other users.\n\nThe data in HOME/.sympow are autoritative over the one system-wide ones,\nand The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative\nover the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.\n\nMy aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).\n\nIf you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.\n\nHaving said that, it is okay to distributed no precomputed data.\n\nMy point is that some examples or tests in the literature may depend on the historical data,\nso having them can speed up tests and keep the end users cool.\nI strongly suggest to distribute the historical precomputed data (and the Sage ones).\n\n\n\n\n\n When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about \"precomputed\" for `/var` and \"user computed\" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?\n\nJust cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.\n\nJerome",
    "created_at": "2018-07-28T17:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23423",
    "user": "@jgmbenoit"
}
```

Replying to [comment:35 gh-timokau]:
> Replying to [comment:34 gh-jgmbenoit]:
> > Replying to [comment:33 gh-timokau]:
> > > ...
> > > Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.
> > 
> > DESTDIR is mainly meant for packaging in custom Makefile (not for testing)
> > 
> > To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.
> 
> Right, `DESTDIR` was a leftover from the old way to package sympow. Using `PREFIX` instead fixes the issue.
> 
> Thank you.
> 
> > > Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.
> > 
> > The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.
> 
> Yes, install checks is exactly what I'd want. To catch issues like this early. I assumed the sage interface was at fault, even though it was just faulty packaging. So after installation (which at least for nix is the same as packaging; the installation result can just be put in an archive and distributed), something like autotools `make installcheck` would be what I want.
> 
> 
> What is the difference between `/var/cache/sympow` and `~/.sympow`?

/var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
1] /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
2] /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.


~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER when the clear version whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
Behind this, there is a community policy: we can reuse data computed by other users.

The data in HOME/.sympow are autoritative over the one system-wide ones,
and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.

My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).

If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.

Having said that, it is okay to distributed no precomputed data.

My point is that some examples or tests in the literature may depend on the historical data,
so having them can speed up tests and keep the end users cool.
I strongly suggest to distribute the historical precomputed data (and the Sage ones).





 When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?

Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.

Jerome



---

archive/issue_comments_023424.json:
```json
{
    "body": "Replying to [comment:36 gh-jgmbenoit]:\n> Replying to [comment:35 gh-timokau]:\n> > What is the difference between `/var/cache/sympow` and `~/.sympow`?\n> \n> /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :\n>\n> * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);\n>\n> * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.\n\nDependant on the exact CPU model or just x86/aarch, 32/64 bits?\n\n\n> ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .\n> Behind this, there is a community policy: we can reuse data computed by other users.\n> \n> The data in HOME/.sympow are autoritative over the one system-wide ones,\n> and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative\n> over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.\n> \n> My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).\n> \n> If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.\n\nIf I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?\n\n\n> Having said that, it is okay to distributed no precomputed data.\n\nI'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.\n\n\n> I strongly suggest to distribute the historical precomputed data (and the Sage ones).\n\nSo basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`? It looks like the debian package still calls gp manually. So that'd be\n\n\n```\nfor data in 1d0 2 2d0h 3d0 3d1 4; do\n\tsympow -new_data \"$data\"\ndone\n```\n\n\nBut that tries to access HOME/.sympow. So you're generating user-level cache files at install time?\n\n>  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about \"precomputed\" for `/var` and \"user computed\" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?\n> \n> Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.\n\nEven after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.",
    "created_at": "2018-07-29T13:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23424",
    "user": "@timokau"
}
```

Replying to [comment:36 gh-jgmbenoit]:
> Replying to [comment:35 gh-timokau]:
> > What is the difference between `/var/cache/sympow` and `~/.sympow`?
> 
> /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
>
> * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
>
> * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.

Dependant on the exact CPU model or just x86/aarch, 32/64 bits?


> ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
> Behind this, there is a community policy: we can reuse data computed by other users.
> 
> The data in HOME/.sympow are autoritative over the one system-wide ones,
> and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
> over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.
> 
> My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).
> 
> If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.

If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?


> Having said that, it is okay to distributed no precomputed data.

I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.


> I strongly suggest to distribute the historical precomputed data (and the Sage ones).

So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`? It looks like the debian package still calls gp manually. So that'd be


```
for data in 1d0 2 2d0h 3d0 3d1 4; do
	sympow -new_data "$data"
done
```


But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?

>  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?
> 
> Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.

Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.



---

archive/issue_comments_023425.json:
```json
{
    "body": "Replying to [comment:37 gh-timokau]:\n> Replying to [comment:36 gh-jgmbenoit]:\n> > Replying to [comment:35 gh-timokau]:\n> > > What is the difference between `/var/cache/sympow` and `~/.sympow`?\n> > \n> > /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :\n> >\n> > * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);\n> >\n> > * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.\n> \n> Dependant on the exact CPU model or just x86/aarch, 32/64 bits?\n\nendianness\n\n\n\n> \n> \n> > ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .\n> > Behind this, there is a community policy: we can reuse data computed by other users.\n> > \n> > The data in HOME/.sympow are autoritative over the one system-wide ones,\n> > and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative\n> > over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.\n> > \n> > My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).\n> > \n> > If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.\n> \n> If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?\n\nyes but just to write the binary data, which the binary version of the clean data:\n1] so whoever write it, the output must be the same ;\n2] any USER can bypass them by writting their own clean file in HOME/.sympow \n3] any USER can remove them;\n4] if faulty binary are set, we can trace back the faulty USER ;\n5] the superuser can create a specific group.\n\n\n\n> \n> \n> > Having said that, it is okay to distributed no precomputed data.\n> \n> I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.\n> \nHe does not: he will get a warning message, but sympow will continue.\nThe USER can pass the -quiet option to silence the warnings.\nNo warning will not be ideal: the user must be aware if the set up is not correct.\n\n> \n> > I strongly suggest to distribute the historical precomputed data (and the Sage ones).\n> \n> So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`?\n\nThere is no such file but a script in debian/adhoc/job which is called at packaging time \nand which complete the original armd.sh . I could merge them, but I will not because it will touch\nthe math part (what I want to avoid).\n\n\n It looks like the debian package still calls gp manually. So that'd be\n> \n> {{{\n> for data in 1d0 2 2d0h 3d0 3d1 4; do\n> \tsympow -new_data \"$data\"\n> done\n> }}}\n\nBut it is not.\n\n\nA debian centric patch is applies to add the extra data: debain/patches/debianization.patch \nAt packaging time, besides the original script armd.sh , the script debian/adhoc/job/sympow-new_data.job  is launched : those scripts call gp (and not sympow).\n\n> \n> But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?\n\nsee above\n\n\n\n> \n> >  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about \"precomputed\" for `/var` and \"user computed\" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?\n> > \n> > Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.\n> \n> Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.\n\nso it is a warning (an not an ERROR message followed but an exit(-1)): I would consider it as a feature but not as a bug.\nIn fact, a couple of checks are performed to detect a corrupted folder set up and avoid surprises . \n\n\nThe bug is in the installation process:\nthe correct privileges must be encoded in Configure : I will try to fix this the next week-end .\nAnd in the README.md file: I should document better this part.\n\nFor now, to silent this warning, just set the right privilege or pass the option  -quiet : no will be write if /usr/share/sympow/datafiles is empty .\n\nLet me know if you think that a mechanism must be implemented to avoid this warning message.\n\nJerome",
    "created_at": "2018-07-29T15:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23425",
    "user": "@jgmbenoit"
}
```

Replying to [comment:37 gh-timokau]:
> Replying to [comment:36 gh-jgmbenoit]:
> > Replying to [comment:35 gh-timokau]:
> > > What is the difference between `/var/cache/sympow` and `~/.sympow`?
> > 
> > /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
> >
> > * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
> >
> > * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.
> 
> Dependant on the exact CPU model or just x86/aarch, 32/64 bits?

endianness



> 
> 
> > ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
> > Behind this, there is a community policy: we can reuse data computed by other users.
> > 
> > The data in HOME/.sympow are autoritative over the one system-wide ones,
> > and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
> > over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.
> > 
> > My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).
> > 
> > If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.
> 
> If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?

yes but just to write the binary data, which the binary version of the clean data:
1] so whoever write it, the output must be the same ;
2] any USER can bypass them by writting their own clean file in HOME/.sympow 
3] any USER can remove them;
4] if faulty binary are set, we can trace back the faulty USER ;
5] the superuser can create a specific group.



> 
> 
> > Having said that, it is okay to distributed no precomputed data.
> 
> I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.
> 
He does not: he will get a warning message, but sympow will continue.
The USER can pass the -quiet option to silence the warnings.
No warning will not be ideal: the user must be aware if the set up is not correct.

> 
> > I strongly suggest to distribute the historical precomputed data (and the Sage ones).
> 
> So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`?

There is no such file but a script in debian/adhoc/job which is called at packaging time 
and which complete the original armd.sh . I could merge them, but I will not because it will touch
the math part (what I want to avoid).


 It looks like the debian package still calls gp manually. So that'd be
> 
> {{{
> for data in 1d0 2 2d0h 3d0 3d1 4; do
> 	sympow -new_data "$data"
> done
> }}}

But it is not.


A debian centric patch is applies to add the extra data: debain/patches/debianization.patch 
At packaging time, besides the original script armd.sh , the script debian/adhoc/job/sympow-new_data.job  is launched : those scripts call gp (and not sympow).

> 
> But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?

see above



> 
> >  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?
> > 
> > Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.
> 
> Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.

so it is a warning (an not an ERROR message followed but an exit(-1)): I would consider it as a feature but not as a bug.
In fact, a couple of checks are performed to detect a corrupted folder set up and avoid surprises . 


The bug is in the installation process:
the correct privileges must be encoded in Configure : I will try to fix this the next week-end .
And in the README.md file: I should document better this part.

For now, to silent this warning, just set the right privilege or pass the option  -quiet : no will be write if /usr/share/sympow/datafiles is empty .

Let me know if you think that a mechanism must be implemented to avoid this warning message.

Jerome



---

archive/issue_comments_023426.json:
```json
{
    "body": "> But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?\n\nThis is the behaviour of the original source, hence the patch.",
    "created_at": "2018-07-29T15:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23426",
    "user": "@jgmbenoit"
}
```

> But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?

This is the behaviour of the original source, hence the patch.



---

archive/issue_comments_023427.json:
```json
{
    "body": "Replying to [comment:38 gh-jgmbenoit]:\n> Replying to [comment:37 gh-timokau]:\n> > Replying to [comment:36 gh-jgmbenoit]:\n> > > Replying to [comment:35 gh-timokau]:\n> > > > What is the difference between `/var/cache/sympow` and `~/.sympow`?\n> > > \n> > > /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :\n> > >\n> > > * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);\n> > >\n> > > * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.\n> > \n> > Dependant on the exact CPU model or just x86/aarch, 32/64 bits?\n> \n> endianness\n\nSo would it be reasonable to pre-compute and distribute all the /var/cache data?\n\n> > > ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .\n> > > Behind this, there is a community policy: we can reuse data computed by other users.\n> > > \n> > > The data in HOME/.sympow are autoritative over the one system-wide ones,\n> > > and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative\n> > > over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.\n> > > \n> > > My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).\n> > > \n> > > If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.\n> > \n> > If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?\n> \n> yes but just to write the binary data, which the binary version of the clean data:\n> 1] so whoever write it, the output must be the same ;\n> 2] any USER can bypass them by writting their own clean file in HOME/.sympow \n> 3] any USER can remove them;\n> 4] if faulty binary are set, we can trace back the faulty USER ;\n> 5] the superuser can create a specific group.\n> \n> > \n> > \n> > > Having said that, it is okay to distributed no precomputed data.\n> > \n> > I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.\n> > \n> He does not: he will get a warning message, but sympow will continue.\n> The USER can pass the -quiet option to silence the warnings.\n> No warning will not be ideal: the user must be aware if the set up is not correct.\n\nAnd then sympow will fall back to `~/.sympow` and behave exactly as usual?\n\n> > > I strongly suggest to distribute the historical precomputed data (and the Sage ones).\n> > \n> > So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`?\n> \n> There is no such file but a script in debian/adhoc/job which is called at packaging time \n> and which complete the original armd.sh . I could merge them, but I will not because it will touch\n> the math part (what I want to avoid).\n> \n> \n>  It looks like the debian package still calls gp manually. So that'd be\n> > \n> > {{{\n> > for data in 1d0 2 2d0h 3d0 3d1 4; do\n> > \tsympow -new_data \"$data\"\n> > done\n> > }}}\n> \n> But it is not.\n> \n> \n> A debian centric patch is applies to add the extra data: debain/patches/debianization.patch \n> At packaging time, besides the original script armd.sh , the script debian/adhoc/job/sympow-new_data.job  is launched : those scripts call gp (and not sympow).\n\nSo what does the debian version do differntly?\n\n> > But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?\n> \n> see above\n\nDoes that mean I should use the debian scripts if I want to distribute the cached binaries?\n\n> > >  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about \"precomputed\" for `/var` and \"user computed\" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?\n> > > \n> > > Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.\n> > \n> > Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.\n> \n> so it is a warning (an not an ERROR message followed but an exit(-1)): I would consider it as a feature but not as a bug.\n> In fact, a couple of checks are performed to detect a corrupted folder set up and avoid surprises . \n\nI would disagree. If I understand correctly the shared cache is only really useful in the nowadays nieche case where a lot of users use the same sympow instance on one PC. And even then it will not have a huge impact because computing power is usually sufficient. Not having the shared state makes things easier to reason about and in general global state is annoying to deal with for packaging.\n\n> The bug is in the installation process:\n> the correct privileges must be encoded in Configure : I will try to fix this the next week-end .\n\nWhat do you mean by that?\n\n> And in the README.md file: I should document better this part.\n> \n> For now, to silent this warning, just set the right privilege or pass the option  -quiet : no will be write if /usr/share/sympow/datafiles is empty .\n\nDoes `-quiet` have any other effects besides surpressing that message?\n\n> Let me know if you think that a mechanism must be implemented to avoid this warning message.\n\nTo make my motivations mroe clear: In nix, every package lives in an immutable subfolder of /nix/store after installation. The name of that subfolder contains a hash describing the recipe used to build the package and all its dependencies. That has a lot of advantages. Two relevant examples:\n\n- packages can be installed with user privileges. That is because installing a package only downlaods a couple of archives and unpacks that at /nix/store. It does not in any way affect other users. The issue with /var here is that we'd need superuser privileges at install time. Also nix doesn't even have the concept of install time scripts, so I'd have to do some ugly hack like creating a wrapper for sympow that sets up the /var folder on first use.\n\n- multiple versions of a package can be installed side-by-side. For example different users may have different versions of sympow. Again, global state is difficult in this situation.\n\nSo if it is not strictly necessary, I'd like to either\n\n- avoid the global cache and use the user cache instead or\n\n- pre-populate the cache at build time. The cache dir would then be read-only at runtime.\n\nIt sounds like currently I can kind of do the first option by writing a wrapper for sympow that always passes the `-quiet` option. Of course it would be nicer to just disable the shared state through a ./Configure option and even nicer to use option two instead.\n\nAm I misunderstanding this?\n\nThank you again for not only taking the time to improve the state of the singular package, but also patiently explaining the details to me :)",
    "created_at": "2018-07-29T17:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23427",
    "user": "@timokau"
}
```

Replying to [comment:38 gh-jgmbenoit]:
> Replying to [comment:37 gh-timokau]:
> > Replying to [comment:36 gh-jgmbenoit]:
> > > Replying to [comment:35 gh-timokau]:
> > > > What is the difference between `/var/cache/sympow` and `~/.sympow`?
> > > 
> > > /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
> > >
> > > * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
> > >
> > > * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.
> > 
> > Dependant on the exact CPU model or just x86/aarch, 32/64 bits?
> 
> endianness

So would it be reasonable to pre-compute and distribute all the /var/cache data?

> > > ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
> > > Behind this, there is a community policy: we can reuse data computed by other users.
> > > 
> > > The data in HOME/.sympow are autoritative over the one system-wide ones,
> > > and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
> > > over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.
> > > 
> > > My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).
> > > 
> > > If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.
> > 
> > If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?
> 
> yes but just to write the binary data, which the binary version of the clean data:
> 1] so whoever write it, the output must be the same ;
> 2] any USER can bypass them by writting their own clean file in HOME/.sympow 
> 3] any USER can remove them;
> 4] if faulty binary are set, we can trace back the faulty USER ;
> 5] the superuser can create a specific group.
> 
> > 
> > 
> > > Having said that, it is okay to distributed no precomputed data.
> > 
> > I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.
> > 
> He does not: he will get a warning message, but sympow will continue.
> The USER can pass the -quiet option to silence the warnings.
> No warning will not be ideal: the user must be aware if the set up is not correct.

And then sympow will fall back to `~/.sympow` and behave exactly as usual?

> > > I strongly suggest to distribute the historical precomputed data (and the Sage ones).
> > 
> > So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`?
> 
> There is no such file but a script in debian/adhoc/job which is called at packaging time 
> and which complete the original armd.sh . I could merge them, but I will not because it will touch
> the math part (what I want to avoid).
> 
> 
>  It looks like the debian package still calls gp manually. So that'd be
> > 
> > {{{
> > for data in 1d0 2 2d0h 3d0 3d1 4; do
> > 	sympow -new_data "$data"
> > done
> > }}}
> 
> But it is not.
> 
> 
> A debian centric patch is applies to add the extra data: debain/patches/debianization.patch 
> At packaging time, besides the original script armd.sh , the script debian/adhoc/job/sympow-new_data.job  is launched : those scripts call gp (and not sympow).

So what does the debian version do differntly?

> > But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?
> 
> see above

Does that mean I should use the debian scripts if I want to distribute the cached binaries?

> > >  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?
> > > 
> > > Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.
> > 
> > Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.
> 
> so it is a warning (an not an ERROR message followed but an exit(-1)): I would consider it as a feature but not as a bug.
> In fact, a couple of checks are performed to detect a corrupted folder set up and avoid surprises . 

I would disagree. If I understand correctly the shared cache is only really useful in the nowadays nieche case where a lot of users use the same sympow instance on one PC. And even then it will not have a huge impact because computing power is usually sufficient. Not having the shared state makes things easier to reason about and in general global state is annoying to deal with for packaging.

> The bug is in the installation process:
> the correct privileges must be encoded in Configure : I will try to fix this the next week-end .

What do you mean by that?

> And in the README.md file: I should document better this part.
> 
> For now, to silent this warning, just set the right privilege or pass the option  -quiet : no will be write if /usr/share/sympow/datafiles is empty .

Does `-quiet` have any other effects besides surpressing that message?

> Let me know if you think that a mechanism must be implemented to avoid this warning message.

To make my motivations mroe clear: In nix, every package lives in an immutable subfolder of /nix/store after installation. The name of that subfolder contains a hash describing the recipe used to build the package and all its dependencies. That has a lot of advantages. Two relevant examples:

- packages can be installed with user privileges. That is because installing a package only downlaods a couple of archives and unpacks that at /nix/store. It does not in any way affect other users. The issue with /var here is that we'd need superuser privileges at install time. Also nix doesn't even have the concept of install time scripts, so I'd have to do some ugly hack like creating a wrapper for sympow that sets up the /var folder on first use.

- multiple versions of a package can be installed side-by-side. For example different users may have different versions of sympow. Again, global state is difficult in this situation.

So if it is not strictly necessary, I'd like to either

- avoid the global cache and use the user cache instead or

- pre-populate the cache at build time. The cache dir would then be read-only at runtime.

It sounds like currently I can kind of do the first option by writing a wrapper for sympow that always passes the `-quiet` option. Of course it would be nicer to just disable the shared state through a ./Configure option and even nicer to use option two instead.

Am I misunderstanding this?

Thank you again for not only taking the time to improve the state of the singular package, but also patiently explaining the details to me :)



---

archive/issue_comments_023428.json:
```json
{
    "body": "update milestone 8.3 -> 8.4",
    "created_at": "2018-08-03T19:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23428",
    "user": "vdelecroix"
}
```

update milestone 8.3 -> 8.4



---

archive/issue_comments_023429.json:
```json
{
    "body": "`@`gh-jgmbenoit ping",
    "created_at": "2018-08-26T20:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23429",
    "user": "@timokau"
}
```

`@`gh-jgmbenoit ping



---

archive/issue_comments_023430.json:
```json
{
    "body": "pong !\n\nDoes -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.\n\nYou only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.\n\n((Is it that hard to read C source file ?))",
    "created_at": "2018-08-27T03:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23430",
    "user": "@jgmbenoit"
}
```

pong !

Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.

You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.

((Is it that hard to read C source file ?))



---

archive/issue_comments_023431.json:
```json
{
    "body": "Replying to [comment:43 gh-jgmbenoit]:\n> Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.\n> \n> You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.\n\nThat is the only blocking issue, but it would still be better to be able to pre-compute the global cache at build time instead of lazily computing it at runtime. You didn't respond to all of my questions, which is understandable considering what a monster of message that was. So I'll summarize:\n\n- could the global cache reasonably be pre-computed at build time?\n- does sympow without a global cache behave exatly as usual, just computing the cache per-user instead?\n- if the debian/adhoc/job file to pre-compute some data is recommended, I would prefer if you would include it in sympow proper. However I understand your reservations about touching the math.\n\n> ((Is it that hard to read C source file ?))\n\nHonestly yes, the sympow code is very hard to read for me. Its a mix of very non-standard formatting, a lack of comments and my limited C and domain knowledge. That is why I'm glad that you have taken up the maintenance.\n\nI'll try a `-quiet` wrapper for now.",
    "created_at": "2018-08-27T10:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23431",
    "user": "@timokau"
}
```

Replying to [comment:43 gh-jgmbenoit]:
> Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.
> 
> You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.

That is the only blocking issue, but it would still be better to be able to pre-compute the global cache at build time instead of lazily computing it at runtime. You didn't respond to all of my questions, which is understandable considering what a monster of message that was. So I'll summarize:

- could the global cache reasonably be pre-computed at build time?
- does sympow without a global cache behave exatly as usual, just computing the cache per-user instead?
- if the debian/adhoc/job file to pre-compute some data is recommended, I would prefer if you would include it in sympow proper. However I understand your reservations about touching the math.

> ((Is it that hard to read C source file ?))

Honestly yes, the sympow code is very hard to read for me. Its a mix of very non-standard formatting, a lack of comments and my limited C and domain knowledge. That is why I'm glad that you have taken up the maintenance.

I'll try a `-quiet` wrapper for now.



---

archive/issue_comments_023432.json:
```json
{
    "body": "Replying to [comment:44 gh-timokau]:\n> Replying to [comment:43 gh-jgmbenoit]:\n> > Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.\n> > \n> > You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.\n> \n> That is the only blocking issue, but it would still be better to be able to pre-compute the global cache at build time instead of lazily computing it at runtime. You didn't respond to all of my questions, which is understandable considering what a monster of message that was. So I'll summarize:\n> \n> - could the global cache reasonably be pre-computed at build time?\n\nNo for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.\n\n> - does sympow without a global cache behave exatly as usual, just computing the cache per-user instead?\n\nYes. \n\n> - if the debian/adhoc/job file to pre-compute some data is recommended, I would prefer if you would include it in sympow proper. However I understand your reservations about touching the math.\n\nI plan to incorporated them latter: the issue is now time.\n\n> \n> > ((Is it that hard to read C source file ?))\n> \n> Honestly yes, the sympow code is very hard to read for me. Its a mix of very non-standard formatting, a lack of comments and my limited C and domain knowledge. That is why I'm glad that you have taken up the maintenance.\n> \n> I'll try a `-quiet` wrapper for now.\n\nI would forget it and spend my time else where.\n\nI plan to change the verbosity level of this message (once I have time before me).\n\nJerome",
    "created_at": "2018-08-27T11:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23432",
    "user": "@jgmbenoit"
}
```

Replying to [comment:44 gh-timokau]:
> Replying to [comment:43 gh-jgmbenoit]:
> > Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.
> > 
> > You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.
> 
> That is the only blocking issue, but it would still be better to be able to pre-compute the global cache at build time instead of lazily computing it at runtime. You didn't respond to all of my questions, which is understandable considering what a monster of message that was. So I'll summarize:
> 
> - could the global cache reasonably be pre-computed at build time?

No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.

> - does sympow without a global cache behave exatly as usual, just computing the cache per-user instead?

Yes. 

> - if the debian/adhoc/job file to pre-compute some data is recommended, I would prefer if you would include it in sympow proper. However I understand your reservations about touching the math.

I plan to incorporated them latter: the issue is now time.

> 
> > ((Is it that hard to read C source file ?))
> 
> Honestly yes, the sympow code is very hard to read for me. Its a mix of very non-standard formatting, a lack of comments and my limited C and domain knowledge. That is why I'm glad that you have taken up the maintenance.
> 
> I'll try a `-quiet` wrapper for now.

I would forget it and spend my time else where.

I plan to change the verbosity level of this message (once I have time before me).

Jerome



---

archive/issue_comments_023433.json:
```json
{
    "body": "Replying to [comment:45 gh-jgmbenoit]:\n> Replying to [comment:44 gh-timokau]:\n> > - could the global cache reasonably be pre-computed at build time?\n> \n> No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.\n\nI don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.\n\n> > I'll try a `-quiet` wrapper for now.\n> \n> I would forget it and spend my time else where.\n> \n> I plan to change the verbosity level of this message (once I have time before me).\n\nWell it seems to break sages parsing, so I'll need to add that wrapper. After that sages tests still fail. I'm now trying to update sages spkg first to find out if thats a quirk with nix's build system or a parsing issue.\nHowever while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an \"experimental\" package that currently isn't included in the sage distribution by default. I would replace it by this python script:\n\n\n```\nimport sys\nimport platform\n\nif sys.byteorder == \"little\":\n    endian = \"le\"\nelse:\n    endian = \"be\"\n\nbits = platform.architecture()[0][:-3]\n\n# for example \"le64\" or \"be32\"\nprint(endian + bits)\n```\n\n\nIs that correct?",
    "created_at": "2018-08-27T14:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23433",
    "user": "@timokau"
}
```

Replying to [comment:45 gh-jgmbenoit]:
> Replying to [comment:44 gh-timokau]:
> > - could the global cache reasonably be pre-computed at build time?
> 
> No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.

I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.

> > I'll try a `-quiet` wrapper for now.
> 
> I would forget it and spend my time else where.
> 
> I plan to change the verbosity level of this message (once I have time before me).

Well it seems to break sages parsing, so I'll need to add that wrapper. After that sages tests still fail. I'm now trying to update sages spkg first to find out if thats a quirk with nix's build system or a parsing issue.
However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:


```
import sys
import platform

if sys.byteorder == "little":
    endian = "le"
else:
    endian = "be"

bits = platform.architecture()[0][:-3]

# for example "le64" or "be32"
print(endian + bits)
```


Is that correct?



---

archive/issue_comments_023434.json:
```json
{
    "body": "Replying to [comment:46 gh-timokau]:\n> Replying to [comment:45 gh-jgmbenoit]:\n> > Replying to [comment:44 gh-timokau]:\n> > > - could the global cache reasonably be pre-computed at build time?\n> > \n> > No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.\n> \n> I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.\n\nthe data are stored as binary, so the data binary file can be detected as an arbitrary binary file,\nnamely as a suspicious file.\n\nOn my box:\n\n$ file ~/.sympow/datafiles/le64/P014M.bin\n\ngives\n\n$ /home/jgmb/.sympow/datafiles/le64/P014M.bin: data\n\nFor any regular binary files, file(1) should be able to identified.\n\n\n> \n> > > I'll try a `-quiet` wrapper for now.\n> > \n> > I would forget it and spend my time else where.\n> > \n> > I plan to change the verbosity level of this message (once I have time before me).\n> \n> Well it seems to break sages parsing, so I'll need to add that wrapper. After that sages tests still fail. I'm now trying to update sages spkg first to find out if thats a quirk with nix's build system or a parsing issue.\n\n\nThis is indeed an issue.\n\n\n> However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an \"experimental\" package that currently isn't included in the sage distribution by default. I would replace it by this python script:\n> \n> {{{\n> import sys\n> import platform\n> \n> if sys.byteorder == \"little\":\n>     endian = \"le\"\n> else:\n>     endian = \"be\"\n> \n> bits = platform.architecture()[0][:-3]\n> \n> # for example \"le64\" or \"be32\"\n> print(endian + bits)\n> }}}\n> \n> Is that correct?\n\n\nit looks correct.",
    "created_at": "2018-08-27T15:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23434",
    "user": "@jgmbenoit"
}
```

Replying to [comment:46 gh-timokau]:
> Replying to [comment:45 gh-jgmbenoit]:
> > Replying to [comment:44 gh-timokau]:
> > > - could the global cache reasonably be pre-computed at build time?
> > 
> > No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.
> 
> I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.

the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,
namely as a suspicious file.

On my box:

$ file ~/.sympow/datafiles/le64/P014M.bin

gives

$ /home/jgmb/.sympow/datafiles/le64/P014M.bin: data

For any regular binary files, file(1) should be able to identified.


> 
> > > I'll try a `-quiet` wrapper for now.
> > 
> > I would forget it and spend my time else where.
> > 
> > I plan to change the verbosity level of this message (once I have time before me).
> 
> Well it seems to break sages parsing, so I'll need to add that wrapper. After that sages tests still fail. I'm now trying to update sages spkg first to find out if thats a quirk with nix's build system or a parsing issue.


This is indeed an issue.


> However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:
> 
> {{{
> import sys
> import platform
> 
> if sys.byteorder == "little":
>     endian = "le"
> else:
>     endian = "be"
> 
> bits = platform.architecture()[0][:-3]
> 
> # for example "le64" or "be32"
> print(endian + bits)
> }}}
> 
> Is that correct?


it looks correct.



---

archive/issue_comments_023435.json:
```json
{
    "body": "New commits:",
    "created_at": "2018-08-27T23:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23435",
    "user": "@timokau"
}
```

New commits:



---

archive/issue_comments_023436.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2018-08-27T23:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23436",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_023437.json:
```json
{
    "body": "New commits:",
    "created_at": "2018-08-27T23:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23437",
    "user": "@timokau"
}
```

New commits:



---

archive/issue_comments_023438.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-08-27T23:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23438",
    "user": "@timokau"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023439.json:
```json
{
    "body": "Replying to [comment:47 gh-jgmbenoit]:\n> Replying to [comment:46 gh-timokau]:\n> > I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.\n> \n> the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,\n> namely as a suspicious file.\n\nWhy is a binary data file any more suspicious than a binary executable?\n\n> \n> > However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an \"experimental\" package that currently isn't included in the sage distribution by default. I would replace it by this python script:\n> > \n[...]\n> \n> \n> it looks correct.\n\nI've implemented it. Its really a shame sagemath doesn't provide autotools by default.",
    "created_at": "2018-08-27T23:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23439",
    "user": "@timokau"
}
```

Replying to [comment:47 gh-jgmbenoit]:
> Replying to [comment:46 gh-timokau]:
> > I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.
> 
> the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,
> namely as a suspicious file.

Why is a binary data file any more suspicious than a binary executable?

> 
> > However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:
> > 
[...]
> 
> 
> it looks correct.

I've implemented it. Its really a shame sagemath doesn't provide autotools by default.



---

archive/issue_comments_023440.json:
```json
{
    "body": "Points for reviewers to focus on I'm not sure about:\n\n- this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.\n- it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.",
    "created_at": "2018-08-27T23:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23440",
    "user": "@timokau"
}
```

Points for reviewers to focus on I'm not sure about:

- this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.
- it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.



---

archive/issue_comments_023441.json:
```json
{
    "body": "Replying to [comment:51 gh-timokau]:\n> Replying to [comment:47 gh-jgmbenoit]:\n> > Replying to [comment:46 gh-timokau]:\n> > > I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.\n> > \n> > the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,\n> > namely as a suspicious file.\n> \n> Why is a binary data file any more suspicious than a binary executable?\n\nA binary executable is recognized as such by file(1): so it recognisable as such.\n\n\n> \n> > \n> > > However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an \"experimental\" package that currently isn't included in the sage distribution by default. I would replace it by this python script:\n> > > \n> [...]\n> > \n> > \n> > it looks correct.\n> \n> I've implemented it. Its really a shame sagemath doesn't provide autotools by default.",
    "created_at": "2018-08-28T03:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23441",
    "user": "@jgmbenoit"
}
```

Replying to [comment:51 gh-timokau]:
> Replying to [comment:47 gh-jgmbenoit]:
> > Replying to [comment:46 gh-timokau]:
> > > I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.
> > 
> > the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,
> > namely as a suspicious file.
> 
> Why is a binary data file any more suspicious than a binary executable?

A binary executable is recognized as such by file(1): so it recognisable as such.


> 
> > 
> > > However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:
> > > 
> [...]
> > 
> > 
> > it looks correct.
> 
> I've implemented it. Its really a shame sagemath doesn't provide autotools by default.



---

archive/issue_comments_023442.json:
```json
{
    "body": "Replying to [comment:53 gh-jgmbenoit]:\n> Replying to [comment:51 gh-timokau]:\n> > Why is a binary data file any more suspicious than a binary executable?\n> \n> A binary executable is recognized as such by file(1): so it recognisable as such.\n\nWhy does that matter? I don't understand why an executable that is recognized as such is any less suspicious or security relevant than a binary data file. The executable is arguably more security relevant.",
    "created_at": "2018-08-28T16:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23442",
    "user": "@timokau"
}
```

Replying to [comment:53 gh-jgmbenoit]:
> Replying to [comment:51 gh-timokau]:
> > Why is a binary data file any more suspicious than a binary executable?
> 
> A binary executable is recognized as such by file(1): so it recognisable as such.

Why does that matter? I don't understand why an executable that is recognized as such is any less suspicious or security relevant than a binary data file. The executable is arguably more security relevant.



---

archive/issue_comments_023443.json:
```json
{
    "body": "Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)",
    "created_at": "2019-03-25T10:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23443",
    "user": "embray"
}
```

Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)



---

archive/issue_comments_023444.json:
```json
{
    "body": "Moving tickets from the Sage 8.8 milestone that have been actively worked on in the last six months to the next release milestone (optimistically).",
    "created_at": "2019-07-03T11:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23444",
    "user": "embray"
}
```

Moving tickets from the Sage 8.8 milestone that have been actively worked on in the last six months to the next release milestone (optimistically).



---

archive/issue_comments_023445.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2019-12-30T14:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23445",
    "user": "embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_comments_023446.json:
```json
{
    "body": "Replying to [comment:51 gh-timokau]:\n> I've implemented it. Its really a shame sagemath doesn't provide autotools by default.\n\nAutotools are supposed to be run by maintainers at \"make dist\" time, not at installation time",
    "created_at": "2020-04-01T13:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23446",
    "user": "mkoeppe"
}
```

Replying to [comment:51 gh-timokau]:
> I've implemented it. Its really a shame sagemath doesn't provide autotools by default.

Autotools are supposed to be run by maintainers at "make dist" time, not at installation time



---

archive/issue_comments_023447.json:
```json
{
    "body": "What are other distributions doing about sympow? \n\nRunning into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true",
    "created_at": "2020-04-01T13:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23447",
    "user": "mkoeppe"
}
```

What are other distributions doing about sympow? 

Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true



---

archive/issue_comments_023448.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2020-04-01T14:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23448",
    "user": "mkoeppe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023449.json:
```json
{
    "body": "Replying to [comment:60 mkoeppe]:\n> Replying to [comment:51 gh-timokau]:\n> > I've implemented it. Its really a shame sagemath doesn't provide autotools by default.\n> \n> Autotools are supposed to be run by maintainers at \"make dist\" time, not at installation time \n\nThis is true.\n\nI have just tried to refresh my memory about:\nbasically the Autotools part jsut run some c code: so I guess that we can replace it with a C source.",
    "created_at": "2020-04-01T15:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23449",
    "user": "@jgmbenoit"
}
```

Replying to [comment:60 mkoeppe]:
> Replying to [comment:51 gh-timokau]:
> > I've implemented it. Its really a shame sagemath doesn't provide autotools by default.
> 
> Autotools are supposed to be run by maintainers at "make dist" time, not at installation time 

This is true.

I have just tried to refresh my memory about:
basically the Autotools part jsut run some c code: so I guess that we can replace it with a C source.



---

archive/issue_comments_023450.json:
```json
{
    "body": "Replying to [comment:61 mkoeppe]:\n> What are other distributions doing about sympow? \n\nWhat do you mean ?\n\n> \n> Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true\n\nI have just seen the merge request on gitlab. Next week I might be on vacation, I will a look then.",
    "created_at": "2020-04-01T15:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23450",
    "user": "@jgmbenoit"
}
```

Replying to [comment:61 mkoeppe]:
> What are other distributions doing about sympow? 

What do you mean ?

> 
> Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true

I have just seen the merge request on gitlab. Next week I might be on vacation, I will a look then.



---

archive/issue_comments_023451.json:
```json
{
    "body": "Replying to [comment:64 gh-jgmbenoit]:\n> Replying to [comment:61 mkoeppe]:\n> > What are other distributions doing about sympow? \n\nconda-forge, arch, etc. are packaging sage and the packages they need. Just wondering whether they are using the fork, and how they have adjusted the sage interface and doctests if necessary.",
    "created_at": "2020-04-01T15:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23451",
    "user": "mkoeppe"
}
```

Replying to [comment:64 gh-jgmbenoit]:
> Replying to [comment:61 mkoeppe]:
> > What are other distributions doing about sympow? 

conda-forge, arch, etc. are packaging sage and the packages they need. Just wondering whether they are using the fork, and how they have adjusted the sage interface and doctests if necessary.



---

archive/issue_comments_023452.json:
```json
{
    "body": "`conda-forge` switched to debian's fork more than a year ago.",
    "created_at": "2020-04-01T15:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23452",
    "user": "isuruf"
}
```

`conda-forge` switched to debian's fork more than a year ago.



---

archive/issue_comments_023453.json:
```json
{
    "body": "nixpkgs is using the fork as well. I've switched it over here: https://github.com/NixOS/nixpkgs/commit/5e58c5f900e51c4dd89de8a4518c5bb13581f3c6\n\nNo patches to sage were necessary to pass the test suite. I still added a patch that puts the cache directory under the `.sage` directory though: https://github.com/NixOS/nixpkgs/commit/9ef44b34316cb47c0bda49f05c57ca2ea6c96816",
    "created_at": "2020-04-01T15:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23453",
    "user": "@timokau"
}
```

nixpkgs is using the fork as well. I've switched it over here: https://github.com/NixOS/nixpkgs/commit/5e58c5f900e51c4dd89de8a4518c5bb13581f3c6

No patches to sage were necessary to pass the test suite. I still added a patch that puts the cache directory under the `.sage` directory though: https://github.com/NixOS/nixpkgs/commit/9ef44b34316cb47c0bda49f05c57ca2ea6c96816



---

archive/issue_comments_023454.json:
```json
{
    "body": "Anything missing on this ticket other than rebasing?",
    "created_at": "2020-04-01T15:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23454",
    "user": "mkoeppe"
}
```

Anything missing on this ticket other than rebasing?



---

archive/issue_comments_023455.json:
```json
{
    "body": "Replying to [comment:52 gh-timokau]:\n> Points for reviewers to focus on I'm not sure about:\n> \n> - this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.\n> - it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.\n\nThis is probably still relevant. Other than that, I don't remember. I won't continue working on this for now, so anybody else should feel free to pick this up.",
    "created_at": "2020-04-01T17:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23455",
    "user": "@timokau"
}
```

Replying to [comment:52 gh-timokau]:
> Points for reviewers to focus on I'm not sure about:
> 
> - this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.
> - it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.

This is probably still relevant. Other than that, I don't remember. I won't continue working on this for now, so anybody else should feel free to pick this up.



---

archive/issue_comments_023456.json:
```json
{
    "body": "Replying to [comment:63 gh-jgmbenoit]:\n> Replying to [comment:60 mkoeppe]:\n> > Replying to [comment:51 gh-timokau]:\n> > > I've implemented it. Its really a shame sagemath doesn't provide autotools by default.\n> > \n> > Autotools are supposed to be run by maintainers at \"make dist\" time, not at installation time \n> \n> This is true.\n> \n> I have just tried to refresh my memory about:\n> basically the Autotools part jsut run some c code: so I guess that we can replace it with a C source.\n\nIn version 2.023.6, the autotools dependency was discarded: the endianess is now determine via a C program. Please check it on exotic architectures if you can, and let me know if any issue arises.",
    "created_at": "2020-04-17T06:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23456",
    "user": "@jgmbenoit"
}
```

Replying to [comment:63 gh-jgmbenoit]:
> Replying to [comment:60 mkoeppe]:
> > Replying to [comment:51 gh-timokau]:
> > > I've implemented it. Its really a shame sagemath doesn't provide autotools by default.
> > 
> > Autotools are supposed to be run by maintainers at "make dist" time, not at installation time 
> 
> This is true.
> 
> I have just tried to refresh my memory about:
> basically the Autotools part jsut run some c code: so I guess that we can replace it with a C source.

In version 2.023.6, the autotools dependency was discarded: the endianess is now determine via a C program. Please check it on exotic architectures if you can, and let me know if any issue arises.



---

archive/issue_comments_023457.json:
```json
{
    "body": "Replying to [comment:64 gh-jgmbenoit]:\n> Replying to [comment:61 mkoeppe]:\n> > What are other distributions doing about sympow? \n> \n> What do you mean ?\n> \n> > \n> > Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true\n> \n> I have just seen the merge request on gitlab. Next week I might be on vacation, I will a look then.\nI applied the patch in version 2.023.6 .",
    "created_at": "2020-04-17T06:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23457",
    "user": "@jgmbenoit"
}
```

Replying to [comment:64 gh-jgmbenoit]:
> Replying to [comment:61 mkoeppe]:
> > What are other distributions doing about sympow? 
> 
> What do you mean ?
> 
> > 
> > Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true
> 
> I have just seen the merge request on gitlab. Next week I might be on vacation, I will a look then.
I applied the patch in version 2.023.6 .



---

archive/issue_comments_023458.json:
```json
{
    "body": "Replying to [comment:69 gh-timokau]:\n> Replying to [comment:52 gh-timokau]:\n> > Points for reviewers to focus on I'm not sure about:\n> > \n> > - this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.\n> > - it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.\n> \n> This is probably still relevant. Other than that, I don't remember. I won't continue working on this for now, so anybody else should feel free to pick this up.\n\n\nIf sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do. And given that this is binary data and the quality of the code, I'm not sure that it's wise to share the cache among a \"sympow\" group anywhere else. So FWIW I would leave it at the default.",
    "created_at": "2020-05-12T19:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23458",
    "user": "mjo"
}
```

Replying to [comment:69 gh-timokau]:
> Replying to [comment:52 gh-timokau]:
> > Points for reviewers to focus on I'm not sure about:
> > 
> > - this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.
> > - it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.
> 
> This is probably still relevant. Other than that, I don't remember. I won't continue working on this for now, so anybody else should feel free to pick this up.


If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do. And given that this is binary data and the quality of the code, I'm not sure that it's wise to share the cache among a "sympow" group anywhere else. So FWIW I would leave it at the default.



---

archive/issue_comments_023459.json:
```json
{
    "body": "Replying to [comment:74 mjo]:\n> \n> If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.\n\nActually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`. I'm not sure what to do about that one; a wrapper or launcher script (that overrides that directory and uses something under `$HOME`) is the only way I've been able to make it work so far. More details eventually on https://gitlab.com/rezozer/forks/sympow/-/issues/3",
    "created_at": "2020-05-15T14:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23459",
    "user": "mjo"
}
```

Replying to [comment:74 mjo]:
> 
> If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.

Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`. I'm not sure what to do about that one; a wrapper or launcher script (that overrides that directory and uses something under `$HOME`) is the only way I've been able to make it work so far. More details eventually on https://gitlab.com/rezozer/forks/sympow/-/issues/3



---

archive/issue_comments_023460.json:
```json
{
    "body": "Replying to [comment:75 mjo]:\n> Replying to [comment:74 mjo]:\n> > \n> > If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.\n> \n> Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`.\n\nThis is true, but turns out to not be a problem. The fork tries to use the directory under `VARPREFIX`, and if that doesn't work, it falls back to using `$HOME/.sympow` for that data as well. The only \"problem\" with that is that a warning is displayed to the user if he runs sympow by hand.\n\nSo, the sage SPKG should leave `VARPREFIX` alone. In Gentoo I'm going to patch out the expected warning (see the gitlab issue), and that may make sense for sage as well since `/var` will not generally be writable by whoever is running sage. The data will ultimately get stored under `$HOME/.sympow`, and that's what we want in the SPKG.",
    "created_at": "2020-05-16T12:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23460",
    "user": "mjo"
}
```

Replying to [comment:75 mjo]:
> Replying to [comment:74 mjo]:
> > 
> > If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.
> 
> Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`.

This is true, but turns out to not be a problem. The fork tries to use the directory under `VARPREFIX`, and if that doesn't work, it falls back to using `$HOME/.sympow` for that data as well. The only "problem" with that is that a warning is displayed to the user if he runs sympow by hand.

So, the sage SPKG should leave `VARPREFIX` alone. In Gentoo I'm going to patch out the expected warning (see the gitlab issue), and that may make sense for sage as well since `/var` will not generally be writable by whoever is running sage. The data will ultimately get stored under `$HOME/.sympow`, and that's what we want in the SPKG.



---

archive/issue_comments_023461.json:
```json
{
    "body": "Replying to [comment:75 mjo]:\n> Replying to [comment:74 mjo]:\n> > \n> > If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.\n> \n> Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`. I'm not sure what to do about that one; a wrapper or launcher script (that overrides that directory and uses something under `$HOME`) is the only way I've been able to make it work so far. More details eventually on https://gitlab.com/rezozer/forks/sympow/-/issues/3\n\nThere was already quite a bit of discussion about this issue here, see the posts following this message: #3360#comment:35\n\nFor nixpkgs, I decided to use a wrapper instead of a patch: https://github.com/NixOS/nixpkgs/blob/962f93c46b1eaaedbc118c06adfd439ce341a0db/pkgs/development/libraries/science/math/sympow/default.nix#L44",
    "created_at": "2020-05-18T16:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23461",
    "user": "@timokau"
}
```

Replying to [comment:75 mjo]:
> Replying to [comment:74 mjo]:
> > 
> > If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.
> 
> Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`. I'm not sure what to do about that one; a wrapper or launcher script (that overrides that directory and uses something under `$HOME`) is the only way I've been able to make it work so far. More details eventually on https://gitlab.com/rezozer/forks/sympow/-/issues/3

There was already quite a bit of discussion about this issue here, see the posts following this message: #3360#comment:35

For nixpkgs, I decided to use a wrapper instead of a patch: https://github.com/NixOS/nixpkgs/blob/962f93c46b1eaaedbc118c06adfd439ce341a0db/pkgs/development/libraries/science/math/sympow/default.nix#L44



---

archive/issue_comments_023462.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2020-06-14T20:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23462",
    "user": "mkoeppe"
}
```

Changing priority from major to critical.



---

archive/issue_comments_023463.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-05T17:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23463",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023464.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-05T17:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23464",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023465.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-05T17:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23465",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023466.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-07-05T17:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23466",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023467.json:
```json
{
    "body": "Builds on macOS, haven't tested anything else yet.",
    "created_at": "2020-07-05T17:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23467",
    "user": "mkoeppe"
}
```

Builds on macOS, haven't tested anything else yet.



---

archive/issue_comments_023468.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-05T18:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23468",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023469.json:
```json
{
    "body": "Tests run at https://github.com/mkoeppe/sage/actions/runs/158805080",
    "created_at": "2020-07-06T02:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23469",
    "user": "mkoeppe"
}
```

Tests run at https://github.com/mkoeppe/sage/actions/runs/158805080



---

archive/issue_comments_023470.json:
```json
{
    "body": "\n```\n  [sympow-2.023.6]     File \"/usr/lib/python3.6/urllib/request.py\", line 1952, in http_error\n  [sympow-2.023.6]       return self.http_error_default(url, fp, errcode, errmsg, headers)\n  [sympow-2.023.6]     File \"/cygdrive/d/a/sage/sage/build/bin/../sage_bootstrap/download/transfer.py\", line 107, in http_error_default\n  [sympow-2.023.6]       raise DownloadError(errcode, errmsg, url)\n  [sympow-2.023.6]   OSError: [Errno socket error] [Errno 403] Forbidden: '//gitlab.com/rezozer/forks/sympow/-/archive/v2.023.6/sympow-v2.023.6.tar.gz'\n  [sympow-2.023.6]   \n```\n",
    "created_at": "2020-07-06T12:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23470",
    "user": "mkoeppe"
}
```


```
  [sympow-2.023.6]     File "/usr/lib/python3.6/urllib/request.py", line 1952, in http_error
  [sympow-2.023.6]       return self.http_error_default(url, fp, errcode, errmsg, headers)
  [sympow-2.023.6]     File "/cygdrive/d/a/sage/sage/build/bin/../sage_bootstrap/download/transfer.py", line 107, in http_error_default
  [sympow-2.023.6]       raise DownloadError(errcode, errmsg, url)
  [sympow-2.023.6]   OSError: [Errno socket error] [Errno 403] Forbidden: '//gitlab.com/rezozer/forks/sympow/-/archive/v2.023.6/sympow-v2.023.6.tar.gz'
  [sympow-2.023.6]   
```




---

archive/issue_comments_023471.json:
```json
{
    "body": "Replying to [comment:92 mkoeppe]:\n> {{{\n>   [sympow-2.023.6]     File \"/usr/lib/python3.6/urllib/request.py\", line 1952, in http_error\n>   [sympow-2.023.6]       return self.http_error_default(url, fp, errcode, errmsg, headers)\n>   [sympow-2.023.6]     File \"/cygdrive/d/a/sage/sage/build/bin/../sage_bootstrap/download/transfer.py\", line 107, in http_error_default\n>   [sympow-2.023.6]       raise DownloadError(errcode, errmsg, url)\n>   [sympow-2.023.6]   OSError: [Errno socket error] [Errno 403] Forbidden: '//gitlab.com/rezozer/forks/sympow/-/archive/v2.023.6/sympow-v2.023.6.tar.gz'\n>   [sympow-2.023.6]   \n> }}}\n\nthe link works from the browser for me.",
    "created_at": "2020-07-06T14:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23471",
    "user": "dimpase"
}
```

Replying to [comment:92 mkoeppe]:
> {{{
>   [sympow-2.023.6]     File "/usr/lib/python3.6/urllib/request.py", line 1952, in http_error
>   [sympow-2.023.6]       return self.http_error_default(url, fp, errcode, errmsg, headers)
>   [sympow-2.023.6]     File "/cygdrive/d/a/sage/sage/build/bin/../sage_bootstrap/download/transfer.py", line 107, in http_error_default
>   [sympow-2.023.6]       raise DownloadError(errcode, errmsg, url)
>   [sympow-2.023.6]   OSError: [Errno socket error] [Errno 403] Forbidden: '//gitlab.com/rezozer/forks/sympow/-/archive/v2.023.6/sympow-v2.023.6.tar.gz'
>   [sympow-2.023.6]   
> }}}

the link works from the browser for me.



---

archive/issue_comments_023472.json:
```json
{
    "body": "https://gitlab.com/gitlab-org/gitlab-runner/-/issues/3230",
    "created_at": "2020-07-06T21:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23472",
    "user": "mkoeppe"
}
```

https://gitlab.com/gitlab-org/gitlab-runner/-/issues/3230



---

archive/issue_comments_023473.json:
```json
{
    "body": "Tests using a temporary github url at https://github.com/mkoeppe/sage/actions/runs/160116395",
    "created_at": "2020-07-07T03:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23473",
    "user": "mkoeppe"
}
```

Tests using a temporary github url at https://github.com/mkoeppe/sage/actions/runs/160116395



---

archive/issue_comments_023474.json:
```json
{
    "body": "`ubuntu-trusty-minimal` (https://github.com/mkoeppe/sage/runs/844024596):\n\n```\ngcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.4) \n****************************************************\nPackage 'sympow' is currently not installed\nNo legacy uninstaller found for 'sympow'; nothing to do\nCFLAGS for SYMPOW: -fno-fast-math -mfpmath=sse -Dx86 -ffp-contract=on \nThe double precision of your FPU is 53 bits.\nCFLAGS for SYMPOW:  -std=gnu11 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH \nThe double precision of your FPU is 53 bits.\nconfig/endiantuple.c:6:2: error: #error \"require C11 or higher\"\n #error \"require C11 or higher\"\n  ^\nError: the command below failed:\ngcc config/endiantuple.c -o config/endiantuple\n********************************************************************************\nError configuring SYMPOW\n```\n\nLikewise on `debian-jessie-minimal`, `linuxmint-17-minimal`.",
    "created_at": "2020-07-07T16:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23474",
    "user": "mkoeppe"
}
```

`ubuntu-trusty-minimal` (https://github.com/mkoeppe/sage/runs/844024596):

```
gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.4) 
****************************************************
Package 'sympow' is currently not installed
No legacy uninstaller found for 'sympow'; nothing to do
CFLAGS for SYMPOW: -fno-fast-math -mfpmath=sse -Dx86 -ffp-contract=on 
The double precision of your FPU is 53 bits.
CFLAGS for SYMPOW:  -std=gnu11 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH 
The double precision of your FPU is 53 bits.
config/endiantuple.c:6:2: error: #error "require C11 or higher"
 #error "require C11 or higher"
  ^
Error: the command below failed:
gcc config/endiantuple.c -o config/endiantuple
********************************************************************************
Error configuring SYMPOW
```

Likewise on `debian-jessie-minimal`, `linuxmint-17-minimal`.



---

archive/issue_comments_023475.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2020-07-07T16:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23475",
    "user": "mkoeppe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023476.json:
```json
{
    "body": "This is now https://gitlab.com/rezozer/forks/sympow/-/issues/4",
    "created_at": "2020-07-08T18:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23476",
    "user": "mkoeppe"
}
```

This is now https://gitlab.com/rezozer/forks/sympow/-/issues/4



---

archive/issue_comments_023477.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-08T18:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23477",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023478.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-08T18:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23478",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023479.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-08T19:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23479",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023480.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-07-08T19:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23480",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023481.json:
```json
{
    "body": "Tests run at https://github.com/mkoeppe/sage/pull/41/checks?check_run_id=851182060",
    "created_at": "2020-07-08T19:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23481",
    "user": "mkoeppe"
}
```

Tests run at https://github.com/mkoeppe/sage/pull/41/checks?check_run_id=851182060



---

archive/issue_comments_023482.json:
```json
{
    "body": "(comment for the wrong ticket)",
    "created_at": "2020-07-09T18:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23482",
    "user": "mkoeppe"
}
```

(comment for the wrong ticket)



---

archive/issue_comments_023483.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2020-07-09T18:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23483",
    "user": "mkoeppe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023484.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-07-09T18:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23484",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023485.json:
```json
{
    "body": "Tests look OK. Ready for review",
    "created_at": "2020-07-09T18:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23485",
    "user": "mkoeppe"
}
```

Tests look OK. Ready for review



---

archive/issue_comments_023486.json:
```json
{
    "body": "do you test with gcc10?",
    "created_at": "2020-07-09T20:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23486",
    "user": "dimpase"
}
```

do you test with gcc10?



---

archive/issue_comments_023487.json:
```json
{
    "body": "Haven't yet. I trust upstream there",
    "created_at": "2020-07-09T20:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23487",
    "user": "mkoeppe"
}
```

Haven't yet. I trust upstream there



---

archive/issue_comments_023488.json:
```json
{
    "body": "We can reuse #30067 as a GCC 10 upgrade test ticket",
    "created_at": "2020-07-09T20:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23488",
    "user": "mkoeppe"
}
```

We can reuse #30067 as a GCC 10 upgrade test ticket



---

archive/issue_comments_023489.json:
```json
{
    "body": "or #29456",
    "created_at": "2020-07-09T20:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23489",
    "user": "mkoeppe"
}
```

or #29456



---

archive/issue_comments_023490.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-10T07:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23490",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023491.json:
```json
{
    "body": "Replying to [comment:111 mkoeppe]:\n> or #29456\n\nGCC10 testing is happening on #29456 now.",
    "created_at": "2020-07-10T17:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23491",
    "user": "mkoeppe"
}
```

Replying to [comment:111 mkoeppe]:
> or #29456

GCC10 testing is happening on #29456 now.



---

archive/issue_comments_023492.json:
```json
{
    "body": "But this ticket does not need to wait for it -- ready for review.",
    "created_at": "2020-07-10T17:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23492",
    "user": "mkoeppe"
}
```

But this ticket does not need to wait for it -- ready for review.



---

archive/issue_comments_023493.json:
```json
{
    "body": "`sympow` builds OK on all platforms (including with gcc 10 for `fedora-32-minimal`) at https://github.com/mkoeppe/sage/actions/runs/168165380\n\nHowever, I see many test failures in sagelib that seem related to `sympow` in `fedora-32-standard` (https://github.com/mkoeppe/sage/runs/867731204) -- where `sympow` comes from the system after #29673!\n\n```\n**********************************************************************\nFile \"src/sage/lfunctions/sympow.py\", line 225, in sage.lfunctions.sympow.Sympow.modular_degree\nFailed example:\n    sympow.modular_degree(EllipticCurve('11a'))\nException raised:\n    Traceback (most recent call last):\n      File \"/sage/local/lib/python3.7/site-packages/sage/doctest/forker.py\", line 707, in _run\n        self.compile_and_execute(example, compiler, test.globs)\n      File \"/sage/local/lib/python3.7/site-packages/sage/doctest/forker.py\", line 1132, in compile_and_execute\n        exec(compiled, globs)\n      File \"<doctest sage.lfunctions.sympow.Sympow.modular_degree[0]>\", line 1, in <module>\n        sympow.modular_degree(EllipticCurve('11a'))\n      File \"/sage/local/lib/python3.7/site-packages/sage/lfunctions/sympow.py\", line 241, in modular_degree\n        raise RuntimeError(\"failed to compute modular degree\")\n    RuntimeError: failed to compute modular degree\n----------------------------------------------------------------------\nsage -t src/sage/lfunctions/sympow.py  # 10 doctests failed\nsage -t src/sage/modular/abvar/abvar.py  # 1 doctest failed\nsage -t src/sage/modular/hecke/submodule.py  # 1 doctest failed\nsage -t src/sage/schemes/elliptic_curves/ell_rational_field.py  # 14 doctests failed\n----------------------------------------------------------------------\n```\n",
    "created_at": "2020-07-14T22:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23493",
    "user": "mkoeppe"
}
```

`sympow` builds OK on all platforms (including with gcc 10 for `fedora-32-minimal`) at https://github.com/mkoeppe/sage/actions/runs/168165380

However, I see many test failures in sagelib that seem related to `sympow` in `fedora-32-standard` (https://github.com/mkoeppe/sage/runs/867731204) -- where `sympow` comes from the system after #29673!

```
**********************************************************************
File "src/sage/lfunctions/sympow.py", line 225, in sage.lfunctions.sympow.Sympow.modular_degree
Failed example:
    sympow.modular_degree(EllipticCurve('11a'))
Exception raised:
    Traceback (most recent call last):
      File "/sage/local/lib/python3.7/site-packages/sage/doctest/forker.py", line 707, in _run
        self.compile_and_execute(example, compiler, test.globs)
      File "/sage/local/lib/python3.7/site-packages/sage/doctest/forker.py", line 1132, in compile_and_execute
        exec(compiled, globs)
      File "<doctest sage.lfunctions.sympow.Sympow.modular_degree[0]>", line 1, in <module>
        sympow.modular_degree(EllipticCurve('11a'))
      File "/sage/local/lib/python3.7/site-packages/sage/lfunctions/sympow.py", line 241, in modular_degree
        raise RuntimeError("failed to compute modular degree")
    RuntimeError: failed to compute modular degree
----------------------------------------------------------------------
sage -t src/sage/lfunctions/sympow.py  # 10 doctests failed
sage -t src/sage/modular/abvar/abvar.py  # 1 doctest failed
sage -t src/sage/modular/hecke/submodule.py  # 1 doctest failed
sage -t src/sage/schemes/elliptic_curves/ell_rational_field.py  # 14 doctests failed
----------------------------------------------------------------------
```




---

archive/issue_comments_023494.json:
```json
{
    "body": "Replying to [comment:116 mkoeppe]:\n> I see many test failures in sagelib that seem related to `sympow` in `fedora-32-standard` (https://github.com/mkoeppe/sage/runs/867731204) -- where `sympow` comes from the system after #29673!\n\nI have opened #30147 (Fix `spkg-configure.m4` for `sympow`) for this.\n\nThe present ticket is ready for review.",
    "created_at": "2020-07-14T22:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23494",
    "user": "mkoeppe"
}
```

Replying to [comment:116 mkoeppe]:
> I see many test failures in sagelib that seem related to `sympow` in `fedora-32-standard` (https://github.com/mkoeppe/sage/runs/867731204) -- where `sympow` comes from the system after #29673!

I have opened #30147 (Fix `spkg-configure.m4` for `sympow`) for this.

The present ticket is ready for review.



---

archive/issue_comments_023495.json:
```json
{
    "body": "lgtm",
    "created_at": "2020-07-17T22:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23495",
    "user": "dimpase"
}
```

lgtm



---

archive/issue_comments_023496.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-17T22:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23496",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023497.json:
```json
{
    "body": "Thanks.",
    "created_at": "2020-07-17T23:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23497",
    "user": "mkoeppe"
}
```

Thanks.



---

archive/issue_comments_023498.json:
```json
{
    "body": "I'm getting lots of errors of the form:\n\n```\n**********************************************************************\nFile \"src/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3845, in sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.congruence_number\nFailed example:\n    E.modular_degree()\nExpected:\n    16\nGot:\n    **WARNING** failed to create data bin package cache folder /home/buildbot/slave/sage_git/build/local/var/cache/sympow/datafiles/le64\n    16\n**********************************************************************\n```\n",
    "created_at": "2020-07-22T22:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23498",
    "user": "vbraun"
}
```

I'm getting lots of errors of the form:

```
**********************************************************************
File "src/sage/schemes/elliptic_curves/ell_rational_field.py", line 3845, in sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.congruence_number
Failed example:
    E.modular_degree()
Expected:
    16
Got:
    **WARNING** failed to create data bin package cache folder /home/buildbot/slave/sage_git/build/local/var/cache/sympow/datafiles/le64
    16
**********************************************************************
```




---

archive/issue_comments_023499.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2020-07-22T22:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23499",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_023500.json:
```json
{
    "body": "on what machine",
    "created_at": "2020-07-22T22:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23500",
    "user": "mkoeppe"
}
```

on what machine



---

archive/issue_comments_023501.json:
```json
{
    "body": "That \"error\" is expected, in general, and shouldn't be output at the default verbosity (in my opinion). I already patched it:\n\nhttps://gitweb.gentoo.org/repo/gentoo.git/plain/sci-mathematics/sympow/files/sympow-2.023.6-no-pkgdatafilesbindir-warnings.patch\n\nThe discussion is here,\n\nhttps://gitlab.com/rezozer/forks/sympow/-/issues/3\n\nif you want to ask upstream about including it.",
    "created_at": "2020-07-23T00:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23501",
    "user": "mjo"
}
```

That "error" is expected, in general, and shouldn't be output at the default verbosity (in my opinion). I already patched it:

https://gitweb.gentoo.org/repo/gentoo.git/plain/sci-mathematics/sympow/files/sympow-2.023.6-no-pkgdatafilesbindir-warnings.patch

The discussion is here,

https://gitlab.com/rezozer/forks/sympow/-/issues/3

if you want to ask upstream about including it.



---

archive/issue_comments_023502.json:
```json
{
    "body": "Let's just include your patch on this ticket",
    "created_at": "2020-07-23T00:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23502",
    "user": "mkoeppe"
}
```

Let's just include your patch on this ticket



---

archive/issue_comments_023503.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-23T01:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23503",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023504.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-07-23T01:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23504",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023505.json:
```json
{
    "body": "over to the bots",
    "created_at": "2020-07-26T22:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23505",
    "user": "dimpase"
}
```

over to the bots



---

archive/issue_comments_023506.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-26T22:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23506",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023507.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2020-07-29T19:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23507",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_023508.json:
```json
{
    "body": "\n```\nmake[5]: Entering directory '/home/release/Sage/local/var/tmp/sage/build/sympow-2.023.6/src'\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o fpu.o fpu.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o analrank.o analrank.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o analytic.o analytic.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o compute.o compute.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o compute2.o compute2.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o help.o help.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o conductors.o conductors.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o disk.o disk.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap.o ec_ap.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap_bsgs.o ec_ap_bsgs.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap_large.o ec_ap_large.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o eulerfactors.o eulerfactors.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o factor.o factor.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o generate.o generate.c\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o init_curve.o init_curve.c\ngenerate.c: In function 'new_data':\ngenerate.c:234:32: error: 'GP' undeclared (first use in this function)\n  234 |  execlp(SH,SH,newdatascript,SH,GP,ARGS,NULL);}\n      |                                ^~\ngenerate.c:234:32: note: each undeclared identifier is reported only once for each function it appears in\ngcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o main.o main.c\nmake[5]: *** [Makefile:39: generate.o] Error 1\n```\n",
    "created_at": "2020-07-29T19:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23508",
    "user": "vbraun"
}
```


```
make[5]: Entering directory '/home/release/Sage/local/var/tmp/sage/build/sympow-2.023.6/src'
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o fpu.o fpu.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o analrank.o analrank.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o analytic.o analytic.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o compute.o compute.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o compute2.o compute2.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o help.o help.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o conductors.o conductors.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o disk.o disk.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap.o ec_ap.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap_bsgs.o ec_ap_bsgs.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap_large.o ec_ap_large.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o eulerfactors.o eulerfactors.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o factor.o factor.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o generate.o generate.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o init_curve.o init_curve.c
generate.c: In function 'new_data':
generate.c:234:32: error: 'GP' undeclared (first use in this function)
  234 |  execlp(SH,SH,newdatascript,SH,GP,ARGS,NULL);}
      |                                ^~
generate.c:234:32: note: each undeclared identifier is reported only once for each function it appears in
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o main.o main.c
make[5]: *** [Makefile:39: generate.o] Error 1
```




---

archive/issue_comments_023509.json:
```json
{
    "body": "on what machine",
    "created_at": "2020-07-29T20:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23509",
    "user": "mkoeppe"
}
```

on what machine



---

archive/issue_comments_023510.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-07-29T21:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23510",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023511.json:
```json
{
    "body": "Tests run at https://github.com/mkoeppe/sage/actions/runs/187726088",
    "created_at": "2020-07-29T21:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23511",
    "user": "mkoeppe"
}
```

Tests run at https://github.com/mkoeppe/sage/actions/runs/187726088



---

archive/issue_comments_023512.json:
```json
{
    "body": "Builds correctly on all platforms.",
    "created_at": "2020-07-30T17:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23512",
    "user": "mkoeppe"
}
```

Builds correctly on all platforms.



---

archive/issue_comments_023513.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2020-07-30T17:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23513",
    "user": "mkoeppe"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_023514.json:
```json
{
    "body": "Fedora 32 x86_64 for the record",
    "created_at": "2020-07-30T23:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23514",
    "user": "vbraun"
}
```

Fedora 32 x86_64 for the record



---

archive/issue_comments_023515.json:
```json
{
    "body": "Replying to [comment:133 vbraun]:\n> Fedora 32 x86_64 for the record\nThanks. Works fine on both `fedora-32-minimal` and `fedora-32-standard` (see above link). Would need more information about the system where it fails.",
    "created_at": "2020-07-31T00:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23515",
    "user": "mkoeppe"
}
```

Replying to [comment:133 vbraun]:
> Fedora 32 x86_64 for the record
Thanks. Works fine on both `fedora-32-minimal` and `fedora-32-standard` (see above link). Would need more information about the system where it fails.



---

archive/issue_comments_023516.json:
```json
{
    "body": "Still doesn't work. My build log has a\n\n```\nwhich: no gp in (/home/release/Sage/build/bin:/home/release/Sage/src/bin:/home/release/Sage/local/bin:/home/release/Sage/build/bin:/home/release/Sage/src/bin:/home/release/Sage/local/bin:/home/release/.local/bin:/home/release/opt/bin:/usr/share/Modules/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/release/.composer/vendor/bin)\n*WARNING*: Could not find gp --- will not be able to build new_data\n```\n\nthats not in yours;  Build race with pari/gp? Seems like this would explain the `error: 'GP' undeclared`",
    "created_at": "2020-08-03T22:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23516",
    "user": "vbraun"
}
```

Still doesn't work. My build log has a

```
which: no gp in (/home/release/Sage/build/bin:/home/release/Sage/src/bin:/home/release/Sage/local/bin:/home/release/Sage/build/bin:/home/release/Sage/src/bin:/home/release/Sage/local/bin:/home/release/.local/bin:/home/release/opt/bin:/usr/share/Modules/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/release/.composer/vendor/bin)
*WARNING*: Could not find gp --- will not be able to build new_data
```

thats not in yours;  Build race with pari/gp? Seems like this would explain the `error: 'GP' undeclared`



---

archive/issue_comments_023517.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2020-08-03T22:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23517",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_023518.json:
```json
{
    "body": "Yes, seems like we may need to add pari as a dependency",
    "created_at": "2020-08-03T23:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23518",
    "user": "mkoeppe"
}
```

Yes, seems like we may need to add pari as a dependency



---

archive/issue_comments_023519.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2020-08-03T23:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23519",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_023520.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-03T23:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23520",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023521.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-08-07T19:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3360#issuecomment-23521",
    "user": "vbraun"
}
```

Resolution: fixed
