# Issue 1304: [graphs] edge-labeled graph isomorphism

Issue created by migration from https://trac.sagemath.org/ticket/1304

Original creator: jason

Original creation time: 2007-11-28 19:48:43

Assignee: mhansen

CC:  boothby

Keywords: graphs

From Robert Miller:


```
> Another ticket you might want to create, but that I would be most
> likely to implement, is edge-labeled graph isomorphism.
```



---

Comment by rlm created at 2007-12-02 04:47:57

Changing status from new to assigned.


---

Comment by rlm created at 2007-12-02 04:47:57

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:12:44

Changing keywords from "graphs" to "isomorphism, labeling".


---

Comment by rlm created at 2007-12-17 15:12:44

Changing component from combinatorics to graph theory.


---

Attachment


---

Comment by mabshoff created at 2008-02-07 18:13:34

This bundle needs to be applied before #2085.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-07 18:21:42

To be more precise: the bundle at #2085 contains the bundle attached here, so if both tickets were reviewed one should just merge the bundle at #2085. Damn bundles ;)

Cheers,

Michael


---

Comment by jason created at 2008-02-18 23:07:16

Looks good to me at this point in my graph isomorphism education.


---

Comment by rlm created at 2008-02-18 23:26:39


```
[1:31pm] jason-: okay, first patch in that bundle:
[1:31pm] jason-: you add the line: while alpha[s] != -1: s += 1
[1:31pm] jason-: why was that again?
[1:32pm] rlm: right, but i no longer need to check: if alpha[s] == j
[1:32pm] rlm: that's so that s is still where it is expected to be
[1:33pm] rlm: i doubt that this will actually speed anything up noticably, but...
[1:34pm] jason-: it seems like redundant code.
[1:34pm] jason-: You have exactly the same while loop above (the one that you put the linebreaks in).
[1:34pm] rlm: yes, one is for the directed case
[1:34pm] jason-: oh, unless j=-1
[1:35pm] rlm: that won't happen
[1:35pm] rlm: -1 indicates the end of the list
[1:35pm] jason-: sorry, what is s, t, and j again?
[1:36pm] rlm: so what this loop is doing is the following:
[1:36pm] jason-: thanks...
[1:37pm] rlm: when we are splitting up a cell according to its degree to something in alpha, if that cell is also a cell in alpha, we replace it with the biggest chunk, and put the other fragments at the end of alpha
[1:37pm] rlm: this loop is checking whether that cell is in alpha
[1:37pm] rlm: so s is going through alpha, the cell is j, and the biggest chunk is t
[1:39pm] rlm: we'll only find j once, so stop searching for j once we have found it, but then s indicates where to put the rest of the fragments, so it still needs to be at the end of the list
[1:39pm] jason-: okay, the code makes sense.
[1:39pm] jason-: thanks.
[1:39pm] rlm: np
[1:40pm] jason-: so that bug fix seems separate from the rest of the changes in the file.  Is that right?
[1:41pm] jason-: (in the first patch)
[1:41pm] rlm: it's not a bug fix - really, it's an unnecessary optimization
[1:41pm] rlm: but it is separate from everything else, yes
[1:42pm] jason-: oh, never mind, you're right.
[1:42pm] jason-: gee, things seem to be simpler than I make them out to be!
[1:42pm] rlm:
[1:42pm] rlm: sorry that those are all lumped into the same patch
[1:42pm] jason-: duh, okay.  The other changes: you're renaming lots of functions here.
[1:42pm] rlm: my thoughts for that patch were "stupid things i should have done a long time ago"
[1:43pm] jason-:
[1:43pm] rlm: well, the other significant change is the following
[1:43pm] rlm: if you're seeing which of two square 0/1 matrices are bigger, what i used to do was construct integers for each one, and then compare the integers
[1:43pm] rlm: now i just compare the two matrices, entry by entry
[1:43pm] jason-: okay
[1:43pm] jason-: got it.
[1:43pm] jason-: a nice optimization.
[1:44pm] rlm: i was glad to delete that "TODO" block
[1:44pm] jason-: so you implemented the old #TODO note, then?
[1:44pm] jason-:
[1:44pm] rlm: yep
[1:45pm] rlm: also, to check whether something was an automorphism, i was doing something similarly arcane
[1:46pm] rlm: the only other change in that patch is 'automorphism discovered:' -> 'checking for automorphism:', which is just making the verbose output more correct
[1:47pm] rlm: rather, correct instead of not 
[1:48pm] jason-: okay, first patch looks good.
.
[1:48pm] jason-: second patch...
[1:48pm] rlm: sweet
[1:49pm] rlm: the idea in the second is to convert an edge-labeled graph into a non-labeled bipartite graph, where the input partition keeps track of the original labeling data
[1:51pm] rlm: each edge becomes a vertex on the right side, together with two edges to the original vertices
[1:51pm] rlm: then, we partition the left vertices as they were originally, and we partition the right vertices by their original labels as edges
[1:54pm] rlm: the only automorphisms of the new graph that weren't already automorphisms of the original are the kind that don't move any vertices, for example if there are two similarly labeled edges on the same vertex
[1:57pm] rlm: ..i wonder if it was the stupid enumeration that was causing such a long time for #1360...
[1:57pm] jason-: um, can we change the names of the functions to be a bit more professional and Tom's description of his additions to be a bit more descriptive? 
[1:57pm] rlm: that patch comes soon, but not yet 
[1:57pm] jason-: happy_non_edge_labeled_graph doesn't sound very maintainable 
[1:58pm] rlm: Tom gets credit for being awesome
[1:58pm] rlm: that's all he really did- he listens to me babble, asks good questions.....
[1:58pm] jason-: definitely!  I'm just saying that we should _what_ is so awesome! 
[1:58pm] rlm: the function name gets changed in a later patch, and we'll get to that one
[1:58pm] jason-: should say ..
[1:59pm] rlm: in fact, look at the second file in #2085
[2:08pm] jason-: I'm a little confused by your doctest example.
[2:08pm] jason-: you have a multi-edge graph on 3 vertices
[2:09pm] jason-: which has 12 distinct labeled edges
[2:09pm] jason-: but the non_edge_labeled graph only has 7 vertices.
[2:09pm] rlm: wait, the last one?
[2:09pm] rlm: that's on 4 vertices
[2:09pm] jason-: oops, 4 vertices, right.
[2:10pm] jason-: But still, why doesn't the returned graph have 4 vertices + 12 "edge" vertices?
[2:10pm] rlm: oh, because i misspoke earlier, to you
[2:11pm] rlm: i apologize
[2:11pm] rlm: there is one vertex for each label
[2:11pm] rlm: no you're right, there's something wrong there...
[2:11pm] rlm: one sec
[2:11pm] rlm: aha
[2:11pm] rlm: here's what happens
[2:12pm] rlm: there is a multi-edge on (0,1)
[2:12pm] rlm: it gets translated to a single edge, with label a dictionary
[2:12pm] rlm: the dictionary describes the original labels, but it itself is a single label
[2:14pm] rlm: i'll start writing a detailed description of what that function does, to go as a patch on top of everything else...
[2:15pm] jason-: the returned graph has vertices
[2:15pm] jason-:  
[2:15pm] jason-: [('o', 0), ('o', 1), ('o', 2), ('o', 3), ('x', 0), ('x', 1), ('x', 2)]
[2:15pm] rlm: correct
[2:15pm] jason-: I presume the 'o' vertices are the original vertices
[2:15pm] rlm: correcty
[2:15pm] rlm: -y
[2:15pm] jason-: the 'x' vertices represent the original edge labels?
[2:16pm] rlm: that is true if the graph input is not multi-edged
[2:16pm] rlm: wait
[2:16pm] rlm: one second, let me get it crystal clear
[2:16pm] jason-: that's fine.  I realize it's been a long time.
[2:16pm] rlm: i was wrong when i said vertices correspond to labels
[2:17pm] rlm: I'll show you what I'm writing to go into the documentation of that function
[2:18pm] rlm: "If the graph is a multigraph, it is translated to a non-multigraph, where each edge is labeled with a dictionary describing how many edges of each label were originally there. "
[2:18pm] rlm: change "it is translated" -> "it is first translated"
[2:20pm] rlm: "Then in either case we are working on a graph without multiple edges. At this point, we create another (bipartite) graph, whose left vertices are the original vertices of the graph, and whose right vertices are edges of the original graph."
[2:21pm] rlm: "We partition the left vertices as they were originally, and the right vertices by common labels: only automorphisms taking edges to like-labeled edges are allowed, and this additional partition information enforces this on the bipartite graph."
[2:21pm] rlm: so in the example, there is one edge representing the ten edges on {0,1}, and the label is this dictionary thing...
[2:22pm] rlm: oops
[2:23pm] rlm: scratch that oops
[2:25pm] jason-: so:
[2:25pm] rlm: change "right vertices are edges of the original graph" -> "right vertices represent the edges"
[2:26pm] jason-: G=Graph()
[2:26pm] jason-: G.add_edge(0,1,'first')
[2:26pm] jason-: G.add_edge(1,2,'second')
[2:26pm] jason-: G.add_edge(2,3,'second')
[2:26pm] jason-: a,b=happy_non_edge_labeled_graph(G, [G.vertices()])
[2:27pm] jason-: "a" should have only two "edge" vertices, right?
[2:27pm] rlm: no, it should have three
[2:27pm] rlm: two will be in the same cell of the partition
[2:27pm] jason-: ah, right.
[2:27pm] jason-: and it is so.
[2:30pm] jason-: okay, the examples I've tried seem to work according to your description.
[2:30pm] rlm: good
[2:37pm] kedlaya left the chat room.
[2:39pm] jason-: okay, looks good to me.
```



---

Comment by mabshoff created at 2008-02-19 15:13:18

Merged in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-19 15:13:18

Resolution: fixed
