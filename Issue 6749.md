# Issue 6749: [with patch, needs review] Knapsack algorithm

archive/issues_006749.json:
```json
{
    "body": "Assignee: jkantor\n\nA general knapsack algorithm using Linear programming ( check you have #6502 installed ! ) to patiently wait for more efficient versions :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6749\n\n",
    "created_at": "2009-08-14T21:01:44Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Knapsack algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6749",
    "user": "@nathanncohen"
}
```
Assignee: jkantor

A general knapsack algorithm using Linear programming ( check you have #6502 installed ! ) to patiently wait for more efficient versions :-)

Issue created by migration from https://trac.sagemath.org/ticket/6749





---

archive/issue_comments_055521.json:
```json
{
    "body": "This needs a really detailed example, worked out so that a non-expert (like myself) can understand it. This of the first example you would try to teach an undergraduate. That would be perfect.",
    "created_at": "2009-08-15T21:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55521",
    "user": "@wdjoyner"
}
```

This needs a really detailed example, worked out so that a non-expert (like myself) can understand it. This of the first example you would try to teach an undergraduate. That would be perfect.



---

archive/issue_comments_055522.json:
```json
{
    "body": "Replying to [comment:1 wdj]:\n> This needs a really detailed example, worked out so that a non-expert (like myself) can understand it. Think of the first example you would try to teach an undergraduate. That would be perfect.\n\nFor example, there seems to be a simple knapsack problems solved here: http://sites.google.com/site/mikescoderama/Home/0-1-knapsack-problem-in-p\nThere is a more complicated one here: http://rosettacode.org/wiki/Knapsack_Problem#Simple_Solution\nAlso, http://webspace.ship.edu/thbrig/DynamicProgramming/Knapsack%20Program/index.html, and the xkcd example\nhttp://www.itl.nist.gov/div897/sqg/dads/HTML/knapsackProblem.html :-)",
    "created_at": "2009-08-16T12:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55522",
    "user": "@wdjoyner"
}
```

Replying to [comment:1 wdj]:
> This needs a really detailed example, worked out so that a non-expert (like myself) can understand it. Think of the first example you would try to teach an undergraduate. That would be perfect.

For example, there seems to be a simple knapsack problems solved here: http://sites.google.com/site/mikescoderama/Home/0-1-knapsack-problem-in-p
There is a more complicated one here: http://rosettacode.org/wiki/Knapsack_Problem#Simple_Solution
Also, http://webspace.ship.edu/thbrig/DynamicProgramming/Knapsack%20Program/index.html, and the xkcd example
http://www.itl.nist.gov/div897/sqg/dads/HTML/knapsackProblem.html :-)



---

archive/issue_comments_055523.json:
```json
{
    "body": "I just added documentation and the example you required. I guess the docstrings took me 10 times what the function requires, but I learned a lot about sage's documentation, the Reference manual, Sphinx, and the fact that you should NEVER, for ANY REASON, delete a branch of Sage.\n\nIt gets angry if you do.\n\nAnd I uploaded a new knapsack.patch replacing the old one ;-)\n\nNathann",
    "created_at": "2009-08-16T14:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55523",
    "user": "@nathanncohen"
}
```

I just added documentation and the example you required. I guess the docstrings took me 10 times what the function requires, but I learned a lot about sage's documentation, the Reference manual, Sphinx, and the fact that you should NEVER, for ANY REASON, delete a branch of Sage.

It gets angry if you do.

And I uploaded a new knapsack.patch replacing the old one ;-)

Nathann



---

archive/issue_comments_055524.json:
```json
{
    "body": "A small mistake when uploading the patch... Well, now the two of them are good ;-)",
    "created_at": "2009-08-16T14:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55524",
    "user": "@nathanncohen"
}
```

A small mistake when uploading the patch... Well, now the two of them are good ;-)



---

archive/issue_comments_055525.json:
```json
{
    "body": "This patch (after the dependencies are applied) applies fine to 4.1.1.rc2 on an intel macbook running 10.4.11. It passes sage -testall except for (apparently unrelated) errors with \n\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/interfaces/maxima.py\"\n        sage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n```\n\nHowever, I will ask someone at work (an expert in OR) to check the code before posting a positive review.",
    "created_at": "2009-08-16T23:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55525",
    "user": "@wdjoyner"
}
```

This patch (after the dependencies are applied) applies fine to 4.1.1.rc2 on an intel macbook running 10.4.11. It passes sage -testall except for (apparently unrelated) errors with 


```
The following tests failed:


        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

However, I will ask someone at work (an expert in OR) to check the code before posting a positive review.



---

archive/issue_comments_055526.json:
```json
{
    "body": "I've had a talk with my OR colleague. I don't think \"A list of pairs (weight,value) where each pair is repeated the number of times it is taken into the solution. \" is the proper English grammar for what is meant. I think \"A list of pairs (w_i, u_i), for each object i occurring in the solution. \" is better. Do you agree? \n\nAlso, he suggested that the \"objective value\" (or maximal useful value, in your terminology) be included in the solution. Perhaps you could include this as an optional keyword, leaving the current behaviour as the default? If you also agree to this, please add a corresponding example to the docstring.",
    "created_at": "2009-08-20T23:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55526",
    "user": "@wdjoyner"
}
```

