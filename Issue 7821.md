# Issue 7821: readline-6.0.p1 fails on FreeBSD

archive/issues_007821.json:
```json
{
    "body": "Assignee: pjeremy\n\nreadline-6.0.p1/spkg-install contains a typo in some FreeBSD-specific code, leading to the following error:\n\n```\n...\n/bin/sh ../support/shlib-install -O freebsd8.0 -d /home/peter/sage/sage-4.3/local/lib -b /home/peter/sage/sage-4.3/local/bin -i \"/usr/bin/install -c -m 644\" libreadline.so.6.0\ninstall: you may need to run ldconfig\nmake[1]: Leaving directory `/home/peter/sage/sage-4.3/spkg/build/readline-6.0.p1/src/shlib'\nln: SAGE_LOCAL/lib/libreadline.so: No such file or directory\n```\n\n\nThe affected code is no longer required with readline-6.0 so delete it.\n\nFreeBSD 3.x and later default to ELF, rather then a.out. A utility objformat(1) was temporarily introduced to enable third-party applications to determine te object format. This has now been deleted and code should assume ELF format if it does not exist. Explicitly linking libreadline against libtermcap is necessary to ensure that dependencies are picked up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7821\n\n",
    "created_at": "2010-01-03T00:53:06Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "readline-6.0.p1 fails on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7821",
    "user": "pjeremy"
}
```
Assignee: pjeremy

readline-6.0.p1/spkg-install contains a typo in some FreeBSD-specific code, leading to the following error:

```
...
/bin/sh ../support/shlib-install -O freebsd8.0 -d /home/peter/sage/sage-4.3/local/lib -b /home/peter/sage/sage-4.3/local/bin -i "/usr/bin/install -c -m 644" libreadline.so.6.0
install: you may need to run ldconfig
make[1]: Leaving directory `/home/peter/sage/sage-4.3/spkg/build/readline-6.0.p1/src/shlib'
ln: SAGE_LOCAL/lib/libreadline.so: No such file or directory
```


The affected code is no longer required with readline-6.0 so delete it.

FreeBSD 3.x and later default to ELF, rather then a.out. A utility objformat(1) was temporarily introduced to enable third-party applications to determine te object format. This has now been deleted and code should assume ELF format if it does not exist. Explicitly linking libreadline against libtermcap is necessary to ensure that dependencies are picked up.

Issue created by migration from https://trac.sagemath.org/ticket/7821





---

archive/issue_comments_067701.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-03T00:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7821#issuecomment-67701",
    "user": "pjeremy"
}
```

Attachment



---

archive/issue_comments_067702.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T01:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7821#issuecomment-67702",
    "user": "pjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067703.json:
```json
{
    "body": "This looks good to me.  I've made an spkg out of the changes at http://sage.math.washington.edu/home/mhansen/readline-6.0.p2.spkg",
    "created_at": "2010-06-22T22:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7821#issuecomment-67703",
    "user": "mhansen"
}
```

This looks good to me.  I've made an spkg out of the changes at http://sage.math.washington.edu/home/mhansen/readline-6.0.p2.spkg



---

archive/issue_comments_067704.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-22T22:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7821#issuecomment-67704",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067705.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7821#issuecomment-67705",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_067706.json:
```json
{
    "body": "For the record:\n\nThe proper fix (btw. also for a couple of other systems, like Arch Linux, OpenSuSE and meanwhile also Ubuntu 11.10 I think) is to add `$(TERMCAP_LIB)` to the link command of `libreadline.so` in `src/shlib/Makefile.in`, rather than setting `SHLIB_LIBS='-ltermcap'`.  This is more generic, since readline's `configure` determines what the proper `libtermcap` (or its replacement) is.  No need to special-case on the platform (operating system / distro).",
    "created_at": "2011-10-28T11:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7821#issuecomment-67706",
    "user": "leif"
}
```

For the record:

The proper fix (btw. also for a couple of other systems, like Arch Linux, OpenSuSE and meanwhile also Ubuntu 11.10 I think) is to add `$(TERMCAP_LIB)` to the link command of `libreadline.so` in `src/shlib/Makefile.in`, rather than setting `SHLIB_LIBS='-ltermcap'`.  This is more generic, since readline's `configure` determines what the proper `libtermcap` (or its replacement) is.  No need to special-case on the platform (operating system / distro).
