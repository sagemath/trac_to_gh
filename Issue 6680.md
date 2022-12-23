# Issue 6680: [with patch, needs review]  (uses Linear Programming)

archive/issues_006680.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  tombuc\n\nHello everybody !!!\n\nHere are several new functions for the Graph class in Sage : \n* def min_dominating_set(g, value_only=False,log=0):\n* def min_independent_dominating_set(g, value_only=False,log=0):\n* def min_vertex_cover(g,value_only=False,log=0):\n* def max_matching(g,value_only=False, use_edge_labels=True):\n* def max_flow(g,x,y,value_only=True,integer=False, use_edge_labels=True):\n* def min_edge_cut(g,s,t,value_only=True,use_edge_labels=True):\n* def min_vertex_cut(g,s,t,value_only=True):\n* def edge_connectivity(g,value_only=True,use_edge_labels=True):\n* def vertex_connectivity(g,value_only=True):\n\nThose new functions all use Linear programming, so to use them you will have to install the patches MIP-1 to MIP-5 in #6502 along with the package GLPK :\n\nhttp://trac.sagemath.org/sage_trac/ticket/6502\n\nIf you want them to be even more efficient, you can also install COIN-OR/CBC ( from #6603 ) with this line :\n\nsage -f http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.spkg\n\nI am sorry for sending a patch with so many functions at once, but most of them only take ten or twenty lines and the linear programs should be pretty elementary. Hopefully, these functions can be reviewed independently as most of them are not related to each other.\n\n( I have to add that I will be absent next week, but even though I will be able to answer any of your questions and to post fixes until tomorrow evening. I chosed to post these two functions now hoping they could be integrated with the patch for LP into the next release of Sage )\n\nIssue created by migration from https://trac.sagemath.org/ticket/6680\n\n",
    "created_at": "2009-08-06T15:38:33Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review]  (uses Linear Programming)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6680",
    "user": "ncohen"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/6680





---

archive/issue_comments_054910.json:
```json
{
    "body": "test",
    "created_at": "2009-08-06T15:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6680#issuecomment-54910",
    "user": "was"
}
```

test



---

archive/issue_comments_054911.json:
```json
{
    "body": "As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.\n\nSorry for the trouble, I'll try to make it quick !\n\nNathann",
    "created_at": "2009-08-31T15:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6680#issuecomment-54911",
    "user": "ncohen"
}
```

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann



---

archive/issue_comments_054912.json:
```json
{
    "body": "New version attached !! Will put some energy into Sage's graph library ! ;-)",
    "created_at": "2009-09-04T21:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6680#issuecomment-54912",
    "user": "ncohen"
}
```

New version attached !! Will put some energy into Sage's graph library ! ;-)



---

archive/issue_comments_054913.json:
```json
{
    "body": "Attachment\n\nI am splitting this ticket into smallers ones",
    "created_at": "2009-12-03T14:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6680#issuecomment-54913",
    "user": "ncohen"
}
```

Attachment

I am splitting this ticket into smallers ones



---

archive/issue_comments_054914.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-12-04T18:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6680#issuecomment-54914",
    "user": "ncohen"
}
```

Resolution: duplicate



---

archive/issue_comments_054915.json:
```json
{
    "body": "Totally duplicated ! See :\n\n#7592   Flow method using LP\n#7593 \tMatching using LP \n#7594 \tDominating set and Independent dominating Set \n#7599 \tvertex_cut and edge_cut ( minimum s-t cut ) \n#7600 \tVertex cover\n#7601 \tGraph.edge_connectivity\n#7605 \tGraph.vertex_connectivity\n\nCan be closed as duplicate.",
    "created_at": "2009-12-04T18:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6680#issuecomment-54915",
    "user": "ncohen"
}
```

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

archive/issue_comments_054916.json:
```json
{
    "body": "Let's say :\n* #7592 Flow method using LP \n* #7593 Matching using LP \n* #7594 Dominating set and Independent dominating Set \n* #7599 vertex_cut and edge_cut ( minimum s-t cut ) \n* #7600 Vertex cover \n* #7601 Graph.edge_connectivity \n* #7605 Graph.vertex_connectivity",
    "created_at": "2009-12-04T18:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6680#issuecomment-54916",
    "user": "ncohen"
}
```

Let's say :
* #7592 Flow method using LP 
* #7593 Matching using LP 
* #7594 Dominating set and Independent dominating Set 
* #7599 vertex_cut and edge_cut ( minimum s-t cut ) 
* #7600 Vertex cover 
* #7601 Graph.edge_connectivity 
* #7605 Graph.vertex_connectivity
