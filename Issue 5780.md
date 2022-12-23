# Issue 5780: [with patch; needs review] plotting -- deal with NaN's in plot range

archive/issues_005780.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5780\n\n",
    "created_at": "2009-04-13T20:13:41Z",
    "labels": [
        "graphics",
        "blocker",
        "bug"
    ],
    "title": "[with patch; needs review] plotting -- deal with NaN's in plot range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5780",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/5780





---

archive/issue_comments_045252.json:
```json
{
    "body": "Attachment\n\nI like this patch, but there is a slight doctesting issue:\n\n```\nbash-3.00$ ./sage -t -long devel/sage/sage/coding/code_bounds.py\nsage -t -long \"devel/sage/sage/coding/code_bounds.py\"       \n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py\", line 383:\n    sage: plot(f,0,1)\nExpected nothing\nGot:\n    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)\n    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py\", line 395:\n    sage: plot(f,0,1)\nExpected nothing\nGot:\n    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)\n    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)\n    <BLANKLINE>\n**********************************************************************\n```\n\nThis is on Solaris and #5779 which RobertWB should have a patch for tonight might then fix the problem. \n\nAnother possibility would be to set verbosity to -1 for this particular doctest, but I would like to avoid that. Positive review for the fix, but I will wait to change the subject once we have dealt with the verbosity.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45252",
    "user": "mabshoff"
}
```

Attachment

I like this patch, but there is a slight doctesting issue:

```
bash-3.00$ ./sage -t -long devel/sage/sage/coding/code_bounds.py
sage -t -long "devel/sage/sage/coding/code_bounds.py"       
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py", line 383:
    sage: plot(f,0,1)
Expected nothing
Got:
    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)
    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)
    <BLANKLINE>
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py", line 395:
    sage: plot(f,0,1)
Expected nothing
Got:
    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)
    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)
    <BLANKLINE>
**********************************************************************
```

This is on Solaris and #5779 which RobertWB should have a patch for tonight might then fix the problem. 

Another possibility would be to set verbosity to -1 for this particular doctest, but I would like to avoid that. Positive review for the fix, but I will wait to change the subject once we have dealt with the verbosity.

Cheers,

Michael



---

archive/issue_comments_045253.json:
```json
{
    "body": "Looks good to me. There is another problem unrelated to this in this area of the plotting code, but that is another ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T23:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45253",
    "user": "mabshoff"
}
```

Looks good to me. There is another problem unrelated to this in this area of the plotting code, but that is another ticket.

Cheers,

Michael



---

archive/issue_comments_045254.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T23:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45254",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045255.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T23:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45255",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
