# Issue 3232: wrap NTL's BKZ

archive/issues_003232.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe BKZ algorithm is a lattice reduction algorithm AFAIK only implemented in NTL. \n\n\n```\n  -- BKZ: Block Korkin-Zolotarev reduction.\n     This is slower, but yields a higher-quality basis,\n     i.e., one with shorter vectors.\n     See the Schnorr-Euchner paper for a description of this.\n     This basically generalizes the LLL reduction condition\n     from blocks of size 2 to blocks of larger size.\n```\n\n\nIt enjoys more widespread use in cryptography these days and possibly other areas. Since Sage has Damien Stehle's fast fpLLL library and NTL's BKZ this would make Sage a very nice tool for people who care about these algorithms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3232\n\n",
    "created_at": "2008-05-16T23:18:54Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "wrap NTL's BKZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3232",
    "user": "@malb"
}
```
Assignee: @williamstein

The BKZ algorithm is a lattice reduction algorithm AFAIK only implemented in NTL. 


```
  -- BKZ: Block Korkin-Zolotarev reduction.
     This is slower, but yields a higher-quality basis,
     i.e., one with shorter vectors.
     See the Schnorr-Euchner paper for a description of this.
     This basically generalizes the LLL reduction condition
     from blocks of size 2 to blocks of larger size.
```


It enjoys more widespread use in cryptography these days and possibly other areas. Since Sage has Damien Stehle's fast fpLLL library and NTL's BKZ this would make Sage a very nice tool for people who care about these algorithms.

Issue created by migration from https://trac.sagemath.org/ticket/3232





---

archive/issue_comments_022390.json:
```json
{
    "body": "The attached patch wraps the appropriate NTL functions. It has doctests for all new methods. However, someone more familiar with BKZ might want to add an example (possibly #long) which showcases the difference between LLL and BKZ.",
    "created_at": "2008-05-25T20:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22390",
    "user": "@malb"
}
```

The attached patch wraps the appropriate NTL functions. It has doctests for all new methods. However, someone more familiar with BKZ might want to add an example (possibly #long) which showcases the difference between LLL and BKZ.



---

archive/issue_comments_022391.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_malb\".",
    "created_at": "2008-06-15T21:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22391",
    "user": "@craigcitro"
}
```

Changing keywords from "" to "editor_malb".



---

archive/issue_comments_022392.json:
```json
{
    "body": "Ralf forwarded the review request to a colleague of his. I'll ping him again by the end of the week to see what happened.",
    "created_at": "2008-06-16T03:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22392",
    "user": "@malb"
}
```

Ralf forwarded the review request to a colleague of his. I'll ping him again by the end of the week to see what happened.



---

archive/issue_comments_022393.json:
```json
{
    "body": "Ralf, can you review the patch without the forwarding which now seems pointless?",
    "created_at": "2008-06-22T17:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22393",
    "user": "@malb"
}
```

Ralf, can you review the patch without the forwarding which now seems pointless?



---

archive/issue_comments_022394.json:
```json
{
    "body": "**state of affairs for editorial meeting 26/06/08**\n\nI didn't hear back from rpw yet. Maybe another referee could jump in.",
    "created_at": "2008-06-25T11:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22394",
    "user": "@malb"
}
```

**state of affairs for editorial meeting 26/06/08**

I didn't hear back from rpw yet. Maybe another referee could jump in.



---

archive/issue_comments_022395.json:
```json
{
    "body": "Attachment [ntru_2_47.sage](tarball://root/attachments/some-uuid/ticket3232/ntru_2_47.sage) by rpw created at 2008-07-07 23:12:17\n\nNTRU derived lattice, n=47",
    "created_at": "2008-07-07T23:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22395",
    "user": "rpw"
}
```

