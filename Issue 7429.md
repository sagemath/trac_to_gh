# Issue 7429: pari is misbuilt on OS X using xcode 3.2.1, making sage be mostly broken

archive/issues_007429.json:
```json
{
    "body": "Assignee: drkirkby\n\nAfter building sage on OS X 10.6.2 with Xcode 3.2.1 (all latest versions right now, and using #7426), PARI doesn't work, which causes massive failures all over the place:\n\n\n```\nPARI/GP is free software, covered by the GNU General Public License, and comes WITHOUT\nANY WARRANTY WHATSOEVER.\n\nType ? for help, \\q to quit.\nType ?12 for how to get moral (and possibly technical) support.\n\nparisize = 8000000, primelimit = 500000\n? polcoeff(1/eta(x)^2, 8, x)\ndyld: lazy symbol binding failed: Symbol not found: ___gmpn_mul_1\n  Referenced from: /Users/was/build/sage-4.2.1.alpha0/local/lib//libpari-gmp.dylib\n  Expected in: flat namespace\n\ndyld: Symbol not found: ___gmpn_mul_1\n  Referenced from: /Users/was/build/sage-4.2.1.alpha0/local/lib//libpari-gmp.dylib\n  Expected in: flat namespace\n\nsage: \n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7429\n\n",
    "created_at": "2009-11-11T17:38:54Z",
    "labels": [
        "porting",
        "blocker",
        "bug"
    ],
    "title": "pari is misbuilt on OS X using xcode 3.2.1, making sage be mostly broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7429",
    "user": "was"
}
```
Assignee: drkirkby

After building sage on OS X 10.6.2 with Xcode 3.2.1 (all latest versions right now, and using #7426), PARI doesn't work, which causes massive failures all over the place:


```
PARI/GP is free software, covered by the GNU General Public License, and comes WITHOUT
ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 8000000, primelimit = 500000
? polcoeff(1/eta(x)^2, 8, x)
dyld: lazy symbol binding failed: Symbol not found: ___gmpn_mul_1
  Referenced from: /Users/was/build/sage-4.2.1.alpha0/local/lib//libpari-gmp.dylib
  Expected in: flat namespace

dyld: Symbol not found: ___gmpn_mul_1
  Referenced from: /Users/was/build/sage-4.2.1.alpha0/local/lib//libpari-gmp.dylib
  Expected in: flat namespace

sage: 
```




Issue created by migration from https://trac.sagemath.org/ticket/7429





---

archive/issue_comments_062515.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-11T18:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7429#issuecomment-62515",
    "user": "was"
}
```

Resolution: invalid



---

archive/issue_comments_062516.json:
```json
{
    "body": "NOTE: I just forced a rebuild of PARI on my box and the above problem vanished.  I think I fixed #7426 but did not force a rebuild of PARI after applying that fix.  So fortunately this problem is invalid :-)",
    "created_at": "2009-11-11T18:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7429#issuecomment-62516",
    "user": "was"
}
```

NOTE: I just forced a rebuild of PARI on my box and the above problem vanished.  I think I fixed #7426 but did not force a rebuild of PARI after applying that fix.  So fortunately this problem is invalid :-)
