# Issue 5232: [with patch; needs review] interact -- major bug in interact ranges due to str versus repr

archive/issues_005232.json:
```json
{
    "body": "Assignee: itolkov\n\nThis is related a little to #5220, but tangentially.\n\nIn sage-3.3.alphpha5 the following is now COMPLETELY BROKEN:\n\n```\n@interact\ndef f(s=(0,pi,1)):\n    print s\n```\n\n\nBasically anything involving symbolics in ranges is broken. If you try this in the console you'll see the reason:\n\n\n```\nsage: @interact\n....: def f(s=(0,pi,1)):\n....:         print s\n....: \n<html><!--notruncate--><div padding=6 id='div-interact-0'> <table width=800px height=20px bgcolor='#c5c5c5'\n                 cellpadding=15><tr><td bgcolor='#f9f9f9' valign=top align=left><table><tr><td align=right><font color=\"black\">s&nbsp;</font></td><td><table><tr><td>\n    \t<div id='slider-s-0' class='ui-slider ui-slider-3' style='margin:0px;'><span class='ui-slider-handle'></span></div>\n    \t</td><td><font color='black' id='slider-s-0-lbl'></font></td></tr></table><script>(function(){ var values = [\"\n                                       0\",\"\n                                       1\",\"\n                                       2\",\"\n                                       3\",\"pi\"]; setTimeout(function() {\n```\n\n\nNotice that the range values -- 0, 1, 2,3, etc., are symbolic and printed via ascii art. This is thus a similar problem.  It is I think a massive bug -- it causes mysterious hangs in numerous natural situations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5232\n\n",
    "created_at": "2009-02-11T05:43:05Z",
    "labels": [
        "interact",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] interact -- major bug in interact ranges due to str versus repr",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5232",
    "user": "was"
}
```
Assignee: itolkov

This is related a little to #5220, but tangentially.

In sage-3.3.alphpha5 the following is now COMPLETELY BROKEN:

```
@interact
def f(s=(0,pi,1)):
    print s
```


Basically anything involving symbolics in ranges is broken. If you try this in the console you'll see the reason:


```
sage: @interact
....: def f(s=(0,pi,1)):
....:         print s
....: 
<html><!--notruncate--><div padding=6 id='div-interact-0'> <table width=800px height=20px bgcolor='#c5c5c5'
                 cellpadding=15><tr><td bgcolor='#f9f9f9' valign=top align=left><table><tr><td align=right><font color="black">s&nbsp;</font></td><td><table><tr><td>
    	<div id='slider-s-0' class='ui-slider ui-slider-3' style='margin:0px;'><span class='ui-slider-handle'></span></div>
    	</td><td><font color='black' id='slider-s-0-lbl'></font></td></tr></table><script>(function(){ var values = ["
                                       0","
                                       1","
                                       2","
                                       3","pi"]; setTimeout(function() {
```


Notice that the range values -- 0, 1, 2,3, etc., are symbolic and printed via ascii art. This is thus a similar problem.  It is I think a massive bug -- it causes mysterious hangs in numerous natural situations.

Issue created by migration from https://trac.sagemath.org/ticket/5232





---

archive/issue_comments_040098.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-11T05:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5232#issuecomment-40098",
    "user": "was"
}
```

Changing priority from major to critical.



---

archive/issue_comments_040099.json:
```json
{
    "body": "Attachment\n\nLooks good.",
    "created_at": "2009-02-11T05:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5232#issuecomment-40099",
    "user": "mhansen"
}
```

Attachment

Looks good.



---

archive/issue_comments_040100.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T06:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5232#issuecomment-40100",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_comments_040101.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-11T06:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5232#issuecomment-40101",
    "user": "mabshoff"
}
```

Resolution: fixed
