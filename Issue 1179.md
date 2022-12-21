# Issue 1179: change all #!/bin/sh to #!/bin/bash in $SAGE_LOCAL/bin (Solaris related)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-15 16:28:49

Assignee: mabshoff

This is related to Solaris:

Klas writes:

```

I've tried started it from bash and tcsh, if that matters.
But please note that on Solaris /bin/sh is not bash, so
if scripts start with

#!/bin/sh

some things may not work as expected. 
```


On neron, i.e. William's Sun we replaced /bin/sh by /bin/bash because the original /bin/sh caused all kinds of problems during the build.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-15 16:28:59

Changing status from new to assigned.


---

Attachment

Looks good to me.


---

Comment by rlm created at 2007-12-02 03:59:55

Testall successful.


---

Comment by mabshoff created at 2007-12-02 04:10:02

Resolution: fixed
