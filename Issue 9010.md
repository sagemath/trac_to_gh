# Issue 9010: Upgrade biopython package to 1.54

archive/issues_009010.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @maxthemouse\n\nA new biopython package was released May 20, 2010.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/9010\n\n",
    "created_at": "2010-05-21T16:23:37Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Upgrade biopython package to 1.54",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: tbd

CC:  @maxthemouse

A new biopython package was released May 20, 2010.  

Issue created by migration from https://trac.sagemath.org/ticket/9010





---

archive/issue_comments_083207.json:
```json
{
    "body": "A first attempt is up at:\n[http://sage.math.washington.edu/home/mhampton/biopython-1.54.p0.spkg](http://sage.math.washington.edu/home/mhampton/biopython-1.54.p0.spkg)\n\nI didn't change anything except upgrading the src folder and noting the upgrade in SPKG.txt.",
    "created_at": "2010-05-21T16:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

A first attempt is up at:
[http://sage.math.washington.edu/home/mhampton/biopython-1.54.p0.spkg](http://sage.math.washington.edu/home/mhampton/biopython-1.54.p0.spkg)

I didn't change anything except upgrading the src folder and noting the upgrade in SPKG.txt.



---

archive/issue_comments_083208.json:
```json
{
    "body": "My first look at it is good. I installed (SAGE_CHECK=yes) on two machines (32 and 64 bit Linux). The self test passed and my two test worksheets passed. One is just a short sheet and the other is the first three chapters of the tutorial. \n\nAdam",
    "created_at": "2010-05-25T08:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83208",
    "user": "https://github.com/maxthemouse"
}
```

My first look at it is good. I installed (SAGE_CHECK=yes) on two machines (32 and 64 bit Linux). The self test passed and my two test worksheets passed. One is just a short sheet and the other is the first three chapters of the tutorial. 

Adam



---

archive/issue_comments_083209.json:
```json
{
    "body": "I tried the new Phylo module and it is nice. I had a problem with one example with networkx. (files in Tests/PhyloXML)\n\n```\nsage: from Bio import Phylo\nsage: import networkx, pylab\nsage: tree = Phylo.read('example.xml', 'phyloxml')\nsage: net = Phylo.to_networkx(tree)\nsage: networkx.draw(net)\nTypeError                                 Traceback (most recent call last)\n\n/home/adamwebb/download/biopython-1.54.p0/src/Tests/PhyloXML/<ipython console> in <module>()\n\n/home/math/sage/local/lib/python/networkx/drawing/nx_pylab.pyc in draw(G, pos, ax, hold, **kwds)\n    108\n    109     if pos is None:\n--> 110         pos=networkx.drawing.spring_layout(G) # default to spring layout\n    111\n    112     cf=pylab.gcf()\n\n/home/math/sage/local/lib/python/networkx/drawing/layout.pyc in fruchterman_reingold_layout(G, dim, pos, fixed, iterations, weighted, scale)\n    209                                          weighted=weighted)\n    210     except:\n--> 211         A=networkx.to_numpy_matrix(G)\n    212         pos=_fruchterman_reingold(A,\n    213                                   pos=pos_arr,\n\n/home/math/sage/local/lib/python/networkx/convert.pyc in to_numpy_matrix(G, nodelist, dtype, order)\n    478         if (u in nodeset) and (v in nodeset):\n    479             i,j = index[u],index[v]\n--> 480             M[i,j] += attrs.get('weight', 1)\n    481             if undirected:\n    482                 M[j,i] = M[i,j]\n\nTypeError: unsupported operand type(s) for +=: 'numpy.float64' and 'str'\n\n```\n\n\nThe next line would be.\nsage: pylab.show()\n\n\nI installed pygraphviz as well and the other graphing examples worked.\n\nAdam",
    "created_at": "2010-05-25T10:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83209",
    "user": "https://github.com/maxthemouse"
}
```

I tried the new Phylo module and it is nice. I had a problem with one example with networkx. (files in Tests/PhyloXML)

```
sage: from Bio import Phylo
sage: import networkx, pylab
sage: tree = Phylo.read('example.xml', 'phyloxml')
sage: net = Phylo.to_networkx(tree)
sage: networkx.draw(net)
TypeError                                 Traceback (most recent call last)

