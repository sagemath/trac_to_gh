# Issue 8514: Optional database_gap-4.4.12 fails to install on Solaris 10 SPARC

Issue created by migration from https://trac.sagemath.org/ticket/8514

Original creator: drkirkby

Original creation time: 2010-03-13 01:13:49

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


---

Comment by dimpase created at 2010-03-15 08:36:56

same spkg-install problem as in #8520


---

Comment by dimpase created at 2010-03-15 12:14:58

Replying to [comment:1 drkirkby]:

please try 

http://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p1.spkg


---

Comment by dimpase created at 2010-03-15 12:14:58

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-03-16 00:21:28

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

Comment by drkirkby created at 2010-03-16 00:21:28

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-03-16 00:23:05

Since the original was called database_gap-4.4.12, the new one should be database_gap-4.4.12.p0 and extract to a directory database_gap-4.4.12.p0. (This is called p1. Convention is we start patch levels at 0). 

Dave


---

Comment by dimpase created at 2010-03-16 12:35:27

Replying to [comment:6 drkirkby]:
> Since the original was called database_gap-4.4.12, the new one should be database_gap-4.4.12.p0 and extract to a directory database_gap-4.4.12.p0. (This is called p1. Convention is we start patch levels at 0). 
> 
 
OK, sorry for this mess.

Here is the numbering done right. I tested this on t2 and elsewhere

 http://sage.math.washington.edu/home/dima/packages/database_gap-4.4.12.p0.spkg


---

Comment by dimpase created at 2010-03-16 12:35:27

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2010-03-25 12:44:16

Hi David, 
would you mind having a look at this?
Thanks,
Dima


---

Comment by wdj created at 2010-03-26 11:15:26

Replying to [comment:8 dimpase]:
> Hi David, 
> would you mind having a look at this?
> Thanks,
> Dima

I am happy to test this but I don't have access to a sparc. It seems David Kirkby is saying that it works on a sparc machine but the download+install was a problem?

Anyway, I donloaded it first the installed using sage -i with no problems. Tested that the database of small groups was loaded into the GAP workspace Sage uses and that IdGroup works as expected.

Positive review from me.


---

Comment by drkirkby created at 2010-03-26 13:01:39

I'll take a look in a few hours - just about to start a chess game!

dave


---

Comment by drkirkby created at 2010-03-28 13:19:58

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-03-28 13:19:58

Sorry for the delay in replying - I got distracted after the chess game, which I rather annoying only drew against a much weaker opponent. 

Although I can't test the packages, due to a lack of knowledge of gap, it looks fine to me. 

Positive review.


---

Comment by jhpalmieri created at 2010-04-20 22:51:04

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-20 22:51:04

Merged 2010/04/20.
