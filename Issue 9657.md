# Issue 9657: cvxopt 0.9 does not compile on Solaris with gcc 4.5 or later.

archive/issues_009657.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jhpalmieri @dimpase @jaapspies @qed777\n\nThere's a problem with cvxopt not building on gcc versions 4.5.0 or later. This has become especially critical lately, as only gcc 4.5.0 is available on Skynet, so this effecitvely means Sage can not be built on any Skynet computer running Solaris (*mark*, *mark2* or *fulvia*)\n\nHere's an example with OpenSolaris with gcc 4.5.0, though the same problem occurs on Solaris 10 SPARC and Solaris 10 x86. \n\n```\ndrkirkby@hawk:~/sage-4.5.1$ ./sage -f cvxopt-0.9.p8\n\n<snip>\n\ngcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.5.1/local/include/python2.6 -c C/base.c -o build/temp.solaris-2.11-i86pc-2.6/C/base.o\nIn file included from C/cvxopt.h:30:0,\n                 from C/base.c:23:\nC/sun_complex.h:9:0: warning: ignoring #pragma ident \nC/sun_complex.h:30:32: error: expected identifier or '(' before '_Imaginary'\nerror: command 'gcc' failed with exit status 1\n\nreal\t0m0.131s\nuser\t0m0.080s\nsys\t0m0.042s\nsage: An error occurred while installing cvxopt-0.9.p8\n```\n\nThis is ultimately due to `_Complex_I` being undefined - exactly the same problem which was observed in the Sage library several months ago - see #7932. \n\nThis patch defines `_Complex_I` to be `1j` on Solaris with gcc versions prior to 4.5.0. \n\nWith this change, cvxopt builds properly \n\n```\nrunning install_egg_info\nRemoving /export/home/drkirkby/sage-4.5.1/local/lib/python2.6/site-packages/cvxopt-0.9-py2.6.egg-info\nWriting /export/home/drkirkby/sage-4.5.1/local/lib/python2.6/site-packages/cvxopt-0.9-py2.6.egg-info\n\nreal\t0m45.306s\nuser\t0m40.395s\nsys\t0m3.786s\nSuccessfully installed cvxopt-0.9.p9\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.5.1/spkg/build/cvxopt-0.9.p9\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\n```\n\n**The patch is only applied on Solaris, so is very safe.**\n\nIssue created by migration from https://trac.sagemath.org/ticket/9657\n\n",
    "created_at": "2010-08-01T03:21:39Z",
    "labels": [
        "component: porting: solaris",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "cvxopt 0.9 does not compile on Solaris with gcc 4.5 or later.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9657",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jhpalmieri @dimpase @jaapspies @qed777

There's a problem with cvxopt not building on gcc versions 4.5.0 or later. This has become especially critical lately, as only gcc 4.5.0 is available on Skynet, so this effecitvely means Sage can not be built on any Skynet computer running Solaris (*mark*, *mark2* or *fulvia*)

Here's an example with OpenSolaris with gcc 4.5.0, though the same problem occurs on Solaris 10 SPARC and Solaris 10 x86. 

```
drkirkby@hawk:~/sage-4.5.1$ ./sage -f cvxopt-0.9.p8

<snip>

gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.5.1/local/include/python2.6 -c C/base.c -o build/temp.solaris-2.11-i86pc-2.6/C/base.o
In file included from C/cvxopt.h:30:0,
                 from C/base.c:23:
C/sun_complex.h:9:0: warning: ignoring #pragma ident 
C/sun_complex.h:30:32: error: expected identifier or '(' before '_Imaginary'
error: command 'gcc' failed with exit status 1

real	0m0.131s
user	0m0.080s
sys	0m0.042s
sage: An error occurred while installing cvxopt-0.9.p8
```

This is ultimately due to `_Complex_I` being undefined - exactly the same problem which was observed in the Sage library several months ago - see #7932. 

This patch defines `_Complex_I` to be `1j` on Solaris with gcc versions prior to 4.5.0. 

With this change, cvxopt builds properly 

```
running install_egg_info
Removing /export/home/drkirkby/sage-4.5.1/local/lib/python2.6/site-packages/cvxopt-0.9-py2.6.egg-info
Writing /export/home/drkirkby/sage-4.5.1/local/lib/python2.6/site-packages/cvxopt-0.9-py2.6.egg-info

real	0m45.306s
user	0m40.395s
sys	0m3.786s
Successfully installed cvxopt-0.9.p9
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.5.1/spkg/build/cvxopt-0.9.p9
Making Sage/Python scripts relocatable...
Making script relocatable
```

**The patch is only applied on Solaris, so is very safe.**

Issue created by migration from https://trac.sagemath.org/ticket/9657





---

archive/issue_comments_093576.json:
```json
{
    "body": "Attachment [9657.patch](tarball://root/attachments/some-uuid/ticket9657/9657.patch) by drkirkby created at 2010-08-01 07:43:53\n\nMercurial patch to allow cvxopt to build with gcc 4.5.0 and later",
    "created_at": "2010-08-01T07:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93576",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9657.patch](tarball://root/attachments/some-uuid/ticket9657/9657.patch) by drkirkby created at 2010-08-01 07:43:53

Mercurial patch to allow cvxopt to build with gcc 4.5.0 and later



---

archive/issue_comments_093577.json:
```json
{
    "body": "A copy of the package may be found here \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/cvxopt-0.9.p9.spkg\n\nAn update of cvxopt be made (#6456), that is waiting on a new upstream release, so it will not be  practical, as this is critical but very small fix. \n\nDave",
    "created_at": "2010-08-01T07:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93577",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

A copy of the package may be found here 

http://boxen.math.washington.edu/home/kirkby/patches/cvxopt-0.9.p9.spkg

An update of cvxopt be made (#6456), that is waiting on a new upstream release, so it will not be  practical, as this is critical but very small fix. 

Dave



---

archive/issue_comments_093578.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-01T08:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93578",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093579.json:
```json
{
    "body": "So the bug has been fixed in gcc 4.5.0, but not the \"more recent\" gcc versions 4.4.4 and 4.3.5? (I see you've tested the patch successfully with gcc 4.4.4 on OpenSolaris, and\n\n```C\n        #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )\n```\nobviously holds for that version.)",
    "created_at": "2010-08-01T14:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93579",
    "user": "https://github.com/nexttime"
}
```

So the bug has been fixed in gcc 4.5.0, but not the "more recent" gcc versions 4.4.4 and 4.3.5? (I see you've tested the patch successfully with gcc 4.4.4 on OpenSolaris, and

```C
        #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )
```
obviously holds for that version.)



---

archive/issue_comments_093580.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> So the bug has been fixed in gcc 4.5.0, but not the \"more recent\" gcc versions 4.4.4 and 4.3.5? \n\n\nYes, it has not been backported to the 4.3 or 4.4 series. Whether it ever will or not is another matter, but so far it has not. \n\nhttp://gcc.gnu.org/bugzilla/show_bug.cgi?id=42753\n\n> (I see you've tested the patch successfully with gcc 4.4.4 on OpenSolaris, and\n> \n> ```\n> #!C\n>         #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )\n> ```\n> obviously holds for that version.)\n\n\nI also tested on gcc 4.4.1 on 't2.math' - i.e. Solaris 10. \n\nAt http://trac.sagemath.org/sage_trac/ticket/6456#comment:85 \n\nI show the results from compiling a test program on a wide range (11 different bits of hardware) under about 25 different conditions (compiler versions). In each case, the bug is see in the 4.3 and 4.4 series, but not in 4.5. \n\n\nDave",
    "created_at": "2010-08-01T15:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93580",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:6 leif]:
> So the bug has been fixed in gcc 4.5.0, but not the "more recent" gcc versions 4.4.4 and 4.3.5? 


Yes, it has not been backported to the 4.3 or 4.4 series. Whether it ever will or not is another matter, but so far it has not. 

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42753

> (I see you've tested the patch successfully with gcc 4.4.4 on OpenSolaris, and
> 
> ```
> #!C
>         #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )
> ```
> obviously holds for that version.)


I also tested on gcc 4.4.1 on 't2.math' - i.e. Solaris 10. 

At http://trac.sagemath.org/sage_trac/ticket/6456#comment:85 

I show the results from compiling a test program on a wide range (11 different bits of hardware) under about 25 different conditions (compiler versions). In each case, the bug is see in the 4.3 and 4.4 series, but not in 4.5. 


Dave



---

archive/issue_comments_093581.json:
```json
{
    "body": "Ok, I was just wondering...\n\nI think somebody more involved with SunOS should give this positive review though. ;-)",
    "created_at": "2010-08-01T17:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93581",
    "user": "https://github.com/nexttime"
}
```

Ok, I was just wondering...

I think somebody more involved with SunOS should give this positive review though. ;-)



