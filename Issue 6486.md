# Issue 6486: minimum distance of all 0 code raised mysterious error message

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2009-07-08 18:40:40

Assignee: rlm

This should return a more useful error message:


```
sage: G = matrix(GF(2),[This is the Trac macro *0,0,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0,0,0-macro))
sage: C = LinearCode(G)
sage: C.list()
[(0, 0, 0)]
sage: C.minimum_distance()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/wdj/.sage/temp/tinah/7902/_home_wdj__sage_init_sage_0.py in <module>()

/home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/coding/linear_code.pyc in minimum_distance(self, method)
   1681             return ZZ(d)
   1682         Gstr = "%s*Z(%s)^0"%(gapG, q)
-> 1683         return hamming_weight(min_wt_vec_gap(Gstr,n,k,F))
   1684
   1685     def module_composition_factors(self,gp):

/home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/sage/coding/linear_code.pyc in min_wt_vec_gap(Gmat, n, k, F, method)
    379         #print [gap.eval("v["+str(i+1)+"]") for i in range(n)]
    380         all.append([v._matrix_(F),m._matrix_(F),int(dist)])
--> 381     ans = all[0]
    382     for x in all:
    383         if x[2]<ans[2] and x[2]>0:

IndexError: list index out of range
```



---

Attachment

Adds some documentation and handles the min distance problem


---

Comment by spancratz created at 2010-01-19 23:47:01

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-01-20 22:40:19

Changing status from needs_review to positive_review.


---

Comment by craigcitro created at 2010-01-20 22:40:19

This looks good. *Tons* of nice cleanup, and it's clearly the right fix for the bug on the ticket.


---

Comment by mvngu created at 2010-01-23 06:11:54

Resolution: fixed
