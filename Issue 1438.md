# Issue 1438: GNUTLS fails to build on RHEL 4 (texinfo related)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-09 19:03:57

Assignee: mabshoff

The issue was reported by Bromskloss:

```
if (/bin/sh /misc/hacks/vol/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/missing --run makeinfo --version) >/dev/null 2>&1; then \
  for f in gnutls.info gnutls.info-[0-9] gnutls.info-[0-9][0-9] gnutls.i[0-9] gnutls.i[0-9][0-9]; do \
    if test -f $f; then mv $f $backupdir; restore=mv; else :; fi; \
  done; \
else :; fi && \
cd "$am__cwd"; \
if /bin/sh /misc/hacks/vol/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/missing --run makeinfo -I ../doc  -I . \
 -o gnutls.info gnutls.texi; \
then \
  rc=0; \
  cd .; \
else \
  rc=$?; \
  cd . && \
  $restore $backupdir/* `echo "./gnutls.info" | sed 's|[^/]*$||'`; \
fi; \
rm -rf $backupdir; exit $rc
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:14: Unknown command `euro'.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:14: Misplaced {.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:14: Misplaced }.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:15: Unknown command `euro'.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:15: Misplaced {.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:15: Misplaced }.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:174: warning: unlikely character [ in `@`var.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:174: warning: unlikely character ] in `@`var.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:347: warning: unlikely character [ in `@`var.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:347: warning: unlikely character ] in `@`var.
makeinfo: Removing output file `gnutls.info' due to errors; use --force to preserve.
make[5]: *** [gnutls.info] Error 1
make[5]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc'
make[4]: *** [all-recursive] Error 1
make[4]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src'
```

The problem seems to be an outdated texinfo. A solution might be to disable building the texinfo documentation.

Cheers,

Michael


---

Comment by rlm created at 2010-07-08 18:34:20

Resolution: fixed
