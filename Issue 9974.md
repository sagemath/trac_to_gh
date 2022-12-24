# Issue 9974: Update GnuTLS  and clean up the package

archive/issues_009974.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime drkirkby\n\nThe current version of GnuTLS in Sage has multiple issues, not all of which will probably be solved by this ticket, but at least of subset of them will be. \n* The current version in Sage is very old. \n* There are security issues with the current version - see #7542\n* There's no `spkg-check` file - see #9308\n* It fails to build on AIX - see #9974\n* It fails to build on HP-UX - see  #7511\n* `make` is used instead of `$MAKE`\n* `-m64` is hard-coded as the compiler flag needed for 64-bit builds\n* `SPKG.txt` lacks the `Special Update/Build Instructions` section.\n* There's an incomplete list of dependencies in `SKG.txt`, with a remark to `FIXME`\n\nIssue created by migration from https://trac.sagemath.org/ticket/9975\n\n",
    "created_at": "2010-09-23T09:54:59Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Update GnuTLS  and clean up the package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9974",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  @nexttime drkirkby

The current version of GnuTLS in Sage has multiple issues, not all of which will probably be solved by this ticket, but at least of subset of them will be. 
* The current version in Sage is very old. 
* There are security issues with the current version - see #7542
* There's no `spkg-check` file - see #9308
* It fails to build on AIX - see #9974
* It fails to build on HP-UX - see  #7511
* `make` is used instead of `$MAKE`
* `-m64` is hard-coded as the compiler flag needed for 64-bit builds
* `SPKG.txt` lacks the `Special Update/Build Instructions` section.
* There's an incomplete list of dependencies in `SKG.txt`, with a remark to `FIXME`

Issue created by migration from https://trac.sagemath.org/ticket/9975





---

archive/issue_comments_100071.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-11T18:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100071",
    "user": "mariah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100072.json:
```json
{
    "body": "Diff for the gnutls spkg, for reviewing only.",
    "created_at": "2011-05-11T18:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100072",
    "user": "mariah"
}
```

Diff for the gnutls spkg, for reviewing only.



---

