# Issue 2783: notebook -- ocassional "crap" in output like this   print "\x01r\x01e580"

archive/issues_002783.json:
```json
{
    "body": "Assignee: boothby\n\nHi,\n\nI was very embarrassed while teaching today since maybe 15 times I got\ncrap like this in the output from the notebook:\n\n```\nprint \"\\x01r\\x01e580\"\n```\n\n\nThis is from the synchronization code that *I* wrote.  It \"should\" never happen.  Anyways it does -- but of course only when 40 people are watching you :-(.  Anyways, to solve this ticket should mean to simply look at that synchro code again, think about it, and rewrite it in a way that is _more_ robust. \n\nWilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/2783\n\n",
    "created_at": "2008-04-02T22:17:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- ocassional \"crap\" in output like this   print \"\\x01r\\x01e580\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2783",
    "user": "was"
}
```
Assignee: boothby

Hi,

I was very embarrassed while teaching today since maybe 15 times I got
crap like this in the output from the notebook:

```
print "\x01r\x01e580"
```


This is from the synchronization code that *I* wrote.  It "should" never happen.  Anyways it does -- but of course only when 40 people are watching you :-(.  Anyways, to solve this ticket should mean to simply look at that synchro code again, think about it, and rewrite it in a way that is _more_ robust. 

William

Issue created by migration from https://trac.sagemath.org/ticket/2783





---

archive/issue_comments_019106.json:
```json
{
    "body": "According to the ticket description the ticket should be marked as invalid since it's past June 1st.",
    "created_at": "2008-09-08T14:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19106",
    "user": "TimothyClemans"
}
```

According to the ticket description the ticket should be marked as invalid since it's past June 1st.



---

archive/issue_comments_019107.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-09-08T18:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19107",
    "user": "mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_019108.json:
```json
{
    "body": "Oh well: invalid.",
    "created_at": "2008-09-08T18:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19108",
    "user": "mabshoff"
}
```

Oh well: invalid.



---

archive/issue_comments_019109.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-09T01:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19109",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_019110.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-09-09T01:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19110",
    "user": "was"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_019111.json:
```json
{
    "body": "I am reopening this since I am able to systematically replicate it now.  All you have to do is\nuse rpy from the notebook, and right after that this crap appears. \n\n\n{{\nimport rpy\nrpy.std([1..1000])\n///\nprint \"\\x01r\\x01e96\"\n288.67499025720952\n}}",
    "created_at": "2008-09-09T01:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19111",
    "user": "was"
}
```

I am reopening this since I am able to systematically replicate it now.  All you have to do is
use rpy from the notebook, and right after that this crap appears. 


{{
import rpy
rpy.std([1..1000])
///
print "\x01r\x01e96"
288.67499025720952
}}



---

archive/issue_comments_019112.json:
```json
{
    "body": "\n```\n{{ \nimport rpy rpy.std([1..1000]) \n/// \nprint \"\\x01r\\x01e96\" 288.67499025720952 \n}}\n```\n",
    "created_at": "2008-09-09T01:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19112",
    "user": "was"
}
```


```
{{ 
import rpy rpy.std([1..1000]) 
/// 
print "\x01r\x01e96" 288.67499025720952 
}}
```




---

archive/issue_comments_019113.json:
```json
{
    "body": "Any chance this could be related to using a terminal which has trouble with dealing with the escape characters related to color? We had similar issues with sage0 and IPython.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T02:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19113",
    "user": "mabshoff"
}
```

Any chance this could be related to using a terminal which has trouble with dealing with the escape characters related to color? We had similar issues with sage0 and IPython.

Cheers,

Michael



---

archive/issue_comments_019114.json:
```json
{
    "body": "Isn't this likely some issue with escape character sequences from colored output being printed?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T00:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19114",
    "user": "mabshoff"
}
```

Isn't this likely some issue with escape character sequences from colored output being printed?

Cheers,

Michael



---

archive/issue_comments_019115.json:
```json
{
    "body": "> Isn't this likely some issue with escape character sequences from colored output being printed?\n\nI doubt it.  rpy is a C-library interface to R.\n\nThose special looking \\x01r characters are synchronization control characters that Sage itself (in the file worksheet.py) puts in the output stream. \n\nWilliam",
    "created_at": "2008-09-22T00:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19115",
    "user": "was"
}
```

> Isn't this likely some issue with escape character sequences from colored output being printed?

I doubt it.  rpy is a C-library interface to R.

Those special looking \x01r characters are synchronization control characters that Sage itself (in the file worksheet.py) puts in the output stream. 

William



---

archive/issue_comments_019116.json:
```json
{
    "body": "ok, good to know.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T00:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19116",
    "user": "mabshoff"
}
```

ok, good to know.

Cheers,

Michael



---

archive/issue_comments_019117.json:
```json
{
    "body": "I still see these pop up sporadically, and I can't reproduce it reliably.  Initial ticket said \"mark as invalid by June 1, 2008\", which is long past.  Thoughts?",
    "created_at": "2009-01-22T00:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19117",
    "user": "boothby"
}
```

I still see these pop up sporadically, and I can't reproduce it reliably.  Initial ticket said "mark as invalid by June 1, 2008", which is long past.  Thoughts?



---

archive/issue_comments_019118.json:
```json
{
    "body": "Has anyone had this problem recently?",
    "created_at": "2009-11-15T17:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19118",
    "user": "timdumol"
}
```

Has anyone had this problem recently?



---

archive/issue_comments_019119.json:
```json
{
    "body": "No, and using rpy2 instead doesn't produce it.  Moreover, I completely rewrote from scratch the pexpect interfaces to use a much better way of synchronizing IO.  The crap mentioned in this ticket was from the old way of synchronizing IO.   So I'm closing this as fixed.",
    "created_at": "2009-11-18T09:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19119",
    "user": "was"
}
```

No, and using rpy2 instead doesn't produce it.  Moreover, I completely rewrote from scratch the pexpect interfaces to use a much better way of synchronizing IO.  The crap mentioned in this ticket was from the old way of synchronizing IO.   So I'm closing this as fixed.



---

archive/issue_comments_019120.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-18T09:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19120",
    "user": "was"
}
```

Resolution: fixed
