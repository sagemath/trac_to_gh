# Issue 8880: CPLEX can bi silenced

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-05-05 00:42:02

Assignee: jason, jkantor

With this patch CPLEX it not priting the usual screens of output by default :-)

Nathann


---

Comment by ncohen created at 2010-05-05 00:42:58

Changing status from new to needs_review.


---

Comment by jason created at 2010-05-05 03:18:10

Design-wise, it seems a little uncomfortable to have all extra keywords passed on to the solvers.  How annoying would it be to have a solver_opt keyword for options passed down?  So something like:

edge_cut(solver_opt=dict(option1=true, option2='solve fast', option3=5))

or

edge_cut(solver_opt={'option1': true, 'option2': 'solve fast', 'option3': 5})

instead of 

edge_cut(option1=true, option2='solve fast', option3=5)

It involves a bit more typing, but it seems like a much cleaner design.



---

Comment by jason created at 2010-05-05 03:27:18

(I guess my comment is the same here as it is on #8364.  I still think it's a better design, but I haven't used these options in practice, so if you think that it is way too annoying, then say so.

My concerns are:

 1. the options are not related to the actual function, so logically they should be separated out from the function options
 1. Anytime we implement a new option for the function (say we make a graph-theoretic algorithm to do the same thing), we have to check all solvers to see if we are accidentally overriding a keyword option for the solver.

You could also make the options part of the solver keyword, like this:

edge_cut(solver=("CPLEX", dict(option1=True, option2=False)))

or

edge_cut(solver=dict(option1=True, option2=False)) # pick the default solver, pass in these options.


---

Comment by ncohen created at 2010-05-05 10:55:55

Oops... It sounds like the patch uploaded here does not corerespond to the ticket at all ^^;

About #8364, well.. I still agree with you when you say a dict is cleaner, but it will definitely be very quickly annoying to do all this when you just want to change the solver.. And to be honest, there are only 2 different arguments which can be passed down to the MixedIntegerLinearProgram at the moment :

 * log ( verbosity)
 * solver (change the default solver)

It may be beter though, to satisfy all of us, to just replace this **kwds by these two parameters... So I will completely rewrite #8364 like this if you agree, which needed to be done anyway as its patch is not based on the latest version of sage :-)

(And now I replace the patch contained in this ticket with the good onem you'll see it is much easier to review :-) )

Thank you again !!

Nathann


---

Comment by jason created at 2010-05-05 14:55:43

Replying to [comment:6 ncohen]:
> Oops... It sounds like the patch uploaded here does not corerespond to the ticket at all ^^;
> 

Thanks.  I was kind of wondering where the CPLEX stuff was... :)


> About #8364, well.. I still agree with you when you say a dict is cleaner, but it will definitely be very quickly annoying to do all this when you just want to change the solver.. And to be honest, there are only 2 different arguments which can be passed down to the MixedIntegerLinearProgram at the moment :
> 
>  * log ( verbosity)
>  * solver (change the default solver)
> 
> It may be beter though, to satisfy all of us, to just replace this **kwds by these two parameters... So I will completely rewrite #8364 like this if you agree, which needed to be done anyway as its patch is not based on the latest version of sage :-)


That sounds like a great plan.


---

Comment by jason created at 2010-05-05 23:42:14

What about making the options solver_log and solver?  That way the log option is a bit more descriptive, and not too much longer than log.


---

Comment by ncohen created at 2010-05-06 02:42:01

Hmmm... Ok, but... why ? The user just wants to incraase the level of verbosity of the function he is using, is he really interested in knowing we are using LP in this particular case ? It's as if we were using algorithm_log or function_log... What do we earn this way ? :-)

Nathann


---

Comment by jason created at 2010-05-06 03:59:06

Replying to [comment:9 ncohen]:
> Hmmm... Ok, but... why ? The user just wants to incraase the level of verbosity of the function he is using, is he really interested in knowing we are using LP in this particular case ? It's as if we were using algorithm_log or function_log... What do we earn this way ? :-)


Good point.  "log" didn't seem to be the usual convention.  It would be more conventional to use a "verbose" keyword for printing out lots of intermediate information.


---

Comment by jason created at 2010-05-06 03:59:42

(I mean that it's Sage's convention to use the verbose keyword for something like that, at least as far as I've seen.)


---

Comment by ncohen created at 2010-05-14 20:30:30

Removes a "CPLEX IS NOT IMPLEMENTED YET" from the solve function's documentation !


---

Comment by jason created at 2010-05-14 20:43:46

Replying to [comment:12 ncohen]:
> Removes a "CPLEX IS NOT IMPLEMENTED YET" from the solve function's documentation !

Nice.  Um, except that the linear programming stuff is not in the "tutorial", but in the "Constructions" document.  I can see that being confusing...

Don't update the patch yet; when I get cplex working, I might have another comment or two.


---

Comment by jason created at 2010-05-15 03:34:30

The cleanup code here should probably be put in a "finally" block, rather than being duplicated.  See http://docs.python.org/reference/compound_stmts.html#the-try-statement


---

Comment by jason created at 2010-05-15 03:34:30

Changing assignee from jason, jkantor to jason.


---

Comment by jason created at 2010-05-15 03:34:44

Changing assignee from jason to ncohen.


---

Comment by jason created at 2010-05-15 03:41:40

Even with this patch, the first time I use p.solve(), I see this from CPLEX:


```
IBM ILOG License Manager: "IBM ILOG Optimization Suite for Academic Initiative" is accessing CPLEX 12 with option(s): "e m b q ".
```


Is that unavoidable?  (Maybe it's desirable, I don't know)


---

Comment by ncohen created at 2010-05-15 15:25:33

I had thought during my first tests that this message was a nice way to debug, though it's true the user only needs to incrase the verbosity to see it... Thank you for this "finally" keyword which I ignored :-)

Patch updated.

Nathan


---

Attachment

This is 5 weeks stale by now. Jason-- do you have any further objections to the patch?


---

Comment by ncohen created at 2010-09-06 11:13:32

Changing component from numerical to linear programming.


---

Comment by ncohen created at 2010-10-08 09:05:37

This ticket can be closed, as the files it modifies are being deleted by #10043

Nathann


---

Comment by mpatel created at 2010-10-09 08:45:27

Resolution: invalid
