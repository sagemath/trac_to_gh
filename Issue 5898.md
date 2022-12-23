# Issue 5898: Plot Field doc

archive/issues_005898.json:
```json
{
    "body": "Assignee: was\n\nThere are a few minor bugs in plot_field.py which should be fixed, e.g. importing math.sqrt when in fact the symbolic square root is imported shortly thereafter (and correctly).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5898\n\n",
    "created_at": "2009-04-26T02:22:12Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "Plot Field doc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5898",
    "user": "kcrisman"
}
```
Assignee: was

There are a few minor bugs in plot_field.py which should be fixed, e.g. importing math.sqrt when in fact the symbolic square root is imported shortly thereafter (and correctly).

Issue created by migration from https://trac.sagemath.org/ticket/5898





---

archive/issue_comments_046630.json:
```json
{
    "body": "Based on 3.4.2.alpha0",
    "created_at": "2009-04-26T02:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5898#issuecomment-46630",
    "user": "kcrisman"
}
```

Based on 3.4.2.alpha0



---

archive/issue_comments_046631.json:
```json
{
    "body": "Attachment\n\nThis patch brings coverage of plot_field.py to 100% and fixes a few minor bugs.  \n\nIf I did not ReSTify correctly, reviewer please give extremely explicit directions for how to correct this.  Also I hope that the init method test will not cause numerical noise problems but please give explicit instructions on how to correct for that.  I find both of those issues confusing to do properly.",
    "created_at": "2009-04-26T02:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5898#issuecomment-46631",
    "user": "kcrisman"
}
```

Attachment

This patch brings coverage of plot_field.py to 100% and fixes a few minor bugs.  

If I did not ReSTify correctly, reviewer please give extremely explicit directions for how to correct this.  Also I hope that the init method test will not cause numerical noise problems but please give explicit instructions on how to correct for that.  I find both of those issues confusing to do properly.



---

archive/issue_comments_046632.json:
```json
{
    "body": "reviewer patch based on sage-3.4.2.alpha0",
    "created_at": "2009-04-26T04:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5898#issuecomment-46632",
    "user": "mvngu"
}
```

reviewer patch based on sage-3.4.2.alpha0



---

archive/issue_comments_046633.json:
```json
{
    "body": "Attachment\n\nREFEREE REPORT\n\n\n\nThat patch `plot_field-patch.patch` applies OK against Sage 3.4.2.alpha0. All doctests passed with options `-t -long`, and the coverage for `sage/plot/plot_field.py` is indeed 100% as claimed. However, when I ran the coverage on that file, I received this\n\n```\n[mvngu@sage sage-3.4.2.alpha0]$ ./sage -coverage devel/sage-exp/sage/plot/plot_field.py \n----------------------------------------------------------------------\ndevel/sage-exp/sage/plot/plot_field.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE devel/sage-exp/sage/plot/plot_field.py: 100% (7 of 7)\n\nPossibly wrong (function name doesn't occur in doctests):\n         * _repr_(self):\n         * _render_on_subplot(self, subplot):\n```\n\nNotice the line\n\n```\nERROR: Please define a s == loads(dumps(s)) doctest.\n```\n\nApart from that, there are some minor typos. These are trivial to fix. The reviewer patch `trac_5898-referee.patch` should take care of them. Basically, it adds a test to dump and load a plot so that the above error line should be gone when running coverage on `sage/plot/plot_field.py `. So `plot_field-patch.patch` gets a positive review; only `trac_5898-referee.patch` needs to be reviewed.",
    "created_at": "2009-04-26T04:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5898#issuecomment-46633",
    "user": "mvngu"
}
```

Attachment

REFEREE REPORT



That patch `plot_field-patch.patch` applies OK against Sage 3.4.2.alpha0. All doctests passed with options `-t -long`, and the coverage for `sage/plot/plot_field.py` is indeed 100% as claimed. However, when I ran the coverage on that file, I received this

```
[mvngu@sage sage-3.4.2.alpha0]$ ./sage -coverage devel/sage-exp/sage/plot/plot_field.py 
----------------------------------------------------------------------
devel/sage-exp/sage/plot/plot_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage-exp/sage/plot/plot_field.py: 100% (7 of 7)

Possibly wrong (function name doesn't occur in doctests):
         * _repr_(self):
         * _render_on_subplot(self, subplot):
```

Notice the line

```
ERROR: Please define a s == loads(dumps(s)) doctest.
```

Apart from that, there are some minor typos. These are trivial to fix. The reviewer patch `trac_5898-referee.patch` should take care of them. Basically, it adds a test to dump and load a plot so that the above error line should be gone when running coverage on `sage/plot/plot_field.py `. So `plot_field-patch.patch` gets a positive review; only `trac_5898-referee.patch` needs to be reviewed.



---

archive/issue_comments_046634.json:
```json
{
    "body": "Patches apply to 3.4.2.a0 and pass sage -testall. \nThe referee patch fixes some simply typos. The original patch adds details to the documentation, as claimed.",
    "created_at": "2009-04-26T11:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5898#issuecomment-46634",
    "user": "wdj"
}
```

Patches apply to 3.4.2.a0 and pass sage -testall. 
The referee patch fixes some simply typos. The original patch adds details to the documentation, as claimed.



---

archive/issue_comments_046635.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T05:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5898#issuecomment-46635",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046636.json:
```json
{
    "body": "Merged both patches in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T05:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5898#issuecomment-46636",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.2.rc0.

Cheers,

Michael
