# Issue 3761: don't allow a sage binary to run if the processor instruction set doesn't support everything that was on the machine where sage was built

archive/issues_003761.json:
```json
{
    "body": "Assignee: cwitty\n\nHaving this in sage-support nearly *every day* is getting really old:\n\n\n```\ni get to install sage in my xubuntu (ubuntu with xfce) but when i try\nto do a simple plot, i get this error message\n\nxinelo@chacal:~/packages/sage-3.0.5-i686-Linux$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThe SAGE install tree may have moved.\nRegenerating Python.pyo and .pyc files that hardcode the install PATH\n(\nit at most a few minutes)...\nPlease do not interrupt this.\nSetting permissions of DOT_SAGE directory so only you can read and\nwrit\n| SAGE Version 3.0.5, Release Date: 2008-07-11                       |\n| Type notebook() for the GUI, and license() for information.        |\nILLEGAL INSTRUCTION...\nsomeone can help me?\nthanks\n```\n\n\nI propose that on linux systems when the script that\ndoes the \"The SAGE install tree may have moved.\" stuff is run,\nSage also does this:\n\n```\nsage@modular:~$ cat /proc/cpuinfo |grep flags|tail -1\nflags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext lm 3dnowext 3dnow up\n```\n\nand if there are any flags that were on the system where sage was -bdist'd, but which aren't on the current machine, then a big message that this binary won't work is displayed.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3761\n\n",
    "created_at": "2008-08-02T20:06:01Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "don't allow a sage binary to run if the processor instruction set doesn't support everything that was on the machine where sage was built",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3761",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

Having this in sage-support nearly *every day* is getting really old:


```
i get to install sage in my xubuntu (ubuntu with xfce) but when i try
to do a simple plot, i get this error message

xinelo@chacal:~/packages/sage-3.0.5-i686-Linux$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(
it at most a few minutes)...
Please do not interrupt this.
Setting permissions of DOT_SAGE directory so only you can read and
writ
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
ILLEGAL INSTRUCTION...
someone can help me?
thanks
```


I propose that on linux systems when the script that
does the "The SAGE install tree may have moved." stuff is run,
Sage also does this:

```
sage@modular:~$ cat /proc/cpuinfo |grep flags|tail -1
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext lm 3dnowext 3dnow up
```

and if there are any flags that were on the system where sage was -bdist'd, but which aren't on the current machine, then a big message that this binary won't work is displayed.



Issue created by migration from https://trac.sagemath.org/ticket/3761





---

archive/issue_comments_026663.json:
```json
{
    "body": "Attachment [scripts-3761.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761.patch) by @williamstein created at 2008-08-02 21:24:02",
    "created_at": "2008-08-02T21:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26663",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-3761.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761.patch) by @williamstein created at 2008-08-02 21:24:02



---

archive/issue_comments_026664.json:
```json
{
    "body": "The patch contains functions without doctests. Though, it might be a bit hard to add doctests since the result is random-ish, they should be there and marked `random`.",
    "created_at": "2008-08-10T13:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26664",
    "user": "https://github.com/malb"
}
```

The patch contains functions without doctests. Though, it might be a bit hard to add doctests since the result is random-ish, they should be there and marked `random`.



---

