# Issue 9210: pkg-config's prefix statements in SAGE_LOCAL/lib/pkgconfig not changed upon Sage move

archive/issues_009210.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirkby @kcrisman\n\nThe attached patch fixes the above issue which causes matplotlib to pick up the system freetype2 after moving Sage (even after #9208).  One thing led to another and I ended up restructuring and rewriting lots of the code in the file too.  I hope it's cleaner and has less portability issues (I changed a lot of things to use os.path.join, for example).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9210\n\n",
    "closed_at": "2010-10-21T10:07:28Z",
    "created_at": "2010-06-11T04:12:13Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "pkg-config's prefix statements in SAGE_LOCAL/lib/pkgconfig not changed upon Sage move",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9210",
    "user": "https://github.com/jasongrout"
}
```
Assignee: drkirkby

CC:  drkirkby @kcrisman

The attached patch fixes the above issue which causes matplotlib to pick up the system freetype2 after moving Sage (even after #9208).  One thing led to another and I ended up restructuring and rewriting lots of the code in the file too.  I hope it's cleaner and has less portability issues (I changed a lot of things to use os.path.join, for example).

Issue created by migration from https://trac.sagemath.org/ticket/9210





---

archive/issue_comments_086066.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-11T06:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86066",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086067.json:
```json
{
    "body": "Note that if you've already moved your build directory, you will have to move it again to trigger the code in this patch that updates the pkg-config file paths.",
    "created_at": "2010-06-11T06:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86067",
    "user": "https://github.com/jasongrout"
}
```

Note that if you've already moved your build directory, you will have to move it again to trigger the code in this patch that updates the pkg-config file paths.



---

archive/issue_comments_086068.json:
```json
{
    "body": "#5776 is related (it's a general ticket about the stuff that old paths that still hang around in various places).",
    "created_at": "2010-06-11T06:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86068",
    "user": "https://github.com/jasongrout"
}
```

#5776 is related (it's a general ticket about the stuff that old paths that still hang around in various places).



---

archive/issue_comments_086069.json:
```json
{
    "body": "In the R .pc file, there are still some other directories that are not changed (besides just the prefix directory).",
    "created_at": "2010-06-11T16:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86069",
    "user": "https://github.com/jasongrout"
}
```

In the R .pc file, there are still some other directories that are not changed (besides just the prefix directory).



---

archive/issue_comments_086070.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-11T16:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86070",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086071.json:
```json
{
    "body": "Attachment [trac-9210-rewrite-sage-location.patch](tarball://root/attachments/some-uuid/ticket9210/trac-9210-rewrite-sage-location.patch) by @jasongrout created at 2010-06-11 20:39:14\n\napply to sage-scripts repository",
    "created_at": "2010-06-11T20:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86071",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9210-rewrite-sage-location.patch](tarball://root/attachments/some-uuid/ticket9210/trac-9210-rewrite-sage-location.patch) by @jasongrout created at 2010-06-11 20:39:14

apply to sage-scripts repository



---

archive/issue_comments_086072.json:
```json
{
    "body": "Updated script to initially set a SAGE_ROOT variable inside the file, and then just update that variable.  This should take care of all paths in the file that need to be changed.",
    "created_at": "2010-06-11T20:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86072",
    "user": "https://github.com/jasongrout"
}
```

Updated script to initially set a SAGE_ROOT variable inside the file, and then just update that variable.  This should take care of all paths in the file that need to be changed.



---

archive/issue_comments_086073.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-11T20:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86073",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086074.json:
```json
{
    "body": "I've started to build the binary on my old Blade 1000. It's not the fastest machine in the world, (not even the fastest SPARC I own, but its convenient at the minute). It will take a few hours to build this, unpack it, then check for hard-coded paths. But I'm working on it. If I can stay awake, I might have something by 0200 GMT on Saturday. \n\nDave",
    "created_at": "2010-06-11T21:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86074",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've started to build the binary on my old Blade 1000. It's not the fastest machine in the world, (not even the fastest SPARC I own, but its convenient at the minute). It will take a few hours to build this, unpack it, then check for hard-coded paths. But I'm working on it. If I can stay awake, I might have something by 0200 GMT on Saturday. 

Dave



---

archive/issue_comments_086075.json:
```json
{
    "body": "It was a lot quicker than I expected. \n\nSomething has gone wrong here though. The installation worked fine before it was moved. First I create the binary. \n\n```\ndrkirkby@redstart:~/32/sage-4.4.3$ ./sage -bdist 4.4.3-ax                                                 \nSage works!\nCopying files over to tmp directory\nlocal/lib/python2.6/python2.6: failed to get acl entries\nlocal/lib/libgfortran.so: failed to get acl entries\ncp: cannot access *.sage\nCopying Sage library over\nMaking empty spkg's\n```\n\nI think we need to copy libgfortran (see #8049) though the failure to do so should not cause me a problem, as the system has it. But when I tried to move the distribution, I get:\n\n```\n-bash-3.00$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThe Sage install tree may have moved\n(from /export/home/drkirkby/32/sage-4.4.3 to /export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS)\nChanging various hardcoded paths\n(please wait at most a few minutes)...\nDo not interrupt this.\nDone resetting paths\n| Sage Version 4.4.3, Release Date: 2010-06-04                       |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\nI don't have gdb on this machine. I'll investigate, but for now, there may be a problem here. \n\n\n\nDave",
    "created_at": "2010-06-11T22:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86075",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It was a lot quicker than I expected. 

Something has gone wrong here though. The installation worked fine before it was moved. First I create the binary. 

```
drkirkby@redstart:~/32/sage-4.4.3$ ./sage -bdist 4.4.3-ax                                                 
Sage works!
Copying files over to tmp directory
local/lib/python2.6/python2.6: failed to get acl entries
local/lib/libgfortran.so: failed to get acl entries
cp: cannot access *.sage
Copying Sage library over
Making empty spkg's
```

I think we need to copy libgfortran (see #8049) though the failure to do so should not cause me a problem, as the system has it. But when I tried to move the distribution, I get:

```
-bash-3.00$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The Sage install tree may have moved
(from /export/home/drkirkby/32/sage-4.4.3 to /export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS)
Changing various hardcoded paths
(please wait at most a few minutes)...
Do not interrupt this.
Done resetting paths
| Sage Version 4.4.3, Release Date: 2010-06-04                       |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

I don't have gdb on this machine. I'll investigate, but for now, there may be a problem here. 



Dave



---

archive/issue_comments_086076.json:
```json
{
    "body": "On closer inspection, gdb was on the machine, so I run sage with the option -gdb.\n\nThe SIGSEGV seems to be caused by Singular failing to find a file 'tesths.cc' though that file does exist. \n\n```\n-bash-3.00$ export PATH=$PATH:/usr/local/bin\n-bash-3.00$ ./sage -gdb\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS/local/bin/sage-ipython\nGNU gdb (GDB) 7.0.1\nCopyright (C) 2009 Free Software Foundation, Inc.\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.  Type \"show copying\"\nand \"show warranty\" for details.\nThis GDB was configured as \"sparc-sun-solaris2.10\".\nFor bug reporting instructions, please see:\n<http://www.gnu.org/software/gdb/bugs/>...\nReading symbols from /export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS/local/bin/python...done.\n[Thread debugging using libthread_db enabled]\n[New Thread 1 (LWP 1)]\nPython 2.6.4 (r264:75706, Jun  6 2010, 00:37:24) \n[GCC 4.4.3] on sunos5\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n| Sage Version 4.4.3, Release Date: 2010-06-04                       |\n| Type notebook() for the GUI, and license() for information.        |\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 1 (LWP 1)]\nsiInit (name=0x1e169b4 <error reading variable>) at tesths.cc:65\n65      tesths.cc: No such file or directory.\n        in tesths.cc\nCurrent language:  auto\nThe current source language is \"auto; currently c++\".\n(gdb) quit\nA debugging session is active.\n\n        Inferior 1 [process 6182    ] will be killed.\n\nQuit anyway? (y or n) y\n-bash-3.00$ find . -name tesths.cc\n./spkg/standard/singular-3.1.0.4.p6/src/Singular/tesths.cc\n-bash-3.00$ cat ./spkg/standard/singular-3.1.0.4.p6/src/Singular/tesths.cc\n/****************************************\n*  Computer Algebra System SINGULAR     *\n****************************************/\n/* $Id: tesths.cc,v 1.115 2008/09/10 09:33:58 Singular Exp $ */\n```\n\nDo you think this can be related? It was fine before the distribution was moved. \n\nDave",
    "created_at": "2010-06-11T22:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86076",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

On closer inspection, gdb was on the machine, so I run sage with the option -gdb.

The SIGSEGV seems to be caused by Singular failing to find a file 'tesths.cc' though that file does exist. 

```
-bash-3.00$ export PATH=$PATH:/usr/local/bin
-bash-3.00$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS/local/bin/sage-ipython
GNU gdb (GDB) 7.0.1
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "sparc-sun-solaris2.10".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS/local/bin/python...done.
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]
Python 2.6.4 (r264:75706, Jun  6 2010, 00:37:24) 
[GCC 4.4.3] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
| Sage Version 4.4.3, Release Date: 2010-06-04                       |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 1 (LWP 1)]
siInit (name=0x1e169b4 <error reading variable>) at tesths.cc:65
65      tesths.cc: No such file or directory.
        in tesths.cc
Current language:  auto
The current source language is "auto; currently c++".
(gdb) quit
A debugging session is active.

        Inferior 1 [process 6182    ] will be killed.

Quit anyway? (y or n) y
-bash-3.00$ find . -name tesths.cc
./spkg/standard/singular-3.1.0.4.p6/src/Singular/tesths.cc
-bash-3.00$ cat ./spkg/standard/singular-3.1.0.4.p6/src/Singular/tesths.cc
/****************************************
*  Computer Algebra System SINGULAR     *
****************************************/
/* $Id: tesths.cc,v 1.115 2008/09/10 09:33:58 Singular Exp $ */
```

Do you think this can be related? It was fine before the distribution was moved. 

Dave



---

archive/issue_comments_086077.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-06-11T22:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86077",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_086078.json:
```json
{
    "body": "It doesn't seem like it should be related (i.e., my guess is that you'd have this problem without the patch as well).  Can you zip up the SAGE_LOCAL/lib/pkgconfig/ directory and the SAGE_LOCAL/lib/sage-current-location.txt file so I can just double-check that the paths are right?",
    "created_at": "2010-06-11T23:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86078",
    "user": "https://github.com/jasongrout"
}
```

It doesn't seem like it should be related (i.e., my guess is that you'd have this problem without the patch as well).  Can you zip up the SAGE_LOCAL/lib/pkgconfig/ directory and the SAGE_LOCAL/lib/sage-current-location.txt file so I can just double-check that the paths are right?



---

archive/issue_comments_086079.json:
```json
{
    "body": "Sure. I've attached two .tar.gz files. It should be obvious which is which from the name. Note I created a second user account to test the moved version on, so you might see different user names on the two tarballs.",
    "created_at": "2010-06-12T00:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86079",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Sure. I've attached two .tar.gz files. It should be obvious which is which from the name. Note I created a second user account to test the moved version on, so you might see different user names on the two tarballs.



---

archive/issue_comments_086080.json:
```json
{
    "body": "After creating a binary distribution and moving it to somewhere else.",
    "created_at": "2010-06-12T00:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86080",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

After creating a binary distribution and moving it to somewhere else.



---

archive/issue_comments_086081.json:
```json
{
    "body": "Attachment [before-moving.tar.gz](tarball://root/attachments/some-uuid/ticket9210/before-moving.tar.gz) by drkirkby created at 2010-06-12 00:54:33\n\nThe files were Sage was built.",
    "created_at": "2010-06-12T00:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86081",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [before-moving.tar.gz](tarball://root/attachments/some-uuid/ticket9210/before-moving.tar.gz) by drkirkby created at 2010-06-12 00:54:33

The files were Sage was built.



---

archive/issue_comments_086082.json:
```json
{
    "body": "Enough stuff looked fishy in your output that I have to ask: Are you using the most recent version of the patch?  From the pkg-config files, it doesn't look like it.\n\nWhat commands are you running?  The following two sequences of commands should work to update the .pc files:\n\n1. Build sage from source in directory A\n\n2. Run Sage (this may be optional---it depends on if the build creates a correct local/lib/sage-current-location.txt file)\n\n3. Move the sage build directory to directory B\n\n4. Run Sage in the new directory (this updates the sage-current-location.txt file, and also updates the .pc files, etc.)\n\nThen the file paths should be updated.\n\nAlternatively, this should work:\n\n1. Build sage from source in directory A\n\n2. Make a bdist (this automatically runs Sage, so it takes care of step 2 above)\n\n3. Extract the bdist\n\n4. Run Sage in the new directory (this updates the sage-current-location.txt file, and also updates the .pc files, etc.)\n\n\nIn either situation, at the top of each local/lib/pkgconfig/*.pc file, there should be a SAGE_ROOT=new directory after step 3, and the local/lib/sage-current-location.txt file should also contain the new directory name.  Neither of those are true for your attached outputs, so I think either you are using the old version of the patch or didn't follow one of the steps.  Or my code has a bug :).",
    "created_at": "2010-06-12T02:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86082",
    "user": "https://github.com/jasongrout"
}
```

Enough stuff looked fishy in your output that I have to ask: Are you using the most recent version of the patch?  From the pkg-config files, it doesn't look like it.

What commands are you running?  The following two sequences of commands should work to update the .pc files:

1. Build sage from source in directory A

2. Run Sage (this may be optional---it depends on if the build creates a correct local/lib/sage-current-location.txt file)

3. Move the sage build directory to directory B

4. Run Sage in the new directory (this updates the sage-current-location.txt file, and also updates the .pc files, etc.)

Then the file paths should be updated.

Alternatively, this should work:

1. Build sage from source in directory A

2. Make a bdist (this automatically runs Sage, so it takes care of step 2 above)

3. Extract the bdist

4. Run Sage in the new directory (this updates the sage-current-location.txt file, and also updates the .pc files, etc.)


In either situation, at the top of each local/lib/pkgconfig/*.pc file, there should be a SAGE_ROOT=new directory after step 3, and the local/lib/sage-current-location.txt file should also contain the new directory name.  Neither of those are true for your attached outputs, so I think either you are using the old version of the patch or didn't follow one of the steps.  Or my code has a bug :).



---

archive/issue_comments_086083.json:
```json
{
    "body": "Replying to [comment:10 jason]:\n \n> In either situation, at the top of each local/lib/pkgconfig/*.pc file, there should be a SAGE_ROOT=new directory after step 3\n\n\nI meant after step 4.",
    "created_at": "2010-06-12T02:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86083",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:10 jason]:
 
> In either situation, at the top of each local/lib/pkgconfig/*.pc file, there should be a SAGE_ROOT=new directory after step 3


I meant after step 4.



---

archive/issue_comments_086084.json:
```json
{
    "body": "I'll have to look at this later today - it is 3:19 am here! It's possible I don't have the latest patch, or I've somehow mess up installing it. Could you attach the full file (not just the patch) of whatever you think I might have wrong. I'll then copy that in directly. \n\nDave",
    "created_at": "2010-06-12T02:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86084",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'll have to look at this later today - it is 3:19 am here! It's possible I don't have the latest patch, or I've somehow mess up installing it. Could you attach the full file (not just the patch) of whatever you think I might have wrong. I'll then copy that in directly. 

Dave



---

archive/issue_comments_086085.json:
```json
{
    "body": "I thought I might have messed up, as I was tired, but as far as I can see, I do get a problem.\n\nThe method I used was:\n\n1. Build sage from source in directory /export/home/drkirkby/32/sage-4.4.3\n\n2. Make a binary distribution using your updated sage-bdist, which I've confirmed works on other systems and mine. \n\n3. Log in as a different user 'sageserv' on my system.\n\n4. Extract the binary .tar.gz file, which was extracted to\n/export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS\n\n5. Run Sage in the new directory, where upon I get the seg fault. But in the other directory, as a different user name, it works fine. \n\n\nAs far as I can see, I have the latest patches. These are the sizes of the patched files.\n\n```\n-rwxr-xr-x   1 drkirkby other       3680 Jun  9 23:54 sage-bdist\n-rwxr-xr-x   1 drkirkby other      10216 Jun 10 20:00 sage-env\n-rwxr-xr-x   1 drkirkby other       7133 Jun 12 15:40 sage-location\n```\n\nThe 'sage-location' script starts\n\n```/usr/bin/env python\n\nimport os, sys\n\nOLD_SAGE_ROOT = None\nSAGE_ROOT     = os.path.realpath(os.environ['SAGE_ROOT'])\n\nlocation_file = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-curent-location.txt')\nflags_file    = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-flags.txt')\n\n# The flags we care about recording in the local/lib/sage-flags.txt file\n# In SAGE_FAT_BINARY mode we only require that ['sse', 'sse2', '3d',\n#  'mmx', 'cmov'] be available, and in particular, don't require pni\n#  or ssse3.\n\ntry:\n    SAGE_FAT_BINARY = os.environ['SAGE_FAT_BINARY']\nexcept:\n    SAGE_FAT_BINARY = \"\"\n```\n\nAnything look wrong? \n\n\nDave",
    "created_at": "2010-06-12T16:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86085",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I thought I might have messed up, as I was tired, but as far as I can see, I do get a problem.

The method I used was:

1. Build sage from source in directory /export/home/drkirkby/32/sage-4.4.3

2. Make a binary distribution using your updated sage-bdist, which I've confirmed works on other systems and mine. 

3. Log in as a different user 'sageserv' on my system.

4. Extract the binary .tar.gz file, which was extracted to
/export/home/sageserv/sage-4.4.3-after-rewrite-sage-location-patch-Solaris10_03_2005-sun4u-SunOS

5. Run Sage in the new directory, where upon I get the seg fault. But in the other directory, as a different user name, it works fine. 


As far as I can see, I have the latest patches. These are the sizes of the patched files.

```
-rwxr-xr-x   1 drkirkby other       3680 Jun  9 23:54 sage-bdist
-rwxr-xr-x   1 drkirkby other      10216 Jun 10 20:00 sage-env
-rwxr-xr-x   1 drkirkby other       7133 Jun 12 15:40 sage-location
```

The 'sage-location' script starts

```/usr/bin/env python

import os, sys

OLD_SAGE_ROOT = None
SAGE_ROOT     = os.path.realpath(os.environ['SAGE_ROOT'])

location_file = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-curent-location.txt')
flags_file    = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-flags.txt')

# The flags we care about recording in the local/lib/sage-flags.txt file
# In SAGE_FAT_BINARY mode we only require that ['sse', 'sse2', '3d',
#  'mmx', 'cmov'] be available, and in particular, don't require pni
#  or ssse3.

try:
    SAGE_FAT_BINARY = os.environ['SAGE_FAT_BINARY']
except:
    SAGE_FAT_BINARY = ""
```

Anything look wrong? 


Dave



---

archive/issue_comments_086086.json:
```json
{
    "body": "new sage-location file (after patch) - do not apply; only for reviewing convenience",
    "created_at": "2010-06-12T17:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86086",
    "user": "https://github.com/jasongrout"
}
```

new sage-location file (after patch) - do not apply; only for reviewing convenience



---

archive/issue_comments_086087.json:
```json
{
    "body": "Attachment [sage-location](tarball://root/attachments/some-uuid/ticket9210/sage-location) by @jasongrout created at 2010-06-12 17:23:42\n\nI've attached the full (new) sage-location script, for reviewing convenience.",
    "created_at": "2010-06-12T17:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86087",
    "user": "https://github.com/jasongrout"
}
```

Attachment [sage-location](tarball://root/attachments/some-uuid/ticket9210/sage-location) by @jasongrout created at 2010-06-12 17:23:42

I've attached the full (new) sage-location script, for reviewing convenience.



---

archive/issue_comments_086088.json:
```json
{
    "body": "Replying to [comment:13 drkirkby]:\n\n> The 'sage-location' script starts\n> \n> \n> ```\n> #!/usr/bin/env python\n> \n> import os, sys\n> \n> OLD_SAGE_ROOT = None\n> SAGE_ROOT     = os.path.realpath(os.environ['SAGE_ROOT'])\n> \n> location_file = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-curent-location.txt')\n> flags_file    = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-flags.txt')\n> \n> # The flags we care about recording in the local/lib/sage-flags.txt file\n> # In SAGE_FAT_BINARY mode we only require that ['sse', 'sse2', '3d',\n> #  'mmx', 'cmov'] be available, and in particular, don't require pni\n> #  or ssse3.\n> \n> try:\n>     SAGE_FAT_BINARY = os.environ['SAGE_FAT_BINARY']\n> except:\n>     SAGE_FAT_BINARY = \"\"\n> ```\n> \n> Anything look wrong? \n\n\n\nYep.  Notice that the sage-location file is 'sage-curent-location' (misspelled \"current\").  That's the old patch.  I've attached the full new file for convenience, or you can pull the patch attached to this ticket currently.\n\nJason",
    "created_at": "2010-06-12T17:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86088",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:13 drkirkby]:

> The 'sage-location' script starts
> 
> 
> ```
> #!/usr/bin/env python
> 
> import os, sys
> 
> OLD_SAGE_ROOT = None
> SAGE_ROOT     = os.path.realpath(os.environ['SAGE_ROOT'])
> 
> location_file = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-curent-location.txt')
> flags_file    = os.path.join(SAGE_ROOT, 'local', 'lib', 'sage-flags.txt')
> 
> # The flags we care about recording in the local/lib/sage-flags.txt file
> # In SAGE_FAT_BINARY mode we only require that ['sse', 'sse2', '3d',
> #  'mmx', 'cmov'] be available, and in particular, don't require pni
> #  or ssse3.
> 
> try:
>     SAGE_FAT_BINARY = os.environ['SAGE_FAT_BINARY']
> except:
>     SAGE_FAT_BINARY = ""
> ```
> 
> Anything look wrong? 



Yep.  Notice that the sage-location file is 'sage-curent-location' (misspelled "current").  That's the old patch.  I've attached the full new file for convenience, or you can pull the patch attached to this ticket currently.

Jason



---

archive/issue_comments_086089.json:
```json
{
    "body": "I'm just building another binary distribution. \n\nI should be able to update this within the next hour or two.",
    "created_at": "2010-06-12T23:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86089",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm just building another binary distribution. 

I should be able to update this within the next hour or two.



---

archive/issue_comments_086090.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-13T00:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86090",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086091.json:
```json
{
    "body": "Hi Jason, \n\nI made another binary distribution, and moved it again. (I mistakenly used the number 4.4.4 in the name, rather than 4.4.3, but it makes no difference. I could call it zebra if I wanted! But this is based on the 4.4.3 in Sage, not on the 4.4.4.alpha0 source code). \n\nSage reports it has been moved, and an attempt to factorise a Mersenne prime behaves as expected. So there is no segmentation fault as there was before. \n\n```\n-bash-3.00$ cd sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS\n-bash-3.00$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThe Sage install tree may have moved\n(from /export/home/drkirkby/32/sage-4.4.3 to /export/home/sageserv/sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS)\nChanging various hardcoded paths\n(please wait at most a few minutes)...\nDo not interrupt this.\nDone resetting paths\nsage: factor(2^607 -1)\n531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127\nsage: \n```\n| Sage Version 4.4.3, Release Date: 2010-06-04                       |\n| Type notebook() for the GUI, and license() for information.        |\nBut when I look at the .pc files, the prefix is not updated. This does not look right to me. \n\n```\n-bash-3.00$ pwd\n/export/home/sageserv/sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS/local/lib/pkgconfig\n-bash-3.00$ cat  freetype2.pc\nprefix=/export/home/drkirkby/32/sage-4.4.3/local\nexec_prefix=${prefix}\nlibdir=${exec_prefix}/lib\nincludedir=${prefix}/include\n\nName: FreeType 2\nDescription: A free, high-quality, and portable font engine.\nVersion: 9.16.3\nRequires:\nLibs: -L${libdir} -lfreetype -lz \nCflags: -I${includedir}/freetype2 -I${includedir}SAGE_ROOT=/export/home/sageserv/sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS\n-bash-3.00$ \n```\n\nThe file sage-location is the one attached to this ticket\n\n```\n-bash-3.00$ digest -a md5 ./local/bin/sage-location\nd73f790e23a60751f6b1b58941515744\n```",
    "created_at": "2010-06-13T00:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86091",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi Jason, 

I made another binary distribution, and moved it again. (I mistakenly used the number 4.4.4 in the name, rather than 4.4.3, but it makes no difference. I could call it zebra if I wanted! But this is based on the 4.4.3 in Sage, not on the 4.4.4.alpha0 source code). 

Sage reports it has been moved, and an attempt to factorise a Mersenne prime behaves as expected. So there is no segmentation fault as there was before. 

```
-bash-3.00$ cd sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS
-bash-3.00$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The Sage install tree may have moved
(from /export/home/drkirkby/32/sage-4.4.3 to /export/home/sageserv/sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS)
Changing various hardcoded paths
(please wait at most a few minutes)...
Do not interrupt this.
Done resetting paths
sage: factor(2^607 -1)
531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
sage: 
```
| Sage Version 4.4.3, Release Date: 2010-06-04                       |
| Type notebook() for the GUI, and license() for information.        |
But when I look at the .pc files, the prefix is not updated. This does not look right to me. 

```
-bash-3.00$ pwd
/export/home/sageserv/sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS/local/lib/pkgconfig
-bash-3.00$ cat  freetype2.pc
prefix=/export/home/drkirkby/32/sage-4.4.3/local
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: FreeType 2
Description: A free, high-quality, and portable font engine.
Version: 9.16.3
Requires:
Libs: -L${libdir} -lfreetype -lz 
Cflags: -I${includedir}/freetype2 -I${includedir}SAGE_ROOT=/export/home/sageserv/sage-4.4.4-revised-sage-location-without-misspelling-sun4u-SunOS
-bash-3.00$ 
```

The file sage-location is the one attached to this ticket

```
-bash-3.00$ digest -a md5 ./local/bin/sage-location
d73f790e23a60751f6b1b58941515744
```



---

archive/issue_comments_086092.json:
```json
{
    "body": "You're right, that .pc file does not look right.  I'll try to take a look at this early next week.",
    "created_at": "2010-06-13T04:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86092",
    "user": "https://github.com/jasongrout"
}
```

You're right, that .pc file does not look right.  I'll try to take a look at this early next week.



---

archive/issue_comments_086093.json:
```json
{
    "body": "I think we need to be more careful about how we review this patch.  I know what files to delete to re-initialize things, but just to make sure, here are the new review instructions.  I'm following these myself, and I'll post them in a bit.",
    "created_at": "2010-06-15T02:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86093",
    "user": "https://github.com/jasongrout"
}
```

I think we need to be more careful about how we review this patch.  I know what files to delete to re-initialize things, but just to make sure, here are the new review instructions.  I'm following these myself, and I'll post them in a bit.



---

archive/issue_comments_086094.json:
```json
{
    "body": "Okay, here are I think better instructions for reviewing this patch:\n\n1. Download and extract the Sage 4.4.3 source tarball\n\n2. Download http://sage.math.washington.edu/home/jason/sage_scripts-4.4.3.spkg and put it in the spkg/standard directory, replacing the existing file of the same name.  This is just an spkg with the patch on this ticket applied, so that the .pc files are initialized correctly\n\n3. Build the source (i.e., type \"make\")\n\n4. Run Sage (this is very important, as hardcoded paths will depend on the build directory, and this step will initialize things to know what the build directory is)\n\n5. Then either move the sage directory, or create a bdist.  Now running Sage after moving directories or extracting and running sage from the bdist should correctly update the .pc files.  The freetype2.pc file, for example, should be something like:\n\n```\nSAGE_ROOT=/home/grout/sage-4.4.3-pkgconfig\nprefix=${SAGE_ROOT}/local\nexec_prefix=${prefix}\nlibdir=${exec_prefix}/lib\nincludedir=${prefix}/include\n\nName: FreeType 2\nDescription: A free, high-quality, and portable font engine.\nVersion: 9.16.3\nRequires:\nLibs: -L${libdir} -lfreetype -lz \nCflags: -I${includedir}/freetype2 -I${includedir}\n\n\n```\n\nwhere the SAGE_ROOT variable should update to the current sage root directory.",
    "created_at": "2010-06-15T04:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86094",
    "user": "https://github.com/jasongrout"
}
```

Okay, here are I think better instructions for reviewing this patch:

1. Download and extract the Sage 4.4.3 source tarball

2. Download http://sage.math.washington.edu/home/jason/sage_scripts-4.4.3.spkg and put it in the spkg/standard directory, replacing the existing file of the same name.  This is just an spkg with the patch on this ticket applied, so that the .pc files are initialized correctly

3. Build the source (i.e., type "make")

4. Run Sage (this is very important, as hardcoded paths will depend on the build directory, and this step will initialize things to know what the build directory is)

5. Then either move the sage directory, or create a bdist.  Now running Sage after moving directories or extracting and running sage from the bdist should correctly update the .pc files.  The freetype2.pc file, for example, should be something like:

```
SAGE_ROOT=/home/grout/sage-4.4.3-pkgconfig
prefix=${SAGE_ROOT}/local
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: FreeType 2
Description: A free, high-quality, and portable font engine.
Version: 9.16.3
Requires:
Libs: -L${libdir} -lfreetype -lz 
Cflags: -I${includedir}/freetype2 -I${includedir}


```

where the SAGE_ROOT variable should update to the current sage root directory.



---

archive/issue_comments_086095.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-15T04:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86095",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086096.json:
```json
{
    "body": "FYI, in April, some discussion happened on the pkg-config mailing list about making some automatic variables to support relocation: \n\nhttp://lists.freedesktop.org/archives/pkg-config/2010-April/000520.html",
    "created_at": "2010-06-15T04:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86096",
    "user": "https://github.com/jasongrout"
}
```

FYI, in April, some discussion happened on the pkg-config mailing list about making some automatic variables to support relocation: 

http://lists.freedesktop.org/archives/pkg-config/2010-April/000520.html



---

archive/issue_comments_086097.json:
```json
{
    "body": "(nothing came out of that discussion yet, but it might be nice to keep an eye on it in the future...)",
    "created_at": "2010-06-15T04:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86097",
    "user": "https://github.com/jasongrout"
}
```

(nothing came out of that discussion yet, but it might be nice to keep an eye on it in the future...)



---

archive/issue_comments_086098.json:
```json
{
    "body": "Since 4.4.4 has now been released, should I be able to apply trac-9210-rewrite-sage-location.patch and get this to work? I've built 4.4.4 but have not moved it yet. \n\n\nDave",
    "created_at": "2010-06-25T05:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86098",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Since 4.4.4 has now been released, should I be able to apply trac-9210-rewrite-sage-location.patch and get this to work? I've built 4.4.4 but have not moved it yet. 


Dave



---

archive/issue_comments_086099.json:
```json
{
    "body": "Not updating the .pc files in `SAGE_LOCAL/lib/pkgconfig` may also cause problems during an upgrade after moving Sage.  Please see [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/67feb1b840ff2710/5499fab47d031a21#5499fab47d031a21) for Karl-Dieter's report about a 4.5.2.rc1-4.5.3.alpha1 upgrade on PPC OS X 10.4\n\nAlso, for some packages that compile Python extension modules during the upgrade, it seems to help to update old paths in `SAGE_LOCAL/lib/python/config/Makefile`.\n\nI checked the .pc file and `Makefile` changes on sage.math with the equivalent of\n\n```sh\n$ tar xf /home/release/sage-4.5.2/sage-4.5.2.tar\n$ mv sage-4.5.2 sage-FOOO\n$ cd sage-FOOO\n$ make build\n$ cd ..\n$ cp -a sage-FOOO/ sage-yyyy\n$ cd sage-yyyy\n$ sed -i 's/FOOO/yyyy/g' local/lib/pkgconfig/*\n$ sed -i 's/FOOO/yyyy/g' local/lib/python/config/Makefile\n$ echo \"y\" | ./sage -upgrade http://sage.math.washington.edu/home/release/sage-4.5.3.alpha1/sage-4.5.3.alpha1.tar | tee -a upgrade.log\n$ grep FOOO upgrade.log\n$\n```\nIf I don't update the .pc files and/or the `Makefile`, I get many matches for `FOOO`.",
    "created_at": "2010-08-20T06:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86099",
    "user": "https://github.com/qed777"
}
```

Not updating the .pc files in `SAGE_LOCAL/lib/pkgconfig` may also cause problems during an upgrade after moving Sage.  Please see [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/67feb1b840ff2710/5499fab47d031a21#5499fab47d031a21) for Karl-Dieter's report about a 4.5.2.rc1-4.5.3.alpha1 upgrade on PPC OS X 10.4

Also, for some packages that compile Python extension modules during the upgrade, it seems to help to update old paths in `SAGE_LOCAL/lib/python/config/Makefile`.

I checked the .pc file and `Makefile` changes on sage.math with the equivalent of

```sh
$ tar xf /home/release/sage-4.5.2/sage-4.5.2.tar
$ mv sage-4.5.2 sage-FOOO
$ cd sage-FOOO
$ make build
$ cd ..
$ cp -a sage-FOOO/ sage-yyyy
$ cd sage-yyyy
$ sed -i 's/FOOO/yyyy/g' local/lib/pkgconfig/*
$ sed -i 's/FOOO/yyyy/g' local/lib/python/config/Makefile
$ echo "y" | ./sage -upgrade http://sage.math.washington.edu/home/release/sage-4.5.3.alpha1/sage-4.5.3.alpha1.tar | tee -a upgrade.log
$ grep FOOO upgrade.log
$
```
If I don't update the .pc files and/or the `Makefile`, I get many matches for `FOOO`.



---

archive/issue_comments_086100.json:
```json
{
    "body": "To review, this should be sufficient:\n\n1. Download and build Sage (important; it must be a fresh build from source).\n\n2. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):\n\nhttp://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch\n\n3. Delete the file SAGE_ROOT/local/lib/sage-current-location.txt, if it exists\n\n4. Now run Sage, then exit (this updates the sage-current-location and pkgconfig files appropriately).\n\n5. Move the sage directory and run Sage again.  The SAGE_ROOT/local/lib/sage-current-location.txt should be updated, and the pkgconfig files in SAGE_ROOT/local/lib/pkgconfig/ should also be updated to the new path (you can check the freetype2.pc file, for example, to see the new sage directory is listed there in the SAGE_ROOT variable).",
    "created_at": "2010-09-09T20:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86100",
    "user": "https://github.com/jasongrout"
}
```

To review, this should be sufficient:

1. Download and build Sage (important; it must be a fresh build from source).

2. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):

http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch

3. Delete the file SAGE_ROOT/local/lib/sage-current-location.txt, if it exists

4. Now run Sage, then exit (this updates the sage-current-location and pkgconfig files appropriately).

5. Move the sage directory and run Sage again.  The SAGE_ROOT/local/lib/sage-current-location.txt should be updated, and the pkgconfig files in SAGE_ROOT/local/lib/pkgconfig/ should also be updated to the new path (you can check the freetype2.pc file, for example, to see the new sage directory is listed there in the SAGE_ROOT variable).



---

archive/issue_comments_086101.json:
```json
{
    "body": "This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.\n\n1) Build Sage fresh in the directory \n\n`/export/home/drkirkby/9/sage-4.5.3.alpha2`\n\nSage had not been run. There was no file SAGE_ROOT/local/lib/sage-current-location.txt\n\n2) Created a tar file with all this in:\n\n```\n$ tar cvf test.tar sage-4.5.3.alpha2\n```\n\n3) Changed to the directory /tmp.\n\n```\n$ cd /tmp\n```\n\n4) Extracted the tar file in /tmp\n\n```\n$ tar xf $HOME/9/test.tar\n```\n\n5) Run Sage from /tmp.\n\nThat created \n\n```\n$SAGE_LOCAL/lib/sage-current-location.txt\n```\n\nwhich had `/tmp/sage-4.5.3.alpha2` \n\nas the contents  - I note there is no end of line. \n\n6) Changed to the directory where all the .pc files are\n\n```\n$ cd /tmp/sage-4.5.3.alpha2/local/lib/pkgconfig\n```\n\n7) Now run grep, and look for my user name \"drkirkby\" which was in the path before, but now I'm in /tmp, it should not be there. \n\n```\ndrkirkby@hawk:/tmp/sage-4.5.3.alpha2/local/lib/pkgconfig$ grep drkirkby *\nbdw-gc.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\nfreetype2.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\ngnutls-extra.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\ngnutls-extra.pc:Libs.private: -L${exec_prefix}/lib -lgnutls-extra -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lopencdk -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lsocket -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgpg-error -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lz -R/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib  -L${exec_prefix}/lib -lgnutls  -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lgpg-error -lnsl -lsocket \ngnutls.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\ngnutls.pc:Libs.private: -L${exec_prefix}/lib -lgnutls  -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lgpg-error -lnsl -lsocket  \ngsl.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\ngsl.pc:exec_prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\ngsl.pc:libdir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib\ngsl.pc:includedir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/include\ngsl.pc:Libs: -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgsl -lgslcblas -lm \ngsl.pc:Cflags: -I/export/home/drkirkby/9/sage-4.5.3.alpha2/local/includeSAGE_ROOT=/tmp/sage-4.5.3.alpha2\nlibpng.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\nlibpng12.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\nlibR.pc:rhome=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib/R\nlibR.pc:rincludedir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib/R/include\nopencdk.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\nopencdk.pc:Libs.private: -L${exec_prefix}/lib -lopencdk -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lgpg-error  -lz\npynac.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\nsqlite3.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\nzlib.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local\nzlib.pc:includedir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/include\n```\n\nAs you can see, there are tons of references to the old location. \n\nNow lets see how many of those files have \"tmp\" in them. \n\n```\ndrkirkby@hawk:/tmp/sage-4.5.3.alpha2/local/lib/pkgconfig$ grep drkirkby * | grep tmp\ngsl.pc:Cflags: -I/export/home/drkirkby/9/sage-4.5.3.alpha2/local/includeSAGE_ROOT=/tmp/sage-4.5.3.alpha2\ndrkirkby@hawk:/tmp/sage-4.5.3.alpha2/local/lib/pkgconfig$ \n```\n\nSo for me at least, those .pc files are not being updated. \n\nWould it be easier to do this with a *simple* `sed` script? I don't know precisely how to do this, but I could ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics?hl=en) I reckon this could be done in a very short unix shell script - it does not need loads of Python IMHO. \n\nDave",
    "created_at": "2010-09-09T22:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86101",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.

1) Build Sage fresh in the directory 

`/export/home/drkirkby/9/sage-4.5.3.alpha2`

Sage had not been run. There was no file SAGE_ROOT/local/lib/sage-current-location.txt

2) Created a tar file with all this in:

```
$ tar cvf test.tar sage-4.5.3.alpha2
```

3) Changed to the directory /tmp.

```
$ cd /tmp
```

4) Extracted the tar file in /tmp

```
$ tar xf $HOME/9/test.tar
```

5) Run Sage from /tmp.

That created 

```
$SAGE_LOCAL/lib/sage-current-location.txt
```

which had `/tmp/sage-4.5.3.alpha2` 

as the contents  - I note there is no end of line. 

6) Changed to the directory where all the .pc files are

```
$ cd /tmp/sage-4.5.3.alpha2/local/lib/pkgconfig
```

7) Now run grep, and look for my user name "drkirkby" which was in the path before, but now I'm in /tmp, it should not be there. 

```
drkirkby@hawk:/tmp/sage-4.5.3.alpha2/local/lib/pkgconfig$ grep drkirkby *
bdw-gc.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
freetype2.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
gnutls-extra.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
gnutls-extra.pc:Libs.private: -L${exec_prefix}/lib -lgnutls-extra -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lopencdk -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lsocket -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgpg-error -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lz -R/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib  -L${exec_prefix}/lib -lgnutls  -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lgpg-error -lnsl -lsocket 
gnutls.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
gnutls.pc:Libs.private: -L${exec_prefix}/lib -lgnutls  -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lgpg-error -lnsl -lsocket  
gsl.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
gsl.pc:exec_prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
gsl.pc:libdir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib
gsl.pc:includedir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/include
gsl.pc:Libs: -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgsl -lgslcblas -lm 
gsl.pc:Cflags: -I/export/home/drkirkby/9/sage-4.5.3.alpha2/local/includeSAGE_ROOT=/tmp/sage-4.5.3.alpha2
libpng.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
libpng12.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
libR.pc:rhome=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib/R
libR.pc:rincludedir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib/R/include
opencdk.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
opencdk.pc:Libs.private: -L${exec_prefix}/lib -lopencdk -L/export/home/drkirkby/9/sage-4.5.3.alpha2/local/lib -lgcrypt -lgpg-error  -lz
pynac.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
sqlite3.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
zlib.pc:prefix=/export/home/drkirkby/9/sage-4.5.3.alpha2/local
zlib.pc:includedir=/export/home/drkirkby/9/sage-4.5.3.alpha2/local/include
```

As you can see, there are tons of references to the old location. 

Now lets see how many of those files have "tmp" in them. 

```
drkirkby@hawk:/tmp/sage-4.5.3.alpha2/local/lib/pkgconfig$ grep drkirkby * | grep tmp
gsl.pc:Cflags: -I/export/home/drkirkby/9/sage-4.5.3.alpha2/local/includeSAGE_ROOT=/tmp/sage-4.5.3.alpha2
drkirkby@hawk:/tmp/sage-4.5.3.alpha2/local/lib/pkgconfig$ 
```

So for me at least, those .pc files are not being updated. 

Would it be easier to do this with a *simple* `sed` script? I don't know precisely how to do this, but I could ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics?hl=en) I reckon this could be done in a very short unix shell script - it does not need loads of Python IMHO. 

Dave



---

archive/issue_comments_086102.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-09T22:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86102",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086103.json:
```json
{
    "body": "I forgot to add  - I did apply the patch!!",
    "created_at": "2010-09-09T22:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86103",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I forgot to add  - I did apply the patch!!



---

archive/issue_comments_086104.json:
```json
{
    "body": "Data point - this does seem to work for me.  \n\n```\nCrismans-Computer:~ crisman$ cd Desktop/sage-4.6/local/lib/pkgconfig/\nCrismans-Computer:~/Desktop/sage-4.6/local/lib/pkgconfig crisman$ grep 4.5.3 *\n```\nThough it wasn't a *totally* fresh build... I did delete everything, though.  Why does this have to be totally fresh?  On this computer (one of the original report computers) it takes a long time to build, that's why I ask.",
    "created_at": "2010-09-09T22:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86104",
    "user": "https://github.com/kcrisman"
}
```

Data point - this does seem to work for me.  

```
Crismans-Computer:~ crisman$ cd Desktop/sage-4.6/local/lib/pkgconfig/
Crismans-Computer:~/Desktop/sage-4.6/local/lib/pkgconfig crisman$ grep 4.5.3 *
```
Though it wasn't a *totally* fresh build... I did delete everything, though.  Why does this have to be totally fresh?  On this computer (one of the original report computers) it takes a long time to build, that's why I ask.



---

archive/issue_comments_086105.json:
```json
{
    "body": "Replying to [comment:28 kcrisman]:\n> Data point - this does seem to work for me.  \n> \n> ```\n> Crismans-Computer:~ crisman$ cd Desktop/sage-4.6/local/lib/pkgconfig/\n> Crismans-Computer:~/Desktop/sage-4.6/local/lib/pkgconfig crisman$ grep 4.5.3 *\n> ```\n> Though it wasn't a *totally* fresh build... I did delete everything, though.  Why does this have to be totally fresh?  On this computer (one of the original report computers) it takes a long time to build, that's why I ask.\n\n\nThe totally fresh part is to make sure that the initialization the first time Sage is started up is done correctly.  In reality, as long as the current directory is the same as the build directory, and the sage-current-location.txt is deleted, it will probably also work.",
    "created_at": "2010-09-09T22:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86105",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:28 kcrisman]:
> Data point - this does seem to work for me.  
> 
> ```
> Crismans-Computer:~ crisman$ cd Desktop/sage-4.6/local/lib/pkgconfig/
> Crismans-Computer:~/Desktop/sage-4.6/local/lib/pkgconfig crisman$ grep 4.5.3 *
> ```
> Though it wasn't a *totally* fresh build... I did delete everything, though.  Why does this have to be totally fresh?  On this computer (one of the original report computers) it takes a long time to build, that's why I ask.


The totally fresh part is to make sure that the initialization the first time Sage is started up is done correctly.  In reality, as long as the current directory is the same as the build directory, and the sage-current-location.txt is deleted, it will probably also work.



---

archive/issue_comments_086106.json:
```json
{
    "body": "Replying to [comment:26 drkirkby]:\n> This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.\n\n\nYou didn't quite follow the instructions.\n\n> \n> 1) Build Sage fresh in the directory \n> \n> `/export/home/drkirkby/9/sage-4.5.3.alpha2`\n> \n> Sage had not been run. There was no file SAGE_ROOT/local/lib/sage-current-location.txt\n\n\nHere you need to apply the patch and run Sage (step 4).  Sage must be run, with the patch applied, from the original build directory, to properly initialize the pkconfig files and the sage-current-location.txt file.\n\nAfter applying the patch, making sure there is no sage-current-location.txt file, then running Sage once, only *then* should you move the directory.\n\n> \n> Would it be easier to do this with a *simple* `sed` script? I don't know precisely how to do this, but I could ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics?hl=en) I reckon this could be done in a very short unix shell script - it does not need loads of Python IMHO. \n\n\nMore than just the pkgconfig files are being updated, so it's not just that simple.  However, a sufficiently talented (or un-busy) shell programmer could do the job, probably.",
    "created_at": "2010-09-09T22:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86106",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:26 drkirkby]:
> This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.


You didn't quite follow the instructions.

> 
> 1) Build Sage fresh in the directory 
> 
> `/export/home/drkirkby/9/sage-4.5.3.alpha2`
> 
> Sage had not been run. There was no file SAGE_ROOT/local/lib/sage-current-location.txt


Here you need to apply the patch and run Sage (step 4).  Sage must be run, with the patch applied, from the original build directory, to properly initialize the pkconfig files and the sage-current-location.txt file.

After applying the patch, making sure there is no sage-current-location.txt file, then running Sage once, only *then* should you move the directory.

> 
> Would it be easier to do this with a *simple* `sed` script? I don't know precisely how to do this, but I could ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics?hl=en) I reckon this could be done in a very short unix shell script - it does not need loads of Python IMHO. 


More than just the pkgconfig files are being updated, so it's not just that simple.  However, a sufficiently talented (or un-busy) shell programmer could do the job, probably.



---

archive/issue_comments_086107.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-09T22:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86107",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086108.json:
```json
{
    "body": "Replying to [comment:30 jason]:\n> Replying to [comment:26 drkirkby]:\n> > This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.\n\n> \n> You didn't quite follow the instructions.\n\n\nI think it was a case of not exactly explaining what I did. I believe I did run Sage in the original location. When I extracted the tar file for a second time, it showed the file \n\n`$SAGE_LOCAL/lib/sage-current-location.txt`\n\nBut prior to running Sage that file did not exist. Then when I moved Sage, the contents of \n\n$SAGE_LOCAL/lib/sage-current-location.txt\n\nchanged, but the contents of the .pc files did not substantially change. \n\nI will revisit this - but I'm still not convinced it is working myself. It might be a platform specific problem. \n\nDave",
    "created_at": "2010-09-10T09:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86108",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:30 jason]:
> Replying to [comment:26 drkirkby]:
> > This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.

> 
> You didn't quite follow the instructions.


I think it was a case of not exactly explaining what I did. I believe I did run Sage in the original location. When I extracted the tar file for a second time, it showed the file 

`$SAGE_LOCAL/lib/sage-current-location.txt`

But prior to running Sage that file did not exist. Then when I moved Sage, the contents of 

$SAGE_LOCAL/lib/sage-current-location.txt

changed, but the contents of the .pc files did not substantially change. 

I will revisit this - but I'm still not convinced it is working myself. It might be a platform specific problem. 

Dave



---

archive/issue_comments_086109.json:
```json
{
    "body": "Replying to [comment:31 drkirkby]:\n> Replying to [comment:30 jason]:\n> > Replying to [comment:26 drkirkby]:\n> > > This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.\n\n> > \n> > You didn't quite follow the instructions.\n\n> \n> I think it was a case of not exactly explaining what I did. I believe I did run Sage in the original location. When I extracted the tar file for a second time, it showed the file \n> \n> `$SAGE_LOCAL/lib/sage-current-location.txt`\n> \n> But prior to running Sage that file did not exist. Then when I moved Sage, the contents of \n> \n> $SAGE_LOCAL/lib/sage-current-location.txt\n> \n> changed, but the contents of the .pc files did not substantially change. \n> \n> I will revisit this - but I'm still not convinced it is working myself. It might be a platform specific problem. \n\n\n\nThe fact that in your before tarball, the pkgconfig files did not start with SAGE_ROOT leads me to believe that the sage-current-location.txt file was created *before* the patch was applied, and was never deleted and sage run before moving the directory.  With the new patch applied, when that file is created, the pkgconfig files should be modified to include a SAGE_ROOT line at the very top.\n\nI tried to use the python OS-agnostic functions everywhere, so on the surface, I doubt it's an OS-specific problem.\n\nSo, if you have time, please try again, and make sure that after the patch is applied, the sage-current-location.txt file is deleted which for convenience, are repeated below:\n\n\n\nTo review, this should be sufficient:\n\n#. Download and build Sage (important; it must be a fresh build from source).\n\n#. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):\n\n http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch\n\n#. Delete the file SAGE_ROOT/local/lib/sage-current-location.txt, if it exists\n\n#. Now run Sage, then exit (this updates the sage-current-location and pkgconfig files appropriately).  Check to make sure that sage-current-location.txt is now created, and that each pkgconfig file starts with a line \"SAGE_ROOT=\" (followed by the build directory)\n\n#. Move the sage directory and run Sage again. The SAGE_ROOT/local/lib/sage-current-location.txt should be updated, and the pkgconfig files in SAGE_ROOT/local/lib/pkgconfig/ should also be updated to the new path (you can check the freetype2.pc file, for example, to see the new sage directory is listed there in the SAGE_ROOT variable).\n\nThanks!",
    "created_at": "2010-10-15T00:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86109",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:31 drkirkby]:
> Replying to [comment:30 jason]:
> > Replying to [comment:26 drkirkby]:
> > > This is simply not working for me. The system is a Sun Ultra 27 running OpenSolaris on an Intel Xeon processor. This is what I did.

> > 
> > You didn't quite follow the instructions.

> 
> I think it was a case of not exactly explaining what I did. I believe I did run Sage in the original location. When I extracted the tar file for a second time, it showed the file 
> 
> `$SAGE_LOCAL/lib/sage-current-location.txt`
> 
> But prior to running Sage that file did not exist. Then when I moved Sage, the contents of 
> 
> $SAGE_LOCAL/lib/sage-current-location.txt
> 
> changed, but the contents of the .pc files did not substantially change. 
> 
> I will revisit this - but I'm still not convinced it is working myself. It might be a platform specific problem. 



The fact that in your before tarball, the pkgconfig files did not start with SAGE_ROOT leads me to believe that the sage-current-location.txt file was created *before* the patch was applied, and was never deleted and sage run before moving the directory.  With the new patch applied, when that file is created, the pkgconfig files should be modified to include a SAGE_ROOT line at the very top.

I tried to use the python OS-agnostic functions everywhere, so on the surface, I doubt it's an OS-specific problem.

So, if you have time, please try again, and make sure that after the patch is applied, the sage-current-location.txt file is deleted which for convenience, are repeated below:



To review, this should be sufficient:

#. Download and build Sage (important; it must be a fresh build from source).

#. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):

 http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch

#. Delete the file SAGE_ROOT/local/lib/sage-current-location.txt, if it exists

#. Now run Sage, then exit (this updates the sage-current-location and pkgconfig files appropriately).  Check to make sure that sage-current-location.txt is now created, and that each pkgconfig file starts with a line "SAGE_ROOT=" (followed by the build directory)

#. Move the sage directory and run Sage again. The SAGE_ROOT/local/lib/sage-current-location.txt should be updated, and the pkgconfig files in SAGE_ROOT/local/lib/pkgconfig/ should also be updated to the new path (you can check the freetype2.pc file, for example, to see the new sage directory is listed there in the SAGE_ROOT variable).

Thanks!



---

archive/issue_comments_086110.json:
```json
{
    "body": "Apparently I don't remember the right wiki syntax.\u00a0 Here are the 5 steps again:\n\n1. Download and build Sage (important; it must be a fresh build from source).\n2. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):[http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch](http://trac.sagemath.org/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch)\n3. Delete the file SAGE_ROOT/local/lib/sage-current-location.txt, if it exists\n4. Now run Sage, then exit (this updates the sage-current-location and  pkgconfig files appropriately).  Check to make sure that  sage-current-location.txt is now created, and that each pkgconfig file  starts with a line \"SAGE_ROOT=\" (followed by the build directory)\n5. Move the sage directory and run Sage again. The  SAGE_ROOT/local/lib/sage-current-location.txt should be updated, and the  pkgconfig files in SAGE_ROOT/local/lib/pkgconfig/ should also be  updated to the new path (you can check the freetype2.pc file, for  example, to see the new sage directory is listed there in the SAGE_ROOT  variable).",
    "created_at": "2010-10-15T00:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86110",
    "user": "https://github.com/jasongrout"
}
```

Apparently I don't remember the right wiki syntax.  Here are the 5 steps again:

1. Download and build Sage (important; it must be a fresh build from source).
2. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):[http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch](http://trac.sagemath.org/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch)
3. Delete the file SAGE_ROOT/local/lib/sage-current-location.txt, if it exists
4. Now run Sage, then exit (this updates the sage-current-location and  pkgconfig files appropriately).  Check to make sure that  sage-current-location.txt is now created, and that each pkgconfig file  starts with a line "SAGE_ROOT=" (followed by the build directory)
5. Move the sage directory and run Sage again. The  SAGE_ROOT/local/lib/sage-current-location.txt should be updated, and the  pkgconfig files in SAGE_ROOT/local/lib/pkgconfig/ should also be  updated to the new path (you can check the freetype2.pc file, for  example, to see the new sage directory is listed there in the SAGE_ROOT  variable).



---

archive/issue_comments_086111.json:
```json
{
    "body": ">  1. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):[http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch](http://trac.sagemath.org/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch)\n\n\nThe link is wrong but the text is right; http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch",
    "created_at": "2010-10-15T02:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86111",
    "user": "https://github.com/kcrisman"
}
```

>  1. Apply the patch at the ticket to the scripts repository (in SAGE_ROOT/local/bin):[http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch](http://trac.sagemath.org/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch)


The link is wrong but the text is right; http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9210/trac-9210-rewrite-sage-location.patch



---

archive/issue_comments_086112.json:
```json
{
    "body": "After doing this on a NON fresh build, just to fix something dumb, I get\n\n```\nnew-host-2:pkgconfig karl-dietercrisman$ grep 4.6 *\nbdw-gc.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\nfreetype2.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\ngnutls-extra.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\ngnutls.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\ngsl.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\nlibR.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\nlibR.pc:rhome=/Users/.../sage-4.6.alpha1/local/lib/R\nlibR.pc:rincludedir=/Users/.../sage-4.6.alpha1/local/lib/R/include\nlibpng.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\nlibpng12.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\nopencdk.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\npynac.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\npynac.pc:prefix=/Users/.../sage-4.6.alpha2/local\nsqlite3.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\nzlib.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4\nnew-host-2:pkgconfig karl-dietercrisman$ grep 4.5 *\nbdw-gc.pc:prefix=/Users/.../sage-4.5.1/local\nfreetype2.pc:prefix=/Users/.../sage-4.5.1/local\ngnutls-extra.pc:prefix=/Users/.../sage-4.5.1/local\ngnutls-extra.pc:Libs.private: -L${exec_prefix}/lib -lgnutls-extra -L/Users/.../sage-4.5.1/local/lib -lopencdk -L/Users/.../sage-4.5.1/local/lib -lgcrypt -L/Users/.../sage-4.5.1/local/lib -lgpg-error -L/Users/.../sage-4.5.1/local/lib -lz -R/Users/.../sage-4.5.1/local/lib  -L${exec_prefix}/lib -lgnutls  -L/Users/.../sage-4.5.1/local/lib -lgcrypt -lgpg-error \ngnutls.pc:prefix=/Users/.../sage-4.5.1/local\ngnutls.pc:Libs.private: -L${exec_prefix}/lib -lgnutls  -L/Users/.../sage-4.5.1/local/lib -lgcrypt -lgpg-error  \ngsl.pc:prefix=/Users/.../sage-4.5.2/local\ngsl.pc:exec_prefix=/Users/.../sage-4.5.2/local\ngsl.pc:libdir=/Users/.../sage-4.5.2/local/lib\ngsl.pc:includedir=/Users/.../sage-4.5.2/local/include\ngsl.pc:Libs: -L/Users/.../sage-4.5.2/local/lib -lgsl -lgslcblas -lm \ngsl.pc:Cflags: -I/Users/.../sage-4.5.2/local/include\nlibpng.pc:prefix=/Users/.../sage-4.5.1/local\nlibpng12.pc:prefix=/Users/.../sage-4.5.1/local\nopencdk.pc:prefix=/Users/.../sage-4.5.1/local\nopencdk.pc:Libs.private: -L${exec_prefix}/lib -lopencdk -L/Users/.../sage-4.5.1/local/lib -lgcrypt -lgpg-error  -lz\nsqlite3.pc:prefix=/Users/.../sage-4.5.1/local\nzlib.pc:prefix=/Users/.../sage-4.5.1/local\nzlib.pc:includedir=/Users/.../sage-4.5.1/local/include\n```\nSo although it relists the `SAGE_ROOT` variable correctly, all those prefixes and includes and whatever else still are bad news.   I don't know how to use `sed` like Mitesh suggested on sage-release, but I think I can change the freetype one by hand.",
    "created_at": "2010-10-15T02:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86112",
    "user": "https://github.com/kcrisman"
}
```

After doing this on a NON fresh build, just to fix something dumb, I get

```
new-host-2:pkgconfig karl-dietercrisman$ grep 4.6 *
bdw-gc.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
freetype2.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
gnutls-extra.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
gnutls.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
gsl.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
libR.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
libR.pc:rhome=/Users/.../sage-4.6.alpha1/local/lib/R
libR.pc:rincludedir=/Users/.../sage-4.6.alpha1/local/lib/R/include
libpng.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
libpng12.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
opencdk.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
pynac.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
pynac.pc:prefix=/Users/.../sage-4.6.alpha2/local
sqlite3.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
zlib.pc:SAGE_ROOT=/Users/.../sage-4.6.alpha4
new-host-2:pkgconfig karl-dietercrisman$ grep 4.5 *
bdw-gc.pc:prefix=/Users/.../sage-4.5.1/local
freetype2.pc:prefix=/Users/.../sage-4.5.1/local
gnutls-extra.pc:prefix=/Users/.../sage-4.5.1/local
gnutls-extra.pc:Libs.private: -L${exec_prefix}/lib -lgnutls-extra -L/Users/.../sage-4.5.1/local/lib -lopencdk -L/Users/.../sage-4.5.1/local/lib -lgcrypt -L/Users/.../sage-4.5.1/local/lib -lgpg-error -L/Users/.../sage-4.5.1/local/lib -lz -R/Users/.../sage-4.5.1/local/lib  -L${exec_prefix}/lib -lgnutls  -L/Users/.../sage-4.5.1/local/lib -lgcrypt -lgpg-error 
gnutls.pc:prefix=/Users/.../sage-4.5.1/local
gnutls.pc:Libs.private: -L${exec_prefix}/lib -lgnutls  -L/Users/.../sage-4.5.1/local/lib -lgcrypt -lgpg-error  
gsl.pc:prefix=/Users/.../sage-4.5.2/local
gsl.pc:exec_prefix=/Users/.../sage-4.5.2/local
gsl.pc:libdir=/Users/.../sage-4.5.2/local/lib
gsl.pc:includedir=/Users/.../sage-4.5.2/local/include
gsl.pc:Libs: -L/Users/.../sage-4.5.2/local/lib -lgsl -lgslcblas -lm 
gsl.pc:Cflags: -I/Users/.../sage-4.5.2/local/include
libpng.pc:prefix=/Users/.../sage-4.5.1/local
libpng12.pc:prefix=/Users/.../sage-4.5.1/local
opencdk.pc:prefix=/Users/.../sage-4.5.1/local
opencdk.pc:Libs.private: -L${exec_prefix}/lib -lopencdk -L/Users/.../sage-4.5.1/local/lib -lgcrypt -lgpg-error  -lz
sqlite3.pc:prefix=/Users/.../sage-4.5.1/local
zlib.pc:prefix=/Users/.../sage-4.5.1/local
zlib.pc:includedir=/Users/.../sage-4.5.1/local/include
```
So although it relists the `SAGE_ROOT` variable correctly, all those prefixes and includes and whatever else still are bad news.   I don't know how to use `sed` like Mitesh suggested on sage-release, but I think I can change the freetype one by hand.



---

archive/issue_comments_086113.json:
```json
{
    "body": "Replying to [comment:35 kcrisman]:\n> After doing this on a NON fresh build, just to fix something dumb, I get\n> \n\n\nThe result is expected.  The SAGE_ROOT directory is no longer the same as the build directory (as evidenced by the plethora of other build directories in the pkgconfig files).  This patch only works correctly if things are initialized in the original build directory.",
    "created_at": "2010-10-15T02:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86113",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:35 kcrisman]:
> After doing this on a NON fresh build, just to fix something dumb, I get
> 


The result is expected.  The SAGE_ROOT directory is no longer the same as the build directory (as evidenced by the plethora of other build directories in the pkgconfig files).  This patch only works correctly if things are initialized in the original build directory.



---

archive/issue_comments_086114.json:
```json
{
    "body": "I had a long followup, but your reply explained things.  So why can't we also update those things?   The new sage-location script `update_pkgconfig_files` doesn't seem to touch anything but that `SAGE_ROOT` guy, but it looks like there isn't any reason it couldn't, in theory, do those prefix statements too and just make them `${SAGE_ROOT}/local` or whatever is appropriate.\n\n(I'm going to try that change 'by hand' on freetype, by the way.)",
    "created_at": "2010-10-15T02:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86114",
    "user": "https://github.com/kcrisman"
}
```

I had a long followup, but your reply explained things.  So why can't we also update those things?   The new sage-location script `update_pkgconfig_files` doesn't seem to touch anything but that `SAGE_ROOT` guy, but it looks like there isn't any reason it couldn't, in theory, do those prefix statements too and just make them `${SAGE_ROOT}/local` or whatever is appropriate.

(I'm going to try that change 'by hand' on freetype, by the way.)



---

archive/issue_comments_086115.json:
```json
{
    "body": "Replying to [comment:37 kcrisman]:\n> I had a long followup, but your reply explained things.  So why can't we also update those things?   The new sage-location script `update_pkgconfig_files` doesn't seem to touch anything but that `SAGE_ROOT` guy, but it looks like there isn't any reason it couldn't, in theory, do those prefix statements too and just make them `${SAGE_ROOT}/local` or whatever is appropriate.\n> \n> (I'm going to try that change 'by hand' on freetype, by the way.)\n\n\nI suppose the general problem is that we only know what the previous `SAGE_ROOT` was (given in the sage-location.txt file).  We don't know what any other path in those pkgconfig files are, including the SAGE_ROOT from the time before the last move.\n\nI suppose we could be more invasive and always change the prefix path as well.  But there are other paths too.  What paths do you change?  In your example, you had at least 3-4 paths from old build directories, and lots of them are in things other than prefix statements.  Which ones are old `SAGE_ROOT`s, and which ones are still valid locations that shouldn't be changed?  For the ones that are old `SAGE_ROOT`s, which are the `SAGE_ROOT` parts and which are the parts that shouldn't be changed?\n\nThe strategy now is to replace all SAGE_ROOT paths with the SAGE_ROOT variable on the first startup, and then only change that in subsequent runs if needed.  That seems *much* safer.\n\nRight now, the strategy breaks down for pkgconfig files created after the initial build.  \n\nAnother ticket should be created to update pkgconfig files that don't have `SAGE_ROOT` already defined, which takes care of spkgs installed later.",
    "created_at": "2010-10-15T03:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86115",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:37 kcrisman]:
> I had a long followup, but your reply explained things.  So why can't we also update those things?   The new sage-location script `update_pkgconfig_files` doesn't seem to touch anything but that `SAGE_ROOT` guy, but it looks like there isn't any reason it couldn't, in theory, do those prefix statements too and just make them `${SAGE_ROOT}/local` or whatever is appropriate.
> 
> (I'm going to try that change 'by hand' on freetype, by the way.)


I suppose the general problem is that we only know what the previous `SAGE_ROOT` was (given in the sage-location.txt file).  We don't know what any other path in those pkgconfig files are, including the SAGE_ROOT from the time before the last move.

I suppose we could be more invasive and always change the prefix path as well.  But there are other paths too.  What paths do you change?  In your example, you had at least 3-4 paths from old build directories, and lots of them are in things other than prefix statements.  Which ones are old `SAGE_ROOT`s, and which ones are still valid locations that shouldn't be changed?  For the ones that are old `SAGE_ROOT`s, which are the `SAGE_ROOT` parts and which are the parts that shouldn't be changed?

The strategy now is to replace all SAGE_ROOT paths with the SAGE_ROOT variable on the first startup, and then only change that in subsequent runs if needed.  That seems *much* safer.

Right now, the strategy breaks down for pkgconfig files created after the initial build.  

Another ticket should be created to update pkgconfig files that don't have `SAGE_ROOT` already defined, which takes care of spkgs installed later.



---

archive/issue_comments_086116.json:
```json
{
    "body": "> > (I'm going to try that change 'by hand' on freetype, by the way.)\n\nWhich worked! \n\nOn another machine, doing that wasn't enough to get out of this issue... there was still a reference to the wrong thing in libR.dylib, which is a binary file, and which I have no idea how to change.  But that's not this ticket.  As far as I have time to test this, it did what it said, so positive review from me.  I don't have time to do the complete build from scratch, but it definitely changed what it claimed to in the right way from a non-scratch situation - and it WAS changed.\n\n> Another ticket should be created to update pkgconfig files that don't have `SAGE_ROOT` already defined, which takes care of spkgs installed later.\n\nThis seems reasonable, and hopefully with time won't be much of an issue.  Sorry I can't give final positive review.",
    "created_at": "2010-10-15T13:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86116",
    "user": "https://github.com/kcrisman"
}
```

> > (I'm going to try that change 'by hand' on freetype, by the way.)

Which worked! 

On another machine, doing that wasn't enough to get out of this issue... there was still a reference to the wrong thing in libR.dylib, which is a binary file, and which I have no idea how to change.  But that's not this ticket.  As far as I have time to test this, it did what it said, so positive review from me.  I don't have time to do the complete build from scratch, but it definitely changed what it claimed to in the right way from a non-scratch situation - and it WAS changed.

> Another ticket should be created to update pkgconfig files that don't have `SAGE_ROOT` already defined, which takes care of spkgs installed later.

This seems reasonable, and hopefully with time won't be much of an issue.  Sorry I can't give final positive review.



---

archive/issue_comments_086117.json:
```json
{
    "body": "Replying to [comment:39 kcrisman]:\n\n> > Another ticket should be created to update pkgconfig files that don't have `SAGE_ROOT` already defined, which takes care of spkgs installed later.\n\n> This seems reasonable, and hopefully with time won't be much of an issue.  Sorry I can't give final positive review.\n\nSo I think that means we need at least one more reviewer.  Dave, do you have time to look at this again?",
    "created_at": "2010-10-15T15:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86117",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:39 kcrisman]:

> > Another ticket should be created to update pkgconfig files that don't have `SAGE_ROOT` already defined, which takes care of spkgs installed later.

> This seems reasonable, and hopefully with time won't be much of an issue.  Sorry I can't give final positive review.

So I think that means we need at least one more reviewer.  Dave, do you have time to look at this again?



---

archive/issue_comments_086118.json:
```json
{
    "body": "Replying to [comment:40 jason]:\n\n> So I think that means we need at least one more reviewer.  Dave, do you have time to look at this again?\n\n\nI won't have much time to play with this until Wednesday, but I'm just doing a fresh build. This time I'm using the 'script' command so it will have an **exact** record of what I did - even my typos are recorded. If there's a problem I'll make that file available, if there's not, I'll give it a positive review. \n\nBTW, someone above said they did not know how to use 'sed'. There are plenty of references on the web, but this file I always find useful, as it normally has something there which is sufficiently similar to what I want to achieve, that I can modify it to do what I want. \n\nhttp://sed.sourceforge.net/sed1line.txt\n\ndave",
    "created_at": "2010-10-16T05:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86118",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:40 jason]:

> So I think that means we need at least one more reviewer.  Dave, do you have time to look at this again?


I won't have much time to play with this until Wednesday, but I'm just doing a fresh build. This time I'm using the 'script' command so it will have an **exact** record of what I did - even my typos are recorded. If there's a problem I'll make that file available, if there's not, I'll give it a positive review. 

BTW, someone above said they did not know how to use 'sed'. There are plenty of references on the web, but this file I always find useful, as it normally has something there which is sufficiently similar to what I want to achieve, that I can modify it to do what I want. 

http://sed.sourceforge.net/sed1line.txt

dave



---

archive/issue_comments_086119.json:
```json
{
    "body": "OK, Sage is built. Let's try my luck for the Nth time!",
    "created_at": "2010-10-16T05:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86119",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

OK, Sage is built. Let's try my luck for the Nth time!



---

archive/issue_comments_086120.json:
```json
{
    "body": "I think that has worked. I am just going to run the doctests to make sure. \n\nDave",
    "created_at": "2010-10-16T06:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86120",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I think that has worked. I am just going to run the doctests to make sure. 

Dave



---

archive/issue_comments_086121.json:
```json
{
    "body": "Em, this is odd. I used 'mv' to move the Sage directory from:\n\n```\n/export/home/drkirkby/9210/sage-4.6.alpha3/local\n```\n\nto:\n\n```\n/tmp/9210/sage-4.6.alpha3/local\n```\n\nI got some warnings about unable to save ACLs. Now when I run the doctests, several are failing. One at least is due to the fact 'Maxima' can't run. When I look at the script $SAGE_ROOT/local/bin/maxima, I see that still have the old location:\n\n\n```\ndrkirkby@hawk:/tmp/9210/sage-4.6.alpha3$ pwd\n/tmp/9210/sage-4.6.alpha3\ndrkirkby@hawk:/tmp/9210/sage-4.6.alpha3$ grep drkirkby local/bin/maxima\n  prefix=`unixize \"/export/home/drkirkby/9210/sage-4.6.alpha3/local\"`\n  top_srcdir=`unixize \"/export/home/drkirkby\"`\n```\n\nSo perhaps the .pc files are not the only things that need changing. I realise that's outside of the scope of this ticket, and it may be due to the warnings about unable to save ALCs, so I build Sage again and use 'tar' to move it. \n\nDave",
    "created_at": "2010-10-16T06:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86121",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Em, this is odd. I used 'mv' to move the Sage directory from:

```
/export/home/drkirkby/9210/sage-4.6.alpha3/local
```

to:

```
/tmp/9210/sage-4.6.alpha3/local
```

I got some warnings about unable to save ACLs. Now when I run the doctests, several are failing. One at least is due to the fact 'Maxima' can't run. When I look at the script $SAGE_ROOT/local/bin/maxima, I see that still have the old location:


```
drkirkby@hawk:/tmp/9210/sage-4.6.alpha3$ pwd
/tmp/9210/sage-4.6.alpha3
drkirkby@hawk:/tmp/9210/sage-4.6.alpha3$ grep drkirkby local/bin/maxima
  prefix=`unixize "/export/home/drkirkby/9210/sage-4.6.alpha3/local"`
  top_srcdir=`unixize "/export/home/drkirkby"`
```

So perhaps the .pc files are not the only things that need changing. I realise that's outside of the scope of this ticket, and it may be due to the warnings about unable to save ALCs, so I build Sage again and use 'tar' to move it. 

Dave



---

archive/issue_comments_086122.json:
```json
{
    "body": "Replying to [comment:44 drkirkby]:\n\n> So perhaps the .pc files are not the only things that need changing. I realise that's outside of the scope of this ticket, and it may be due to the warnings about unable to save ALCs, so I build Sage again and use 'tar' to move it. \n> \n\n\nMost definitely there are other issues besides the pkgconfig files.  I'm not confident in moving my installation at all anymore.  This ticket just takes care of one aspect of the problem that prevented compiling things in a new location.",
    "created_at": "2010-10-16T15:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86122",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:44 drkirkby]:

> So perhaps the .pc files are not the only things that need changing. I realise that's outside of the scope of this ticket, and it may be due to the warnings about unable to save ALCs, so I build Sage again and use 'tar' to move it. 
> 


Most definitely there are other issues besides the pkgconfig files.  I'm not confident in moving my installation at all anymore.  This ticket just takes care of one aspect of the problem that prevented compiling things in a new location.



---

archive/issue_comments_086123.json:
```json
{
    "body": "I've taken another look at this. It looks like I was mistaken when I thought the .pc file were not being updated properly, since they do now need to be. \n\nPrior to moving the distribution, there were two doctest failures - #10041 and 10042. \n\n```\nsage -t -long \"devel/sage/sage/rings/polynomial/polynomial_element.pyx\" \nsage -t -long \"devel/sage/sage/tensor/differential_forms.py\" \n```\n\nAfter moving the location, there are 5 doctest failures. \n\n```\nThe following tests failed:\n\n\tsage -t  -long -force_lib devel/sage/doc/en/tutorial/tour_advanced.rst # 2 doctests failed\n\tsage -t  -long -force_lib devel/sage/doc/fr/tutorial/tour_advanced.rst # 2 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/tensor/differential_forms.py # 1 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/rings/polynomial/groebner_fan.py # 76 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1583.2 seconds\n```\n\nSo clearly this is not a complete fix for moving Sage, but it's a step in the right direction. \n\nSo I'm giving this positive review. \n\nI'm sorry I have dragged this ticket out so long. I was of the belief it was not working correctly, so that is why I declined to give it positive review before, but now I'm convinced it is ok. \n\nLike Jason, I'm not happy to move Sage. It makes me wonder how good the binaries are that we distribute. Does anyone doctest the binaries after they are created before they are made public? \n\nDave",
    "created_at": "2010-10-17T10:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86123",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've taken another look at this. It looks like I was mistaken when I thought the .pc file were not being updated properly, since they do now need to be. 

Prior to moving the distribution, there were two doctest failures - #10041 and 10042. 

```
sage -t -long "devel/sage/sage/rings/polynomial/polynomial_element.pyx" 
sage -t -long "devel/sage/sage/tensor/differential_forms.py" 
```

After moving the location, there are 5 doctest failures. 

```
The following tests failed:

	sage -t  -long -force_lib devel/sage/doc/en/tutorial/tour_advanced.rst # 2 doctests failed
	sage -t  -long -force_lib devel/sage/doc/fr/tutorial/tour_advanced.rst # 2 doctests failed
	sage -t  -long -force_lib devel/sage/sage/tensor/differential_forms.py # 1 doctests failed
	sage -t  -long -force_lib devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
	sage -t  -long -force_lib devel/sage/sage/rings/polynomial/groebner_fan.py # 76 doctests failed
	sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1583.2 seconds
```

So clearly this is not a complete fix for moving Sage, but it's a step in the right direction. 

So I'm giving this positive review. 

I'm sorry I have dragged this ticket out so long. I was of the belief it was not working correctly, so that is why I declined to give it positive review before, but now I'm convinced it is ok. 

Like Jason, I'm not happy to move Sage. It makes me wonder how good the binaries are that we distribute. Does anyone doctest the binaries after they are created before they are made public? 

Dave



---

archive/issue_comments_086124.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-17T10:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86124",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086125.json:
```json
{
    "body": "Replying to [comment:46 drkirkby]:\n> {{{\n> The following tests failed:\n> \n> \tsage -t  -long -force_lib devel/sage/doc/en/tutorial/tour_advanced.rst # 2 doctests failed\n> \tsage -t  -long -force_lib devel/sage/doc/fr/tutorial/tour_advanced.rst # 2 doctests failed\n> \tsage -t  -long -force_lib devel/sage/sage/tensor/differential_forms.py # 1 doctests failed\n> \tsage -t  -long -force_lib devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed\n> \tsage -t  -long -force_lib devel/sage/sage/rings/polynomial/groebner_fan.py # 76 doctests failed\n> \tsage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed\n> \n> ---\n> Total time for all tests: 1583.2 seconds\n> }}}\n\n\nIf you still have it, could you attach or give a link to the test log?",
    "created_at": "2010-10-17T11:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86125",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:46 drkirkby]:
> {{{
> The following tests failed:
> 
> 	sage -t  -long -force_lib devel/sage/doc/en/tutorial/tour_advanced.rst # 2 doctests failed
> 	sage -t  -long -force_lib devel/sage/doc/fr/tutorial/tour_advanced.rst # 2 doctests failed
> 	sage -t  -long -force_lib devel/sage/sage/tensor/differential_forms.py # 1 doctests failed
> 	sage -t  -long -force_lib devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
> 	sage -t  -long -force_lib devel/sage/sage/rings/polynomial/groebner_fan.py # 76 doctests failed
> 	sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed
> 
> ---
> Total time for all tests: 1583.2 seconds
> }}}


If you still have it, could you attach or give a link to the test log?



---

archive/issue_comments_086126.json:
```json
{
    "body": "Replying to [comment:47 mpatel]:\n\n> If you still have it, could you attach or give a link to the test log?\n\n\nSure, it is here. The tests were run on 'hawk', my OpenSolaris machine.\n\nhttp://boxen.math.washington.edu/home/kirkby/logs/ptestlong-sage-4.6.alpha3-after-applying-9210-and-moving-to-another-location.log",
    "created_at": "2010-10-17T12:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86126",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:47 mpatel]:

> If you still have it, could you attach or give a link to the test log?


Sure, it is here. The tests were run on 'hawk', my OpenSolaris machine.

http://boxen.math.washington.edu/home/kirkby/logs/ptestlong-sage-4.6.alpha3-after-applying-9210-and-moving-to-another-location.log



---

archive/issue_comments_086127.json:
```json
{
    "body": "Replying to [comment:48 drkirkby]:\n> Replying to [comment:47 mpatel]:\n> > If you still have it, could you attach or give a link to the test log?\n\n\n> Sure, it is here. The tests were run on 'hawk', my OpenSolaris machine.\n\n \n> http://boxen.math.washington.edu/home/kirkby/logs/ptestlong-sage-4.6.alpha3-after-applying-9210-and-moving-to-another-location.log\n\n\nThanks.  At least, the new errors all have one \"cause\":\n\n```python\nRuntimeError: ld.so.1: gfan: fatal: relocation error: file /export/home/test/sage-4.6.alpha3/local/bin/gfan: symbol _ZNSt15_List_node_base7_M_hookEPS_: referenced symbol not found\n```\nOf course, we can make this a separate ticket, but why would this `fatal: relocation error` happen?",
    "created_at": "2010-10-17T22:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86127",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:48 drkirkby]:
> Replying to [comment:47 mpatel]:
> > If you still have it, could you attach or give a link to the test log?


> Sure, it is here. The tests were run on 'hawk', my OpenSolaris machine.

 
> http://boxen.math.washington.edu/home/kirkby/logs/ptestlong-sage-4.6.alpha3-after-applying-9210-and-moving-to-another-location.log


Thanks.  At least, the new errors all have one "cause":

```python
RuntimeError: ld.so.1: gfan: fatal: relocation error: file /export/home/test/sage-4.6.alpha3/local/bin/gfan: symbol _ZNSt15_List_node_base7_M_hookEPS_: referenced symbol not found
```
Of course, we can make this a separate ticket, but why would this `fatal: relocation error` happen?



---

archive/issue_comments_086128.json:
```json
{
    "body": "I wonder if this should be a blocker...",
    "created_at": "2010-10-20T12:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86128",
    "user": "https://github.com/nexttime"
}
```

I wonder if this should be a blocker...



---

archive/issue_comments_086129.json:
```json
{
    "body": "Replying to [comment:50 leif]:\n> I wonder if this should be a blocker...\n\n\nNo.  At most critical.  Sage certainly has been released for a long time without this fix.",
    "created_at": "2010-10-20T13:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86129",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:50 leif]:
> I wonder if this should be a blocker...


No.  At most critical.  Sage certainly has been released for a long time without this fix.



---

archive/issue_comments_086130.json:
```json
{
    "body": "I found the reason gfan has unresolved variables when moved - it is to do with gcc and the linker run time search path. \n\nIn a Sage shell, before the move:\n\n```\n(sage subshell) hawk:sage-4.6.alpha3 drkirkby$ ldd local/bin/gfan\n\tlibgmp.so.3 =>\t /export/home/drkirkby/sage-4.6.alpha3/local/lib//libgmp.so.3\n\tlibstdc++.so.6 =>\t /usr/local/gcc-4.5.0/lib/libstdc++.so.6\n\tlibm.so.2 =>\t /lib/libm.so.2\n\tlibgcc_s.so.1 =>\t /usr/local/gcc-4.5.0/lib/libgcc_s.so.1\n\tlibc.so.1 =>\t /lib/libc.so.1\nSAGE_ROOT=/export/home/drkirkby/sage-4.6.alpha3\n```\n\nAfter creating another account, and moving Sage, I must have not set LD_LIBRARY_PATH identically, so ldd shows:\n\n```\n(sage subshell) hawk:bin test$ ldd gfan\n\tlibgmp.so.3 =>\t /export/home/test/sage-4.6.alpha3/local/lib//libgmp.so.3\n\tlibstdc++.so.6 =>\t /usr/lib/libstdc++.so.6\n\tlibm.so.2 =>\t /lib/libm.so.2\n\tlibgcc_s.so.1 =>\t /usr/lib/libgcc_s.so.1\n\tlibc.so.1 =>\t /lib/libc.so.1\nSAGE_ROOT=/export/home/test/sage-4.6.alpha3\n```\n\ni.e. instead of gfan finding the C++ libary it was linked against (e..g. /usr/local/gcc-4.5.0/lib/libstdc++.so.6) if finds an older library in `/usr/lib/libstdc++.so.6`. That is from gcc 3.4.3 - i.e. very old. \n\nThis is something we have to be very weary of on Solaris. We should make available recent run-time libraries, otherwise the user will probably have trouble. I know there have been reports of this on sage-support, and other sage-developers have hit it on t2.math. If we compile Sage with a recent gcc, and the person using a binary only had old gcc libraries, and/or new libraries are not in their linker search path, Sage will not run well. \n\nThere was one other thing I found odd. **Before** moving the code, though after Sage had been run, I tried this in a Sage shell. \n\n```\n(sage subshell) hawk:sage-4.6.alpha3 drkirkby$ local/bin/gfan\n1+2\nPARSER ERROR: Expected: \"field\"    Found: \"1\"\nAssertion failed: 0, file parser.cpp, line 509\nAbort (core dumped)\nSAGE_ROOT=/export/home/drkirkby/sage-4.6.alpha3\n```\n\nI've got no idea how gfan is supposed to be used, but trying 1+2 is enough to make it dump core, which is a bug in my opinion. \n\nI tried it on sage.math too. Whilst it does not dump core, it is not very elegant:\n\n```\n(sage subshell) sage:bin kirkby$ gfan\n1+2\nPARSER ERROR: Expected: \"field\"    Found: \"1\"\ngfan: parser.cpp:509: Field CharacterBasedParser::parseField(): Assertion `0' failed.\nAborted\nSAGE_ROOT=/usr/local/sage\n```\n\nAnd on bsd.math (OS X)\n\n```\n(sage subshell) bsd:bin kirkby$ gfan\n1+1\nPARSER ERROR: Expected: \"field\"    Found: \"1\"\nAssertion failed: (0), function parseField, file parser.cpp, line 509.\nAbort trap\nSAGE_ROOT=/Users/kirkby/sage-4.6.alpha0\n```\n\nSo as soon as the parser sees something it does not reconise, it either aborts or dumps core. Not very elegant. \n\nDave",
    "created_at": "2010-10-20T13:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86130",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I found the reason gfan has unresolved variables when moved - it is to do with gcc and the linker run time search path. 

In a Sage shell, before the move:

```
(sage subshell) hawk:sage-4.6.alpha3 drkirkby$ ldd local/bin/gfan
	libgmp.so.3 =>	 /export/home/drkirkby/sage-4.6.alpha3/local/lib//libgmp.so.3
	libstdc++.so.6 =>	 /usr/local/gcc-4.5.0/lib/libstdc++.so.6
	libm.so.2 =>	 /lib/libm.so.2
	libgcc_s.so.1 =>	 /usr/local/gcc-4.5.0/lib/libgcc_s.so.1
	libc.so.1 =>	 /lib/libc.so.1
SAGE_ROOT=/export/home/drkirkby/sage-4.6.alpha3
```

After creating another account, and moving Sage, I must have not set LD_LIBRARY_PATH identically, so ldd shows:

```
(sage subshell) hawk:bin test$ ldd gfan
	libgmp.so.3 =>	 /export/home/test/sage-4.6.alpha3/local/lib//libgmp.so.3
	libstdc++.so.6 =>	 /usr/lib/libstdc++.so.6
	libm.so.2 =>	 /lib/libm.so.2
	libgcc_s.so.1 =>	 /usr/lib/libgcc_s.so.1
	libc.so.1 =>	 /lib/libc.so.1
SAGE_ROOT=/export/home/test/sage-4.6.alpha3
```

i.e. instead of gfan finding the C++ libary it was linked against (e..g. /usr/local/gcc-4.5.0/lib/libstdc++.so.6) if finds an older library in `/usr/lib/libstdc++.so.6`. That is from gcc 3.4.3 - i.e. very old. 

This is something we have to be very weary of on Solaris. We should make available recent run-time libraries, otherwise the user will probably have trouble. I know there have been reports of this on sage-support, and other sage-developers have hit it on t2.math. If we compile Sage with a recent gcc, and the person using a binary only had old gcc libraries, and/or new libraries are not in their linker search path, Sage will not run well. 

There was one other thing I found odd. **Before** moving the code, though after Sage had been run, I tried this in a Sage shell. 

```
(sage subshell) hawk:sage-4.6.alpha3 drkirkby$ local/bin/gfan
1+2
PARSER ERROR: Expected: "field"    Found: "1"
Assertion failed: 0, file parser.cpp, line 509
Abort (core dumped)
SAGE_ROOT=/export/home/drkirkby/sage-4.6.alpha3
```

I've got no idea how gfan is supposed to be used, but trying 1+2 is enough to make it dump core, which is a bug in my opinion. 

I tried it on sage.math too. Whilst it does not dump core, it is not very elegant:

```
(sage subshell) sage:bin kirkby$ gfan
1+2
PARSER ERROR: Expected: "field"    Found: "1"
gfan: parser.cpp:509: Field CharacterBasedParser::parseField(): Assertion `0' failed.
Aborted
SAGE_ROOT=/usr/local/sage
```

And on bsd.math (OS X)

```
(sage subshell) bsd:bin kirkby$ gfan
1+1
PARSER ERROR: Expected: "field"    Found: "1"
Assertion failed: (0), function parseField, file parser.cpp, line 509.
Abort trap
SAGE_ROOT=/Users/kirkby/sage-4.6.alpha0
```

So as soon as the parser sees something it does not reconise, it either aborts or dumps core. Not very elegant. 

Dave



---

archive/issue_comments_086131.json:
```json
{
    "body": "Dave,\n\nJust to clarify, are you saying something more needs to be done on this ticket, or are you commenting on another issue (with valuable information that should go on another ticket to fix the gfan issue)?",
    "created_at": "2010-10-20T13:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86131",
    "user": "https://github.com/jasongrout"
}
```

Dave,

Just to clarify, are you saying something more needs to be done on this ticket, or are you commenting on another issue (with valuable information that should go on another ticket to fix the gfan issue)?



---

archive/issue_comments_086132.json:
```json
{
    "body": "No, I'm happy with this ticket. \n\nThe gfan core dump should go on another ticket. \n\nI'm not sure how best to handle the situation with libraries that are older than the version Sage was built with. \n\nNeither issue is related to the ticket as such. \n\nDave",
    "created_at": "2010-10-20T13:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86132",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

No, I'm happy with this ticket. 

The gfan core dump should go on another ticket. 

I'm not sure how best to handle the situation with libraries that are older than the version Sage was built with. 

Neither issue is related to the ticket as such. 

Dave



---

archive/issue_comments_086133.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-10-21T08:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86133",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_086134.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-21T10:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86134",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022690.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-21T10:07:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9210#event-22690"
}
```



---

archive/issue_comments_086135.json:
```json
{
    "body": "Replying to [comment:24 mpatel]:\n> Not updating the .pc files in `SAGE_LOCAL/lib/pkgconfig` may also cause problems during an upgrade after moving Sage.  Please see [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/67feb1b840ff2710/5499fab47d031a21#5499fab47d031a21) for Karl-Dieter's report about a 4.5.2.rc1-4.5.3.alpha1 upgrade on PPC OS X 10.4\n> \n> Also, for some packages that compile Python extension modules during the upgrade, it seems to help to update old paths in `SAGE_LOCAL/lib/python/config/Makefile`. [...]\n\n\nCf. #9896. Python's Makefile and  `pyconfig.h` define lots of variables that contain hard-coded paths. These all go into `distutils.sysconfig.get_config_vars()` (a dictionary), but only some are used, and not all obsolete paths are actually harmful.\n\nMy patch to `devel/sage/setup.py` at #9896 e.g. just fixes invalid / obsolete library search directories coded into distutils' dynamic linker **command**(!) (on Darwin).\n\nAn alternative is to patch distutils itself.",
    "created_at": "2010-10-21T14:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86135",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:24 mpatel]:
> Not updating the .pc files in `SAGE_LOCAL/lib/pkgconfig` may also cause problems during an upgrade after moving Sage.  Please see [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/67feb1b840ff2710/5499fab47d031a21#5499fab47d031a21) for Karl-Dieter's report about a 4.5.2.rc1-4.5.3.alpha1 upgrade on PPC OS X 10.4
> 
> Also, for some packages that compile Python extension modules during the upgrade, it seems to help to update old paths in `SAGE_LOCAL/lib/python/config/Makefile`. [...]


Cf. #9896. Python's Makefile and  `pyconfig.h` define lots of variables that contain hard-coded paths. These all go into `distutils.sysconfig.get_config_vars()` (a dictionary), but only some are used, and not all obsolete paths are actually harmful.

My patch to `devel/sage/setup.py` at #9896 e.g. just fixes invalid / obsolete library search directories coded into distutils' dynamic linker **command**(!) (on Darwin).

An alternative is to patch distutils itself.



---

archive/issue_comments_086136.json:
```json
{
    "body": "See #10162 for a follow-up.",
    "created_at": "2010-10-23T21:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86136",
    "user": "https://github.com/jhpalmieri"
}
```

See #10162 for a follow-up.



---

archive/issue_comments_086137.json:
```json
{
    "body": "Replying to [comment:59 jhpalmieri]:\n> See #10162 for a follow-up.\n\n\nAnd also (more important) #10202.",
    "created_at": "2010-11-02T17:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9210#issuecomment-86137",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:59 jhpalmieri]:
> See #10162 for a follow-up.


And also (more important) #10202.
