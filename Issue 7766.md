# Issue 7766: Upgrade optional spkg valgrind to valgrind-3.6.0.svn

archive/issues_007766.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  timdumol rlm iandrus jpflori kini\n\nKeywords: memory testing\n\nThe optional valgrind-3.1.1 did not build in Fedora 12 x86_64\n\nreason: glibc-11 is not supported. Even in the last released stable valgrind-3.5.0\n\nSo I downloaded from SVN and made an spkg.\n\nSee: [http://sage.math.washington.edu/home/jsp/valgrind-3.6.0.svn.spkg](http://sage.math.washington.edu/home/jsp/valgrind-3.6.0.svn.spkg)\n\nUrgent: we need a maintainer other than me and Michael!\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/7766\n\n",
    "created_at": "2009-12-25T20:36:30Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Upgrade optional spkg valgrind to valgrind-3.6.0.svn",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7766",
    "user": "jsp"
}
```
Assignee: tbd

CC:  timdumol rlm iandrus jpflori kini

Keywords: memory testing

The optional valgrind-3.1.1 did not build in Fedora 12 x86_64

reason: glibc-11 is not supported. Even in the last released stable valgrind-3.5.0

So I downloaded from SVN and made an spkg.

See: [http://sage.math.washington.edu/home/jsp/valgrind-3.6.0.svn.spkg](http://sage.math.washington.edu/home/jsp/valgrind-3.6.0.svn.spkg)

Urgent: we need a maintainer other than me and Michael!

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/7766





---

archive/issue_comments_066915.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T13:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66915",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066916.json:
```json
{
    "body": "Ticket #7440 has upgraded the optional Valgrind spkg to version 3.5.0. Tim Dumol has agreed to maintain that spkg.",
    "created_at": "2010-01-23T09:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66916",
    "user": "mvngu"
}
```

Ticket #7440 has upgraded the optional Valgrind spkg to version 3.5.0. Tim Dumol has agreed to maintain that spkg.



---

archive/issue_comments_066917.json:
```json
{
    "body": "Replying to [comment:2 mvngu]:\n> Ticket #7440 has upgraded the optional Valgrind spkg to version 3.5.0. Tim Dumol has agreed to maintain that spkg.\n\n\nvalgrind-3.5.0 didn't compile with Fedora 12 64 bit.\n\nJaap",
    "created_at": "2010-01-23T10:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66917",
    "user": "jsp"
}
```

Replying to [comment:2 mvngu]:
> Ticket #7440 has upgraded the optional Valgrind spkg to version 3.5.0. Tim Dumol has agreed to maintain that spkg.


valgrind-3.5.0 didn't compile with Fedora 12 64 bit.

Jaap



---

archive/issue_comments_066918.json:
```json
{
    "body": "It may be worth rebasing this on #7440. `spkg-install` was updated on #7440 to detect Darwin 9.0 as well, on which Valgrind 3.5.0 works on. Also, mabshoff's name should be removed from the package, as per #7738. Feel free to add your own name to the maintainers list as well. Those issues aside, the package seems to work perfectly here. Nice work.",
    "created_at": "2010-01-23T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66918",
    "user": "timdumol"
}
```

It may be worth rebasing this on #7440. `spkg-install` was updated on #7440 to detect Darwin 9.0 as well, on which Valgrind 3.5.0 works on. Also, mabshoff's name should be removed from the package, as per #7738. Feel free to add your own name to the maintainers list as well. Those issues aside, the package seems to work perfectly here. Nice work.



---

archive/issue_comments_066919.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-23T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66919",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066920.json:
```json
{
    "body": "Replying to [comment:4 timdumol]:\n> It may be worth rebasing this on #7440. `spkg-install` was updated on #7440 to detect Darwin 9.0 as well, on which Valgrind 3.5.0 works on. Also, mabshoff's name should be removed from the package, as per #7738. Feel free to add your own name to the maintainers list as well. Those issues aside, the package seems to work perfectly here. Nice work.\n\nHi Tim,\n\nWould you mind taking over? I'm not a valgrind expert as Michael was.\n\nI have some problems with sage -t on Fedora 12 64 bit on my computer with i7 860 processor. So I tried valgrind. It came up with some issues. See:\n[http://trac.sagemath.org/sage_trac/ticket/7773](http://trac.sagemath.org/sage_trac/ticket/7773) \n\nJaap",
    "created_at": "2010-01-23T22:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66920",
    "user": "jsp"
}
```

Replying to [comment:4 timdumol]:
> It may be worth rebasing this on #7440. `spkg-install` was updated on #7440 to detect Darwin 9.0 as well, on which Valgrind 3.5.0 works on. Also, mabshoff's name should be removed from the package, as per #7738. Feel free to add your own name to the maintainers list as well. Those issues aside, the package seems to work perfectly here. Nice work.

Hi Tim,

Would you mind taking over? I'm not a valgrind expert as Michael was.

I have some problems with sage -t on Fedora 12 64 bit on my computer with i7 860 processor. So I tried valgrind. It came up with some issues. See:
[http://trac.sagemath.org/sage_trac/ticket/7773](http://trac.sagemath.org/sage_trac/ticket/7773) 

Jaap



---

archive/issue_comments_066921.json:
```json
{
    "body": "Is there an option to install the package via SVN or is the spkg-file in the download link really broken?\n\nThere are some empty shell script in the package, I repaired it for my self with copying some of the files from valgrind.3,5.0 package, and it worked fine.",
    "created_at": "2010-08-28T14:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66921",
    "user": "maldun"
}
```

Is there an option to install the package via SVN or is the spkg-file in the download link really broken?

There are some empty shell script in the package, I repaired it for my self with copying some of the files from valgrind.3,5.0 package, and it worked fine.



---

archive/issue_comments_066922.json:
```json
{
    "body": "I created a new spkg from 3.6.1.  Since 3.6.1 works on OS X 10.6, I added support for that as well.  You can find the spkg at http://boxen.math.washington.edu/home/iandrus/valgrind-3.6.1.p0.spkg\nI based it off of the spkg at #7440.\n\nOne other (perhaps controversial) thing that I did is add suppressions so that starting sage under valgrind and immediately exiting shows no leaks.  I was also using the suppression file provided by python which should probably be installed as part of the python spkg-install.  Some (or many) of these may be actual leaks, but I don't have the expertise to check them all.  Because I don't know if all the suppressions are valid I'm hesitant to mark this as needs_review.",
    "created_at": "2011-03-23T22:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66922",
    "user": "iandrus"
}
```

I created a new spkg from 3.6.1.  Since 3.6.1 works on OS X 10.6, I added support for that as well.  You can find the spkg at http://boxen.math.washington.edu/home/iandrus/valgrind-3.6.1.p0.spkg
I based it off of the spkg at #7440.

One other (perhaps controversial) thing that I did is add suppressions so that starting sage under valgrind and immediately exiting shows no leaks.  I was also using the suppression file provided by python which should probably be installed as part of the python spkg-install.  Some (or many) of these may be actual leaks, but I don't have the expertise to check them all.  Because I don't know if all the suppressions are valid I'm hesitant to mark this as needs_review.



---

archive/issue_comments_066923.json:
```json
{
    "body": "I have added `spkg-test` to run valgrind's test suite (which fails for me on OS X 10.6.7).\n\nI created 2 suppression files sage.supp which is the same file as before and sage-liberal.supp which is enough to suppress all the errors caused by sage startup.  When testing you can set `MEMCHECK_FLAGS` to change the suppression file you use.  In #11035 I plan to patch sage-valgrind to be able to switch between the two easily.\n\nThe default for the moment is to use the same suppression file as before, so it should be 'safer'.",
    "created_at": "2011-03-26T01:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66923",
    "user": "iandrus"
}
```

I have added `spkg-test` to run valgrind's test suite (which fails for me on OS X 10.6.7).

I created 2 suppression files sage.supp which is the same file as before and sage-liberal.supp which is enough to suppress all the errors caused by sage startup.  When testing you can set `MEMCHECK_FLAGS` to change the suppression file you use.  In #11035 I plan to patch sage-valgrind to be able to switch between the two easily.

The default for the moment is to use the same suppression file as before, so it should be 'safer'.



---

archive/issue_comments_066924.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-26T01:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66924",
    "user": "iandrus"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066925.json:
```json
{
    "body": "I changed the title to indicate the ticket now upgrades to 3.6.1 rather than 3.6.0.svn. Personally I think upgrading to svn snapshots is generally a bad idea, as those are less tested than official releases. But I know sometimes its not possible to use a stable release. \n\nDave",
    "created_at": "2011-04-27T21:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66925",
    "user": "drkirkby"
}
```

I changed the title to indicate the ticket now upgrades to 3.6.1 rather than 3.6.0.svn. Personally I think upgrading to svn snapshots is generally a bad idea, as those are less tested than official releases. But I know sometimes its not possible to use a stable release. 

Dave



---

archive/issue_comments_066926.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-25T21:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66926",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066927.json:
```json
{
    "body": "The package does not work for me (on `openSUSE 12.1 \"Asparagus\"`). It fails with\n\n```\nchecking for a supported OS... ok (linux-gnu)\nchecking for the kernel version... unsupported (3.1.0-1.2-desktop)\nconfigure: error: Valgrind works on kernels 2.4, 2.6\nerror configuring valgrind 3.6.1\n\nreal    0m2.260s\nuser    0m0.347s\nsys     0m0.382s\n************************************************************************\nError installing package valgrind-3.6.1\n************************************************************************\nPlease email sage-devel (http://groups.google.com/group/sage-devel)\nexplaining the problem and including the relevant part of the log file\n  /home/simon/SAGE/sage-4.8.alpha3/spkg/logs/valgrind-3.6.1.log\n```\n",
    "created_at": "2011-12-25T21:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66927",
    "user": "SimonKing"
}
```

The package does not work for me (on `openSUSE 12.1 "Asparagus"`). It fails with

```
checking for a supported OS... ok (linux-gnu)
checking for the kernel version... unsupported (3.1.0-1.2-desktop)
configure: error: Valgrind works on kernels 2.4, 2.6
error configuring valgrind 3.6.1

