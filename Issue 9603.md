# Issue 9603: Build iconv in parallel, install it on HP-UX and make it work properly on Solaris 64-bit.

archive/issues_009603.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @peterjeremy mvngu @qed777\n\nThis patch, which started out with the sole intension of building iconv on HP-UX, with a very trivial change, now has a number of  changes to generally improve the package. \n\n* Use `$MAKE` instead of `make` to permit parallel builds. \n* Install `iconv` on HP-UX in addition to Solaris and Cygwin.\n* Make this build properly 64-bit on all versions of Solaris and OpenSolaris - prior to this, there was a problem on some systems - see #9718.\n* A cleanup of spkg-install, spkg-check and SPKG.txt was also undertaken. \n\nDave\n\n---\n\n**Final spkg: http://spkg-upload.googlecode.com/files/iconv-1.13.1.p3.spkg**\n\n(All three reviewer patches applied.)\n\n```sh\n$ md5sum iconv-1.13.1.p3.spkg\naa4fd0c04699b806f8a60da64812d792  iconv-1.13.1.p3.spkg\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9603\n\n",
    "closed_at": "2010-09-16T00:48:49Z",
    "created_at": "2010-07-26T13:33:05Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Build iconv in parallel, install it on HP-UX and make it work properly on Solaris 64-bit.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9603",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @peterjeremy mvngu @qed777

This patch, which started out with the sole intension of building iconv on HP-UX, with a very trivial change, now has a number of  changes to generally improve the package. 

* Use `$MAKE` instead of `make` to permit parallel builds. 
* Install `iconv` on HP-UX in addition to Solaris and Cygwin.
* Make this build properly 64-bit on all versions of Solaris and OpenSolaris - prior to this, there was a problem on some systems - see #9718.
* A cleanup of spkg-install, spkg-check and SPKG.txt was also undertaken. 

Dave

---

**Final spkg: http://spkg-upload.googlecode.com/files/iconv-1.13.1.p3.spkg**

(All three reviewer patches applied.)

```sh
$ md5sum iconv-1.13.1.p3.spkg
aa4fd0c04699b806f8a60da64812d792  iconv-1.13.1.p3.spkg
```


Issue created by migration from https://trac.sagemath.org/ticket/9603





---

archive/issue_comments_092797.json:
```json
{
    "body": "Here we can see all tests pass on HP-UX. It should also be clear the changes only effect HP-UX and will have no effect on other platforms. \n\n```\n-bash-4.0$ uname -a\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n\n-bash-4.0$ ./sage -f iconv-1.13.1.p3\n\n<snip>\n\n./check-translit . Quotes UTF-8 ASCII\n./check-translit . Translit1 ISO-8859-1 ASCII\n./check-translitfailure . TranslitFail1 ISO-8859-1 ASCII\n./check-subst\n./test-shiftseq\nmake[1]: Leaving directory `/home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3/src/tests'\nAll the tests for iconv passed\nNow cleaning up tmp files.\n```",
    "created_at": "2010-07-26T14:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92797",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Here we can see all tests pass on HP-UX. It should also be clear the changes only effect HP-UX and will have no effect on other platforms. 

