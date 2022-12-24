# Issue 452: multi_polynomial_libsingular.c doesn't compile on Solaris

archive/issues_000452.json:
```json
{
    "body": "Assignee: @malb\n\nthe compilation fails complaining about OSTREAM:\n\n> gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -\n> fPIC -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular\n> -I/extra/home/mabshoff/SAGE-build/sage-2.8/local//include -I/extra/\n> home/mabshoff/SAGE-build/sage-2.8/local//include/python -I/extra/home/\n> mabshoff/SAGE-build/sage-2.8/devel//sage/sage/ext -I/extra/home/\n> mabshoff/SAGE-build/sage-2.8/local/include/python2.5 -c sage/rings/\n> polynomial/multi_polynomial_libsingular.cpp -o build/temp.solaris-2.9-\n> sun4u-2.5/sage/rings/polynomial/multi_polynomial_libsingular.o -w\n> cc1plus: warning: command line option \"-Wstrict-prototypes\" is valid\n> for Ada/C/ObjC but not for C++\n> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/factory.h:43,\n>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/interrupt.h:6,\n>                  from sage/rings/polynomial/\n> multi_polynomial_libsingular.cpp:30:\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_array.h:38: error: 'OSTREAM' has not been declared\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_array.h:44: error: expected constructor, destructor, or type\n> conversion before '&' token\n> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/factory.h:44,\n>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/interrupt.h:6,\n>                  from sage/rings/polynomial/\n> multi_polynomial_libsingular.cpp:30:\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_factor.h:40: error: 'OSTREAM' has not been declared\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_factor.h:49: error: expected constructor, destructor, or type\n> conversion before '&' token\n> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/factory.h:45,\n>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/interrupt.h:6,\n>                  from sage/rings/polynomial/\n> multi_polynomial_libsingular.cpp:30:\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_list.h:27: error: expected constructor, destructor, or type\n> conversion before '&' token\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_list.h:47: error: 'OSTREAM' has not been declared\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_list.h:78: error: 'OSTREAM' has not been declared\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_list.h:79: error: ISO C++ forbids declaration of 'OSTREAM' with\n> no type\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_list.h:79: error: 'OSTREAM' is neither function nor member\n> function; cannot be declared friend\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_list.h:79: error: expected ';' before '&' token\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_list.h:86: error: expected constructor, destructor, or type\n> conversion before '&' token\n> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/factory.h:46,\n>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/interrupt.h:6,\n>                  from sage/rings/polynomial/\n> multi_polynomial_libsingular.cpp:30:\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_matrix.h:27: error: expected constructor, destructor, or type\n> conversion before '&' token\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_matrix.h:37: error: 'OSTREAM' has not been declared\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_matrix.h:57: error: 'OSTREAM' has not been declared\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_matrix.h:58: error: ISO C++ forbids declaration of 'OSTREAM'\n> with no type\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_matrix.h:58: error: 'OSTREAM' is neither function nor member\n> function; cannot be declared friend\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_matrix.h:58: error: expected ';' before '&' token\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/\n> ftmpl_matrix.h:93: error: expected constructor, destructor, or type\n> conversion before '&' token\n> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/tmpl_inst.h:8,\n>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/\n> include/singular/interrupt.h:8,\n>                  from sage/rings/polynomial/\n> multi_polynomial_libsingular.cpp:30:\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/\n> class.h:43: error: 'OSTREAM' has not been declared\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/\n> class.h:44: error: ISO C++ forbids declaration of 'OSTREAM' with no\n> type\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/\n> class.h:44: error: 'OSTREAM' is neither function nor member function;\n> cannot be declared friend\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/\n> class.h:44: error: expected ';' before '&' token\n> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/\n> class.h:50: error: expected `;' before '}' token\n> error: command 'gcc' failed with exit status 1\n> sage: There was an error installing modified sage library code.\n\n\n\nYou can build libCF with and without IO support and apparently this got mixed\nup. This is why we build a stand-alone libCF/libfac after we built SINGULAR\nand libSINGULAR. This way we make sure OSTREAM is known properly. Short\nanswer: I'll have look at it.\n\nMartin \n\nIssue created by migration from https://trac.sagemath.org/ticket/452\n\n",
    "created_at": "2007-08-19T08:03:45Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "multi_polynomial_libsingular.c doesn't compile on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/452",
    "user": "mabshoff"
}
```
Assignee: @malb

the compilation fails complaining about OSTREAM:

> gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -
> fPIC -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular
> -I/extra/home/mabshoff/SAGE-build/sage-2.8/local//include -I/extra/
> home/mabshoff/SAGE-build/sage-2.8/local//include/python -I/extra/home/
> mabshoff/SAGE-build/sage-2.8/devel//sage/sage/ext -I/extra/home/
> mabshoff/SAGE-build/sage-2.8/local/include/python2.5 -c sage/rings/
> polynomial/multi_polynomial_libsingular.cpp -o build/temp.solaris-2.9-
> sun4u-2.5/sage/rings/polynomial/multi_polynomial_libsingular.o -w
> cc1plus: warning: command line option "-Wstrict-prototypes" is valid
> for Ada/C/ObjC but not for C++
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:43,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_array.h:38: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_array.h:44: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:44,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_factor.h:40: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_factor.h:49: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:45,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:27: error: expected constructor, destructor, or type
> conversion before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:47: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:78: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:79: error: ISO C++ forbids declaration of 'OSTREAM' with
> no type
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:79: error: 'OSTREAM' is neither function nor member
> function; cannot be declared friend
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:79: error: expected ';' before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:86: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:46,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:27: error: expected constructor, destructor, or type
> conversion before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:37: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:57: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:58: error: ISO C++ forbids declaration of 'OSTREAM'
> with no type
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:58: error: 'OSTREAM' is neither function nor member
> function; cannot be declared friend
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:58: error: expected ';' before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:93: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/tmpl_inst.h:8,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:8,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:43: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:44: error: ISO C++ forbids declaration of 'OSTREAM' with no
> type
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:44: error: 'OSTREAM' is neither function nor member function;
> cannot be declared friend
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:44: error: expected ';' before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:50: error: expected `;' before '}' token
> error: command 'gcc' failed with exit status 1
> sage: There was an error installing modified sage library code.



