# Issue 4821: Experimental scilab-5.0.3.spkg [with spkg, needs review]

archive/issues_004821.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mkoeppe\n\nKeywords: scilab, matlab\n\nI made an experimental scilab-5.0.3.spkg\n\n[http://sage.math.washington.edu/home/jsp/SPKGS/Scilab/scilab-5.0.3.spkg\n]\n\n```\n\nPlease test it by downloading it into $SAGEROOT\nand type\n\n./sage -f -m scilab-5.0.3.spkg\n\nThe -m argument keeps the package in the spkg/build directory for\nfurther experimentation.\n\nSee spkg-install:\nI did a minimal\n./configure --without-javasci --without-gui --with-gfortran\n\n\nThere are two dependencies left: pcre and matio\n\nI don't know how essential they are for a full functional scilab :(\n\n\n```\n\nCheers,\n\nJaap\n\n\nFor me it worked on Fedora 9 and Fedora 10\n\n```\nreal\t36m7.756s\nuser\t22m25.173s\nsys\t9m55.849s\nSuccessfully installed scilab-5.0.3\nYou can safely delete the temporary build directory\n/home/jaap/downloads/sage-3.2.2.alpha0/spkg/build/scilab-5.0.3\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing scilab-5.0.3.spkg\n[jaap@paix sage-3.2.2.alpha0]$\n[...]\nsage: scilab.console()\ngraphics module not found.\njavasci module not found.\n         ___________________________________________\n                        scilab-5.0.3\n\n                  Consortium Scilab (DIGITEO)\n                Copyright (c) 1989-2008 (INRIA)\n                Copyright (c) 1989-2007 (ENPC)\n         ___________________________________________\n\n\nStartup execution:\n   loading initial environment\n\n-->\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4821\n\n",
    "created_at": "2008-12-17T18:32:04Z",
    "labels": [
        "component: packages: experimental",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Experimental scilab-5.0.3.spkg [with spkg, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4821",
    "user": "https://github.com/jaapspies"
}
```
Assignee: mabshoff

CC:  @mkoeppe

Keywords: scilab, matlab

I made an experimental scilab-5.0.3.spkg

[http://sage.math.washington.edu/home/jsp/SPKGS/Scilab/scilab-5.0.3.spkg
]

```

Please test it by downloading it into $SAGEROOT
and type

./sage -f -m scilab-5.0.3.spkg

The -m argument keeps the package in the spkg/build directory for
further experimentation.

See spkg-install:
I did a minimal
./configure --without-javasci --without-gui --with-gfortran


There are two dependencies left: pcre and matio

I don't know how essential they are for a full functional scilab :(


```

Cheers,

Jaap


For me it worked on Fedora 9 and Fedora 10

```
real	36m7.756s
user	22m25.173s
sys	9m55.849s
Successfully installed scilab-5.0.3
You can safely delete the temporary build directory
/home/jaap/downloads/sage-3.2.2.alpha0/spkg/build/scilab-5.0.3
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing scilab-5.0.3.spkg
[jaap@paix sage-3.2.2.alpha0]$
[...]
sage: scilab.console()
graphics module not found.
javasci module not found.
         ___________________________________________
                        scilab-5.0.3

                  Consortium Scilab (DIGITEO)
                Copyright (c) 1989-2008 (INRIA)
                Copyright (c) 1989-2007 (ENPC)
         ___________________________________________


Startup execution:
   loading initial environment

-->
```

Issue created by migration from https://trac.sagemath.org/ticket/4821





---

archive/issue_comments_036479.json:
```json
{
    "body": "This spkg needs at least to attempt to pick the right Fortran runtime at configure time.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T11:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4821#issuecomment-36479",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This spkg needs at least to attempt to pick the right Fortran runtime at configure time.

Cheers,

Michael



---

archive/issue_comments_036480.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> This spkg needs at least to attempt to pick the right Fortran runtime at configure time.\n> \n\n\nOf course you are right, but I don't know how to do that.\n\nBesides there are other dependencies to be resolved.\n\nWhat I did on Fedora was cycling .configure and installing missing dependencies.\n\nNot very suited for inclusion in spkg-install :-)!\n\nJaap",
    "created_at": "2009-02-05T16:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4821#issuecomment-36480",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:1 mabshoff]:
> This spkg needs at least to attempt to pick the right Fortran runtime at configure time.
> 


Of course you are right, but I don't know how to do that.

Besides there are other dependencies to be resolved.

What I did on Fedora was cycling .configure and installing missing dependencies.

Not very suited for inclusion in spkg-install :-)!

Jaap



---

archive/issue_events_011047.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11047"
}
```



---

archive/issue_events_011048.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11048"
}
```



---

archive/issue_events_011049.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11049"
}
```



---

archive/issue_events_011050.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11050"
}
```



---

archive/issue_events_011051.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11051"
}
```



---

archive/issue_events_011052.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11052"
}
```



---

archive/issue_events_011053.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11053"
}
```



---

archive/issue_events_011054.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-05-13T11:25:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11054"
}
```



---

archive/issue_events_011055.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-05-13T11:25:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11055"
}
```



---

archive/issue_comments_036481.json:
```json
{
    "body": "Maybe we can close this ancient ticket now ?",
    "created_at": "2020-05-13T11:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4821#issuecomment-36481",
    "user": "https://github.com/fchapoton"
}
```

Maybe we can close this ancient ticket now ?



---

archive/issue_comments_036482.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-05-13T11:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4821#issuecomment-36482",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_036483.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-05-13T21:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4821#issuecomment-36483",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_011056.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-05-14T09:17:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4821#event-11056"
}
```



---

archive/issue_comments_036484.json:
```json
{
    "body": "thx",
    "created_at": "2020-05-14T09:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4821#issuecomment-36484",
    "user": "https://github.com/fchapoton"
}
```

thx



---

archive/issue_comments_036485.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-05-14T09:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4821#issuecomment-36485",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
