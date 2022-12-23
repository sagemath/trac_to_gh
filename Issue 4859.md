# Issue 4859: basic covering design module

Issue created by migration from https://trac.sagemath.org/ticket/4859

Original creator: dgordon

Original creation time: 2008-12-23 17:18:59

Assignee: mhansen

CC:  sage-combinat

I maintain a database of covering designs (k-subsets of a v-set such that all t-sets are
in at least one of the k-sets) at http://www.ccrwest.org/cover.html.  This patch implements
covering designs in Sage using the IncidenceStructure class, and allows a user to get coverings
from the website.


---

Attachment


---

Comment by wdj created at 2008-12-23 21:08:37

Two minor comments:

(1) I'm confused by this docstring


```
A $(v,k,t)$ covering design $C$ is an incidence structure ...
```


combined with this behaviour:



```
sage: C = best_known_covering_design_www(7, 3, 2); C
<class 'sage.combinat.designs.covering_design.CoveringDesign'>
sage: D = C.incidence_structure
sage: type(D)
<class 'sage.combinat.designs.incidence_structures.IncidenceStructure'>
```


D is an incidence structure but the way of creating D seems slightly nonstandard.
Why not


```
sage: D = C.incidence_structure()
```

instead? I'm not saying change this, just wondering why it is the way it is.

(2) For future reference, the patch naming is slightly non-standard (trac_4859-covering-designs.patch or something like that is more typical).


---

Comment by wdj created at 2008-12-30 02:56:27

Got an email from Dan that he plans to go some minor modifications, after while I'll give this a positive review.


---

Comment by was created at 2009-01-20 07:40:08

REFEREE REPORT:

The overall style of the code looks really good.

 * This worries me:

```
        82	    bound = 1.0 
 	83	    for i in range(t-1,-1,-1): 
 	84	        bound = (bound*RDF(v-i)/RDF(k-i)).ceiling() 
 	85	 
 	86	    return bound 
```

I'm worried about overflow.  Maybe using interval arithmetic would be better, i.e., the real interval field.  You could make a comment about why precision isn't an issue, but I sort of wonder. 


 *  I think it might be nice to avoid confusion if you make all the attributes private (i.e., put an underscore (or two) in the beginning of their names), then have methods to access them, e.g., 

```
This is bad:
sage:  C=CoveringDesign(7,3,2,7,range(7),[[0, 1, 2], [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6], [2, 3, 6], [2, 4, 5]],0, 'Projective Plane')
sage: C.method
'Projective Plane'
sage: C.method = 'foo bar'
sage: C.method
'foo bar'

This is better:
sage: C.method()
'Projective Plane'
sage: C.method?
lots of nice documentation about what the C.__method *means* and how to use it. 
```

Do the same with all the other attributes.   This is for consistency with the rest of Sage, and because it is easier for users. 

 * You defined a `show` method. This is reserved for graphical display.   Instead call that method `_repr_`, so it gets automatically picked up by the print and str(...) methods.   Also `_repr_` should return a string instead of using the print command. 

 * change ` requires internet, optional ` to `optional -- requires internet`.  Doing that isn't documented anywhere, but it's the "new way" now that I wrote an optional doctesting framework that really singles out various components. 


With the above issues addressed, this code should go into sage.


---

Attachment

fix to problems in first patch pointed out by the reviewers


---

Comment by wdj created at 2009-01-28 00:06:41

Both patches (in order) apply cleanly to 3.3.alpha1. They pass sage -t and sage -t -optional. 

Looks good to me.


---

Comment by was created at 2009-01-28 01:57:16

MABSHOFF -- when you apply this patch, make sure to add Dan Gordon as an official Sage developer somehow to the list.


---

Comment by mabshoff created at 2009-01-28 13:02:47

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 13:02:47

Merged both patches into Sage 3.3.alpha3.

Cheers,

Michael
