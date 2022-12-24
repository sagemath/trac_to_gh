# Issue 7781: Update prereq to version 0.6

archive/issues_007781.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @mwhansen georgsweber mvngu\n\nKeywords: gcc AIX HP-UX IRIX Tru64 Solaris\n\nThis is a further update of the code which checks the prerequisites for Sage are OK. Previous updates were #7021 and #7352. \n\n == Changes in files ==\n\n**Changes to configure.ac (This gets included in prereq-0.6.tar)**\n\n* Exit for a gcc 3.4 series compiler, unless the variable 'SAGE_USE_OLD_GCC' is set to something non-empty. This was desirable, as the only compiler shipped with Solaris is 3.4.3, which is too old. As in prereq 0.4 and 0.5, the Sage build exits with gcc < 3.4.0 (as it's too old) and with gcc 4.0.0 (as it's too buggy). \n\n**Changes to prereq-0.6-install**\n\n* Exit on Solaris if the version of 'make' is not the GNU one. It was my intension this was done for both 'tar' and 'make' in prereq 0.5, but I'd overlooked to put the number '1' on one of the exit statements, so the build did not exit for Sun's 'make'.\n* Exit on Solaris 2.6, 7, 8 and 9 unless SAGE_PORT is set to something non-empty. This seems logical, as nobody is testing Sage on the older Solaris releases. It's probably worth testing Sage on Solaris 8 and 9, but not 2.6 or 7, as they are too old to worry about. \n* Test for the GNU versions of 'make' and 'tar' on AIX, HP-UX, IRIX and Tru64 - this was already done on Solaris. As I'm not so sure where the GNU tools will be found on AIX, HP-UX, IRIX or Tru64, so the error message is not as informative as on Solaris, where I know the systems much better. \n* Provides links to pages on the Sage Wiki for Solaris (http://wiki.sagemath.org/solaris) and HP-UX (http://wiki.sagemath.org/HP-UX), which are printed on those platforms if there are any issues detected (Generally that means if 'SAGE_PORT' is needed for the build to continue). There are no Wiki pages for AIX, Tru64 or IRIX, and I somewhat doubt I will create any for Tru64 or IRIX, but I might for AIX. \n* Change the comment about using VMWare to VirtualBox, as that is the preferred system for Sage now.\n* Mention a port to HP-UX does not look particularly difficult, as it might encourage some developers. It actually looks to be relatively easy, judging by the number of packages that build OK on HP-UX. \n\nUpdated versions of prereq-0.6-install and prereq-0.6.tar are provided in the directory below. prereq-0.6-install must be put into Sage with execute permissions. \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/\n\n == How to test these changes ==\n* Copy the files prereq-0.6.tar & prereq-0.6-install to $SAGE_ROOT/spkg/base/ \n* Ensure prereq-0.6-install has execute permissions. \n* Remove spkg/installed/prerequ-0.5\n* Type 'make' \n\nAnyone wishing to test on HP-UX is welcome to have an account on my own machine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7781\n\n",
    "created_at": "2009-12-29T05:38:55Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Update prereq to version 0.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7781",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @mwhansen georgsweber mvngu

Keywords: gcc AIX HP-UX IRIX Tru64 Solaris

This is a further update of the code which checks the prerequisites for Sage are OK. Previous updates were #7021 and #7352. 

 == Changes in files ==

**Changes to configure.ac (This gets included in prereq-0.6.tar)**

* Exit for a gcc 3.4 series compiler, unless the variable 'SAGE_USE_OLD_GCC' is set to something non-empty. This was desirable, as the only compiler shipped with Solaris is 3.4.3, which is too old. As in prereq 0.4 and 0.5, the Sage build exits with gcc < 3.4.0 (as it's too old) and with gcc 4.0.0 (as it's too buggy). 

**Changes to prereq-0.6-install**

