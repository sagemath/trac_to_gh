# Issue 5858: Octave library linking problems

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-04-22 17:57:18

Assignee: was

Keywords: octave, library linking

Email from sage-support describes the problem and Michael Abshoff's comments about what needs to be done:

On Apr 22, 12:46 am, Ajay Rawat <ajay.rawa...`@`gmail.com> wrote:

> Well i tried the command
> sage:octave_version()
> sage:3.0.0
> but when i tried octave_console
> it replied...................

> octave:
> /usr/local/sage-3.2.3-Ubuntu8.04LTS-64bit-Intel-x86_64-Linux/local/lib/l\
> ibz.so.1: no version information available (required by
> /usr/lib/octave-3.0.0/liboctinterp.so)

The problem is that the libz shipped by Sage and the one used by the
system (and which was linked by Octave) do not play nicely together.

To work around this write a script called octave (I assume that is the
name of the octave start script/binary

#!/bin/sh
LD_LIBRARY_PATH=SAGE_ORIG_LD_LIBRARY_PATH; export LD_LIBRARY_PATH
exec octave "$`@`"

I didn't try this, so you might need to adjust something.

To fix this once and for all in sage we should use native execute -
would someone open a ticket since I am about to go offline for the
night :)

Cheers,

Michael 



---

Comment by jjh created at 2009-09-11 04:45:56

Patch


---

Attachment


---

Comment by jjh created at 2009-09-11 04:47:31

This seems to fix the problem. Octave passes all doctests on my machine.


---

Comment by jason created at 2009-09-15 04:26:13

The fix looks right, applies to my tree, and -optional doctests pass.


---

Comment by jason created at 2009-09-15 04:26:33

(-optional on octave.py, that is).


---

Comment by mvngu created at 2009-09-15 23:28:51

Resolution: fixed