archive/issue_comments_100073.json:
```json
{
    "body": "Attachment [gnutls-2.2.1.p5-2.12.3.diff](tarball://root/attachments/some-uuid/ticket9975/gnutls-2.2.1.p5-2.12.3.diff) by @jhpalmieri created at 2011-07-23 20:02:58\n\nThis seems to build on sage.math, an OS X box, and OpenSolaris.  I'm getting self-test failures, though.  On sage.math:\n\n```\nmake[5]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\\\n2.3/src/tests/openpgp-certs'\nmake[4]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\\\n2.3/src/tests/openpgp-certs'\nmake[3]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\\\n2.3/src/tests'\nmake[3]: Entering directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.\\\n12.3/src'\nmake[3]: warning: -jN forced in submake: disabling jobserver mode.\nmake[3]: Nothing to be done for `check-am'.\nmake[3]: INTERNAL: Exiting with 1 jobserver tokens available; should be 12!\nmake[3]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\\\n2.3/src'\nmake[2]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\\\n2.3/src'\nAn error occurred while testing GnuTLS\n*************************************\nError testing package ** gnutls-2.12.3 **\n*************************************\n```\n\nOn OS X:\n\n```\nsuccessSelf test `/Applications/sage/spkg/build/gnutls-2.12.3/src/tests/.libs/rng-fork' finished with 0 errors\nPASS: rng-fork\nSelf test `/Applications/sage/spkg/build/gnutls-2.12.3/src/tests/.libs/openssl' finished with 0 errors\nPASS: openssl\nserver handshake Error in the push function. (-53) \n```\n\nand then it hangs.  On OpenSolaris (David Kirkby's machine hawk):\n\n```\n  CC     test-vasnprintf.o\ntest-unistd.c:27:1: error: 'NULL' undeclared here (not in a function)\ntest-unistd.c:27:1: error: bit-field 'verify_error_if_negative_size__' width not an integer constant\ntest-unistd.c:30:14: error: 'SEEK_CUR' undeclared here (not in a function)\ntest-unistd.c:30:24: error: 'SEEK_END' undeclared here (not in a function)\ntest-unistd.c:30:34: error: 'SEEK_SET' undeclared here (not in a function)\ntest-unistd.c:35:9: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'or'\ntest-unistd.c:40:9: error: expected '=', ',', ';', 'asm' or '__attribute__' before 't2'\ntest-unistd.c:45:7: error: expected '=', ',', ';', 'asm' or '__attribute__' before 't5'\ntest-unistd.c:46:7: error: expected '=', ',', ';', 'asm' or '__attribute__' before 't6'\n  CC     test-vasprintf.o\nmake[7]: *** [test-unistd.o] Error 1\nmake[7]: *** Waiting for unfinished jobs....\nmake[7]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'\nmake[6]: *** [check-am] Error 2\nmake[6]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'\nmake[5]: *** [check-recursive] Error 1\nmake[5]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'\nmake[4]: *** [check] Error 2\nmake[4]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'\nmake[3]: *** [check-recursive] Error 1\nmake[3]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl'\nmake[2]: *** [check] Error 2\nmake[2]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl'\nmake[1]: *** [check-recursive] Error 1\nmake[1]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib'\nmake: *** [check-recursive] Error 1\nAn error occurred while testing GnuTLS\n*************************************\nError testing package ** gnutls-2.12.3 **\n*************************************\n```\n\n\n\nOne more thing: `$RM` is no longer set by sage-env, so do you need to modify it in spkg-install?  If you do, should you test whether `$RM_SAVE` is nonempty before\n\n```\nRM=$RM_SAVE\nexport RM\n```\n\nDo you even need to export `RM` at the end, or are the changes in this script (in particular `unset RM`) just local to the script?",
    "created_at": "2011-07-23T20:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100073",
    "user": "@jhpalmieri"
}
```

Attachment [gnutls-2.2.1.p5-2.12.3.diff](tarball://root/attachments/some-uuid/ticket9975/gnutls-2.2.1.p5-2.12.3.diff) by @jhpalmieri created at 2011-07-23 20:02:58

This seems to build on sage.math, an OS X box, and OpenSolaris.  I'm getting self-test failures, though.  On sage.math:

```
make[5]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\
2.3/src/tests/openpgp-certs'
make[4]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\
2.3/src/tests/openpgp-certs'
make[3]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\
2.3/src/tests'
make[3]: Entering directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.\
12.3/src'
make[3]: warning: -jN forced in submake: disabling jobserver mode.
make[3]: Nothing to be done for `check-am'.
make[3]: INTERNAL: Exiting with 1 jobserver tokens available; should be 12!
make[3]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\
2.3/src'
make[2]: Leaving directory `/mnt/usb1/scratch/palmieri/gnutls/sage-4.7.1.rc0/spkg/build/gnutls-2.1\
2.3/src'
An error occurred while testing GnuTLS
*************************************
Error testing package ** gnutls-2.12.3 **
*************************************
```

On OS X:

```
successSelf test `/Applications/sage/spkg/build/gnutls-2.12.3/src/tests/.libs/rng-fork' finished with 0 errors
PASS: rng-fork
Self test `/Applications/sage/spkg/build/gnutls-2.12.3/src/tests/.libs/openssl' finished with 0 errors
PASS: openssl
server handshake Error in the push function. (-53) 
```

and then it hangs.  On OpenSolaris (David Kirkby's machine hawk):

```
  CC     test-vasnprintf.o
test-unistd.c:27:1: error: 'NULL' undeclared here (not in a function)
test-unistd.c:27:1: error: bit-field 'verify_error_if_negative_size__' width not an integer constant
test-unistd.c:30:14: error: 'SEEK_CUR' undeclared here (not in a function)
test-unistd.c:30:24: error: 'SEEK_END' undeclared here (not in a function)
test-unistd.c:30:34: error: 'SEEK_SET' undeclared here (not in a function)
test-unistd.c:35:9: error: expected '=', ',', ';', 'asm' or '__attribute__' before 'or'
test-unistd.c:40:9: error: expected '=', ',', ';', 'asm' or '__attribute__' before 't2'
test-unistd.c:45:7: error: expected '=', ',', ';', 'asm' or '__attribute__' before 't5'
test-unistd.c:46:7: error: expected '=', ',', ';', 'asm' or '__attribute__' before 't6'
  CC     test-vasprintf.o
