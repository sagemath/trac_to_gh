# Issue 7485: make fortran a prerequisite on all platforms except OS X.  Remove g95 binaries from Sage

archive/issues_007485.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7485\n\n",
    "created_at": "2009-11-18T07:14:59Z",
    "labels": [
        "component: build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "make fortran a prerequisite on all platforms except OS X.  Remove g95 binaries from Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7485",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/7485





---

archive/issue_comments_063104.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T11:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63104",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063105.json:
```json
{
    "body": "Here is the spkg:\n\n   http://wstein.org/home/wstein/patches/fortran-20100117.spkg\n\nNote, after first trying to do something very complicated, involving changing the gfortran OS X binary to really use its quadcore stuff, etc., etc., I realized that could cause endless trouble, so can be put off.  So the point of this spkg is just a very simple and humble goal -- no more g95 binaries when building Sage on linux.  That is it.\n\nOh, regarding SAGE_FORTRAN_LIB, one shouldn't need to set that unless one's setup is weird, in which case one sets SAGE_FORTAN and SAGE_FORTRAN_LIB anyways.  So in the attached spkg, I only set SAGE_FORTRAN, not SAGE_FORTRAN_LIB.\n\nNOTE: On Linux, this spkg change makes Sage depend on having gfortran installed.  So it would be a good idea to update prereq accordingly, but that should not be part of this ticket.",
    "created_at": "2010-01-17T11:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63105",
    "user": "https://github.com/williamstein"
}
```

Here is the spkg:

   http://wstein.org/home/wstein/patches/fortran-20100117.spkg

Note, after first trying to do something very complicated, involving changing the gfortran OS X binary to really use its quadcore stuff, etc., etc., I realized that could cause endless trouble, so can be put off.  So the point of this spkg is just a very simple and humble goal -- no more g95 binaries when building Sage on linux.  That is it.

Oh, regarding SAGE_FORTRAN_LIB, one shouldn't need to set that unless one's setup is weird, in which case one sets SAGE_FORTAN and SAGE_FORTRAN_LIB anyways.  So in the attached spkg, I only set SAGE_FORTRAN, not SAGE_FORTRAN_LIB.

NOTE: On Linux, this spkg change makes Sage depend on having gfortran installed.  So it would be a good idea to update prereq accordingly, but that should not be part of this ticket.



---

archive/issue_comments_063106.json:
```json
{
    "body": "The new Fortran spkg cuts about 7 MB. The Fortran spkg in Sage 4.3.1.rc0 is about 40MB:\n\n```\nmvngu@mod standard]$ du -hs fortran-20071120.p9.spkg \n40M     fortran-20071120.p9.spkg\n```\n\nwhile the new spkg is about 33 MB:\n\n```\n[mvngu@mod fortran]$ du -hs fortran-20100117.spkg \n33M\tfortran-20100117.spkg\n```\n\nThat should be good news for mirroring and downloading the source distribution. Just a trivial nit-pick. The file `spkg-install` has changes that are not yet checked in:\n\n```\n[mvngu@mod fortran-20100117]$ hg st\nM spkg-install\n```\n\nSince the Linux Fortran binaries have been removed from the Fortran spkg, do you still want to keep the following conditional in the file `spkg-install`? Between lines 75--81:\n\n```\n    elif OS == 'linux':\n       if arch == 'x86_64':\n          print \"Installing Linux x86-64 g95 compiler\"\n          file = 'g95_linux_64.tar.bz2'\n       elif arch == 'i686' or arch == 'i586' or arch == 'i486' or arch == 'i386':\n          print \"Installing Linux i686 g95 compiler\"\n          file = 'g95_linux_32.tar.bz2'\n```\n",
    "created_at": "2010-01-18T12:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63106",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The new Fortran spkg cuts about 7 MB. The Fortran spkg in Sage 4.3.1.rc0 is about 40MB:

```
mvngu@mod standard]$ du -hs fortran-20071120.p9.spkg 
40M     fortran-20071120.p9.spkg
```

while the new spkg is about 33 MB:

```
[mvngu@mod fortran]$ du -hs fortran-20100117.spkg 
33M	fortran-20100117.spkg
```

That should be good news for mirroring and downloading the source distribution. Just a trivial nit-pick. The file `spkg-install` has changes that are not yet checked in:

```
[mvngu@mod fortran-20100117]$ hg st
M spkg-install
```

Since the Linux Fortran binaries have been removed from the Fortran spkg, do you still want to keep the following conditional in the file `spkg-install`? Between lines 75--81:

```
    elif OS == 'linux':
       if arch == 'x86_64':
          print "Installing Linux x86-64 g95 compiler"
          file = 'g95_linux_64.tar.bz2'
       elif arch == 'i686' or arch == 'i586' or arch == 'i486' or arch == 'i386':
          print "Installing Linux i686 g95 compiler"
          file = 'g95_linux_32.tar.bz2'
```




---

archive/issue_comments_063107.json:
```json
{
    "body": "> Since the Linux Fortran binaries have been removed from the \n>Fortran spkg, do you still want to keep the following conditional in the file spkg-install? \n\nI do.  I want to make minimal changes to the spkg so that it works.  I'm not keen on breaking anything, and there is arbitrarily much that can go wrong.\n\nNote that in future we should be able to get rid of the rest of the g95 binaries, shrinking the size of the spkg another 10MB or so.\n\nThe new spkg is here:\n\n    http://wstein.org/home/wstein/patches/fortran-20100118.spkg\n\nIt just checks in the changes.",
    "created_at": "2010-01-18T13:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63107",
    "user": "https://github.com/williamstein"
}
```

