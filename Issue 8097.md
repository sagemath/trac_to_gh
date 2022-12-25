# Issue 8097: termcap fails to build in Open Solaris x64 as 64 bit

archive/issues_008097.json:
```json
{
    "body": "Assignee: drkirkby\n\nWith no CFLAGS set the build is 32 bit\n\n\n\n```\ngcc -std=gnu99 -O2 -g -m64 -D_REENTRANT -D_THREAD_SAFE -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -O2 -g -m64 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o .libs/certtool certtool-gaa.o certtool.o prime.o certtool-cfg.o cfg+.o cfgfile.o cmdline.o parse.o props.o shared.o dynfgets.o strctype.o strdyn.o strplus.o  ../lib/.libs/libgnutls.so -L/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib -lz ../gl/.libs/libgnu.a /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libgcrypt.so /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libgpg-error.so -lreadline -ltermcap -lnsl -lsocket  -R/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib\nld: warning: file /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libtermcap.a(termcap.o): wrong ELF class: ELFCLASS32\n\n```\n\n\n\nA patch is ready.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8097\n\n",
    "created_at": "2010-01-27T20:55:21Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "termcap fails to build in Open Solaris x64 as 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8097",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

With no CFLAGS set the build is 32 bit



```
gcc -std=gnu99 -O2 -g -m64 -D_REENTRANT -D_THREAD_SAFE -I/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/include -O2 -g -m64 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o .libs/certtool certtool-gaa.o certtool.o prime.o certtool-cfg.o cfg+.o cfgfile.o cmdline.o parse.o props.o shared.o dynfgets.o strctype.o strdyn.o strplus.o  ../lib/.libs/libgnutls.so -L/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib -lz ../gl/.libs/libgnu.a /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libgcrypt.so /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libgpg-error.so -lreadline -ltermcap -lnsl -lsocket  -R/export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib
ld: warning: file /export/home/jaap/Downloads/sage-4.3.2.alpha0/local/lib/libtermcap.a(termcap.o): wrong ELF class: ELFCLASS32

```



A patch is ready.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8097





---

archive/issue_comments_070913.json:
```json
{
    "body": "Attachment [termcap-1.3.1.p1.patch](tarball://root/attachments/some-uuid/ticket8097/termcap-1.3.1.p1.patch) by @jaapspies created at 2010-01-27 20:59:38",
    "created_at": "2010-01-27T20:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70913",
    "user": "https://github.com/jaapspies"
}
```

Attachment [termcap-1.3.1.p1.patch](tarball://root/attachments/some-uuid/ticket8097/termcap-1.3.1.p1.patch) by @jaapspies created at 2010-01-27 20:59:38



---

archive/issue_comments_070914.json:
```json
{
    "body": "The spkgs can be found here:\n\n\n\n```\nhttp://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg\n```\n\n\n\nJaap",
    "created_at": "2010-01-27T21:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70914",
    "user": "https://github.com/jaapspies"
}
```

The spkgs can be found here:



```
http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg
```



Jaap



---

archive/issue_comments_070915.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-27T21:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70915",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070916.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-28T08:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70916",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070917.json:
```json
{
    "body": "The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.\n\nA more accurate comment would be. \n\n* #8097 Ensures the compiler flag -m64 is added at any time SAGE64 was set to \"yes\" - previously this was only happening on OS X. This should aid building 64-bit on any platform, although it has only been tested on Open Solaris. \n\nIt's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. \n\nIt would be good to see some evidence the patch actually works. Such as by showing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and for others, adding it does not generate 64-bit binaries. \n\nFor zlib, adding -m64 stops the build of shared libraries. \n\nDave",
    "created_at": "2010-01-28T08:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70917",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris.

A more accurate comment would be. 

* #8097 Ensures the compiler flag -m64 is added at any time SAGE64 was set to "yes" - previously this was only happening on OS X. This should aid building 64-bit on any platform, although it has only been tested on Open Solaris. 

It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 

It would be good to see some evidence the patch actually works. Such as by showing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and for others, adding it does not generate 64-bit binaries. 

For zlib, adding -m64 stops the build of shared libraries. 

Dave



---

archive/issue_comments_070918.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n\n> \n> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. \n> \n> It would be good to see some evidence the patch actually works. Such as by showing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and for others, adding it does not generate 64-bit binaries. \n> \n> For zlib, adding -m64 stops the build of shared libraries. \n> \n\nI really don't like those cut and paste comments.\n\n\nJaap",
    "created_at": "2010-01-28T11:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70918",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:2 drkirkby]:

