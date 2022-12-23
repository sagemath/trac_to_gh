# Issue 7132: mpir-1.2.p7 fails to build as CXXFLAGS has no 64-bit option on Solaris

archive/issues_007132.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  dimpase\n\nI'm using the following hardware and software now.\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\" \n\nmpir-1.2.p7 consists of both C and C++ code, but although the spkg-install is adding -m64 to CFLAGS, it is not doing this to CXXFLAGS on Solaris. Hence it attempts to build with a mix of 32 and 64-bit binaries, which gives the usual error:\n\nld: fatal: file .libs/dummy.o: wrong ELF class: ELFCLASS32\nquired\n\nA look at the object files, clearly shows some are built 32-bit, whilst others are 64-bit. \n\n\n\n```\n./cxx/.libs/ismpf.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required\n./cxx/.libs/ismpq.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required\n./cxx/.libs/osfuns.o:   ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required\n./cxx/.libs/ismpz.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required\n```\n\n\nthough others (not shown) are 64-bit as they are supposed to be. \n\nThere are a number of packages in Sage building as 32-bit on Solaris, despite SAGE64 being set to \"yes\" This include, but are almost certainly not limited to:\n\n* zlib #7128\n* libgpg_error #7129\n* libpng #7130\n* libcliquer #7131\n\nmpir fails to build at all, since it is trying to mix 32 and 64-bit objects. \n\nThe fix to this will be quite easy, but I will wait until I've written a better sage-env, which will mean the correct flags for 64-bit will be generated on all platforms and compilers we can possibly envisage. Whilst -m64 works with Sun and GNU compilers, it will not work with native compilers on AIX or HP-UX. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7132\n\n",
    "created_at": "2009-10-06T00:04:42Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "mpir-1.2.p7 fails to build as CXXFLAGS has no 64-bit option on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7132",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  dimpase

I'm using the following hardware and software now.
* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes" 

mpir-1.2.p7 consists of both C and C++ code, but although the spkg-install is adding -m64 to CFLAGS, it is not doing this to CXXFLAGS on Solaris. Hence it attempts to build with a mix of 32 and 64-bit binaries, which gives the usual error:

ld: fatal: file .libs/dummy.o: wrong ELF class: ELFCLASS32
quired

A look at the object files, clearly shows some are built 32-bit, whilst others are 64-bit. 



```
./cxx/.libs/ismpf.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
./cxx/.libs/ismpq.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
./cxx/.libs/osfuns.o:   ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
./cxx/.libs/ismpz.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
```


though others (not shown) are 64-bit as they are supposed to be. 

There are a number of packages in Sage building as 32-bit on Solaris, despite SAGE64 being set to "yes" This include, but are almost certainly not limited to:

* zlib #7128
* libgpg_error #7129
* libpng #7130
* libcliquer #7131

mpir fails to build at all, since it is trying to mix 32 and 64-bit objects. 

The fix to this will be quite easy, but I will wait until I've written a better sage-env, which will mean the correct flags for 64-bit will be generated on all platforms and compilers we can possibly envisage. Whilst -m64 works with Sun and GNU compilers, it will not work with native compilers on AIX or HP-UX. 


Issue created by migration from https://trac.sagemath.org/ticket/7132





---

archive/issue_comments_059146.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7132#issuecomment-59146",
    "user": "mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_059147.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7132#issuecomment-59147",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059148.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-14T16:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7132#issuecomment-59148",
    "user": "chapoton"
}
```

Resolution: invalid
