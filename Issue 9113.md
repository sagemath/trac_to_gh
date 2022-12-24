# Issue 9113: sage-4.4.3.alpha1 -lpng blocker issue

archive/issues_009113.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nOn OS X we have:\n\n\n```\nrunning build_ext\nbuilding 'sage.rings.polynomial.pbori' extension\ng++ -L/Users/was/build/sage-4.4.3.alpha1/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/rings/polynomial/pbori.o -L/Users/was/build/sage-4.4.3.alpha1/local//lib -lcsage -lpolybori -lpboriCudd -lgroebner -lgd -lpng -lm4ri -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/rings/polynomial/pbori.so\nld: library not found for -lpng\ncollect2: ld returned 1 exit status\nerror: command 'g++' failed with exit status 1\nsage: There was an error installing modified sage library code.\n\n\nreal    0m1.706s\nuser    0m1.187s\nsys     0m0.503s\nmake: *** [testlong] Error 1\n```\n\n\nThis was caused by some patch to get Sage to build on Cygwin.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9113\n\n",
    "created_at": "2010-06-02T02:21:57Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-4.4.3.alpha1 -lpng blocker issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9113",
    "user": "@williamstein"
}
```
Assignee: GeorgSWeber

On OS X we have:


```
running build_ext
building 'sage.rings.polynomial.pbori' extension
g++ -L/Users/was/build/sage-4.4.3.alpha1/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/rings/polynomial/pbori.o -L/Users/was/build/sage-4.4.3.alpha1/local//lib -lcsage -lpolybori -lpboriCudd -lgroebner -lgd -lpng -lm4ri -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/rings/polynomial/pbori.so
ld: library not found for -lpng
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.


real    0m1.706s
user    0m1.187s
sys     0m0.503s
make: *** [testlong] Error 1
```


This was caused by some patch to get Sage to build on Cygwin.

Issue created by migration from https://trac.sagemath.org/ticket/9113





---

archive/issue_comments_084792.json:
```json
{
    "body": "This is due to #8844.  We should replace the include of \"-lpng\" with a uname_specific command to use \"png12\" where needed.",
    "created_at": "2010-06-02T02:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9113#issuecomment-84792",
    "user": "@mwhansen"
}
```

This is due to #8844.  We should replace the include of "-lpng" with a uname_specific command to use "png12" where needed.



---

archive/issue_comments_084793.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-03T04:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9113#issuecomment-84793",
    "user": "@williamstein"
}
```

Resolution: duplicate



---

archive/issue_comments_084794.json:
```json
{
    "body": "I made a dupe of this: #9116",
    "created_at": "2010-06-03T04:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9113#issuecomment-84794",
    "user": "@williamstein"
}
```

I made a dupe of this: #9116
