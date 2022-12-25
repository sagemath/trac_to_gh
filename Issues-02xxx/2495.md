# Issue 2495: [with spkg, two positive reviews] Updated experimental Mayavi2 spkg (mayavi_2.1.1) linux only

archive/issues_002495.json:
```json
{
    "body": "Assignee: mabshoff\n\nUpdated to the latest release of Mayavi2.\n\nNow uses vtk-5.0.4 with GL2EPS enabled, so picures can be saved as eps, ps and pdf files!\n\nSee:\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/\n\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/mayavi_2.1.1-20080307.spkg\n\nwith dependencies:\n\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/vtk-5.0.4.spkg \n\nnew version of setuptools (will be in sage-2.10.4 standard): http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/setuptools-0.6c8.spkg\n\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/wxPython-2.8.7.1.spkg (already in experimental)  \n\nIssue created by migration from https://trac.sagemath.org/ticket/2495\n\n",
    "closed_at": "2008-03-31T11:27:25Z",
    "created_at": "2008-03-12T15:14:59Z",
    "labels": [
        "component: packages: experimental",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with spkg, two positive reviews] Updated experimental Mayavi2 spkg (mayavi_2.1.1) linux only",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2495",
    "user": "https://github.com/jaapspies"
}
```
Assignee: mabshoff

Updated to the latest release of Mayavi2.

Now uses vtk-5.0.4 with GL2EPS enabled, so picures can be saved as eps, ps and pdf files!

See:
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/mayavi_2.1.1-20080307.spkg

with dependencies:

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/vtk-5.0.4.spkg 

new version of setuptools (will be in sage-2.10.4 standard): http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/setuptools-0.6c8.spkg

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/wxPython-2.8.7.1.spkg (already in experimental)  

Issue created by migration from https://trac.sagemath.org/ticket/2495





---

archive/issue_comments_016869.json:
```json
{
    "body": "I used these packages to upgrade from earlier versions of Jaap's packages; the installations went perfectly, and my code (which uses wxPython, vtk, and tvtk (from mayavi)) worked fine after the upgrade.\n\nDebian testing 32-bit x86.",
    "created_at": "2008-03-13T04:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16869",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I used these packages to upgrade from earlier versions of Jaap's packages; the installations went perfectly, and my code (which uses wxPython, vtk, and tvtk (from mayavi)) worked fine after the upgrade.

Debian testing 32-bit x86.



---

archive/issue_comments_016870.json:
```json
{
    "body": "There is a small typo in\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/README.txt\nThe line\nype ./sage -i mayavi_2.1.1.20080307\nshould read\nype ./sage -i mayavi_2.1.1-20080307",
    "created_at": "2008-03-13T11:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16870",
    "user": "https://github.com/wdjoyner"
}
```

There is a small typo in
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/README.txt
The line
ype ./sage -i mayavi_2.1.1.20080307
should read
ype ./sage -i mayavi_2.1.1-20080307



---

archive/issue_comments_016871.json:
```json
{
    "body": "I tried this and got the following install error:\n\n```\n...\nInstalling mayavi2 script to /home/wdj/wdj/sagefiles/sage-2.10.3/local/bin\n\nInstalled /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.mayavi-2.1.1.dev_r18151-py2.5.egg\nProcessing dependencies for enthought.mayavi==2.1.1.dev-r18151\nSearching for enthought.util>=2.0.3.dev,<3.0a\nBest match: enthought.util 2.0.3\nProcessing enthought.util-2.0.3-py2.5.egg\ncreating /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.util-2.0.3-py2.5.egg\nExtracting enthought.util-2.0.3-py2.5.egg to /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages\nAdding enthought.util 2.0.3 to easy-install.pth file\n\nInstalled /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.util-2.0.3-py2.5.egg\nSearching for enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a\n\nLink to http://code.enthought.com/enstaller/eggs/source ***BLOCKED*** by --allow-hosts\n\n\nLink to http://pypi.python.org/simple/enthought.tvtk/ ***BLOCKED*** by --allow-hosts\n\nCouldn't find index page for 'enthought.tvtk' (maybe misspelled?)\nScanning index of all packages (this may take a while)\n\nLink to http://pypi.python.org/simple/ ***BLOCKED*** by --allow-hosts\n\nNo local packages or download links found for enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a\nerror: Could not find suitable distribution for Requirement.parse('enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a')\n\nreal    34m27.361s\nuser    24m49.633s\nsys     3m27.337s\nsage: An error occurred while installing mayavi_2.1.1-20080307\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /home/wdj/wdj/sagefiles/sage-2.10.3/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/home/wdj/wdj/sagefiles/sage-2.10.3/spkg/build/mayavi_2.1.1-20080307 and type 'make'.\nInstead type \"/home/wdj/wdj/sagefiles/sage-2.10.3/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/home/wdj/wdj/sagefiles/sage-2.10.3/spkg/build/mayavi_2.1.1-20080307\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n```",
    "created_at": "2008-03-13T13:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16871",
    "user": "https://github.com/wdjoyner"
}
```

I tried this and got the following install error:

```
...
Installing mayavi2 script to /home/wdj/wdj/sagefiles/sage-2.10.3/local/bin

