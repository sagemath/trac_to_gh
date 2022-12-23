# Issue 8892: Many doctests fails since the update of NetworkX !

Issue created by migration from https://trac.sagemath.org/ticket/8892

Original creator: ncohen

Original creation time: 2010-05-05 17:44:26

Assignee: jason, ncohen, rlm

Hello everybody !!!

I noticed working on something quite different that many doctests were failing in Sage's graph library because of the recent update of NetworkX... The reason is easy : the default edge label is not "None" anymore but {}. Besides, dictionary are not hashable !!!

This patch fixes it ! 

Nathann


---

Comment by jason created at 2010-05-05 18:39:12

Apparently now, networkx has moved to having a dictionary of edge attributes, rather than a specific "label".  See http://networkx.lanl.gov/reference/api_1.0.html#edge-attributes

I'm not saying we should follow the convention, but it does seem to make sense.  Instead of just storing a single value, store a dict of attributes.

Why is it important that dictionaries are not hashable?


---

Comment by ncohen created at 2010-05-05 18:48:07

Because I sometimes stored them as keys of dictionaries. It means I will need to forget to store the label, and just the endpoints. The other detail is that in many algorithms, the labels are used as a weight, and I you will see very often in Sage's code :
weight = lambda label : 1 if label is None else label

So all these occurrences need to be replaces to label == {} in this case... Does that mean we should assume labels are ALWAYS dictionaries ? This would mean trouble... Where would we store numerical values for edges then.. a default field ?

Nathann


---

Comment by jason created at 2010-05-05 18:58:28

A little farther down the networkx page listed, we find http://networkx.lanl.gov/reference/api_1.0.html#converting-your-existing-code-to-networkx-1-0, which says that now all algorithms (in Networkx) look for the "weight" edge attribute.

Sounds like that would be a huge change for Sage code, though...


---

Comment by rbeezer created at 2010-05-06 03:22:17

Hi Nathann,

Thanks for uncovering this one.  Not sure right now I have a good idea about what should be done.

However, is there a patch to go on this?  I'm not seeing one.

Rob


---

Comment by ncohen created at 2010-05-06 03:25:17

Not yet. For the moment, my patch is a nasty one : replaces tests "is None" by "is None or == {}". I thought it may be better to settle on what we want to do with these labels, but I can upload it otherwise (somewhere on another computer at the moment) :-)

Nathann


---

Comment by ncohen created at 2010-05-08 00:53:47

Here is a patch that does not make any choice. I replaced the "is None" by "in RR" :-)

The failing docstrings come from GraphViz ( at least on my computer ) !

Nathann


---

Comment by ncohen created at 2010-05-08 00:53:47

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-05-10 17:31:33

Now also fixes the edge_coloring function from the graph_coloring module, as reported by Minh in #8781

Sorry for that !

Nathann


---

Attachment


---

Attachment

I'm mostly happy with [trac_8892.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8892/trac_8892.patch). I have attached a reviewer patch that deals with the part I'm not happy with, i.e. fix some typos introduced by the first patch. Apart from myself, anyone is welcome to give a final sign off on this ticket.


---

Comment by jason created at 2010-05-11 07:15:41

I sign off on your changes.  Are you asking someone else to also sign off on the original patch?


---

Comment by jason created at 2010-05-11 07:15:41

Changing assignee from jason, ncohen, rlm to jason.


---

Comment by jason created at 2010-05-11 07:15:58

Changing assignee from jason to ncohen.


---

Comment by jason created at 2010-05-11 07:16:56

(I didn't apply your changes, but it is clear that they are cosmetic things.)


---

Comment by mvngu created at 2010-05-11 08:05:57

Replying to [comment:9 jason]:
> Are you asking someone else to also sign off on the original patch?

Not really. I'm OK with ncohen's patch.


---

Comment by mvngu created at 2010-05-11 08:05:57

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-12 22:48:50

Resolution: fixed
