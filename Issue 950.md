# Issue 950: include guava in sage (in the gap package?)

archive/issues_000950.json:
```json
{
    "body": "Assignee: was\n\nThe only obstruction right now is that it doesn't build on OS X:\n\n\n```\n\nif ! grep darwin sysinfo.gap ; then ( cd bin/i686-apple-darwin8.10.1-gcc ; strip gap) ; fi\nGAParch=i686-apple-darwin8.10.1-gcc\n( test -d bin || mkdir bin; \\\ntest -d bin/i686-apple-darwin8.10.1-gcc || mkdir bin/i686-apple-darwin8.10.1-gcc; cd bin/i686-apple-darwin8.10.1-gcc; \\\nmake -f ../../Makefile all2 CC=\"gcc\" CFLAGS=\"-O2\"; \\\n        cp wtdist ../wtdist; cp desauto ../desauto )\ngcc -c -O2 -o leonconv.o -c ../../src/leonconv.c\n../../src/leonconv.c:2:20: error: malloc.h: No such file or directory\n../../src/leonconv.c: In function 'main':\n../../src/leonconv.c:17: warning: incompatible implicit declaration of built-in function 'exit'\n../../src/leonconv.c:28: warning: incompatible implicit declaration of built-in function 'exit'\n../../src/leonconv.c: In function 'EquivalentToGuave':\n../../src/leonconv.c:121: warning: incompatible implicit declaration of built-in function 'exit'\nmake[1]: *** [leonconv.o] Error 1\ncp: wtdist: No such file or directory\ncp: desauto: No such file or directory\nmake: *** [all] Error 1\n\nreal    2m23.081s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/950\n\n",
    "created_at": "2007-10-20T21:07:44Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "include guava in sage (in the gap package?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/950",
    "user": "was"
}
```
Assignee: was

The only obstruction right now is that it doesn't build on OS X:


```

if ! grep darwin sysinfo.gap ; then ( cd bin/i686-apple-darwin8.10.1-gcc ; strip gap) ; fi
GAParch=i686-apple-darwin8.10.1-gcc
( test -d bin || mkdir bin; \
test -d bin/i686-apple-darwin8.10.1-gcc || mkdir bin/i686-apple-darwin8.10.1-gcc; cd bin/i686-apple-darwin8.10.1-gcc; \
make -f ../../Makefile all2 CC="gcc" CFLAGS="-O2"; \
        cp wtdist ../wtdist; cp desauto ../desauto )
gcc -c -O2 -o leonconv.o -c ../../src/leonconv.c
../../src/leonconv.c:2:20: error: malloc.h: No such file or directory
../../src/leonconv.c: In function 'main':
../../src/leonconv.c:17: warning: incompatible implicit declaration of built-in function 'exit'
../../src/leonconv.c:28: warning: incompatible implicit declaration of built-in function 'exit'
../../src/leonconv.c: In function 'EquivalentToGuave':
../../src/leonconv.c:121: warning: incompatible implicit declaration of built-in function 'exit'
make[1]: *** [leonconv.o] Error 1
cp: wtdist: No such file or directory
cp: desauto: No such file or directory
make: *** [all] Error 1

real    2m23.081s
```


Issue created by migration from https://trac.sagemath.org/ticket/950





---

archive/issue_comments_005796.json:
```json
{
    "body": "Hmm. What is the current status of this?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/950#issuecomment-5796",
    "user": "mabshoff"
}
```

Hmm. What is the current status of this?

Cheers,

Michael



---

archive/issue_comments_005797.json:
```json
{
    "body": "Related to #1452",
    "created_at": "2007-12-11T17:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/950#issuecomment-5797",
    "user": "rlm"
}
```

Related to #1452



---

archive/issue_comments_005798.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-19T06:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/950#issuecomment-5798",
    "user": "rlm"
}
```

Resolution: fixed
