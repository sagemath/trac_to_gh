# Issue 8880: CPLEX can bi silenced

archive/issues_008880.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nWith this patch CPLEX it not priting the usual screens of output by default :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8880\n\n",
    "created_at": "2010-05-05T00:42:02Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "CPLEX can bi silenced",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8880",
    "user": "ncohen"
}
```
Assignee: jason, jkantor

With this patch CPLEX it not priting the usual screens of output by default :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8880





---

archive/issue_comments_081596.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-05T00:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81596",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081597.json:
```json
{
    "body": "Design-wise, it seems a little uncomfortable to have all extra keywords passed on to the solvers.\u00a0 How annoying would it be to have a solver_opt keyword for options passed down?\u00a0 So something like:\n\nedge_cut(solver_opt=dict(option1=true, option2='solve fast', option3=5))\n\nor\n\nedge_cut(solver_opt={'option1': true, 'option2': 'solve fast', 'option3': 5})\n\ninstead of \n\nedge_cut(option1=true, option2='solve fast', option3=5)\n\nIt involves a bit more typing, but it seems like a much cleaner design.\n",
    "created_at": "2010-05-05T03:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81597",
    "user": "jason"
}
```

Design-wise, it seems a little uncomfortable to have all extra keywords passed on to the solvers.  How annoying would it be to have a solver_opt keyword for options passed down?  So something like:

edge_cut(solver_opt=dict(option1=true, option2='solve fast', option3=5))

or

edge_cut(solver_opt={'option1': true, 'option2': 'solve fast', 'option3': 5})

instead of 

edge_cut(option1=true, option2='solve fast', option3=5)

It involves a bit more typing, but it seems like a much cleaner design.




---

archive/issue_comments_081598.json:
```json
{
    "body": "(I guess my comment is the same here as it is on #8364.\u00a0 I still think it's a better design, but I haven't used these options in practice, so if you think that it is way too annoying, then say so.\n\nMy concerns are:\n\n1. the options are not related to the actual function, so logically they should be separated out from the function options\n2. Anytime we implement a new option for the function (say we make a graph-theoretic algorithm to do the same thing), we have to check all solvers to see if we are accidentally overriding a keyword option for the solver.\n\nYou could also make the options part of the solver keyword, like this:\n\nedge_cut(solver=(\"CPLEX\", dict(option1=True, option2=False)))\n\nor\n\nedge_cut(solver=dict(option1=True, option2=False)) # pick the default solver, pass in these options.",
    "created_at": "2010-05-05T03:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81598",
    "user": "jason"
}
```

(I guess my comment is the same here as it is on #8364.  I still think it's a better design, but I haven't used these options in practice, so if you think that it is way too annoying, then say so.

My concerns are:

1. the options are not related to the actual function, so logically they should be separated out from the function options
2. Anytime we implement a new option for the function (say we make a graph-theoretic algorithm to do the same thing), we have to check all solvers to see if we are accidentally overriding a keyword option for the solver.

You could also make the options part of the solver keyword, like this:

edge_cut(solver=("CPLEX", dict(option1=True, option2=False)))

or

edge_cut(solver=dict(option1=True, option2=False)) # pick the default solver, pass in these options.



---

archive/issue_comments_081599.json:
```json
{
    "body": "Oops... It sounds like the patch uploaded here does not corerespond to the ticket at all ^^;\n\nAbout #8364, well.. I still agree with you when you say a dict is cleaner, but it will definitely be very quickly annoying to do all this when you just want to change the solver.. And to be honest, there are only 2 different arguments which can be passed down to the MixedIntegerLinearProgram at the moment :\n\n* log ( verbosity)\n* solver (change the default solver)\n\nIt may be beter though, to satisfy all of us, to just replace this **kwds by these two parameters... So I will completely rewrite #8364 like this if you agree, which needed to be done anyway as its patch is not based on the latest version of sage :-)\n\n(And now I replace the patch contained in this ticket with the good onem you'll see it is much easier to review :-) )\n\nThank you again !!\n\nNathann",
    "created_at": "2010-05-05T10:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81599",
    "user": "ncohen"
}
```

Oops... It sounds like the patch uploaded here does not corerespond to the ticket at all ^^;

About #8364, well.. I still agree with you when you say a dict is cleaner, but it will definitely be very quickly annoying to do all this when you just want to change the solver.. And to be honest, there are only 2 different arguments which can be passed down to the MixedIntegerLinearProgram at the moment :

* log ( verbosity)
* solver (change the default solver)

It may be beter though, to satisfy all of us, to just replace this **kwds by these two parameters... So I will completely rewrite #8364 like this if you agree, which needed to be done anyway as its patch is not based on the latest version of sage :-)

(And now I replace the patch contained in this ticket with the good onem you'll see it is much easier to review :-) )

Thank you again !!

Nathann



---

archive/issue_comments_081600.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> Oops... It sounds like the patch uploaded here does not corerespond to the ticket at all ^^;\n> \n\nThanks.  I was kind of wondering where the CPLEX stuff was... :)\n\n\n> About #8364, well.. I still agree with you when you say a dict is cleaner, but it will definitely be very quickly annoying to do all this when you just want to change the solver.. And to be honest, there are only 2 different arguments which can be passed down to the MixedIntegerLinearProgram at the moment :\n> \n>  * log ( verbosity)\n>  * solver (change the default solver)\n> \n> It may be beter though, to satisfy all of us, to just replace this **kwds by these two parameters... So I will completely rewrite #8364 like this if you agree, which needed to be done anyway as its patch is not based on the latest version of sage :-)\n\n\nThat sounds like a great plan.",
    "created_at": "2010-05-05T14:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81600",
    "user": "jason"
}
```

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

