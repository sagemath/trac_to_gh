# Issue 5382: Update MPFR to 2.4.1 (security)

archive/issues_005382.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nAfter a buffer overflow has been found (and fixed) in the\nmpfr_snprintf and mpfr_vsnprintf functions of MPFR 2.4.0,\nit has been decided to release MPFR 2.4.1 immediately.\nIt is available for download from the MPFR web site:\n\n  http://www.mpfr.org/mpfr-2.4.1/\n\nThe MD5's:\n22402995cf2496d8faea42c8da02ce1f  mpfr-2.4.1.tar.lzma\nc5ee0a8ce82ad55fe29ac57edd35d09e  mpfr-2.4.1.tar.bz2\na70bbde2a23d82e8f3314d4293500ae4  mpfr-2.4.1.tar.gz\n63c1ebc19f720853c75e5bef22405490  mpfr-2.4.1.zip\n\nChanges from version 2.4.0 to version 2.4.1:\n- Security fix in mpfr_snprintf and mpfr_vsnprintf (buffer overflow).\n- Configure: new checks for length modifiers hh and ll (new in C99)\n  as hh is absent on alpha-OSF1-V5.\n- Miscellaneous corrections in the MPFR manual. In particular,\n  mpfr_inits, mpfr_inits2, mpfr_clears and MPFR_DECL_INIT have been\n  in the public API since MPFR 2.4.0.\n\nYou can send success and failure reports to <mpfr@loria.fr>, and give\nus the canonical system name as returned by the config.guess script,\nthe processor and compiler version, in order to complete the\n\"Platforms Known to Support MPFR\" section of the MPFR 2.4.1 web page.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5382\n\n",
    "created_at": "2009-02-26T04:15:10Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Update MPFR to 2.4.1 (security)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5382",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
After a buffer overflow has been found (and fixed) in the
mpfr_snprintf and mpfr_vsnprintf functions of MPFR 2.4.0,
it has been decided to release MPFR 2.4.1 immediately.
It is available for download from the MPFR web site:

  http://www.mpfr.org/mpfr-2.4.1/

The MD5's:
22402995cf2496d8faea42c8da02ce1f  mpfr-2.4.1.tar.lzma
c5ee0a8ce82ad55fe29ac57edd35d09e  mpfr-2.4.1.tar.bz2
a70bbde2a23d82e8f3314d4293500ae4  mpfr-2.4.1.tar.gz
63c1ebc19f720853c75e5bef22405490  mpfr-2.4.1.zip

Changes from version 2.4.0 to version 2.4.1:
- Security fix in mpfr_snprintf and mpfr_vsnprintf (buffer overflow).
- Configure: new checks for length modifiers hh and ll (new in C99)
  as hh is absent on alpha-OSF1-V5.
- Miscellaneous corrections in the MPFR manual. In particular,
  mpfr_inits, mpfr_inits2, mpfr_clears and MPFR_DECL_INIT have been
  in the public API since MPFR 2.4.0.

You can send success and failure reports to <mpfr@loria.fr>, and give
us the canonical system name as returned by the config.guess script,
the processor and compiler version, in order to complete the
"Platforms Known to Support MPFR" section of the MPFR 2.4.1 web page.
```


Issue created by migration from https://trac.sagemath.org/ticket/5382





---

archive/issue_comments_041453.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-26T04:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5382#issuecomment-41453",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041454.json:
```json
{
    "body": "The new spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/rc0/mpfr-2.4.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T23:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5382#issuecomment-41454",
    "user": "mabshoff"
}
```

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/rc0/mpfr-2.4.1.spkg

Cheers,

Michael



---

archive/issue_comments_041455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T23:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5382#issuecomment-41455",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041456.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T23:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5382#issuecomment-41456",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael
