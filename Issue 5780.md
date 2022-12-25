# Issue 5780: [with patch; positive review] plotting -- deal with NaN's in plot range

archive/issues_005780.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5780\n\n",
    "closed_at": "2009-04-15T23:18:35Z",
    "created_at": "2009-04-13T20:13:41Z",
    "labels": [
        "component: graphics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; positive review] plotting -- deal with NaN's in plot range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5780",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/5780





---

archive/issue_comments_045166.json:
```json
{
    "body": "Attachment [trac5780.patch](tarball://root/attachments/some-uuid/ticket5780/trac5780.patch) by mabshoff created at 2009-04-13 23:15:11\n\nI like this patch, but there is a slight doctesting issue:\n\n```\nbash-3.00$ ./sage -t -long devel/sage/sage/coding/code_bounds.py\nsage -t -long \"devel/sage/sage/coding/code_bounds.py\"       \n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py\", line 383:\n    sage: plot(f,0,1)\nExpected nothing\nGot:\n    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)\n    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py\", line 395:\n    sage: plot(f,0,1)\nExpected nothing\nGot:\n    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)\n    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)\n    <BLANKLINE>\n**********************************************************************\n```\nThis is on Solaris and #5779 which RobertWB should have a patch for tonight might then fix the problem. \n\nAnother possibility would be to set verbosity to -1 for this particular doctest, but I would like to avoid that. Positive review for the fix, but I will wait to change the subject once we have dealt with the verbosity.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T23:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac5780.patch](tarball://root/attachments/some-uuid/ticket5780/trac5780.patch) by mabshoff created at 2009-04-13 23:15:11

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

archive/issue_comments_045167.json:
```json
{
    "body": "Looks good to me. There is another problem unrelated to this in this area of the plotting code, but that is another ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T23:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. There is another problem unrelated to this in this area of the plotting code, but that is another ticket.

Cheers,

Michael



---

archive/issue_comments_045168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T23:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013567.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-15T23:18:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5780#event-13567"
}
```



---

archive/issue_comments_045169.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T23:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5780#issuecomment-45169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
