# Issue 4891: make a command that installs all optional spkg's and reports the ones that don't work.

archive/issues_004891.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is 100% for testing use.  I've written this and will post a patch soon.\n\nNOTE: Nauty has a stupid interactive license agreement which somewhat messes up this command, since it makes it not 100% automatic.    I hate that.  I've made trac #4890 to get rid of it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4891\n\n",
    "created_at": "2008-12-30T07:28:37Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "make a command that installs all optional spkg's and reports the ones that don't work.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4891",
    "user": "was"
}
```
Assignee: mabshoff

This is 100% for testing use.  I've written this and will post a patch soon.

NOTE: Nauty has a stupid interactive license agreement which somewhat messes up this command, since it makes it not 100% automatic.    I hate that.  I've made trac #4890 to get rid of it.

Issue created by migration from https://trac.sagemath.org/ticket/4891





---

archive/issue_comments_037085.json:
```json
{
    "body": "Attachment [trac_4891.patch](tarball://root/attachments/some-uuid/ticket4891/trac_4891.patch) by was created at 2008-12-30 07:54:50\n\nFor the record, when I run this on sage.math it takes a total of a half hour (pretty fast!) and finishes with the following:\n\n```\n...\nSuccessfully installed valgrind_3.3.1\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing valgrind_3.3.1.spkg\nCPU times: user 0.03 s, sys: 1.54 s, total: 1.57 s\nWall time: 1925.36 s\n['boehm_gc-7.1.p0', 'mpi4py-0.3.1']\n```\n\n\nSo boehm and mpi4py failed to install.  But everything else in optional succeeded.  Note that there is  an inconsistency, since according to the output of optional_packages() in fact mpi4py and fricas failed but everything else succeeded:\n\n```\n ['fricas-1.0.3.p0', 'mpi4py-0.3.1'])\n```\n\nThis I think points to bugs in the package install system, not in this patch.",
    "created_at": "2008-12-30T07:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37085",
    "user": "was"
}
```

Attachment [trac_4891.patch](tarball://root/attachments/some-uuid/ticket4891/trac_4891.patch) by was created at 2008-12-30 07:54:50

For the record, when I run this on sage.math it takes a total of a half hour (pretty fast!) and finishes with the following:

```
...
Successfully installed valgrind_3.3.1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing valgrind_3.3.1.spkg
CPU times: user 0.03 s, sys: 1.54 s, total: 1.57 s
Wall time: 1925.36 s
['boehm_gc-7.1.p0', 'mpi4py-0.3.1']
```


So boehm and mpi4py failed to install.  But everything else in optional succeeded.  Note that there is  an inconsistency, since according to the output of optional_packages() in fact mpi4py and fricas failed but everything else succeeded:

```
 ['fricas-1.0.3.p0', 'mpi4py-0.3.1'])
```

This I think points to bugs in the package install system, not in this patch.



---

archive/issue_comments_037086.json:
```json
{
    "body": "boehm_gc-7.1.p0 is already in standard Sage, but also in the optional repo in case someone wants to install M2 into an older version of Sage.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T10:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37086",
    "user": "mabshoff"
}
```

boehm_gc-7.1.p0 is already in standard Sage, but also in the optional repo in case someone wants to install M2 into an older version of Sage.

Cheers,

Michael



---

archive/issue_comments_037087.json:
```json
{
    "body": "I tested on OS X and got:\n\n```\nThread model: posix\ngcc version 4.0.1 (Apple Inc. build 5465)\n****************************************************\nValgring does not work on non-Linux yet\n\nreal    0m0.012s\nuser    0m0.003s\nsys     0m0.007s\nsage: An error occurred while installing valgrind_3.3.1\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Users/was/build/sage-3.2.2/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/Users/was/build/sage-3.2.2/spkg/build/valgrind_3.3.1 and type 'make'.\nInstead type \"/Users/was/build/sage-3.2.2/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/Users/was/build/sage-3.2.2/spkg/build/valgrind_3.3.1\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\nCPU times: user 0.07 s, sys: 1.29 s, total: 1.37 s\nWall time: 4061.35 s\nsage:\nsage: v\n['boehm_gc-7.1.p0', 'mpi4py-0.3.1']\nsage:\n```\n\n\nSo the error detection (i.e., when an exception is raised) in install_packages is clearly buggy.  But I don't think that should hold this patch back, since that's a separate bug in a different function, and should be addressed in another ticket.",
    "created_at": "2008-12-30T17:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37087",
    "user": "was"
}
```

I tested on OS X and got:

```
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5465)
****************************************************
Valgring does not work on non-Linux yet

real    0m0.012s
user    0m0.003s
sys     0m0.007s
sage: An error occurred while installing valgrind_3.3.1
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/was/build/sage-3.2.2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/was/build/sage-3.2.2/spkg/build/valgrind_3.3.1 and type 'make'.
Instead type "/Users/was/build/sage-3.2.2/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/was/build/sage-3.2.2/spkg/build/valgrind_3.3.1
(When you are done debugging, you can type "exit" to leave the
subshell.)
CPU times: user 0.07 s, sys: 1.29 s, total: 1.37 s
Wall time: 4061.35 s
sage:
sage: v
['boehm_gc-7.1.p0', 'mpi4py-0.3.1']
sage:
```


So the error detection (i.e., when an exception is raised) in install_packages is clearly buggy.  But I don't think that should hold this patch back, since that's a separate bug in a different function, and should be addressed in another ticket.



---

archive/issue_comments_037088.json:
```json
{
    "body": "> boehm_gc-7.1.p0 is already in standard Sage, but also in the optional repo in case \n> someone wants to install M2 into an older version of Sage. \n\nI propose removing it or at least moving it to experimental, since M2 is only in experimental after all.",
    "created_at": "2008-12-30T17:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37088",
    "user": "was"
}
```

> boehm_gc-7.1.p0 is already in standard Sage, but also in the optional repo in case 
> someone wants to install M2 into an older version of Sage. 

I propose removing it or at least moving it to experimental, since M2 is only in experimental after all.



---

archive/issue_comments_037089.json:
```json
{
    "body": "Replying to [comment:5 was]:\n\n> I propose removing it or at least moving it to experimental, since M2 is only in experimental after all. \n> \n\nFine by me since we have shipped it with standard for a while. Maybe the install_package routine should be smarter about already installed spkgs, too?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T17:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37089",
    "user": "mabshoff"
}
```

Replying to [comment:5 was]:

> I propose removing it or at least moving it to experimental, since M2 is only in experimental after all. 
> 

Fine by me since we have shipped it with standard for a while. Maybe the install_package routine should be smarter about already installed spkgs, too?

Cheers,

Michael



---

archive/issue_comments_037090.json:
```json
{
    "body": "Replying to [comment:4 was]:\n\n<SNIP>\n\n> So the error detection (i.e., when an exception is raised) in install_packages is clearly buggy.  But I don't think that should hold this patch back, since that's a separate bug in a different function, and should be addressed in another ticket. \n\nSure. Should we chose a certain exit code if the spkg does not work on a given platform to signal that? So far we always seem to exit spkg-install with 1 when a failure occurs, so assigning meaningful exit codes could come in handy.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T17:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37090",
    "user": "mabshoff"
}
```

Replying to [comment:4 was]:

<SNIP>

> So the error detection (i.e., when an exception is raised) in install_packages is clearly buggy.  But I don't think that should hold this patch back, since that's a separate bug in a different function, and should be addressed in another ticket. 

Sure. Should we chose a certain exit code if the spkg does not work on a given platform to signal that? So far we always seem to exit spkg-install with 1 when a failure occurs, so assigning meaningful exit codes could come in handy.

Cheers,

Michael



---

archive/issue_comments_037091.json:
```json
{
    "body": "Code looks fine, here's the test output:\n\n\n```\n...\nMaking script relocatable\nFinished installing valgrind_3.3.1.spkg\n['boehm_gc-7.1.p0', 'mpi4py-0.3.1']\nsage: optional_packages()\n...\n  'trac-20071204',\n  'valgrind_3.3.1'],\n ['mpi4py-0.3.1', 'polymake-2.2.p5'])\n```\n",
    "created_at": "2009-01-24T12:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37091",
    "user": "malb"
}
```

Code looks fine, here's the test output:


```
...
Making script relocatable
Finished installing valgrind_3.3.1.spkg
['boehm_gc-7.1.p0', 'mpi4py-0.3.1']
sage: optional_packages()
...
  'trac-20071204',
  'valgrind_3.3.1'],
 ['mpi4py-0.3.1', 'polymake-2.2.p5'])
```




---

archive/issue_comments_037092.json:
```json
{
    "body": "I guess that means **positiv review**",
    "created_at": "2009-01-24T12:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37092",
    "user": "malb"
}
```

I guess that means **positiv review**



---

archive/issue_comments_037093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37093",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037094.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4891#issuecomment-37094",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