archive/issue_comments_081601.json:
```json
{
    "body": "What about making the options solver_log and solver?  That way the log option is a bit more descriptive, and not too much longer than log.",
    "created_at": "2010-05-05T23:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81601",
    "user": "jason"
}
```

What about making the options solver_log and solver?  That way the log option is a bit more descriptive, and not too much longer than log.



---

archive/issue_comments_081602.json:
```json
{
    "body": "Hmmm... Ok, but... why ? The user just wants to incraase the level of verbosity of the function he is using, is he really interested in knowing we are using LP in this particular case ? It's as if we were using algorithm_log or function_log... What do we earn this way ? :-)\n\nNathann",
    "created_at": "2010-05-06T02:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81602",
    "user": "ncohen"
}
```

Hmmm... Ok, but... why ? The user just wants to incraase the level of verbosity of the function he is using, is he really interested in knowing we are using LP in this particular case ? It's as if we were using algorithm_log or function_log... What do we earn this way ? :-)

Nathann



---

archive/issue_comments_081603.json:
```json
{
    "body": "Replying to [comment:9 ncohen]:\n> Hmmm... Ok, but... why ? The user just wants to incraase the level of verbosity of the function he is using, is he really interested in knowing we are using LP in this particular case ? It's as if we were using algorithm_log or function_log... What do we earn this way ? :-)\n\n\nGood point.  \"log\" didn't seem to be the usual convention.  It would be more conventional to use a \"verbose\" keyword for printing out lots of intermediate information.",
    "created_at": "2010-05-06T03:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81603",
    "user": "jason"
}
```

Replying to [comment:9 ncohen]:
> Hmmm... Ok, but... why ? The user just wants to incraase the level of verbosity of the function he is using, is he really interested in knowing we are using LP in this particular case ? It's as if we were using algorithm_log or function_log... What do we earn this way ? :-)


Good point.  "log" didn't seem to be the usual convention.  It would be more conventional to use a "verbose" keyword for printing out lots of intermediate information.



---

archive/issue_comments_081604.json:
```json
{
    "body": "(I mean that it's Sage's convention to use the verbose keyword for something like that, at least as far as I've seen.)",
    "created_at": "2010-05-06T03:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81604",
    "user": "jason"
}
```