```
-bash-4.0$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license

-bash-4.0$ ./sage -f iconv-1.13.1.p3

<snip>

./check-translit . Quotes UTF-8 ASCII
./check-translit . Translit1 ISO-8859-1 ASCII
./check-translitfailure . TranslitFail1 ISO-8859-1 ASCII
./check-subst
./test-shiftseq
make[1]: Leaving directory `/home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3/src/tests'
All the tests for iconv passed
Now cleaning up tmp files.
```



---

archive/issue_comments_092798.json:
```json
{
    "body": "Mercurial patch to force iconv to build on HP-UX  in addition to the Solaris and Cygwin it currently builds on. iconv passes all tests on HP-UX. The changes will have no effect on other platforms.",
    "created_at": "2010-07-26T14:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92798",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch to force iconv to build on HP-UX  in addition to the Solaris and Cygwin it currently builds on. iconv passes all tests on HP-UX. The changes will have no effect on other platforms.



---

archive/issue_comments_092799.json:
```json
{
    "body": "Attachment [9603.patch](tarball://root/attachments/some-uuid/ticket9603/9603.patch) by drkirkby created at 2010-07-26 14:11:08",
    "created_at": "2010-07-26T14:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92799",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9603.patch](tarball://root/attachments/some-uuid/ticket9603/9603.patch) by drkirkby created at 2010-07-26 14:11:08



---

archive/issue_comments_092800.json:
```json
{
    "body": "The package may be found here. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n\nI'd appreciate a review. I realise not many people have access to HP-UX, but it should be apparent this will affect no other platform. \n\nDave",
    "created_at": "2010-07-26T21:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92800",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The package may be found here. 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

I'd appreciate a review. I realise not many people have access to HP-UX, but it should be apparent this will affect no other platform. 

Dave



---

archive/issue_comments_092801.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-26T21:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92801",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092802.json:
```json
{
    "body": "I am unable to test on HP-UX but visual inspection of the diffs between iconv-1.13.1.p2.spkg and http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg looks correct.  Running both spkg-install and spkg-check on FreeBSD behave as expected.",
    "created_at": "2010-07-26T23:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92802",
    "user": "https://github.com/peterjeremy"
}
```

I am unable to test on HP-UX but visual inspection of the diffs between iconv-1.13.1.p2.spkg and http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg looks correct.  Running both spkg-install and spkg-check on FreeBSD behave as expected.



---

archive/issue_comments_092803.json:
```json
{
    "body": "Replying to [comment:5 pjeremy]:\n> I am unable to test on HP-UX but visual inspection of the diffs between iconv-1.13.1.p2.spkg and http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg looks correct.  Running both spkg-install and spkg-check on FreeBSD behave as expected.\n\n\nThank you Peter. \n\nI'm attaching a log of an install on HP-UX. \n\nI also noticed that the message saying it was being installed since the OS was Solaris or Cygwin. I changed that message to:\n\n```\nInstalling iconv as the operating system is Cygwin, HP-UX or Solaris\n```\n\nDave",
    "created_at": "2010-07-27T09:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92803",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:5 pjeremy]:
> I am unable to test on HP-UX but visual inspection of the diffs between iconv-1.13.1.p2.spkg and http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg looks correct.  Running both spkg-install and spkg-check on FreeBSD behave as expected.


Thank you Peter. 

I'm attaching a log of an install on HP-UX. 

I also noticed that the message saying it was being installed since the OS was Solaris or Cygwin. I changed that message to:

```
Installing iconv as the operating system is Cygwin, HP-UX or Solaris
```

Dave



---

archive/issue_comments_092804.json:
```json
{
    "body": "Improve a message as the package installed, to mention HP-UX too.",
    "created_at": "2010-07-27T09:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92804",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Improve a message as the package installed, to mention HP-UX too.



---

archive/issue_comments_092805.json:
```json
{
    "body": "Attachment [9603-informative-message-correction.patch](tarball://root/attachments/some-uuid/ticket9603/9603-informative-message-correction.patch) by drkirkby created at 2010-07-27 17:49:51\n\nBuild log from a HP C3600 running HP-UX. Note SAGE_CHECK was set to \"yes\" so the self tests were run. They all pass",
    "created_at": "2010-07-27T17:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92805",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9603-informative-message-correction.patch](tarball://root/attachments/some-uuid/ticket9603/9603-informative-message-correction.patch) by drkirkby created at 2010-07-27 17:49:51

Build log from a HP C3600 running HP-UX. Note SAGE_CHECK was set to "yes" so the self tests were run. They all pass



---

archive/issue_comments_092806.json:
```json
{
    "body": "Attachment [HP-UX-install.log](tarball://root/attachments/some-uuid/ticket9603/HP-UX-install.log) by drkirkby created at 2010-07-27 18:23:48",
    "created_at": "2010-07-27T18:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92806",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [HP-UX-install.log](tarball://root/attachments/some-uuid/ticket9603/HP-UX-install.log) by drkirkby created at 2010-07-27 18:23:48



---

archive/issue_comments_092807.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-07-27T18:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92807",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_092808.json:
```json
{
    "body": "Style-wise, I would invert the test to something like:\n\n```sh\nif [ \"$UNAME\" = SunOS -o \"$UNAME\" = CYGWIN -o \"$UNAME\" = HP-UX ]; then\n\n    # install spkg/run test suite, check exit code, ...\n\nelse\n\n    # print message that iconv will not be installed/tested\n    # because *the system's* one is/will be used (rather than\n    # the one shipped with Sage), exit 0\n\nfi\n```\n(I.e., clarifying the messages a bit, too.)\n\n\nDave, you're right, I do not have access to an HP-UX system, but I don't think that's necessary to give it a positive review.\n\n\nI'll later take a look at the whole...\n\n\n-Leif\n\nP.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?",
    "created_at": "2010-07-27T19:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92808",
    "user": "https://github.com/nexttime"
}
```

Style-wise, I would invert the test to something like:

```sh
if [ "$UNAME" = SunOS -o "$UNAME" = CYGWIN -o "$UNAME" = HP-UX ]; then

    # install spkg/run test suite, check exit code, ...

else

    # print message that iconv will not be installed/tested
    # because *the system's* one is/will be used (rather than
    # the one shipped with Sage), exit 0

fi
```
(I.e., clarifying the messages a bit, too.)


Dave, you're right, I do not have access to an HP-UX system, but I don't think that's necessary to give it a positive review.


I'll later take a look at the whole...


-Leif

P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?



---

archive/issue_comments_092809.json:
```json
{
    "body": "```\n...\nNow cleaning up tmp files.\nrm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory\nMaking Sage/Python scripts relocatable...\n...\n```\n\nYet another `sage-spkg` bug... :|",
    "created_at": "2010-07-27T20:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92809",
    "user": "https://github.com/nexttime"
}
```

```
...
Now cleaning up tmp files.
rm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory
Making Sage/Python scripts relocatable...
...
```

Yet another `sage-spkg` bug... :|



---

archive/issue_comments_092810.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Style-wise, I would invert the test to something like:\n> \n> ```\n> #!sh\n> if [ \"$UNAME\" = SunOS -o \"$UNAME\" = CYGWIN -o \"$UNAME\" = HP-UX ]; then\n> \n>     # install spkg/run test suite, check exit code, ...\n> \n> else\n> \n>     # print message that iconv will not be installed/tested\n>     # because *the system's* one is/will be used (rather than\n>     # the one shipped with Sage), exit 0\n> \n> fi\n> ```\n> (I.e., clarifying the messages a bit, too.)\n> \n> \n> Dave, you're right, I do not have access to an HP-UX system, but I don't think that's necessary to give it a positive review.\n> \n> \n> I'll later take a look at the whole...\n> \n> \n> -Leif\n> \n> P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?\n\n\nI try to write my scripts as portable as I possibly can. I've tended to ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics) where some shell scripting wizards hang out. I've just asked [for comment on -o vs ||](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/4081999fef86b878#)\n\nIt's true that for the bash shell, either `-o` or `||` will work, but there are a number of older shells which don't behave well in such circumstances. `||` is more portable than `-o`, and `&&` is more portable than `-a`. Likewise testing for `\"\"` causes problems with some shells. I think the problems usually occur if there is more than one -o or -a on a line, which is what is needed here. I try to write my scripts which will work with any shell, though I stick `#!/usr/bin/env bash` at the top to be consistent with the rest of Sage. \n\nChanging the style introduces risks that I'd rather not introduce. The risk of introducing a bug increases the more changes one makes to the script. I would not be very popular if I tried to implement something for HP-UX that happens to break on some Linux system! At the moment the script does work reliably, so I'd prefer to limit the changes that are necessary to achieve the aim. \n\nI've tested this on Solaris, HP-UX and Linux. Peter has checked it on FreeBSD. If the style of the script is changed, so that testing needs to be repeated. \n\nThe top of spkg-install has a description of what it is doing, and a link to the ticket which resulted in the decision to make iconv install only on Solaris and Cygwing, so I'm not really sure there is need for further explanation. \n\nIf you feel there needs to be some more comments in the code, I will add them. But I do not feel changing the style is a good idea. It introduces unnecessary risks. \n\nPerhaps Peter has some comments on this. \n\nThere's no need to delete Peter as a reviewer, as he has provided valuable input. \n\nDave",
    "created_at": "2010-07-27T21:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92810",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:8 leif]:
> Style-wise, I would invert the test to something like:
> 
> ```
> #!sh
> if [ "$UNAME" = SunOS -o "$UNAME" = CYGWIN -o "$UNAME" = HP-UX ]; then
> 
>     # install spkg/run test suite, check exit code, ...
> 
> else
> 
>     # print message that iconv will not be installed/tested
>     # because *the system's* one is/will be used (rather than
>     # the one shipped with Sage), exit 0
> 
> fi
> ```
> (I.e., clarifying the messages a bit, too.)
> 
> 
> Dave, you're right, I do not have access to an HP-UX system, but I don't think that's necessary to give it a positive review.
> 
> 
> I'll later take a look at the whole...
> 
> 
> -Leif
> 
> P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?


I try to write my scripts as portable as I possibly can. I've tended to ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics) where some shell scripting wizards hang out. I've just asked [for comment on -o vs ||](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/4081999fef86b878#)

It's true that for the bash shell, either `-o` or `||` will work, but there are a number of older shells which don't behave well in such circumstances. `||` is more portable than `-o`, and `&&` is more portable than `-a`. Likewise testing for `""` causes problems with some shells. I think the problems usually occur if there is more than one -o or -a on a line, which is what is needed here. I try to write my scripts which will work with any shell, though I stick `#!/usr/bin/env bash` at the top to be consistent with the rest of Sage. 

Changing the style introduces risks that I'd rather not introduce. The risk of introducing a bug increases the more changes one makes to the script. I would not be very popular if I tried to implement something for HP-UX that happens to break on some Linux system! At the moment the script does work reliably, so I'd prefer to limit the changes that are necessary to achieve the aim. 

I've tested this on Solaris, HP-UX and Linux. Peter has checked it on FreeBSD. If the style of the script is changed, so that testing needs to be repeated. 

The top of spkg-install has a description of what it is doing, and a link to the ticket which resulted in the decision to make iconv install only on Solaris and Cygwing, so I'm not really sure there is need for further explanation. 

If you feel there needs to be some more comments in the code, I will add them. But I do not feel changing the style is a good idea. It introduces unnecessary risks. 

Perhaps Peter has some comments on this. 

There's no need to delete Peter as a reviewer, as he has provided valuable input. 

Dave



---

archive/issue_comments_092811.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> {{{\n> ...\n> Now cleaning up tmp files.\n> rm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory\n> Making Sage/Python scripts relocatable...\n> ...\n> }}}\n> \n> Yet another `sage-spkg` bug... :|\n\n\nYes, I've seen endless messages about being unable to delete the current directory. This is another instance where one would need to be very careful in changing things. Fixing the bug might actually introduce a bug. Adding a -f just hides the problem. I don't really know the answer to this. \n\nI see this on both Solaris and HP-UX - can't recall if that warning is printed on Linux or not. \n\nDave",
    "created_at": "2010-07-27T21:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92811",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:9 leif]:
> {{{
> ...
> Now cleaning up tmp files.
> rm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory
> Making Sage/Python scripts relocatable...
> ...
> }}}
> 
> Yet another `sage-spkg` bug... :|


Yes, I've seen endless messages about being unable to delete the current directory. This is another instance where one would need to be very careful in changing things. Fixing the bug might actually introduce a bug. Adding a -f just hides the problem. I don't really know the answer to this. 

I see this on both Solaris and HP-UX - can't recall if that warning is printed on Linux or not. 

Dave



---

archive/issue_comments_092812.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> Replying to [comment:9 leif]:\n\n{{{\n...\nNow cleaning up tmp files.\nrm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory\nMaking Sage/Python scripts relocatable...\n...\n}}}\n> > \n> > Yet another `sage-spkg` bug... :|\n\n> \n> Yes, I've seen endless messages about being unable to delete the current directory.\n\n\nThis **must** happen on any system...\n\n> This is another instance where one would need to be very careful in changing things. Fixing the bug might actually introduce a bug. Adding a -f just hides the problem. I don't really know the answer to this.\n\n\nNo, the fix is harmless. The solution is not to add `-f` (it is already `-rf` btw), but to `cd ..` before doing so. (It seems somebody added the `cd $BASEDIR` later without looking at all the code below it.)\n\n> I see this on both Solaris and HP-UX - can't recall if that warning is printed on Linux or not. \n\n\nSee above, it's a \"must have\" :)",
    "created_at": "2010-07-27T22:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92812",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 drkirkby]:
> Replying to [comment:9 leif]:

{{{
...
Now cleaning up tmp files.
rm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory
Making Sage/Python scripts relocatable...
...
}}}
> > 
> > Yet another `sage-spkg` bug... :|

> 
> Yes, I've seen endless messages about being unable to delete the current directory.


This **must** happen on any system...

> This is another instance where one would need to be very careful in changing things. Fixing the bug might actually introduce a bug. Adding a -f just hides the problem. I don't really know the answer to this.


No, the fix is harmless. The solution is not to add `-f` (it is already `-rf` btw), but to `cd ..` before doing so. (It seems somebody added the `cd $BASEDIR` later without looking at all the code below it.)

> I see this on both Solaris and HP-UX - can't recall if that warning is printed on Linux or not. 


See above, it's a "must have" :)



---

archive/issue_comments_092813.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> See above, it's a \"must have\" :)\n\n\nOh, I think I lied. The `-f` seems to suppress the message on Linux.",
    "created_at": "2010-07-27T22:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92813",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:12 leif]:
> See above, it's a "must have" :)


Oh, I think I lied. The `-f` seems to suppress the message on Linux.



---

archive/issue_comments_092814.json:
```json
{
    "body": "Replying to [comment:10 drkirkby]:\n> Replying to [comment:8 leif]:\n> > P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?\n\n\nI completely missed his comment at that time, and did not notice he added his name himself there, sorry for that. (Though most tickets only list those as reviewers who actually gave *positive* review... - not a very good practice IMO.)\n\n> I try to write my scripts as portable as I possibly can. I've tended to ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics) where some shell scripting wizards hang out. I've just asked [for comment on -o vs ||](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/4081999fef86b878#)\n\n\nOf course a bit funny to both require `bash` and then try to be as portable as possible with respect to the shell (though `test` is actually a *program*, too), but I don't mind.\n\n> Changing the style introduces risks that I'd rather not introduce. The risk of introducing a bug increases the more changes one makes to the script. I would not be very popular if I tried to implement something for HP-UX that happens to break on some Linux system! At the moment the script does work reliably, so I'd prefer to limit the changes that are necessary to achieve the aim.\n\n\nHmm, my main intention was to just invert the test, because it's bad style (and inefficient and I think more error-prone) as it is now.\n\nOf course you can use `[ ... ] || [ ... ] || ...` as well, though this invokes more instances of `test` if it's not a shell built-in.\n\n> The top of spkg-install has a description of what it is doing, and a link to the ticket which resulted in the decision to make iconv install only on Solaris and Cygwing, so I'm not really sure there is need for further explanation.\n> If you feel there needs to be some more comments in the code, I will add them.\n\n\nI meant just the *messages* visible to the user. \n\n> But I do not feel changing the style is a good idea. It introduces unnecessary risks.\n\n\nSee above. Every code change of course carries some risk (cf. the garbage in PARI's `spkg-install`), but if tickets were always reviewed properly, such things would (or will) not happen. In my opinion cleaning up \"grown\" code is important, too. (And sometimes it's even better to rewrite things from scratch.)\n\n\n-Leif",
    "created_at": "2010-07-27T22:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92814",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:10 drkirkby]:
> Replying to [comment:8 leif]:
> > P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?


I completely missed his comment at that time, and did not notice he added his name himself there, sorry for that. (Though most tickets only list those as reviewers who actually gave *positive* review... - not a very good practice IMO.)

> I try to write my scripts as portable as I possibly can. I've tended to ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics) where some shell scripting wizards hang out. I've just asked [for comment on -o vs ||](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/4081999fef86b878#)


Of course a bit funny to both require `bash` and then try to be as portable as possible with respect to the shell (though `test` is actually a *program*, too), but I don't mind.

> Changing the style introduces risks that I'd rather not introduce. The risk of introducing a bug increases the more changes one makes to the script. I would not be very popular if I tried to implement something for HP-UX that happens to break on some Linux system! At the moment the script does work reliably, so I'd prefer to limit the changes that are necessary to achieve the aim.


Hmm, my main intention was to just invert the test, because it's bad style (and inefficient and I think more error-prone) as it is now.

Of course you can use `[ ... ] || [ ... ] || ...` as well, though this invokes more instances of `test` if it's not a shell built-in.

> The top of spkg-install has a description of what it is doing, and a link to the ticket which resulted in the decision to make iconv install only on Solaris and Cygwing, so I'm not really sure there is need for further explanation.
> If you feel there needs to be some more comments in the code, I will add them.


I meant just the *messages* visible to the user. 

> But I do not feel changing the style is a good idea. It introduces unnecessary risks.


See above. Every code change of course carries some risk (cf. the garbage in PARI's `spkg-install`), but if tickets were always reviewed properly, such things would (or will) not happen. In my opinion cleaning up "grown" code is important, too. (And sometimes it's even better to rewrite things from scratch.)


-Leif



---

archive/issue_comments_092815.json:
```json
{
    "body": "> No, the fix is harmless. The solution is not to add -f (it is already -rf btw), but to cd .. before doing so.\n\n\nSee #9444.",
    "created_at": "2010-07-27T22:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92815",
    "user": "https://github.com/jhpalmieri"
}
```

> No, the fix is harmless. The solution is not to add -f (it is already -rf btw), but to cd .. before doing so.


See #9444.



---

archive/issue_comments_092816.json:
```json
{
    "body": "Change the style of the tests, in the light of comments from the reviewer.",
    "created_at": "2010-07-28T00:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92816",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Change the style of the tests, in the light of comments from the reviewer.



---

archive/issue_comments_092817.json:
```json
{
    "body": "Attachment [9603-cleanup.patch](tarball://root/attachments/some-uuid/ticket9603/9603-cleanup.patch) by drkirkby created at 2010-07-28 00:44:02\n\nI've changed the style of the tests somewhat, which will hopefully make the logic clearer. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n\nI've checked it on Solaris and Linux. It installs and passes the tests on Solaris, but does not install on Linux. On Linux it correctly reports that the tests will not be run. \n\nIs that better? \n\nDave",
    "created_at": "2010-07-28T00:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92817",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9603-cleanup.patch](tarball://root/attachments/some-uuid/ticket9603/9603-cleanup.patch) by drkirkby created at 2010-07-28 00:44:02

I've changed the style of the tests somewhat, which will hopefully make the logic clearer. 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

I've checked it on Solaris and Linux. It installs and passes the tests on Solaris, but does not install on Linux. On Linux it correctly reports that the tests will not be run. 

Is that better? 

Dave



---

archive/issue_comments_092818.json:
```json
{
    "body": "Replying to [comment:16 drkirkby]:\n> I've changed the style of the tests somewhat, which will hopefully make the logic clearer.\n\n\nYes, I like that. (Mike will perhaps not be amused by testing for HP-UX prior to Cygwin in `spkg-install`... ;-) )\n\nThere are some typos/grammatical flaws in the comments and messages.\n\nI'd prefer using `$UNAME` all the time (instead of in addition ``uname``).\n\n`CFLAGS` are overwritten when `$SAGE64=yes`.\n\nI'd use `$MAKE` instead of `make` (in both `spkg-check` and `spkg-install`). If parallel make should be disabled in some cases, I would then either do `$MAKE -j1 [target]` or `export MAKE=\"$MAKE -j1\" ; ... $MAKE [target]`.\n\nI've still not looked at the whole; I think I'll do tomorrow...",
    "created_at": "2010-07-28T01:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92818",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:16 drkirkby]:
> I've changed the style of the tests somewhat, which will hopefully make the logic clearer.


Yes, I like that. (Mike will perhaps not be amused by testing for HP-UX prior to Cygwin in `spkg-install`... ;-) )

There are some typos/grammatical flaws in the comments and messages.

I'd prefer using `$UNAME` all the time (instead of in addition ``uname``).

`CFLAGS` are overwritten when `$SAGE64=yes`.

I'd use `$MAKE` instead of `make` (in both `spkg-check` and `spkg-install`). If parallel make should be disabled in some cases, I would then either do `$MAKE -j1 [target]` or `export MAKE="$MAKE -j1" ; ... $MAKE [target]`.

I've still not looked at the whole; I think I'll do tomorrow...



---

archive/issue_comments_092819.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n\n> There are some typos/grammatical flaws in the comments and messages.\n> \n> I'd prefer using `$UNAME` all the time (instead of in addition ``uname``).\n> \n> `CFLAGS` are overwritten when `$SAGE64=yes`.\n> \n> I'd use `$MAKE` instead of `make` (in both `spkg-check` and `spkg-install`). If parallel make should be disabled in some cases, I would then either do `$MAKE -j1 [target]` or `export MAKE=\"$MAKE -j1\" ; ... $MAKE [target]`.\n> \n> I've still not looked at the whole; I think I'll do tomorrow...\n\n\nDid you get a chance to look at this? I'd rather fix all the problems at once. \n\nDave",
    "created_at": "2010-07-29T10:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92819",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:17 leif]:

> There are some typos/grammatical flaws in the comments and messages.
> 
> I'd prefer using `$UNAME` all the time (instead of in addition ``uname``).
> 
> `CFLAGS` are overwritten when `$SAGE64=yes`.
> 
> I'd use `$MAKE` instead of `make` (in both `spkg-check` and `spkg-install`). If parallel make should be disabled in some cases, I would then either do `$MAKE -j1 [target]` or `export MAKE="$MAKE -j1" ; ... $MAKE [target]`.
> 
> I've still not looked at the whole; I think I'll do tomorrow...


Did you get a chance to look at this? I'd rather fix all the problems at once. 

Dave



---

archive/issue_comments_092820.json:
```json
{
    "body": "Replying to [comment:18 drkirkby]:\n> Replying to [comment:17 leif]:\n> > I've still not looked at the whole; I think I'll do tomorrow...\n\n> Did you get a chance to look at this?\n\nNo, I'm sorry, not yet. It'll most probably get Saturday or Sunday.\n\n> I'd rather fix all the problems at once. \n\n\nYes, I understand that.",
    "created_at": "2010-07-29T18:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92820",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:18 drkirkby]:
> Replying to [comment:17 leif]:
> > I've still not looked at the whole; I think I'll do tomorrow...

> Did you get a chance to look at this?

No, I'm sorry, not yet. It'll most probably get Saturday or Sunday.

> I'd rather fix all the problems at once. 


Yes, I understand that.



---

archive/issue_comments_092821.json:
```json
{
    "body": "Replying to [comment:19 leif]:\n> Replying to [comment:18 drkirkby]:\n> > Replying to [comment:17 leif]:\n> > > I've still not looked at the whole; I think I'll do tomorrow...\n\n> > Did you get a chance to look at this?\n> \n> No, I'm sorry, not yet. It'll most probably get Saturday or Sunday.\n> \n> > I'd rather fix all the problems at once. \n\n> \n> Yes, I understand that.\n\n\nAny chance of you looking at this? I'd like to get it reviewed and out of the way. What was originally the change of about 50 bytes has now taken a long time! \n\nDave",
    "created_at": "2010-08-07T22:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92821",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:19 leif]:
> Replying to [comment:18 drkirkby]:
> > Replying to [comment:17 leif]:
> > > I've still not looked at the whole; I think I'll do tomorrow...

> > Did you get a chance to look at this?
> 
> No, I'm sorry, not yet. It'll most probably get Saturday or Sunday.
> 
> > I'd rather fix all the problems at once. 

> 
> Yes, I understand that.


Any chance of you looking at this? I'd like to get it reviewed and out of the way. What was originally the change of about 50 bytes has now taken a long time! 

Dave



---

archive/issue_comments_092822.json:
```json
{
    "body": "Unfortunately, I'd make *a lot* of changes (besides those I already mentioned), in different \"categories\", but most of them more or less important or of cosmetic nature.\n\nThe only actual change *to the code* is quoting all instances of `$SAGE_LOCAL`, for (far) future support of spaces in `$SAGE_ROOT`. (In addition, one *could* test if spaces in it would break `configure` or `make` etc.)\n\nIn random order:\n\n* Remove trailing whitespace (and a superfluous semicolon in `spkg-install` and `spkg-check`).\n  (I really hate such changes, since they make [cumulative] patches unreadable.)\n* `s/== iconv ==/= iconv =/` since it is the top-level heading.\n* Add blank lines below section headings. (I think this is common practice, and makes the plain text more readable.)\n* Move *\"For more details ...\"* to (new) *\"Upstream Contact\"* section.\n* The following is perhaps (partly) obsolete, but currently completely misleading:\n    *\"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv.*\n\n    *The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install.\"*\n  (In fact **nothing** is removed **after** `make install`. I don't think something has been removed from the upstream source tree; at least in `spkg-install` nothing gets removed (\"patched\") from that, and `configure` doesn't get any `--without-...` options or alike. In short, when updating the package, one should make sure all traces of *previous installations* of iconv still get removed *prior to [re]installation*. Otherwise some code has to be added to remove \"useless\" parts of iconv *from the Sage installation* **after** `make install`.)\n* One could add the usual *\"Building a 64-bit version of ...\"* message.\n* Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also \"layout\")...\n\nI've looked at the package yesterday, but I don't think I've forgotten something... ;-)",
    "created_at": "2010-08-10T14:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92822",
    "user": "https://github.com/nexttime"
}
```

Unfortunately, I'd make *a lot* of changes (besides those I already mentioned), in different "categories", but most of them more or less important or of cosmetic nature.

The only actual change *to the code* is quoting all instances of `$SAGE_LOCAL`, for (far) future support of spaces in `$SAGE_ROOT`. (In addition, one *could* test if spaces in it would break `configure` or `make` etc.)

In random order:

* Remove trailing whitespace (and a superfluous semicolon in `spkg-install` and `spkg-check`).
  (I really hate such changes, since they make [cumulative] patches unreadable.)
* `s/== iconv ==/= iconv =/` since it is the top-level heading.
* Add blank lines below section headings. (I think this is common practice, and makes the plain text more readable.)
* Move *"For more details ..."* to (new) *"Upstream Contact"* section.
* The following is perhaps (partly) obsolete, but currently completely misleading:
    *"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv.*

    *The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install."*
  (In fact **nothing** is removed **after** `make install`. I don't think something has been removed from the upstream source tree; at least in `spkg-install` nothing gets removed ("patched") from that, and `configure` doesn't get any `--without-...` options or alike. In short, when updating the package, one should make sure all traces of *previous installations* of iconv still get removed *prior to [re]installation*. Otherwise some code has to be added to remove "useless" parts of iconv *from the Sage installation* **after** `make install`.)
* One could add the usual *"Building a 64-bit version of ..."* message.
* Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also "layout")...

