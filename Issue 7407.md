# Issue 7407: Fix building of binary distribution so it works on Solaris. Make name of .tar.gz file sensible too.

archive/issues_007407.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby georgsweber mvngu\n\nKeywords: solairs GNUism cp\n\nIn version 4.2 of Sage, an attempt to build a binary distribution failed on Solaris, due to the use of a non-portable '-a' option to the 'cp' command, which is not defined by the POSIX specification of Unix. \n\nThe only options that should be used are given here. \n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/cp.html\n\nAlso, the file name created seems a bit silly. After typing:\n\n~/sage-4.2$ ./sage -bdist 4.2-Solaris-10-SPARC\n\na useless output file of about 4 KB in size named 'sage-4.2-Solaris-10-SPARC-sun4u-SunOS.tar.gz' was created. I do not think it is sensible to have 'sun4u' in the name, since it would run on sun4v machines too. Also, since Sun's operating system is known as 'Solaris' far more than 'SunOS', the use of 'SunOS' in the name is not necessary. I assume the 'sun4u' and 'SunOS' are probably taken from the output of the 'uname' command. \n\nHere is the result of trying to build a binary distribution on a Sun Netra T1, running the first release of Solaris 10. Had this not failed, the resulting binary should have worked on any Solaris 10 sun4u or sun4v (i.e the CoolThreads machines like the Sun T5240 't2'). Building a Sage binary for Solaris 10 on 't2' would not be sensible, as the resulting binary might not run on earlier release of Solaris 10. The T5240 is not supported on the first release of Solaris 10, so it would be impossible to downgrade the operating system if one wanted to. For building this, I specifically used an old version of Solaris. \n\n\n```\ndrkirkby@kestrel:~/sage-4.2$ ./sage -bdist 4.2-Solaris-10-SPARC\nSage works!\nCopying files over to tmp directory\ncp: illegal option -- a\nUsage: cp [-f] [-i] [-p] [-@] f1 f2\n       cp [-f] [-i] [-p] [-@] f1 ... fn d1\n       cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-@] d1 ... dn-1 dn\nCopying Sage library over\ncp: illegal option -- a\nUsage: cp [-f] [-i] [-p] [-@] f1 f2\n       cp [-f] [-i] [-p] [-@] f1 ... fn d1\n       cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-@] d1 ... dn-1 dn\n/export/home/drkirkby/sage-4.2/local/bin/sage-bdist: line 60: cd: sage: No such file or directory\n/export/home/drkirkby/sage-4.2/local/bin/sage-bdist: line 63: cd: /export/home/drkirkby/sage-4.2/tmp/sage-4.2-Solaris-10-SPARC-sun4u-SunOS/local/lib/python/site-packages: No such file or directory\nMaking empty spkg's\ncp: illegal option -- a\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7407\n\n",
    "created_at": "2009-11-07T04:49:27Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Fix building of binary distribution so it works on Solaris. Make name of .tar.gz file sensible too.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7407",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/7407





---

