# Issue 8514: Optional database_gap-4.4.12 fails to install on Solaris 10 SPARC

archive/issues_008514.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wdj\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n\nThis builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. \n\n == The problem with the optional database_gap-4.4.12 ==\n\n```\ndatabase_gap-4.4.12/.hg/requires\ndatabase_gap-4.4.12/.hg/00changelog.i\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.4.3 (GCC)\n****************************************************\n./spkg-install: bad substitution\n\nreal    0m0.015s\nuser    0m0.004s\nsys     0m0.011s\nsage: An error occurred while installing database_gap-4.4.12\n```\n\n\n == The solution ==\n\nspkg-install looks a bit of a mess to me. I will need to try to work out what the author intended. SPKG.txt gives no idea of the author or anything very useful. It's contents are just:\n\n\n```\nGAP's databases of finite groups and table of marks.\n```\n\n\nI need to be a bit of a detective to work this out!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/8514\n\n",
    "created_at": "2010-03-13T01:13:49Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "title": "Optional database_gap-4.4.12 fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8514",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  wdj

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.3.4.alpha1

This builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. 

 == The problem with the optional database_gap-4.4.12 ==

```
database_gap-4.4.12/.hg/requires
database_gap-4.4.12/.hg/00changelog.i
Finished extraction
****************************************************
Host system
uname -a:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.4.3 (GCC)
****************************************************
./spkg-install: bad substitution

real    0m0.015s
user    0m0.004s
sys     0m0.011s
sage: An error occurred while installing database_gap-4.4.12
```


 == The solution ==

spkg-install looks a bit of a mess to me. I will need to try to work out what the author intended. SPKG.txt gives no idea of the author or anything very useful. It's contents are just:


```
GAP's databases of finite groups and table of marks.
```


I need to be a bit of a detective to work this out!!

Issue created by migration from https://trac.sagemath.org/ticket/8514





---

archive/issue_comments_076901.json:
```json
{
    "body": "same spkg-install problem as in #8520",
    "created_at": "2010-03-15T08:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76901",
    "user": "dimpase"
}
```

same spkg-install problem as in #8520



---

archive/issue_comments_076902.json:
```json
{
    "body": "Replying to [comment:1 drkirkby]:\n\nplease try \n\nhttp://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p1.spkg",
    "created_at": "2010-03-15T12:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76902",
    "user": "dimpase"
}
```

Replying to [comment:1 drkirkby]:

please try 

http://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p1.spkg



---

archive/issue_comments_076903.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-15T12:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76903",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076904.json:
```json
{
    "body": "No, this does not work:\n\n\n```\ndrkirkby@redstart:~/sage-4.3.4.alpha1$ ./sage -i http://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p1.spkg\n\n<snip all downloading and most extracting> \n\ndatabase_gap-4.4.12/.hg/undo.dirstate\ndatabase_gap-4.4.12/.hg/undo.branch\ndatabase_gap-4.4.12/spkg-install\ntar: This does not look like a tar archive\ntar: Skipping to next header\ntar: Archive contains obsolescent base-64 headers\ntar: Read 2894 bytes from /export/home/drkirkby/sage-4.3.4.alpha1/spkg/optional/database_gap-4.4.12.p1.spkg\ntar: Error exit delayed from previous errors\nFinished extraction\nsage: After decompressing the directory database_gap-4.4.12.p1 does not exist\nThis means that the corresponding .spkg needs to be downloaded\nagain.\nhttp://www.sagemath.org//packages/optional/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg\n[ ]\nhttp://www.sagemath.org//packages/standard/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg\n[ ]\nhttp://www.sagemath.org//packages/experimental/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg\n[ ]\nhttp://www.sagemath.org//packages/archive/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg\n[ ]\n**********************************************************************\n* Unable to download database_gap-4.4.12.p1\n* Please see http://www.sagemath.org//packages for a list of valid\n* packages or check the package name.\n**********************************************************************\n/export/home/drkirkby/sage-4.3.4.alpha1/spkg/build\nbunzip2: Can't open input file database_gap-4.4.12.p1.spkg: No such file or directory.\ntar: database_gap-4.4.12.p1.spkg: Cannot open: No such file or directory\ntar: Error is not recoverable: exiting now\nSecond download resulted in a corrupted package.\n```\n\n\nDespite the fact the database is called database_gap-4.4.12.p0, the files are in a directory database_gap-4.4.12, which is not the normal way to do it. But in any case, it is now working.",
    "created_at": "2010-03-16T00:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76904",
    "user": "drkirkby"
}
```

No, this does not work:


```
drkirkby@redstart:~/sage-4.3.4.alpha1$ ./sage -i http://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p1.spkg

<snip all downloading and most extracting> 

