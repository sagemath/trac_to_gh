# Issue 8441: Coleman-Gross local height pairing on hyperelliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/8441

Original creator: jen

Original creation time: 2010-03-05 01:26:33

Assignee: was

CC:  kedlaya

Keywords: heights, Coleman integration, hyperelliptic curves

Currently, a work in progress (lots of doctests need to be written and internal print statements removed; the code itself will be cleaned up over the next few weeks), but the main function, which computes the Coleman-Gross local height pairing at p for hyperelliptic curves, does the following:

(This example is computing h_7(D_1, D_2) and h_7(D_2, D_1), for D_1 = (P) - (Q) and D_2 = (Pprime)-(Qprime), in the notation of R. Coleman and B. Gross, p-adic heights on curves, Algebraic Number Theory, 1989, pp-73-81.)


```
        sage: R.<x> = QQ[]                                                                                
        sage: H = HyperellipticCurve(x*(x-1)*(x+9))                                                       
        sage: K = Qp(7,10)                                                                                
        sage: HK = H.change_ring(K)                                                                       
        sage: P = HK(9,36)                                                                                
        sage: Q = HK.teichmuller(P)                                                                       
        sage: Pprime = HK(-4,10)                                                                          
        sage: Qprime = HK.teichmuller(Pprime)                                                             
        sage: HK.height([(1,P),(-1,Q)],[(1,Pprime),(-1,Qprime)],10)                                       
        2*7^2 + 5*7^3 + 7^4 + 7^5 + 2*7^6 + 3*7^7 + 7^8 + 3*7^9 + O(7^10)                                 
        sage: HK.height([(1,Pprime),(-1,Qprime)],[(1,P),(-1,Q)],10)                                       
        2*7^2 + 5*7^3 + 7^4 + 7^5 + 2*7^6 + 3*7^7 + 7^8 + 3*7^9 + O(7^10)      
```



---

Comment by jen created at 2010-03-05 01:33:26

a first attempt at collecting all of the local heights code


---

Comment by jen created at 2010-03-05 01:34:27

Changing status from new to needs_work.


---

Attachment


---

Comment by chapoton created at 2013-08-29 09:58:41

here is a tentative of rebasing on 5.12.beta3

* the part in ``hyperelliptic_generic`` is rather clean and could even go in a separate ticket

* the part in ``hyperelliptic_padic_field`` needs a lot of work and care


---

Comment by chapoton created at 2013-08-29 10:45:18

apply only trac_8441_rebased.patch​


---

Comment by chapoton created at 2013-08-29 16:56:45

apply only trac_8441_rebased.patch


---

Attachment


---

Comment by chapoton created at 2013-10-15 18:21:24

apply only trac_8441_rebased.patch


---

Comment by chapoton created at 2014-01-09 19:48:50

New commits:


---

Comment by git created at 2014-06-23 19:35:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-06-24 20:25:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-07-27 11:10:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-01-06 20:18:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-02-26 10:39:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-03-27 17:17:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-29 11:41:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kedlaya created at 2016-08-11 15:00:14

So is there any mathematical obstruction to giving this a positive review? (I haven't checked all the doctest formatting, so maybe that is still an issue.)


---

Comment by kedlaya created at 2016-08-17 15:00:35

To answer my own question: it looks like there are still some missing doctests on intermediate functions, and some comments in the code that suggest points that still need to be addressed (but I didn't look more closely at the code to evaluate the suggestions).

Would it make to separate out the part of this code which is actually done into a ticket that can be reviewed and merged right away (and make that a dependency for this ticket)?


---

Comment by git created at 2016-08-17 18:58:41

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-08-17 19:38:37

One could easily split to another ticket the simple (but not so interesting) changes in the file `hyperelliptic_generic`.


---

Comment by git created at 2016-08-19 00:02:09

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:
