# Issue 6749: [with patch, needs review] Knapsack algorithm

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-08-14 21:01:44

Assignee: jkantor

A general knapsack algorithm using Linear programming ( check you have #6502 installed ! ) to patiently wait for more efficient versions :-)


---

Comment by wdj created at 2009-08-15 21:20:10

This needs a really detailed example, worked out so that a non-expert (like myself) can understand it. This of the first example you would try to teach an undergraduate. That would be perfect.


---

Comment by wdj created at 2009-08-16 12:48:40

Replying to [comment:1 wdj]:
> This needs a really detailed example, worked out so that a non-expert (like myself) can understand it. Think of the first example you would try to teach an undergraduate. That would be perfect.

For example, there seems to be a simple knapsack problems solved here: http://sites.google.com/site/mikescoderama/Home/0-1-knapsack-problem-in-p
There is a more complicated one here: http://rosettacode.org/wiki/Knapsack_Problem#Simple_Solution
Also, http://webspace.ship.edu/thbrig/DynamicProgramming/Knapsack%20Program/index.html, and the xkcd example
http://www.itl.nist.gov/div897/sqg/dads/HTML/knapsackProblem.html :-)


---

Comment by ncohen created at 2009-08-16 14:54:15

I just added documentation and the example you required. I guess the docstrings took me 10 times what the function requires, but I learned a lot about sage's documentation, the Reference manual, Sphinx, and the fact that you should NEVER, for ANY REASON, delete a branch of Sage.

It gets angry if you do.

And I uploaded a new knapsack.patch replacing the old one ;-)

Nathann


---

Comment by ncohen created at 2009-08-16 14:55:30

A small mistake when uploading the patch... Well, now the two of them are good ;-)


---

Comment by wdj created at 2009-08-16 23:46:18

This patch (after the dependencies are applied) applies fine to 4.1.1.rc2 on an intel macbook running 10.4.11. It passes sage -testall except for (apparently unrelated) errors with 


```
The following tests failed:


        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

However, I will ask someone at work (an expert in OR) to check the code before posting a positive review.


---

Comment by wdj created at 2009-08-20 23:32:23

I've had a talk with my OR colleague. I don't think "A list of pairs (weight,value) where each pair is repeated the number of times it is taken into the solution. " is the proper English grammar for what is meant. I think "A list of pairs (w_i, u_i), for each object i occurring in the solution. " is better. Do you agree? 

Also, he suggested that the "objective value" (or maximal useful value, in your terminology) be included in the solution. Perhaps you could include this as an optional keyword, leaving the current behaviour as the default? If you also agree to this, please add a corresponding example to the docstring.


---

Comment by ncohen created at 2009-08-21 07:44:55

Excellent suggestion ! So :
  * I fixed the grammar error ( sorry, I'm still learning english every day ;-) )
  * I Included the objective value in the output

But :
Actually, this objective value requires no computation at all as it is automatically computed by the LP solver.. So as it can be useful anyway, the function now returns a pair [value, list] ( where list is the value the function returned previously ), and value=maximum useful value.
Besides, I added the flag value_only in case the use only needs the optimal value and does not care about the assignment. This, because the LP solvers can be forced not to return the assignment of the variables and only the objective value, avoiding this way some computations.

Besides, this syntax makes knapsack consistant with the other optimization functions I wrote for graphs, and I hope will all the LP functions we will write in the future ;-)

To avoid mistakes, I updated both patches ( they were identical ), and the new version obviously contains the old one, plus the update I just wrote ! 

Thank you for your review !

Nathann


---

Comment by wdj created at 2009-08-22 01:01:56

There was this failure:


```
sage -t  "devel/sage/sage/numerical/knapsack.py"            
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage/sage/numerical/knapsack.py", line 608:
    sage: knapsack([1,1.5,0.5], max=2)
Expected:
    [2.0, [1, 0.500000000000000]]
Got:
    [2.0, [1.50000000000000, 0.500000000000000]]
**********************************************************************
```



---

Comment by ncohen created at 2009-08-22 06:17:48

I always forget the LP solvers are non-deterministic algorithms, and because of this the values they return sometimes change, which causes trouble with docstrings ;-)

Sorry !

( Fixed, as usual the two patches are updated )


---

Comment by wdj created at 2009-08-22 18:44:16

This last patch (and its dependency) installed fine as before (same system, and version) with the following failures:


```
The following tests failed:


        sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

I think these are unrelated, so this gets a positive review from me. Thanks for implementing it!


---

Comment by mvngu created at 2009-08-25 03:11:46

This will have to wait until #6502 is resolved. Which patch is to be merged? Most likely, I think some if not all doctests would have to be flagged with "# optional" if they require the optional GLPK spkg.


---

Attachment


---

Attachment

Updated. And you can apply any one of them, they're both the same ( I uploaded two by mistake the first time, then updated both )


---

Comment by wdj created at 2009-08-25 18:05:47

This patch (on top of the updated 6502) did not apply for me (4.1.1.rc2, intel macbook 10.4.11).


---

Comment by ncohen created at 2009-08-25 18:57:02

I am using 4.1.1, perhaps it explains ?

I just tried it again with only 6502 and this one, and noticed nothing wrong O_o


---

Comment by ncohen created at 2009-08-25 18:59:07

Could you please try it again on a 4.1.1 ?


---

Comment by wdj created at 2009-08-25 20:49:44

Replying to [comment:18 ncohen]:
> Could you please try it again on a 4.1.1 ?

I created a new clone and re-tried this. This time it worked! Passed tests as before (same Sage version, same machine ....).


---

Comment by ncohen created at 2009-08-31 15:55:16

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann


---

Comment by ncohen created at 2009-09-03 09:44:06

Here is the new version, slightly modified to use the symbolics from #6869 ( the new version of MIP you need to try this code ! )


---

Attachment


---

Comment by wdj created at 2009-09-08 18:05:48

This applies fine to 4.1.2.a0 and passes testall without any other packages installed (no glpk, etc).

Running more tests...


---

Comment by wdj created at 2009-09-09 10:52:59

This applies fine to 4.1.2.a0 and passes testall with glpk package installed.


---

Comment by mvngu created at 2009-09-10 12:02:01

Resolution: fixed


---

Comment by mvngu created at 2009-09-10 12:02:01

Merged `knapsack-symbolics.patch`.



With `knapsack-symbolics.patch`, I got a warning when building the reference manual:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/local/lib/python2.6/site-packages/sage/numerical/knapsack.py:docstring of sage.numerical.knapsack.knapsack:69: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```

See #6916 for a follow-up to this ticket.
