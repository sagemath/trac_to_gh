# Issue 3981: finance.TimeSeries - Add candlestick plot method.

Issue created by migration from https://trac.sagemath.org/ticket/3981

Original creator: cswiercz

Original creation time: 2008-08-28 23:12:46

Assignee: cswiercz

CC:  cswiercz

Keywords: finance

A candlestick plot is a nice way of visualizing open, high, low, and close stock information over intervals in a time series. The attached patch adds the method TimeSeries.plot_candlestick(bins) to do exactly that.


---

Comment by cswiercz created at 2008-08-29 17:14:41

Changing status from new to assigned.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-09-18 23:57:35

Looks good to me.  I added a patch which does a few tiny cleanups.  Apply both patches.


---

Comment by mabshoff created at 2008-09-19 03:13:17

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 03:13:17

Merged both patches in Sage 3.1.3.alpha0