You can build libCF with and without IO support and apparently this got mixed
up. This is why we build a stand-alone libCF/libfac after we built SINGULAR
and libSINGULAR. This way we make sure OSTREAM is known properly. Short
answer: I'll have look at it.

Martin 

Issue created by migration from https://trac.sagemath.org/ticket/452





---

archive/issue_comments_002252.json:
```json
{
    "body": "Fixed by Martin Albrecht in  Singular-20070819p2.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-21T15:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/452#issuecomment-2252",
    "user": "mabshoff"
}
```

Fixed by Martin Albrecht in  Singular-20070819p2.

Cheers,

Michael



---

archive/issue_comments_002253.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-21T15:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/452#issuecomment-2253",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002254.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-08-22T02:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/452#issuecomment-2254",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002255.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-22T02:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/452#issuecomment-2255",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002256.json:
```json
{
    "body": "Unfortunately, that new package breaks compilation on OSX and/or Linux. William has revered back to some former version of the spkg, so let's reopen this and target it at 2.8.3 and hope that it will be all sorted out be by then.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-22T02:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/452#issuecomment-2256",
    "user": "mabshoff"
}
```

Unfortunately, that new package breaks compilation on OSX and/or Linux. William has revered back to some former version of the spkg, so let's reopen this and target it at 2.8.3 and hope that it will be all sorted out be by then.

Cheers,

Michael



---

archive/issue_comments_002257.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-30T00:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/452#issuecomment-2257",
    "user": "@williamstein"
}
```

Resolution: fixed
