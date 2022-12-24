# Issue 9985: MPFI fails to build on AIX 5.3 - appears not to know .a is the extension for shared libraries on AIX

archive/issues_009985.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  cwitty@newtonlabs.com @fchapoton\n\nUsing the following system: \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1\n\nMPFI fails to build. The important part of the error message is:\n\n\n```\nchecking for gmp.h... yes\nchecking for valid GMP... yes\nchecking for mpfr.h... yes\nchecking MPFR library... configure: error: /home/users/drkirkby/sage-4.6.alpha1/local/lib/libmpfr.so or libmpfr.dylib not found\nError configuring mpfi\n\nreal    4m28.501s\nuser    0m52.337s\nsys     0m27.257s\nsage: An error occurred while installing mpfi-1.3.4-cvs20071125.p8\n```\n\n\nThe extension for shared libraries on AIX is .a - not .so or .dylib.\n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/9986\n\n",
    "created_at": "2010-09-23T21:00:39Z",
    "labels": [
        "porting: AIX or HP-UX",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "MPFI fails to build on AIX 5.3 - appears not to know .a is the extension for shared libraries on AIX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9985",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  cwitty@newtonlabs.com @fchapoton

Using the following system: 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* sage-4.6.alpha1

MPFI fails to build. The important part of the error message is:


```
checking for gmp.h... yes
checking for valid GMP... yes
checking for mpfr.h... yes
checking MPFR library... configure: error: /home/users/drkirkby/sage-4.6.alpha1/local/lib/libmpfr.so or libmpfr.dylib not found
Error configuring mpfi

real    4m28.501s
user    0m52.337s
sys     0m27.257s
sage: An error occurred while installing mpfi-1.3.4-cvs20071125.p8
```


The extension for shared libraries on AIX is .a - not .so or .dylib.

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/9986





---

archive/issue_comments_100333.json:
```json
{
    "body": "Attachment [mpfi-1.3.4-cvs20071125.p8.log](tarball://root/attachments/some-uuid/ticket9986/mpfi-1.3.4-cvs20071125.p8.log) by drkirkby created at 2010-09-23 21:01:25\n\nBuild failure observed on an RS/6000 running AIX 5.3",
    "created_at": "2010-09-23T21:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100333",
    "user": "drkirkby"
}
```

Attachment [mpfi-1.3.4-cvs20071125.p8.log](tarball://root/attachments/some-uuid/ticket9986/mpfi-1.3.4-cvs20071125.p8.log) by drkirkby created at 2010-09-23 21:01:25

Build failure observed on an RS/6000 running AIX 5.3



---

archive/issue_comments_100334.json:
```json
{
    "body": "Could you give MPFI's latest svn a try (outside of sage, I mean)?\n\nI have looked at their latest sources just this morning, and it looked pretty good ; but I have no AIX box and only read the configure.ac...",
    "created_at": "2011-05-02T11:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100334",
    "user": "Snark"
}
```

Could you give MPFI's latest svn a try (outside of sage, I mean)?

I have looked at their latest sources just this morning, and it looked pretty good ; but I have no AIX box and only read the configure.ac...



---

archive/issue_comments_100335.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-05-02T11:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100335",
    "user": "Snark"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_100336.json:
```json
{
    "body": "Replying to [comment:1 Snark]:\n> Could you give MPFI's latest svn a try (outside of sage, I mean)?\n> \n> I have looked at their latest sources just this morning, and it looked pretty good ; but I have no AIX box and only read the configure.ac...\n\nSure, my AIX box is not on now, but I'll try later. \n\nI later found out that .so is a permitted extension for the libraries on AIX, though all the systems libraries are .a. It appears the .a files can have both static and shared objects in the same library - I don't fully understand it, and are no AIX guru. I just have an old machine I bought long ago to ensure my code was portable. \n\nI'll give the svn a go later today after I've woke up properly and powered up the RS/6000. \n\nBTW, I'm not sure if you are an MPFI developer, but if so, and the latest svn does not work, you are welcome to have an account on the AIX box to try. Either way, on AIX, I think it would be useful if you permitted the .a extension too. \n\n\nDave",
    "created_at": "2011-05-03T06:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100336",
    "user": "drkirkby"
}
```

Replying to [comment:1 Snark]:
> Could you give MPFI's latest svn a try (outside of sage, I mean)?
> 
> I have looked at their latest sources just this morning, and it looked pretty good ; but I have no AIX box and only read the configure.ac...

Sure, my AIX box is not on now, but I'll try later. 

I later found out that .so is a permitted extension for the libraries on AIX, though all the systems libraries are .a. It appears the .a files can have both static and shared objects in the same library - I don't fully understand it, and are no AIX guru. I just have an old machine I bought long ago to ensure my code was portable. 

I'll give the svn a go later today after I've woke up properly and powered up the RS/6000. 

BTW, I'm not sure if you are an MPFI developer, but if so, and the latest svn does not work, you are welcome to have an account on the AIX box to try. Either way, on AIX, I think it would be useful if you permitted the .a extension too. 


Dave



---

archive/issue_comments_100337.json:
```json
{
    "body": "Replying to [comment:1 Snark]:\n> Could you give MPFI's latest svn a try (outside of sage, I mean)?\n\nCan you please give me the command to get the latest svn snapshot. I tried googling, but can only find links to download stable versions, not snapshots. \n\nDave",
    "created_at": "2011-05-03T06:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100337",
    "user": "drkirkby"
}
```

Replying to [comment:1 Snark]:
> Could you give MPFI's latest svn a try (outside of sage, I mean)?

Can you please give me the command to get the latest svn snapshot. I tried googling, but can only find links to download stable versions, not snapshots. 

Dave



---

archive/issue_comments_100338.json:
```json
{
    "body": "I'm not an MPFI developper -- I just looked at it because I have things to do within sage which require good quality packages (from a portability point of view).\n\nThis will get you their most up-to-date sources :\nsvn checkout svn://scm.gforge.inria.fr/svn/mpfi/trunk/mpfi mpfi\n\nNotice that as it isn't a proper snapshot but the raw code, you'll need to run ./autogen.sh, then make -- the ./autogen.sh step will build and run the configure script.\n\nHope this helps.",
    "created_at": "2011-05-03T07:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100338",
    "user": "Snark"
}
```

I'm not an MPFI developper -- I just looked at it because I have things to do within sage which require good quality packages (from a portability point of view).

This will get you their most up-to-date sources :
svn checkout svn://scm.gforge.inria.fr/svn/mpfi/trunk/mpfi mpfi

Notice that as it isn't a proper snapshot but the raw code, you'll need to run ./autogen.sh, then make -- the ./autogen.sh step will build and run the configure script.

Hope this helps.



---

archive/issue_comments_100339.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100339",
    "user": "@embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100340.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100340",
    "user": "@mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_100341.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100341",
    "user": "@mkoeppe"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_100342.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9985#issuecomment-100342",
    "user": "@fchapoton"
}
```

Resolution: invalid
