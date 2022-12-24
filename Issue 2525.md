# Issue 2525: update Linbox to 1.1.5.rc3 upstream release

archive/issues_002525.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe upstream release contains plenty of bugfixes. Since the givaro.spkg at #2524 requires a bump anyway we might as well upgrade this too in unison.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2525\n\n",
    "created_at": "2008-03-15T01:56:12Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "update Linbox to 1.1.5.rc3 upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2525",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The upstream release contains plenty of bugfixes. Since the givaro.spkg at #2524 requires a bump anyway we might as well upgrade this too in unison.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2525





---

archive/issue_comments_017221.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-15T01:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2525#issuecomment-17221",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017222.json:
```json
{
    "body": "Diffing the current linbox directory in 1.1.5rc2 against 1.1.5.r2921 shows massive differences:\n\n```\nFiles linbox/aclocal.m4 and svn/linbox/aclocal.m4 differ\nOnly in linbox: a.out.dSYM\nOnly in svn/linbox/: autogen.sh\nOnly in svn/linbox/: autogen.status\nOnly in svn/linbox/: autom4te.cache\nOnly in svn/linbox/: CHANGED-INTERFACES\nFiles linbox/ChangeLog and svn/linbox/ChangeLog differ\nFiles linbox/config.guess and svn/linbox/config.guess differ\nOnly in svn/linbox/: config.log\nOnly in linbox: _configs.sed\nFiles linbox/config.sub and svn/linbox/config.sub differ\nFiles linbox/configure and svn/linbox/configure differ\nFiles linbox/configure.in and svn/linbox/configure.in differ\nOnly in svn/linbox/doc: install-1.0.html\nOnly in svn/linbox/doc: .iso-ent\nFiles linbox/doc/Makefile.in and svn/linbox/doc/Makefile.in differ\nOnly in svn/linbox/doc: organization\nOnly in svn/linbox/doc: .sedfile\nOnly in svn/linbox/doc: tex\nOnly in svn/linbox/examples: athadet.C\nOnly in svn/linbox/examples: bigmat.C\nOnly in svn/linbox/examples: blackbox\nOnly in svn/linbox/examples: data\nOnly in svn/linbox/examples: dense-det.C\nOnly in svn/linbox/examples: examples.doxy\nFiles linbox/examples/fields/Makefile.in and svn/linbox/examples/fields/Makefile.in differ\nOnly in svn/linbox/examples: integer-mul.C\nOnly in svn/linbox/examples: integers\nFiles linbox/examples/Makefile.in and svn/linbox/examples/Makefile.in differ\nOnly in svn/linbox/examples: makefile.mpi\nOnly in svn/linbox/examples: mpidet.C\nOnly in svn/linbox/examples: power_rank.C\nOnly in svn/linbox/examples: qchar.C\nOnly in svn/linbox/examples: samplebb.C\nOnly in svn/linbox/examples: solver\nFiles linbox/gmp++/Makefile.in and svn/linbox/gmp++/Makefile.in differ\nFiles linbox/INSTALL and svn/linbox/INSTALL differ\nFiles linbox/install-sh and svn/linbox/install-sh differ\nOnly in svn/linbox/interfaces/driver: compile-readme.txt\nFiles linbox/interfaces/driver/Makefile.in and svn/linbox/interfaces/driver/Makefile.in differ\nOnly in svn/linbox/interfaces: interfaces.dxx\nFiles linbox/interfaces/kaapi/Makefile.in and svn/linbox/interfaces/kaapi/Makefile.in differ\nFiles linbox/interfaces/Makefile.in and svn/linbox/interfaces/Makefile.in differ\nOnly in svn/linbox/interfaces/maple: lb-maple.mpl.bak\nOnly in svn/linbox/interfaces/maple: lb-maple-path.pl\nOnly in svn/linbox/interfaces/maple: lb-maple-path.sh\nOnly in svn/linbox/interfaces/maple: linbox-demonstration-good.mw\nOnly in svn/linbox/interfaces/maple: linbox-demonstration.mw\nFiles linbox/interfaces/maple/Makefile.in and svn/linbox/interfaces/maple/Makefile.in differ\nOnly in svn/linbox/interfaces: maple-old\nOnly in svn/linbox/: libtool\nFiles linbox/linbox/algorithms/block-massey-domain.h and svn/linbox/linbox/algorithms/block-massey-domain.h differ\nOnly in svn/linbox/linbox/algorithms: density.h\nFiles linbox/linbox/algorithms/Makefile.in and svn/linbox/linbox/algorithms/Makefile.in differ\nOnly in svn/linbox/linbox/algorithms: short-vector.h\nOnly in svn/linbox/linbox/blackbox: blackbox_parallel.h\nOnly in svn/linbox/linbox/blackbox: blackbox_thread.h\nFiles linbox/linbox/blackbox/Makefile.in and svn/linbox/linbox/blackbox/Makefile.in differ\nFiles linbox/linbox/blackbox/moore-penrose.h and svn/linbox/linbox/blackbox/moore-penrose.h differ\nOnly in svn/linbox/linbox/blackbox: quad-matrix.h\nOnly in svn/linbox/linbox/blackbox: subrowmatrix.h\nOnly in svn/linbox/linbox/blackbox: zo.h\nOnly in svn/linbox/linbox/blackbox: zoi.inl\nOnly in svn/linbox/linbox/blackbox: zo.inl\nFiles linbox/linbox/element/Makefile.in and svn/linbox/linbox/element/Makefile.in differ\nOnly in svn/linbox/linbox/fflas: fflas.dxx\nFiles linbox/linbox/fflas/Makefile.in and svn/linbox/linbox/fflas/Makefile.in differ\nFiles linbox/linbox/ffpack/ffpack_charpoly.inl and svn/linbox/linbox/ffpack/ffpack_charpoly.inl differ\nFiles linbox/linbox/ffpack/ffpack_frobenius.inl and svn/linbox/linbox/ffpack/ffpack_frobenius.inl differ\nFiles linbox/linbox/ffpack/ffpack.h and svn/linbox/linbox/ffpack/ffpack.h differ\nFiles linbox/linbox/ffpack/Makefile.in and svn/linbox/linbox/ffpack/Makefile.in differ\nFiles linbox/linbox/field/gmp-rational.h and svn/linbox/linbox/field/gmp-rational.h differ\nFiles linbox/linbox/field/Makefile.in and svn/linbox/linbox/field/Makefile.in differ\nOnly in svn/linbox/linbox: iterators\nOnly in linbox/linbox: linbox-config.h\nFiles linbox/linbox/Makefile.in and svn/linbox/linbox/Makefile.in differ\nFiles linbox/linbox/matrix/Makefile.in and svn/linbox/linbox/matrix/Makefile.in differ\nOnly in svn/linbox/linbox/matrix: matrix.dxx\nOnly in svn/linbox/linbox/randiter: archetype.dxx\nOnly in svn/linbox/linbox/randiter: generic.h\nFiles linbox/linbox/randiter/Makefile.in and svn/linbox/linbox/randiter/Makefile.in differ\nOnly in svn/linbox/linbox/randiter: randiter.dxx\nOnly in svn/linbox/linbox/randiter: randiter-wrappers.dxx\nOnly in svn/linbox/linbox/ring: gcd32.h\nOnly in svn/linbox/linbox/ring: gcd64.h\nFiles linbox/linbox/ring/Makefile.in and svn/linbox/linbox/ring/Makefile.in differ\nFiles linbox/linbox/solutions/charpoly.h and svn/linbox/linbox/solutions/charpoly.h differ\nFiles linbox/linbox/solutions/det.h and svn/linbox/linbox/solutions/det.h differ\nFiles linbox/linbox/solutions/getentry.h and svn/linbox/linbox/solutions/getentry.h differ\nFiles linbox/linbox/solutions/is-positive-definite.h and svn/linbox/linbox/solutions/is-positive-definite.h differ\nFiles linbox/linbox/solutions/is-positive-semidefinite.h and svn/linbox/linbox/solutions/is-positive-semidefinite.h differ\nFiles linbox/linbox/solutions/Makefile.in and svn/linbox/linbox/solutions/Makefile.in differ\nFiles linbox/linbox/switch/Makefile.in and svn/linbox/linbox/switch/Makefile.in differ\nOnly in svn/linbox/linbox/util: Attic\nFiles linbox/linbox/util/commentator.h and svn/linbox/linbox/util/commentator.h differ\nOnly in linbox/linbox/util: commentator.h~\nFiles linbox/linbox/util/formats/Makefile.in and svn/linbox/linbox/util/formats/Makefile.in differ\nOnly in svn/linbox/linbox/util/gmp++: gmp++.C\nFiles linbox/linbox/util/gmp++/Makefile.in and svn/linbox/linbox/util/gmp++/Makefile.in differ\nFiles linbox/linbox/util/Makefile.in and svn/linbox/linbox/util/Makefile.in differ\nFiles linbox/linbox/vector/Makefile.in and svn/linbox/linbox/vector/Makefile.in differ\nFiles linbox/ltmain.sh and svn/linbox/ltmain.sh differ\nOnly in svn/linbox/macros: autogen.sh\nFiles linbox/macros/Makefile.in and svn/linbox/macros/Makefile.in differ\nFiles linbox/Makefile.am and svn/linbox/Makefile.am differ\nFiles linbox/Makefile.in and svn/linbox/Makefile.in differ\nFiles linbox/missing and svn/linbox/missing differ\nOnly in svn/linbox/: RELEASE-INSTRUCTIONS\nOnly in svn/linbox/: .svnignore\nOnly in linbox/tests: 10\nOnly in svn/linbox/tests/data: gssv10-20\nOnly in svn/linbox/tests/data: gssv_rank_data\nFiles linbox/tests/data/Makefile.in and svn/linbox/tests/data/Makefile.in differ\nFiles linbox/tests/Makefile.in and svn/linbox/tests/Makefile.in differ\nOnly in svn/linbox/tests: Matio.h\nFiles linbox/tests/test-field.h and svn/linbox/tests/test-field.h differ\nOnly in svn/linbox/tests: test-fields.C\nFiles linbox/tests/test-givaro-zpz.C and svn/linbox/tests/test-givaro-zpz.C differ\nFiles linbox/tests/test-givaro-zpzuns.C and svn/linbox/tests/test-givaro-zpzuns.C differ\nOnly in svn/linbox/tests: test-image-field.C\nFiles linbox/tests/test-rational-solver-adaptive.C and svn/linbox/tests/test-rational-solver-adaptive.C differ\nFiles linbox/tests/test-rational-solver.C and svn/linbox/tests/test-rational-solver.C differ\nFiles linbox/tests/test-scalar-matrix.C and svn/linbox/tests/test-scalar-matrix.C differ\nOnly in svn/linbox/tests: tests.doxy\nOnly in svn/linbox/tests: tests.dxx\nFiles linbox/tests/test-smith-form-iliopoulos.C and svn/linbox/tests/test-smith-form-iliopoulos.C differ\nFiles linbox/tests/test-zero-one.C and svn/linbox/tests/test-zero-one.C differ\nOnly in svn/linbox/: TODO-1.1\n```\n\n\nIt seems that at least commentator.h has been modified to be totally disabled due to some bug that only hits on OSX PPC. So I am waiting for Clement to come back into IRC before attempting to fix this and clean up this mess.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T05:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2525#issuecomment-17222",
    "user": "mabshoff"
}
```

