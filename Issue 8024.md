# Issue 8024: Update prereq to check for Fortran compiler

archive/issues_008024.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  was\n\nPrior to 4.3.1.rc2, Sage included a Fortran compiler for Linux and OS X, so there was no need to have one. \n\nAs such, the 'prereq' script did not check for it. #7485 merged in sage-4.3.1.rc2 removed the Fortran compiler. \n\nIt would appear from at least one log posted\n\nhttp://sporadic.stanford.edu/bump/sage-4.3.1-errors\n\nthat despite gcc being built with Fortran support\n\n\n```\nConfigured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang \n--prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext \n--enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 \n--enable-clocale=gnu --enable-libstdcxx-debug \n--enable-objc-gc --enable-mpfr --enable-targets=all \n--enable-checking=release --build=i486-linux-gnu \n--host=i486-linux-gnu --target=i486-linux-gnu\n```\n\n\nFortran it is not installed on some Ubunta systems. As such, prereq should be modified to check for a Fortran compiler on every platform except OS X. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/8024\n\n",
    "created_at": "2010-01-21T12:05:49Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Update prereq to check for Fortran compiler",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8024",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  was

Prior to 4.3.1.rc2, Sage included a Fortran compiler for Linux and OS X, so there was no need to have one. 

As such, the 'prereq' script did not check for it. #7485 merged in sage-4.3.1.rc2 removed the Fortran compiler. 

It would appear from at least one log posted

http://sporadic.stanford.edu/bump/sage-4.3.1-errors

that despite gcc being built with Fortran support


```
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang 
--prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext 
--enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 
--enable-clocale=gnu --enable-libstdcxx-debug 
--enable-objc-gc --enable-mpfr --enable-targets=all 
--enable-checking=release --build=i486-linux-gnu 
--host=i486-linux-gnu --target=i486-linux-gnu
```


Fortran it is not installed on some Ubunta systems. As such, prereq should be modified to check for a Fortran compiler on every platform except OS X. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/8024





---

archive/issue_comments_070103.json:
```json
{
    "body": "Changing priority to critical, as William created a duplicate (#8026) and marked that as critical.",
    "created_at": "2010-01-24T22:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8024#issuecomment-70103",
    "user": "drkirkby"
}
```

Changing priority to critical, as William created a duplicate (#8026) and marked that as critical.



---

archive/issue_comments_070104.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-01-24T22:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8024#issuecomment-70104",
    "user": "drkirkby"
}
```

Changing priority from major to critical.



---

archive/issue_comments_070105.json:
```json
{
    "body": "#8026 is a duplicate of this, with one minor difference being this checks for a Fortran compiler, not gfortran.",
    "created_at": "2010-01-24T23:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8024#issuecomment-70105",
    "user": "drkirkby"
}
```

#8026 is a duplicate of this, with one minor difference being this checks for a Fortran compiler, not gfortran.



---

archive/issue_comments_070106.json:
```json
{
    "body": "This is solved by #8052, which currently needs review",
    "created_at": "2010-01-31T06:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8024#issuecomment-70106",
    "user": "drkirkby"
}
```

This is solved by #8052, which currently needs review



---

archive/issue_comments_070107.json:
```json
{
    "body": "Close as fixed by #8052.",
    "created_at": "2010-01-31T22:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8024#issuecomment-70107",
    "user": "mvngu"
}
```

Close as fixed by #8052.



---

archive/issue_comments_070108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-31T22:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8024#issuecomment-70108",
    "user": "mvngu"
}
```

Resolution: fixed
