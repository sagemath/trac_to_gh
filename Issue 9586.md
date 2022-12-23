# Issue 9586: Lecture Scheduler

Issue created by migration from https://trac.sagemath.org/ticket/9586

Original creator: schilly

Original creation time: 2010-07-23 10:23:09

Assignee: jason, jkantor

CC:  ncohen jason

Let Sage schedule all the lectures at a university via an object oriented framework using the MILP solver infrastructure.


---

Comment by schilly created at 2010-07-23 10:39:24

Changing status from new to needs_work.


---

Comment by schilly created at 2010-07-25 17:37:24

Changing status from needs_work to needs_review.


---

Attachment

Hi Harald,

I'm sorry for the delay of looking at this carefully.  The code seems very clean and the example is helpful (and *really* important).  In any case, a couple of questions crossed my mind:

    #. Is it clear that a program to schedule lectures should be part of Sage?  I'm not saying it shouldn't be - it's hardly for me to decide.  I don't want to judge the usefulness of this program either.  But it's clearly slightly off the core mathematical track when compared to, say, integer addition :).  (Just to bring up a completely random example, should Sage also contain a Connect Four solver, say?)

    #. It seems clear that the usage of this class would be largely driven by the examples.  As such I think there should be at least one example showing how the program deals with clashes which cannot be avoided.  Does it just abort the generation of the schedule altogether?  Or does it minimize the number of lectures affected?

    #. It's not quite clear to me how this scales to large real-world examples.  Is there a way to obtain suitable input data to test this?

Best wishes,

Sebastian


---

Comment by schilly created at 2010-07-29 14:29:25

Thank's for looking into this.

ad 1. I just wish to have it in sage because I spent much time implementing it and I like it. About part-of-sage-or-not, there is afaik also a rubic cube solver, even with some visuals, and also a sudoku solver in sage ... and there are more papers about combinatorial optimization w.r.t. scheduling than about sudoku! ;)

ad 2. it depends on the solver, i.e. if there is no feasible solution [that means that all constraints are true] it returns an exception. handling this in a better way is not part of the scope of this application, it's part of the mip.pyx file where the solver interfaces are. also, there are sophisticated methods to deal with infeasible CSP problems, i.e. solvers like gurobi can generate an IIS set to learn more about why the problem is infesible. (but we haven't even wrapped gurobi now). so, for now just an error depending on the selected solver.

ad 3. it doesn't scale with glpk or cbc (you get the later one via a spkg and the `solver='Coin'` parameter in `solve()`. the only open source csp solver that might be able to scale to real world applications is scip, but it is currently not able to solve this kind of problem due to a bug (reported upstream, this bug will be resolved in the next release in oct 2010). cplex might be the best choice for now. apart from that, i have a real world example for that model, but it's  not meant for the public (real names and so on).


---

Comment by jason created at 2010-09-03 21:42:33

I agree that it would be good to have in Sage.  Sebastian, did Harald satisfy you with his answers to (2) and (3)?

I haven't had time to look it very carefully, but I really like the cool demo.


---

Comment by kini created at 2011-10-13 09:48:30

Is it possible to rework this into an spkg that installs a module into Sage's Python installation? I share spancratz's doubts about whether this should go into the Sage library proper, though I think it's a cool application to have.


---

Comment by davidloeffler created at 2012-03-11 15:50:26

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-11 15:50:26

According to the patchbot log, this fails doctests on every single version of Sage it's been tested on, including current release and dev, so I'm putting it to "needs work".


---

Comment by mkoeppe created at 2019-12-25 15:28:04

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2019-12-25 15:28:04

Proposing to close this ancient ticket.


---

Comment by mjo created at 2021-10-04 23:05:25

It's a cute LP example, but hard to argue with a decade of "needs work" when there's only one proponent.


---

Comment by mjo created at 2021-10-04 23:05:25

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-10-04 23:44:13

Resolution: invalid
