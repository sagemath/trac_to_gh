# Issue 7511: gnutls-2.2.1  fails to build on HP-UX

archive/issues_007511.json:
```json
{
    "body": "Assignee: drkirkby\n\ngnutls seems to be a problem package, as it is not building properly on HP-UX or OpenSolaris - see #7387 for the OpenSolaris problem. \n\nThis is the failure on HP-UX 11.11 on a HP C3600 workstation. \n\n```\nmkdir .libs/libgnutls-openssl.lax/liblgnu.a\n(cd .libs/libgnutls-openssl.lax/liblgnu.a && ar x /home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra/../lgl/.libs/liblgnu.a)\nrm -fr .libs/libgnutls-openssl.lax/libminitasn1.a\nmkdir .libs/libgnutls-openssl.lax/libminitasn1.a\n(cd .libs/libgnutls-openssl.lax/libminitasn1.a && ar x /home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra/../lib/minitasn1/.libs/libminitasn1.a)\ngcc -std=gnu99 -shared -fPIC -Wl,+h -Wl,libgnutls-openssl.sl.27 -Wl,+b -Wl,/home/drkirkby/sage-4.2.1/local/lib -o .libs/libgnutls-openssl.sl.27.2  .libs/gnutls_openssl.o .libs/openssl_compat.o  .libs/libgnutls-openssl.lax/liblgnu.a/dummy.o .libs/libgnutls-openssl.lax/liblgnu.a/asnprintf.o .libs/libgnutls-openssl.lax/liblgnu.a/asprintf.o .libs/libgnutls-openssl.lax/liblgnu.a/gc-libgcrypt.o .libs/libgnutls-openssl.lax/liblgnu.a/gc-pbkdf2-sha1.o .libs/libgnutls-openssl.lax/liblgnu.a/md2.o .libs/libgnutls-openssl.lax/liblgnu.a/memmem.o .libs/libgnutls-openssl.lax/liblgnu.a/printf-args.o .libs/libgnutls-openssl.lax/liblgnu.a/printf-parse.o .libs/libgnutls-openssl.lax/liblgnu.a/read-file.o .libs/libgnutls-openssl.lax/liblgnu.a/strverscmp.o .libs/libgnutls-openssl.lax/liblgnu.a/vasnprintf.o .libs/libgnutls-openssl.lax/liblgnu.a/vasprintf.o  .libs/libgnutls-openssl.lax/libminitasn1.a/decoding.o .libs/libgnutls-openssl.lax/libminitasn1.a/gstr.o .libs/libgnutls-openssl.lax/libminitasn1.a/errors.o .libs/libgnutls-openssl.lax/libminitasn1.a/parser_aux.o .libs/libgnutls-openssl.lax/libminitasn1.a/structure.o .libs/libgnutls-openssl.lax/libminitasn1.a/element.o .libs/libgnutls-openssl.lax/libminitasn1.a/coding.o   -L/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/lib/.libs -L/home/drkirkby/sage-4.2.1/local/lib /home/drkirkby/sage-4.2.1/local/lib/libgcrypt.sl /home/drkirkby/sage-4.2.1/local/lib/libgpg-error.sl ../lib/.libs/libgnutls.sl -lc \n(cd .libs && rm -f libgnutls-openssl.sl.27 && ln -s libgnutls-openssl.sl.27.2 libgnutls-openssl.sl.27)\n(cd .libs && rm -f libgnutls-openssl.sl && ln -s libgnutls-openssl.sl.27.2 libgnutls-openssl.sl)\nrm -fr .libs/libgnutls-openssl.lax\ncreating libgnutls-openssl.la\n(cd .libs && rm -f libgnutls-openssl.la && ln -s ../libgnutls-openssl.la libgnutls-openssl.la)\nmake[5]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra'\nmake[4]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra'\nMaking all in src\nmake[4]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'\nMaking all in cfg\nmake[5]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'\nMaking all in platon\nmake[6]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'\nMaking all in str\nmake[7]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon/str'\nmake[7]: Nothing to be done for `all'.\nmake[7]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon/str'\nmake[7]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'\nmake[7]: Nothing to be done for `all-am'.\nmake[7]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'\nmake[6]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'\nmake[6]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'\nmake[6]: Nothing to be done for `all-am'.\nmake[6]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'\nmake[5]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'\nmake[5]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'\ngcc -std=gnu99 -DHAVE_CONFIG_H -I. -I..  -I../includes -I../includes -I../lgl -I../lgl -I../gl -I../gl -I./cfg -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -MT serv-gaa.o -MD -MP -MF .deps/serv-gaa.Tpo -c -o serv-gaa.o serv-gaa.c\nmv -f .deps/serv-gaa.Tpo .deps/serv-gaa.Po\ngcc -std=gnu99 -DHAVE_CONFIG_H -I. -I..  -I../includes -I../includes -I../lgl -I../lgl -I../gl -I../gl -I./cfg -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -MT serv.o -MD -MP -MF .deps/serv.Tpo -c -o serv.o serv.c\nserv.c:774: warning: 'struct sockaddr_storage' declared inside parameter list\nserv.c:774: warning: its scope is only this definition or declaration, which is probably not what you want\nserv.c: In function 'get_port':\nserv.c:776: error: dereferencing pointer to incomplete type\nserv.c: In function 'main':\nserv.c:803: error: storage size of 'client_address' isn't known\nmake[5]: *** [serv.o] Error 1\nmake[5]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'\nmake[4]: *** [all-recursive] Error 1\nmake[4]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src'\nfailed to build GNUTLS\n\nreal 5m35.208s\nuser 3m55.400s\nsys 1m4.950s\nsage: An error occurred while installing gnutls-2.2.1.p4\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7511\n\n",
    "closed_at": "2012-10-05T09:12:55Z",
    "created_at": "2009-11-21T18:44:23Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gnutls-2.2.1  fails to build on HP-UX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7511",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

gnutls seems to be a problem package, as it is not building properly on HP-UX or OpenSolaris - see #7387 for the OpenSolaris problem. 

This is the failure on HP-UX 11.11 on a HP C3600 workstation. 

```
mkdir .libs/libgnutls-openssl.lax/liblgnu.a
(cd .libs/libgnutls-openssl.lax/liblgnu.a && ar x /home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra/../lgl/.libs/liblgnu.a)
rm -fr .libs/libgnutls-openssl.lax/libminitasn1.a
mkdir .libs/libgnutls-openssl.lax/libminitasn1.a
(cd .libs/libgnutls-openssl.lax/libminitasn1.a && ar x /home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra/../lib/minitasn1/.libs/libminitasn1.a)
gcc -std=gnu99 -shared -fPIC -Wl,+h -Wl,libgnutls-openssl.sl.27 -Wl,+b -Wl,/home/drkirkby/sage-4.2.1/local/lib -o .libs/libgnutls-openssl.sl.27.2  .libs/gnutls_openssl.o .libs/openssl_compat.o  .libs/libgnutls-openssl.lax/liblgnu.a/dummy.o .libs/libgnutls-openssl.lax/liblgnu.a/asnprintf.o .libs/libgnutls-openssl.lax/liblgnu.a/asprintf.o .libs/libgnutls-openssl.lax/liblgnu.a/gc-libgcrypt.o .libs/libgnutls-openssl.lax/liblgnu.a/gc-pbkdf2-sha1.o .libs/libgnutls-openssl.lax/liblgnu.a/md2.o .libs/libgnutls-openssl.lax/liblgnu.a/memmem.o .libs/libgnutls-openssl.lax/liblgnu.a/printf-args.o .libs/libgnutls-openssl.lax/liblgnu.a/printf-parse.o .libs/libgnutls-openssl.lax/liblgnu.a/read-file.o .libs/libgnutls-openssl.lax/liblgnu.a/strverscmp.o .libs/libgnutls-openssl.lax/liblgnu.a/vasnprintf.o .libs/libgnutls-openssl.lax/liblgnu.a/vasprintf.o  .libs/libgnutls-openssl.lax/libminitasn1.a/decoding.o .libs/libgnutls-openssl.lax/libminitasn1.a/gstr.o .libs/libgnutls-openssl.lax/libminitasn1.a/errors.o .libs/libgnutls-openssl.lax/libminitasn1.a/parser_aux.o .libs/libgnutls-openssl.lax/libminitasn1.a/structure.o .libs/libgnutls-openssl.lax/libminitasn1.a/element.o .libs/libgnutls-openssl.lax/libminitasn1.a/coding.o   -L/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/lib/.libs -L/home/drkirkby/sage-4.2.1/local/lib /home/drkirkby/sage-4.2.1/local/lib/libgcrypt.sl /home/drkirkby/sage-4.2.1/local/lib/libgpg-error.sl ../lib/.libs/libgnutls.sl -lc 
(cd .libs && rm -f libgnutls-openssl.sl.27 && ln -s libgnutls-openssl.sl.27.2 libgnutls-openssl.sl.27)
(cd .libs && rm -f libgnutls-openssl.sl && ln -s libgnutls-openssl.sl.27.2 libgnutls-openssl.sl)
rm -fr .libs/libgnutls-openssl.lax
creating libgnutls-openssl.la
(cd .libs && rm -f libgnutls-openssl.la && ln -s ../libgnutls-openssl.la libgnutls-openssl.la)
make[5]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra'
make[4]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/libextra'
Making all in src
make[4]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'
Making all in cfg
make[5]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'
Making all in platon
make[6]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'
Making all in str
make[7]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon/str'
make[7]: Nothing to be done for `all'.
make[7]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon/str'
make[7]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'
make[7]: Nothing to be done for `all-am'.
make[7]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'
make[6]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg/platon'
make[6]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'
make[6]: Nothing to be done for `all-am'.
make[6]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'
make[5]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src/cfg'
make[5]: Entering directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'
gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I..  -I../includes -I../includes -I../lgl -I../lgl -I../gl -I../gl -I./cfg -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -MT serv-gaa.o -MD -MP -MF .deps/serv-gaa.Tpo -c -o serv-gaa.o serv-gaa.c
mv -f .deps/serv-gaa.Tpo .deps/serv-gaa.Po
gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I..  -I../includes -I../includes -I../lgl -I../lgl -I../gl -I../gl -I./cfg -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/drkirkby/sage-4.2.1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -MT serv.o -MD -MP -MF .deps/serv.Tpo -c -o serv.o serv.c
serv.c:774: warning: 'struct sockaddr_storage' declared inside parameter list
serv.c:774: warning: its scope is only this definition or declaration, which is probably not what you want
serv.c: In function 'get_port':
serv.c:776: error: dereferencing pointer to incomplete type
serv.c: In function 'main':
serv.c:803: error: storage size of 'client_address' isn't known
make[5]: *** [serv.o] Error 1
make[5]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'
make[4]: *** [all-recursive] Error 1
make[4]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/home/drkirkby/sage-4.2.1/spkg/build/gnutls-2.2.1.p4/src'
failed to build GNUTLS

real 5m35.208s
user 3m55.400s
sys 1m4.950s
sage: An error occurred while installing gnutls-2.2.1.p4
```