Installed /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.mayavi-2.1.1.dev_r18151-py2.5.egg
Processing dependencies for enthought.mayavi==2.1.1.dev-r18151
Searching for enthought.util>=2.0.3.dev,<3.0a
Best match: enthought.util 2.0.3
Processing enthought.util-2.0.3-py2.5.egg
creating /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.util-2.0.3-py2.5.egg
Extracting enthought.util-2.0.3-py2.5.egg to /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages
Adding enthought.util 2.0.3 to easy-install.pth file

Installed /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.util-2.0.3-py2.5.egg
Searching for enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a

Link to http://code.enthought.com/enstaller/eggs/source ***BLOCKED*** by --allow-hosts


Link to http://pypi.python.org/simple/enthought.tvtk/ ***BLOCKED*** by --allow-hosts

Couldn't find index page for 'enthought.tvtk' (maybe misspelled?)
Scanning index of all packages (this may take a while)

Link to http://pypi.python.org/simple/ ***BLOCKED*** by --allow-hosts

No local packages or download links found for enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a
error: Could not find suitable distribution for Requirement.parse('enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a')

real    34m27.361s
user    24m49.633s
sys     3m27.337s
sage: An error occurred while installing mayavi_2.1.1-20080307
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wdj/wdj/sagefiles/sage-2.10.3/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/wdj/wdj/sagefiles/sage-2.10.3/spkg/build/mayavi_2.1.1-20080307 and type 'make'.
Instead type "/home/wdj/wdj/sagefiles/sage-2.10.3/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wdj/wdj/sagefiles/sage-2.10.3/spkg/build/mayavi_2.1.1-20080307
(When you are done debugging, you can type "exit" to leave the
subshell.)
```



---

archive/issue_comments_016872.json:
```json
{
    "body": "mayvi2 should be built locally, so no need to get external sources!\n\nDependencies for now:\n\ninstall vtk-5.0.4.spkg (see http://trac.sagemath.org/sage_trac/ticket/2493 )\n\nBe sure you have installed wxPython-2.8.7.1.spkg (in experimental already!)\n and setuptools-0.6c8.spkg\n\nOr put everything temporarily in spkg/standard, etcetera see the README.txt",
    "created_at": "2008-03-14T18:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16872",
    "user": "https://github.com/jaapspies"
}
```

mayvi2 should be built locally, so no need to get external sources!

Dependencies for now:

install vtk-5.0.4.spkg (see http://trac.sagemath.org/sage_trac/ticket/2493 )

Be sure you have installed wxPython-2.8.7.1.spkg (in experimental already!)
 and setuptools-0.6c8.spkg

Or put everything temporarily in spkg/standard, etcetera see the README.txt



---

archive/issue_comments_016873.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> I tried this and got the following install error:\n> \n\n>\n\nCould you try once again following the instructions?\n\nAnd by doing so also comment on trac ticket #2493",
    "created_at": "2008-03-16T19:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16873",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:4 wdj]:
> I tried this and got the following install error:
> 

>

Could you try once again following the instructions?

And by doing so also comment on trac ticket #2493



---

archive/issue_comments_016874.json:
```json
{
    "body": "A couple remarks:\n\n* the build directory should be called src\n* please remove the `.svn` directories, that cuts the size of the spkg in half.\n* check in the file to the repo. I did the initial checkin, so in the future you need to check in only the changes\n\nThe updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/mayavi_2.1.1-20080307.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T05:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16874",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A couple remarks:

* the build directory should be called src
* please remove the `.svn` directories, that cuts the size of the spkg in half.
* check in the file to the repo. I did the initial checkin, so in the future you need to check in only the changes

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/mayavi_2.1.1-20080307.p0.spkg

Cheers,

Michael



---

archive/issue_comments_016875.json:
```json
{
    "body": "Changing component from graphics to experimental package.",
    "created_at": "2008-03-22T05:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from graphics to experimental package.



---

archive/issue_comments_016876.json:
```json
{
    "body": "One thing I forgot: I very much dislike the fact that it forced automated downloads of things like wxPython in case it isn't installed. It is clear from the readme that those ought to be already installed, but we need to find a more elegant way how to solve the \"dependency of non-standard spkg\" problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T05:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One thing I forgot: I very much dislike the fact that it forced automated downloads of things like wxPython in case it isn't installed. It is clear from the readme that those ought to be already installed, but we need to find a more elegant way how to solve the "dependency of non-standard spkg" problem.

Cheers,

Michael



---

archive/issue_comments_016877.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-03-22T05:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_016878.json:
```json
{
    "body": "Merged in the experimental spkg repo.",
    "created_at": "2008-03-22T05:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in the experimental spkg repo.



---

archive/issue_comments_016879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T05:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005873.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-22T05:19:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2495#event-5873"
}
```



---

archive/issue_comments_016880.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> One thing I forgot: I very much dislike the fact that it forced automated downloads of things like wxPython in case it isn't installed. It is clear from the readme that those ought to be already installed, but we need to find a more elegant way how to solve the \"dependency of non-standard spkg\" problem.\n> \n\n\nBefore we have this elegant solution the spkg-install should be consistent with reality!\nSo reflect that mayavi2 depends on vtk-5.0.4.p0 as you name the package.\n\nThe same holds for the vtk spkg, because it depends on cmake.\n\nJaap\n\n\n\n```/bin/sh\n\nsage -i wxPython-2.8.7.1\nsage -i vtk-5.0.4.p0\n\n\ncd src\n\npython egg_builder.py -r -v\n\neasy_install -f dist -H dist enthought.mayavi*",
    "created_at": "2008-03-22T17:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16880",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:8 mabshoff]:
> One thing I forgot: I very much dislike the fact that it forced automated downloads of things like wxPython in case it isn't installed. It is clear from the readme that those ought to be already installed, but we need to find a more elegant way how to solve the "dependency of non-standard spkg" problem.
> 


Before we have this elegant solution the spkg-install should be consistent with reality!
So reflect that mayavi2 depends on vtk-5.0.4.p0 as you name the package.

The same holds for the vtk spkg, because it depends on cmake.

Jaap



```/bin/sh

sage -i wxPython-2.8.7.1
sage -i vtk-5.0.4.p0


cd src

python egg_builder.py -r -v

easy_install -f dist -H dist enthought.mayavi*



---

archive/issue_comments_016881.json:
```json
{
    "body": "The mayavi_2.1.1-20080307.p1.spkg does not work for me.\n\n\n```\nMayaVi2 seems to build, but fails to run mlab!\n\nWhat the difference between mayavi_2.1.1-20080307.p1.spkg\nand my original mayavi_2.1.1-20080307.spkg?\n\n1) mv mayavi_build src\n2) rm all .svn stuff\n3) add .hg and friends\n\n```\n\nMy hypothesis for now is that the .svn directories contain\nessential information for the build system. I might be wrong, ...\n\nI did a diff -r on both directories, only .svn files missing! See:\n\nhttp://sage.math.washington.edu/home/jsp/diff_file\n\nI did a fresh install on fresh installed sage-2.10.4,\nsage-2.11.alpha0, sage-2.11.alpha1 on two machines. The results are consistent.",
    "created_at": "2008-03-27T15:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16881",
    "user": "https://github.com/jaapspies"
}
```

The mayavi_2.1.1-20080307.p1.spkg does not work for me.


```
MayaVi2 seems to build, but fails to run mlab!

What the difference between mayavi_2.1.1-20080307.p1.spkg
and my original mayavi_2.1.1-20080307.spkg?

1) mv mayavi_build src
2) rm all .svn stuff
3) add .hg and friends