/home/adamwebb/download/biopython-1.54.p0/src/Tests/PhyloXML/<ipython console> in <module>()

/home/math/sage/local/lib/python/networkx/drawing/nx_pylab.pyc in draw(G, pos, ax, hold, **kwds)
    108
    109     if pos is None:
--> 110         pos=networkx.drawing.spring_layout(G) # default to spring layout
    111
    112     cf=pylab.gcf()

/home/math/sage/local/lib/python/networkx/drawing/layout.pyc in fruchterman_reingold_layout(G, dim, pos, fixed, iterations, weighted, scale)
    209                                          weighted=weighted)
    210     except:
--> 211         A=networkx.to_numpy_matrix(G)
    212         pos=_fruchterman_reingold(A,
    213                                   pos=pos_arr,

/home/math/sage/local/lib/python/networkx/convert.pyc in to_numpy_matrix(G, nodelist, dtype, order)
    478         if (u in nodeset) and (v in nodeset):
    479             i,j = index[u],index[v]
--> 480             M[i,j] += attrs.get('weight', 1)
    481             if undirected:
    482                 M[j,i] = M[i,j]

TypeError: unsupported operand type(s) for +=: 'numpy.float64' and 'str'

```


The next line would be.
sage: pylab.show()


I installed pygraphviz as well and the other graphing examples worked.

Adam



---

archive/issue_comments_083210.json:
```json
{
    "body": "Should this be \"needs review\"?",
    "created_at": "2010-06-11T07:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83210",
    "user": "https://github.com/jasongrout"
}
```

Should this be "needs review"?



---

archive/issue_comments_083211.json:
```json
{
    "body": "I think it should be \"positive review\", but someone else should do that.  I have been using it for weeks on linux and os x versions of sage with no problems.  Given the upstream testing on this, and the fact that its an optional package, I don't see why it should be held back.",
    "created_at": "2010-06-11T17:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83211",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I think it should be "positive review", but someone else should do that.  I have been using it for weeks on linux and os x versions of sage with no problems.  Given the upstream testing on this, and the fact that its an optional package, I don't see why it should be held back.



---

archive/issue_comments_083212.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-11T17:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83212",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083213.json:
```json
{
    "body": "I was going to give it a positive review originally but was uncertain in regards to the networkx related error. Is this only on my setup? Should this be a ticket for networkx? The other plotting options worked for me so is this fine for an optional package? I assume that perfection is not required.\n\nIn any case, I think that the biopython package is fine as an optional package. \n\nAdam",
    "created_at": "2010-06-13T18:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83213",
    "user": "https://github.com/maxthemouse"
}
```

I was going to give it a positive review originally but was uncertain in regards to the networkx related error. Is this only on my setup? Should this be a ticket for networkx? The other plotting options worked for me so is this fine for an optional package? I assume that perfection is not required.

In any case, I think that the biopython package is fine as an optional package. 

Adam



---

archive/issue_comments_083214.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-13T18:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83214",
    "user": "https://github.com/maxthemouse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083215.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-02T22:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83215",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083216.json:
```json
{
    "body": "The optional biopython package on the website is already at `.p0`. Did someone already do this, or should the one here be a `.p1`?",
    "created_at": "2010-07-02T22:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83216",
    "user": "https://github.com/rlmill"
}
```

The optional biopython package on the website is already at `.p0`. Did someone already do this, or should the one here be a `.p1`?



---

archive/issue_comments_083217.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-07-02T22:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83217",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_083218.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-07-02T22:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83218",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_083219.json:
```json
{
    "body": "Oops, nevermind, I see the version number change.",
    "created_at": "2010-07-02T22:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83219",
    "user": "https://github.com/rlmill"
}
```

Oops, nevermind, I see the version number change.



---

archive/issue_comments_083220.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T22:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83220",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083221.json:
```json
{
    "body": "Not sure about the merged-in field, but why not?\n\n\"Updated on 2 July 2010.\"",
    "created_at": "2010-07-02T22:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83221",
    "user": "https://github.com/rlmill"
}
```

Not sure about the merged-in field, but why not?

"Updated on 2 July 2010."



---

archive/issue_comments_083222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-02T22:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9010#issuecomment-83222",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_009164.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-02T22:39:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9010",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9010#event-9164"
}
```