I've had a talk with my OR colleague. I don't think "A list of pairs (weight,value) where each pair is repeated the number of times it is taken into the solution. " is the proper English grammar for what is meant. I think "A list of pairs (w_i, u_i), for each object i occurring in the solution. " is better. Do you agree? 

Also, he suggested that the "objective value" (or maximal useful value, in your terminology) be included in the solution. Perhaps you could include this as an optional keyword, leaving the current behaviour as the default? If you also agree to this, please add a corresponding example to the docstring.



---

archive/issue_comments_055527.json:
```json
{
    "body": "Excellent suggestion ! So :\n* I fixed the grammar error ( sorry, I'm still learning english every day ;-) )\n* I Included the objective value in the output\n\nBut :\nActually, this objective value requires no computation at all as it is automatically computed by the LP solver.. So as it can be useful anyway, the function now returns a pair [value, list] ( where list is the value the function returned previously ), and value=maximum useful value.\nBesides, I added the flag value_only in case the use only needs the optimal value and does not care about the assignment. This, because the LP solvers can be forced not to return the assignment of the variables and only the objective value, avoiding this way some computations.\n\nBesides, this syntax makes knapsack consistant with the other optimization functions I wrote for graphs, and I hope will all the LP functions we will write in the future ;-)\n\nTo avoid mistakes, I updated both patches ( they were identical ), and the new version obviously contains the old one, plus the update I just wrote ! \n\nThank you for your review !\n\nNathann",
    "created_at": "2009-08-21T07:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55527",
    "user": "@nathanncohen"
}
```

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

archive/issue_comments_055528.json:
```json
{
    "body": "There was this failure:\n\n\n```\nsage -t  \"devel/sage/sage/numerical/knapsack.py\"            \n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage/sage/numerical/knapsack.py\", line 608:\n    sage: knapsack([1,1.5,0.5], max=2)\nExpected:\n    [2.0, [1, 0.500000000000000]]\nGot:\n    [2.0, [1.50000000000000, 0.500000000000000]]\n**********************************************************************\n```\n",
    "created_at": "2009-08-22T01:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55528",
    "user": "@wdjoyner"
}
```

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

archive/issue_comments_055529.json:
```json
{
    "body": "I always forget the LP solvers are non-deterministic algorithms, and because of this the values they return sometimes change, which causes trouble with docstrings ;-)\n\nSorry !\n\n( Fixed, as usual the two patches are updated )",
    "created_at": "2009-08-22T06:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55529",
    "user": "@nathanncohen"
}
```

I always forget the LP solvers are non-deterministic algorithms, and because of this the values they return sometimes change, which causes trouble with docstrings ;-)

Sorry !

( Fixed, as usual the two patches are updated )



---

archive/issue_comments_055530.json:
```json
{
    "body": "This last patch (and its dependency) installed fine as before (same system, and version) with the following failures:\n\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/doc/en/bordeaux_2008/birds_other.rst\"\n        sage -t  \"devel/sage/sage/interfaces/maxima.py\"\n        sage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n```\n\nI think these are unrelated, so this gets a positive review from me. Thanks for implementing it!",
    "created_at": "2009-08-22T18:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55530",
    "user": "@wdjoyner"
}
```

This last patch (and its dependency) installed fine as before (same system, and version) with the following failures:


```
The following tests failed:


        sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

I think these are unrelated, so this gets a positive review from me. Thanks for implementing it!



---

archive/issue_comments_055531.json:
```json
{
    "body": "This will have to wait until #6502 is resolved. Which patch is to be merged? Most likely, I think some if not all doctests would have to be flagged with \"# optional\" if they require the optional GLPK spkg.",
    "created_at": "2009-08-25T03:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55531",
    "user": "mvngu"
}
```

This will have to wait until #6502 is resolved. Which patch is to be merged? Most likely, I think some if not all doctests would have to be flagged with "# optional" if they require the optional GLPK spkg.



---

archive/issue_comments_055532.json:
```json
{
    "body": "Attachment [knapsack.patch](tarball://root/attachments/some-uuid/ticket6749/knapsack.patch) by @nathanncohen created at 2009-08-25 06:55:31",
    "created_at": "2009-08-25T06:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55532",
    "user": "@nathanncohen"
}
```

