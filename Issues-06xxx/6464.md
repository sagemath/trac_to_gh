# Issue 6464: [with patch, positive review] notebook: Unicode in notebook worksheets

archive/issues_006464.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: Unicode, notebook\n\nAt this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e3b8dce14b6375bf) thread, there is a patch to fix a Unicode problem related to typesetting Korean in notebook worksheets. Here's an essential snippet:\n\n```\nSo I find the python code and modify it.\n\nsageroot/devel/sage/sage/server/notebook/cell.py:211\n\n211 : </script>\"\"\"%(self.__id,self.__id,self.__text)\n\n=>\n\n211 : </script>\"\"\"%(self.__id,self.__id,((self.__text).decode\n('utf-8')).encode('ascii', 'xmlcharrefreplace'))\n```\nThis might be related to #6417.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6464\n\n",
    "closed_at": "2009-08-26T21:15:40Z",
    "created_at": "2009-07-05T02:06:05Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] notebook: Unicode in notebook worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: boothby

Keywords: Unicode, notebook

At this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e3b8dce14b6375bf) thread, there is a patch to fix a Unicode problem related to typesetting Korean in notebook worksheets. Here's an essential snippet:

```
So I find the python code and modify it.

sageroot/devel/sage/sage/server/notebook/cell.py:211

211 : </script>"""%(self.__id,self.__id,self.__text)

=>

211 : </script>"""%(self.__id,self.__id,((self.__text).decode
('utf-8')).encode('ascii', 'xmlcharrefreplace'))
```
This might be related to #6417.

Issue created by migration from https://trac.sagemath.org/ticket/6464





---

archive/issue_comments_052136.json:
```json
{
    "body": "The ticket 6562 is nearly the same. I wrote that, because I didn't know about this ticket. I suggest that we should use this solution.",
    "created_at": "2009-07-25T01:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52136",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

The ticket 6562 is nearly the same. I wrote that, because I didn't know about this ticket. I suggest that we should use this solution.



---

archive/issue_events_015253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mora",
    "created_at": "2009-07-25T01:23:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "milestone": "sage-4.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6464#event-15253"
}
```



---

archive/issue_comments_052137.json:
```json
{
    "body": "I suggest that we should apply this patch.",
    "created_at": "2009-08-05T22:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52137",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

I suggest that we should apply this patch.



---

archive/issue_comments_052138.json:
```json
{
    "body": "Replying to [comment:3 mora]:\n> I suggest that we should apply this patch.\n\nI don't see any patch file attached to this ticket.",
    "created_at": "2009-08-07T00:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52138",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 mora]:
> I suggest that we should apply this patch.

I don't see any patch file attached to this ticket.



---

archive/issue_comments_052139.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n> Replying to [comment:3 mora]:\n> > I suggest that we should apply this patch.\n\n> I don't see any patch file attached to this ticket.\nIn the description mvngu suggested a little modofication of the file cell.py. I will make a patch as soon as I arrive home.",
    "created_at": "2009-08-07T12:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52139",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

Replying to [comment:4 mvngu]:
> Replying to [comment:3 mora]:
> > I suggest that we should apply this patch.

> I don't see any patch file attached to this ticket.
In the description mvngu suggested a little modofication of the file cell.py. I will make a patch as soon as I arrive home.



---

