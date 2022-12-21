# Issue 7314: Average distance, Wiener Index, Szeged index

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-26 16:09:59

Assignee: rlm

Hello !!

This patch defines :
    * The average distance between vertices : Graph.average_distance
    * The Szeged Index of a graph : Graph.szeged_index
    * The Wiener Index of a graph : Graph.wiener_index

Everything this patch adds (except the average distance) is documented in :
http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TY9-3VVCHY8-9&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&_docanchor=&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=6d22be39b064af51023439c3bb59c459

This reference is mentioned in the docstrings.

Nathann



---

Comment by ncohen created at 2009-10-26 16:12:22

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-10-26 16:59:43

In the docstrings, you should not put comments on the sage: line like in 


```
EXAMPLE:: 

    sage: # From [2], cited in [1] 
    sage: g=graphs.PathGraph(10) 
    sage: w=lambda x: (x*(x*x -1)/6) 
    sage: g.wiener_index()==w(10) 
    True 
```


Instead, it should be


```
EXAMPLE:

From [2], cited in [1]::

    sage: g=graphs.PathGraph(10) 
    sage: w=lambda x: (x*(x*x -1)/6) 
    sage: g.wiener_index()==w(10) 
    True 
```


Also, you should see the way that references are handled elsewhere in the Sage library.


---

Comment by ncohen created at 2009-10-26 19:03:28

I hope you will prefer this one ! I had taken as examples other docstrings which you may find badly formatted... This time, I took as an example Minh's code from Cliques functiosn, knowing that never I witnessed Minh making the slightest error :-)

Nathann


---

Comment by rlm created at 2009-12-15 17:17:02

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mhansen created at 2009-12-15 17:29:02

Resolution: fixed
