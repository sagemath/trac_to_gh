# Issue 4916: convert sage.lfunctions.* docstrings to Sphinx

archive/issues_004916.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4916\n\n",
    "created_at": "2009-01-01T22:52:38Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.lfunctions.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4916",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4916





---

archive/issue_comments_037236.json:
```json
{
    "body": "Attachment [trac_4916.patch](tarball://root/attachments/some-uuid/ticket4916/trac_4916.patch) by @mwhansen created at 2009-01-02 02:32:43",
    "created_at": "2009-01-02T02:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4916#issuecomment-37236",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4916.patch](tarball://root/attachments/some-uuid/ticket4916/trac_4916.patch) by @mwhansen created at 2009-01-02 02:32:43



---

archive/issue_comments_037237.json:
```json
{
    "body": "Just looking at the patch looks mostly good, is this rendered somewhere to look at? \n\nAlso, I noticed significant readability degradation plain text documentation: \n\n\n```\n        conductor -- integer, the conductor \n48\t \t        gammaV -- list of Gamma-factor parameters, \n49\t \t                  e.g. [0] for Riemann zeta, [0,1] for ell.curves, \n50\t \t                  (see examples). \n51\t \t        weight -- positive real number, usually an integer \n52\t \t                  e.g. 1 for Riemann zeta, 2 for $H^1$ of curves/$\\Q$ \n53\t \t        eps   --  complex number; sign in functional equation \n54\t \t        poles --  (default: []) list of points where $L^*(s)$ has (simple) poles; \n55\t \t                  only poles with Re(s)>weight/2 should be included \n56\t \t        residues -- vector of residues of $L^*(s)$ in those poles \n57\t \t                    or set residues='automatic' (default value) \n58\t \t        prec -- integer (default: 53) number of *bits* of precision \n```\n\n\n vs\n \n\n```\n \t50\t     \n \t51\t    conductor - integer, the conductor gammaV - list of Gamma-factor \n \t52\t    parameters, e.g. [0] for Riemann zeta, [0,1] for ell.curves, (see \n \t53\t    examples). weight - positive real number, usually an integer e.g. 1 \n \t54\t    for Riemann zeta, 2 for `H^1` of \n \t55\t    curves/`\\mathbb{Q}` eps - complex number; sign in \n \t56\t    functional equation poles - (default: []) list of points where \n \t57\t    `L^*(s)` has (simple) poles; only poles with Re(s)weight/2 \n \t58\t    should be included residues - vector of residues of \n \t59\t    `L^*(s)` in those poles or set residues='automatic' \n \t60\t    (default value) prec - integer (default: 53) number of *bits* of \n \t61\t    precision \n```\n\n\nAnother note, the EXAMPLES:: seems redundant, would it make sense to replace EXAMPLES: with EXAMPLES:: (same with TESTS, etc.) Or perhaps all sage: blocks could automatically be detected (doesn't seem too hard).",
    "created_at": "2009-02-12T21:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4916#issuecomment-37237",
    "user": "https://github.com/robertwb"
}
```

Just looking at the patch looks mostly good, is this rendered somewhere to look at? 

Also, I noticed significant readability degradation plain text documentation: 


```
        conductor -- integer, the conductor 