> 
> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 
> 
> It would be good to see some evidence the patch actually works. Such as by showing the output of the 'ldd' command, that the library and/or binary is now a 64-bit one. For some packages, it is unnecessary to add -m64 and for others, adding it does not generate 64-bit binaries. 
> 
> For zlib, adding -m64 stops the build of shared libraries. 
> 

I really don't like those cut and paste comments.


Jaap



---

archive/issue_comments_070919.json:
```json
{
    "body": "Sorry, I did not mean to offend by putting the same comment more than once.",
    "created_at": "2010-01-28T12:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70919",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Sorry, I did not mean to offend by putting the same comment more than once.



---

archive/issue_comments_070920.json:
```json
{
    "body": "Attachment [termcap-1.3.1.p1+.patch](tarball://root/attachments/some-uuid/ticket8097/termcap-1.3.1.p1+.patch) by @jaapspies created at 2010-01-28 13:49:30\n\nChanged SPKG.txt to reflect the comments from David.\n\nNo change of patch level applied.\n\n[http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg)\n\ntermcap only builds a static library local/lib/libtermcap.a containing\n\n64 bit *.o files (I double checked that).\n\nJaap",
    "created_at": "2010-01-28T13:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70920",
    "user": "https://github.com/jaapspies"
}
```

Attachment [termcap-1.3.1.p1+.patch](tarball://root/attachments/some-uuid/ticket8097/termcap-1.3.1.p1+.patch) by @jaapspies created at 2010-01-28 13:49:30

Changed SPKG.txt to reflect the comments from David.

No change of patch level applied.

[http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/termcap-1.3.1.p1.spkg)

termcap only builds a static library local/lib/libtermcap.a containing

64 bit *.o files (I double checked that).

Jaap



---

archive/issue_comments_070921.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-28T13:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70921",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070922.json:
```json
{
    "body": "Agreed. Positive review.",
    "created_at": "2010-01-28T13:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70922",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Agreed. Positive review.



---

archive/issue_comments_070923.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T13:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70923",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070924.json:
```json
{
    "body": "Chacking static libraries:\n\n\n\n```\njaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ ar -x local/lib/libtermcap.a \njaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ ls\nCOPYING.txt  install.log  local     README.txt\tsage-python\t     spkg\ttmp\t  version.o\ndata\t     ipython\t  makefile  sage\tsage-README-osx.txt  termcap.o\ttparam.o\njaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ file *.o\ntermcap.o:\tELF 64-bit LSB relocatable AMD64 Version 1\ntparam.o:\tELF 64-bit LSB relocatable AMD64 Version 1\nversion.o:\tELF 64-bit LSB relocatable AMD64 Version 1\n\n```\n\n\n\nJaap",
    "created_at": "2010-01-28T14:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70924",
    "user": "https://github.com/jaapspies"
}
```

Chacking static libraries:



```
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ ar -x local/lib/libtermcap.a 
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ ls
COPYING.txt  install.log  local     README.txt	sage-python	     spkg	tmp	  version.o
data	     ipython	  makefile  sage	sage-README-osx.txt  termcap.o	tparam.o
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ file *.o
termcap.o:	ELF 64-bit LSB relocatable AMD64 Version 1
tparam.o:	ELF 64-bit LSB relocatable AMD64 Version 1
version.o:	ELF 64-bit LSB relocatable AMD64 Version 1

```



Jaap



---

archive/issue_comments_070925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8097#issuecomment-70925",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008305.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T15:13:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8097",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8097#event-8305"
}
```