make[7]: *** [test-unistd.o] Error 1
make[7]: *** Waiting for unfinished jobs....
make[7]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'
make[6]: *** [check-am] Error 2
make[6]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'
make[5]: *** [check-recursive] Error 1
make[5]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'
make[4]: *** [check] Error 2
make[4]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl/tests'
make[3]: *** [check-recursive] Error 1
make[3]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl'
make[2]: *** [check] Error 2
make[2]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib/gl'
make[1]: *** [check-recursive] Error 1
make[1]: Leaving directory `/export/home/palmieri/testing/sage-4.7.1.rc0/spkg/build/gnutls-2.12.3/src/lib'
make: *** [check-recursive] Error 1
An error occurred while testing GnuTLS
*************************************
Error testing package ** gnutls-2.12.3 **
*************************************
```



One more thing: `$RM` is no longer set by sage-env, so do you need to modify it in spkg-install?  If you do, should you test whether `$RM_SAVE` is nonempty before

```
RM=$RM_SAVE
export RM
```

Do you even need to export `RM` at the end, or are the changes in this script (in particular `unset RM`) just local to the script?



---

archive/issue_comments_100074.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-07-23T20:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100074",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_100075.json:
```json
{
    "body": "Ahem, restoring `RM` is useless since `spkg-install` never gets sourced. (`unset RM` is sufficient and ok.)\n\nSome things are still in, some are new:\n* `$SAGE_LOCAL` should be quoted in the first tests (both scripts).\n* `-m64` is still hard-coded.\n* `CFLAGS` and `CXXFLAGS` get overwritten when `SAGE64=yes`.\n* `sage-check` uses `make` instead of `$MAKE`.\n* If we have to `--disable-cxx` on MacOS X, why disable it on all platforms?\n* Error messages should start with `\"Error ...\"`, and perhaps be written to `stderr`. (It would then be better to redirect *all* messages to prevent them getting out of sync.)\n\n(Haven't yet looked at the whole spkg, just the attached patch.)",
    "created_at": "2011-07-24T00:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100075",
    "user": "@nexttime"
}
```

Ahem, restoring `RM` is useless since `spkg-install` never gets sourced. (`unset RM` is sufficient and ok.)

Some things are still in, some are new:
* `$SAGE_LOCAL` should be quoted in the first tests (both scripts).
* `-m64` is still hard-coded.
* `CFLAGS` and `CXXFLAGS` get overwritten when `SAGE64=yes`.
* `sage-check` uses `make` instead of `$MAKE`.
* If we have to `--disable-cxx` on MacOS X, why disable it on all platforms?
* Error messages should start with `"Error ..."`, and perhaps be written to `stderr`. (It would then be better to redirect *all* messages to prevent them getting out of sync.)

(Haven't yet looked at the whole spkg, just the attached patch.)



---

archive/issue_comments_100076.json:
```json
{
    "body": "P.S.:\n\nOld libraries should (if at all) only be deleted *after a successful build*.\n\nThe package apparently doesn't use (or even find) Sage's libgcrypt:\n\n```\n...\nchecking for libgcrypt... no\nconfigure: error: \n***\n*** Libgcrypt v1.4.0 or later was not found. You may want to get it from\n*** ftp://ftp.gnupg.org/gcrypt/libgcrypt/\n***\n    \nfailed to configure GNUTLS\n\nreal\t0m9.511s\nuser\t0m2.400s\nsys\t0m0.410s\nsage: An error occurred while installing gnutls-2.12.3\n...\n```\n",
    "created_at": "2011-07-24T00:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100076",
    "user": "@nexttime"
}
```

P.S.:

Old libraries should (if at all) only be deleted *after a successful build*.

The package apparently doesn't use (or even find) Sage's libgcrypt:

```
...
checking for libgcrypt... no
configure: error: 
***
*** Libgcrypt v1.4.0 or later was not found. You may want to get it from
*** ftp://ftp.gnupg.org/gcrypt/libgcrypt/
***
    
