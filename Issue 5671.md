# Issue 5671: Create a spkg for minisat

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-04-02 22:10:41

Assignee: boothby

CC:  fichtejo

We want miniSAT.  spkg it up!


---

Attachment


---

Comment by mabshoff created at 2009-04-02 22:42:41

Might I point out that this is a dupe of #418.

You also 

 * should assign a milestone when you open a ticket
 * not attach spkgs to tickets, but post a link. Given that this one is 77kb it might be a borderline case.

Cheers,

Michael


---

Attachment


---

Attachment

With just the posted code to this point:

```
sage: S = minisat.Solver(verbosity=2)
sage: S.new_var()
0
sage: S.new_var()
1
sage: S.new_var()
2
sage: S.new_var()
3
sage: S.add_clause([1])
pushing lit.p =  Literal 1
sage: S.add_clause([2])
pushing lit.p =  Literal 2
sage: S.solve()
============================[ Search Statistics ]==============================
===============================================================================
===============================================================================
Verified 0 original clauses.
True
```



---

Comment by malb created at 2009-09-02 10:31:59

This

   http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html

might be relevant. It is an enhanced MiniSat with:

 * Natively handled XOR functions
 * Statistics generation
 * Search randomization
 * Detailed solving process visualization
 * Clause grouping and group naming
 * Variable naming
 * Debug mode
 * Code cleanup


---

Comment by kcrisman created at 2012-06-04 19:14:33

Replying to [comment:5 malb]:
> This
> 
>    http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html
> 
> might be relevant. It is an enhanced MiniSat with:
> 
>  * Natively handled XOR functions
>  * Statistics generation
>  * Search randomization
>  * Detailed solving process visualization
>  * Clause grouping and group naming
>  * Variable naming
>  * Debug mode
>  * Code cleanup

Given this and recent developments at #418, perhaps this is a dupe?


---

Comment by malb created at 2012-06-15 16:19:30

I vote for declaring this ticket a dupe.


---

Comment by mmezzarobba created at 2014-03-14 15:29:41

Changing status from new to needs_review.


---

Comment by malb created at 2014-03-14 15:47:38

I'm not sure what needs review here?


---

Comment by kcrisman created at 2014-03-14 15:51:18

Changing status from needs_review to positive_review.


---

Comment by mmezzarobba created at 2014-03-14 16:17:25

Replying to [comment:12 malb]:
> I'm not sure what needs review here?

As far as I understand the way to have a ticket closes as "wontfix" or similar is to set the milestone to `duplicate/invalid/wontfix` and wait for someone else to review that choice.


---

Comment by kcrisman created at 2014-03-14 16:23:19

Which has been done :)  mmezz, just add your real name in the reviewers field.


---

Comment by vbraun created at 2014-03-19 04:41:52

Resolution: duplicate
