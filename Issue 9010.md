# Issue 9010: Upgrade biopython package to 1.54

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2010-05-21 16:23:37

Assignee: tbd

CC:  awebb

A new biopython package was released May 20, 2010.  


---

Comment by mhampton created at 2010-05-21 16:25:09

A first attempt is up at:
[http://sage.math.washington.edu/home/mhampton/biopython-1.54.p0.spkg](http://sage.math.washington.edu/home/mhampton/biopython-1.54.p0.spkg)

I didn't change anything except upgrading the src folder and noting the upgrade in SPKG.txt.


---

Comment by awebb created at 2010-05-25 08:19:28

My first look at it is good. I installed (SAGE_CHECK=yes) on two machines (32 and 64 bit Linux). The self test passed and my two test worksheets passed. One is just a short sheet and the other is the first three chapters of the tutorial. 

Adam


---

Comment by awebb created at 2010-05-25 10:51:49

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

Comment by jason created at 2010-06-11 07:46:12

Should this be "needs review"?


---

Comment by mhampton created at 2010-06-11 17:35:43

I think it should be "positive review", but someone else should do that.  I have been using it for weeks on linux and os x versions of sage with no problems.  Given the upstream testing on this, and the fact that its an optional package, I don't see why it should be held back.


---

Comment by mhampton created at 2010-06-11 17:35:43

Changing status from new to needs_review.


---

Comment by awebb created at 2010-06-13 18:21:46

I was going to give it a positive review originally but was uncertain in regards to the networkx related error. Is this only on my setup? Should this be a ticket for networkx? The other plotting options worked for me so is this fine for an optional package? I assume that perfection is not required.

In any case, I think that the biopython package is fine as an optional package. 

Adam


---

Comment by awebb created at 2010-06-13 18:21:46

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-02 22:32:36

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-07-02 22:32:36

The optional biopython package on the website is already at `.p0`. Did someone already do this, or should the one here be a `.p1`?


---

Comment by rlm created at 2010-07-02 22:32:42

Changing status from needs_work to needs_info.


---

Comment by rlm created at 2010-07-02 22:33:22

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2010-07-02 22:33:22

Oops, nevermind, I see the version number change.


---

Comment by rlm created at 2010-07-02 22:33:28

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-02 22:39:04

Not sure about the merged-in field, but why not?

"Updated on 2 July 2010."


---

Comment by rlm created at 2010-07-02 22:39:04

Resolution: fixed
