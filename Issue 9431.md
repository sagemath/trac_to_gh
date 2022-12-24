# Issue 9431: opencdk spkg should add $SAGE_LOCAL/lib to LDFLAGS

archive/issues_009431.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  wjp saliola\n\nWillem explained this one to me. Apparently opencdk is now linking libgcrypt from the wrong place, due to libtools, caused by the addition of `-lgcrypt` in #8658. The short term fix is to make sure that `$SAGE_LOCAL/lib` is included in `LDFLAGS` in the `spkg-install` script, but the longer term fix will be to figure out why libtools is linking against `/usr/lib` in the first place.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9431\n\n",
    "created_at": "2010-07-05T19:40:53Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "opencdk spkg should add $SAGE_LOCAL/lib to LDFLAGS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9431",
    "user": "rlm"
}
```
Assignee: GeorgSWeber

CC:  wjp saliola

Willem explained this one to me. Apparently opencdk is now linking libgcrypt from the wrong place, due to libtools, caused by the addition of `-lgcrypt` in #8658. The short term fix is to make sure that `$SAGE_LOCAL/lib` is included in `LDFLAGS` in the `spkg-install` script, but the longer term fix will be to figure out why libtools is linking against `/usr/lib` in the first place.

Issue created by migration from https://trac.sagemath.org/ticket/9431





---

archive/issue_comments_090037.json:
```json
{
    "body": "Some relevant lines in the build log:\n\n\n```\n/bin/sh ../libtool --tag=CC   --mode=link gcc  -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -no-install  -o t-stream t-stream.o ../src/libopencdk.la -lgcrypt -lz\n\ngcc -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -o t-stream t-stream.o  ../src/.libs/libopencdk.so /usr/lib64/libgcrypt.so -lz -Wl,--rpath -Wl,/data2/wpalenst/sage-4.4.4/spkg/build/opencdk-0.6.6.p4/src/src/.libs -Wl,--rpath -Wl,/data2/wpalenst/sage-4.4.4/local/lib\n../src/.libs/libopencdk.so: undefined reference to `gcry_cipher_setkey@GCRYPT_1.2'\n../src/.libs/libopencdk.so: undefined reference to `gcry_cipher_setiv@GCRYPT_1.2'\n```\n\n\nOn another machine on which I've tried, opencdk also ended linking its tests against /usr/lib64/libgcrypt.so, but it didn't cause an error there.",
    "created_at": "2010-07-05T20:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9431#issuecomment-90037",
    "user": "wjp"
}
```

Some relevant lines in the build log:


```
/bin/sh ../libtool --tag=CC   --mode=link gcc  -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -no-install  -o t-stream t-stream.o ../src/libopencdk.la -lgcrypt -lz

gcc -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -o t-stream t-stream.o  ../src/.libs/libopencdk.so /usr/lib64/libgcrypt.so -lz -Wl,--rpath -Wl,/data2/wpalenst/sage-4.4.4/spkg/build/opencdk-0.6.6.p4/src/src/.libs -Wl,--rpath -Wl,/data2/wpalenst/sage-4.4.4/local/lib
../src/.libs/libopencdk.so: undefined reference to `gcry_cipher_setkey@GCRYPT_1.2'
../src/.libs/libopencdk.so: undefined reference to `gcry_cipher_setiv@GCRYPT_1.2'
```


On another machine on which I've tried, opencdk also ended linking its tests against /usr/lib64/libgcrypt.so, but it didn't cause an error there.



---

archive/issue_comments_090038.json:
```json
{
    "body": "Some more preliminary results:\n\nIt seems that adding `$SAGE_LOCAL/lib` to `$LIBRARY_PATH` as `sage-env` does, might have unexpected effects:\n\nOn 64 bit gentoo:\n\n\n```\n$ export LIBRARY_PATH=/blah\n$ gcc -print-search-dirs\n[...]\nlibraries: =/blah/x86_64-pc-linux-gnu/4.1.2/:/blah/../lib64/\n```\n\n\nSo `$SAGE_LOCAL/lib` does _not_ end up being searched by gcc in this case. (But the non-existent `$SAGE_LOCAL/lib64` does.)\n\n\nOn 64 bit debian (Lenny), this is\n\n\n```\nlibraries: =/blah/x86_64-linux-gnu/4.3.2/:/blah/../lib/\n```\n\n\n\nIt looks like we're completely mis-using `LIBRARY_PATH`... Maybe it's worth considering putting `-L$SAGE_LOCAL/lib` in `$LDFLAGS` in `sage-env`.",
    "created_at": "2010-07-05T21:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9431#issuecomment-90038",
    "user": "wjp"
}
```

Some more preliminary results:

It seems that adding `$SAGE_LOCAL/lib` to `$LIBRARY_PATH` as `sage-env` does, might have unexpected effects:

On 64 bit gentoo:


```
$ export LIBRARY_PATH=/blah
$ gcc -print-search-dirs
[...]
libraries: =/blah/x86_64-pc-linux-gnu/4.1.2/:/blah/../lib64/
```


So `$SAGE_LOCAL/lib` does _not_ end up being searched by gcc in this case. (But the non-existent `$SAGE_LOCAL/lib64` does.)


On 64 bit debian (Lenny), this is


```
libraries: =/blah/x86_64-linux-gnu/4.3.2/:/blah/../lib/
```



It looks like we're completely mis-using `LIBRARY_PATH`... Maybe it's worth considering putting `-L$SAGE_LOCAL/lib` in `$LDFLAGS` in `sage-env`.



---

archive/issue_comments_090039.json:
```json
{
    "body": "New spkg with the LDFLAGS workaround:\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/opencdk-0.6.6.p5.spkg",
    "created_at": "2010-07-06T07:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9431#issuecomment-90039",
    "user": "wjp"
}
```

New spkg with the LDFLAGS workaround:

http://www.math.leidenuniv.nl/~wpalenst/sage/opencdk-0.6.6.p5.spkg



---

archive/issue_comments_090040.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T07:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9431#issuecomment-90040",
    "user": "wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090041.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-06T07:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9431#issuecomment-90041",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090042.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T08:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9431#issuecomment-90042",
    "user": "rlm"
}
```

Resolution: fixed