I've looked at the package yesterday, but I don't think I've forgotten something... ;-)



---

archive/issue_comments_092823.json:
```json
{
    "body": "P.S.: I tried to mark this ticket `# long time`, but that didn't work.\n\n(Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )",
    "created_at": "2010-08-10T14:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92823",
    "user": "https://github.com/nexttime"
}
```

P.S.: I tried to mark this ticket `# long time`, but that didn't work.

(Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )



---

archive/issue_comments_092824.json:
```json
{
    "body": "Replying to [comment:21 leif]:\n> Unfortunately, I'd make *a lot* of changes (besides those I already mentioned), in different \"categories\", but most of them more or less important or of cosmetic nature.\n\n\nBut those lots of changes should be on another ticket. They have nothing to do with fixing the HP-UX issue! \n\nAs you know, I am quite keen to improve the quality of Sage, so I will make them. But be aware I've tried to get people to make more important changes before, and William has overruled, saying that the patch fixes the problem it aims to fix, and that other changes should be on another ticket. \n\nI'll produce a new package in a day or so. \n\n> The only actual change *to the code* is quoting all instances of `$SAGE_LOCAL`, for (far) future support of spaces in `$SAGE_ROOT`. (In addition, one *could* test if spaces in it would break `configure` or `make` etc.)\n\n\n\nI'll try to make all changes. \n \n> In random order:\n> \n> * Remove trailing whitespace (and a superfluous semicolon in `spkg-install` and `spkg-check`).\n>   (I really hate such changes, since they make [cumulative] patches unreadable.)\n> * `s/== iconv ==/= iconv =/` since it is the top-level heading.\n> * Add blank lines below section headings. (I think this is common practice, and makes the plain text more readable.)\n> * Move *\"For more details ...\"* to (new) *\"Upstream Contact\"* section.\n> * The following is perhaps (partly) obsolete, but currently completely misleading:\n>     *\"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv.*\n\n\nThe point of that is that if you run `make install`, then run the package for a second time, it will clean out all the files made on a previous build. You can't do `make distclean` at that point as there's no makefile. But I'll remove that. \n \n>      *The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install.\"*\n\n>    (In fact **nothing** is removed **after** `make install`. I don't think something has been removed from the upstream source tree; at least in `spkg-install` nothing gets removed (\"patched\") from that, and `configure` doesn't get any `--without-...` options or alike. In short, when updating the package, one should make sure all traces of *previous installations* of iconv still get removed *prior to [re]installation*. Otherwise some code has to be added to remove \"useless\" parts of iconv *from the Sage installation* **after** `make install`.)\n\nNothing is removed. It was just a remark. I can remove it if you feel it causes confusion. \n\n>  * One could add the usual *\"Building a 64-bit version of ...\"* message.\n\n\nNo problem. \n\n>  * Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also \"layout\")...\n\n\nI'll try, but lets hope there are not too many itterations of this! \n \n> I've looked at the package yesterday, but I don't think I've forgotten something... ;-)",
    "created_at": "2010-08-10T15:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92824",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:21 leif]:
> Unfortunately, I'd make *a lot* of changes (besides those I already mentioned), in different "categories", but most of them more or less important or of cosmetic nature.


But those lots of changes should be on another ticket. They have nothing to do with fixing the HP-UX issue! 

As you know, I am quite keen to improve the quality of Sage, so I will make them. But be aware I've tried to get people to make more important changes before, and William has overruled, saying that the patch fixes the problem it aims to fix, and that other changes should be on another ticket. 

I'll produce a new package in a day or so. 

> The only actual change *to the code* is quoting all instances of `$SAGE_LOCAL`, for (far) future support of spaces in `$SAGE_ROOT`. (In addition, one *could* test if spaces in it would break `configure` or `make` etc.)



I'll try to make all changes. 
 
> In random order:
> 
> * Remove trailing whitespace (and a superfluous semicolon in `spkg-install` and `spkg-check`).
>   (I really hate such changes, since they make [cumulative] patches unreadable.)
> * `s/== iconv ==/= iconv =/` since it is the top-level heading.
> * Add blank lines below section headings. (I think this is common practice, and makes the plain text more readable.)
> * Move *"For more details ..."* to (new) *"Upstream Contact"* section.
> * The following is perhaps (partly) obsolete, but currently completely misleading:
>     *"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv.*


The point of that is that if you run `make install`, then run the package for a second time, it will clean out all the files made on a previous build. You can't do `make distclean` at that point as there's no makefile. But I'll remove that. 
 
>      *The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install."*

>    (In fact **nothing** is removed **after** `make install`. I don't think something has been removed from the upstream source tree; at least in `spkg-install` nothing gets removed ("patched") from that, and `configure` doesn't get any `--without-...` options or alike. In short, when updating the package, one should make sure all traces of *previous installations* of iconv still get removed *prior to [re]installation*. Otherwise some code has to be added to remove "useless" parts of iconv *from the Sage installation* **after** `make install`.)

Nothing is removed. It was just a remark. I can remove it if you feel it causes confusion. 

>  * One could add the usual *"Building a 64-bit version of ..."* message.


No problem. 

>  * Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also "layout")...


I'll try, but lets hope there are not too many itterations of this! 
 
> I've looked at the package yesterday, but I don't think I've forgotten something... ;-)



---

archive/issue_comments_092825.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-10T15:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92825",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092826.json:
```json
{
    "body": "Replying to [comment:22 leif]:\n> P.S.: I tried to mark this ticket `# long time`, but that didn't work.\n\n\nI'm not sure of what you mean there. \n\n> (Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )\n\n\nI realise that. Thanks for looking at the ticket - it's hard to get anyone to look at HP-UX tickets! \n\nHP-UX can be useful, since where there are problems on one platform but not another, it helps to get a third perspective of it. I'm not convinced there will ever be a complete HP-UX port. \n\nDave",
    "created_at": "2010-08-10T15:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92826",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:22 leif]:
> P.S.: I tried to mark this ticket `# long time`, but that didn't work.


I'm not sure of what you mean there. 

> (Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )


I realise that. Thanks for looking at the ticket - it's hard to get anyone to look at HP-UX tickets! 

HP-UX can be useful, since where there are problems on one platform but not another, it helps to get a third perspective of it. I'm not convinced there will ever be a complete HP-UX port. 

Dave



---

archive/issue_comments_092827.json:
```json
{
    "body": "Replying to [comment:23 drkirkby]:\n> Replying to [comment:21 leif]:\n> > Unfortunately, I'd make *a lot* of changes (besides those I already mentioned), in different \"categories\", but most of them more or less important or of cosmetic nature.\n\n> \n> But those lots of changes should be on another ticket. They have nothing to do with fixing the HP-UX issue!\n\n\nIf you don't emphasize/focus on HP-UX (i.e. e.g. add *\"improve iconv package\"*), perhaps more people will take a look at this ticket. :)\n\n> As you know, I am quite keen to improve the quality of Sage, so I will make them. But be aware I've tried to get people to make more important changes before, and William has overruled, saying that the patch fixes the problem it aims to fix, and that other changes should be on another ticket.\n\n\nPerhaps sometimes [this](http://en.wikipedia.org/wiki/Procrastination). But it really depends on whether the changes are to the Sage library or spkgs, and - more important - on the type of the changes. If major bugs have to be fixed, doing so shouldn't be delayed by cosmetic improvements. Other code changes carry the risk of introducing new issues, so it might be appropriate to separate them. Others are better done at the same time, especially to avoid conflicting patches/tickets, and I think we don't want to create lots of new spkgs in sequence fixing \"minor\" things step by step.\n\n*Either* change 10 *or* 10000 bytes..., i.e. fix a single issue *and open a follow-up ticket* (with instructions) for *all* the rest, or do the whole job. My opinion. (Almost nobody will open a ticket to fix a single typo, and people seem unlikely to review \"cosmetic\" tickets. Similar to the apparently ever-lasting documentation problem.)\n\n> I'll produce a new package in a day or so. \n\n\nOr just upload one (or more) patch(es) prior to creating a new spkg.\n\n> >  * The following is perhaps (partly) obsolete, but currently completely misleading:\n> >      *\"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv.*\n \n> \n> The point of that is that if you run `make install`, then run the package for a second time, it will clean out all the files made on a previous build. You can't do `make distclean` at that point as there's no makefile. But I'll remove that.\n\n\nI'd simply clarify that. (And emphasize somehow this is unrelated to the next sentence/paragraph:)\n\n> >      *The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install.\"*\n\n\n> Nothing is removed. It was just a remark. I can remove it if you feel it causes confusion.\n\n\n(See above.) Perhaps make this an explicit, *separate* suggestion (*\"TODO:\"*) to avoid confusion.\n\n> >  * Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also \"layout\")...\n \n> \n> I'll try, but lets hope there are not too many itterations of this!\n\n\n:) I fear that, too. Perhaps create a *separate* patch for that (or omit it in the first place), and let Peter or me create a reviewer patch on top of the other changes.",
    "created_at": "2010-08-10T16:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92827",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:23 drkirkby]:
> Replying to [comment:21 leif]:
> > Unfortunately, I'd make *a lot* of changes (besides those I already mentioned), in different "categories", but most of them more or less important or of cosmetic nature.

> 
> But those lots of changes should be on another ticket. They have nothing to do with fixing the HP-UX issue!


If you don't emphasize/focus on HP-UX (i.e. e.g. add *"improve iconv package"*), perhaps more people will take a look at this ticket. :)

> As you know, I am quite keen to improve the quality of Sage, so I will make them. But be aware I've tried to get people to make more important changes before, and William has overruled, saying that the patch fixes the problem it aims to fix, and that other changes should be on another ticket.


Perhaps sometimes [this](http://en.wikipedia.org/wiki/Procrastination). But it really depends on whether the changes are to the Sage library or spkgs, and - more important - on the type of the changes. If major bugs have to be fixed, doing so shouldn't be delayed by cosmetic improvements. Other code changes carry the risk of introducing new issues, so it might be appropriate to separate them. Others are better done at the same time, especially to avoid conflicting patches/tickets, and I think we don't want to create lots of new spkgs in sequence fixing "minor" things step by step.

*Either* change 10 *or* 10000 bytes..., i.e. fix a single issue *and open a follow-up ticket* (with instructions) for *all* the rest, or do the whole job. My opinion. (Almost nobody will open a ticket to fix a single typo, and people seem unlikely to review "cosmetic" tickets. Similar to the apparently ever-lasting documentation problem.)

> I'll produce a new package in a day or so. 


Or just upload one (or more) patch(es) prior to creating a new spkg.

> >  * The following is perhaps (partly) obsolete, but currently completely misleading:
> >      *"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv.*
 
> 
> The point of that is that if you run `make install`, then run the package for a second time, it will clean out all the files made on a previous build. You can't do `make distclean` at that point as there's no makefile. But I'll remove that.


I'd simply clarify that. (And emphasize somehow this is unrelated to the next sentence/paragraph:)

> >      *The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install."*


> Nothing is removed. It was just a remark. I can remove it if you feel it causes confusion.


(See above.) Perhaps make this an explicit, *separate* suggestion (*"TODO:"*) to avoid confusion.

> >  * Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also "layout")...
 
> 
> I'll try, but lets hope there are not too many itterations of this!


:) I fear that, too. Perhaps create a *separate* patch for that (or omit it in the first place), and let Peter or me create a reviewer patch on top of the other changes.



---

archive/issue_comments_092828.json:
```json
{
    "body": "Attachment [9306-more-cleanup.patch](tarball://root/attachments/some-uuid/ticket9603/9306-more-cleanup.patch) by drkirkby created at 2010-08-10 20:16:32\n\nCorrect unquoted \"$SAGE_LOCAL\" and a bit of a cosmetic cleanup.",
    "created_at": "2010-08-10T20:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92828",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9306-more-cleanup.patch](tarball://root/attachments/some-uuid/ticket9603/9306-more-cleanup.patch) by drkirkby created at 2010-08-10 20:16:32

Correct unquoted "$SAGE_LOCAL" and a bit of a cosmetic cleanup.



---

archive/issue_comments_092829.json:
```json
{
    "body": "I've attached a patch, and also updated the .spkg at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n\nHopefully that is to your liking - it not, make a reviewer patch. \n\nI think I'll open a few \"clean-up\" packages when I want to sneak in an HP-UX patch. \n\nDave",
    "created_at": "2010-08-10T20:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92829",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've attached a patch, and also updated the .spkg at 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

Hopefully that is to your liking - it not, make a reviewer patch. 

I think I'll open a few "clean-up" packages when I want to sneak in an HP-UX patch. 

Dave



---

archive/issue_comments_092830.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-10T20:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92830",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_023918.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-08-14T15:39:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9603#event-23918"
}
```



---

archive/issue_comments_092831.json:
```json
{
    "body": "Replying to [comment:22 leif]:\n> P.S.: I tried to mark this ticket `# long time`, but that didn't work.\n> \n> (Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )\n\n\nI realise HP-UX is not top of your priority list (it is not mine either), but this ticket could have been very simple, but it has now been open for more than a month. The original patch just added the following:\n\n`&& [ \"x$UNAME\" != xHP-UX ]`\n\nin a couple of files.\n\nSince then you have asked me to make many changes to the `iconv` package that are unrelated to the HP-UX patch. I've done them, though I think it is fair to say that the `iconv` package was already one of the cleaner ones - compare it to Singular, Pari, ATLAS and many others! \n\nBut the ticket has now been open a month, and it is two weeks since you last commented. If you don't feel you will be able to review it within the next few days, please let me know and I'll consider trying to find another reviewer. \n\n\nDave",
    "created_at": "2010-08-26T00:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92831",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:22 leif]:
> P.S.: I tried to mark this ticket `# long time`, but that didn't work.
> 
> (Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )


I realise HP-UX is not top of your priority list (it is not mine either), but this ticket could have been very simple, but it has now been open for more than a month. The original patch just added the following:

`&& [ "x$UNAME" != xHP-UX ]`

in a couple of files.

Since then you have asked me to make many changes to the `iconv` package that are unrelated to the HP-UX patch. I've done them, though I think it is fair to say that the `iconv` package was already one of the cleaner ones - compare it to Singular, Pari, ATLAS and many others! 

But the ticket has now been open a month, and it is two weeks since you last commented. If you don't feel you will be able to review it within the next few days, please let me know and I'll consider trying to find another reviewer. 