(I mean that it's Sage's convention to use the verbose keyword for something like that, at least as far as I've seen.)



---

archive/issue_comments_081605.json:
```json
{
    "body": "Removes a \"CPLEX IS NOT IMPLEMENTED YET\" from the solve function's documentation !",
    "created_at": "2010-05-14T20:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81605",
    "user": "ncohen"
}
```

Removes a "CPLEX IS NOT IMPLEMENTED YET" from the solve function's documentation !



---

archive/issue_comments_081606.json:
```json
{
    "body": "Replying to [comment:12 ncohen]:\n> Removes a \"CPLEX IS NOT IMPLEMENTED YET\" from the solve function's documentation !\n\nNice.  Um, except that the linear programming stuff is not in the \"tutorial\", but in the \"Constructions\" document.  I can see that being confusing...\n\nDon't update the patch yet; when I get cplex working, I might have another comment or two.",
    "created_at": "2010-05-14T20:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81606",
    "user": "jason"
}
```

Replying to [comment:12 ncohen]:
> Removes a "CPLEX IS NOT IMPLEMENTED YET" from the solve function's documentation !

Nice.  Um, except that the linear programming stuff is not in the "tutorial", but in the "Constructions" document.  I can see that being confusing...

Don't update the patch yet; when I get cplex working, I might have another comment or two.



---

archive/issue_comments_081607.json:
```json
{
    "body": "The cleanup code here should probably be put in a \"finally\" block, rather than being duplicated.  See http://docs.python.org/reference/compound_stmts.html#the-try-statement",
    "created_at": "2010-05-15T03:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81607",
    "user": "jason"
}
```

The cleanup code here should probably be put in a "finally" block, rather than being duplicated.  See http://docs.python.org/reference/compound_stmts.html#the-try-statement



---

archive/issue_comments_081608.json:
```json
{
    "body": "Changing assignee from jason, jkantor to jason.",
    "created_at": "2010-05-15T03:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81608",
    "user": "jason"
}
```

Changing assignee from jason, jkantor to jason.



---

archive/issue_comments_081609.json:
```json
{
    "body": "Changing assignee from jason to ncohen.",
    "created_at": "2010-05-15T03:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81609",
    "user": "jason"
}
```

Changing assignee from jason to ncohen.



---

archive/issue_comments_081610.json:
```json
{
    "body": "Even with this patch, the first time I use p.solve(), I see this from CPLEX:\n\n\n```\nIBM ILOG License Manager: \"IBM ILOG Optimization Suite for Academic Initiative\" is accessing CPLEX 12 with option(s): \"e m b q \".\n```\n\n\nIs that unavoidable?  (Maybe it's desirable, I don't know)",
    "created_at": "2010-05-15T03:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81610",
    "user": "jason"
}
```

Even with this patch, the first time I use p.solve(), I see this from CPLEX:


```
IBM ILOG License Manager: "IBM ILOG Optimization Suite for Academic Initiative" is accessing CPLEX 12 with option(s): "e m b q ".
```


Is that unavoidable?  (Maybe it's desirable, I don't know)



---

archive/issue_comments_081611.json:
```json
{
    "body": "I had thought during my first tests that this message was a nice way to debug, though it's true the user only needs to incrase the verbosity to see it... Thank you for this \"finally\" keyword which I ignored :-)\n\nPatch updated.\n\nNathan",
    "created_at": "2010-05-15T15:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81611",
    "user": "ncohen"
}
```

I had thought during my first tests that this message was a nice way to debug, though it's true the user only needs to incrase the verbosity to see it... Thank you for this "finally" keyword which I ignored :-)

Patch updated.

Nathan



---

archive/issue_comments_081612.json:
```json
{
    "body": "Attachment\n\nThis is 5 weeks stale by now. Jason-- do you have any further objections to the patch?",
    "created_at": "2010-06-17T21:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81612",
    "user": "rlm"
}
```

Attachment

This is 5 weeks stale by now. Jason-- do you have any further objections to the patch?



---

archive/issue_comments_081613.json:
```json
{
    "body": "Changing component from numerical to linear programming.",
    "created_at": "2010-09-06T11:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81613",
    "user": "ncohen"
}
```

Changing component from numerical to linear programming.



---

archive/issue_comments_081614.json:
```json
{
    "body": "This ticket can be closed, as the files it modifies are being deleted by #10043\n\nNathann",
    "created_at": "2010-10-08T09:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81614",
    "user": "ncohen"
}
```

This ticket can be closed, as the files it modifies are being deleted by #10043

Nathann



---

archive/issue_comments_081615.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-10-09T08:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8880#issuecomment-81615",
    "user": "mpatel"
}
```

Resolution: invalid
