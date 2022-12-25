# Issue 9852: Enumerate Integer solution of a LP through new CPLEX interface

archive/issues_009852.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  @nthiery\n\nThis tickets implements a new (and direct) interface to CPLEX, using its C library. We are now able to iterate over integer solutions of a MILP, which is a *very* good news (after quite a lot of work debugging Cython code) `:-D`\n\nI also updated the method MixedIntegerLinearProgram.solve to show two different ways to use CPLEX, and modified modules_list.py to compile the right files. #8880 is not needed either anymore once this patch is merged.\n\nTips for the reviewer :\n\n* Do not read the parts of the .patch file related to the changes in files mip_cplex and mip_osi cplex. Here is what happened : the former file named mip_cplex has been renamed to mip_osi_cplex (as it uses CPLEX through the OSI library), and the mip_cplex file is brand new, and contains the new interface. Of course, I changed in the docstrings of mip_osi_cplex lines such as \n  {{{\n  from sage.numerical.mip_cplex import [something]\n  }}}\n  to\n  {{{\n  from sage.numerical.mip_osi_cplex import [something]\n  }}}\n  So there is no need to deal with all these - and + lines.\n*  Please, pick an enumeration problem that you like, and check CPLEX is indeed returning ALL the solutions. It first \"forgot\" some of them, and I had to change a very badly documented parameter to get all the answers I wanted for my problems. Please check on some other examples `:-)`\n\nNathann\n     \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9853\n\n",
    "closed_at": "2010-10-09T08:46:15Z",
    "created_at": "2010-09-03T18:39:05Z",
    "labels": [
        "component: linear programming"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Enumerate Integer solution of a LP through new CPLEX interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9852",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, jkantor

CC:  @nthiery

This tickets implements a new (and direct) interface to CPLEX, using its C library. We are now able to iterate over integer solutions of a MILP, which is a *very* good news (after quite a lot of work debugging Cython code) `:-D`

I also updated the method MixedIntegerLinearProgram.solve to show two different ways to use CPLEX, and modified modules_list.py to compile the right files. #8880 is not needed either anymore once this patch is merged.

Tips for the reviewer :

* Do not read the parts of the .patch file related to the changes in files mip_cplex and mip_osi cplex. Here is what happened : the former file named mip_cplex has been renamed to mip_osi_cplex (as it uses CPLEX through the OSI library), and the mip_cplex file is brand new, and contains the new interface. Of course, I changed in the docstrings of mip_osi_cplex lines such as 
  {{{
  from sage.numerical.mip_cplex import [something]
  }}}
  to
  {{{
  from sage.numerical.mip_osi_cplex import [something]
  }}}
  So there is no need to deal with all these - and + lines.
*  Please, pick an enumeration problem that you like, and check CPLEX is indeed returning ALL the solutions. It first "forgot" some of them, and I had to change a very badly documented parameter to get all the answers I wanted for my problems. Please check on some other examples `:-)`

Nathann
     


Issue created by migration from https://trac.sagemath.org/ticket/9853





---

archive/issue_comments_097080.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-03T18:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97080",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097081.json:
```json
{
    "body": "Changing component from numerical to linear programming.",
    "created_at": "2010-09-06T11:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97081",
    "user": "https://github.com/nathanncohen"
}
```

Changing component from numerical to linear programming.



---

archive/issue_comments_097082.json:
```json
{
    "body": "Attachment [trac_9853.patch](tarball://root/attachments/some-uuid/ticket9853/trac_9853.patch) by @nathanncohen created at 2010-09-19 10:52:28",
    "created_at": "2010-09-19T10:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97082",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9853.patch](tarball://root/attachments/some-uuid/ticket9853/trac_9853.patch) by @nathanncohen created at 2010-09-19 10:52:28



---

archive/issue_comments_097083.json:
```json
{
    "body": "(just added a sage_free where I had forgotten it) `:-)`\n\nNathann",
    "created_at": "2010-09-19T10:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97083",
    "user": "https://github.com/nathanncohen"
}
```

(just added a sage_free where I had forgotten it) `:-)`

Nathann



---

archive/issue_comments_097084.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T15:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97084",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_097085.json:
```json
{
    "body": "This ticket also modifies files which are deleted by #10043. I'll rewrite it using the new interface anyway !\n\nNathann",
    "created_at": "2010-10-09T08:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97085",
    "user": "https://github.com/nathanncohen"
}
```

This ticket also modifies files which are deleted by #10043. I'll rewrite it using the new interface anyway !

Nathann



---

archive/issue_events_024798.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-09T08:46:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9852#event-24798"
}
```



---

archive/issue_comments_097086.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-10-09T08:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97086",
    "user": "https://github.com/qed777"
}
```

Resolution: invalid



---

archive/issue_events_024799.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-09T08:46:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9852#event-24799"
}
```



---

archive/issue_comments_097087.json:
```json
{
    "body": "Why was this ticket considered as invalid?",
    "created_at": "2012-01-04T23:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97087",
    "user": "https://github.com/nthiery"
}
```

Why was this ticket considered as invalid?



---

archive/issue_comments_097088.json:
```json
{
    "body": "> Why was this ticket considered as invalid?\n\n\nBecause it worked on an ooooooold version of the LP backends, that have been totally rewritten since. But it is nice to have this code around, because I remember I went through hell to find the CPLEX methods that should be use to enumerate integer solutions.\n\nThis being said, we have a Gurobi backend too, now. Perhaps it can also enumerate integer solutions.",
    "created_at": "2012-01-04T23:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97088",
    "user": "https://github.com/nathanncohen"
}
```

> Why was this ticket considered as invalid?


Because it worked on an ooooooold version of the LP backends, that have been totally rewritten since. But it is nice to have this code around, because I remember I went through hell to find the CPLEX methods that should be use to enumerate integer solutions.

This being said, we have a Gurobi backend too, now. Perhaps it can also enumerate integer solutions.



---

archive/issue_comments_097089.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> Because it worked on an ooooooold version of the LP backends, that have been totally rewritten since. But it is nice to have this code around, because I remember I went through hell to find the CPLEX methods that should be use to enumerate integer solutions.\n> \n> This being said, we have a Gurobi backend too, now. Perhaps it can also enumerate integer solutions.\n\n\nOk, so it's more like the current patch is invalid. The feature would still be useful (be it implemented through CPLEX or other). So, unless there is another ticket for this feature, I would recommend to (have the release manager?) reopen this ticket.\n\nCheers,\n                                Nicolas",
    "created_at": "2012-01-05T01:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9852#issuecomment-97089",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:8 ncohen]:
> Because it worked on an ooooooold version of the LP backends, that have been totally rewritten since. But it is nice to have this code around, because I remember I went through hell to find the CPLEX methods that should be use to enumerate integer solutions.
> 
> This being said, we have a Gurobi backend too, now. Perhaps it can also enumerate integer solutions.


Ok, so it's more like the current patch is invalid. The feature would still be useful (be it implemented through CPLEX or other). So, unless there is another ticket for this feature, I would recommend to (have the release manager?) reopen this ticket.

Cheers,
                                Nicolas