48	 	        gammaV -- list of Gamma-factor parameters, 
49	 	                  e.g. [0] for Riemann zeta, [0,1] for ell.curves, 
50	 	                  (see examples). 
51	 	        weight -- positive real number, usually an integer 
52	 	                  e.g. 1 for Riemann zeta, 2 for $H^1$ of curves/$\Q$ 
53	 	        eps   --  complex number; sign in functional equation 
54	 	        poles --  (default: []) list of points where $L^*(s)$ has (simple) poles; 
55	 	                  only poles with Re(s)>weight/2 should be included 
56	 	        residues -- vector of residues of $L^*(s)$ in those poles 
57	 	                    or set residues='automatic' (default value) 
58	 	        prec -- integer (default: 53) number of *bits* of precision 
```


 vs
 

```
 	50	     
 	51	    conductor - integer, the conductor gammaV - list of Gamma-factor 
 	52	    parameters, e.g. [0] for Riemann zeta, [0,1] for ell.curves, (see 
 	53	    examples). weight - positive real number, usually an integer e.g. 1 
 	54	    for Riemann zeta, 2 for `H^1` of 
 	55	    curves/`\mathbb{Q}` eps - complex number; sign in 
 	56	    functional equation poles - (default: []) list of points where 
 	57	    `L^*(s)` has (simple) poles; only poles with Re(s)weight/2 
 	58	    should be included residues - vector of residues of 
 	59	    `L^*(s)` in those poles or set residues='automatic' 
 	60	    (default value) prec - integer (default: 53) number of *bits* of 
 	61	    precision 
```


Another note, the EXAMPLES:: seems redundant, would it make sense to replace EXAMPLES: with EXAMPLES:: (same with TESTS, etc.) Or perhaps all sage: blocks could automatically be detected (doesn't seem too hard).



---

archive/issue_comments_037238.json:
```json
{
    "body": "Could you explain \n\n\n```\nAnother note, the EXAMPLES:: seems redundant, would it make sense to replace EXAMPLES: with EXAMPLES:: (same with TESTS, etc.) Or perhaps all sage: blocks could automatically be detected (doesn't seem too hard).\n```\n\n\n\na bit more?  I wasn't quite sure what you were saying.\n\nThe \"sage:\" blocks are automatically picked up by the doctesting framework, but ReST uses the \"::\" to denote a verbatim block.\n\nI've also fixed the above issue ( http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/lfunctions/dokchitser.html ).  Notice that the formatting is currently butchered in the current reference manual http://sagemath.org/doc/ref/module-sage.lfunctions.dokchitser.html",
    "created_at": "2009-02-17T16:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4916#issuecomment-37238",
    "user": "https://github.com/mwhansen"
}
```

Could you explain 


```
Another note, the EXAMPLES:: seems redundant, would it make sense to replace EXAMPLES: with EXAMPLES:: (same with TESTS, etc.) Or perhaps all sage: blocks could automatically be detected (doesn't seem too hard).
```



a bit more?  I wasn't quite sure what you were saying.

The "sage:" blocks are automatically picked up by the doctesting framework, but ReST uses the "::" to denote a verbatim block.

I've also fixed the above issue ( http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/lfunctions/dokchitser.html ).  Notice that the formatting is currently butchered in the current reference manual http://sagemath.org/doc/ref/module-sage.lfunctions.dokchitser.html



---

archive/issue_comments_037239.json:
```json
{
    "body": "Sorry for not being clear enough. What I meant was :: seems to proceed every sage code block. It seems that ReST could be modified/enhanced to detect the same and automatically know that it's a verbatim block.",
    "created_at": "2009-02-18T03:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4916#issuecomment-37239",
    "user": "https://github.com/robertwb"
}
```

Sorry for not being clear enough. What I meant was :: seems to proceed every sage code block. It seems that ReST could be modified/enhanced to detect the same and automatically know that it's a verbatim block.



---

archive/issue_comments_037240.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4916#issuecomment-37240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011334.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-24T18:54:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4916",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4916#event-11334"
}
```



---

archive/issue_comments_037241.json:
```json
{
    "body": "Attachment [sage.lfunctions-final.patch](tarball://root/attachments/some-uuid/ticket4916/sage.lfunctions-final.patch) by mabshoff created at 2009-02-24 18:54:42\n\nMerged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4916#issuecomment-37241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage.lfunctions-final.patch](tarball://root/attachments/some-uuid/ticket4916/sage.lfunctions-final.patch) by mabshoff created at 2009-02-24 18:54:42

Merged in Sage 3.4.alpha0.

Cheers,

Michael