* Exit on Solaris if the version of 'make' is not the GNU one. It was my intension this was done for both 'tar' and 'make' in prereq 0.5, but I'd overlooked to put the number '1' on one of the exit statements, so the build did not exit for Sun's 'make'.
* Exit on Solaris 2.6, 7, 8 and 9 unless SAGE_PORT is set to something non-empty. This seems logical, as nobody is testing Sage on the older Solaris releases. It's probably worth testing Sage on Solaris 8 and 9, but not 2.6 or 7, as they are too old to worry about. 
* Test for the GNU versions of 'make' and 'tar' on AIX, HP-UX, IRIX and Tru64 - this was already done on Solaris. As I'm not so sure where the GNU tools will be found on AIX, HP-UX, IRIX or Tru64, so the error message is not as informative as on Solaris, where I know the systems much better. 
* Provides links to pages on the Sage Wiki for Solaris (http://wiki.sagemath.org/solaris) and HP-UX (http://wiki.sagemath.org/HP-UX), which are printed on those platforms if there are any issues detected (Generally that means if 'SAGE_PORT' is needed for the build to continue). There are no Wiki pages for AIX, Tru64 or IRIX, and I somewhat doubt I will create any for Tru64 or IRIX, but I might for AIX. 
* Change the comment about using VMWare to VirtualBox, as that is the preferred system for Sage now.
* Mention a port to HP-UX does not look particularly difficult, as it might encourage some developers. It actually looks to be relatively easy, judging by the number of packages that build OK on HP-UX. 

Updated versions of prereq-0.6-install and prereq-0.6.tar are provided in the directory below. prereq-0.6-install must be put into Sage with execute permissions. 

http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/

 == How to test these changes ==
* Copy the files prereq-0.6.tar & prereq-0.6-install to $SAGE_ROOT/spkg/base/ 
* Ensure prereq-0.6-install has execute permissions. 
* Remove spkg/installed/prerequ-0.5
* Type 'make' 

Anyone wishing to test on HP-UX is welcome to have an account on my own machine.

Issue created by migration from https://trac.sagemath.org/ticket/7781





---

archive/issue_comments_067087.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-29T05:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67087",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067088.json:
```json
{
    "body": "Attachment [testcc.sh](tarball://root/attachments/some-uuid/ticket7781/testcc.sh) by drkirkby created at 2009-12-31 20:35:16\n\nWith correected comment about number of command line arguments.",
    "created_at": "2009-12-31T20:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67088",
    "user": "drkirkby"
}
```

Attachment [testcc.sh](tarball://root/attachments/some-uuid/ticket7781/testcc.sh) by drkirkby created at 2009-12-31 20:35:16

With correected comment about number of command line arguments.



---

archive/issue_comments_067089.json:
```json
{
    "body": "Ignore testcc.sh - I attached it to the wrong ticket! \n\nDave",
    "created_at": "2009-12-31T20:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67089",
    "user": "drkirkby"
}
```

Ignore testcc.sh - I attached it to the wrong ticket! 

Dave



---

archive/issue_comments_067090.json:
```json
{
    "body": "In the file `prereq-0.6-install`: For portability, line 151\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n```\n\ncould be replaced with\n\n```\nif [ `uname` = \"Darwin\" ] && [ \"$SAGE64\" = \"yes\" ]; then\n```\n\nFrom line 356 onward, the following section appears twice:\n\n```\nif [ `uname` = \"HP-UX\" ] ||  [ `uname` = \"AIX\" ] ||   [ `uname` = \"Tru64\" ] ; then\n   if [ -z \"`tar --version 2>&1 | grep GNU`\" ] ; then\n       echo \"\"\n       echo \"You must use the GNU version of tar on `uname` Please\"\n       echo \"ensure that a GNU version of tar is first in your path\"\n       exit 1\n   fi\nfi\n\nif [ `uname` = \"IRIX\" ] ||  [ `uname` = \"IRIX64\" ] ; then\n   if [ -z \"`tar --version 2>&1 | grep GNU`\" ] ; then\n       echo \"\"\n       echo \"You must use the GNU version of tar on IRIX. Please\"\n       echo \"ensure that a GNU version of tar is first in your path\"\n       exit 1\n   fi\nfi\n```\n",
    "created_at": "2010-01-02T12:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67090",
    "user": "mvngu"
}
```

In the file `prereq-0.6-install`: For portability, line 151

```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
```

could be replaced with

```
if [ `uname` = "Darwin" ] && [ "$SAGE64" = "yes" ]; then
```

From line 356 onward, the following section appears twice:

```
if [ `uname` = "HP-UX" ] ||  [ `uname` = "AIX" ] ||   [ `uname` = "Tru64" ] ; then
   if [ -z "`tar --version 2>&1 | grep GNU`" ] ; then
       echo ""
       echo "You must use the GNU version of tar on `uname` Please"
       echo "ensure that a GNU version of tar is first in your path"
       exit 1
   fi
fi

if [ `uname` = "IRIX" ] ||  [ `uname` = "IRIX64" ] ; then
   if [ -z "`tar --version 2>&1 | grep GNU`" ] ; then
       echo ""
       echo "You must use the GNU version of tar on IRIX. Please"
       echo "ensure that a GNU version of tar is first in your path"
       exit 1
   fi
fi
```




---

archive/issue_comments_067091.json:
```json
{
    "body": "Thank you for your comments. \n\n* I take your first point. It will be updated. \n* The second point is of course true, but from what I have read, it is unwise to have more than 4 tests, as some shell implementations do not handle such cases well. However, the test for 'tar' is performed twice there, which can be simplified somewhat\n\nI'll make those changes. \n\nDave",
    "created_at": "2010-01-02T17:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67091",
    "user": "drkirkby"
}
```

Thank you for your comments. 

* I take your first point. It will be updated. 
* The second point is of course true, but from what I have read, it is unwise to have more than 4 tests, as some shell implementations do not handle such cases well. However, the test for 'tar' is performed twice there, which can be simplified somewhat

I'll make those changes. 

Dave



---

archive/issue_comments_067092.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-02T17:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67092",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067093.json:
```json
{
    "body": "I made those changes, and a few more where the tests could be made sightly more robust. They probably make no practical difference, but a good habit to get into. \n\ndave",
    "created_at": "2010-01-02T21:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67093",
    "user": "drkirkby"
}
```

I made those changes, and a few more where the tests could be made sightly more robust. They probably make no practical difference, but a good habit to get into. 

dave



---

archive/issue_comments_067094.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-03T22:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67094",
    "user": "drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067095.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-05T04:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67095",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067096.json:
```json
{
    "body": "As of Sage 4.3, some files are not propertly under revision control:\n\n```\n[mvngu@boxen base]$ pwd\n/scratch/mvngu/sage-src/sage-4.3-7781/spkg/base\n[mvngu@boxen base]$ hg st\nM sage-env\nM sage-spkg\n! prereq-0.3-install\n? prereq-0.5-install\n? prereq-0.5.tar\n```\n\nThe release manager needs to first do the following:\n\n1. Check in changes to `sage-env` and `sage-spkg` with \"hg ci\"\n2. Remove the file `prereq-0.3-install` from revision control using \"hg remove\".\n3. Delete `prereq-0.5-install` and `prereq-0.5.tar`.\n4. Edit `.hgignore` to ignore the file `prereq-0.6.tar`.\n\nAfter going through the above steps, then get \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/prereq-0.6-install\n\nput it under `SAGE_ROOT/spkg/base` and commit it in David Kirkby's name. Also get\n\nhttp://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/prereq-0.6.tar\n\nand put it under `SAGE_ROOT/spkg/base` as well. Here are the results of my tests on various combinations of platform and hardware:\n\n1. AIX 6.1 64-bit (machine from OpenAIX at http://www.metamodul.com/10.html), PowerPC_POWER5 `@` 2097 MHz, GCC 4.2.4 --- build failed when trying to compile bzip2-1.0.5:\n {{{\ngcc -fPIC -c bzip2.c\nIn file included from /usr/include/fcntl.h:188,\n                 from bzip2.c:70:\n/usr/include/unistd.h:909: error: expected ')' before '[' token\n/usr/include/unistd.h:910: error: expected declaration specifiers or '...' befor\ne 'rid_t'\nmake[2]: *** [bzip2.o] Error 1\nmake[2]: Leaving directory `/home/mvngu/sandbox/sage-4.3-7781/spkg/build/bzip2-1\n.0.5'\nError building bzip2\nmake[1]: *** [installed/bzip2-1.0.5] Error 1\nmake[1]: Leaving directory `/home/mvngu/sandbox/sage-4.3-7781/spkg'\ninstall.log (97%)\nreal    0m9.234s\nuser    0m2.410s\nsys     0m0.743s\nError building Sage.\n }}}\n This is expected, as AIX is not yet supported. As expected, a message would be printed warning about AIX being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue \"make\".\n1. Cygwin 1.5.25(0.156/4/2) 32-bit (winxp1 on boxen.math), Intel(R) Xeon(R)  CPU X7460 `@` 2.66GHz, GCC 4.3.2 20080827 (beta) 2 --- build failed when trying to compile python-2.6.2.p4:\n {{{\ngcc -L/home/mvngu/scratch/sage-4.3-7781/local/lib   -o python.exe \\\n                        Modules/python.o \\\n                        libpython2.6.dll.a -ldl    -lm  \nmake[2]: *** [sharedmods] Error 57\nmake[2]: Leaving directory `/home/mvngu/scratch/sage-4.3-7781/spkg/build/python-\n2.6.2.p4/src'\nError building Python.\n }}}\n This is expected, as Sage is not supported on Cygwin. As expected, a message would be printed warning about Cygwin being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue \"make\".\n1. HP-UX B.11.11 (David Kirkby's HP-UX machine), GCC 4.3.3 --- build failed when trying to compile cliquer-1.2.p2:\n {{{\nconfigure scripts and/or makefiles might override these later\n \nCannot determine your platform or it is not supported... exiting\n\nreal    0m0.078s\nuser    0m0.050s\nsys     0m0.020s\nsage: An error occurred while installing cliquer-1.2.p2\n }}}\n This is expected. I think one can build cliquer by some suitable editing of that spkg's file spkg-install. As of Sage 4.3, only Linux, Mac OS X, and Solaris are supported by that installation script. As expected, a message would be printed warning about HP-UX being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue \"make\".\n1. Solaris 10 (fulvia on SkyNet), i386 processor `@` 2400 MHz, GCC 4.4.2 --- build failed when trying to compile gnutls-2.2.1.p4:\n {{{\nserv.o: In function `peer_print_info':\n/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src/serv.c:489: undefined reference to `gnutls_x509_crt_print'\ncommon.o: In function `print_x509_info':\n/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src/common.c:151: undefined reference to `gnutls_x509_crt_check_hostname'\n../libextra/.libs/libgnutls-extra.so: undefined reference to `_gnutls_hostname_compare'\ncollect2: ld returned 1 exit status\nmake[5]: *** [gnutls-serv] Error 1\nmake[5]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src'\nmake[4]: *** [all-recursive] Error 1\nmake[4]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src'\nfailed to build GNUTLS\n        \nreal    36m28.030s\nuser    0m46.756s\nsys     0m58.655s\nsage: An error occurred while installing gnutls-2.2.1.p4\n }}}\n This is expected as x86 Solaris is not yet supported. As expected, a message would be printed warning about non-SPARC Solaris being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue \"make\".\n1. Ubuntu 8.04.3 LTS (boxen.math), Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz, GCC 4.2.4 --- build OK, all doctests pass.\n2. Mac OS X 10.6.2 (bsd.math), Dual-Core Intel Xeon `@` 2.66 GHz, GCC 4.2.1 --- build OK, many doctest failures as expected.\n3. Solaris 10 (t2.math), SPARC, GCC 4.4.1 --- build wasn't successful as expected.\n\nFor the above test platforms, the updated prereq package works as advertised.",
    "created_at": "2010-01-05T04:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67096",
    "user": "mvngu"
}
```

As of Sage 4.3, some files are not propertly under revision control:

```
[mvngu@boxen base]$ pwd
/scratch/mvngu/sage-src/sage-4.3-7781/spkg/base
[mvngu@boxen base]$ hg st
M sage-env
M sage-spkg
! prereq-0.3-install
? prereq-0.5-install
? prereq-0.5.tar
```

The release manager needs to first do the following:

1. Check in changes to `sage-env` and `sage-spkg` with "hg ci"
2. Remove the file `prereq-0.3-install` from revision control using "hg remove".
3. Delete `prereq-0.5-install` and `prereq-0.5.tar`.
4. Edit `.hgignore` to ignore the file `prereq-0.6.tar`.

After going through the above steps, then get 

http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/prereq-0.6-install

put it under `SAGE_ROOT/spkg/base` and commit it in David Kirkby's name. Also get

http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/prereq-0.6.tar

and put it under `SAGE_ROOT/spkg/base` as well. Here are the results of my tests on various combinations of platform and hardware:

1. AIX 6.1 64-bit (machine from OpenAIX at http://www.metamodul.com/10.html), PowerPC_POWER5 `@` 2097 MHz, GCC 4.2.4 --- build failed when trying to compile bzip2-1.0.5:
 {{{
gcc -fPIC -c bzip2.c
In file included from /usr/include/fcntl.h:188,
                 from bzip2.c:70:
/usr/include/unistd.h:909: error: expected ')' before '[' token
/usr/include/unistd.h:910: error: expected declaration specifiers or '...' befor
e 'rid_t'
make[2]: *** [bzip2.o] Error 1
make[2]: Leaving directory `/home/mvngu/sandbox/sage-4.3-7781/spkg/build/bzip2-1
.0.5'
Error building bzip2
make[1]: *** [installed/bzip2-1.0.5] Error 1
make[1]: Leaving directory `/home/mvngu/sandbox/sage-4.3-7781/spkg'
install.log (97%)
real    0m9.234s
user    0m2.410s
sys     0m0.743s
Error building Sage.
 }}}
 This is expected, as AIX is not yet supported. As expected, a message would be printed warning about AIX being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue "make".
1. Cygwin 1.5.25(0.156/4/2) 32-bit (winxp1 on boxen.math), Intel(R) Xeon(R)  CPU X7460 `@` 2.66GHz, GCC 4.3.2 20080827 (beta) 2 --- build failed when trying to compile python-2.6.2.p4:
 {{{
gcc -L/home/mvngu/scratch/sage-4.3-7781/local/lib   -o python.exe \
                        Modules/python.o \
                        libpython2.6.dll.a -ldl    -lm  
make[2]: *** [sharedmods] Error 57
make[2]: Leaving directory `/home/mvngu/scratch/sage-4.3-7781/spkg/build/python-
2.6.2.p4/src'
Error building Python.
 }}}
 This is expected, as Sage is not supported on Cygwin. As expected, a message would be printed warning about Cygwin being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue "make".
