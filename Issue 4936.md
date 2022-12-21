# Issue 4936: massive bloat: make something delete everything in ~/.sage/gap > 1 week old and untouched

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-04 17:02:31

Assignee: mabshoff

It is *always* safe to delete anything in ~/.sage/gap, since it will get autorecreated when Sage is started.   I just looked at my ~/.sage/gap on sage.math and it is HUGE:


```
wstein`@`sage:~/.sage/gap$ ls -1 |wc -l
90
wstein`@`sage:~/.sage/gap$ du -sch .
1.3G	.
1.3G	total
```


I have stuff in there going back to March 2008.

The code in gap.py that creates the workspace in .sage/gap should also delete all old workspaces.   I think 1 week is arbitrary, but is safe since as mentioned above any time length is safe.


---

Comment by wdj created at 2009-01-04 17:34:56

I know there are GAP users who always load GAP via a workspace. I'm worried that if the only way to use GAP in Sage was to use a "recent" workspace then these users would not be well-werved.

A possible workaround would be if there was a way to optionally use a specific workspace. In other words, .\sage -gap and gap_console() could take an optional argument with a specific workspace. Does this seem reasonable? It might be rarely used, but it could be a potentially very useful feature to allow users to use another workspace.


---

Comment by was created at 2009-01-05 17:01:25

> I know there are GAP users who always load GAP via a workspace. 
> I'm worried that if the only way to use GAP in Sage was to use 
> a "recent" workspace then these users would not be well-werved.

This criticism of my suggestion doesn't make sense, because I'm *only* suggesting deleting the old workspaces in ~/.sage/gap/.  Not all workspaces on the users computer or something.      Anyway, I think your worry about makes no sense (to me). Please correct me if I'm wrong (quite possible).  Thanks.


---

Comment by was created at 2009-01-24 06:07:40

To test the attached patch, look $HOME/.sage/gap, and notice if you have a lot of old files there.  Maybe even fake some old workspace files like this:

```
touch -t 01010000 workspace-00
```


Then touch local/bin/gap_stamp to force a recheck

```
cd SAGE_ROOT
touch local/bin/gap_stamp
```


and note that when you start sage the files you created in $DOT_SAGE/gap are deleted.


---

Attachment

This works perfectly for me.


---

Comment by mabshoff created at 2009-01-24 14:31:19

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 14:31:19

Merged in Sage 3.3.alpha2
