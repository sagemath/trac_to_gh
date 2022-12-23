# Issue 7407: Fix building of binary distribution so it works on Solaris. Make name of .tar.gz file sensible too.

Issue created by migration from https://trac.sagemath.org/ticket/7407

Original creator: drkirkby

Original creation time: 2009-11-07 04:49:27

Assignee: tbd

CC:  drkirkby georgsweber mvngu

Keywords: solairs GNUism cp

In version 4.2 of Sage, an attempt to build a binary distribution failed on Solaris, due to the use of a non-portable '-a' option to the 'cp' command, which is not defined by the POSIX specification of Unix. 

The only options that should be used are given here. 

http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html

Also, the file name created seems a bit silly. After typing:

~/sage-4.2$ ./sage -bdist 4.2-Solaris-10-SPARC

a useless output file of about 4 KB in size named 'sage-4.2-Solaris-10-SPARC-sun4u-SunOS.tar.gz' was created. I do not think it is sensible to have 'sun4u' in the name, since it would run on sun4v machines too. Also, since Sun's operating system is known as 'Solaris' far more than 'SunOS', the use of 'SunOS' in the name is not necessary. I assume the 'sun4u' and 'SunOS' are probably taken from the output of the 'uname' command. 

Here is the result of trying to build a binary distribution on a Sun Netra T1, running the first release of Solaris 10. Had this not failed, the resulting binary should have worked on any Solaris 10 sun4u or sun4v (i.e the CoolThreads machines like the Sun T5240 't2'). Building a Sage binary for Solaris 10 on 't2' would not be sensible, as the resulting binary might not run on earlier release of Solaris 10. The T5240 is not supported on the first release of Solaris 10, so it would be impossible to downgrade the operating system if one wanted to. For building this, I specifically used an old version of Solaris. 


```
drkirkby@kestrel:~/sage-4.2$ ./sage -bdist 4.2-Solaris-10-SPARC
Sage works!
Copying files over to tmp directory
cp: illegal option -- a
Usage: cp [-f] [-i] [-p] [-@] f1 f2
       cp [-f] [-i] [-p] [-@] f1 ... fn d1
       cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-@] d1 ... dn-1 dn
Copying Sage library over
cp: illegal option -- a
Usage: cp [-f] [-i] [-p] [-@] f1 f2
       cp [-f] [-i] [-p] [-@] f1 ... fn d1
       cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-@] d1 ... dn-1 dn
/export/home/drkirkby/sage-4.2/local/bin/sage-bdist: line 60: cd: sage: No such file or directory
/export/home/drkirkby/sage-4.2/local/bin/sage-bdist: line 63: cd: /export/home/drkirkby/sage-4.2/tmp/sage-4.2-Solaris-10-SPARC-sun4u-SunOS/local/lib/python/site-packages: No such file or directory
Making empty spkg's
cp: illegal option -- a
```



---

Comment by drkirkby created at 2009-12-09 15:43:32

I modified the title and description slightly, since with second thoughts, perhaps its best to leave the name of the file unchaged. 

Dave


---

Comment by jhpalmieri created at 2010-04-26 17:13:33

It seems to work on t2.math to use `cp -RPp`.  There are some warnings, but the resulting tar.gz file seems to unpack okay and producing a working version of Sage.

```
-R  
  Copy file hierarchies.
-P
  Take actions on any symbolic link specified as a source_file operand or any symbolic link 
  encountered during traversal of a file hierarchy.
-p
  Duplicate the following characteristics of each source file in the corresponding destination
  file: The time of last data modification and time of last access. If this duplication fails for any 
  reason, cp shall write a diagnostic message to standard error.

  The user ID and group ID. If this duplication fails for any reason, it is unspecified whether cp 
  writes a diagnostic message to standard error.

  The file permission bits and the S_ISUID and S_ISGID bits. Other, implementation-defined, bits 
  may be duplicated as well. If this duplication fails for any reason, cp shall write a diagnostic 
  message to standard error.

  If the user ID or the group ID cannot be duplicated, the file permission bits S_ISUID and 
  S_ISGID shall be cleared. If these bits are present in the source file but are not duplicated 
  in the destination file, it is unspecified whether cp writes a diagnostic message to standard error.

  The order in which the preceding characteristics are duplicated is unspecified. The dest_file 
  shall not be deleted if these characteristics cannot be preserved.
```