```

My hypothesis for now is that the .svn directories contain
essential information for the build system. I might be wrong, ...

I did a diff -r on both directories, only .svn files missing! See:

http://sage.math.washington.edu/home/jsp/diff_file

I did a fresh install on fresh installed sage-2.10.4,
sage-2.11.alpha0, sage-2.11.alpha1 on two machines. The results are consistent.



---

archive/issue_comments_016882.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-27T15:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16882",
    "user": "https://github.com/jaapspies"
}
```

Changing status from closed to reopened.



---

archive/issue_events_005874.json:
```json
{
    "actor": "https://github.com/jaapspies",
    "created_at": "2008-03-27T15:14:27Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2495#event-5874"
}
```



---

archive/issue_comments_016883.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-03-27T15:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16883",
    "user": "https://github.com/jaapspies"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_016884.json:
```json
{
    "body": "About time to close this ticket again! A working modified version can be found here:\n\nhttp://sage.math.washington.edu/home/jsp/mayavi_2.1.1-20080307.p1.spkg\n\nNow the package is announced to be in sage-2.11 I don't think it is wise to have a wrong spkg in the experimental repo.\n\nJaap",
    "created_at": "2008-03-31T11:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16884",
    "user": "https://github.com/jaapspies"
}
```

About time to close this ticket again! A working modified version can be found here:

http://sage.math.washington.edu/home/jsp/mayavi_2.1.1-20080307.p1.spkg

Now the package is announced to be in sage-2.11 I don't think it is wise to have a wrong spkg in the experimental repo.

Jaap



---

archive/issue_comments_016885.json:
```json
{
    "body": "Updated the spkg with Jaap's latest. So I am closing this again since I just mirrored the repo out again.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-31T11:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Updated the spkg with Jaap's latest. So I am closing this again since I just mirrored the repo out again.

Cheers,

Michael



---

archive/issue_events_005875.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-31T11:27:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2495#event-5875"
}
```



---

archive/issue_comments_016886.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-31T11:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2495#issuecomment-16886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
