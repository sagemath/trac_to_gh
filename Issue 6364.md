# Issue 6364: error message at end of successful "sage -merge"

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-06-20 13:25:47

Assignee: tbd

Keywords: merge

Reported on sage-devel:

```
All seemed well with that test (all tests passed, etc), but the final
lines of output are

All tests passed! Popping patches from queue ...
cd "/home/jec/sage-4.0.2/devel/sage" && hg qpop -a
cd "/home/jec/sage-4.0.2/devel/sage" && hg qdelete trac_5307.patch
Building failed with SystemExit: 0

-- what's with the "failed" in the last line?
```


Craig suggested:

```
Interesting ... I've never seen that before. What os/arch are you on?
Could I ask you to try one thing: go to $SAGE_ROOT/local/bin, and edit
sage-apply-ticket. On the 5th line from the bottom is "sys.exit(0)" --
could you try deleting that line and moving it to the very bottom (and
outdenting it)? I suspect that error will go away. Actually, you could
even try just deleting that line, and I suspect that will fix it, too.
```

and was right:

```
That did the trick -- ran fine and no "failure" line at the end.  (I
moved that line to the end as suggested)
```






---

Attachment


---

Comment by cremona created at 2009-06-20 19:30:38

The patch looks good, but would not apply using the usual system (which could not find the file being patched).
If you tell me how to apply it I will do so and test it!


---

Comment by craigcitro created at 2009-06-20 20:34:32

How do you usually apply patches? Do you use `hg_sage` or do you change to the appropriate directory and apply directly with `hg`? If it's the former, use `hg_scripts`; if it's the latter, go to `$SAGE_ROOT/local/bin` and use `hg`. If neither of those work, copy-paste the error message and I'll go from there. `:)`


---

Comment by cremona created at 2009-06-20 21:57:49

I did not know about hg_scripts.  I always used to use hg_sage (though did not realise the significance in the "sage" part of that as meaning "the sage library, i.e. the devel directory");  more recently I usually use mercurial queues via "sage -hg" from the command line.

Now using hg_scripts pops up various editor windows, complaining about unsaved changes.  Same in a completely new clone.  I'll try again tomorrow, but it may be that my failed attempts at this trivial test have messed up my sage build so I might have to rebuild from source.  Meanwhile perhaps someone who knows what they are doing can review the patch!


---

Comment by cremona created at 2009-07-11 15:22:16

apply to 4.1 (instead of previous patch)


---

Attachment

Craig's patch would not work for me, it failed to apply, perhaps because the script has changed in the interim.

I have added a new patch and hope it can be reviewed before things  change again!


---

Attachment


---

Comment by boothby created at 2009-07-17 22:10:32

Works for me -- however, there was a typo in the file (my fault) which prevents the merge script from working at all.  I attached a patch which fixes that typo.


---

Comment by mvngu created at 2009-07-18 18:22:40

Resolution: fixed


---

Comment by mvngu created at 2009-07-18 18:22:40

Merged only `trac_6364.patch`. The typo issue addressed by `scripts_6364_pre.patch` has been fixed by ticket #6511.