---

archive/issue_comments_093582.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Ok, I was just wondering...\n> \n> I think somebody more involved with SunOS should give this positive review though. ;-)\n> \n> \n\n\nPerhaps John can try \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/cvxopt-0.9.p9.spkg\n\nI could attach build logs if it would convince you more! \n\nDave",
    "created_at": "2010-08-01T17:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93582",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:8 leif]:
> Ok, I was just wondering...
> 
> I think somebody more involved with SunOS should give this positive review though. ;-)
> 
> 


Perhaps John can try 

http://boxen.math.washington.edu/home/kirkby/patches/cvxopt-0.9.p9.spkg

I could attach build logs if it would convince you more! 

Dave



---

archive/issue_comments_093583.json:
```json
{
    "body": "I'm currently trying to build on mark, mark2, fulvia, and t2 (and also on a few non-solaris machines just to be safe, although I can't see how this patch would have any effect on those machines).  I'm building sage-4.5.2.rc0 from scratch using this spkg, so it will take a while.",
    "created_at": "2010-08-01T17:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93583",
    "user": "https://github.com/jhpalmieri"
}
```

I'm currently trying to build on mark, mark2, fulvia, and t2 (and also on a few non-solaris machines just to be safe, although I can't see how this patch would have any effect on those machines).  I'm building sage-4.5.2.rc0 from scratch using this spkg, so it will take a while.



