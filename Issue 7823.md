# Issue 7823: libgcrypt-1.4.4.p1 references incorrect shared library on FreeBSD

archive/issues_007823.json:
```json
{
    "body": "Assignee: pjeremy\n\nCC:  drkirby was\n\nChase shared library name difference on FreeBSD.  Otherwise the gnutls build fails similar to:\n\n```\n(cd /home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/libextra; /bin/sh ../libtool  --tag=CC --mode=relink gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -pipe -I/home/peter/sage/sage-4.3/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -no-undefined -L../lib/.libs -L/home/peter/sage/sage-4.3/local/lib -lopencdk -L/usr/local/lib -L/usr/local/lib -lgcrypt -L/usr/local/lib -lgpg-error -L/usr/local/lib -lintl -L/usr/local/lib -liconv -L/home/peter/sage/sage-4.3/local/lib -lz -R/home/peter/sage/sage-4.3/local/lib -R/usr/local/lib -version-info 27:2:1 -o libgnutls-extra.la -rpath /home/peter/sage/sage-4.3/local/lib gnutls_extra.lo gnutls_openpgp.lo gnutls_ia.lo openpgp/libgnutls_openpgp.la ../lgl/liblgnu.la ../lib/libgnutls.la minilzo/libminilzo.la )  \ngcc -std=gnu99 -shared  .libs/gnutls_extra.o .libs/gnutls_openpgp.o .libs/gnutls_ia.o -Wl,--whole-archive openpgp/.libs/libgnutls_openpgp.a ../lgl/.libs/liblgnu.a minilzo/.libs/libminilzo.a -Wl,--no-whole-archive  -Wl,--rpath -Wl,/home/peter/sage/sage-4.3/local/lib -Wl,--rpath -Wl,/usr/local/lib -L/home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/lib/.libs -L/home/peter/sage/sage-4.3/local/lib -lopencdk -L/usr/local/lib -lz -lgcrypt -lintl -liconv -lgpg-error -lgnutls  -Wl,-soname -Wl,libgnutls-extra.so.27 -o .libs/libgnutls-extra.so.27\n/usr/bin/ld: /home/peter/sage/sage-4.3/local/lib/libgcrypt.a(libgcrypt_la-visibility.o): relocation R_X86_64_32 can not be used when making a shared object; recompile with -fPIC\n/home/peter/sage/sage-4.3/local/lib/libgcrypt.a: could not read symbols: Bad value\nlibtool: install: error: relink `libgnutls-extra.la' with the above command before installing it\n*** Error code 1\n\nStop in /home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/libextra.\n*** Error code 1\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7823\n\n",
    "created_at": "2010-01-03T01:53:05Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "libgcrypt-1.4.4.p1 references incorrect shared library on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7823",
    "user": "pjeremy"
}
```
Assignee: pjeremy

CC:  drkirby was

Chase shared library name difference on FreeBSD.  Otherwise the gnutls build fails similar to:

```
(cd /home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/libextra; /bin/sh ../libtool  --tag=CC --mode=relink gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -pipe -I/home/peter/sage/sage-4.3/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -no-undefined -L../lib/.libs -L/home/peter/sage/sage-4.3/local/lib -lopencdk -L/usr/local/lib -L/usr/local/lib -lgcrypt -L/usr/local/lib -lgpg-error -L/usr/local/lib -lintl -L/usr/local/lib -liconv -L/home/peter/sage/sage-4.3/local/lib -lz -R/home/peter/sage/sage-4.3/local/lib -R/usr/local/lib -version-info 27:2:1 -o libgnutls-extra.la -rpath /home/peter/sage/sage-4.3/local/lib gnutls_extra.lo gnutls_openpgp.lo gnutls_ia.lo openpgp/libgnutls_openpgp.la ../lgl/liblgnu.la ../lib/libgnutls.la minilzo/libminilzo.la )  
gcc -std=gnu99 -shared  .libs/gnutls_extra.o .libs/gnutls_openpgp.o .libs/gnutls_ia.o -Wl,--whole-archive openpgp/.libs/libgnutls_openpgp.a ../lgl/.libs/liblgnu.a minilzo/.libs/libminilzo.a -Wl,--no-whole-archive  -Wl,--rpath -Wl,/home/peter/sage/sage-4.3/local/lib -Wl,--rpath -Wl,/usr/local/lib -L/home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/lib/.libs -L/home/peter/sage/sage-4.3/local/lib -lopencdk -L/usr/local/lib -lz -lgcrypt -lintl -liconv -lgpg-error -lgnutls  -Wl,-soname -Wl,libgnutls-extra.so.27 -o .libs/libgnutls-extra.so.27
/usr/bin/ld: /home/peter/sage/sage-4.3/local/lib/libgcrypt.a(libgcrypt_la-visibility.o): relocation R_X86_64_32 can not be used when making a shared object; recompile with -fPIC
/home/peter/sage/sage-4.3/local/lib/libgcrypt.a: could not read symbols: Bad value
libtool: install: error: relink `libgnutls-extra.la' with the above command before installing it
*** Error code 1

Stop in /home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/libextra.
*** Error code 1
```



Issue created by migration from https://trac.sagemath.org/ticket/7823





---

archive/issue_comments_067720.json:
```json
{
    "body": "Attachment [7823.libgcrypt.patch](tarball://root/attachments/some-uuid/ticket7823/7823.libgcrypt.patch) by pjeremy created at 2010-01-03 01:54:01",
    "created_at": "2010-01-03T01:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7823#issuecomment-67720",
    "user": "pjeremy"
}
```

Attachment [7823.libgcrypt.patch](tarball://root/attachments/some-uuid/ticket7823/7823.libgcrypt.patch) by pjeremy created at 2010-01-03 01:54:01



---

archive/issue_comments_067721.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T01:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7823#issuecomment-67721",
    "user": "pjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067722.json:
```json
{
    "body": "I'll trust you it worked on FreeBSD. Clearly it can have no impact on any other system, so its a positive from me. \n\nDave",
    "created_at": "2010-01-05T18:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7823#issuecomment-67722",
    "user": "drkirkby"
}
```

I'll trust you it worked on FreeBSD. Clearly it can have no impact on any other system, so its a positive from me. 

Dave



---

archive/issue_comments_067723.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-05T18:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7823#issuecomment-67723",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067724.json:
```json
{
    "body": "Here is an updated spkg with pjeremy's patch: \n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/libgcrypt/libgcrypt-1.4.4.p2.spkg\n\nI took libgcrypt-1.4.4.p1.spkg and first checked in all outstanding changes by drkirby in his name. Then I applied pjeremy's patch and checked in changes in pjeremy's name.",
    "created_at": "2010-01-24T14:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7823#issuecomment-67724",
    "user": "mvngu"
}
```

Here is an updated spkg with pjeremy's patch: 

http://sage.math.washington.edu/home/mvngu/spkg/standard/libgcrypt/libgcrypt-1.4.4.p2.spkg

I took libgcrypt-1.4.4.p1.spkg and first checked in all outstanding changes by drkirby in his name. Then I applied pjeremy's patch and checked in changes in pjeremy's name.



---

archive/issue_comments_067725.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T14:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7823#issuecomment-67725",
    "user": "mvngu"
}
```

Resolution: fixed