database_gap-4.4.12/.hg/undo.dirstate
database_gap-4.4.12/.hg/undo.branch
database_gap-4.4.12/spkg-install
tar: This does not look like a tar archive
tar: Skipping to next header
tar: Archive contains obsolescent base-64 headers
tar: Read 2894 bytes from /export/home/drkirkby/sage-4.3.4.alpha1/spkg/optional/database_gap-4.4.12.p1.spkg
tar: Error exit delayed from previous errors
Finished extraction
sage: After decompressing the directory database_gap-4.4.12.p1 does not exist
This means that the corresponding .spkg needs to be downloaded
again.
http://www.sagemath.org//packages/optional/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg
[ ]
http://www.sagemath.org//packages/standard/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg
[ ]
http://www.sagemath.org//packages/experimental/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg
[ ]
http://www.sagemath.org//packages/archive/database_gap-4.4.12.p1.spkg --> database_gap-4.4.12.p1.spkg
[ ]
**********************************************************************
* Unable to download database_gap-4.4.12.p1
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
/export/home/drkirkby/sage-4.3.4.alpha1/spkg/build
bunzip2: Can't open input file database_gap-4.4.12.p1.spkg: No such file or directory.
tar: database_gap-4.4.12.p1.spkg: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
Second download resulted in a corrupted package.
```


Despite the fact the database is called database_gap-4.4.12.p0, the files are in a directory database_gap-4.4.12, which is not the normal way to do it. But in any case, it is now working.



---

archive/issue_comments_076905.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-16T00:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76905",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076906.json:
```json
{
    "body": "Since the original was called database_gap-4.4.12, the new one should be database_gap-4.4.12.p0 and extract to a directory database_gap-4.4.12.p0. (This is called p1. Convention is we start patch levels at 0). \n\nDave",
    "created_at": "2010-03-16T00:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76906",
    "user": "drkirkby"
}
```

Since the original was called database_gap-4.4.12, the new one should be database_gap-4.4.12.p0 and extract to a directory database_gap-4.4.12.p0. (This is called p1. Convention is we start patch levels at 0). 

Dave



---

archive/issue_comments_076907.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n> Since the original was called database_gap-4.4.12, the new one should be database_gap-4.4.12.p0 and extract to a directory database_gap-4.4.12.p0. (This is called p1. Convention is we start patch levels at 0). \n> \n \nOK, sorry for this mess.\n\nHere is the numbering done right. I tested this on t2 and elsewhere\n\n http://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p0.spkg",
    "created_at": "2010-03-16T12:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76907",
    "user": "dimpase"
}
```

Replying to [comment:6 drkirkby]:
> Since the original was called database_gap-4.4.12, the new one should be database_gap-4.4.12.p0 and extract to a directory database_gap-4.4.12.p0. (This is called p1. Convention is we start patch levels at 0). 
> 
 
OK, sorry for this mess.

Here is the numbering done right. I tested this on t2 and elsewhere

 http://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p0.spkg



---

archive/issue_comments_076908.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-16T12:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76908",
    "user": "dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076909.json:
```json
{
    "body": "Hi David, \nwould you mind having a look at this?\nThanks,\nDima",
    "created_at": "2010-03-25T12:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76909",
    "user": "dimpase"
}
```

Hi David, 
would you mind having a look at this?
Thanks,
Dima



---

archive/issue_comments_076910.json:
```json
{
    "body": "Replying to [comment:8 dimpase]:\n> Hi David, \n> would you mind having a look at this?\n> Thanks,\n> Dima\n\nI am happy to test this but I don't have access to a sparc. It seems David Kirkby is saying that it works on a sparc machine but the download+install was a problem?\n\nAnyway, I donloaded it first the installed using sage -i with no problems. Tested that the database of small groups was loaded into the GAP workspace Sage uses and that IdGroup works as expected.\n\nPositive review from me.",
    "created_at": "2010-03-26T11:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76910",
    "user": "wdj"
}
```

Replying to [comment:8 dimpase]:
> Hi David, 
> would you mind having a look at this?
> Thanks,
> Dima

I am happy to test this but I don't have access to a sparc. It seems David Kirkby is saying that it works on a sparc machine but the download+install was a problem?

Anyway, I donloaded it first the installed using sage -i with no problems. Tested that the database of small groups was loaded into the GAP workspace Sage uses and that IdGroup works as expected.

Positive review from me.



---

archive/issue_comments_076911.json:
```json
{
    "body": "I'll take a look in a few hours - just about to start a chess game!\n\ndave",
    "created_at": "2010-03-26T13:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76911",
    "user": "drkirkby"
}
```

I'll take a look in a few hours - just about to start a chess game!

dave



---

archive/issue_comments_076912.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-28T13:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76912",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076913.json:
```json
{
    "body": "Sorry for the delay in replying - I got distracted after the chess game, which I rather annoying only drew against a much weaker opponent. \n\nAlthough I can't test the packages, due to a lack of knowledge of gap, it looks fine to me. \n\nPositive review.",
    "created_at": "2010-03-28T13:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76913",
    "user": "drkirkby"
}
```

Sorry for the delay in replying - I got distracted after the chess game, which I rather annoying only drew against a much weaker opponent. 

Although I can't test the packages, due to a lack of knowledge of gap, it looks fine to me. 

Positive review.



---

archive/issue_comments_076914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-20T22:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76914",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_076915.json:
```json
{
    "body": "Merged 2010/04/20.",
    "created_at": "2010-04-20T22:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8514#issuecomment-76915",
    "user": "jhpalmieri"
}
```

Merged 2010/04/20.