Diffing the current linbox directory in 1.1.5rc2 against 1.1.5.r2921 shows massive differences:

```
Files linbox/aclocal.m4 and svn/linbox/aclocal.m4 differ
Only in linbox: a.out.dSYM
Only in svn/linbox/: autogen.sh
Only in svn/linbox/: autogen.status
Only in svn/linbox/: autom4te.cache
Only in svn/linbox/: CHANGED-INTERFACES
Files linbox/ChangeLog and svn/linbox/ChangeLog differ
Files linbox/config.guess and svn/linbox/config.guess differ
Only in svn/linbox/: config.log
Only in linbox: _configs.sed
Files linbox/config.sub and svn/linbox/config.sub differ
Files linbox/configure and svn/linbox/configure differ
Files linbox/configure.in and svn/linbox/configure.in differ
Only in svn/linbox/doc: install-1.0.html
Only in svn/linbox/doc: .iso-ent
Files linbox/doc/Makefile.in and svn/linbox/doc/Makefile.in differ
Only in svn/linbox/doc: organization
Only in svn/linbox/doc: .sedfile
Only in svn/linbox/doc: tex
Only in svn/linbox/examples: athadet.C
Only in svn/linbox/examples: bigmat.C
Only in svn/linbox/examples: blackbox
Only in svn/linbox/examples: data
Only in svn/linbox/examples: dense-det.C
Only in svn/linbox/examples: examples.doxy
Files linbox/examples/fields/Makefile.in and svn/linbox/examples/fields/Makefile.in differ
Only in svn/linbox/examples: integer-mul.C
Only in svn/linbox/examples: integers
Files linbox/examples/Makefile.in and svn/linbox/examples/Makefile.in differ
Only in svn/linbox/examples: makefile.mpi
Only in svn/linbox/examples: mpidet.C
Only in svn/linbox/examples: power_rank.C
Only in svn/linbox/examples: qchar.C
Only in svn/linbox/examples: samplebb.C
Only in svn/linbox/examples: solver
Files linbox/gmp++/Makefile.in and svn/linbox/gmp++/Makefile.in differ
Files linbox/INSTALL and svn/linbox/INSTALL differ
Files linbox/install-sh and svn/linbox/install-sh differ
Only in svn/linbox/interfaces/driver: compile-readme.txt
Files linbox/interfaces/driver/Makefile.in and svn/linbox/interfaces/driver/Makefile.in differ
Only in svn/linbox/interfaces: interfaces.dxx
Files linbox/interfaces/kaapi/Makefile.in and svn/linbox/interfaces/kaapi/Makefile.in differ
Files linbox/interfaces/Makefile.in and svn/linbox/interfaces/Makefile.in differ
Only in svn/linbox/interfaces/maple: lb-maple.mpl.bak
Only in svn/linbox/interfaces/maple: lb-maple-path.pl
Only in svn/linbox/interfaces/maple: lb-maple-path.sh
Only in svn/linbox/interfaces/maple: linbox-demonstration-good.mw
Only in svn/linbox/interfaces/maple: linbox-demonstration.mw
Files linbox/interfaces/maple/Makefile.in and svn/linbox/interfaces/maple/Makefile.in differ
Only in svn/linbox/interfaces: maple-old
Only in svn/linbox/: libtool
Files linbox/linbox/algorithms/block-massey-domain.h and svn/linbox/linbox/algorithms/block-massey-domain.h differ
Only in svn/linbox/linbox/algorithms: density.h
Files linbox/linbox/algorithms/Makefile.in and svn/linbox/linbox/algorithms/Makefile.in differ
Only in svn/linbox/linbox/algorithms: short-vector.h
Only in svn/linbox/linbox/blackbox: blackbox_parallel.h
Only in svn/linbox/linbox/blackbox: blackbox_thread.h
Files linbox/linbox/blackbox/Makefile.in and svn/linbox/linbox/blackbox/Makefile.in differ
Files linbox/linbox/blackbox/moore-penrose.h and svn/linbox/linbox/blackbox/moore-penrose.h differ
Only in svn/linbox/linbox/blackbox: quad-matrix.h
Only in svn/linbox/linbox/blackbox: subrowmatrix.h
Only in svn/linbox/linbox/blackbox: zo.h
Only in svn/linbox/linbox/blackbox: zoi.inl
Only in svn/linbox/linbox/blackbox: zo.inl
Files linbox/linbox/element/Makefile.in and svn/linbox/linbox/element/Makefile.in differ
Only in svn/linbox/linbox/fflas: fflas.dxx
Files linbox/linbox/fflas/Makefile.in and svn/linbox/linbox/fflas/Makefile.in differ
Files linbox/linbox/ffpack/ffpack_charpoly.inl and svn/linbox/linbox/ffpack/ffpack_charpoly.inl differ
Files linbox/linbox/ffpack/ffpack_frobenius.inl and svn/linbox/linbox/ffpack/ffpack_frobenius.inl differ
Files linbox/linbox/ffpack/ffpack.h and svn/linbox/linbox/ffpack/ffpack.h differ
Files linbox/linbox/ffpack/Makefile.in and svn/linbox/linbox/ffpack/Makefile.in differ
Files linbox/linbox/field/gmp-rational.h and svn/linbox/linbox/field/gmp-rational.h differ
Files linbox/linbox/field/Makefile.in and svn/linbox/linbox/field/Makefile.in differ
Only in svn/linbox/linbox: iterators
Only in linbox/linbox: linbox-config.h
Files linbox/linbox/Makefile.in and svn/linbox/linbox/Makefile.in differ
Files linbox/linbox/matrix/Makefile.in and svn/linbox/linbox/matrix/Makefile.in differ
Only in svn/linbox/linbox/matrix: matrix.dxx
Only in svn/linbox/linbox/randiter: archetype.dxx
Only in svn/linbox/linbox/randiter: generic.h
Files linbox/linbox/randiter/Makefile.in and svn/linbox/linbox/randiter/Makefile.in differ
Only in svn/linbox/linbox/randiter: randiter.dxx
Only in svn/linbox/linbox/randiter: randiter-wrappers.dxx
Only in svn/linbox/linbox/ring: gcd32.h
Only in svn/linbox/linbox/ring: gcd64.h
Files linbox/linbox/ring/Makefile.in and svn/linbox/linbox/ring/Makefile.in differ
Files linbox/linbox/solutions/charpoly.h and svn/linbox/linbox/solutions/charpoly.h differ
Files linbox/linbox/solutions/det.h and svn/linbox/linbox/solutions/det.h differ
Files linbox/linbox/solutions/getentry.h and svn/linbox/linbox/solutions/getentry.h differ
Files linbox/linbox/solutions/is-positive-definite.h and svn/linbox/linbox/solutions/is-positive-definite.h differ
Files linbox/linbox/solutions/is-positive-semidefinite.h and svn/linbox/linbox/solutions/is-positive-semidefinite.h differ
Files linbox/linbox/solutions/Makefile.in and svn/linbox/linbox/solutions/Makefile.in differ
Files linbox/linbox/switch/Makefile.in and svn/linbox/linbox/switch/Makefile.in differ
Only in svn/linbox/linbox/util: Attic
Files linbox/linbox/util/commentator.h and svn/linbox/linbox/util/commentator.h differ
Only in linbox/linbox/util: commentator.h~
Files linbox/linbox/util/formats/Makefile.in and svn/linbox/linbox/util/formats/Makefile.in differ
Only in svn/linbox/linbox/util/gmp++: gmp++.C
Files linbox/linbox/util/gmp++/Makefile.in and svn/linbox/linbox/util/gmp++/Makefile.in differ
Files linbox/linbox/util/Makefile.in and svn/linbox/linbox/util/Makefile.in differ
Files linbox/linbox/vector/Makefile.in and svn/linbox/linbox/vector/Makefile.in differ
Files linbox/ltmain.sh and svn/linbox/ltmain.sh differ
Only in svn/linbox/macros: autogen.sh
Files linbox/macros/Makefile.in and svn/linbox/macros/Makefile.in differ
Files linbox/Makefile.am and svn/linbox/Makefile.am differ
Files linbox/Makefile.in and svn/linbox/Makefile.in differ
Files linbox/missing and svn/linbox/missing differ
Only in svn/linbox/: RELEASE-INSTRUCTIONS
Only in svn/linbox/: .svnignore
Only in linbox/tests: 10
Only in svn/linbox/tests/data: gssv10-20
Only in svn/linbox/tests/data: gssv_rank_data
Files linbox/tests/data/Makefile.in and svn/linbox/tests/data/Makefile.in differ
Files linbox/tests/Makefile.in and svn/linbox/tests/Makefile.in differ
Only in svn/linbox/tests: Matio.h
Files linbox/tests/test-field.h and svn/linbox/tests/test-field.h differ
Only in svn/linbox/tests: test-fields.C
Files linbox/tests/test-givaro-zpz.C and svn/linbox/tests/test-givaro-zpz.C differ
Files linbox/tests/test-givaro-zpzuns.C and svn/linbox/tests/test-givaro-zpzuns.C differ
Only in svn/linbox/tests: test-image-field.C
Files linbox/tests/test-rational-solver-adaptive.C and svn/linbox/tests/test-rational-solver-adaptive.C differ
Files linbox/tests/test-rational-solver.C and svn/linbox/tests/test-rational-solver.C differ
Files linbox/tests/test-scalar-matrix.C and svn/linbox/tests/test-scalar-matrix.C differ
Only in svn/linbox/tests: tests.doxy
Only in svn/linbox/tests: tests.dxx
Files linbox/tests/test-smith-form-iliopoulos.C and svn/linbox/tests/test-smith-form-iliopoulos.C differ
Files linbox/tests/test-zero-one.C and svn/linbox/tests/test-zero-one.C differ
Only in svn/linbox/: TODO-1.1
```


