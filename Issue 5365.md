# Issue 5365: graphplot arrowheads are hidden in multi-edge digraphs

Issue created by migration from Trac.

Original creator: ekirkman

Original creation time: 2009-02-24 23:44:54

Assignee: ekirkman, rlm

Kristin Lauter pointed out that the following input:

sage: S = SupersingularModule(389)
sage: D = DiGraph(S.hecke_matrix(2))
sage: D.plot(vertex_size=50).show(figsize=10)

produces a graph where the arrowheads of some edges are hidden by the vertex.  

This is going to be a one-ish line fix that I can post as soon as I'm done building 3.3.



---

Attachment

The picture attachment (t2.png) is the current buggy output.  I will post another picture example with my patch this evening.


---

Comment by ekirkman created at 2009-02-24 23:56:48

Resolution: duplicate


---

Comment by ekirkman created at 2009-02-24 23:56:48

This is a duplicate now...  (See ticket #5366).  Apparently the back button isn't the best way to adjust your wiki formatting...  (Sorry mabs).
