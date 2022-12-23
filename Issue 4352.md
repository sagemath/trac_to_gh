# Issue 4352: add support for weight vectors to gran/groebner_fan

archive/issues_004352.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: gfan, groebner_fan, weight vectors\n\nThis should be pretty straightforward.\n\nsage-support request from Ursula Whitcher:\nI asked Anders Jensen, \"I would like to compute the weight vectors\ncorresponding to each reduced Groebner basis in gfan's output.  Is\nthere a way to tell gfan to do this?\"\n\nHe replied:\n\n\"There is a command \"weightvector\" that does exactly this. The command\nis hidden (does not show up in the manual or the file system). To run\nit type \"gfan _weightvector\" in your shell. MIND THE SPACE BEFORE '_'.\nAccording to the --help text the correct thing to do would be to run\n\"gfan _weightvector -m\" with the gfan output as input.\n\nFor example\ngfan | gfan _weightvector -m\nQ[x,y]\n{x-y}\n\nwill produce a list of two vectors.\nI hope this works out for you.\nBest regards,\nAnders\"\n\nIs there a way to access the weightvector command from the Sage\nimplementation of gfan?\n\nThanks!\nUrsula \n\nIssue created by migration from https://trac.sagemath.org/ticket/4352\n\n",
    "created_at": "2008-10-23T21:23:08Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "title": "add support for weight vectors to gran/groebner_fan",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4352",
    "user": "mhampton"
}
```
Assignee: mhampton

Keywords: gfan, groebner_fan, weight vectors

This should be pretty straightforward.

sage-support request from Ursula Whitcher:
I asked Anders Jensen, "I would like to compute the weight vectors
corresponding to each reduced Groebner basis in gfan's output.  Is
there a way to tell gfan to do this?"

He replied:

"There is a command "weightvector" that does exactly this. The command
is hidden (does not show up in the manual or the file system). To run
it type "gfan _weightvector" in your shell. MIND THE SPACE BEFORE '_'.
According to the --help text the correct thing to do would be to run
"gfan _weightvector -m" with the gfan output as input.

For example
gfan | gfan _weightvector -m
Q[x,y]
{x-y}

will produce a list of two vectors.
I hope this works out for you.
Best regards,
Anders"

Is there a way to access the weightvector command from the Sage
implementation of gfan?

Thanks!
Ursula 

Issue created by migration from https://trac.sagemath.org/ticket/4352





---

archive/issue_comments_031959.json:
```json
{
    "body": "Attachment\n\nbased on 3.1.4 but should be fine against 3.2-alpha0",
    "created_at": "2008-10-24T02:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4352#issuecomment-31959",
    "user": "mhampton"
}
```

Attachment

based on 3.1.4 but should be fine against 3.2-alpha0



---

archive/issue_comments_031960.json:
```json
{
    "body": "REVIEW:\n\npatch applies and passes test.  Code raises major red flag!!\n\n```\n\t        ans = eval(ans.replace('{','').replace('}','').replace('\\n','')) \n```\n\n\nIf the output -- which you make into vectors over QQ ever actually has any rational numbers, then eval will do very bad things to them, e.g., \n\n```\nsage: eval('2/3')\n0\n```\n\nOops!\n\nUse sage_eval instead:\n\n```\nsage: sage_eval('2/3')\n2/3\n```\n",
    "created_at": "2008-11-29T02:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4352#issuecomment-31960",
    "user": "was"
}
```

REVIEW:

patch applies and passes test.  Code raises major red flag!!

```
	        ans = eval(ans.replace('{','').replace('}','').replace('\n','')) 
```


If the output -- which you make into vectors over QQ ever actually has any rational numbers, then eval will do very bad things to them, e.g., 

```
sage: eval('2/3')
0
```

Oops!

Use sage_eval instead:

```
sage: sage_eval('2/3')
2/3
```




---

archive/issue_comments_031961.json:
```json
{
    "body": "Attachment\n\nsupercedes previous patch, addresses review",
    "created_at": "2008-11-29T14:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4352#issuecomment-31961",
    "user": "mhampton"
}
```

Attachment

supercedes previous patch, addresses review



---

archive/issue_comments_031962.json:
```json
{
    "body": "This patch no longer applies cleanly to my 3.2.1.rc1 merge tree:\n\n```\nsage-3.2.1.rc1/devel/sage$ patch -p1 --dry-run < trac_4352_2.patch \npatching file sage/rings/polynomial/groebner_fan.py\nHunk #2 FAILED at 76.\n1 out of 3 hunks FAILED -- saving rejects to file sage/rings/polynomial/groebner_fan.py.rej\n```\n\nI gather from the patch description that only trac_4352_2.patch should be applied. So unless I am mistaken please rebase this. If there are unknown dependencies for this ticket please list them.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T06:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4352#issuecomment-31962",
    "user": "mabshoff"
}
```

This patch no longer applies cleanly to my 3.2.1.rc1 merge tree:

```
sage-3.2.1.rc1/devel/sage$ patch -p1 --dry-run < trac_4352_2.patch 
patching file sage/rings/polynomial/groebner_fan.py
Hunk #2 FAILED at 76.
1 out of 3 hunks FAILED -- saving rejects to file sage/rings/polynomial/groebner_fan.py.rej
```

I gather from the patch description that only trac_4352_2.patch should be applied. So unless I am mistaken please rebase this. If there are unknown dependencies for this ticket please list them.

Cheers,

Michael



---

archive/issue_comments_031963.json:
```json
{
    "body": "Attachment\n\nrebased against 3.2.1.rc0",
    "created_at": "2008-11-30T14:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4352#issuecomment-31963",
    "user": "mhampton"
}
```

Attachment

rebased against 3.2.1.rc0



---

archive/issue_comments_031964.json:
```json
{
    "body": "Merged 4352_3.patch in Sage 3.2.1.rc1",
    "created_at": "2008-11-30T23:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4352#issuecomment-31964",
    "user": "mabshoff"
}
```

Merged 4352_3.patch in Sage 3.2.1.rc1



---

archive/issue_comments_031965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T23:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4352#issuecomment-31965",
    "user": "mabshoff"
}
```

Resolution: fixed
