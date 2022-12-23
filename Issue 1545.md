# Issue 1545: gmp 4.2.2: add #include <cstdio> in gmp.h

Issue created by migration from https://trac.sagemath.org/ticket/1545

Original creator: mabshoff

Original creation time: 2007-12-17 03:36:06

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


---

Comment by mabshoff created at 2008-04-15 20:33:04

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 20:33:04

This has been fixed in #2929.

Cheers,

Michael