failed to configure GNUTLS

real	0m9.511s
user	0m2.400s
sys	0m0.410s
sage: An error occurred while installing gnutls-2.12.3
...
```




---

archive/issue_comments_100077.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> The package apparently doesn't use (or even find) Sage's libgcrypt [...]\n\nAutocrap...\n\nAccording to `configure --help`, it also takes a `--with-libgcrypt-prefix=...` option, which -- sad enough -- requires in addition `--with-libgcrypt`, but apparently doesn't work (at least in `configure` itself to detect `libgcrypt`, as the corresponding `gcc` command for `conftest.c` doesn't have any `-I`s and `-L`s).\n\nAdding\n\n```sh\nCPPFLAGS=\"-I$SAGE_LOCAL/include $CPPFLAGS\"\nCFLAGS=\"-I$SAGE_LOCAL/include $CFLAGS\" # It's safer to add it here, too.\nLDFLAGS=\"-L$SAGE_LOCAL/lib $LDFLAGS\"\n```\n\n(which *in general* one should do to make sure Sage's version of whatsoever gets picked up first) cures this, at the same time making `--with-libgcrypt-prefix` superfluous.\n\n\nRegarding the test suite, I get nice warnings during compilation (*\"cast to pointer from integer of different size\"*) and the following:\n\n```\n...\nAll 34 tests passed\n...\nAll 50 tests passed\n(1 test was not run)\n...\nvex amd64->IR: unhandled instruction bytes: 0x66 0xF 0x38 0x25 0xCA 0x48\n==13210== valgrind: Unrecognised instruction at address 0x4e88206.\n==13210== Your program just tried to execute an instruction that Valgrind\n==13210== did not recognise.  There are two possible reasons for this.\n==13210== 1. Your program has a bug and erroneously jumped to a non-code\n==13210==    location.  If you are running Memcheck and you just saw a\n==13210==    warning about a bad jump, it's probably your program's fault.\n==13210== 2. The instruction is legitimate but Valgrind doesn't handle it,\n==13210==    i.e. it's Valgrind's fault.  If you think this is the case or\n==13210==    you are not sure, please let us know and we'll try to fix it.\n==13210== Either way, Valgrind will now raise a SIGILL signal which will\n==13210== probably kill your program.\n==13210== \n==13210== Process terminating with default action of signal 4 (SIGILL)\n==13210==  Illegal opcode at address 0x4E88206\n==13210==    at 0x4E88206: _gnutls_x509_time2gtime (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)\n==13210==    by 0x4E88DDE: _gnutls_x509_get_time (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)\n==13210==    by 0x4E99A55: gnutls_x509_crt_print (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)\n==13210==    by 0x400F79: doit (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/chainverify)\n==13210==    by 0x401804: main (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/chainverify)\n/bin/bash: line 5: 13210 Illegal instruction     PKCS12FILE=./pkcs12-decode/client.p12 PKCS12PASSWORD=foobar PKCS12FILE_2=./pkcs12-decode/pkcs12_2certs.p12 PKCS12PASSWORD_2=\"\" EXEEXT= srcdir=\".\" valgrind -q ${dir}$tst\nFAIL: chainverify\n...\nvex amd64->IR: unhandled instruction bytes: 0x66 0xF 0x38 0x25 0xCA 0x48\n==13258== valgrind: Unrecognised instruction at address 0x4e88206.\n==13258== Your program just tried to execute an instruction that Valgrind\n==13258== did not recognise.  There are two possible reasons for this.\n==13258== 1. Your program has a bug and erroneously jumped to a non-code\n==13258==    location.  If you are running Memcheck and you just saw a\n==13258==    warning about a bad jump, it's probably your program's fault.\n==13258== 2. The instruction is legitimate but Valgrind doesn't handle it,\n==13258==    i.e. it's Valgrind's fault.  If you think this is the case or\n==13258==    you are not sure, please let us know and we'll try to fix it.\n==13258== Either way, Valgrind will now raise a SIGILL signal which will\n==13258== probably kill your program.\n==13258== \n==13258== Process terminating with default action of signal 4 (SIGILL)\n==13258==  Illegal opcode at address 0x4E88206\n==13258==    at 0x4E88206: _gnutls_x509_time2gtime (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)\n==13258==    by 0x4E88DDE: _gnutls_x509_get_time (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)\n==13258==    by 0x4E99A55: gnutls_x509_crt_print (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)\n==13258==    by 0x400BB1: doit (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/dn2)\n==13258==    by 0x401164: main (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/dn2)\n/bin/bash: line 5: 13258 Illegal instruction     PKCS12FILE=./pkcs12-decode/client.p12 PKCS12PASSWORD=foobar PKCS12FILE_2=./pkcs12-decode/pkcs12_2certs.p12 PKCS12PASSWORD_2=\"\" EXEEXT= srcdir=\".\" valgrind -q ${dir}$tst\nFAIL: dn2\n...\n2 of 44 tests failed\nPlease report to bug-gnutls@gnu.org\n...\nmake: *** [check-recursive] Error 1\nAn error occurred while testing GnuTLS\n*************************************\nError testing package ** gnutls-2.12.3 **\n*************************************\nsage: An error occurred while testing gnutls-2.12.3\n...\n```\n\nHaven't yet inspected that further. (This is with GCC 4.5.1 on a Core2, using `-march=native`).\n\n\nBtw., the attached spkg diff is not current.",
    "created_at": "2011-07-24T03:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100077",
    "user": "@nexttime"
}
```

Replying to [comment:4 leif]:
> The package apparently doesn't use (or even find) Sage's libgcrypt [...]

Autocrap...

According to `configure --help`, it also takes a `--with-libgcrypt-prefix=...` option, which -- sad enough -- requires in addition `--with-libgcrypt`, but apparently doesn't work (at least in `configure` itself to detect `libgcrypt`, as the corresponding `gcc` command for `conftest.c` doesn't have any `-I`s and `-L`s).

Adding

```sh
CPPFLAGS="-I$SAGE_LOCAL/include $CPPFLAGS"
CFLAGS="-I$SAGE_LOCAL/include $CFLAGS" # It's safer to add it here, too.
LDFLAGS="-L$SAGE_LOCAL/lib $LDFLAGS"
```

(which *in general* one should do to make sure Sage's version of whatsoever gets picked up first) cures this, at the same time making `--with-libgcrypt-prefix` superfluous.


Regarding the test suite, I get nice warnings during compilation (*"cast to pointer from integer of different size"*) and the following:

```
...
All 34 tests passed
...
All 50 tests passed
(1 test was not run)
...
vex amd64->IR: unhandled instruction bytes: 0x66 0xF 0x38 0x25 0xCA 0x48
==13210== valgrind: Unrecognised instruction at address 0x4e88206.
==13210== Your program just tried to execute an instruction that Valgrind
==13210== did not recognise.  There are two possible reasons for this.
==13210== 1. Your program has a bug and erroneously jumped to a non-code
==13210==    location.  If you are running Memcheck and you just saw a
==13210==    warning about a bad jump, it's probably your program's fault.
==13210== 2. The instruction is legitimate but Valgrind doesn't handle it,
==13210==    i.e. it's Valgrind's fault.  If you think this is the case or
==13210==    you are not sure, please let us know and we'll try to fix it.
==13210== Either way, Valgrind will now raise a SIGILL signal which will
==13210== probably kill your program.
==13210== 
==13210== Process terminating with default action of signal 4 (SIGILL)
==13210==  Illegal opcode at address 0x4E88206
==13210==    at 0x4E88206: _gnutls_x509_time2gtime (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)
==13210==    by 0x4E88DDE: _gnutls_x509_get_time (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)
==13210==    by 0x4E99A55: gnutls_x509_crt_print (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)
==13210==    by 0x400F79: doit (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/chainverify)
==13210==    by 0x401804: main (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/chainverify)
/bin/bash: line 5: 13210 Illegal instruction     PKCS12FILE=./pkcs12-decode/client.p12 PKCS12PASSWORD=foobar PKCS12FILE_2=./pkcs12-decode/pkcs12_2certs.p12 PKCS12PASSWORD_2="" EXEEXT= srcdir="." valgrind -q ${dir}$tst
FAIL: chainverify
...
vex amd64->IR: unhandled instruction bytes: 0x66 0xF 0x38 0x25 0xCA 0x48
==13258== valgrind: Unrecognised instruction at address 0x4e88206.
==13258== Your program just tried to execute an instruction that Valgrind
==13258== did not recognise.  There are two possible reasons for this.
==13258== 1. Your program has a bug and erroneously jumped to a non-code
==13258==    location.  If you are running Memcheck and you just saw a
==13258==    warning about a bad jump, it's probably your program's fault.
==13258== 2. The instruction is legitimate but Valgrind doesn't handle it,
==13258==    i.e. it's Valgrind's fault.  If you think this is the case or
==13258==    you are not sure, please let us know and we'll try to fix it.
==13258== Either way, Valgrind will now raise a SIGILL signal which will
==13258== probably kill your program.
==13258== 
==13258== Process terminating with default action of signal 4 (SIGILL)
==13258==  Illegal opcode at address 0x4E88206
==13258==    at 0x4E88206: _gnutls_x509_time2gtime (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)
==13258==    by 0x4E88DDE: _gnutls_x509_get_time (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)
==13258==    by 0x4E99A55: gnutls_x509_crt_print (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/lib/.libs/libgnutls.so.26.18.11)
==13258==    by 0x400BB1: doit (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/dn2)
==13258==    by 0x401164: main (in /tmp/Sage/sage-4.7.1.rc0-8664/spkg/build/gnutls-2.12.3/src/tests/dn2)
/bin/bash: line 5: 13258 Illegal instruction     PKCS12FILE=./pkcs12-decode/client.p12 PKCS12PASSWORD=foobar PKCS12FILE_2=./pkcs12-decode/pkcs12_2certs.p12 PKCS12PASSWORD_2="" EXEEXT= srcdir="." valgrind -q ${dir}$tst
FAIL: dn2
...
2 of 44 tests failed
Please report to bug-gnutls@gnu.org
...
make: *** [check-recursive] Error 1
An error occurred while testing GnuTLS
*************************************
Error testing package ** gnutls-2.12.3 **
*************************************
sage: An error occurred while testing gnutls-2.12.3
...
```

Haven't yet inspected that further. (This is with GCC 4.5.1 on a Core2, using `-march=native`).


Btw., the attached spkg diff is not current.



---

archive/issue_comments_100078.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> Regarding the test suite, I get [...] the following:\n\n```\n...\nvex amd64->IR: unhandled instruction bytes: 0x66 0xF 0x38 0x25 0xCA 0x48\n==13210== valgrind: Unrecognised instruction at address 0x4e88206.\n...\n```\n\n> Haven't yet inspected that further. (This is with GCC 4.5.1 on a Core2, using `-march=native`).\n\nAs expected, compiling with `-march=core2` (to which GCC is configured to default to for 64-bit builds anyway), even more tests get run and all pass, so this is just a Valgrind problem not recognizing some fancy instructions.\n\n\n\n\n> Btw., the attached spkg diff is not current.\n\nSorry, I think there I just confused something.\n\n\n\n\nJohn, to what does Dave's `gcc` default to?\n\nYou **might** have to add `-std=c99` (or `-std=gnu99`) or define `_POSIX_SOURCE` or alike to pull in the correct definitions from Solaris headers, but better ask Dave, as IMHO the inclusion of `unistd.h` itself already implies at least POSIX.1.",
    "created_at": "2011-07-24T04:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100078",
    "user": "@nexttime"
}
```

Replying to [comment:5 leif]:
> Regarding the test suite, I get [...] the following:

```
...
vex amd64->IR: unhandled instruction bytes: 0x66 0xF 0x38 0x25 0xCA 0x48
==13210== valgrind: Unrecognised instruction at address 0x4e88206.
...
```

> Haven't yet inspected that further. (This is with GCC 4.5.1 on a Core2, using `-march=native`).

As expected, compiling with `-march=core2` (to which GCC is configured to default to for 64-bit builds anyway), even more tests get run and all pass, so this is just a Valgrind problem not recognizing some fancy instructions.




> Btw., the attached spkg diff is not current.

Sorry, I think there I just confused something.




John, to what does Dave's `gcc` default to?

You **might** have to add `-std=c99` (or `-std=gnu99`) or define `_POSIX_SOURCE` or alike to pull in the correct definitions from Solaris headers, but better ask Dave, as IMHO the inclusion of `unistd.h` itself already implies at least POSIX.1.



---

archive/issue_comments_100079.json:
```json
{
    "body": "> John, to what does Dave's gcc default to?\n\n\n```\n$ gcc --version\ngcc (GCC) 4.5.0\n```\n\n\n(cc'ing Dave so he can answer other questions about hawk's setup)",
    "created_at": "2011-07-25T01:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100079",
    "user": "@jhpalmieri"
}
```

