# Issue 9757: implement Watkins-Delaunay's algorithm for computing modular degrees in Sage

Issue created by migration from https://trac.sagemath.org/ticket/9758

Original creator: was

Original creation time: 2010-08-17 22:29:48

Assignee: was

CC:  mpatel robertwb cremona

Relevant paper:

    http://www.emis.ams.org/journals/EM/expmath/volumes/11/11.4/pp487_502.pdf

When this is done and of comparable speed to the current modular degree code in Sage, then Sympow can be moved from standard to optional (or worse) as a Sage spkg.  Implementation options:

   * Build on top of the Dokchiter l-series code in Sage (via PARI)

   * Build something on Robert Bradshaw's soon-to-be-in-Sage re-implementation of Dokchitser:   #9193


---

Comment by was created at 2010-08-19 00:11:43

Kirkby said:
> It would be good to state on the ticket what level of student project
> this is (undergrad, postgrad), and the skill set needed (C, Python
> etc). I expect you would prefer it in Python, though I think
> personally a C implementation like Mark's, which you can easily call
> from Python, would be more beneficial to the scientific community in
> general - not everyone is using Sage/Python.

Good idea.  

Level: graduate student or greater, with a background in number theory.

Skill set needed:  read C, write Python, possibly Cython later for speed purposes. 

C versus Python: the implementation can depend on absolutely anything in Sage; for this I'm not concerned about providing a general tool for the scientific community.


---

Comment by drkirkby created at 2010-08-31 09:49:18

I'm adding John Cremona to this, as I think this is his area of interest. If not, John can delete himself!

For anyone taking this project on, it may be useful to know that in the opinion of Mark Watkins, double-precsion maths is *probably* good enough for computing the modular degrees. That would no doubt make the code simpler and faster than using MPFR. See

http://groups.google.co.uk/group/sage-devel/msg/ecac09831622179c

Strange as it may seem, fixing the SYMPOW bug (#9703) was actually one of the more interesting changes I've made to Sage. It required reading the paper in the quad double package to understand how that was supposed to work, then reading the Intel manual on the 387 processor to sort out how to get the processor to work as required by quad double. 

Dave


---

Comment by cremona created at 2012-09-29 22:07:00

Here's one case which can be used for testing (I have correspondence with Mark Watkins which explains the problem and how to fix it, and will open a new ticket for that):

```
sage: E = EllipticCurve([1,-1,0,-318360868065,-69208434591226115]) 
sage: E.modular_degree(algorithm='magma')                         
2417135616
```

but

```
sage: E = EllipticCurve([1,-1,0,-318360868065,-69208434591226115]) 
sage: E.modular_degree()    
# boom
```