real    0m2.260s
user    0m0.347s
sys     0m0.382s
************************************************************************
Error installing package valgrind-3.6.1
************************************************************************
Please email sage-devel (http://groups.google.com/group/sage-devel)
explaining the problem and including the relevant part of the log file
  /home/simon/SAGE/sage-4.8.alpha3/spkg/logs/valgrind-3.6.1.log
```




---

archive/issue_comments_066928.json:
```json
{
    "body": "Yes, this was fixed in 4.7.0. (\"275278  valgrind does not build on Linux kernel 3.0.* due to silly\" in the changelog). So we apparently need a newer spkg now.",
    "created_at": "2011-12-25T21:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66928",
    "user": "kini"
}
```

Yes, this was fixed in 4.7.0. ("275278  valgrind does not build on Linux kernel 3.0.* due to silly" in the changelog). So we apparently need a newer spkg now.



---

archive/issue_comments_066929.json:
```json
{
    "body": "Er, sorry, I meant 3.7.0.",
    "created_at": "2011-12-25T21:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66929",
    "user": "kini"
}
```

Er, sorry, I meant 3.7.0.



---

archive/issue_comments_066930.json:
```json
{
    "body": "I created a new spkg from 3.7.0 which can be found at http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.spkg\n\nI would like to get this reviewed since the current valgrind package is at 3.3.1 and doesn't support OS X or 3.x linux kernels.  I ran some doctests under valgrind on my machine and things worked (well there were lots of leaks, but...).",
    "created_at": "2012-02-10T17:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66930",
    "user": "iandrus"
}
```

I created a new spkg from 3.7.0 which can be found at http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.spkg

I would like to get this reviewed since the current valgrind package is at 3.3.1 and doesn't support OS X or 3.x linux kernels.  I ran some doctests under valgrind on my machine and things worked (well there were lots of leaks, but...).



---

archive/issue_comments_066931.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-10T17:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66931",
    "user": "iandrus"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066932.json:
```json
{
    "body": "I guess that make should be replaced by $MAKE in both spkg-check and spkg-install.\n\nThe SAGE_LOCAL logic should also be added to spkg-check.\n\nSome message should be printed if tests fail.\n\nThe updated changelog in SPKG.txt is wrong (3.6.1 instead of 3.7.0).\n\nI guess the hg log could contain this ticket number at the beginning (#7766: ...)\n\nMoreover the spkg should be named .... .p0.spkg.\n\nOtherwise it looks fine.\n\nI'll test the package now.",
    "created_at": "2012-02-16T15:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66932",
    "user": "jpflori"
}
```

I guess that make should be replaced by $MAKE in both spkg-check and spkg-install.

The SAGE_LOCAL logic should also be added to spkg-check.

Some message should be printed if tests fail.

The updated changelog in SPKG.txt is wrong (3.6.1 instead of 3.7.0).

I guess the hg log could contain this ticket number at the beginning (#7766: ...)

Moreover the spkg should be named .... .p0.spkg.

Otherwise it looks fine.

I'll test the package now.



---

archive/issue_comments_066933.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-16T15:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66933",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066934.json:
```json
{
    "body": "It runs fine on my quite common amd64 debian system.",
    "created_at": "2012-02-16T15:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66934",
    "user": "jpflori"
}
```

It runs fine on my quite common amd64 debian system.



---

archive/issue_comments_066935.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-16T21:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66935",
    "user": "iandrus"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066936.json:
```json
{
    "body": "Replying to [comment:18 jpflori]:\n> I guess that make should be replaced by $MAKE in both spkg-check and spkg-install.\n\nDone.\n\n> The SAGE_LOCAL logic should also be added to spkg-check.\n\nIt probably doesn't need it since it will run after spkg-install succeeded, but I added it anyway since it's safer than way.  Is there a way to run the tests of an already installed package?\n\n> Some message should be printed if tests fail.\n\nDone.\n\n> The updated changelog in SPKG.txt is wrong (3.6.1 instead of 3.7.0).\n\nOops.\n\n> I guess the hg log could contain this ticket number at the beginning (#7766: ...)\n\nGood point.\n\n> Moreover the spkg should be named .... .p0.spkg.\n\nI thought I read that if there were no patches to upstream then we weren't supposed to put the `.p0` on it, but I changed it since I don't really know.\n\nThanks for taking the time to review this.",
    "created_at": "2012-02-16T21:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66936",
    "user": "iandrus"
}
```

Replying to [comment:18 jpflori]:
> I guess that make should be replaced by $MAKE in both spkg-check and spkg-install.

Done.

> The SAGE_LOCAL logic should also be added to spkg-check.

It probably doesn't need it since it will run after spkg-install succeeded, but I added it anyway since it's safer than way.  Is there a way to run the tests of an already installed package?

> Some message should be printed if tests fail.

Done.

> The updated changelog in SPKG.txt is wrong (3.6.1 instead of 3.7.0).

Oops.

> I guess the hg log could contain this ticket number at the beginning (#7766: ...)

Good point.

> Moreover the spkg should be named .... .p0.spkg.

I thought I read that if there were no patches to upstream then we weren't supposed to put the `.p0` on it, but I changed it since I don't really know.

Thanks for taking the time to review this.



---

archive/issue_comments_066937.json:
```json
{
    "body": "I forgot to say the updated spkg is at http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.p0.spkg .",
    "created_at": "2012-02-16T21:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66937",
    "user": "iandrus"
}
```

I forgot to say the updated spkg is at http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.p0.spkg .



---

archive/issue_comments_066938.json:
```json
{
    "body": "About the p0, the problem was that the directory inside the archive was named with a p0 but not the spkg itself so sage would not find it after decompression.\n\nSo removing the p0 from both might be a better choice :)\n\nFor the check I'm not aware of any way to do that without rebuilding the package but I might have missed something. But if the build dir is deleted after installation that might be impossible anyway.",
    "created_at": "2012-02-16T22:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66938",
    "user": "jpflori"
}
```

About the p0, the problem was that the directory inside the archive was named with a p0 but not the spkg itself so sage would not find it after decompression.

So removing the p0 from both might be a better choice :)

For the check I'm not aware of any way to do that without rebuilding the package but I might have missed something. But if the build dir is deleted after installation that might be impossible anyway.



---

archive/issue_comments_066939.json:
```json
{
    "body": "Replying to [comment:22 jpflori]:\n> About the p0, the problem was that the directory inside the archive was named with a p0 but not the spkg itself so sage would not find it after decompression.\n> \n> So removing the p0 from both might be a better choice :)\n\nOh I see now.  Let me know if you want me to change it.  I don't know how big of a deal having a `.p0` or not is.",
    "created_at": "2012-02-17T07:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66939",
    "user": "iandrus"
}
```

Replying to [comment:22 jpflori]:
> About the p0, the problem was that the directory inside the archive was named with a p0 but not the spkg itself so sage would not find it after decompression.
> 
> So removing the p0 from both might be a better choice :)

Oh I see now.  Let me know if you want me to change it.  I don't know how big of a deal having a `.p0` or not is.



---

archive/issue_comments_066940.json:
```json
{
    "body": "Could you just post the diff with the previous patch here, \"just for review\"?\n\nAfter that, I'll be completely happy with the ticket.",
    "created_at": "2012-02-24T11:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66940",
    "user": "jpflori"
}
```

Could you just post the diff with the previous patch here, "just for review"?

After that, I'll be completely happy with the ticket.



---

archive/issue_comments_066941.json:
```json
{
    "body": "Let's also remove the p0, while we are at it.",
    "created_at": "2012-02-24T11:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66941",
    "user": "jpflori"
}
```

Let's also remove the p0, while we are at it.



---

archive/issue_comments_066942.json:
```json
{
    "body": "I've made the mentioned changes and some minor other changes. I've also updated the descr/license in the SPKG file.\n\nThe updated spkg is at [http://perso.telecom-paristech/~flori/sage/valgrind-3.7.0.spkg](http://perso.telecom-paristech/%7Eflori/sage/valgrind-3.7.0.spkg) \n\nIvan: If you don't mind, it may be a good idea to add yourself as a maintainer?\n\nIf you do agree, or if you don\"t as wel, I'll put this as positive review.",
    "created_at": "2012-02-24T12:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66942",
    "user": "jpflori"
}
```

I've made the mentioned changes and some minor other changes. I've also updated the descr/license in the SPKG file.

The updated spkg is at [http://perso.telecom-paristech/~flori/sage/valgrind-3.7.0.spkg](http://perso.telecom-paristech/%7Eflori/sage/valgrind-3.7.0.spkg) 

Ivan: If you don't mind, it may be a good idea to add yourself as a maintainer?

If you do agree, or if you don"t as wel, I'll put this as positive review.



---

archive/issue_comments_066943.json:
```json
{
    "body": "Replying to [comment:26 jpflori]:\n> I've made the mentioned changes and some minor other changes. I've also updated the descr/license in the SPKG file.\n> \n> The updated spkg is at [http://perso.telecom-paristech/~flori/sage/valgrind-3.7.0.spkg](http://perso.telecom-paristech/%7Eflori/sage/valgrind-3.7.0.spkg) \n\nFWIW I had to add `.fr` to the server to get the spkg.\n\n> Ivan: If you don't mind, it may be a good idea to add yourself as a maintainer?\n\nYeah, I can be a maintainer.  I took your spkg and added myself as maintainer in SPKG.txt.  New version is at \n\nhttp://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.spkg\n\nYour patches look good BTW.\n\n> If you do agree, or if you don\"t as wel, I'll put this as positive review.\n\nExcellent.  Thanks again.",
    "created_at": "2012-02-24T15:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66943",
    "user": "iandrus"
}
```

Replying to [comment:26 jpflori]:
> I've made the mentioned changes and some minor other changes. I've also updated the descr/license in the SPKG file.
> 
> The updated spkg is at [http://perso.telecom-paristech/~flori/sage/valgrind-3.7.0.spkg](http://perso.telecom-paristech/%7Eflori/sage/valgrind-3.7.0.spkg) 

FWIW I had to add `.fr` to the server to get the spkg.

> Ivan: If you don't mind, it may be a good idea to add yourself as a maintainer?

Yeah, I can be a maintainer.  I took your spkg and added myself as maintainer in SPKG.txt.  New version is at 

http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.spkg

Your patches look good BTW.

> If you do agree, or if you don"t as wel, I'll put this as positive review.

Excellent.  Thanks again.



---

archive/issue_comments_066944.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-24T16:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66944",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066945.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-25T16:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66945",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066946.json:
```json
{
    "body": "In `SPKG.txt`, `valgrind_3.7.0` should be `valgrind-3.7.0`",
    "created_at": "2012-02-25T16:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66946",
    "user": "jdemeyer"
}
```

In `SPKG.txt`, `valgrind_3.7.0` should be `valgrind-3.7.0`



---

archive/issue_comments_066947.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-25T18:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66947",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066948.json:
```json
{
    "body": "I corrected the last version name as well as all the old ones.\n\nPackage available at http://perso.telecom-paristech.fr/~flori/sage/valgrind-3.7.0.spkg",
    "created_at": "2012-02-25T18:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66948",
    "user": "jpflori"
}
```

I corrected the last version name as well as all the old ones.

Package available at http://perso.telecom-paristech.fr/~flori/sage/valgrind-3.7.0.spkg



---

archive/issue_comments_066949.json:
```json
{
    "body": "Attachment [trac_7666_spkg.patch](tarball://root/attachments/some-uuid/ticket7766/trac_7666_spkg.patch) by jpflori created at 2012-02-25 18:31:49\n\nspkg diff, for review only",
    "created_at": "2012-02-25T18:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66949",
    "user": "jpflori"
}
```

Attachment [trac_7666_spkg.patch](tarball://root/attachments/some-uuid/ticket7766/trac_7666_spkg.patch) by jpflori created at 2012-02-25 18:31:49

spkg diff, for review only



---

archive/issue_comments_066950.json:
```json
{
    "body": "**Update the ticket description if you post a new package**",
    "created_at": "2012-02-28T12:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66950",
    "user": "jdemeyer"
}
```

**Update the ticket description if you post a new package**



---

archive/issue_comments_066951.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-28T12:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66951",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-03T14:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7766#issuecomment-66952",
    "user": "jdemeyer"
}
```

Resolution: fixed
