# Issue 479: linbox-20070814.spkg abuses [CPP|CXX|C]FLAGS in spkg-install

archive/issues_000479.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  cpernet drkirkby\n\nKeywords: LinBox\n\nHello,\n\nThe current LinBox package in Sage 2.8.2 has the following assignments in spkg-install\n\n\n```\nCFLAGS=\"$CFLAGS -fPIC -I\\\"$SAGE_LOCAL/include\\\" -I\\\"$SAGE_LOCAL/include/linbox\\\"-L\\\"$SAGE_LOCAL/lib\\\"\"\nCXXFLAGS=\"$CXXFLAGS -fPIC -I\\\"$SAGE_LOCAL/include\\\" -I\\\"$SAGE_LOCAL/include/linbox\\\"  -L\\\"$SAGE_LOCAL/lib\\\"\"\nCPPFLAGS=\"$CPPFLAGS  -I\\\"$SAGE_LOCAL/include/linbox\\\" -I\\\"$SAGE_LOCAL\\\"/include\"\n```\n\nbut uses the configure with the following options:\n\n```\n./configure --prefix=\"$SAGE_LOCAL\" --with-givaro=\"$SAGE_LOCAL\" --with-gmp=\"$SAGE_LOCAL\" --with-ntl=\"$SAGE_LOCAL\" $OPS --with-blas=\"$LINBOX_BLAS\"\n```\n\nThis is due to a bug in LinBox where for exmaple GMP_CFLAGS is not propagated down into the Makefiles (via Makefile.am). I have fixed this for the GMP and I assume that it is the same fix for NTL and Givaro. The GMP fix already made it into LinBox-20070814.spkg and I did verify on my systems that the right gmp selected during configure is also linked against. Once I have made the fixes for NTL and Givaro I will push those fixes toward LinBox upstream.\n\nCheers,\n\nMichael\n\nI \n\nIssue created by migration from https://trac.sagemath.org/ticket/479\n\n",
    "created_at": "2007-08-22T19:36:34Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "linbox-20070814.spkg abuses [CPP|CXX|C]FLAGS in spkg-install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/479",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  cpernet drkirkby

Keywords: LinBox

Hello,

The current LinBox package in Sage 2.8.2 has the following assignments in spkg-install


```
CFLAGS="$CFLAGS -fPIC -I\"$SAGE_LOCAL/include\" -I\"$SAGE_LOCAL/include/linbox\"-L\"$SAGE_LOCAL/lib\""
CXXFLAGS="$CXXFLAGS -fPIC -I\"$SAGE_LOCAL/include\" -I\"$SAGE_LOCAL/include/linbox\"  -L\"$SAGE_LOCAL/lib\""
CPPFLAGS="$CPPFLAGS  -I\"$SAGE_LOCAL/include/linbox\" -I\"$SAGE_LOCAL\"/include"
```

but uses the configure with the following options:

```
./configure --prefix="$SAGE_LOCAL" --with-givaro="$SAGE_LOCAL" --with-gmp="$SAGE_LOCAL" --with-ntl="$SAGE_LOCAL" $OPS --with-blas="$LINBOX_BLAS"
```

This is due to a bug in LinBox where for exmaple GMP_CFLAGS is not propagated down into the Makefiles (via Makefile.am). I have fixed this for the GMP and I assume that it is the same fix for NTL and Givaro. The GMP fix already made it into LinBox-20070814.spkg and I did verify on my systems that the right gmp selected during configure is also linked against. Once I have made the fixes for NTL and Givaro I will push those fixes toward LinBox upstream.

Cheers,

Michael

I 

Issue created by migration from https://trac.sagemath.org/ticket/479





---

archive/issue_comments_002384.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T19:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2384",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002385.json:
```json
{
    "body": "Just to confirm that this bug is still around, CCing Cl\u00e9ment :-)",
    "created_at": "2008-08-17T00:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2385",
    "user": "malb"
}
```

Just to confirm that this bug is still around, CCing Clément :-)



---

archive/issue_comments_002386.json:
```json
{
    "body": "Well, this should be trivial to fix. Any takers?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T09:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2386",
    "user": "mabshoff"
}
```

Well, this should be trivial to fix. Any takers?

Cheers,

Michael



---

archive/issue_comments_002387.json:
```json
{
    "body": "Has this one been addressed in the meantime, due to Kirkby's many helpful flag comments?",
    "created_at": "2009-12-30T04:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2387",
    "user": "kcrisman"
}
```

Has this one been addressed in the meantime, due to Kirkby's many helpful flag comments?



---

archive/issue_comments_002388.json:
```json
{
    "body": "linbox appears to have several errors. \n\n* #7058 \n* -m64  (a GNUism in itself) hard coded on only OS X, so it will not build 64-bit with Solaris. \n* The issues you mention here. \n* The fact -fPIC is a GNU specific flag. \n\nI'm a bit reluctant to go around editing any more spkg-install files, until we have in place a better system for dealing with the 64-bit issues which is not dependent on a particular platform or compiler. This spkg-install makes the assumption the only compiler is gcc (not true) and the only operating system on which one might want to force a 64-bit build is OS X (again not true). It was rather short-sighted the way this SAGE64 issue was handled. \n\nOnce there is a way of handling this better, I'll revise this. #7505 is needing review and will allow the compiler to be determined. Later I will add an updated version of sage-env, which will set the flags globally. But it needs #7505 to be integrated first. \n\nDave",
    "created_at": "2009-12-30T16:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2388",
    "user": "drkirkby"
}
```

linbox appears to have several errors. 

* #7058 
* -m64  (a GNUism in itself) hard coded on only OS X, so it will not build 64-bit with Solaris. 
* The issues you mention here. 
* The fact -fPIC is a GNU specific flag. 

I'm a bit reluctant to go around editing any more spkg-install files, until we have in place a better system for dealing with the 64-bit issues which is not dependent on a particular platform or compiler. This spkg-install makes the assumption the only compiler is gcc (not true) and the only operating system on which one might want to force a 64-bit build is OS X (again not true). It was rather short-sighted the way this SAGE64 issue was handled. 

Once there is a way of handling this better, I'll revise this. #7505 is needing review and will allow the compiler to be determined. Later I will add an updated version of sage-env, which will set the flags globally. But it needs #7505 to be integrated first. 

Dave



---

archive/issue_comments_002389.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T14:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2389",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_002390.json:
```json
{
    "body": "Fixed in #12762?",
    "created_at": "2015-04-13T14:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2390",
    "user": "mmezzarobba"
}
```

Fixed in #12762?



---

archive/issue_comments_002391.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-19T18:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2391",
    "user": "aapitzsch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_002392.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-19T08:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/479#issuecomment-2392",
    "user": "vbraun"
}
```

Resolution: fixed