archive/issue_comments_062212.json:
```json
{
    "body": "I modified the title and description slightly, since with second thoughts, perhaps its best to leave the name of the file unchaged. \n\nDave",
    "created_at": "2009-12-09T15:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62212",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I modified the title and description slightly, since with second thoughts, perhaps its best to leave the name of the file unchaged. 

Dave



---

archive/issue_comments_062213.json:
```json
{
    "body": "It seems to work on t2.math to use `cp -RPp`.  There are some warnings, but the resulting tar.gz file seems to unpack okay and producing a working version of Sage.\n\n```\n-R  \n  Copy file hierarchies.\n-P\n  Take actions on any symbolic link specified as a source_file operand or any symbolic link \n  encountered during traversal of a file hierarchy.\n-p\n  Duplicate the following characteristics of each source file in the corresponding destination\n  file: The time of last data modification and time of last access. If this duplication fails for any \n  reason, cp shall write a diagnostic message to standard error.\n\n  The user ID and group ID. If this duplication fails for any reason, it is unspecified whether cp \n  writes a diagnostic message to standard error.\n\n  The file permission bits and the S_ISUID and S_ISGID bits. Other, implementation-defined, bits \n  may be duplicated as well. If this duplication fails for any reason, cp shall write a diagnostic \n  message to standard error.\n\n  If the user ID or the group ID cannot be duplicated, the file permission bits S_ISUID and \n  S_ISGID shall be cleared. If these bits are present in the source file but are not duplicated \n  in the destination file, it is unspecified whether cp writes a diagnostic message to standard error.\n\n  The order in which the preceding characteristics are duplicated is unspecified. The dest_file \n  shall not be deleted if these characteristics cannot be preserved.\n```\n\nOpinions?",
    "created_at": "2010-04-26T17:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62213",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_062214.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-09T20:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62214",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062215.json:
```json
{
    "body": "Here's a patch, changing the options to -pPR for all platforms.  This needs testing on a variety of platforms.  It seems to work for me on a Mac and on sage.math.  Something similar worked for me on t2 before, and I'll try this patch with t2 when I've built sage there.",
    "created_at": "2010-06-09T20:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62215",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch, changing the options to -pPR for all platforms.  This needs testing on a variety of platforms.  It seems to work for me on a Mac and on sage.math.  Something similar worked for me on t2 before, and I'll try this patch with t2 when I've built sage there.



---

archive/issue_comments_062216.json:
```json
{
    "body": "Attachment [trac_7407-bdist-scripts.patch](tarball://root/attachments/some-uuid/ticket7407/trac_7407-bdist-scripts.patch) by @jhpalmieri created at 2010-06-09 20:44:43\n\nscripts repo",
    "created_at": "2010-06-09T20:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62216",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7407-bdist-scripts.patch](tarball://root/attachments/some-uuid/ticket7407/trac_7407-bdist-scripts.patch) by @jhpalmieri created at 2010-06-09 20:44:43

scripts repo



---

archive/issue_comments_062217.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-06-09T20:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62217",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_062218.json:
```json
{
    "body": "When you say it works, is the binary distribution a sensible size? I've found ways before, which meant that libraries were copied rather than links made, which swelled the size of the binary considerably. \n\nDave",
    "created_at": "2010-06-09T20:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62218",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

When you say it works, is the binary distribution a sensible size? I've found ways before, which meant that libraries were copied rather than links made, which swelled the size of the binary considerably. 

Dave



---

archive/issue_comments_062219.json:
```json
{
    "body": "When I said that \"something similar worked for me on t2 before\", you can see the results on sage.math in /home/release/sage-4.4:\n\n```\n  /home/release/sage-4.4:\n  total used in directory 1354258 available 1248959488\n  drwxr-xr-x  3 palmieri palmieri         9 Apr 25 19:45 .\n  drwxrwxrwx 19 root     root            21 Jun  7 00:36 ..\n  drwxr-xr-x  3 palmieri palmieri         8 Apr 24 20:19 sage-4.4\n  -rw-r--r--  1 palmieri palmieri 544636534 Apr 25 07:31 sage-4.4-sage.math.washington.edu-x86_64-Linux.tar.gz\n  -rw-r--r--  1 palmieri palmieri        88 Apr 25 07:38 sage-4.4-sage.math.washington.edu-x86_64-Linux.tar.gz.md5\n  -rw-r--r--  1 palmieri palmieri 530396009 Apr 25 19:45 sage-4.4-t2.math.washington.edu-sun4v-SunOS.tar.gz\n  -rw-r--r--  1 palmieri palmieri        85 Apr 25 19:45 sage-4.4-t2.math.washington.edu-sun4v-SunOS.tar.gz.md5\n  -rw-r--r--  1 palmieri palmieri 311080960 Apr 24 20:19 sage-4.4.tar\n  -rw-r--r--  1 palmieri palmieri     17257 Apr 25 09:07 sage-4.4.txt\n```\n\nSo the binary for t2 is about the same as the one for sage.math (which was produced using the old method).\n\nWhen I used the new method on sage.math today, I got a binary more or less the same size as with the old method.  Same on the mac: the \"dmg\" file with the new method is about the same size:\n\n```\n  -rw-r--r--@  1 palmieri  palmieri  420294832 May 20 08:23 sage-4.4.2-OSX-64bit-10.6-i386-Darwin.dmg\n  -rw-r--r--@  1 palmieri  admin     417800348 Jun  9 12:03 sage-TESTING-i386-Darwin.dmg\n```\n\n(The \"TESTING\" version was based on 4.4.3.alpha3, not 4.4.2, for what that's worth.)\n\nBut these are issues which should also be examined by reviewers.",
    "created_at": "2010-06-09T21:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62219",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_062220.json:
```json
{
    "body": "It's 1150 pm here in the UK, so I am going to bed soon. \n\nBut since making a binary takes ages on my Sun Blade 1000, I'll apply the patch now and see what I have in the morning. I'll comment then. \n\nThis is great news if you have fixed this. It's a real pain this issue. The only \"solution\" I found before was to use the GNU version of 'cp'. That was a pain, as GNU 'cp' is not included as part of Solaris (unlike GNU make, GNU tar, gcc etc). So one has to build GNU coreutils just to get a version of 'cp' that would work. \n\n\nDave",
    "created_at": "2010-06-09T22:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62220",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It's 1150 pm here in the UK, so I am going to bed soon. 

But since making a binary takes ages on my Sun Blade 1000, I'll apply the patch now and see what I have in the morning. I'll comment then. 

This is great news if you have fixed this. It's a real pain this issue. The only "solution" I found before was to use the GNU version of 'cp'. That was a pain, as GNU 'cp' is not included as part of Solaris (unlike GNU make, GNU tar, gcc etc). So one has to build GNU coreutils just to get a version of 'cp' that would work. 


Dave



---

archive/issue_comments_062221.json:
```json
{
    "body": "It applied cleanly:\n\n\n```\ndrkirkby@redstart:~/32/sage-4.4.3$ time ./sage -bdist Solaris10_release_3_05_for_sun4u_or_sun4v\nSage works!\nCopying files over to tmp directory\n```\n\n\ntime for bed!",
    "created_at": "2010-06-09T23:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62221",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It applied cleanly:


```
drkirkby@redstart:~/32/sage-4.4.3$ time ./sage -bdist Solaris10_release_3_05_for_sun4u_or_sun4v
Sage works!
Copying files over to tmp directory
```


time for bed!



---

archive/issue_comments_062222.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-11T01:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62222",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062223.json:
```json
{
    "body": "This works well. The resulting binaries work fine (tested on both Solaris and Linux). \n\nPositive review.",
    "created_at": "2010-06-11T01:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62223",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This works well. The resulting binaries work fine (tested on both Solaris and Linux). 

Positive review.



---

archive/issue_comments_062224.json:
```json
{
    "body": "Replying to [comment:10 drkirkby]:\n> This works well. The resulting binaries work fine (tested on both Solaris and Linux). \n\nGreat.  Just to confirm: was the linux system (or systems) using the Gnu version of cp, so that we have evidence it works with that version?",
    "created_at": "2010-06-11T05:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62224",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:10 drkirkby]:
> This works well. The resulting binaries work fine (tested on both Solaris and Linux). 

Great.  Just to confirm: was the linux system (or systems) using the Gnu version of cp, so that we have evidence it works with that version?



---

archive/issue_comments_062225.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-11T20:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7407#issuecomment-62225",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007632.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-06-11T20:51:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7407",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7407#event-7632"
}
```
