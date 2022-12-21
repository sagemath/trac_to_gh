# Issue 4916: convert sage.lfunctions.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:52:38

Assignee: tba




---

Attachment


---

Comment by robertwb created at 2009-02-12 21:35:21

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

Comment by mhansen created at 2009-02-17 16:06:48

Could you explain 


```
Another note, the EXAMPLES:: seems redundant, would it make sense to replace EXAMPLES: with EXAMPLES:: (same with TESTS, etc.) Or perhaps all sage: blocks could automatically be detected (doesn't seem too hard).
```



a bit more?  I wasn't quite sure what you were saying.

The "sage:" blocks are automatically picked up by the doctesting framework, but ReST uses the "::" to denote a verbatim block.

I've also fixed the above issue ( http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/lfunctions/dokchitser.html ).  Notice that the formatting is currently butchered in the current reference manual http://sagemath.org/doc/ref/module-sage.lfunctions.dokchitser.html


---

Comment by robertwb created at 2009-02-18 03:08:20

Sorry for not being clear enough. What I meant was :: seems to proceed every sage code block. It seems that ReST could be modified/enhanced to detect the same and automatically know that it's a verbatim block.


---

Comment by mabshoff created at 2009-02-24 18:54:42

Resolution: fixed


---

Attachment

Merged in Sage 3.4.alpha0.

Cheers,

Michael
