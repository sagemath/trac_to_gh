# Issue 8763: put licensing information into published worksheets

archive/issues_008763.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman @fchapoton\n\nAs discussed in http://groups.google.com/group/sage-edu/browse_thread/thread/aa651032bb34a285, it would be very nice if published worksheets could include licensing information, so that we could collect, modify, and redistribute excellent worksheets.\n\nSo, when publishing worksheets, there should be a mechanism to choose a license; as a start, maybe just hard-code four choices: CC by-sa-nc, by-sa, GFDL, and no licensing information at all. If a license is chosen, this would put something like this into the worksheet:\n\n```\n<a rel=\"license\" href=\"http://creativecommons.org/licenses/by-sa/3.0/us/\">\n<img alt=\"Creative Commons License\" style=\"border-width:0\" \nsrc=\"http://i.creativecommons.org/l/by-sa/3.0/us/80x15.png\" \n/></a><br />This worksheet is licensed under a <a rel=\"license\" \nhref=\"http://creativecommons.org/licenses/by-sa/3.0/us/\">Creative \nCommons Attribution-Share Alike 3.0 United States License</a>.\n```\n\nThe rel=\"license\" bit is a microformat that will make the licensing information computer-readable, so that eventually one could search for worksheets available with a certain license.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8763\n\n",
    "created_at": "2010-04-25T07:24:53Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "put licensing information into published worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8763",
    "user": "https://github.com/dandrake"
}
```
Assignee: jason, was

CC:  @kcrisman @fchapoton

As discussed in http://groups.google.com/group/sage-edu/browse_thread/thread/aa651032bb34a285, it would be very nice if published worksheets could include licensing information, so that we could collect, modify, and redistribute excellent worksheets.

So, when publishing worksheets, there should be a mechanism to choose a license; as a start, maybe just hard-code four choices: CC by-sa-nc, by-sa, GFDL, and no licensing information at all. If a license is chosen, this would put something like this into the worksheet:

```
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/us/">
<img alt="Creative Commons License" style="border-width:0" 
src="http://i.creativecommons.org/l/by-sa/3.0/us/80x15.png" 
/></a><br />This worksheet is licensed under a <a rel="license" 
href="http://creativecommons.org/licenses/by-sa/3.0/us/">Creative 
Commons Attribution-Share Alike 3.0 United States License</a>.
```

The rel="license" bit is a microformat that will make the licensing information computer-readable, so that eventually one could search for worksheets available with a certain license.

Issue created by migration from https://trac.sagemath.org/ticket/8763





---

archive/issue_comments_080041.json:
```json
{
    "body": "Can we add CC-by and CC0 (http://creativecommons.org/publicdomain/) as well?",
    "created_at": "2010-04-26T23:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80041",
    "user": "https://github.com/jasongrout"
}
```

Can we add CC-by and CC0 (http://creativecommons.org/publicdomain/) as well?



---

archive/issue_comments_080042.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> Can we add CC-by and CC0 (http://creativecommons.org/publicdomain/) as well?\n\nIf you make a patch, you can add any licenses you want. :)",
    "created_at": "2010-04-27T00:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80042",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:1 jason]:
> Can we add CC-by and CC0 (http://creativecommons.org/publicdomain/) as well?

If you make a patch, you can add any licenses you want. :)



---

archive/issue_comments_080043.json:
```json
{
    "body": "I believe that if we want to incorporate such worksheets eventually into the Sage proper, none of the above licenses would allow it, as I think all are incompatible with GPL.  Ah, the joys of licensing headaches!",
    "created_at": "2010-05-11T16:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80043",
    "user": "https://github.com/jasongrout"
}
```

I believe that if we want to incorporate such worksheets eventually into the Sage proper, none of the above licenses would allow it, as I think all are incompatible with GPL.  Ah, the joys of licensing headaches!



---

archive/issue_comments_080044.json:
```json
{
    "body": "(well, I believe CC-by and CC0 would allow incorporation into a GPL project).",
    "created_at": "2010-05-11T16:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80044",
    "user": "https://github.com/jasongrout"
}
```

(well, I believe CC-by and CC0 would allow incorporation into a GPL project).



---

archive/issue_comments_080045.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> I believe that if we want to incorporate such worksheets eventually into the Sage proper, none of the above licenses would allow it, as I think all are incompatible with GPL.  Ah, the joys of licensing headaches!\n\nWell, I don't want to get into licensing discussion here, but my first thought was that there's a difference between \"functionally including\" something into Sage -- adding new code or doctests -- and just including some ancillary material. From a licensing perspective, there's perhaps no difference.\n\nIn any case, clear licensing information would make it easier for someone to somehow collect and redistribute good worksheets.",
    "created_at": "2010-05-11T23:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80045",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:3 jason]:
> I believe that if we want to incorporate such worksheets eventually into the Sage proper, none of the above licenses would allow it, as I think all are incompatible with GPL.  Ah, the joys of licensing headaches!

Well, I don't want to get into licensing discussion here, but my first thought was that there's a difference between "functionally including" something into Sage -- adding new code or doctests -- and just including some ancillary material. From a licensing perspective, there's perhaps no difference.

In any case, clear licensing information would make it easier for someone to somehow collect and redistribute good worksheets.



---

archive/issue_comments_080046.json:
```json
{
    "body": "As a note for whoever implements this: given [this message to sage-edu](https://groups.google.com/group/sage-edu/msg/2d9f106c9b358b4e), perhaps when setting license information, the notebook should ask the user what name to use for attribution. A suggestion of \"name <email>\" would be helpful.",
    "created_at": "2011-04-20T00:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80046",
    "user": "https://github.com/dandrake"
}
```

As a note for whoever implements this: given [this message to sage-edu](https://groups.google.com/group/sage-edu/msg/2d9f106c9b358b4e), perhaps when setting license information, the notebook should ask the user what name to use for attribution. A suggestion of "name <email>" would be helpful.



---

archive/issue_comments_080047.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80047",
    "user": "https://github.com/mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_080048.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80048",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080049.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-13T07:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8763#issuecomment-80049",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
