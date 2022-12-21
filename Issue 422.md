# Issue 422: hostname's with dashes (?) in them break SAGE interfaces

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-10 20:24:06

Assignee: was

I discovered live during my SAGE demo at CECM that if the hostname is really weird,
complicated, and has dashes, dots, spaces ? etc., in it, then e.g., 

```
   maple('2+2')
```

won't work.

The fix is to clean the hostname before using it to construct the relevant
temp directory in .sage/temp.  By clean, I mean replace any bad characters
by underscores, say. 


---

Comment by was created at 2007-08-19 06:55:31


```
[23:48] <william> anyway, regarding #422, any thoughts?
[23:48] <william> it's hard to replicate.
[23:48] <mabshoff> re #422: my host has a dash in it.
[23:48] <william> i happened to me *during* a big talk, which was pretty crazy.
[23:48] <mabshoff> you cannot have spaces in names.
[23:48] <william> there were other symbols, so maybe it wasn't the dash.
[23:49] <mabshoff> And dots are usually present.
[23:49] <william> The hostname was really bad.
[23:49] <william> Maybe a *.
[23:49] <mabshoff> Yeah, that could screw with things.
[23:49] <william> this broken *all* interfaces, including gap, etc.
[23:49] <mabshoff> I think there is a standard, i.e. name \in [0..9] \cup [a-Z] \cup {-,.} or something like that.
[23:50] <william> it's also possible that the problem wasn't the hostname.
[23:50] <william> in the talk somebody said it was, and i disabled my network connection, and the problem went away.
[23:50] <william> the hostname looked very complicated.
[23:50] <william> I wish I had copied it.
[23:50] <mabshoff> okay
[23:51] <william> wait -- they are all in .sage/temp
[23:51] <william> cleaner-d142-058-050-016.wireless.sfu.ca.pid
[23:51] <mabshoff> Any thoughts on "sage -t -gdb foo.py"?, i.e. #374
[23:51] <william> d142-058-050-016.wireless.sfu.ca
[23:51] <william> those hostnames are fine.

```



---

Comment by mabshoff created at 2007-09-10 05:40:18

We need to find an actual failure in order to solve this.

Cheers,

Michael


---

Comment by craigcitro created at 2008-02-08 07:06:06

Resolution: invalid


---

Comment by craigcitro created at 2008-02-08 07:06:06

Not reproducible.
