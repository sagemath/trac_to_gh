# Issue 9984: Freetype fails to build on AIX - looks as though it does not find Sage's zlib header files.

archive/issues_009984.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  chapoton\n\nUsing the following system: \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* DDS-4 tape drive \n\nFreeType fails to build, but reports:\n\n\n```\nkby/sage-4.6.alpha1/spkg/build/freetype-2.3.5.p2/src/src/lzw/ftlzw.c\nIn file included from /home/users/drkirkby/sage-4.6.alpha1/spkg/build/freetype-2.3.5.p2/src/src/gzip/ftgzip.c:45:\n/opt/pware/include/zlib.h:1585: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gzseek'\n/opt/pware/include/zlib.h:1586: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gztell'\n/opt/pware/include/zlib.h:1587: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gzoffset'\n/opt/pware/include/zlib.h:1588: error: expected declaration specifiers or '...' before 'off_t'\n/opt/pware/include/zlib.h:1589: error: expected declaration specifiers or '...' before 'off_t'\n```\n\n\nI can't understand why this is using the header files from `/opt/pware/include/` when it should be using the header file from `$SAGE_LOCAL/local/include/zlib.h`\n\nIssue created by migration from https://trac.sagemath.org/ticket/9985\n\n",
    "created_at": "2010-09-23T20:51:00Z",
    "labels": [
        "porting: AIX or HP-UX",
        "major",
        "bug"
    ],
    "title": "Freetype fails to build on AIX - looks as though it does not find Sage's zlib header files.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9984",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  chapoton

Using the following system: 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* DDS-4 tape drive 

FreeType fails to build, but reports:


```
kby/sage-4.6.alpha1/spkg/build/freetype-2.3.5.p2/src/src/lzw/ftlzw.c
In file included from /home/users/drkirkby/sage-4.6.alpha1/spkg/build/freetype-2.3.5.p2/src/src/gzip/ftgzip.c:45:
/opt/pware/include/zlib.h:1585: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gzseek'
/opt/pware/include/zlib.h:1586: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gztell'
/opt/pware/include/zlib.h:1587: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'gzoffset'
/opt/pware/include/zlib.h:1588: error: expected declaration specifiers or '...' before 'off_t'
/opt/pware/include/zlib.h:1589: error: expected declaration specifiers or '...' before 'off_t'
```


I can't understand why this is using the header files from `/opt/pware/include/` when it should be using the header file from `$SAGE_LOCAL/local/include/zlib.h`

Issue created by migration from https://trac.sagemath.org/ticket/9985





---

archive/issue_comments_100327.json:
```json
{
    "body": "Attachment\n\nBuild failure observed on an RS/6000 running AIX 5.3",
    "created_at": "2010-09-23T20:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9984#issuecomment-100327",
    "user": "drkirkby"
}
```

Attachment

Build failure observed on an RS/6000 running AIX 5.3



---

archive/issue_comments_100328.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-09-23T20:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9984#issuecomment-100328",
    "user": "drkirkby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_100329.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9984#issuecomment-100329",
    "user": "embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100330.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9984#issuecomment-100330",
    "user": "mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_100331.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9984#issuecomment-100331",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100332.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9984#issuecomment-100332",
    "user": "chapoton"
}
```

Resolution: invalid