Dave



---

archive/issue_comments_092832.json:
```json
{
    "body": "Well, meanwhile iconv was buried rather deep in one of my stacks of notes...\n\nThe latest patch looks quite fine, so my reviewer patch will be fairly small. :)\n\nCan you confirm that *reinstalling* iconv still works, since you also dropped *the code* that removed the traces of previous iconv installations?\n\n(I only meant *the remarks in `SPKG.txt`* were confusing, especially the second - perhaps unrelated - paragraph; see my [comment above](http://trac.sagemath.org/sage_trac/ticket/9603#comment:21). I suggested replacing this by *\"When updating the package, one should make sure all traces of previous installations of iconv still get removed prior to [re]installation.\"*, unless this has become obsolete now, which I don't know.)\n\nAlso, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?\n\n(You haven't [yet] changed that, but we should *always* use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `\"make -j\"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)",
    "created_at": "2010-08-26T11:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92832",
    "user": "https://github.com/nexttime"
}
```

Well, meanwhile iconv was buried rather deep in one of my stacks of notes...

The latest patch looks quite fine, so my reviewer patch will be fairly small. :)

Can you confirm that *reinstalling* iconv still works, since you also dropped *the code* that removed the traces of previous iconv installations?

(I only meant *the remarks in `SPKG.txt`* were confusing, especially the second - perhaps unrelated - paragraph; see my [comment above](http://trac.sagemath.org/sage_trac/ticket/9603#comment:21). I suggested replacing this by *"When updating the package, one should make sure all traces of previous installations of iconv still get removed prior to [re]installation."*, unless this has become obsolete now, which I don't know.)

Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?

(You haven't [yet] changed that, but we should *always* use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `"make -j"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)



---

archive/issue_comments_092833.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-08-26T11:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92833",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_092834.json:
```json
{
    "body": "Replying to [comment:29 leif]:\n> Well, meanwhile iconv was buried rather deep in one of my stacks of notes...\n> \n> The latest patch looks quite fine, so my reviewer patch will be fairly small. :)\n\n\nRelief!! \n \n> Can you confirm that *reinstalling* iconv still works, since you also dropped *the code* that removed the traces of previous iconv installations?\n\n\nYes, it is OK\n\nAlthough I added the code originally to delete previous parts of the install, I think it is perhaps not wise. It's simply going to be impossible to do this accurately all the time. The best we could do it to get it working for most people most of the time. It might be feasible if a package only installs a few files, but when many files are installed, and the installed files will probably change with operating system, it is hard to do well. I think it's best simply to not try at all. In any case, few if any other Sage packages do this. I can't think of one in fact. \n \n> Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?\n\n\nI will do. \n\n> (You haven't [yet] changed that, but we should *always* use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `\"make -j\"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)\n\n \nI realise this. However, I am well aware that making changes like that are well outside the scope of the original ticket, and potentially more risky. \n\nIf I get a ticket merged with the title **Force iconv to build + install on HP-UX. Currently it is only installed on Solaris and Cygwin** and that screws up a build on Linux, I am not going to be a very popular person that is for sure! Enabling parallel builds is easy to do, but difficult to test thoroughly. \n\nThankfully, iconv is only installed on Solaris and Cygwin, so hopefully this wont cause too many guns to be fired at me if it goes wrong! This ticket has been changed from one that was very safe (adding `&& [ \"x$UNAME\" != xHP-UX ]` in a couple of places), into one which has major changes to the structure, style and possibly the inclusion of parallel builds. Really I feel those changes should have been on another ticket.  \n\nI think I'm going to change the title. And you can be sure I will deflect some of the blame at you if it goes wrong!!! \n\nI'll check to **needs review** once I've tested this. \n\nDave",
    "created_at": "2010-08-26T13:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92834",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:29 leif]:
> Well, meanwhile iconv was buried rather deep in one of my stacks of notes...
> 
> The latest patch looks quite fine, so my reviewer patch will be fairly small. :)


Relief!! 
 
> Can you confirm that *reinstalling* iconv still works, since you also dropped *the code* that removed the traces of previous iconv installations?


Yes, it is OK

Although I added the code originally to delete previous parts of the install, I think it is perhaps not wise. It's simply going to be impossible to do this accurately all the time. The best we could do it to get it working for most people most of the time. It might be feasible if a package only installs a few files, but when many files are installed, and the installed files will probably change with operating system, it is hard to do well. I think it's best simply to not try at all. In any case, few if any other Sage packages do this. I can't think of one in fact. 
 
> Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?


I will do. 

> (You haven't [yet] changed that, but we should *always* use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `"make -j"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)

 
I realise this. However, I am well aware that making changes like that are well outside the scope of the original ticket, and potentially more risky. 

If I get a ticket merged with the title **Force iconv to build + install on HP-UX. Currently it is only installed on Solaris and Cygwin** and that screws up a build on Linux, I am not going to be a very popular person that is for sure! Enabling parallel builds is easy to do, but difficult to test thoroughly. 

Thankfully, iconv is only installed on Solaris and Cygwin, so hopefully this wont cause too many guns to be fired at me if it goes wrong! This ticket has been changed from one that was very safe (adding `&& [ "x$UNAME" != xHP-UX ]` in a couple of places), into one which has major changes to the structure, style and possibly the inclusion of parallel builds. Really I feel those changes should have been on another ticket.  

I think I'm going to change the title. And you can be sure I will deflect some of the blame at you if it goes wrong!!! 

I'll check to **needs review** once I've tested this. 

Dave



---

archive/issue_comments_092835.json:
```json
{
    "body": "Replying to [comment:30 drkirkby]:\n> Replying to [comment:29 leif]:\n> > Can you confirm that *reinstalling* iconv still works, since you also dropped *the code* that removed the traces of previous iconv installations?\n\n> \n> Yes, it is OK\n> \n> Although I added the code originally to delete previous parts of the install, I think it is perhaps not wise. It's simply going to be impossible to do this accurately all the time. The best we could do it to get it working for most people most of the time. It might be feasible if a package only installs a few files, but when many files are installed, and the installed files will probably change with operating system, it is hard to do well. I think it's best simply to not try at all. In any case, few if any other Sage packages do this. I can't think of one in fact.\n\n\nI thought it was some iconv flaw that previously broke reinstallations; in that case, we could perhaps as well have patched the upstream installation procedure.\n\n \n> > Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?\n\n> \n> I will do. \n> \n> > (You haven't [yet] changed that, but we should *always* use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `\"make -j\"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)\n\n>  \n> I realise this. However, I am well aware that making changes like that are well outside the scope of the original ticket, and potentially more risky.\n\n\nPerhaps ask Mike if this would currently cause any issues on Cygwin.\n\n\n> If I get a ticket merged with the title **Force iconv to build + install on HP-UX. Currently it is only installed on Solaris and Cygwin** and that screws up a build on Linux, I am not going to be a very popular person that is for sure! Enabling parallel builds is easy to do, but difficult to test thoroughly. \n> \n> Thankfully, iconv is only installed on Solaris and Cygwin, so hopefully this wont cause too many guns to be fired at me if it goes wrong!\n\n\n:)\n\n> This ticket has been changed from one that was very safe (adding `&& [ \"x$UNAME\" != xHP-UX ]` in a couple of places), into one which has major changes to the structure, style and possibly the inclusion of parallel builds. Really I feel those changes should have been on another ticket.  \n> \n> I think I'm going to change the title. And you can be sure I will deflect some of the blame at you if it goes wrong!!! \n\n\nI thought \"HP-UX\" already went into a footnote to attract more reviewers... ;-)\n\n(It's now actually a clean-up ticket, too.)\n\n \n> I'll check to **needs review** once I've tested this. \n\n\nOk.",
    "created_at": "2010-08-26T14:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92835",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:30 drkirkby]:
> Replying to [comment:29 leif]:
> > Can you confirm that *reinstalling* iconv still works, since you also dropped *the code* that removed the traces of previous iconv installations?

> 
> Yes, it is OK
> 
> Although I added the code originally to delete previous parts of the install, I think it is perhaps not wise. It's simply going to be impossible to do this accurately all the time. The best we could do it to get it working for most people most of the time. It might be feasible if a package only installs a few files, but when many files are installed, and the installed files will probably change with operating system, it is hard to do well. I think it's best simply to not try at all. In any case, few if any other Sage packages do this. I can't think of one in fact.


I thought it was some iconv flaw that previously broke reinstallations; in that case, we could perhaps as well have patched the upstream installation procedure.

 
> > Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?

> 
> I will do. 
> 
> > (You haven't [yet] changed that, but we should *always* use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `"make -j"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)

>  
> I realise this. However, I am well aware that making changes like that are well outside the scope of the original ticket, and potentially more risky.


Perhaps ask Mike if this would currently cause any issues on Cygwin.


> If I get a ticket merged with the title **Force iconv to build + install on HP-UX. Currently it is only installed on Solaris and Cygwin** and that screws up a build on Linux, I am not going to be a very popular person that is for sure! Enabling parallel builds is easy to do, but difficult to test thoroughly. 
> 
> Thankfully, iconv is only installed on Solaris and Cygwin, so hopefully this wont cause too many guns to be fired at me if it goes wrong!


:)

> This ticket has been changed from one that was very safe (adding `&& [ "x$UNAME" != xHP-UX ]` in a couple of places), into one which has major changes to the structure, style and possibly the inclusion of parallel builds. Really I feel those changes should have been on another ticket.  
> 
> I think I'm going to change the title. And you can be sure I will deflect some of the blame at you if it goes wrong!!! 


I thought "HP-UX" already went into a footnote to attract more reviewers... ;-)

