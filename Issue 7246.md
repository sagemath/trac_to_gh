# Issue 7246: digraph.DeBruijn in graph_generators

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-19 07:00:16

Assignee: rlm

This patch adds the DeBruijn digraph to the ( still very short ) list of digraphs generators.

More information here : http://en.wikipedia.org/wiki/De_Bruijn_graph

I found no way to define automatically a layout for this graph. If you have an idea, do not hesitate to tell me :-)

Nathann


---

Attachment


---

Comment by ncohen created at 2009-10-19 07:00:42

Changing status from new to needs_review.


---

Comment by slabbe created at 2009-10-19 11:29:58

Dear Nathann, I just reviewed your code and made some modifications (see patch). I mostly used some possibilities offered by the word code in sage (e.g. * instead of concatenation and Words(n,1) for words of length one). Tell me if you agree with those modifications.

The output when k=0 was broken (vertices of length one were appearing). Although it could not be supported (return an error), I think it may be defined using multiedges and hence the "Each vertex has exactly n incoming and n outgoing edges" statement stays true. The wiki page doesn't talk about k=0...... 

I am giving a positive review to your patch pending a solution for the case k=0. Can you review my patch?


---

Attachment

I think your patch is perfect, including the case k=0... I did not think about empty words, though it can not hurt :-)

Positive review !

Nathann


---

Comment by ncohen created at 2009-10-19 16:55:35

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-21 07:20:50

Resolution: fixed
