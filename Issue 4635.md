# Issue 4635: Sage 3.2.1.a1: numerical noise in sage/plot/plot.py

Issue created by migration from https://trac.sagemath.org/ticket/4635

Original creator: mabshoff

Original creation time: 2008-11-27 03:44:10

Assignee: mabshoff

CC:  jhpalmieri


```
File "/Applications/sage-3.2.1.alpha1/devel/sage/sage/plot/plot.py",
line 4576:
   sage: adaptive_refinement(sin, (0,0), (pi,0),
adaptive_tolerance=0.01)
Expected:
   [(0.125*pi, 0.38268343236508978), (0.1875*pi,
0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,
0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi,
0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043),
(0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546),
(0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218),
(0.875*pi, 0.38268343236508989)]
Got:
   [(0.125*pi, 0.38268343236508978), (0.1875*pi,
0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,
0.83146961230254512), (0.375*pi, 0.92387953251128674), (0.4375*pi,
0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043),
(0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546),
(0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218),
(0.875*pi, 0.38268343236508984)]
```



---

Comment by mabshoff created at 2008-11-27 04:16:08

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-27 04:16:08

The problem is this:

```
0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi,
0.83146961230254512), (0.375*pi, 0.92387953251128674), (0.4375*pi,
```


Cheers,

Michael


---

Attachment


---

Comment by ncalexan created at 2008-11-27 04:17:27

Fine by me.


---

Comment by mabshoff created at 2008-11-27 04:19:29

Merged in Sage 3.2.1.alpha2


---

Comment by mabshoff created at 2008-11-27 04:19:29

Resolution: fixed


---

Comment by jhpalmieri created at 2008-11-27 04:22:20

Wait, it doesn't work for me!  The very last digit differs in the two cases -- see the output in the description of the ticket.


---

Comment by mabshoff created at 2008-11-27 04:25:42

Replying to [comment:4 jhpalmieri]:
> Wait, it doesn't work for me!  The very last digit differs in the two cases -- see the output in the description of the ticket.
> 
> 

Ok, I will recheck and post an patch on top.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 04:26:39

Indeed: the last line is different, too:

```
(0.875*pi, 0.38268343236508989)]
(0.875*pi, 0.38268343236508984)]
```

I will recheck all of it again - patch coming up.

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-11-27 04:27:07

this replaces the old patch


---

Attachment

Here's a patch.


---

Comment by mabshoff created at 2008-11-27 04:31:39

Replying to [comment:7 jhpalmieri]:
> Here's a patch.

Thanks for the patch. I had already applied mine, but I will rebase your patch relative to my fix.

Positive review for John's patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 04:49:50

I also merged John's additional fix from 4635-new.patch.

Cheers,

Michael