(It's now actually a clean-up ticket, too.)

 
> I'll check to **needs review** once I've tested this. 


Ok.



---

archive/issue_comments_092836.json:
```json
{
    "body": "P.S.: Using `make` could in fact fail for people who [have to] set `MAKE` to e.g. `gmake` or `/some/strange/path/to/functional/make`.",
    "created_at": "2010-08-26T14:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92836",
    "user": "https://github.com/nexttime"
}
```

P.S.: Using `make` could in fact fail for people who [have to] set `MAKE` to e.g. `gmake` or `/some/strange/path/to/functional/make`.



---

archive/issue_comments_092837.json:
```json
{
    "body": "I've tested this in parallel on my Sun Ultra 27 running OpenSolaris 127 times. It builds and passes all iconv's tests every time. \n\nMy machine is under a **very** heavy load at the minute as I'm running `make ptestlong` 100 times in a loop! Needless to say `iconv` takes a while to install. But with `MAKE` to to `make -j12`, the time to just install (not run the tests), is\n\n```\nreal\t1m59.844s\nuser\t0m19.226s\nsys\t0m9.280s\nSuccessfully installed iconv-1.13.1.p3\n```\n\nSo the total CPU time is 28.5 seconds, and the installation time 1m59s for a parallel build with 12 threads on this 4-core, hyperthreaded machine. (1 physical PCU, 4 cores, 8 threads). \n\nWith `MAKE` unset, so a serial build, the installation time rose to 3m:49s\n\n```\nreal\t3m46.106s\nuser\t0m19.233s\nsys\t0m9.788s\nSuccessfully installed iconv-1.13.1.p3\n```\n\nThe parallel build is faster by a factor of around 1.9. The actual CPU time used remained virtually unchanged. So the parallel install seems worthwhile. \n\nI'll repeat this on `t2.math` for as long as my patience permits. That has a lot more cores, but is very slow overall. I doubt I'll test as extensively. I'll then ask Mike to test on Cygwin. \n\nI've not updated the package yet. I'll do that when I'm finished more testing. \n\nI've changed the title, so I don't get quite as much **** thrown at me if this goes wrong! The content of the HP-UX changes are now about 1% I think!\n\nDave",
    "created_at": "2010-08-26T22:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92837",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've tested this in parallel on my Sun Ultra 27 running OpenSolaris 127 times. It builds and passes all iconv's tests every time. 

My machine is under a **very** heavy load at the minute as I'm running `make ptestlong` 100 times in a loop! Needless to say `iconv` takes a while to install. But with `MAKE` to to `make -j12`, the time to just install (not run the tests), is

```
real	1m59.844s
user	0m19.226s
sys	0m9.280s
Successfully installed iconv-1.13.1.p3
```

So the total CPU time is 28.5 seconds, and the installation time 1m59s for a parallel build with 12 threads on this 4-core, hyperthreaded machine. (1 physical PCU, 4 cores, 8 threads). 

With `MAKE` unset, so a serial build, the installation time rose to 3m:49s

```
real	3m46.106s
user	0m19.233s
sys	0m9.788s
Successfully installed iconv-1.13.1.p3
```

The parallel build is faster by a factor of around 1.9. The actual CPU time used remained virtually unchanged. So the parallel install seems worthwhile. 

I'll repeat this on `t2.math` for as long as my patience permits. That has a lot more cores, but is very slow overall. I doubt I'll test as extensively. I'll then ask Mike to test on Cygwin. 

I've not updated the package yet. I'll do that when I'm finished more testing. 

I've changed the title, so I don't get quite as much **** thrown at me if this goes wrong! The content of the HP-UX changes are now about 1% I think!

Dave



---

archive/issue_comments_092838.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-27T18:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92838",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_092839.json:
```json
{
    "body": "OK, I'm happy with \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n\nnow. Mike Hansen has said it OK on Cygwin:\n\n```\nOn Fri, Aug 27, 2010 at 3:21 AM, Dr. David Kirkby\n<david.kirkby@onetel.net> wrote:\n> > http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n> >\n> > I don't believe there will be any issues with Cygwin, but it would be nice\n> > to know.\nLooks good to me.\n\n--Mike\n```\n\nand I've personally tested it with parallel builds many times. \n\n* 127 times on OpenSolaris using my Sun Ultra 27 with 12 threads. \n* 50 times on Solaris 10 (t2.math) with 128 threads. \n* 13 times on HP-UX. Single threaded only - this is a uni-processor machine. \n\nIn each case, all iconv's tests pass. \n\nPerhaps Leif could add a reviewer patch for anything else he feels needs addressing, as it should be very minor now. \n\nDave",
    "created_at": "2010-08-27T18:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92839",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

OK, I'm happy with 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

now. Mike Hansen has said it OK on Cygwin:

```
On Fri, Aug 27, 2010 at 3:21 AM, Dr. David Kirkby
<david.kirkby@onetel.net> wrote:
> > http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg
> >
> > I don't believe there will be any issues with Cygwin, but it would be nice
> > to know.
Looks good to me.

--Mike
```

and I've personally tested it with parallel builds many times. 

* 127 times on OpenSolaris using my Sun Ultra 27 with 12 threads. 
* 50 times on Solaris 10 (t2.math) with 128 threads. 
* 13 times on HP-UX. Single threaded only - this is a uni-processor machine. 

In each case, all iconv's tests pass. 

Perhaps Leif could add a reviewer patch for anything else he feels needs addressing, as it should be very minor now. 

Dave



---

archive/issue_comments_092840.json:
```json
{
    "body": "Replaces 'make' by '$MAKE'. Hopefully the last patch needed!",
    "created_at": "2010-08-27T18:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92840",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replaces 'make' by '$MAKE'. Hopefully the last patch needed!



---

archive/issue_comments_092841.json:
```json
{
    "body": "Attachment [9603-parallel-and-HP-UX.patch](tarball://root/attachments/some-uuid/ticket9603/9603-parallel-and-HP-UX.patch) by drkirkby created at 2010-08-29 11:52:37\n\nI'm marking this as needs work, since another problem with iconv (#9718) on some 64-bit Solaris systems has been solved by the libtool developer Ralf Wildenhues. It makes sense to fix that issue at the same time. \n\nI'll address this later. \n\nDave",
    "created_at": "2010-08-29T11:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92841",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9603-parallel-and-HP-UX.patch](tarball://root/attachments/some-uuid/ticket9603/9603-parallel-and-HP-UX.patch) by drkirkby created at 2010-08-29 11:52:37

I'm marking this as needs work, since another problem with iconv (#9718) on some 64-bit Solaris systems has been solved by the libtool developer Ralf Wildenhues. It makes sense to fix that issue at the same time. 

I'll address this later. 

Dave



---

archive/issue_comments_092842.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-29T11:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92842",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092843.json:
```json
{
    "body": "I'm now marking this as needs review.\n\nI've changed the priority from minor to major, as this resolves a problem (#9718) on 64-bit Solaris, and there is a concerted effort to now get Sage to build on 64-bit Solaris and OpenSolaris. Prior to this, the ticket was originally to build iconv on HP-UX, which was a minor issue.",
    "created_at": "2010-08-29T16:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92843",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm now marking this as needs review.

I've changed the priority from minor to major, as this resolves a problem (#9718) on 64-bit Solaris, and there is a concerted effort to now get Sage to build on 64-bit Solaris and OpenSolaris. Prior to this, the ticket was originally to build iconv on HP-UX, which was a minor issue.



---

archive/issue_comments_092844.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-29T16:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92844",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092845.json:
```json
{
    "body": "Attachment [9603-move-from-CFLAGS-to-CC.patch](tarball://root/attachments/some-uuid/ticket9603/9603-move-from-CFLAGS-to-CC.patch) by drkirkby created at 2010-08-29 16:18:33\n\nChange the place where the flag for 64-bit builds is inserted from CFLAGS to CC.",
    "created_at": "2010-08-29T16:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92845",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9603-move-from-CFLAGS-to-CC.patch](tarball://root/attachments/some-uuid/ticket9603/9603-move-from-CFLAGS-to-CC.patch) by drkirkby created at 2010-08-29 16:18:33

Change the place where the flag for 64-bit builds is inserted from CFLAGS to CC.



---

archive/issue_comments_092846.json:
```json
{
    "body": "```\n## Special Update/Build Instructions\n * [...] anyone updating this package should be familiar with how\n   to write shell scripts.\n```\nCan we paste this into **every** `SPKG.txt`? :D :D :D\n\nI'll commit your latest changes in your name...",
    "created_at": "2010-09-08T12:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92846",
    "user": "https://github.com/nexttime"
}
```

```
## Special Update/Build Instructions
 * [...] anyone updating this package should be familiar with how
   to write shell scripts.
```
Can we paste this into **every** `SPKG.txt`? :D :D :D

I'll commit your latest changes in your name...



---

archive/issue_comments_092847.json:
```json
{
    "body": "Attachment [trac_9603-iconv_spkg-first_reviewer.patch](tarball://root/attachments/some-uuid/ticket9603/trac_9603-iconv_spkg-first_reviewer.patch) by @nexttime created at 2010-09-08 16:05:23\n\nSPKG patch. Apply on top of other patches. (Consistently use `\"$UNAME\"`; clean-up.)",
    "created_at": "2010-09-08T16:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92847",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_9603-iconv_spkg-first_reviewer.patch](tarball://root/attachments/some-uuid/ticket9603/trac_9603-iconv_spkg-first_reviewer.patch) by @nexttime created at 2010-09-08 16:05:23

SPKG patch. Apply on top of other patches. (Consistently use `"$UNAME"`; clean-up.)



---

archive/issue_comments_092848.json:
```json
{
    "body": "Replying to [comment:37 leif]:\n> {{{\n> == Special Update/Build Instructions ==\n> * [...] anyone updating this package should be familiar with how\n>   to write shell scripts.\n> }}}\n> Can we paste this into **every** `SPKG.txt`? :D :D :D\n\n\nYes, but then nothing would ever get updated I guess. \n\nDo you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? \n\nDave",
    "created_at": "2010-09-08T16:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92848",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:37 leif]:
> {{{
> == Special Update/Build Instructions ==
> * [...] anyone updating this package should be familiar with how
>   to write shell scripts.
> }}}
> Can we paste this into **every** `SPKG.txt`? :D :D :D


Yes, but then nothing would ever get updated I guess. 

Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? 

Dave



---

archive/issue_comments_092849.json:
```json
{
    "body": "Replying to [comment:38 drkirkby]:\n> Replying to [comment:37 leif]:\n\n{{{\n## Special Update/Build Instructions\n* [...] anyone updating this package should be familiar with how\n  to write shell scripts.\n}}}\n> > Can we paste this into **every** `SPKG.txt`? :D :D :D\n\n> \n> Yes, but then nothing would ever get updated I guess. \n\n\nAnd we (still) have spkgs with (only) Python scripts, too.\n\nIf no new patches have to be applied (or old ones removed), and no configuration changes are necessary, replacing the contents of `src/` shouldn't be a big deal. (Though some people copy the whole spkg folder to a new one omitting \"hidden\" files, i.e. the Mercurial repository! ;-) )\n\n> Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? \n\n\nI'm currently preparing a second, *optional* reviewer patch with stylistic changes to `spkg-install` and `spkg-check` as a suggestion, for \"review\". I wonder if such would cause further excessive testing, so I consider it optional.\n\nI could upload one or two new spkgs soon, too. At your taste.",
    "created_at": "2010-09-08T16:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92849",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:38 drkirkby]:
> Replying to [comment:37 leif]:

{{{
## Special Update/Build Instructions
* [...] anyone updating this package should be familiar with how
  to write shell scripts.
}}}
> > Can we paste this into **every** `SPKG.txt`? :D :D :D

> 
> Yes, but then nothing would ever get updated I guess. 


And we (still) have spkgs with (only) Python scripts, too.

If no new patches have to be applied (or old ones removed), and no configuration changes are necessary, replacing the contents of `src/` shouldn't be a big deal. (Though some people copy the whole spkg folder to a new one omitting "hidden" files, i.e. the Mercurial repository! ;-) )

> Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? 


I'm currently preparing a second, *optional* reviewer patch with stylistic changes to `spkg-install` and `spkg-check` as a suggestion, for "review". I wonder if such would cause further excessive testing, so I consider it optional.

I could upload one or two new spkgs soon, too. At your taste.



---

archive/issue_comments_092850.json:
```json
{
    "body": "Replying to [comment:39 leif]:\n\n> If no new patches have to be applied (or old ones removed), and no configuration changes are necessary, replacing the contents of `src/` shouldn't be a big deal. (Though some people copy the whole spkg folder to a new one omitting \"hidden\" files, i.e. the Mercurial repository! ;-) )\n\n\nYes, I think I've seen this. \n\n> > Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? \n\n> \n> I'm currently preparing a second, *optional* reviewer patch with stylistic changes to `spkg-install` and `spkg-check` as a suggestion, for \"review\". I wonder if such would cause further excessive testing, so I consider it optional.\n\n\nI'm keen to see the back of this ticket. The quicker it gets a positive review, the more chance it is of getting into an early 4.6 alpha. \n \n> I could upload one or two new spkgs soon, too. At your taste.\n\n\nLet me look at your \"optional\" patch, but I'm not keen on making unnecessary changes now. \n\nDave",
    "created_at": "2010-09-08T16:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92850",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:39 leif]:

> If no new patches have to be applied (or old ones removed), and no configuration changes are necessary, replacing the contents of `src/` shouldn't be a big deal. (Though some people copy the whole spkg folder to a new one omitting "hidden" files, i.e. the Mercurial repository! ;-) )


Yes, I think I've seen this. 

> > Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? 

> 
> I'm currently preparing a second, *optional* reviewer patch with stylistic changes to `spkg-install` and `spkg-check` as a suggestion, for "review". I wonder if such would cause further excessive testing, so I consider it optional.


I'm keen to see the back of this ticket. The quicker it gets a positive review, the more chance it is of getting into an early 4.6 alpha. 
 
> I could upload one or two new spkgs soon, too. At your taste.


Let me look at your "optional" patch, but I'm not keen on making unnecessary changes now. 

Dave



---

archive/issue_comments_092851.json:
```json
{
    "body": "P.S.: I also wonder if we should really drop the removal of previous iconv installations. Doing so can potentially cause trouble, while (properly) attempting to remove old traces shouldn't [hurt].\n\n(My comment regarding that only referred to the confusing description in `SPKG.txt`, not to the code or the removal in general.)",
    "created_at": "2010-09-08T16:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92851",
    "user": "https://github.com/nexttime"
}
```

P.S.: I also wonder if we should really drop the removal of previous iconv installations. Doing so can potentially cause trouble, while (properly) attempting to remove old traces shouldn't [hurt].

(My comment regarding that only referred to the confusing description in `SPKG.txt`, not to the code or the removal in general.)



---

archive/issue_comments_092852.json:
```json
{
    "body": "I think doing this in practice will be fraught with difficulty. The actual files installed might even depend on platform. (For example, shared libraries on HP-UX are .sl not .so). In general the files might depend on the value of environment variables. I think it's just best to not try to do that. I think it was a bad idea of mine, and one not worth revisiting. \n\nDave",
    "created_at": "2010-09-08T17:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92852",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I think doing this in practice will be fraught with difficulty. The actual files installed might even depend on platform. (For example, shared libraries on HP-UX are .sl not .so). In general the files might depend on the value of environment variables. I think it's just best to not try to do that. I think it was a bad idea of mine, and one not worth revisiting. 

Dave



---

archive/issue_comments_092853.json:
```json
{
    "body": "Optional SPKG patch. Apply on top of first reviewer patch. (Stylistic change.))",
    "created_at": "2010-09-08T17:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92853",
    "user": "https://github.com/nexttime"
}
```

Optional SPKG patch. Apply on top of first reviewer patch. (Stylistic change.))



---

archive/issue_comments_092854.json:
```json
{
    "body": "Attachment [trac_9603-iconv_spkg-optional_second_reviewer.patch](tarball://root/attachments/some-uuid/ticket9603/trac_9603-iconv_spkg-optional_second_reviewer.patch) by @nexttime created at 2010-09-08 18:11:52\n\nReplying to [comment:42 drkirkby]:\n> I think doing this in practice will be fraught with difficulty. The actual files installed might even depend on platform. (For example, shared libraries on HP-UX are .sl not .so). In general the files might depend on the value of environment variables. I think it's just best to not try to do that.\n\n\nWell, we have `rm -f` and (not only) filename globbing. In case we later run into problems (e.g. when upstream gets updated), *you* 're to blame (and you'll have to solve it)... So I won't mind omitting it now. ;-)\n\n> I think it was a bad idea of mine, and one not worth revisiting.\n\n\nMost spkgs do that.\n\n---\n\nI've attached my second reviewer patch which I would really like to see merged, too. :-)\n\n---\n\nI'll set this to \"positive review\" if you (and Peter) are ok with my changes (either both or just my first reviewer patch).",
    "created_at": "2010-09-08T18:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92854",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_9603-iconv_spkg-optional_second_reviewer.patch](tarball://root/attachments/some-uuid/ticket9603/trac_9603-iconv_spkg-optional_second_reviewer.patch) by @nexttime created at 2010-09-08 18:11:52

Replying to [comment:42 drkirkby]:
> I think doing this in practice will be fraught with difficulty. The actual files installed might even depend on platform. (For example, shared libraries on HP-UX are .sl not .so). In general the files might depend on the value of environment variables. I think it's just best to not try to do that.


Well, we have `rm -f` and (not only) filename globbing. In case we later run into problems (e.g. when upstream gets updated), *you* 're to blame (and you'll have to solve it)... So I won't mind omitting it now. ;-)

> I think it was a bad idea of mine, and one not worth revisiting.


Most spkgs do that.

---

I've attached my second reviewer patch which I would really like to see merged, too. :-)

---

I'll set this to "positive review" if you (and Peter) are ok with my changes (either both or just my first reviewer patch).



---

archive/issue_comments_092855.json:
```json
{
    "body": "The package I reference at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n\nhas a couple of changes that are not checked in. However, I have a copy with all changes checked in here - I failed to upload it.\n\nWhen I apply your patches to that, so I get a reject. Can you create a complete package and provide a link. Then I'll check it.\n\nI'll go with your second reviewer patch too, though is there not a mistake on line 21 of `spkg-check` ? \n\nDave",
    "created_at": "2010-09-08T19:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92855",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The package I reference at 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

has a couple of changes that are not checked in. However, I have a copy with all changes checked in here - I failed to upload it.

When I apply your patches to that, so I get a reject. Can you create a complete package and provide a link. Then I'll check it.

I'll go with your second reviewer patch too, though is there not a mistake on line 21 of `spkg-check` ? 

Dave



---

archive/issue_comments_092856.json:
```json
{
    "body": "Replying to [comment:44 drkirkby]:\n> The package I reference at \n> \n> http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n> \n> has a couple of changes that are not checked in. \n\n\nI mentioned that somewhere above. I've committed your changes in your name (these were only those related to #9718 - hopefully).\n\n> When I apply your patches to that, so I get a reject.\n\n\nOoops? Don't know why; should not happen... 8|\n\n> Can you create a complete package and provide a link. Then I'll check it.\n\n\nYes, I already have it (actually two), just have to upload one of them.\n\n> I'll go with your second reviewer patch too,\n\n\nFine, thanks.\n\n> though is there not a mistake on line 21 of `spkg-check` ? \n\n\nYou mean `;&`? That's \"the opposite\" of `;;` (\"break\"), i.e. fall-through.",
    "created_at": "2010-09-08T21:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92856",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:44 drkirkby]:
> The package I reference at 
> 
> http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg
> 
> has a couple of changes that are not checked in. 


I mentioned that somewhere above. I've committed your changes in your name (these were only those related to #9718 - hopefully).

> When I apply your patches to that, so I get a reject.


Ooops? Don't know why; should not happen... 8|

> Can you create a complete package and provide a link. Then I'll check it.


Yes, I already have it (actually two), just have to upload one of them.

> I'll go with your second reviewer patch too,


Fine, thanks.

> though is there not a mistake on line 21 of `spkg-check` ? 


You mean `;&`? That's "the opposite" of `;;` ("break"), i.e. fall-through.



---

archive/issue_comments_092857.json:
```json
{
    "body": "Replying to [comment:45 leif]:\n> Replying to [comment:44 drkirkby]:\n> > The package I reference at \n> > \n> > http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg\n> > \n> > has a couple of changes that are not checked in. \n\n> \n> I mentioned that somewhere above. I've committed your changes in your name (these were only those related to #9718 - hopefully).\n> \n> > When I apply your patches to that, so I get a reject.\n\n> \n> Ooops? Don't know why; should not happen... 8|\n\n\n```\nchangeset:   11:7ffde08f86a0\ntag:         tip\nuser:        Leif Leonhardy <not.really@online.de>\ndate:        Wed Sep 08 19:39:14 2010 +0200\nfiles:       SPKG.txt spkg-check spkg-install\ndescription:\n#9603: Stylistic change: Use 'case' statements for $UNAME case distinctions.\n\n\nchangeset:   10:e5178b991bd2\nuser:        Leif Leonhardy <not.really@online.de>\ndate:        Wed Sep 08 17:58:58 2010 +0200\nfiles:       SPKG.txt spkg-check spkg-install\ndescription:\n#9603: Consistently use \"$UNAME\"; more comments, corrections & cosmetic changes.\n\n\nchangeset:   9:ceb9cde565c1\nuser:        David Kirkby <david.kirkby@onetel.net>\ndate:        Wed Sep 08 14:18:58 2010 +0200\nfiles:       SPKG.txt spkg-install\ndescription:\n#9718/#9603 Set the compiler flag for building 64-bit binaries in CC not CFLAGS\n\n\nchangeset:   8:db6e4a8c74d8\nuser:        David Kirkby <david.kirkby@onetel.net>\ndate:        Thu Aug 26 23:36:08 2010 +0100\nfiles:       SPKG.txt spkg-check spkg-install\ndescription:\n#9603 Use $MAKE instead of 'make' to speed up parallel builds.\n\n\nchangeset:   7:c91f30ba571d\nuser:        David Kirkby <david.kirkby@onetel.net>\ndate:        Tue Aug 10 20:47:59 2010 +0100\nfiles:       SPKG.txt spkg-check spkg-install\ndescription:\n#9603 Address more reviewer comments. Mainly cosmetic, but also fix the fact $SAGE_LOCAL was not quoted.\n\n\nchangeset:   6:745799a814dd\nuser:        David Kirkby <david.kirkby@onetel.net>\ndate:        Wed Jul 28 01:35:01 2010 +0100\nfiles:       SPKG.txt spkg-check spkg-install\ndescription:\n#9603 Clean up spkg-install and spkg-check in the light of reviewer comments.\n\n\nchangeset:   5:3fe4fc14de91\nuser:        David Kirkby <david.kirkby@onetel.net>\ndate:        Tue Jul 27 10:36:47 2010 +0100\nfiles:       spkg-install\ndescription:\n#9603 Corrected an informative message about the operating system this is installed on. A trivial change, but it might as well be right.\n\n\nchangeset:   4:31960cb87501\nuser:        David Kirkby <david.kirkby@onetel.net>\ndate:        Mon Jul 26 14:36:15 2010 +0100\nfiles:       SPKG.txt spkg-check spkg-install\ndescription:\n#9603 Force iconv to build on HP-UX in addition to the previous Solaris and Cygwin.\n\n\nchangeset:   3:32e7f7a36cea\nuser:        J. H. Palmieri <palmieri@math.washington.edu>\ndate:        Wed Mar 31 18:35:42 2010 -0700\nfiles:       SPKG.txt spkg-check\ndescription:\nspkg-check: only run on Solaris or Cygwin\n\n...\n```\n(I've committed changeset 9 for you.)",
    "created_at": "2010-09-08T21:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92857",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:45 leif]:
> Replying to [comment:44 drkirkby]:
> > The package I reference at 
> > 
> > http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg
> > 
> > has a couple of changes that are not checked in. 

> 
> I mentioned that somewhere above. I've committed your changes in your name (these were only those related to #9718 - hopefully).
> 
> > When I apply your patches to that, so I get a reject.

> 
> Ooops? Don't know why; should not happen... 8|


```
changeset:   11:7ffde08f86a0
tag:         tip
user:        Leif Leonhardy <not.really@online.de>
date:        Wed Sep 08 19:39:14 2010 +0200
files:       SPKG.txt spkg-check spkg-install
description:
#9603: Stylistic change: Use 'case' statements for $UNAME case distinctions.


changeset:   10:e5178b991bd2
user:        Leif Leonhardy <not.really@online.de>
date:        Wed Sep 08 17:58:58 2010 +0200
files:       SPKG.txt spkg-check spkg-install
description:
#9603: Consistently use "$UNAME"; more comments, corrections & cosmetic changes.


changeset:   9:ceb9cde565c1
user:        David Kirkby <david.kirkby@onetel.net>
date:        Wed Sep 08 14:18:58 2010 +0200
files:       SPKG.txt spkg-install
description:
#9718/#9603 Set the compiler flag for building 64-bit binaries in CC not CFLAGS


changeset:   8:db6e4a8c74d8
user:        David Kirkby <david.kirkby@onetel.net>
date:        Thu Aug 26 23:36:08 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Use $MAKE instead of 'make' to speed up parallel builds.


changeset:   7:c91f30ba571d
user:        David Kirkby <david.kirkby@onetel.net>
date:        Tue Aug 10 20:47:59 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Address more reviewer comments. Mainly cosmetic, but also fix the fact $SAGE_LOCAL was not quoted.


changeset:   6:745799a814dd
user:        David Kirkby <david.kirkby@onetel.net>
date:        Wed Jul 28 01:35:01 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Clean up spkg-install and spkg-check in the light of reviewer comments.


changeset:   5:3fe4fc14de91
user:        David Kirkby <david.kirkby@onetel.net>
date:        Tue Jul 27 10:36:47 2010 +0100
files:       spkg-install
description:
#9603 Corrected an informative message about the operating system this is installed on. A trivial change, but it might as well be right.


changeset:   4:31960cb87501
user:        David Kirkby <david.kirkby@onetel.net>
date:        Mon Jul 26 14:36:15 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Force iconv to build on HP-UX in addition to the previous Solaris and Cygwin.


changeset:   3:32e7f7a36cea
user:        J. H. Palmieri <palmieri@math.washington.edu>
date:        Wed Mar 31 18:35:42 2010 -0700
files:       SPKG.txt spkg-check
description:
spkg-check: only run on Solaris or Cygwin

...
```
(I've committed changeset 9 for you.)



---

archive/issue_comments_092858.json:
```json
{
    "body": "OK, where's the .spkg I can test? \n\nDave",
    "created_at": "2010-09-08T22:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92858",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

OK, where's the .spkg I can test? 

Dave



---

archive/issue_comments_092859.json:
```json
{
    "body": "Thank you for the link to a .spkg file. I'll test the package and let you know. \n\nDave",
    "created_at": "2010-09-08T22:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92859",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you for the link to a .spkg file. I'll test the package and let you know. 

Dave



---

archive/issue_comments_092860.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-08T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92860",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092861.json:
```json
{
    "body": "No, there's a problem if SPKG_CHECK is set to \"yes\" on `sage.math`. It happens to be on the bit of code I was suspicious of - i.e. line 21 of `spkg-check`\n\n```\niconv will not be installed, as we only need to build it on\nSolaris, HP-UX and Cygwin, as the system's iconv will be used\non other platforms, rather than the one shipped with Sage.\nSee:\n    http://trac.sagemath.org/sage_trac/ticket/8567\n    http://trac.sagemath.org/sage_trac/ticket/9603\n\nreal\t0m0.005s\nuser\t0m0.000s\nsys\t0m0.000s\nSuccessfully installed iconv-1.13.1.p3\nRunning the test suite.\n./spkg-check: line 21: syntax error near unexpected token `;'\n./spkg-check: line 21: `    ;&'\n*************************************\nError testing package ** iconv-1.13.1.p3 **\n*************************************\nsage: An error occurred while testing iconv-1.13.1.p3\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /home/kirkby/sage-4.5.3.rc0/install.log.  Describe your computer, operating system, etc.\n```",
    "created_at": "2010-09-08T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92861",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

No, there's a problem if SPKG_CHECK is set to "yes" on `sage.math`. It happens to be on the bit of code I was suspicious of - i.e. line 21 of `spkg-check`

```
iconv will not be installed, as we only need to build it on
Solaris, HP-UX and Cygwin, as the system's iconv will be used
on other platforms, rather than the one shipped with Sage.
See:
    http://trac.sagemath.org/sage_trac/ticket/8567
    http://trac.sagemath.org/sage_trac/ticket/9603

real	0m0.005s
user	0m0.000s
sys	0m0.000s
Successfully installed iconv-1.13.1.p3
Running the test suite.
./spkg-check: line 21: syntax error near unexpected token `;'
./spkg-check: line 21: `    ;&'
*************************************
Error testing package ** iconv-1.13.1.p3 **
*************************************
sage: An error occurred while testing iconv-1.13.1.p3
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/kirkby/sage-4.5.3.rc0/install.log.  Describe your computer, operating system, etc.
```



---

archive/issue_comments_092862.json:
```json
{
    "body": "Replying to [comment:50 drkirkby]:\n> No, there's a problem if SPKG_CHECK is set to \"yes\" on `sage.math`.\n\n\nArgh... Update to 10.04 LTS! (Again trouble with dead old bashes... :/ )\n\nOk, I'll upload a patch fixing that.",
    "created_at": "2010-09-08T22:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92862",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:50 drkirkby]:
> No, there's a problem if SPKG_CHECK is set to "yes" on `sage.math`.


Argh... Update to 10.04 LTS! (Again trouble with dead old bashes... :/ )

Ok, I'll upload a patch fixing that.



---

archive/issue_comments_092863.json:
```json
{
    "body": "Attachment [trac_9603-iconv_spkg-fix_old_bash_problem-third_reviewer.patch](tarball://root/attachments/some-uuid/ticket9603/trac_9603-iconv_spkg-fix_old_bash_problem-third_reviewer.patch) by @nexttime created at 2010-09-08 23:11:12\n\nSPKG patch. Apply on top of second reviewer patch. (Fixes use of `;&`, which old `bash`es don't understand.)",
    "created_at": "2010-09-08T23:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92863",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_9603-iconv_spkg-fix_old_bash_problem-third_reviewer.patch](tarball://root/attachments/some-uuid/ticket9603/trac_9603-iconv_spkg-fix_old_bash_problem-third_reviewer.patch) by @nexttime created at 2010-09-08 23:11:12

SPKG patch. Apply on top of second reviewer patch. (Fixes use of `;&`, which old `bash`es don't understand.)



---

archive/issue_comments_092864.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-08T23:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92864",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092865.json:
```json
{
    "body": "Replying to [comment:51 leif]:\n> Ok, I'll upload a patch fixing that.\n\n\nDone.",
    "created_at": "2010-09-08T23:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92865",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:51 leif]:
> Ok, I'll upload a patch fixing that.


Done.



---

archive/issue_comments_092866.json:
```json
{
    "body": "Dave, do you want to apply the patch and upload a new spkg to `sage.math`?\n\n(Or I can replace the one at googlecode, but that's a bit odd since afaik those files are under revision control somehow, and that's not nice for binary / compressed files. It's \"only\" 3.7 MB though.)",
    "created_at": "2010-09-08T23:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92866",
    "user": "https://github.com/nexttime"
}
```

Dave, do you want to apply the patch and upload a new spkg to `sage.math`?

(Or I can replace the one at googlecode, but that's a bit odd since afaik those files are under revision control somehow, and that's not nice for binary / compressed files. It's "only" 3.7 MB though.)



---

archive/issue_comments_092867.json:
```json
{
    "body": "I'd rather you apply the patch and give me a .spkg to test. \n\nCan you not do it on sage.math, and leave the package there? It will be much faster all around if the package can be on the uni network. \n\nDave",
    "created_at": "2010-09-08T23:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92867",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'd rather you apply the patch and give me a .spkg to test. 

Can you not do it on sage.math, and leave the package there? It will be much faster all around if the package can be on the uni network. 

Dave



---

archive/issue_comments_092868.json:
```json
{
    "body": "Replying to [comment:54 drkirkby]:\n> I'd rather you apply the patch and give me a .spkg to test.\n\n\nI've **deleted** the old one and am currently uploading the new one with all my patches (i.e. including the third) applied. Takes a moment... (I'll update the md5sum in the description then.)\n\n> Can you not do it on sage.math, and leave the package there?\n\n\nI don't have an account.\n\n> It will be much faster all around if the package can be on the uni network. \n\n\nI suspect Google is faster... ;-) (Though using spkg-upload is a bit tedious.)",
    "created_at": "2010-09-08T23:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92868",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:54 drkirkby]:
> I'd rather you apply the patch and give me a .spkg to test.


I've **deleted** the old one and am currently uploading the new one with all my patches (i.e. including the third) applied. Takes a moment... (I'll update the md5sum in the description then.)

> Can you not do it on sage.math, and leave the package there?


I don't have an account.

> It will be much faster all around if the package can be on the uni network. 


I suspect Google is faster... ;-) (Though using spkg-upload is a bit tedious.)



---

archive/issue_comments_092869.json:
```json
{
    "body": "I'm happy with that. I assume you  are too. \n\nYou may feel it more appropriate to put us both as authors and both as reviewers. That would seem most logical to me. Leave Peter as a reviewer too, since he did make a comment before that the code looked OK, though he was unable to test it. \n\nPerhaps I can wake up and see \"positive review\". Luckily I don't have any heart problems - otherwise the shock would probably kill me!\n\nI've checked it on both platforms where it installs (Solaris, HP-UX) and where it does not (Linux). It behaves as expected. \n\nDave",
    "created_at": "2010-09-09T01:00:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92869",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm happy with that. I assume you  are too. 

You may feel it more appropriate to put us both as authors and both as reviewers. That would seem most logical to me. Leave Peter as a reviewer too, since he did make a comment before that the code looked OK, though he was unable to test it. 

Perhaps I can wake up and see "positive review". Luckily I don't have any heart problems - otherwise the shock would probably kill me!

I've checked it on both platforms where it installs (Solaris, HP-UX) and where it does not (Linux). It behaves as expected. 

Dave



---

archive/issue_comments_092870.json:
```json
{
    "body": "Shocked by positive review?",
    "created_at": "2010-09-09T05:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92870",
    "user": "https://github.com/nexttime"
}
```

Shocked by positive review?



---

archive/issue_comments_092871.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-09T05:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92871",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092872.json:
```json
{
    "body": "Replying to [comment:58 leif]:\n> Shocked by positive review?\n\n\nYes, a bit! \n\nBut seriously, I do not think it is appropriate to try to force your style of coding on someone else. I try to write code in a way that will work with virtually any Bourne shell - anyone can take code I write and it will run with almost any shell. As we see here, your stylistic changes resulted in something that would not work with the bash on `sage.math`, as that was too old. \n\nAnyway, thank you for the work you have done on the ticket. \n\nDave",
    "created_at": "2010-09-09T07:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92872",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:58 leif]:
> Shocked by positive review?


Yes, a bit! 

But seriously, I do not think it is appropriate to try to force your style of coding on someone else. I try to write code in a way that will work with virtually any Bourne shell - anyone can take code I write and it will run with almost any shell. As we see here, your stylistic changes resulted in something that would not work with the bash on `sage.math`, as that was too old. 

Anyway, thank you for the work you have done on the ticket. 

Dave



---

archive/issue_events_023919.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-16T00:48:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9603#event-23919"
}
```



---

archive/issue_comments_092873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-16T00:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9603#issuecomment-92873",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