archive/issue_comments_052140.json:
```json
{
    "body": "Unicode in notebook worksheets, the modification was made by mvngu.",
    "created_at": "2009-08-08T12:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52140",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

Unicode in notebook worksheets, the modification was made by mvngu.



---

archive/issue_comments_052141.json:
```json
{
    "body": "Attachment [12659.patch](tarball://root/attachments/some-uuid/ticket6464/12659.patch) by mora created at 2009-08-08 12:48:43",
    "created_at": "2009-08-08T12:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

Attachment [12659.patch](tarball://root/attachments/some-uuid/ticket6464/12659.patch) by mora created at 2009-08-08 12:48:43



---

archive/issue_comments_052142.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-08-11T22:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

apply only this patch



---

archive/issue_comments_052143.json:
```json
{
    "body": "Attachment [trac_6464-unicode.patch](tarball://root/attachments/some-uuid/ticket6464/trac_6464-unicode.patch) by mvngu created at 2009-08-11 22:23:25\n\nThe patch `trac_6464-unicode.patch` gives proper credit to NoSyu, the person who proposed the fix. Only this patch should be applied.",
    "created_at": "2009-08-11T22:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52143",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6464-unicode.patch](tarball://root/attachments/some-uuid/ticket6464/trac_6464-unicode.patch) by mvngu created at 2009-08-11 22:23:25

The patch `trac_6464-unicode.patch` gives proper credit to NoSyu, the person who proposed the fix. Only this patch should be applied.



---

archive/issue_comments_052144.json:
```json
{
    "body": "Either of the patches `12659.patch` or `trac_6464-unicode.patch` results in a doctest failure:\n\n```\nsage -t -long devel/sage-main/sage/server/simple/twist.py\n**********************************************************************\nFile \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/devel/sage-main/sage/server/simpl\\\ne/twist.py\", line 95:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s'\\\n % (port, session, urllib.quote(code)))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [\"a.txt\"],\n    \"cell_id\": 3\n    }\n    ___S_A_G_E___\nGot:\n    {\n    \"status\": \"done\",\n    \"files\": [\"a.txt\"],\n    \"cell_id\": 3\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n    ^Ae2\n**********************************************************************\n1 items had failures:\n   1 of  24 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/tmp\\\n/.doctest_twist.py\n         [9.5 s]\n```",
    "created_at": "2009-08-11T22:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52144",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Either of the patches `12659.patch` or `trac_6464-unicode.patch` results in a doctest failure:

```
sage -t -long devel/sage-main/sage/server/simple/twist.py
**********************************************************************
File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/devel/sage-main/sage/server/simpl\
e/twist.py", line 95:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s'\
 % (port, session, urllib.quote(code)))
Expected:
    {
    "status": "done",
    "files": ["a.txt"],
    "cell_id": 3
    }
    ___S_A_G_E___
Got:
    {
    "status": "done",
    "files": ["a.txt"],
    "cell_id": 3
    }
    ___S_A_G_E___
    <BLANKLINE>
    ^Ae2
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/tmp\
/.doctest_twist.py
         [9.5 s]
```



---

archive/issue_comments_052145.json:
```json
{
    "body": "I used the patches on Sage 4.1 and Sage 4.1.1.rc2, but I didn't get any doctest failure. I got:\n\n```\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"      \n         [8.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n```\nI don't know how to help, it works for me.\n\n\n\"The patch trac_6464-unicode.patch gives proper credit to NoSyu, the person who proposed the fix.\" Then it's my mistake, I'm sorry.",
    "created_at": "2009-08-12T11:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52145",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

I used the patches on Sage 4.1 and Sage 4.1.1.rc2, but I didn't get any doctest failure. I got:

```
sage -t -long "devel/sage/sage/server/simple/twist.py"      
         [8.9 s]
 
----------------------------------------------------------------------
All tests passed!
```
I don't know how to help, it works for me.


"The patch trac_6464-unicode.patch gives proper credit to NoSyu, the person who proposed the fix." Then it's my mistake, I'm sorry.



---

archive/issue_comments_052146.json:
```json
{
    "body": "Replying to [comment:10 mora]:\n> I used the patches on Sage 4.1 and Sage 4.1.1.rc2, but I didn't get any doctest failure. I got:\n\n{{{\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"      \n         [8.9 s]\n \n---\nAll tests passed!\n}}}\n> I don't know how to help, it works for me.\nHmmm... that's rather strange. I may have done something wrong.\n\n\n\n> \"The patch trac_6464-unicode.patch gives proper credit to NoSyu, the person who proposed the fix.\" Then it's my mistake, I'm sorry.\n\nNo worries :-)",
    "created_at": "2009-08-12T11:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52146",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:10 mora]:
> I used the patches on Sage 4.1 and Sage 4.1.1.rc2, but I didn't get any doctest failure. I got:

{{{
sage -t -long "devel/sage/sage/server/simple/twist.py"      
         [8.9 s]
 
---
All tests passed!
}}}
> I don't know how to help, it works for me.
Hmmm... that's rather strange. I may have done something wrong.



> "The patch trac_6464-unicode.patch gives proper credit to NoSyu, the person who proposed the fix." Then it's my mistake, I'm sorry.

No worries :-)



---

archive/issue_comments_052147.json:
```json
{
    "body": "Tried this in FF3.5 and Safari 4 on Mac OSX.5 Intel.  Tried, saved, quit, resaved, went from browser to browser several times, and nothing made it break.  Character sets I used include \ud55c\uae00, Cyrillic, \u00fc\u00f6\u00e4, some Chinese characters, Arabic, ... I didn't try all the ones available on my system, but it seems like this solution will work fine.  It's really sort of embarrassing this isn't in yet, to be honest.  \n\nTest for the above file passes when added to 4.1.1, so positive review - maybe mvgnu didn't use a clean tree? Don't forget to close #6562 as well.",
    "created_at": "2009-08-25T20:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52147",
    "user": "https://github.com/kcrisman"
}
```

Tried this in FF3.5 and Safari 4 on Mac OSX.5 Intel.  Tried, saved, quit, resaved, went from browser to browser several times, and nothing made it break.  Character sets I used include 한글, Cyrillic, üöä, some Chinese characters, Arabic, ... I didn't try all the ones available on my system, but it seems like this solution will work fine.  It's really sort of embarrassing this isn't in yet, to be honest.  

Test for the above file passes when added to 4.1.1, so positive review - maybe mvgnu didn't use a clean tree? Don't forget to close #6562 as well.



---

archive/issue_events_015254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-26T21:15:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6464#event-15254"
}
```



---

archive/issue_comments_052148.json:
```json
{
    "body": "Merged `trac_6464-unicode.patch`.",
    "created_at": "2009-08-26T21:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52148",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac_6464-unicode.patch`.



---

archive/issue_comments_052149.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-26T21:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6464#issuecomment-52149",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
