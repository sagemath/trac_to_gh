# Issue 972: SAGE 2.8.8.1 blows up building cddlib if libgmp is in /usr/local/lib

archive/issues_000972.json:
```json
{
    "body": "Assignee: @williamstein\n\nI encountered this on Mac OS X (10.4.10), on a dual Quad Xeon system.  The build of cddlib-094b blows up here:\n\nThe build of cddlib-094b blows chunks, with this complaint:\n\ng++  -I /SandBox/Justin/sb/sage-2.8.8.1/local/include   -L/usr/local/lib -o scdd_gmp  simplecdd.o ../lib-src-gmp/libcddgmp.a -lgmp\n\nbecause of a separately-built libgmp there.\n\nThe error produces this complaint:\n/usr/bin/ld: Undefined symbols:\n___gmpq_add\n___gmpq_clear\n___gmpq_cmp\n___gmpq_div\n___gmpq_init\n___gmpq_mul\n___gmpq_set\n___gmpq_sub\n___gmpq_get_d\n___gmpq_set_den\n___gmpq_set_num\n___gmpq_set_si\n___gmpq_set_ui\n___gmpz_clear\n___gmpz_init\n___gmpz_set_si\n___gmpz_set_ui\n___gmpq_canonicalize\n___gmpq_get_den\n___gmpq_get_num\n___gmpz_cmp_ui\n___gmpz_init_set_str\n___gmpz_out_str\n___gmpz_set\n\nIssue created by migration from https://trac.sagemath.org/ticket/972\n\n",
    "created_at": "2007-10-23T04:57:34Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.14",
    "title": "SAGE 2.8.8.1 blows up building cddlib if libgmp is in /usr/local/lib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/972",
    "user": "justin"
}
```
Assignee: @williamstein

I encountered this on Mac OS X (10.4.10), on a dual Quad Xeon system.  The build of cddlib-094b blows up here:

The build of cddlib-094b blows chunks, with this complaint:

g++  -I /SandBox/Justin/sb/sage-2.8.8.1/local/include   -L/usr/local/lib -o scdd_gmp  simplecdd.o ../lib-src-gmp/libcddgmp.a -lgmp

because of a separately-built libgmp there.

The error produces this complaint:
/usr/bin/ld: Undefined symbols:
___gmpq_add
___gmpq_clear
___gmpq_cmp
___gmpq_div
___gmpq_init
___gmpq_mul
___gmpq_set
___gmpq_sub
___gmpq_get_d
___gmpq_set_den
___gmpq_set_num
___gmpq_set_si
___gmpq_set_ui
___gmpz_clear
___gmpz_init
___gmpz_set_si
___gmpz_set_ui
___gmpq_canonicalize
___gmpq_get_den
___gmpq_get_num
___gmpz_cmp_ui
___gmpz_init_set_str
___gmpz_out_str
___gmpz_set

Issue created by migration from https://trac.sagemath.org/ticket/972





---

archive/issue_comments_005929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-30T08:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/972#issuecomment-5929",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005930.json:
```json
{
    "body": "This was fixed in 2.8.14 by an updated cddlib.spkg.\n\nCheers,\n\nMichal",
    "created_at": "2007-11-30T08:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/972",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/972#issuecomment-5930",
    "user": "mabshoff"
}
```

This was fixed in 2.8.14 by an updated cddlib.spkg.

Cheers,

Michal