Attachment [ntru_2_47.sage](tarball://root/attachments/some-uuid/ticket3232/ntru_2_47.sage) by rpw created at 2008-07-07 23:12:17

NTRU derived lattice, n=47



---

archive/issue_comments_022396.json:
```json
{
    "body": "Patch applied against SAGE 3.0.3. Works fine, doctests OK. Successfully tested on some cryptographically relevant toy sample lattices (NTRU derived, one is attached, provided by Markus R\u00fcckert).\n\nTwo typos found in documentation: \n* permuation -> permutation\n* Gramm-Schmidt -> Gram-Schmidt",
    "created_at": "2008-07-07T23:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22396",
    "user": "rpw"
}
```

Patch applied against SAGE 3.0.3. Works fine, doctests OK. Successfully tested on some cryptographically relevant toy sample lattices (NTRU derived, one is attached, provided by Markus Rückert).

Two typos found in documentation: 
* permuation -> permutation
* Gramm-Schmidt -> Gram-Schmidt



---

archive/issue_comments_022397.json:
```json
{
    "body": "w00t, I'll fix the typos today-ish.",
    "created_at": "2008-07-08T08:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22397",
    "user": "@malb"
}
```

w00t, I'll fix the typos today-ish.



---

archive/issue_comments_022398.json:
```json
{
    "body": "To highlight BKZ's features here is a Sage session for the NTRU example rpw provided:\n\n```\nsage: M = eval(open(\"ntru_2_47.sage\").read()[4:])\nsage: M\n94 x 94 dense matrix over Integer Ring\n\nsage: %time M_BKZ = M.BKZ()\nCPU times: user 17.64 s, sys: 0.03 s, total: 17.67 s\nWall time: 17.98 s\n\nsage: %time M_LLL = M.LLL()\nCPU times: user 0.30 s, sys: 0.00 s, total: 0.30 s\nWall time: 0.30 s\n\nsage: %time M_LLL_NTL = M.LLL(algorithm=\"NTL:LLL\")\nCPU times: user 0.11 s, sys: 0.01 s, total: 0.12 s\nWall time: 0.16 s\n\nsage: sqrt(sum([ a^2 for a in M_BKZ[0] ])).n()\n10.1488915650922\n\nsage: sqrt(sum([ a^2 for a in M_LLL[0] ])).n()\n23.0000000000000\n\nsage: sqrt(sum([ a^2 for a in M_LLL_NTL[0] ])).n()\n23.0000000000000\n\nsage: sqrt(sum([ a^2 for a in M_BKZ[93] ])).n()\n20.7364413533277\n\nsage: sqrt(sum([ a^2 for a in M_LLL[93] ])).n()\n43.0116263352131\n\nsage: sqrt(sum([ a^2 for a in M_LLL_NTL[93] ])).n()\n47.6340214552582\n```\n",
    "created_at": "2008-07-08T11:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22398",
    "user": "@malb"
}
```

To highlight BKZ's features here is a Sage session for the NTRU example rpw provided:

```
sage: M = eval(open("ntru_2_47.sage").read()[4:])
sage: M
94 x 94 dense matrix over Integer Ring

sage: %time M_BKZ = M.BKZ()
CPU times: user 17.64 s, sys: 0.03 s, total: 17.67 s
Wall time: 17.98 s

sage: %time M_LLL = M.LLL()
CPU times: user 0.30 s, sys: 0.00 s, total: 0.30 s
Wall time: 0.30 s

sage: %time M_LLL_NTL = M.LLL(algorithm="NTL:LLL")
CPU times: user 0.11 s, sys: 0.01 s, total: 0.12 s
Wall time: 0.16 s

sage: sqrt(sum([ a^2 for a in M_BKZ[0] ])).n()
10.1488915650922

sage: sqrt(sum([ a^2 for a in M_LLL[0] ])).n()
23.0000000000000

sage: sqrt(sum([ a^2 for a in M_LLL_NTL[0] ])).n()
23.0000000000000

sage: sqrt(sum([ a^2 for a in M_BKZ[93] ])).n()
20.7364413533277

sage: sqrt(sum([ a^2 for a in M_LLL[93] ])).n()
43.0116263352131

sage: sqrt(sum([ a^2 for a in M_LLL_NTL[93] ])).n()
47.6340214552582
```




---

archive/issue_comments_022399.json:
```json
{
    "body": "addresses rpw's review",
    "created_at": "2008-07-08T11:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22399",
    "user": "@malb"
}
```

addresses rpw's review



---

archive/issue_comments_022400.json:
```json
{
    "body": "Attachment [bkz.patch](tarball://root/attachments/some-uuid/ticket3232/bkz.patch) by @malb created at 2008-07-08 11:55:28\n\nTypos fixed in updated patch, apply `bkz.patch` only.",
    "created_at": "2008-07-08T11:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22400",
    "user": "@malb"
}
```

Attachment [bkz.patch](tarball://root/attachments/some-uuid/ticket3232/bkz.patch) by @malb created at 2008-07-08 11:55:28

Typos fixed in updated patch, apply `bkz.patch` only.



---

archive/issue_comments_022401.json:
```json
{
    "body": "Merged bkz.patch in Sage 3.0.6.alpha0",
    "created_at": "2008-07-15T03:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22401",
    "user": "mabshoff"
}
```

Merged bkz.patch in Sage 3.0.6.alpha0



---

archive/issue_comments_022402.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-15T03:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3232#issuecomment-22402",
    "user": "mabshoff"
}
```

Resolution: fixed