archive/issue_comments_026665.json:
```json
{
    "body": "The patch looks nice and I disagree with malb about the doctests since this is the scripts repo. But what should be added is the automatic generation of $SAGE_ROOT/local/lib/sage-flags.txt of -bdist since otherwise the flags file will not exist (unless created my moving the install), so it will not be really useful.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-10T18:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26665",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch looks nice and I disagree with malb about the doctests since this is the scripts repo. But what should be added is the automatic generation of $SAGE_ROOT/local/lib/sage-flags.txt of -bdist since otherwise the flags file will not exist (unless created my moving the install), so it will not be really useful.

Cheers,

Michael



---

archive/issue_comments_026666.json:
```json
{
    "body": "Actually: Why would the flags file be rewritten when the Sage install was moved? That would mean that after each install on the new target machine the file would be written and the test would always pass, not fixing the problem at all.\n\nWe should write the file *once* after building Sage, i.e. the creation should be part of the build process. Even -upgrade should not change the flags since -upgrade might only build parts of Sage, i.e. not upgrading ATLAS during -upgrade would still cause problems.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T00:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Actually: Why would the flags file be rewritten when the Sage install was moved? That would mean that after each install on the new target machine the file would be written and the test would always pass, not fixing the problem at all.

We should write the file *once* after building Sage, i.e. the creation should be part of the build process. Even -upgrade should not change the flags since -upgrade might only build parts of Sage, i.e. not upgrading ATLAS during -upgrade would still cause problems.

Cheers,

Michael



---

archive/issue_comments_026667.json:
```json
{
    "body": "For the patch **scripts-3761.patch**, here are some possible documentation fixes:\n\n\n\n1.\n\n```\n-moved make sure the location and processor flags files are\n+moved, make sure the location and processor flags files are\n```\n\nSo after applying that diff, you'd get this documentation snippet:\n\n```\n\"\"\"\nCheck whether or not this install of Sage moved.  If it hasn't \nmoved, make sure the location and processor flags files are \nwritten. \n\"\"\" \n```\n\nI know I'm nit-picking, but the second sentence is rather long. Leaving out the extra comma won't change what you're trying to say with that sentence. But it can take some time for readers (including yours truly) to figure out what you're saying. I think the extra comma would make it easier to read your documentation.\n\n\n\n2.\n\n```\n-# On a system without /proc/cpuinfo, so don't bother In\n+# On a system without /proc/cpuinfo, so don't bother. In\n```\n",
    "created_at": "2008-10-27T04:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

For the patch **scripts-3761.patch**, here are some possible documentation fixes:



1.

```
-moved make sure the location and processor flags files are
+moved, make sure the location and processor flags files are
```

So after applying that diff, you'd get this documentation snippet:

```
"""
Check whether or not this install of Sage moved.  If it hasn't 
moved, make sure the location and processor flags files are 
written. 
""" 
```

I know I'm nit-picking, but the second sentence is rather long. Leaving out the extra comma won't change what you're trying to say with that sentence. But it can take some time for readers (including yours truly) to figure out what you're saying. I think the extra comma would make it easier to read your documentation.



2.

```
-# On a system without /proc/cpuinfo, so don't bother In
+# On a system without /proc/cpuinfo, so don't bother. In
```




---

archive/issue_comments_026668.json:
```json
{
    "body": "I've made no changes to this patch.  Michael has refused to give it a positive review, since he claims (in the review above and in person) that the flags file is deleted and rewritten whenever the install moves.   However, he's wrong.   I just read the code and there is exactly *one* place that the flags file is written:\n\n```\n        16          # Write the flags file if it isn't there. \n \t17\t    if not os.path.exists(flags_file): \n \t18\t        write_flags_file() \n```\n\nSince flags_file is never deleted, and is only written when the flags_file doesn't exist, it can't be deleted or overwritten when the install moves.   So I don't see what the problem is.\n\nWilliam",
    "created_at": "2008-11-09T23:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26668",
    "user": "https://github.com/williamstein"
}
```

I've made no changes to this patch.  Michael has refused to give it a positive review, since he claims (in the review above and in person) that the flags file is deleted and rewritten whenever the install moves.   However, he's wrong.   I just read the code and there is exactly *one* place that the flags file is written:

```
        16          # Write the flags file if it isn't there. 
 	17	    if not os.path.exists(flags_file): 
 	18	        write_flags_file() 
```

Since flags_file is never deleted, and is only written when the flags_file doesn't exist, it can't be deleted or overwritten when the install moves.   So I don't see what the problem is.

William



---

archive/issue_comments_026669.json:
```json
{
    "body": "Hi William,\n>I just read the code and there is exactly *one* place that the flags file is written\nyeah, but that might be too late. Take the following use case:\n\n- unpack a Sage src distribution\n\n- type \"make\" in the SAGE_ROOT directory\n\n- type \"./sage -bdist Test\" in that directory\n\nand you get a binary distribution which lacks the flags_file, rendering its introduction pretty useless.\n\nThe whole point is that the \"sage-location\" script, where the flags file is written, is never called in the above sequence.\n\nMichaels first post says implicitly he would like to have the \"sage-bdist\" script call \"sage-location\" (say right at its start). His second post says he would like to have \"sage-location\" being called somewhere in the build process started by \"make\", say in the script \"spkg/install\" right after the line \"time make -f standard/deps $1\" near the end.\n\nIMHO it would be a good idea to do both. I give a positive review to this ticket provided these two trivial one-liners are added.\n\n(Someone actually should have tested the case of moving such a protected Sage distro from one Linux system to another Linux system where the new protection mechanism barfs about missing flags. I can't do it myself because currently I have only very limited access to some Linux system. OTOH, the worst thing to happen is that we get \"false positives\". This is the current situation, so there ... let's include this code until someone has a better solution.)\n\nCheers,\n\ngsw",
    "created_at": "2008-11-10T22:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26669",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi William,
>I just read the code and there is exactly *one* place that the flags file is written
yeah, but that might be too late. Take the following use case:

- unpack a Sage src distribution

- type "make" in the SAGE_ROOT directory

- type "./sage -bdist Test" in that directory

and you get a binary distribution which lacks the flags_file, rendering its introduction pretty useless.

The whole point is that the "sage-location" script, where the flags file is written, is never called in the above sequence.

Michaels first post says implicitly he would like to have the "sage-bdist" script call "sage-location" (say right at its start). His second post says he would like to have "sage-location" being called somewhere in the build process started by "make", say in the script "spkg/install" right after the line "time make -f standard/deps $1" near the end.

IMHO it would be a good idea to do both. I give a positive review to this ticket provided these two trivial one-liners are added.

(Someone actually should have tested the case of moving such a protected Sage distro from one Linux system to another Linux system where the new protection mechanism barfs about missing flags. I can't do it myself because currently I have only very limited access to some Linux system. OTOH, the worst thing to happen is that we get "false positives". This is the current situation, so there ... let's include this code until someone has a better solution.)

Cheers,

gsw



---

archive/issue_comments_026670.json:
```json
{
    "body": "> and you get a binary distribution which lacks the flags_file, rendering its \n> introduction pretty useless.\n\n> The whole point is that the \"sage-location\" script, where the flags file \n> is written, is never called in the above sequence. \n\nWrong?  The step\n\n```\n  - type \"make\" in the SAGE_ROOT directory\n```\n\nat some point involves running Sage, and once Sage is run the sage-location script gets called. \n\nWilliam",
    "created_at": "2008-11-11T19:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26670",
    "user": "https://github.com/williamstein"
}
```

> and you get a binary distribution which lacks the flags_file, rendering its 
> introduction pretty useless.

> The whole point is that the "sage-location" script, where the flags file 
> is written, is never called in the above sequence. 

Wrong?  The step

```
  - type "make" in the SAGE_ROOT directory
