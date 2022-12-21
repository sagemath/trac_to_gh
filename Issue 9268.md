# Issue 9268: Notebook Server replies to Plot3d-Data-Request with Status 301

Issue created by migration from Trac.

Original creator: ManDay

Original creation time: 2010-06-18 20:57:52

Assignee: jason, was

CC:  kcrisman jhpalmieri

Keywords: notebook java jmol black

This issue has long caused problems, although many people managed to get it fixed without actually knowing what caused it. As discussed in all detail in the following thread

http://groups.google.com/group/sage-notebook/browse_thread/thread/9191e031224a3ce9

JMol requests the data for the plot3d from the Sage backend. When it does so, on some occasions it receives a 301 Moved Permanently which Java is not following but interprets as 200 and parses the content - which then causes the error.

This is partly a client-side Java problem as Java should perhaps follow the 301 to the new location and then pass the data transparently but also Sage shouldn't provide a 301'd location in the first place.

Further details, such as the fact that this does not happen for applets which are part of a published worksheet can be found in the thread.

Can be fixed by making JMol pointing to the correct location or make Sage transparently return the data instead of a 301.

This problem occurs with both, the open IcedTea (OpenJDK) and propritary Sun Java in Firefox 3.6 on Ubuntu 10.4LTS.

On a sidenote, I assume that other people do not have this problem because they might have additional packages installed which compensate for the 301.


---

Comment by chapoton created at 2020-03-28 20:36:28

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-03-28 20:36:28

ancient ticket about deprecated sagenb, can we close ?


---

Comment by kcrisman created at 2020-03-28 20:43:01

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2020-03-28 20:43:01

There were a number of wonky things like this we never saw often enough to diagnose, true.


---

Comment by chapoton created at 2020-03-28 20:45:33

Resolution: invalid


---

Comment by chapoton created at 2020-03-28 20:45:33

thx