> John, to what does Dave's gcc default to?


```
$ gcc --version
gcc (GCC) 4.5.0
```


(cc'ing Dave so he can answer other questions about hawk's setup)



---

archive/issue_comments_100080.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> > John, to what does Dave's gcc default to?\n> \n\n```\n$ gcc --version\ngcc (GCC) 4.5.0\n```\n\n\nI rather meant the language standard, which I think unfortunately isn't shown by `gcc -v` (prints more than the version number), i.e. if it is an internal default on Solaris.\n\n`gcc -E -dM -x c /dev/null` prints all preprocessor definitions, piping it to `egrep -i \"std|ansi|iso|posix|gnu\"` selects (also) some standard-related ones.\n\nBut you may really try with e.g. `-D_POSIX_SOURCE`, `-std=iso9899:199409`, `-std=c99`  or `-std=gnu99` (in `CFLAGS`, perhaps also `CPPFLAGS`, but the latter shouldn't be necessary).\n\nOr, even better, search Solaris' `unistd.h` for suspicious `#if[def]`s... :-)\n\n\n\n\n> (cc'ing Dave so he can answer other questions about hawk's setup)\n\nDave opened this ticket. ;-)",
    "created_at": "2011-07-25T03:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100080",
    "user": "@nexttime"
}
```

Replying to [comment:7 jhpalmieri]:
> > John, to what does Dave's gcc default to?
> 

```
$ gcc --version
gcc (GCC) 4.5.0
```


I rather meant the language standard, which I think unfortunately isn't shown by `gcc -v` (prints more than the version number), i.e. if it is an internal default on Solaris.

`gcc -E -dM -x c /dev/null` prints all preprocessor definitions, piping it to `egrep -i "std|ansi|iso|posix|gnu"` selects (also) some standard-related ones.

But you may really try with e.g. `-D_POSIX_SOURCE`, `-std=iso9899:199409`, `-std=c99`  or `-std=gnu99` (in `CFLAGS`, perhaps also `CPPFLAGS`, but the latter shouldn't be necessary).

Or, even better, search Solaris' `unistd.h` for suspicious `#if[def]`s... :-)




