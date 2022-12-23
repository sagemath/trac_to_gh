# Issue 8763: put licensing information into published worksheets

Issue created by migration from https://trac.sagemath.org/ticket/8763

Original creator: ddrake

Original creation time: 2010-04-25 07:24:53

Assignee: jason, was

CC:  kcrisman chapoton

As discussed in http://groups.google.com/group/sage-edu/browse_thread/thread/aa651032bb34a285, it would be very nice if published worksheets could include licensing information, so that we could collect, modify, and redistribute excellent worksheets.

So, when publishing worksheets, there should be a mechanism to choose a license; as a start, maybe just hard-code four choices: CC by-sa-nc, by-sa, GFDL, and no licensing information at all. If a license is chosen, this would put something like this into the worksheet:

```
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/us/">
<img alt="Creative Commons License" style="border-width:0" 
src="http://i.creativecommons.org/l/by-sa/3.0/us/80x15.png" 
/></a><br />This worksheet is licensed under a <a rel="license" 
href="http://creativecommons.org/licenses/by-sa/3.0/us/">Creative 
Commons Attribution-Share Alike 3.0 United States License</a>.
```

The rel="license" bit is a microformat that will make the licensing information computer-readable, so that eventually one could search for worksheets available with a certain license.


---

Comment by jason created at 2010-04-26 23:47:24

Can we add CC-by and CC0 (http://creativecommons.org/publicdomain/) as well?


---

Comment by ddrake created at 2010-04-27 00:27:52

Replying to [comment:1 jason]:
> Can we add CC-by and CC0 (http://creativecommons.org/publicdomain/) as well?

If you make a patch, you can add any licenses you want. :)


---

Comment by jason created at 2010-05-11 16:24:42

I believe that if we want to incorporate such worksheets eventually into the Sage proper, none of the above licenses would allow it, as I think all are incompatible with GPL.  Ah, the joys of licensing headaches!


---

Comment by jason created at 2010-05-11 16:25:35

(well, I believe CC-by and CC0 would allow incorporation into a GPL project).


---

Comment by ddrake created at 2010-05-11 23:27:44

Replying to [comment:3 jason]:
> I believe that if we want to incorporate such worksheets eventually into the Sage proper, none of the above licenses would allow it, as I think all are incompatible with GPL.  Ah, the joys of licensing headaches!

Well, I don't want to get into licensing discussion here, but my first thought was that there's a difference between "functionally including" something into Sage -- adding new code or doctests -- and just including some ancillary material. From a licensing perspective, there's perhaps no difference.

In any case, clear licensing information would make it easier for someone to somehow collect and redistribute good worksheets.


---

Comment by ddrake created at 2011-04-20 00:12:16

As a note for whoever implements this: given [this message to sage-edu](https://groups.google.com/group/sage-edu/msg/2d9f106c9b358b4e), perhaps when setting license information, the notebook should ask the user what name to use for attribution. A suggestion of "name <email>" would be helpful.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-13 07:27:02

Resolution: invalid
