# Issue 9737: Moved interact to view an induced subgraph from wiki to library

Issue created by migration from https://trac.sagemath.org/ticket/9737

Original creator: punchagan

Original creation time: 2010-08-12 20:39:21

Assignee: itolkov, jason

CC:  mkoeppe dimpase slelievre tscrim

Moved the interact that shows an induced subgraph obtained on deleting a vertex, from the wiki to library. 


---

Attachment

I really have to say: is this example worth it? 

IMHO, the graph editor now shipped with Sage makes this example out of order. Use graph_editor on the chosen graph, and double click on a vertex to delete it, and you're showing the same idea, with a more strightforward interface. 

There are loads of awesome things to do with graphs in Sage. With the new patch #8631, we can do much better than this.


---

Comment by chapoton created at 2020-09-30 09:21:16

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-30 09:21:16

obsolete ?


---

Comment by chapoton created at 2021-01-12 14:40:48

can we close ?


---

Comment by tscrim created at 2021-01-13 07:01:49

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2021-01-13 07:01:49

I think so.


---

Comment by chapoton created at 2021-01-13 08:15:27

Resolution: invalid
