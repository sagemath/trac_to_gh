# Issue 5039: Create a class for SetPartition (with no s)

Issue created by migration from https://trac.sagemath.org/ticket/5039

Original creator: slabbe

Original creation time: 2009-01-20 20:17:01

Assignee: mhansen

CC:  sage-combinat

The Elements of `SetPartitions` of a set A are actually Sets of Sets. But there are specific functionalities I would like for those "Sets of Sets". For example : merge the classes of a an b and ask what is the representant of a, where a, b are in A.

Right now, Arnaud Bergeron and I coded and named it as `DisjointSet` and it is available in the sage-combinat tree. The implementation is inspired from :

http://en.wikipedia.org/wiki/Disjoint_set_data_structure

See also this thread :
http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/4b6d5bb2983d81c2/f52adb855eb3b09f?lnk=gst&q=disjoint+set#f52adb855eb3b09f


---

Comment by slabbe created at 2009-01-20 20:17:54

Changing assignee from mhansen to slabbe.


---

Comment by tscrim created at 2013-03-19 17:21:51

This was integrated into sage in #6775, but I've reorganized the docs for `DisjointSet` to make the interactive documentation more informative.


---

Comment by tscrim created at 2013-03-19 17:21:51

Changing status from new to needs_review.


---

Comment by ncohen created at 2013-03-24 19:21:51

Helloooooooooo !!

Several remarks :
* Could you update the ticket's title and description ?
* Why did you move the description of the data structure from the module to the function ? `:-/` I prefer when it is at the top of the html documentation, and here you have no idea of what is happening in that module... Plus there is a function and three classes in that module, so something should be said at the module level `:-/`
* I know it's not the point of this ticket but what would you think of changing `cardinality()` so that it actually returns the cardinality of the partition, and not the cardinality of its union ? And have another method named "`number_of_elements`" which would return what `cardinality` currently returns ? Would make more sense, wouldn't it ? It does not have to be in this ticket, though.

Nice patch though ! Always good to improve the doc `:-)`

Nathann


---

Comment by ncohen created at 2013-03-24 19:21:51

Changing status from needs_review to needs_info.


---

Attachment


---

Comment by tscrim created at 2013-03-27 23:41:48

Replying to [comment:4 ncohen]:
> * Could you update the ticket's title and description ?
Done

> * Why did you move the description of the data structure from the module to the function ? `:-/` I prefer when it is at the top of the html documentation, and here you have no idea of what is happening in that module... Plus there is a function and three classes in that module, so something should be said at the module level `:-/`

The main reason is for viewing the interactive doc using `DisjoinSet?` since getting the module level doc interactively is unintuitive IMO. I have I've added somethings to the module level directing you to the function for more info.

> * I know it's not the point of this ticket but what would you think of changing `cardinality()` so that it actually returns the cardinality of the partition, and not the cardinality of its union ? And have another method named "`number_of_elements`" which would return what `cardinality` currently returns ? Would make more sense, wouldn't it ? It does not have to be in this ticket, though.

Part of me says yes, part no. However because this is how it's been, I don't want to make any changes. If you feel strongly about it, you can make the change on another ticket.

> Nice patch though ! Always good to improve the doc `:-)`

Thank you. Ready for review again.


---

Comment by tscrim created at 2013-03-27 23:41:48

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2013-03-28 09:07:44

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2013-03-28 09:07:44

Hellooooooooooooo !!!!

> The main reason is for viewing the interactive doc using `DisjoinSet?` since getting the module level doc interactively is unintuitive IMO. I have I've added somethings to the module level directing you to the function for more info.

Hmmmmm.. Well, I have the opposite view. With time I add more and more stuff at module level because I use Sage's documentation through Google, and it's hard to find the documentation when it's lost among dozens of functions :-)

http://www.sagemath.org/doc/reference/graphs/sage/graphs/graph_decompositions/vertex_separation.html

But well, for as long as we fight by adding doc in Sage this fight is a good fight `:-P`

> Part of me says yes, part no. However because this is how it's been, I don't want to make any changes. If you feel strongly about it, you can make the change on another ticket.

Got it !

Have fuuuuuuuuuuuuuuuuuuuuun !

Nathann


---

Comment by tscrim created at 2013-03-28 12:37:26

Thank you for the review.

Travis


---

Comment by ncohen created at 2013-03-28 12:44:15

A pleasure ! You can cc me for this kind of stuff, they'll be reviewed quickly.

Nathann


---

Comment by ncohen created at 2013-03-28 12:44:46

Well, this one was opened 4 years ago but you know what I mean `:-P`

Nathann


---

Comment by jdemeyer created at 2013-04-01 10:37:53

Resolution: fixed


---

Comment by slabbe created at 2013-04-02 13:09:20

Thanks Travis for closing this ticket and Nathann for the review.

Having doc in the top of the module (for web doc browsing) vs in the the class (for ?  interactive doc browsing) is a good question. One answer could be to copy the same information in both place... At least now, there is a link at the top of the module linking to the class...

Sébastien


---

Comment by nthiery created at 2013-04-02 13:32:23

Replying to [comment:11 slabbe]:

> Having doc in the top of the module (for web doc browsing) vs in the
> the class (for ?  interactive doc browsing) is a good question.

Yup.

> One answer could be to copy the same information in both place...

Nah, don't duplicate. Better one good piece of documentation than two
things that will diverge.

> At least now, there is a link at the top of the module linking to
> the class...

I aim to put class-specific documentation in the class (so that it can
be accessed by introspection on the class; that's often how the user
will get to that). And when there is more than one class, to put an
overview/tutorial in the module. With cross links.

Cheers,
                                   Nicolas
