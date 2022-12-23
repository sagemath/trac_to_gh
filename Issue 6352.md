# Issue 6352: gap_packages upgrade

Issue created by migration from https://trac.sagemath.org/ticket/6352

Original creator: wdj

Original creation time: 2009-06-17 23:06:26

Assignee: tbd

CC:  awebb

Keywords: gap

This is an upgrade optional package for gap-4.4.12, as in #6348.
This spkg applies fine to 4.0.2.rc1 and all related failures in sage -testall -optional are fixed in the patch in #6348.

The command "newest-version gap" mentioned in the old spkg-install script is broken. I was unable to locate that script, so I slightly modified the spkg-install so it would compile the binaries correctly.


---

Comment by wdj created at 2009-06-17 23:09:56

See http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.12_0.spkg.


---

Comment by boothby created at 2009-06-19 18:19:30

Changing component from algebra to optional packages.


---

Comment by awebb created at 2009-07-17 12:26:40

I had troubles with: 


```
sage -t -long --optional "devel/sage/sage/groups/perm_gps/permgroup.py"

... skip 450 lines of traceback

**********************************************************************
9 items had failures:
   1 of   4 in __main__.example_31
   1 of   4 in __main__.example_32
   4 of   9 in __main__.example_37
   2 of   6 in __main__.example_38
   4 of   7 in __main__.example_39
   2 of  18 in __main__.example_4
   1 of   4 in __main__.example_40
   1 of   9 in __main__.example_5
   2 of   6 in __main__.example_73
***Test Failed*** 18 failures.

```


They were from both database_gap and gap_packages. I have database_gap-4.4.10 installed and the spkgs here and from #6348 on Sage 4.1. These might be related although I don't get errors from gap-4.4.12. It probably doesn't make sense to worry about this until #6348 is cleared up. The full log is attached.


---

Attachment

Replying to [comment:4 awebb]:
> I had troubles with: 
> 
> {{{
> sage -t -long --optional "devel/sage/sage/groups/perm_gps/permgroup.py"
> 
> ... skip 450 lines of traceback
> 
> **********************************************************************
> 9 items had failures:
>    1 of   4 in __main__.example_31
>    1 of   4 in __main__.example_32
>    4 of   9 in __main__.example_37
>    2 of   6 in __main__.example_38
>    4 of   7 in __main__.example_39
>    2 of  18 in __main__.example_4
>    1 of   4 in __main__.example_40
>    1 of   9 in __main__.example_5
>    2 of   6 in __main__.example_73
> ***Test Failed*** 18 failures.
> 
> }}}
> 
> They were from both database_gap and gap_packages. I have database_gap-4.4.10 installed and the spkgs 
> here and from #6348 on Sage 4.1. These might be related although I don't get errors from gap-4.4.12. 
> It probably doesn't make sense to worry about this until #6348 is cleared up. The full log is attached.

All I can say is that they worked fine for me when I posted them. I agree that it is a waste of time
to work on this until #6348 is cleared up.


---

Comment by awebb created at 2009-10-14 08:09:10

Changing status from needs_review to needs_work.


---

Comment by awebb created at 2010-07-15 17:29:49

As gap_packages has been updated to 4.4.12 this ticket seems to be no longer needed. I think it can be closed.

Adam


---

Comment by awebb created at 2010-09-21 10:44:53

Resolution: duplicate


---

Comment by awebb created at 2010-09-21 10:44:53

This was closed in #8229.
