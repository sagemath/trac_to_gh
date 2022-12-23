# Issue 1060: fix flintqs compile on OSX 10.5

Issue created by migration from https://trac.sagemath.org/ticket/1060

Original creator: mabshoff

Original creation time: 2007-11-02 00:25:17

Assignee: mabshoff

The fix for flintqs is the same as for givaro, basically. To the file

```
    src/lanczos.c
```

add the following as the first line:

```
#include "sys/types.h"
```

Then it builds fine. 

-- William


---

Comment by mabshoff created at 2007-11-02 01:08:01

applied to 2.8.11.rc1 - via new flintqs-20070817.p0


---

Comment by mabshoff created at 2007-11-02 01:08:01

Resolution: fixed