```

at some point involves running Sage, and once Sage is run the sage-location script gets called. 

William



---

archive/issue_comments_026671.json:
```json
{
    "body": "Mhh:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin$ patch -p1 < scripts-3761.patch\\?format\\=raw \npatching file sage-location\nHunk #1 FAILED at 2.\nHunk #2 FAILED at 130.\n2 out of 2 hunks FAILED -- saving rejects to file sage-location.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-11T20:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mhh:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin$ patch -p1 < scripts-3761.patch\?format\=raw 
patching file sage-location
Hunk #1 FAILED at 2.
Hunk #2 FAILED at 130.
2 out of 2 hunks FAILED -- saving rejects to file sage-location.rej
```


Cheers,

Michael



---

archive/issue_comments_026672.json:
```json
{
    "body": "Attachment [scripts-3761-3.2.alpha3.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761-3.2.alpha3.patch) by @williamstein created at 2008-11-12 03:51:06",
    "created_at": "2008-11-12T03:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26672",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-3761-3.2.alpha3.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761-3.2.alpha3.patch) by @williamstein created at 2008-11-12 03:51:06



---

archive/issue_comments_026673.json:
```json
{
    "body": "I posted a rebased patch.  Let me know if there are any problems.",
    "created_at": "2008-11-12T03:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26673",
    "user": "https://github.com/williamstein"
}
```

I posted a rebased patch.  Let me know if there are any problems.



---

archive/issue_comments_026674.json:
```json
{
    "body": ">>     and you get a binary distribution which lacks the flags_file, rendering its >>introduction pretty useless.\n>>\n>>    The whole point is that the \"sage-location\" script, where the flags file is >>written, is never called in the above sequence.\n>\n>Wrong? The step\n\n```\n  - type \"make\" in the SAGE_ROOT directory\n```\n\n>at some point involves running Sage, and once Sage is run the sage-location script gets called.\n>\n>William\n\nI was sure I checked that this was not the case, i.e. Sage itself was not started during the \"make\" run ... I'll double check it again with Sage 3.2.rc0 as soon as I get home this evening. Thanks for rebasing the patch!\n\nCheers, gsw",
    "created_at": "2008-11-12T09:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26674",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

>>     and you get a binary distribution which lacks the flags_file, rendering its >>introduction pretty useless.
>>
>>    The whole point is that the "sage-location" script, where the flags file is >>written, is never called in the above sequence.
>
>Wrong? The step

```
  - type "make" in the SAGE_ROOT directory
```

>at some point involves running Sage, and once Sage is run the sage-location script gets called.
>
>William

I was sure I checked that this was not the case, i.e. Sage itself was not started during the "make" run ... I'll double check it again with Sage 3.2.rc0 as soon as I get home this evening. Thanks for rebasing the patch!

Cheers, gsw



---

archive/issue_comments_026675.json:
```json
{
    "body": "Begging your pardon, but I just did:\n\n```\nsusanne-webers-computer:~/Public/sage georgweber$ tar -xf sage-3.2.rc0.tar\nsusanne-webers-computer:~/Public/sage georgweber$ cd sage-3.2.rc0\nsusanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ make\n.\n.\nSAGE build/upgrade complete!\nsusanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt\nls: local/lib/*.txt: No such file or directory\nsusanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls ../sage-3.2.alpha2/local/lib/*.txt\n../sage-3.2.alpha2/local/lib/sage-current-location.txt\n```\n\nSo Sage cannot have been called during the \"make\" run, otherwise the \"sage-location\" script would have been called.\n\n(The last two lines show that I did run Sage at least once with my former Sage 3.2.alpha2 copy.)\n\nI intend to post another ticket with the trivial one-liner patch I proposed in a minute, but before I do that, I just have to check whether my potential fix for trac #4500 works, that I have created, while waiting for the \"make\" run to complete.",
    "created_at": "2008-11-12T22:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26675",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Begging your pardon, but I just did:

```
susanne-webers-computer:~/Public/sage georgweber$ tar -xf sage-3.2.rc0.tar
susanne-webers-computer:~/Public/sage georgweber$ cd sage-3.2.rc0
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ make
.
.
SAGE build/upgrade complete!
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt
ls: local/lib/*.txt: No such file or directory
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls ../sage-3.2.alpha2/local/lib/*.txt
../sage-3.2.alpha2/local/lib/sage-current-location.txt
```

So Sage cannot have been called during the "make" run, otherwise the "sage-location" script would have been called.

(The last two lines show that I did run Sage at least once with my former Sage 3.2.alpha2 copy.)

I intend to post another ticket with the trivial one-liner patch I proposed in a minute, but before I do that, I just have to check whether my potential fix for trac #4500 works, that I have created, while waiting for the "make" run to complete.



---

archive/issue_comments_026676.json:
```json
{
    "body": "No other ticket because I don't know how to post a patch for the file \"spkg-install\" in the spkg \"sage_scripts-3.2.rc0\".\n\nBut the patch I had in mind is trivial: Just add one line at the end of this script with \"sage-location\" (actually a call) on it, thus calling the \"sage-location\" script once during installation, at a time where we definitely know it exists.\n\nMichael, William, what do you think?\n\nCheers, gsw",
    "created_at": "2008-11-13T00:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26676",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

No other ticket because I don't know how to post a patch for the file "spkg-install" in the spkg "sage_scripts-3.2.rc0".

But the patch I had in mind is trivial: Just add one line at the end of this script with "sage-location" (actually a call) on it, thus calling the "sage-location" script once during installation, at a time where we definitely know it exists.

Michael, William, what do you think?

Cheers, gsw



---

archive/issue_comments_026677.json:
```json
{
    "body": "> But the patch I had in mind is trivial: Just add one line \n> at the end of this script with \"sage-location\" (actually a \n> call) on it, thus calling the \"sage-location\" script once \n> during installation, at a time where we definitely know it exists.\n> Michael, William, what do you think?\n> Cheers, gsw \n\nSince sage_scripts is basically the first thing installed during the sage build from source process, I'm worried that won't work.  In fact, it definitely won't on some systems, because the first line of sage-location is:\n\n```/usr/bin/env sage.bin\n```\n\n\nI'm surprised that sage is never run during \"make\"; it certainly used to be run, which resulted in some complaints (since people building as root were annoyed that /root got modified).   That said, you're right and I'm glad you pointed this out!! It not being run never broke the sage-location stuff for me, since my scripts to build the Sage binaries always do \"make check\" before making the binary (a very good idea!), and that of course runs Sage.   I mean, in my opinion it would be really dumb to ever do \"sage -bdist\" without once starting Sage, since you could be building a binary that certainly doesn't work. \n\nWhat about adding a line to sage-bdist to run Sage once?  And even checking that the run actually worked, since that's a good test, and refusing to make the bdist if Sage won't even run. \n\n -- William",
    "created_at": "2008-11-13T01:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26677",
    "user": "https://github.com/williamstein"
}
```

> But the patch I had in mind is trivial: Just add one line 
> at the end of this script with "sage-location" (actually a 
> call) on it, thus calling the "sage-location" script once 
> during installation, at a time where we definitely know it exists.
> Michael, William, what do you think?
> Cheers, gsw 

Since sage_scripts is basically the first thing installed during the sage build from source process, I'm worried that won't work.  In fact, it definitely won't on some systems, because the first line of sage-location is:

```/usr/bin/env sage.bin
```


I'm surprised that sage is never run during "make"; it certainly used to be run, which resulted in some complaints (since people building as root were annoyed that /root got modified).   That said, you're right and I'm glad you pointed this out!! It not being run never broke the sage-location stuff for me, since my scripts to build the Sage binaries always do "make check" before making the binary (a very good idea!), and that of course runs Sage.   I mean, in my opinion it would be really dumb to ever do "sage -bdist" without once starting Sage, since you could be building a binary that certainly doesn't work. 

What about adding a line to sage-bdist to run Sage once?  And even checking that the run actually worked, since that's a good test, and refusing to make the bdist if Sage won't even run. 

 -- William



---

archive/issue_comments_026678.json:
```json
{
    "body": "apply this after the scripts patch above.  This makes sure that \"sage -bdist\" runs Sage at least once before building the bdist.",
    "created_at": "2008-11-13T01:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26678",
    "user": "https://github.com/williamstein"
}
```

apply this after the scripts patch above.  This makes sure that "sage -bdist" runs Sage at least once before building the bdist.



---

archive/issue_comments_026679.json:
```json
{
    "body": "Attachment [scripts-3761-PART2-bdist.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761-PART2-bdist.patch) by @williamstein created at 2008-11-13 01:32:54\n\nI attached a patch that makes sure sage runs right when one does \"sage -bdist\".",
    "created_at": "2008-11-13T01:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26679",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-3761-PART2-bdist.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761-PART2-bdist.patch) by @williamstein created at 2008-11-13 01:32:54

I attached a patch that makes sure sage runs right when one does "sage -bdist".



---

archive/issue_comments_026680.json:
```json
{
    "body": "Agreed, positive review.\n\n`@`Michael: I have access to a Sage installation only in ~ 10 hours from now on, so I could only \"code-review\" the PART2 - patch. I don't think there is much space for a typo in it to break it for a trivial reason, but one never knows. Please either wait half a day, I do intend do see that \"alive and working\" with my own eyes, or just test it out yourself. (\"rm $SAGE_ROOT/local/lib/*.txt\" and then \"sage -bdist\" ...)\n\nCheers, gsw",
    "created_at": "2008-11-13T09:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26680",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Agreed, positive review.

`@`Michael: I have access to a Sage installation only in ~ 10 hours from now on, so I could only "code-review" the PART2 - patch. I don't think there is much space for a typo in it to break it for a trivial reason, but one never knows. Please either wait half a day, I do intend do see that "alive and working" with my own eyes, or just test it out yourself. ("rm $SAGE_ROOT/local/lib/*.txt" and then "sage -bdist" ...)

Cheers, gsw



---

archive/issue_comments_026681.json:
```json
{
    "body": "Sigh.\n\nAnything that isn't tested will not work. QED.\n\nSeveral issues remain, to show just two:\n\n```\nsusanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt\nls: local/lib/*.txt: No such file or directory\nsusanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ./sage -bdist\n** MISSING VERSION NUMBER! ** \nSage works!\nUsage: /Users/georgweber/Public/sage/sage-3.2.rc0/local/bin/sage-bdist <SAGE_VERSION> <SAGE_ROOT>\nsusanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt\nls: local/lib/*.txt: No such file or directory\n```\n\nApart from the annoying fact that the fat error message is displayed, and then the job continues and calls ' sage -c \"print 'Sage works!'\" ' nevertheless, this latter command does not seem to call \"sage-location\" ... and we're trapped in the \"make\" run behaviour again.\n\nIt is pretty obvious who to heal the \"Part2\" patch for sage-bdist, and now I'll turn things round: this time I'm really going to that myself, and then let somebody else review it :-)",
    "created_at": "2008-11-13T20:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26681",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Sigh.

Anything that isn't tested will not work. QED.

Several issues remain, to show just two:

```
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt
ls: local/lib/*.txt: No such file or directory
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ./sage -bdist
** MISSING VERSION NUMBER! ** 
Sage works!
Usage: /Users/georgweber/Public/sage/sage-3.2.rc0/local/bin/sage-bdist <SAGE_VERSION> <SAGE_ROOT>
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt
ls: local/lib/*.txt: No such file or directory
```

Apart from the annoying fact that the fat error message is displayed, and then the job continues and calls ' sage -c "print 'Sage works!'" ' nevertheless, this latter command does not seem to call "sage-location" ... and we're trapped in the "make" run behaviour again.

It is pretty obvious who to heal the "Part2" patch for sage-bdist, and now I'll turn things round: this time I'm really going to that myself, and then let somebody else review it :-)



---

archive/issue_comments_026682.json:
```json
{
    "body": "apply this after the scripts patch above. This makes sure that \"sage -bdist\" runs Sage at least once before building the bdist. Hopefully now really ...",
    "created_at": "2008-11-13T20:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26682",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

apply this after the scripts patch above. This makes sure that "sage -bdist" runs Sage at least once before building the bdist. Hopefully now really ...



---

archive/issue_comments_026683.json:
```json
{
    "body": "Attachment [scripts-3761-PART2fixed-bdist.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761-PART2fixed-bdist.patch) by GeorgSWeber created at 2008-11-13 20:50:45\n\nOK, here we go:\n\nI give the \"sage-location\" patch of William a positive review (apply only the rebased one) pending an epsilon --- a PART2 patch is needed.\n\nI give the \"sage-bdist\" PART2 patch of William a negative review (reason: see my post above).\n\nI kindly ask for my own \"sage-bdist\" PART2fixed patch (to be applied together with the first patch) to be reviewed, so yet another of the thousands of tickets can finally be closed in O(1) time --- on a positive review of this Part2fixed patch, the remaining epsilon is supplied, thus giving the ticket as such a positive review.\n\nCheers, gsw\n\n(goes off and fetches a beer)",
    "created_at": "2008-11-13T20:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26683",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [scripts-3761-PART2fixed-bdist.patch](tarball://root/attachments/some-uuid/ticket3761/scripts-3761-PART2fixed-bdist.patch) by GeorgSWeber created at 2008-11-13 20:50:45

OK, here we go:

I give the "sage-location" patch of William a positive review (apply only the rebased one) pending an epsilon --- a PART2 patch is needed.

I give the "sage-bdist" PART2 patch of William a negative review (reason: see my post above).

I kindly ask for my own "sage-bdist" PART2fixed patch (to be applied together with the first patch) to be reviewed, so yet another of the thousands of tickets can finally be closed in O(1) time --- on a positive review of this Part2fixed patch, the remaining epsilon is supplied, thus giving the ticket as such a positive review.

Cheers, gsw

(goes off and fetches a beer)



---

archive/issue_comments_026684.json:
```json
{
    "body": "I agree that my original patch didn't work, but that was because of a bug in sage-sage.   Your patch scripts-3761-PART2fixed-bdist.patch just programs around that bug instead of fixing it.    The bug is that `sage -c \"...\"` doesn't run sage-location.  This came up when I was fixing #4515, so the first patch there fixes this bug.  After applying that patch (the first at #4515), one should apply the following:\n\n```\nscripts-3761-3.2.alpha3.patch\nscripts-3761-PART2-bdist.patch\n```\n",
    "created_at": "2008-11-13T23:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26684",
    "user": "https://github.com/williamstein"
}
```

I agree that my original patch didn't work, but that was because of a bug in sage-sage.   Your patch scripts-3761-PART2fixed-bdist.patch just programs around that bug instead of fixing it.    The bug is that `sage -c "..."` doesn't run sage-location.  This came up when I was fixing #4515, so the first patch there fixes this bug.  After applying that patch (the first at #4515), one should apply the following:

```
scripts-3761-3.2.alpha3.patch
scripts-3761-PART2-bdist.patch
```




---

archive/issue_comments_026685.json:
```json
{
    "body": "> Cheers, gsw\n> (goes off and fetches a beer) \n\nIf I recall correctly, last time we had a beer together it was non-alcoholic :-)",
    "created_at": "2008-11-14T00:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26685",
    "user": "https://github.com/williamstein"
}
```

> Cheers, gsw
> (goes off and fetches a beer) 

If I recall correctly, last time we had a beer together it was non-alcoholic :-)



---

archive/issue_comments_026686.json:
```json
{
    "body": "OK, I'm fine with he redefinition of \"epsilon\" to mean \"sage-4515-sage_c_bug.patch\".\n\nSince I just gave the entire #4515 a positive review, next try:\n\nPositive review for this ticket (Wiliams two patches) pending the prior inclusion of #4515.\n\n`@`William: I couldn't possibly make it to Loria (nice photos of you all, by the way!), but I surely do intend to attend some SD xy. Anyway, hope to see you again!\n\nCheers, gsw",
    "created_at": "2008-11-14T22:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26686",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

OK, I'm fine with he redefinition of "epsilon" to mean "sage-4515-sage_c_bug.patch".

Since I just gave the entire #4515 a positive review, next try:

Positive review for this ticket (Wiliams two patches) pending the prior inclusion of #4515.

`@`William: I couldn't possibly make it to Loria (nice photos of you all, by the way!), but I surely do intend to attend some SD xy. Anyway, hope to see you again!

Cheers, gsw



---

archive/issue_comments_026687.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T04:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026688.json:
```json
{
    "body": "Merged scripts-3761-3.2.alpha3.patch and scripts-3761-PART2-bdist.patch in Sage 3.2.rc1",
    "created_at": "2008-11-15T04:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3761#issuecomment-26688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged scripts-3761-3.2.alpha3.patch and scripts-3761-PART2-bdist.patch in Sage 3.2.rc1



---

archive/issue_events_003983.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-15T04:58:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3761",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3761#event-3983"
}
```
