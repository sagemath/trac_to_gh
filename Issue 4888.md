# Issue 4888: laplacian_matrix() broken for DiGraphs

archive/issues_004888.json:
```json
{
    "body": "Assignee: @rlmill\n\nDavid reports in http://groups.google.com/group/sage-devel/t/51fdef25ed45ceee\n\n\n```\nI am running Sage 3.1.4 under Fedora 9 and have found a bug in the \nfile graph.py. \n------------------------------------------------------------------- \nsage: G = DiGraph({0:{}, 1:{0:1}, 2:{0:1}}, weighted = True) \nsage: G.weighted_adjacency_matrix() \n[0] \n[1] \n[1] \nsage: G.adjacency_matrix() \n[0 0 0] \n[1 0 0] \n[1 0 0] \nsage: G.laplacian_matrix() \n--------------------------------------------------------------------------- \nIndexError                                Traceback (most recent call \nlast) \n/home/davidp/.sage/temp/xyzzy/16886/ \n_home_davidp_math_sandpile_sage_sandpile_sage_14.py in <module>() \n----> 1 \n      2 \n      3 \n      4 \n      5 \n/usr/local/sage-3.1.4-fc8-i686-Linux/local/lib/python2.5/site-packages/ \nsage/graphs/graph.pyc in kirchhoff_matrix(self, weighted, \nboundary_first) \n    904         S = [sum(M.row(i)) for i in range(M.nrows())] \n    905         for i in range(len(A)): \n--> 906             A[i][i] = S[i] \n    907         return M.parent()(A) \n    908 \n/usr/local/sage-3.1.4-fc8-i686-Linux/local/lib/python2.5/site-packages/ \nsage/modules/free_module_element.so in \nsage.modules.free_module_element.FreeModuleElement_generic_sparse.__setitem __ \n(sage/modules/free_module_element.c:15074)() \n   1765 \n   1766 \n-> 1767 \n   1768 \n   1769 \nIndexError: index (i=1) must be between 0 and 0 \nsage: \n--------------------------------------------------------------------------- --------- \nThe laplacian_matrix function is not working because \nweighted_adjacency matrix is not returning a square matrix.  A \nsuggested fix is to change line 845 (in the graph.py code for \nweighted_adjacency_matrix) from \nM = matrix(D, sparse=sparse) \nto \nM = matrix(self.num_verts(), D, sparse=sparse) \nDavid \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4888\n\n",
    "created_at": "2008-12-29T21:56:16Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "laplacian_matrix() broken for DiGraphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4888",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @rlmill

David reports in http://groups.google.com/group/sage-devel/t/51fdef25ed45ceee


```
I am running Sage 3.1.4 under Fedora 9 and have found a bug in the 
file graph.py. 
------------------------------------------------------------------- 
sage: G = DiGraph({0:{}, 1:{0:1}, 2:{0:1}}, weighted = True) 
sage: G.weighted_adjacency_matrix() 
[0] 
[1] 
[1] 
sage: G.adjacency_matrix() 
[0 0 0] 
[1 0 0] 
[1 0 0] 
sage: G.laplacian_matrix() 
--------------------------------------------------------------------------- 
IndexError                                Traceback (most recent call 
last) 
/home/davidp/.sage/temp/xyzzy/16886/ 
_home_davidp_math_sandpile_sage_sandpile_sage_14.py in <module>() 
----> 1 
      2 
      3 
      4 
      5 
/usr/local/sage-3.1.4-fc8-i686-Linux/local/lib/python2.5/site-packages/ 
sage/graphs/graph.pyc in kirchhoff_matrix(self, weighted, 
boundary_first) 
    904         S = [sum(M.row(i)) for i in range(M.nrows())] 
    905         for i in range(len(A)): 
--> 906             A[i][i] = S[i] 
    907         return M.parent()(A) 
    908 
/usr/local/sage-3.1.4-fc8-i686-Linux/local/lib/python2.5/site-packages/ 
sage/modules/free_module_element.so in 
sage.modules.free_module_element.FreeModuleElement_generic_sparse.__setitem __ 
(sage/modules/free_module_element.c:15074)() 
   1765 
   1766 
-> 1767 
   1768 
   1769 
IndexError: index (i=1) must be between 0 and 0 
sage: 
--------------------------------------------------------------------------- --------- 
The laplacian_matrix function is not working because 
weighted_adjacency matrix is not returning a square matrix.  A 
suggested fix is to change line 845 (in the graph.py code for 
weighted_adjacency_matrix) from 
M = matrix(D, sparse=sparse) 
to 
M = matrix(self.num_verts(), D, sparse=sparse) 
David 
```


Issue created by migration from https://trac.sagemath.org/ticket/4888





---

archive/issue_comments_036977.json:
```json
{
    "body": "I agree with David's proposed fix, and blame boothby ;)",
    "created_at": "2009-01-04T18:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4888#issuecomment-36977",
    "user": "https://github.com/rlmill"
}
```

I agree with David's proposed fix, and blame boothby ;)



---

archive/issue_comments_036978.json:
```json
{
    "body": "Let's get this into 3.3 then.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T19:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4888#issuecomment-36978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Let's get this into 3.3 then.

Cheers,

Michael



---

archive/issue_comments_036979.json:
```json
{
    "body": "Attachment [trac_4888.patch](tarball://root/attachments/some-uuid/ticket4888/trac_4888.patch) by mabshoff created at 2009-01-18 05:53:14\n\nPositive review for the fix suggested by rlm. I have attached the patch with a doctest and it passes `-t -long` with my current merge tree. Credit for authorship goes to David Perkinson in whose name I committed the patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T05:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4888#issuecomment-36979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4888.patch](tarball://root/attachments/some-uuid/ticket4888/trac_4888.patch) by mabshoff created at 2009-01-18 05:53:14

Positive review for the fix suggested by rlm. I have attached the patch with a doctest and it passes `-t -long` with my current merge tree. Credit for authorship goes to David Perkinson in whose name I committed the patch.

Cheers,

Michael



---

archive/issue_comments_036980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T05:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4888#issuecomment-36980",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036981.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T05:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4888#issuecomment-36981",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