Issue created by migration from https://trac.sagemath.org/ticket/7511





---

archive/issue_comments_063462.json:
```json
{
    "body": "Repored upstream to gnutls-devel at gnu.org under the title \"gnutls-2.2.1 fails to build on HP-UX\" at 0157 GMT on 25th Nov 2009.",
    "created_at": "2009-11-25T02:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7511#issuecomment-63462",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Repored upstream to gnutls-devel at gnu.org under the title "gnutls-2.2.1 fails to build on HP-UX" at 0157 GMT on 25th Nov 2009.



---

archive/issue_comments_063463.json:
```json
{
    "body": "Changing component from porting to AIX or HP-UX ports.",
    "created_at": "2010-09-23T15:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7511#issuecomment-63463",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from porting to AIX or HP-UX ports.



---

archive/issue_events_017804.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-05T09:12:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7511",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7511#event-17804"
}
```



---

archive/issue_comments_063464.json:
```json
{
    "body": "GNUTLS is no longer part of Sage.",
    "created_at": "2012-10-05T09:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7511#issuecomment-63464",
    "user": "https://github.com/jdemeyer"
}
```

GNUTLS is no longer part of Sage.



---

archive/issue_events_017805.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-05T09:12:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7511",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7511#event-17805"
}
```



---

archive/issue_comments_063465.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-10-05T09:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7511#issuecomment-63465",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