It seems that at least commentator.h has been modified to be totally disabled due to some bug that only hits on OSX PPC. So I am waiting for Clement to come back into IRC before attempting to fix this and clean up this mess.

Cheers,

Michael



---

archive/issue_comments_017223.json:
```json
{
    "body": "I created the new linbox-1.1.5.spkg from upstream linbox v1.1.5 (that I simultaneously officially released). So far, I have successfully tested it on my x86_32Linux box, sage-math, and my  PPC-OS-X box.\n\nThis should close #2453 as well. I tested it that and the bug is no longer showing up.\nI attach a patch reverting default minpoly/charpoly to linbox.",
    "created_at": "2008-04-04T00:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2525#issuecomment-17223",
    "user": "@ClementPernet"
}
```

I created the new linbox-1.1.5.spkg from upstream linbox v1.1.5 (that I simultaneously officially released). So far, I have successfully tested it on my x86_32Linux box, sage-math, and my  PPC-OS-X box.

This should close #2453 as well. I tested it that and the bug is no longer showing up.
I attach a patch reverting default minpoly/charpoly to linbox.



---

archive/issue_comments_017224.json:
```json
{
    "body": "Attachment [revert-charpoly-linbox-2453.patch](tarball://root/attachments/some-uuid/ticket2525/revert-charpoly-linbox-2453.patch) by @ClementPernet created at 2008-04-04 00:51:30",
    "created_at": "2008-04-04T00:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2525#issuecomment-17224",
    "user": "@ClementPernet"
}
```

Attachment [revert-charpoly-linbox-2453.patch](tarball://root/attachments/some-uuid/ticket2525/revert-charpoly-linbox-2453.patch) by @ClementPernet created at 2008-04-04 00:51:30



---

archive/issue_comments_017225.json:
```json
{
    "body": "Looks good to me, fixes the problem. Compiles. Doctests pass. This ticket fixes also #2453 and #2526.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T01:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2525#issuecomment-17225",
    "user": "mabshoff"
}
```

Looks good to me, fixes the problem. Compiles. Doctests pass. This ticket fixes also #2453 and #2526.

Cheers,

Michael



---

archive/issue_comments_017226.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-04T01:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2525#issuecomment-17226",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha0



---

archive/issue_comments_017227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T01:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2525#issuecomment-17227",
    "user": "mabshoff"
}
```

Resolution: fixed
