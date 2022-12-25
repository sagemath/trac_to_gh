# Issue 2783: notebook -- ocassional "crap" in output like this   print "\x01r\x01e580"

archive/issues_002783.json:
```json
{
    "body": "Assignee: boothby\n\nHi,\n\nI was very embarrassed while teaching today since maybe 15 times I got\ncrap like this in the output from the notebook:\n\n```\nprint \"\\x01r\\x01e580\"\n```\n\n\nThis is from the synchronization code that *I* wrote.  It \"should\" never happen.  Anyways it does -- but of course only when 40 people are watching you :-(.  Anyways, to solve this ticket should mean to simply look at that synchro code again, think about it, and rewrite it in a way that is _more_ robust. \n\nWilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/2783\n\n",
    "created_at": "2008-04-02T22:17:45Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook -- ocassional \"crap\" in output like this   print \"\\x01r\\x01e580\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2783",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_019066.json:
```json
{
    "body": "According to the ticket description the ticket should be marked as invalid since it's past June 1st.",
    "created_at": "2008-09-08T14:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19066",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

According to the ticket description the ticket should be marked as invalid since it's past June 1st.



---

archive/issue_comments_019067.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-09-08T18:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_019068.json:
```json
{
    "body": "Oh well: invalid.",
    "created_at": "2008-09-08T18:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oh well: invalid.



---

archive/issue_comments_019069.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-09T01:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19069",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_019070.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-09-09T01:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19070",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_019071.json:
```json
{
    "body": "I am reopening this since I am able to systematically replicate it now.  All you have to do is\nuse rpy from the notebook, and right after that this crap appears. \n\n\n{{\nimport rpy\nrpy.std([1..1000])\n///\nprint \"\\x01r\\x01e96\"\n288.67499025720952\n}}",
    "created_at": "2008-09-09T01:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19071",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_019072.json:
```json
{
    "body": "\n```\n{{ \nimport rpy rpy.std([1..1000]) \n/// \nprint \"\\x01r\\x01e96\" 288.67499025720952 \n}}\n```\n",
    "created_at": "2008-09-09T01:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19072",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_019073.json:
```json
{
    "body": "Any chance this could be related to using a terminal which has trouble with dealing with the escape characters related to color? We had similar issues with sage0 and IPython.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T02:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19073",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Any chance this could be related to using a terminal which has trouble with dealing with the escape characters related to color? We had similar issues with sage0 and IPython.

Cheers,

Michael



---

archive/issue_comments_019074.json:
```json
{
    "body": "Isn't this likely some issue with escape character sequences from colored output being printed?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T00:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Isn't this likely some issue with escape character sequences from colored output being printed?

Cheers,

Michael



---

archive/issue_comments_019075.json:
```json
{
    "body": "> Isn't this likely some issue with escape character sequences from colored output being printed?\n\nI doubt it.  rpy is a C-library interface to R.\n\nThose special looking \\x01r characters are synchronization control characters that Sage itself (in the file worksheet.py) puts in the output stream. \n\nWilliam",
    "created_at": "2008-09-22T00:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19075",
    "user": "https://github.com/williamstein"
}
```

> Isn't this likely some issue with escape character sequences from colored output being printed?

I doubt it.  rpy is a C-library interface to R.

Those special looking \x01r characters are synchronization control characters that Sage itself (in the file worksheet.py) puts in the output stream. 

William



---

archive/issue_comments_019076.json:
```json
{
    "body": "ok, good to know.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-22T00:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

ok, good to know.

Cheers,

Michael



---

archive/issue_comments_019077.json:
```json
{
    "body": "I still see these pop up sporadically, and I can't reproduce it reliably.  Initial ticket said \"mark as invalid by June 1, 2008\", which is long past.  Thoughts?",
    "created_at": "2009-01-22T00:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19077",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I still see these pop up sporadically, and I can't reproduce it reliably.  Initial ticket said "mark as invalid by June 1, 2008", which is long past.  Thoughts?



---

archive/issue_comments_019078.json:
```json
{
    "body": "Has anyone had this problem recently?",
    "created_at": "2009-11-15T17:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19078",
    "user": "https://github.com/TimDumol"
}
```

Has anyone had this problem recently?



---

archive/issue_comments_019079.json:
```json
{
    "body": "No, and using rpy2 instead doesn't produce it.  Moreover, I completely rewrote from scratch the pexpect interfaces to use a much better way of synchronizing IO.  The crap mentioned in this ticket was from the old way of synchronizing IO.   So I'm closing this as fixed.",
    "created_at": "2009-11-18T09:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19079",
    "user": "https://github.com/williamstein"
}
```

No, and using rpy2 instead doesn't produce it.  Moreover, I completely rewrote from scratch the pexpect interfaces to use a much better way of synchronizing IO.  The crap mentioned in this ticket was from the old way of synchronizing IO.   So I'm closing this as fixed.



---

archive/issue_comments_019080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-18T09:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2783#issuecomment-19080",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
