# Issue 3137: view command in misc/latex.py -- fix to not hardcode xdvi command

Issue created by migration from https://trac.sagemath.org/ticket/3137

Original creator: was

Original creation time: 2008-05-09 00:15:30

Assignee: was


```
On Wed, May 7, 2008 at 12:26 PM, John H Palmieri <jhpalmieri64@gmail.com> wrote:
>
> A problem: on my linux box, if I use 'view' (not in a notebook), an
> xdvi window appears then immediately disappears.  If I run view with
> 'debug=True', toward the end I get this:
>
> Output written on sage.dvi (1 page, 740 bytes).
> Transcript written on sage.log.
> gs: Unrecoverable error: limitcheck in .putdeviceprops
> xdvik gs_io: Broken pipe
> xdvik gs_io: Broken pipe
> xdvik gs_io: Broken pipe
> ghostscript died unexpectedly.
> xdvi.bin: spcl_scan: shouldn't happen: POST encountered, offset 659
>
> Has anyone seen this before?  (This works on my mac, just not on my
> linux box.)
>

I have never seen that before.

> And a question: on my mac, suppose I want to use TeXShop instead of
> xdvi to display the output of the view command.  Is there a way to do
> this?
>

The use of xdvi is hardcoded in

sage/misc/latex.py

so the answer is I guess to change this and submit a patch
or make it a trac ticket.   It's reasonable to consider this
a bug, since view should I think just use the OS X open
command as defined in sage/misc/viewer.py, i.e., use
whatever is the default opener for a dvi file on your system.

It's hardcoded xdvi right now since that was some of the first
sage code I ever wrote and that was long before I ported
Sage to run on OS X...
```



---

Attachment

patch to use dvi_viewer() from misc/viewer.py


---

Comment by yi created at 2008-05-09 16:22:17

This has annoyed me for a while now so I fixed it to use the sage/misc/viewer.py helper file to determine the correct viewer. 

Please test on Linux (only tested on OS X).


---

Comment by jhpalmieri created at 2008-05-16 17:10:28

Works for me on my linux box.  I'm using some version of Red Hat; perhaps people using other linux distributions should test it on their machines, too.


---

Comment by mabshoff created at 2008-05-18 14:50:15

Resolution: fixed


---

Comment by mabshoff created at 2008-05-18 14:50:15

Merged in Sage 3.0.2.alpha1
