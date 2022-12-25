# Issue 6563: [with spkg, positive review] Singular fails to install header files, since it fails to find install-sh

archive/issues_006563.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @malb\n\nKeywords: solaris\n\nsingular-3-1-0-2-20090620 appeared to install on a Solaris machine, with the file $SAGE_HOME/spkg/installed/singular-3-1-0-2-20090620 existing. \n\nHowever, it was later realised that some of the singular header files were not copied to $SAGE_HOME/local/include/singular. Closer inspection of the install.log showed: \n\n```\n\nmake[1]: Entering directory \n`/export/home/drkirkby/sage/sage-4.1/spkg/build/singular-3-1-0-2-20090620/src/kernel'\n./mkinstalldirs /export/home/drkirkby/sage/sage-4.1/local/include/singular\nfor file in *.h; do ../.././install-sh -c $file \n/export/home/drkirkby/sage/sage-4.1/local/include/singular; done\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n/bin/sh: ../.././install-sh: not found\n```\n\n\n\nChanging to the directory \n`/export/home/drkirkby/sage/sage-4.1/spkg/build/singular-3-1-0-2-20090620/src/kernel' \nand doing an 'ls' of ../.././ I see that it got me to the root directory \nof the singular installation - by that I mean where spkh-install, \nSPKG.txt etc exist.\n\nCopying install-sh to there solved the problem.\n\nWillem Jan Palenstijn said on sage-devel:\n\n''If I understand things correctly, this is what happens:\nwhen src/Singular/config.status outputs ../kernel/Makefile, it\ninterprets the two slashes in that path as the output file being two\nsubdirectories down from Makefile, and so adjusts (the correct)\n'./install.sh' (i.e., actually src/Singular/install-sh) to (the broken)''\n\n'../.././install.sh' .\n\n''The reason this doesn't show up on my system (and presumably other\nsystems) is that /usr/bin/install (with an absolute path) is found and used\ninstead of ./install.sh.''\n\n[actually, the missing file is install-sh, not install.sh]\n\nWhatever may or may not be the real reason for this, the simplest solution is to simply copy install-sh to the top level directory. I know it's not normal to do it this way, but it might be the quickest. I've created a patch based on doing just that. \n http://sage.math.washington.edu/home/kirkby/Solaris-fixes/singular-3-1-0-2-20090620.p0/\n\nThe actual .spkg file is:\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/singular-3-1-0-2-20090620.p0/singular-3-1-0-2-20090620.p0.spkg\n\nIt should be noted there are about 10-15 identical copies of the file in the source distribution! Perhaps someone before had trouble find the file. \n\nSo far this has only been seen on Solaris I believe. but is clearly not specifically a Solaris bug. \n\nDave \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6563\n\n",
    "closed_at": "2009-07-24T00:06:17Z",
    "created_at": "2009-07-19T23:03:29Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with spkg, positive review] Singular fails to install header files, since it fails to find install-sh",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6563",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @malb

Keywords: solaris

singular-3-1-0-2-20090620 appeared to install on a Solaris machine, with the file $SAGE_HOME/spkg/installed/singular-3-1-0-2-20090620 existing. 

However, it was later realised that some of the singular header files were not copied to $SAGE_HOME/local/include/singular. Closer inspection of the install.log showed: 

```

make[1]: Entering directory 
`/export/home/drkirkby/sage/sage-4.1/spkg/build/singular-3-1-0-2-20090620/src/kernel'
./mkinstalldirs /export/home/drkirkby/sage/sage-4.1/local/include/singular
for file in *.h; do ../.././install-sh -c $file 
/export/home/drkirkby/sage/sage-4.1/local/include/singular; done
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
```



Changing to the directory 
`/export/home/drkirkby/sage/sage-4.1/spkg/build/singular-3-1-0-2-20090620/src/kernel' 
and doing an 'ls' of ../.././ I see that it got me to the root directory 
of the singular installation - by that I mean where spkh-install, 
SPKG.txt etc exist.

Copying install-sh to there solved the problem.

Willem Jan Palenstijn said on sage-devel:

''If I understand things correctly, this is what happens:
when src/Singular/config.status outputs ../kernel/Makefile, it
interprets the two slashes in that path as the output file being two
subdirectories down from Makefile, and so adjusts (the correct)
'./install.sh' (i.e., actually src/Singular/install-sh) to (the broken)''

'../.././install.sh' .

''The reason this doesn't show up on my system (and presumably other
systems) is that /usr/bin/install (with an absolute path) is found and used
instead of ./install.sh.''

[actually, the missing file is install-sh, not install.sh]

Whatever may or may not be the real reason for this, the simplest solution is to simply copy install-sh to the top level directory. I know it's not normal to do it this way, but it might be the quickest. I've created a patch based on doing just that. 
 http://sage.math.washington.edu/home/kirkby/Solaris-fixes/singular-3-1-0-2-20090620.p0/

The actual .spkg file is:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/singular-3-1-0-2-20090620.p0/singular-3-1-0-2-20090620.p0.spkg

It should be noted there are about 10-15 identical copies of the file in the source distribution! Perhaps someone before had trouble find the file. 

So far this has only been seen on Solaris I believe. but is clearly not specifically a Solaris bug. 

Dave 


Issue created by migration from https://trac.sagemath.org/ticket/6563





---

archive/issue_comments_053426.json:
```json
{
    "body": "I've checked in all changes in your name. The updated SPKG is up at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/singular-3-1-0-2-20090620.p0.spkg",
    "created_at": "2009-07-23T07:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6563#issuecomment-53426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I've checked in all changes in your name. The updated SPKG is up at

http://sage.math.washington.edu/home/mvngu/patch/singular-3-1-0-2-20090620.p0.spkg



---

archive/issue_comments_053427.json:
```json
{
    "body": "The SPKG at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/singular-3-1-0-2-20090620.p0.spkg\n\nbuilds OK on the machine t2 running Solaris. (It also compiles on Linux.)",
    "created_at": "2009-07-24T00:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6563#issuecomment-53427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The SPKG at

http://sage.math.washington.edu/home/mvngu/patch/singular-3-1-0-2-20090620.p0.spkg

builds OK on the machine t2 running Solaris. (It also compiles on Linux.)



---

archive/issue_events_015480.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-24T00:06:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6563",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6563#event-15480"
}
```



---

archive/issue_comments_053428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T00:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6563#issuecomment-53428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053429.json:
```json
{
    "body": "Did this ever get reported upstream?  Just wondering whether the fix is still needed today (making a new Singular spkg at #12137).\n\nThis quote from the description really made me laugh:\n> It should be noted there are about 10-15 identical copies of the file in the source distribution! Perhaps someone before had trouble find the file.\n\n\nSo many copies but still not enough...",
    "created_at": "2011-12-10T00:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6563#issuecomment-53429",
    "user": "https://github.com/jdemeyer"
}
```

Did this ever get reported upstream?  Just wondering whether the fix is still needed today (making a new Singular spkg at #12137).

This quote from the description really made me laugh:
> It should be noted there are about 10-15 identical copies of the file in the source distribution! Perhaps someone before had trouble find the file.


So many copies but still not enough...