Attachment [knapsack.patch](tarball://root/attachments/some-uuid/ticket6749/knapsack.patch) by @nathanncohen created at 2009-08-25 06:55:31



---

archive/issue_comments_055533.json:
```json
{
    "body": "Attachment [knapsack.2.patch](tarball://root/attachments/some-uuid/ticket6749/knapsack.2.patch) by @nathanncohen created at 2009-08-25 06:56:21\n\nUpdated. And you can apply any one of them, they're both the same ( I uploaded two by mistake the first time, then updated both )",
    "created_at": "2009-08-25T06:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55533",
    "user": "@nathanncohen"
}
```

Attachment [knapsack.2.patch](tarball://root/attachments/some-uuid/ticket6749/knapsack.2.patch) by @nathanncohen created at 2009-08-25 06:56:21

Updated. And you can apply any one of them, they're both the same ( I uploaded two by mistake the first time, then updated both )



---

archive/issue_comments_055534.json:
```json
{
    "body": "This patch (on top of the updated 6502) did not apply for me (4.1.1.rc2, intel macbook 10.4.11).",
    "created_at": "2009-08-25T18:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55534",
    "user": "@wdjoyner"
}
```

This patch (on top of the updated 6502) did not apply for me (4.1.1.rc2, intel macbook 10.4.11).



---

archive/issue_comments_055535.json:
```json
{
    "body": "I am using 4.1.1, perhaps it explains ?\n\nI just tried it again with only 6502 and this one, and noticed nothing wrong O_o",
    "created_at": "2009-08-25T18:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55535",
    "user": "@nathanncohen"
}
```

I am using 4.1.1, perhaps it explains ?

I just tried it again with only 6502 and this one, and noticed nothing wrong O_o



---

archive/issue_comments_055536.json:
```json
{
    "body": "Could you please try it again on a 4.1.1 ?",
    "created_at": "2009-08-25T18:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55536",
    "user": "@nathanncohen"
}
```

Could you please try it again on a 4.1.1 ?



---

archive/issue_comments_055537.json:
```json
{
    "body": "Replying to [comment:18 ncohen]:\n> Could you please try it again on a 4.1.1 ?\n\nI created a new clone and re-tried this. This time it worked! Passed tests as before (same Sage version, same machine ....).",
    "created_at": "2009-08-25T20:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55537",
    "user": "@wdjoyner"
}
```

Replying to [comment:18 ncohen]:
> Could you please try it again on a 4.1.1 ?

I created a new clone and re-tried this. This time it worked! Passed tests as before (same Sage version, same machine ....).



---

archive/issue_comments_055538.json:
```json
{
    "body": "As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.\n\nSorry for the trouble, I'll try to make it quick !\n\nNathann",
    "created_at": "2009-08-31T15:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55538",
    "user": "@nathanncohen"
}
```

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann



---

archive/issue_comments_055539.json:
```json
{
    "body": "Here is the new version, slightly modified to use the symbolics from #6869 ( the new version of MIP you need to try this code ! )",
    "created_at": "2009-09-03T09:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55539",
    "user": "@nathanncohen"
}
```

Here is the new version, slightly modified to use the symbolics from #6869 ( the new version of MIP you need to try this code ! )



---

archive/issue_comments_055540.json:
```json
{
    "body": "Attachment [knapsack-symbolics.patch](tarball://root/attachments/some-uuid/ticket6749/knapsack-symbolics.patch) by @nathanncohen created at 2009-09-03 09:44:24",
    "created_at": "2009-09-03T09:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55540",
    "user": "@nathanncohen"
}
```

Attachment [knapsack-symbolics.patch](tarball://root/attachments/some-uuid/ticket6749/knapsack-symbolics.patch) by @nathanncohen created at 2009-09-03 09:44:24



---

archive/issue_comments_055541.json:
```json
{
    "body": "This applies fine to 4.1.2.a0 and passes testall without any other packages installed (no glpk, etc).\n\nRunning more tests...",
    "created_at": "2009-09-08T18:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55541",
    "user": "@wdjoyner"
}
```

This applies fine to 4.1.2.a0 and passes testall without any other packages installed (no glpk, etc).

Running more tests...



---

archive/issue_comments_055542.json:
```json
{
    "body": "This applies fine to 4.1.2.a0 and passes testall with glpk package installed.",
    "created_at": "2009-09-09T10:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55542",
    "user": "@wdjoyner"
}
```

This applies fine to 4.1.2.a0 and passes testall with glpk package installed.



---

archive/issue_comments_055543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-10T12:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55543",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055544.json:
```json
{
    "body": "Merged `knapsack-symbolics.patch`.\n\n\n\nWith `knapsack-symbolics.patch`, I got a warning when building the reference manual:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/local/lib/python2.6/site-packages/sage/numerical/knapsack.py:docstring of sage.numerical.knapsack.knapsack:69: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```\n\nSee #6916 for a follow-up to this ticket.",
    "created_at": "2009-09-10T12:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6749#issuecomment-55544",
    "user": "mvngu"
}
```

Merged `knapsack-symbolics.patch`.



With `knapsack-symbolics.patch`, I got a warning when building the reference manual:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha1/local/lib/python2.6/site-packages/sage/numerical/knapsack.py:docstring of sage.numerical.knapsack.knapsack:69: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```

See #6916 for a follow-up to this ticket.
