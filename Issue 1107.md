# Issue 1107: [with patch] add minkowski bound function for number fields

Issue created by migration from https://trac.sagemath.org/ticket/1107

Original creator: was

Original creation time: 2007-11-05 21:29:44

Assignee: was

Add computation of Minkowski bound to number fields (very simple). 


---

Comment by robertwb created at 2007-11-18 09:16:10

The patch is good.


---

Comment by mabshoff created at 2007-11-19 21:24:29

The patch no longer applies cleanly:

```
mabshoff@sage:/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/devel/sage$ hg import minkowski.patch
applying minkowski.patch
patching file sage/rings/rational_field.py
Hunk #1 succeeded at 298 with fuzz 2 (offset 23 lines).
Hunk #2 FAILED at 362
Hunk #3 FAILED at 370
Hunk #4 FAILED at 378
3 out of 4 hunks FAILED -- saving rejects to file sage/rings/rational_field.py.rej
abort: patch failed to apply
```


Cheers,

Michaell


---

Comment by was created at 2007-11-27 05:18:01


```
cwitty: williamstein, did you notice mabshoff's comment on your #1107 patch?  Evidently it no longer applies.
[9:13pm] williamstein: Thanks.  
[9:16pm] williamstein: actually it's fine -- the one hunk that doesn't get applied with 1107 doesn't apply because it is already applied in the current sage.
[9:16pm] williamstein: So it's OK.  Just ignore the one hunk that fails. 
```



---

Comment by was created at 2007-11-27 05:21:45


```

[9:17pm] cwitty: The three hunks that don't get applied, you mean?  (Judging from mabshoff's comment.)
[9:20pm] williamstein: Yes, that's what I meant.  Thanks.
```



---

Attachment

This is rebased against 2.8.15


---

Comment by was created at 2007-11-27 05:48:30

OK, I rebased it so I get credit :-)


---

Comment by robertwb created at 2007-11-29 22:22:55

Looks good to me.


---

Comment by mabshoff created at 2007-12-01 11:30:21

Merged in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 11:30:21

Resolution: fixed