---

archive/issue_comments_093584.json:
```json
{
    "body": "Replying to [comment:9 drkirkby]:\n> I could attach build logs if it would convince you more! \n\n\nIt's not that I wasn't convinced this will work, but others are more competent here.\n\nI see \"workhorse John\" is already at reviewing it... :)",
    "created_at": "2010-08-01T17:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93584",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:9 drkirkby]:
> I could attach build logs if it would convince you more! 


It's not that I wasn't convinced this will work, but others are more competent here.

I see "workhorse John" is already at reviewing it... :)



---

archive/issue_comments_093585.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-02T04:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93585",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093586.json:
```json
{
    "body": "This builds successfully on t2, mark, mark2, and fulvia (both 32-bit and 64-bit, as far as I can tell).  The patch clearly only makes a difference on Solaris machines.",
    "created_at": "2010-08-02T04:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93586",
    "user": "https://github.com/jhpalmieri"
}
```

This builds successfully on t2, mark, mark2, and fulvia (both 32-bit and 64-bit, as far as I can tell).  The patch clearly only makes a difference on Solaris machines.



---

archive/issue_comments_093587.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-08-02T08:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93587",
    "user": "https://github.com/qed777"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_093588.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-04T02:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9657#issuecomment-93588",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024094.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-04T02:10:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9657",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9657#event-24094"
}
```
