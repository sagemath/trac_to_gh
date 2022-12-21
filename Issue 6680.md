# Issue 6680: [with patch, needs review]  (uses Linear Programming)

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-08-06 15:38:33

Assignee: rlm

CC:  tombuc

Hello everybody !!!

Here are several new functions for the Graph class in Sage : 
* def min_dominating_set(g, value_only=False,log=0):
* def min_independent_dominating_set(g, value_only=False,log=0):
* def min_vertex_cover(g,value_only=False,log=0):
* def max_matching(g,value_only=False, use_edge_labels=True):
* def max_flow(g,x,y,value_only=True,integer=False, use_edge_labels=True):
* def min_edge_cut(g,s,t,value_only=True,use_edge_labels=True):
* def min_vertex_cut(g,s,t,value_only=True):
* def edge_connectivity(g,value_only=True,use_edge_labels=True):
* def vertex_connectivity(g,value_only=True):

Those new functions all use Linear programming, so to use them you will have to install the patches MIP-1 to MIP-5 in #6502 along with the package GLPK :

http://trac.sagemath.org/sage_trac/ticket/6502

If you want them to be even more efficient, you can also install COIN-OR/CBC ( from #6603 ) with this line :

sage -f http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.spkg

I am sorry for sending a patch with so many functions at once, but most of them only take ten or twenty lines and the linear programs should be pretty elementary. Hopefully, these functions can be reviewed independently as most of them are not related to each other.

( I have to add that I will be absent next week, but even though I will be able to answer any of your questions and to post fixes until tomorrow evening. I chosed to post these two functions now hoping they could be integrated with the patch for LP into the next release of Sage )


---

Comment by was created at 2009-08-06 15:51:15

test


---

Comment by ncohen created at 2009-08-31 15:55:03

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann


---

Comment by ncohen created at 2009-09-04 21:54:03

New version attached !! Will put some energy into Sage's graph library ! ;-)


---

Attachment

I am splitting this ticket into smallers ones


---

Comment by ncohen created at 2009-12-04 18:31:49

Resolution: duplicate


---

Comment by ncohen created at 2009-12-04 18:31:49

Totally duplicated ! See :

#7592   Flow method using LP
#7593 	Matching using LP 
#7594 	Dominating set and Independent dominating Set 
#7599 	vertex_cut and edge_cut ( minimum s-t cut ) 
#7600 	Vertex cover
#7601 	Graph.edge_connectivity
#7605 	Graph.vertex_connectivity

Can be closed as duplicate.


---

Comment by ncohen created at 2009-12-04 18:32:41

Let's say :
* #7592 Flow method using LP 
* #7593 Matching using LP 
* #7594 Dominating set and Independent dominating Set 
* #7599 vertex_cut and edge_cut ( minimum s-t cut ) 
* #7600 Vertex cover 
* #7601 Graph.edge_connectivity 
* #7605 Graph.vertex_connectivity