Opinions?


---

Comment by jhpalmieri created at 2010-06-09 20:44:27

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-06-09 20:44:27

Here's a patch, changing the options to -pPR for all platforms.  This needs testing on a variety of platforms.  It seems to work for me on a Mac and on sage.math.  Something similar worked for me on t2 before, and I'll try this patch with t2 when I've built sage there.


---

Attachment

scripts repo


---

Comment by drkirkby created at 2010-06-09 20:47:22

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2010-06-09 20:47:22

When you say it works, is the binary distribution a sensible size? I've found ways before, which meant that libraries were copied rather than links made, which swelled the size of the binary considerably. 

Dave


---

Comment by jhpalmieri created at 2010-06-09 21:11:34

When I said that "something similar worked for me on t2 before", you can see the results on sage.math in /home/release/sage-4.4:

```
  /home/release/sage-4.4:
  total used in directory 1354258 available 1248959488
  drwxr-xr-x  3 palmieri palmieri         9 Apr 25 19:45 .
  drwxrwxrwx 19 root     root            21 Jun  7 00:36 ..
  drwxr-xr-x  3 palmieri palmieri         8 Apr 24 20:19 sage-4.4
  -rw-r--r--  1 palmieri palmieri 544636534 Apr 25 07:31 sage-4.4-sage.math.washington.edu-x86_64-Linux.tar.gz
  -rw-r--r--  1 palmieri palmieri        88 Apr 25 07:38 sage-4.4-sage.math.washington.edu-x86_64-Linux.tar.gz.md5
  -rw-r--r--  1 palmieri palmieri 530396009 Apr 25 19:45 sage-4.4-t2.math.washington.edu-sun4v-SunOS.tar.gz
  -rw-r--r--  1 palmieri palmieri        85 Apr 25 19:45 sage-4.4-t2.math.washington.edu-sun4v-SunOS.tar.gz.md5
  -rw-r--r--  1 palmieri palmieri 311080960 Apr 24 20:19 sage-4.4.tar
  -rw-r--r--  1 palmieri palmieri     17257 Apr 25 09:07 sage-4.4.txt
```

So the binary for t2 is about the same as the one for sage.math (which was produced using the old method).

When I used the new method on sage.math today, I got a binary more or less the same size as with the old method.  Same on the mac: the "dmg" file with the new method is about the same size:

```
  -rw-r--r--@  1 palmieri  palmieri  420294832 May 20 08:23 sage-4.4.2-OSX-64bit-10.6-i386-Darwin.dmg
  -rw-r--r--@  1 palmieri  admin     417800348 Jun  9 12:03 sage-TESTING-i386-Darwin.dmg
```

(The "TESTING" version was based on 4.4.3.alpha3, not 4.4.2, for what that's worth.)

But these are issues which should also be examined by reviewers.


---

Comment by drkirkby created at 2010-06-09 22:50:29

It's 1150 pm here in the UK, so I am going to bed soon. 

But since making a binary takes ages on my Sun Blade 1000, I'll apply the patch now and see what I have in the morning. I'll comment then. 

This is great news if you have fixed this. It's a real pain this issue. The only "solution" I found before was to use the GNU version of 'cp'. That was a pain, as GNU 'cp' is not included as part of Solaris (unlike GNU make, GNU tar, gcc etc). So one has to build GNU coreutils just to get a version of 'cp' that would work. 


Dave


---

Comment by drkirkby created at 2010-06-09 23:01:05

It applied cleanly:


```
drkirkby@redstart:~/32/sage-4.4.3$ time ./sage -bdist Solaris10_release_3_05_for_sun4u_or_sun4v
Sage works!
Copying files over to tmp directory
```


time for bed!


---

Comment by drkirkby created at 2010-06-11 01:12:50

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-11 01:12:50

This works well. The resulting binaries work fine (tested on both Solaris and Linux). 

Positive review.


---

Comment by jhpalmieri created at 2010-06-11 05:36:04

Replying to [comment:10 drkirkby]:
> This works well. The resulting binaries work fine (tested on both Solaris and Linux). 

Great.  Just to confirm: was the linux system (or systems) using the Gnu version of cp, so that we have evidence it works with that version?


---

Comment by mhansen created at 2010-06-11 20:51:31

Resolution: fixed
