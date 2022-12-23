# Issue 8631: Make a graph-input interact control

Issue created by migration from https://trac.sagemath.org/ticket/8631

Original creator: rbeezer

Original creation time: 2010-03-30 14:54:01

Assignee: itolkov

CC:  rkirov was kevinc

Keywords: graph editor

Should be able to use the graph editor as an input widget for interacts.  

Preliminary proposal on sage-devel:
http://groups.google.com/group/sage-devel/browse_thread/thread/f5b850969340bc37/

Current state of graph editor:  #8222


---

Comment by was created at 2010-03-30 17:23:43

Good idea.  If we do this, we might want to also have an interact control that gives a nice interactive way of choosing a graph from the family of all graphs. This would be what graphs.[tab] gives, but more graphical.

I wonder if interact controls should be rewritten to somehow be as easy to make as `@`interact's themselves?  It would cool to abstract out the whole idea of interact controls so that users could just make them on the fly.


---

Comment by rkirov created at 2010-04-12 00:13:42

Similarly to what Rob tried. I opened interact.py and started editing (this is probably the longest .py file I ever worked with).

So far I can make the virtual interact and it can try to start the embedded graph editor. But i run into a weird thing where my injected graph data gets transformed as follows all " , " -> " ,="" ".

Anyways, if anybody else is working on this, we should exchange some patches even if they are very incomplete.


---

Comment by rbeezer created at 2010-04-12 00:47:57

Replying to [comment:2 rkirov]:
> Anyways, if anybody else is working on this, we should exchange some patches even if they are very incomplete.

Definitely.  I'll try to recover what I worked up before and post it here in the next couple days.  My work on this got a bit jumbled, which stopped me a few days ago on a final review of the editor itself at #8222.  

So I'll tackle both of these in one shot.

Rob


---

Attachment

patch for sagenb - depends on #8222


---

Attachment

tiny sage patch to avoid a circular import


---

Comment by rkirov created at 2010-04-29 02:38:17

the graph interact is ready. The patches depends on the newest graph_editor which is #8222.

Needs work because i haven't done doctests and haven't decided how to incorporate the overlapping code with the graph_editor into one js graph library (right now i just copied it into a new file graph_interact.js and modified).

In any case it is working for anyone who wants to see how eigenvalues or chromatic numbers change dynamically (as you throw in or throw out vertices and edges). Enjoy!


---

Comment by rkirov created at 2010-04-29 02:38:17

Changing status from new to needs_work.


---

Comment by rbeezer created at 2010-04-29 05:40:45

Rado,

Very nice!  This works for me - I'll upload a screenshot next.

For anybody else testing, you just need a line like

`G=Graph(...)`

in the argument list of the function you are using as the interact.  It seems that you need to specify the initial graph as something other than a null graph, and whatever this graph might be, the routine expects to find position information.  

Nice work!

Rob


---

Comment by rbeezer created at 2010-04-29 05:41:48

Screenshot of graph editor interact control


---

Attachment

Nice!

It looks like in the patch that there is a huge section of code that is commented out that should be just deleted.


---

Comment by mkoeppe created at 2022-04-03 18:38:11

#30540 has made a graph editor available


---

Comment by mkoeppe created at 2022-04-03 18:38:11

Changing status from needs_work to needs_review.


---

Comment by @jfraymond created at 2022-04-25 07:41:37

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2022-05-11 02:14:43

Resolution: invalid
