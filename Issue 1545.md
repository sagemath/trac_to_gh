# Issue 1545: gmp 4.2.2: add #include <cstdio> in gmp.h

archive/issues_001545.json:
```json
{
    "body": "Assignee: was\n\nRichard B. Kreckel suggested in http://gmplib.org/list-archives/gmp-bugs/2007-December/000892.html to add `#include cstdio>` to `gmp.h`:\n\n```\nHi Torbjorn!\n\nThere's this line in gmp.h.\n\nBut std::FILE hasn't been defined and with a conforming C++ compiler it \nwon't be unless <cstdio> has been included before <gmp.h>. Note that \nincluding <stdio.h> is not enough, as it doesn't define namespace std. \nSo, defined(__cplusplus) and including <stdio.h> is not enough to \nguarantee that std::FILE is known to the compiler.\n\nApparently, the intent is to avoid including stdio.h or cstdio. Why? I \nwould suggest including it.\n\nBesides, these using declarations are considered bad practice in header \nfiles. It would be better defining GMP_FILE or similar to either expand \nto FILE or std::FILE and use that instead of FILE.\n\nCheers\n   -richy.\n```\n\nI can only second that and we should do it per default since I have been bitten by this issue numerous times during the gcc 4.3 port. This should be during while doing #542 \"get gmp-4.2.2 into SAGE\"\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1545\n\n",
    "created_at": "2007-12-17T03:36:06Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "gmp 4.2.2: add #include <cstdio> in gmp.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1545",
    "user": "mabshoff"
}
```
Assignee: was

Richard B. Kreckel suggested in http://gmplib.org/list-archives/gmp-bugs/2007-December/000892.html to add `#include cstdio>` to `gmp.h`:

```
Hi Torbjorn!

There's this line in gmp.h.

But std::FILE hasn't been defined and with a conforming C++ compiler it 
won't be unless <cstdio> has been included before <gmp.h>. Note that 
including <stdio.h> is not enough, as it doesn't define namespace std. 
So, defined(__cplusplus) and including <stdio.h> is not enough to 
guarantee that std::FILE is known to the compiler.

Apparently, the intent is to avoid including stdio.h or cstdio. Why? I 
would suggest including it.

Besides, these using declarations are considered bad practice in header 
files. It would be better defining GMP_FILE or similar to either expand 
to FILE or std::FILE and use that instead of FILE.

Cheers
   -richy.
```

I can only second that and we should do it per default since I have been bitten by this issue numerous times during the gcc 4.3 port. This should be during while doing #542 "get gmp-4.2.2 into SAGE"

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1545





---

archive/issue_comments_009864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T20:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1545#issuecomment-9864",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009865.json:
```json
{
    "body": "This has been fixed in #2929.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T20:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1545#issuecomment-9865",
    "user": "mabshoff"
}
```

This has been fixed in #2929.

Cheers,

Michael
