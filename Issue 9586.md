# Issue 9586: Lecture Scheduler

archive/issues_009586.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  ncohen jason\n\nLet Sage schedule all the lectures at a university via an object oriented framework using the MILP solver infrastructure.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9586\n\n",
    "created_at": "2010-07-23T10:23:09Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Lecture Scheduler",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9586",
    "user": "schilly"
}
```
Assignee: jason, jkantor

CC:  ncohen jason

Let Sage schedule all the lectures at a university via an object oriented framework using the MILP solver infrastructure.

Issue created by migration from https://trac.sagemath.org/ticket/9586





---

archive/issue_comments_092694.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-23T10:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92694",
    "user": "schilly"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_092695.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-25T17:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92695",
    "user": "schilly"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092696.json:
```json
{
    "body": "Attachment [9586-lecturescheduler.patch](tarball://root/attachments/some-uuid/ticket9586/9586-lecturescheduler.patch) by spancratz created at 2010-07-29 14:01:40\n\nHi Harald,\n\nI'm sorry for the delay of looking at this carefully.  The code seems very clean and the example is helpful (and *really* important).  In any case, a couple of questions crossed my mind:\n\n#. Is it clear that a program to schedule lectures should be part of Sage?  I'm not saying it shouldn't be - it's hardly for me to decide.  I don't want to judge the usefulness of this program either.  But it's clearly slightly off the core mathematical track when compared to, say, integer addition :).  (Just to bring up a completely random example, should Sage also contain a Connect Four solver, say?)\n\n#. It seems clear that the usage of this class would be largely driven by the examples.  As such I think there should be at least one example showing how the program deals with clashes which cannot be avoided.  Does it just abort the generation of the schedule altogether?  Or does it minimize the number of lectures affected?\n\n#. It's not quite clear to me how this scales to large real-world examples.  Is there a way to obtain suitable input data to test this?\n\nBest wishes,\n\nSebastian",
    "created_at": "2010-07-29T14:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92696",
    "user": "spancratz"
}
```

Attachment [9586-lecturescheduler.patch](tarball://root/attachments/some-uuid/ticket9586/9586-lecturescheduler.patch) by spancratz created at 2010-07-29 14:01:40

Hi Harald,

I'm sorry for the delay of looking at this carefully.  The code seems very clean and the example is helpful (and *really* important).  In any case, a couple of questions crossed my mind:

#. Is it clear that a program to schedule lectures should be part of Sage?  I'm not saying it shouldn't be - it's hardly for me to decide.  I don't want to judge the usefulness of this program either.  But it's clearly slightly off the core mathematical track when compared to, say, integer addition :).  (Just to bring up a completely random example, should Sage also contain a Connect Four solver, say?)

#. It seems clear that the usage of this class would be largely driven by the examples.  As such I think there should be at least one example showing how the program deals with clashes which cannot be avoided.  Does it just abort the generation of the schedule altogether?  Or does it minimize the number of lectures affected?

#. It's not quite clear to me how this scales to large real-world examples.  Is there a way to obtain suitable input data to test this?

Best wishes,

Sebastian



---

archive/issue_comments_092697.json:
```json
{
    "body": "Thank's for looking into this.\n\nad 1. I just wish to have it in sage because I spent much time implementing it and I like it. About part-of-sage-or-not, there is afaik also a rubic cube solver, even with some visuals, and also a sudoku solver in sage ... and there are more papers about combinatorial optimization w.r.t. scheduling than about sudoku! ;)\n\nad 2. it depends on the solver, i.e. if there is no feasible solution [that means that all constraints are true] it returns an exception. handling this in a better way is not part of the scope of this application, it's part of the mip.pyx file where the solver interfaces are. also, there are sophisticated methods to deal with infeasible CSP problems, i.e. solvers like gurobi can generate an IIS set to learn more about why the problem is infesible. (but we haven't even wrapped gurobi now). so, for now just an error depending on the selected solver.\n\nad 3. it doesn't scale with glpk or cbc (you get the later one via a spkg and the `solver='Coin'` parameter in `solve()`. the only open source csp solver that might be able to scale to real world applications is scip, but it is currently not able to solve this kind of problem due to a bug (reported upstream, this bug will be resolved in the next release in oct 2010). cplex might be the best choice for now. apart from that, i have a real world example for that model, but it's  not meant for the public (real names and so on).",
    "created_at": "2010-07-29T14:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92697",
    "user": "schilly"
}
```

Thank's for looking into this.

ad 1. I just wish to have it in sage because I spent much time implementing it and I like it. About part-of-sage-or-not, there is afaik also a rubic cube solver, even with some visuals, and also a sudoku solver in sage ... and there are more papers about combinatorial optimization w.r.t. scheduling than about sudoku! ;)

ad 2. it depends on the solver, i.e. if there is no feasible solution [that means that all constraints are true] it returns an exception. handling this in a better way is not part of the scope of this application, it's part of the mip.pyx file where the solver interfaces are. also, there are sophisticated methods to deal with infeasible CSP problems, i.e. solvers like gurobi can generate an IIS set to learn more about why the problem is infesible. (but we haven't even wrapped gurobi now). so, for now just an error depending on the selected solver.

ad 3. it doesn't scale with glpk or cbc (you get the later one via a spkg and the `solver='Coin'` parameter in `solve()`. the only open source csp solver that might be able to scale to real world applications is scip, but it is currently not able to solve this kind of problem due to a bug (reported upstream, this bug will be resolved in the next release in oct 2010). cplex might be the best choice for now. apart from that, i have a real world example for that model, but it's  not meant for the public (real names and so on).



---

archive/issue_comments_092698.json:
```json
{
    "body": "I agree that it would be good to have in Sage.  Sebastian, did Harald satisfy you with his answers to (2) and (3)?\n\nI haven't had time to look it very carefully, but I really like the cool demo.",
    "created_at": "2010-09-03T21:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92698",
    "user": "jason"
}
```

I agree that it would be good to have in Sage.  Sebastian, did Harald satisfy you with his answers to (2) and (3)?

I haven't had time to look it very carefully, but I really like the cool demo.



---

archive/issue_comments_092699.json:
```json
{
    "body": "Is it possible to rework this into an spkg that installs a module into Sage's Python installation? I share spancratz's doubts about whether this should go into the Sage library proper, though I think it's a cool application to have.",
    "created_at": "2011-10-13T09:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92699",
    "user": "kini"
}
```

Is it possible to rework this into an spkg that installs a module into Sage's Python installation? I share spancratz's doubts about whether this should go into the Sage library proper, though I think it's a cool application to have.



---

archive/issue_comments_092700.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-11T15:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92700",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092701.json:
```json
{
    "body": "According to the patchbot log, this fails doctests on every single version of Sage it's been tested on, including current release and dev, so I'm putting it to \"needs work\".",
    "created_at": "2012-03-11T15:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92701",
    "user": "davidloeffler"
}
```

According to the patchbot log, this fails doctests on every single version of Sage it's been tested on, including current release and dev, so I'm putting it to "needs work".



---

archive/issue_comments_092702.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2019-12-25T15:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92702",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092703.json:
```json
{
    "body": "Proposing to close this ancient ticket.",
    "created_at": "2019-12-25T15:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92703",
    "user": "mkoeppe"
}
```

Proposing to close this ancient ticket.



---

archive/issue_comments_092704.json:
```json
{
    "body": "It's a cute LP example, but hard to argue with a decade of \"needs work\" when there's only one proponent.",
    "created_at": "2021-10-04T23:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92704",
    "user": "mjo"
}
```

It's a cute LP example, but hard to argue with a decade of "needs work" when there's only one proponent.



---

archive/issue_comments_092705.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-04T23:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92705",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092706.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-04T23:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9586#issuecomment-92706",
    "user": "mkoeppe"
}
```

Resolution: invalid
