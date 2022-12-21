# Issue 4125: Build breaks entirely or pulls in non-standard libraries with fink and macports

Issue created by migration from Trac.

Original creator: dphilp

Original creation time: 2008-09-15 01:53:19

Assignee: mabshoff

CC:  dphilp

The Sage build process pulls in non-standard libraries if they are easily found.  Fink and MacPorts have a habit of making their libraries easily found, because they fiddle with $PATH, etc.  This sometimes means that the build fails, or works, but the resulting product is broken.  

The fix is simple: move /sw and /opt/local during the build process.  However, this is not at all obvious the first time.  This script runs a simple test to check whether fink or ports are likely to interfere, and gives a useful error message.

{{{#!/bin/bash

# Try to find ports automatically.
PORTS_PATH=`which port`

# Try to find fink automatically.
FINK_PATH=`which fink`

if [ "$PORTS_PATH" -o "$FINK_PATH" ] ; then
  echo "Found either MacPorts or Fink in your path, which often prevents Sage from compiling."
  if [ "$SAGE_COMPILE_DESPITE_PORTS_AND_FINK" ] ; then
    echo "Continuing because SAGE_COMPILE_DESPITE_PORTS_AND_FINK is set."
  else
    echo "If you want to want to compile, you should rename /opt/local and /sw"
    echo "during the build process.  (Once Sage is built, you can move them to"
    echo "their original location.)"
    exit 1
  fi
fi
```



---

Attachment


---

Comment by rlm created at 2008-09-15 02:31:35

Looks good to me!


---

Comment by mabshoff created at 2008-09-15 02:49:14

Resolution: fixed


---

Comment by mabshoff created at 2008-09-15 02:49:14

Merged in Sage 3.1.2.rc4


---

Comment by mhampton created at 2008-09-15 14:47:56

This doesn't work for me: I don't have macports or fink and it kills my build.


---

Comment by GeorgSWeber created at 2008-10-06 19:23:12

Resolution changed from fixed to 


---

Comment by GeorgSWeber created at 2008-10-06 19:23:12

Negative review, please revert the patch.

It breaks age builds that otherwise went fine, thus is a "false negative", e.g. for mhampton as reported above, or for David Harvey, as reported in the sage-devel discussion "macports" on Oct. 5th., see there for more (negative) opinions.

On the other hand, the patch might has become superfluous by patch 4127, but that should be confirmed by others.

If not, probably it is best to enhance 4127 until that one works as desired.

So please revert the patch of this ticket and then close the ticket as "wont", or better, as a "doublette" to 4127.


---

Comment by GeorgSWeber created at 2008-10-06 19:23:12

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-10-07 11:56:46

Resolution: fixed


---

Comment by mabshoff created at 2008-10-07 11:56:46

Replying to [comment:5 GeorgSWeber]:
> Negative review, please revert the patch.
> 
> It breaks age builds that otherwise went fine, thus is a "false negative", e.g. for mhampton as reported above, or for David Harvey, as reported in the sage-devel discussion "macports" on Oct. 5th., see there for more (negative) opinions.

I do not care. This ticket resolves numerous problems where in the end after *much* debugging it turned out that either MacPorts or Fink was at fault. 

> On the other hand, the patch might has become superfluous by patch 4127, but that should be confirmed by others.


> If not, probably it is best to enhance 4127 until that one works as desired.
> 
> So please revert the patch of this ticket and then close the ticket as "wont", or better, as a "doublette" to 4127.

This patch will not be reverted.

Cheers,

Michael
