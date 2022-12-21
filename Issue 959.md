# Issue 959: errors building sage because singular gets confused by system-wide boost

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-21 12:41:12

Assignee: was


```
> It looks like maybe there is an issue with the system-wide boost
> you have installed.

Thanks William. Moving /usr/include/boost to /usr/include/boost.old and
typing again make in SAGE_ROOT did it. You can recommend it to users who
encounter the same problem.
```


So, can we turn off Singular using boost at all, by default?


---

Comment by mabshoff created at 2007-10-21 13:43:52

Well, we should fix the bug upstream by fixing the boost detection code or alternatively introducing a switch to turn off boost.

Cheers,

Michael


---

Comment by malb created at 2007-10-21 22:43:35

Changing status from new to assigned.


---

Comment by malb created at 2007-10-21 22:43:35

Changing assignee from was to malb.


---

Comment by malb created at 2007-10-23 21:36:47

We can't just turn it off because they don't have an option for that for their configure script. Also, fiddling with that script is tricky because it is created from a configure.in newer autoconfs don't understand. I'll report this upstream.


---

Comment by malb created at 2007-10-30 14:52:22

I reported this upstream and a fix will be available in the next point release of Singular. In the meantime Hans recommends to comment out this code


```
#ifdef HAVE_BOOST_DYNAMIC_BITSET_HPP
#define  HAVE_BOOST 1
#endif
```


in `kernel/tgb_internal.h`.


---

Comment by malb created at 2007-10-31 12:50:45

The code stated above was commented out in the most recent singular spkg found at: http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071031.spkg


---

Comment by mabshoff created at 2007-11-01 10:35:34

applied to 2.8.11.alpha0: this should have been fixed via the new Singular.spkg from #948.


---

Comment by mabshoff created at 2007-11-01 10:36:40

Resolution: fixed
