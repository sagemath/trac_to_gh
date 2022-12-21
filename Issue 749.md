# Issue 749: graphs: enum() functionality duplicated in relabel()

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-24 22:02:34

Assignee: was

Keywords: graphs

The enum() code is duplicated in relabel() for the quick option.  It sure would be nice to factor that out so that the enum() code was all in one place.


---

Comment by rlm created at 2007-10-22 16:30:51

See ticket #729 for some relevant comments...


---

Comment by rlm created at 2007-10-23 17:56:36

Or instead, just read them here:

__cmp__ ultimateley ends up using enum() twice, and this is kind of too much, since we could just look at the two graphs from lexicographically most significant, and return the answer as soon as they differ. Also, as Jason points out we should be using __eq__, __neq__, __lt__, __le__, __gt__, __ge__ instead.


---

Comment by rlm created at 2007-10-26 21:10:52

Note - the quick option in the relabel function was originally an optimization for the graph_isom code, and no longer applies, since it is never used. Other than that purpose, it doesn't make sense to have it as an option, so I'll just remove it.

Here is another aspect:

```
sage: G._nxg.adj
{0: {1: [None]}, 1: {0: [None]}}
sage: H._nxg.adj
{0: {1: [None, None]}, 1: {0: [None, None]}}
sage: G == H
True
```



---

Comment by rlm created at 2007-10-26 23:59:29

There is an attached patch that cleans up the whole situation.


---

Comment by rlm created at 2007-10-26 23:59:29

Changing status from new to assigned.


---

Comment by rlm created at 2007-10-26 23:59:29

Changing assignee from was to rlm.


---

Attachment

This one first, removed quick option from relabel().


---

Comment by rlm created at 2007-10-27 00:02:29

This is the main overhaul.


---

Attachment


---

Comment by cwitty created at 2007-10-27 04:52:27

Resolution: fixed