> (cc'ing Dave so he can answer other questions about hawk's setup)

Dave opened this ticket. ;-)



---

archive/issue_comments_100081.json:
```json
{
    "body": "\n```\n$ gcc -E -dM -x c /dev/null | egrep -i \"std|ansi|iso|posix|gnu\"\n#define __GNUC_PATCHLEVEL__ 0\n#define __STDC_HOSTED__ 1\n#define __GNUC__ 4\n#define __GNUC_MINOR__ 5\n#define __GNUC_GNU_INLINE__ 1\n```\n\nI could try to search `unistd.h`, but I wouldn't know a suspicious `#if[def]` if it bit me.",
    "created_at": "2011-07-25T06:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100081",
    "user": "@jhpalmieri"
}
```


```
$ gcc -E -dM -x c /dev/null | egrep -i "std|ansi|iso|posix|gnu"
#define __GNUC_PATCHLEVEL__ 0
#define __STDC_HOSTED__ 1
#define __GNUC__ 4
#define __GNUC_MINOR__ 5
#define __GNUC_GNU_INLINE__ 1
```

I could try to search `unistd.h`, but I wouldn't know a suspicious `#if[def]` if it bit me.



---

archive/issue_comments_100082.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n\n```\n$ gcc -E -dM -x c /dev/null | egrep -i \"std|ansi|iso|posix|gnu\"\n#define __GNUC_PATCHLEVEL__ 0\n#define __STDC_HOSTED__ 1\n#define __GNUC__ 4\n#define __GNUC_MINOR__ 5\n#define __GNUC_GNU_INLINE__ 1\n```\n\n\nFunny, it does not\n\n```C\n#define __STDC__ 1\n```\n\nwhich might be the cause and a bug in GCC 4.5.0, so you could try adding `-D__STDC__` to `CFLAGS`.\n\n\n\n\nDid you try any of the `-std=...`?\n\nYou could also try just\n\n```sh\ngcc -std=gnu99 -E -dM -x c /dev/null | egrep -i \"std|ansi|iso|posix|gnu\"\n```\n\nand see if `__STDC__` gets defined then.\n\n\n\n\n> I could try to search `unistd.h`, but I wouldn't know a suspicious `#if[def]` if it bit me.\n\n:) You're not familiar with the C/C++ preprocessor?\n\nIt just adds a meta-level (all directives on lines starting with `#`) and has things like `define`, `undef`ine, `if` or `ifdef`inded-`elif`-`else`-`endif` and the usual expressions in `if`-conditions, and of course also `include`.\n\nYou usually have constructs like\n\n```C\n#ifdef __IMPORTANT_MACRO_SIGNALING_A_STANDARD__\n\n// define the constants and functions required by that standard\n\n#elif defined(__OTHER_IMPORTANT_STANDARD__) || defined(__SOMETHING_ELSE__)\n\n#include <file_that_accommodates_these.h>\n\n// perhaps other C declarations and macro definitions\n\n#else\n\n// perhaps define things that oppose the standard(s)\n\n#endif\n```\n\nin C header files like `unistd.h`, located in `/usr/include/` or `/usr/local/include/`.",
    "created_at": "2011-07-25T07:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100082",
    "user": "@nexttime"
}
```

Replying to [comment:9 jhpalmieri]:

```
$ gcc -E -dM -x c /dev/null | egrep -i "std|ansi|iso|posix|gnu"
#define __GNUC_PATCHLEVEL__ 0
#define __STDC_HOSTED__ 1
#define __GNUC__ 4
#define __GNUC_MINOR__ 5
#define __GNUC_GNU_INLINE__ 1
```


Funny, it does not

```C
#define __STDC__ 1
```

which might be the cause and a bug in GCC 4.5.0, so you could try adding `-D__STDC__` to `CFLAGS`.




Did you try any of the `-std=...`?

You could also try just

```sh
gcc -std=gnu99 -E -dM -x c /dev/null | egrep -i "std|ansi|iso|posix|gnu"
```

and see if `__STDC__` gets defined then.




> I could try to search `unistd.h`, but I wouldn't know a suspicious `#if[def]` if it bit me.

:) You're not familiar with the C/C++ preprocessor?

It just adds a meta-level (all directives on lines starting with `#`) and has things like `define`, `undef`ine, `if` or `ifdef`inded-`elif`-`else`-`endif` and the usual expressions in `if`-conditions, and of course also `include`.

You usually have constructs like

```C
#ifdef __IMPORTANT_MACRO_SIGNALING_A_STANDARD__

// define the constants and functions required by that standard

#elif defined(__OTHER_IMPORTANT_STANDARD__) || defined(__SOMETHING_ELSE__)

#include <file_that_accommodates_these.h>

// perhaps other C declarations and macro definitions

#else

// perhaps define things that oppose the standard(s)

#endif
```

in C header files like `unistd.h`, located in `/usr/include/` or `/usr/local/include/`.



---

archive/issue_comments_100083.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100083",
    "user": "@williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_100084.json:
```json
{
    "body": "GNUTLS is no longer part of Sage.",
    "created_at": "2012-10-05T09:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100084",
    "user": "@jdemeyer"
}
```

GNUTLS is no longer part of Sage.



---

archive/issue_comments_100085.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-10-05T09:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9974#issuecomment-100085",
    "user": "@jdemeyer"
}
```

Resolution: invalid