1. HP-UX B.11.11 (David Kirkby's HP-UX machine), GCC 4.3.3 --- build failed when trying to compile cliquer-1.2.p2:
 {{{
configure scripts and/or makefiles might override these later
 
Cannot determine your platform or it is not supported... exiting

real    0m0.078s
user    0m0.050s
sys     0m0.020s
sage: An error occurred while installing cliquer-1.2.p2
 }}}
 This is expected. I think one can build cliquer by some suitable editing of that spkg's file spkg-install. As of Sage 4.3, only Linux, Mac OS X, and Solaris are supported by that installation script. As expected, a message would be printed warning about HP-UX being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue "make".
1. Solaris 10 (fulvia on SkyNet), i386 processor `@` 2400 MHz, GCC 4.4.2 --- build failed when trying to compile gnutls-2.2.1.p4:
 {{{
serv.o: In function `peer_print_info':
/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src/serv.c:489: undefined reference to `gnutls_x509_crt_print'
common.o: In function `print_x509_info':
/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src/common.c:151: undefined reference to `gnutls_x509_crt_check_hostname'
../libextra/.libs/libgnutls-extra.so: undefined reference to `_gnutls_hostname_compare'
collect2: ld returned 1 exit status
make[5]: *** [gnutls-serv] Error 1
make[5]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src'
make[4]: *** [all-recursive] Error 1
make[4]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/home/mvngu/usr/fulvia/sandbox/sage-4.3-7781/spkg/build/gnutls-2.2.1.p4/src'
failed to build GNUTLS
        
real    36m28.030s
user    0m46.756s
sys     0m58.655s
sage: An error occurred while installing gnutls-2.2.1.p4
 }}}
 This is expected as x86 Solaris is not yet supported. As expected, a message would be printed warning about non-SPARC Solaris being an unsupported platform. To get pass the message, one could set the SAGE_PORT=yes and then issue "make".
1. Ubuntu 8.04.3 LTS (boxen.math), Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz, GCC 4.2.4 --- build OK, all doctests pass.
2. Mac OS X 10.6.2 (bsd.math), Dual-Core Intel Xeon `@` 2.66 GHz, GCC 4.2.1 --- build OK, many doctest failures as expected.
3. Solaris 10 (t2.math), SPARC, GCC 4.4.1 --- build wasn't successful as expected.

For the above test platforms, the updated prereq package works as advertised.



---

archive/issue_comments_067097.json:
```json
{
    "body": "I've fixed the issues with the base/ repo in 4.3.1.alpha0.",
    "created_at": "2010-01-05T04:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67097",
    "user": "@mwhansen"
}
```

I've fixed the issues with the base/ repo in 4.3.1.alpha0.



---

archive/issue_comments_067098.json:
```json
{
    "body": "Just note, \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/prereq-0.6-install\n\nwill need execute permissions, as its a shell script. If you download via the web, it will probably lose them.",
    "created_at": "2010-01-05T11:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67098",
    "user": "drkirkby"
}
```

Just note, 

http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.6/prereq-0.6-install

will need execute permissions, as its a shell script. If you download via the web, it will probably lose them.



---

archive/issue_comments_067099.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T02:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67099",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_067100.json:
```json
{
    "body": "Very carefully followed all instructions to the letter!",
    "created_at": "2010-01-14T02:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67100",
    "user": "@rlmill"
}
```

Very carefully followed all instructions to the letter!



---

archive/issue_comments_067101.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-01-16T00:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67101",
    "user": "@rlmill"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_067102.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-01-16T00:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67102",
    "user": "@rlmill"
}
```

Changing status from closed to new.



---

archive/issue_comments_067103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-16T00:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67103",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_067104.json:
```json
{
    "body": "Sorry!",
    "created_at": "2010-01-16T00:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7781#issuecomment-67104",
    "user": "@rlmill"
}
```

Sorry!
