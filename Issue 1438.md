# Issue 1438: GNUTLS fails to build on RHEL 4 (texinfo related)

archive/issues_001438.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe issue was reported by Bromskloss:\n\n```\nif (/bin/sh /misc/hacks/vol/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/missing --run makeinfo --version) >/dev/null 2>&1; then \\\n  for f in gnutls.info gnutls.info-[0-9] gnutls.info-[0-9][0-9] gnutls.i[0-9] gnutls.i[0-9][0-9]; do \\\n    if test -f $f; then mv $f $backupdir; restore=mv; else :; fi; \\\n  done; \\\nelse :; fi && \\\ncd \"$am__cwd\"; \\\nif /bin/sh /misc/hacks/vol/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/missing --run makeinfo -I ../doc  -I . \\\n -o gnutls.info gnutls.texi; \\\nthen \\\n  rc=0; \\\n  cd .; \\\nelse \\\n  rc=$?; \\\n  cd . && \\\n  $restore $backupdir/* `echo \"./gnutls.info\" | sed 's|[^/]*$||'`; \\\nfi; \\\nrm -rf $backupdir; exit $rc\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:14: Unknown command `euro'.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:14: Misplaced {.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:14: Misplaced }.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:15: Unknown command `euro'.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:15: Misplaced {.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//signatures.texi:15: Misplaced }.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:174: warning: unlikely character [ in @var.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:174: warning: unlikely character ] in @var.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:347: warning: unlikely character [ in @var.\n/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:347: warning: unlikely character ] in @var.\nmakeinfo: Removing output file `gnutls.info' due to errors; use --force to preserve.\nmake[5]: *** [gnutls.info] Error 1\nmake[5]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc'\nmake[4]: *** [all-recursive] Error 1\nmake[4]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src'\n```\n\nThe problem seems to be an outdated texinfo. A solution might be to disable building the texinfo documentation.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1438\n\n",
    "created_at": "2007-12-09T19:03:57Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "GNUTLS fails to build on RHEL 4 (texinfo related)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
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
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:174: warning: unlikely character [ in @var.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:174: warning: unlikely character ] in @var.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:347: warning: unlikely character [ in @var.
/afs/kth.se/misc/hacks/sys/vol/i386_linux6/sage/sage-2.8.15/spkg/build/gnutls-1.6.3/src/doc//pgp-api.texi:347: warning: unlikely character ] in @var.
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

Issue created by migration from https://trac.sagemath.org/ticket/1438





---

archive/issue_events_003682.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-08T18:34:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1438",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1438#event-3682"
}
```



---

archive/issue_events_003683.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-08T18:34:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1438",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1438#event-3683"
}
```



---

archive/issue_comments_009256.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-08T18:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1438#issuecomment-9256",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