> Since the Linux Fortran binaries have been removed from the 
>Fortran spkg, do you still want to keep the following conditional in the file spkg-install? 

I do.  I want to make minimal changes to the spkg so that it works.  I'm not keen on breaking anything, and there is arbitrarily much that can go wrong.

Note that in future we should be able to get rid of the rest of the g95 binaries, shrinking the size of the spkg another 10MB or so.

The new spkg is here:

    http://wstein.org/home/wstein/patches/fortran-20100118.spkg

It just checks in the changes.



---

archive/issue_comments_063108.json:
```json
{
    "body": "Looks good. On Linux and Solaris machines (mod.math, rosemary.math, t2.math), only the script `sage_fortran` is installed under `SAGE_LOCAL/bin`. This is in contrast to the previous behaviour, which was to install Linux Fortran binaries regardless of whether the Linux system already had a system-wide Fortran compiler. On OS X machine (bsd.math), `sage_fortran` and OS X specific Fortran binaries are installed under `SAGE_LOCAL/bin` as expected. I tested [fortran-20100118.spkg](http://wstein.org/home/wstein/patches/fortran-20100118.spkg) with Sage 4.3.1.rc1 on mod.math, rosemary.math, and bsd.math. Doctesting resulted in the following known failure as reported on [sage-devel](http://groups.google.com/group/sage-devel/msg/7c9e8c5a006e4f9f):\n\n```\n[mvngu@boxen sage-4.3.1.rc1]$ ./sage -t -long devel/sage-main/sage/misc/sagedoc.py \nsage -t -long \"devel/sage-main/sage/misc/sagedoc.py\"        \n**********************************************************************\nFile \"/dev/shm/mvngu/sage-4.3.1.rc1/devel/sage-main/sage/misc/sagedoc.py\", line 365:\n    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_sagedoc.py\n\t [20.8 s]\nexit code: 1024\n```\n\nThe changes in this updated Fortran spkg are minimal. Linux specific Fortran binaries have been removed. The install script `spkg-install` is essentially as it was previously, with the added test that if the current system is Linux, then test to see if that system has a Fortran compiler.",
    "created_at": "2010-01-19T18:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63108",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Looks good. On Linux and Solaris machines (mod.math, rosemary.math, t2.math), only the script `sage_fortran` is installed under `SAGE_LOCAL/bin`. This is in contrast to the previous behaviour, which was to install Linux Fortran binaries regardless of whether the Linux system already had a system-wide Fortran compiler. On OS X machine (bsd.math), `sage_fortran` and OS X specific Fortran binaries are installed under `SAGE_LOCAL/bin` as expected. I tested [fortran-20100118.spkg](http://wstein.org/home/wstein/patches/fortran-20100118.spkg) with Sage 4.3.1.rc1 on mod.math, rosemary.math, and bsd.math. Doctesting resulted in the following known failure as reported on [sage-devel](http://groups.google.com/group/sage-devel/msg/7c9e8c5a006e4f9f):

```
[mvngu@boxen sage-4.3.1.rc1]$ ./sage -t -long devel/sage-main/sage/misc/sagedoc.py 
sage -t -long "devel/sage-main/sage/misc/sagedoc.py"        
**********************************************************************
File "/dev/shm/mvngu/sage-4.3.1.rc1/devel/sage-main/sage/misc/sagedoc.py", line 365:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_sagedoc.py
	 [20.8 s]
exit code: 1024
```

The changes in this updated Fortran spkg are minimal. Linux specific Fortran binaries have been removed. The install script `spkg-install` is essentially as it was previously, with the added test that if the current system is Linux, then test to see if that system has a Fortran compiler.



---

archive/issue_comments_063109.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T18:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63109",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063110.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T20:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63110",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_017745.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-19T20:27:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7485#event-17745"
}
```



---

archive/issue_comments_063111.json:
```json
{
    "body": "This may also fix some of the R issues we have seen, e.g at #6279.  See #6532 for more details.",
    "created_at": "2010-01-19T20:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63111",
    "user": "https://github.com/kcrisman"
}
```

This may also fix some of the R issues we have seen, e.g at #6279.  See #6532 for more details.



---

archive/issue_comments_063112.json:
```json
{
    "body": "See #7484 for a follow-up to update README.txt to require Fortran as a pre-requisite under Linux.",
    "created_at": "2010-01-20T20:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63112",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #7484 for a follow-up to update README.txt to require Fortran as a pre-requisite under Linux.



---

archive/issue_comments_063113.json:
```json
{
    "body": "See #8024 for an update to 'prereq' to check a Fortran compiler exists on platforms other than OS X.",
    "created_at": "2010-01-21T13:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63113",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

See #8024 for an update to 'prereq' to check a Fortran compiler exists on platforms other than OS X.



---

archive/issue_comments_063114.json:
```json
{
    "body": "Why not include it for Linux? I think having a good fortran compiler is essential for library dependencies such as BLAS",
    "created_at": "2010-02-17T13:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7485#issuecomment-63114",
    "user": "https://trac.sagemath.org/admin/accounts/users/magawake"
}
```

Why not include it for Linux? I think having a good fortran compiler is essential for library dependencies such as BLAS
