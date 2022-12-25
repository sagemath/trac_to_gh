# Issue 4440: [with patch, positive work] Automatic Indentation

archive/issues_004440.json:
```json
{
    "body": "Assignee: ahupfer\n\nCC:  @jasongrout\n\nThe patch provides automatic indentation for python after colons and same level identation.\nIt works up to four levels of identation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4440\n\n",
    "closed_at": "2009-02-20T07:24:49Z",
    "created_at": "2008-11-04T19:26:07Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive work] Automatic Indentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4440",
    "user": "https://trac.sagemath.org/admin/accounts/users/ahupfer"
}
```
Assignee: ahupfer

CC:  @jasongrout

The patch provides automatic indentation for python after colons and same level identation.
It works up to four levels of identation.

Issue created by migration from https://trac.sagemath.org/ticket/4440





---

archive/issue_comments_032573.json:
```json
{
    "body": "There is already an attempt to do this at #1684. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-04T20:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is already an attempt to do this at #1684. 

Cheers,

Michael



---

archive/issue_comments_032574.json:
```json
{
    "body": "The restriction to 4 indentation levels is decidedly strange, given that the patch itself has a 6-deep indentation.  This can be written more elegantly:\n\n```\nvar indenting, id, tab;\nindenting = RegExp(\"\\n( *)\",\"g\");\nwhile(indenting.test(text[0])) {\n  id   = indexing.lastIndex;\n  tab  = RegExp.lastMatch.substring(1);\n}\nif( id == second_last_break && second_last_break != -1) {\n    get_cell(id).value = text[0] + tab + text[1]; \n    set_cursor_position(cell, position + tab.length);\n}\n```\n\nThe above code hasn't been tested, but should be a good start.",
    "created_at": "2008-11-05T00:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32574",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

The restriction to 4 indentation levels is decidedly strange, given that the patch itself has a 6-deep indentation.  This can be written more elegantly:

```
var indenting, id, tab;
indenting = RegExp("\n( *)","g");
while(indenting.test(text[0])) {
  id   = indexing.lastIndex;
  tab  = RegExp.lastMatch.substring(1);
}
if( id == second_last_break && second_last_break != -1) {
    get_cell(id).value = text[0] + tab + text[1]; 
    set_cursor_position(cell, position + tab.length);
}
```

The above code hasn't been tested, but should be a good start.



---

archive/issue_comments_032575.json:
```json
{
    "body": "Attachment [identation.patch](tarball://root/attachments/some-uuid/ticket4440/identation.patch) by ahupfer created at 2008-11-21 13:45:46",
    "created_at": "2008-11-21T13:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32575",
    "user": "https://trac.sagemath.org/admin/accounts/users/ahupfer"
}
```

Attachment [identation.patch](tarball://root/attachments/some-uuid/ticket4440/identation.patch) by ahupfer created at 2008-11-21 13:45:46



---

archive/issue_comments_032576.json:
```json
{
    "body": "Improved identation support with unlimited ident. Tested with Firefox, Safari, Chrome.\nWorks not, but doesn't break Internet Explorer and Opera.",
    "created_at": "2008-11-21T13:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32576",
    "user": "https://trac.sagemath.org/admin/accounts/users/ahupfer"
}
```

Improved identation support with unlimited ident. Tested with Firefox, Safari, Chrome.
Works not, but doesn't break Internet Explorer and Opera.



---

archive/issue_comments_032577.json:
```json
{
    "body": "REVIEW\n\nThis is *REALLY* nice and *almost* works.  It has one bug, which is that if you enter a blank line, the auto-indent is off by one.  E.g., I got the following when I entered a blank line after the first print statement:\n\n```\nif True:\n    print \"hi\"\n    \n   print \"mom\"\n```\n\nI should have got either\n\n```\nif True:\n    print \"hi\"\n    \n    print \"mom\"\n```\nor \n\n```\nif True:\n    print \"hi\"\n\nprint \"mom\"\n```\n\nWhich is a design decision.  To be more like the Python/Ipython command line, one would get the latter.  To be more like an IDE, maybe the former.  I don't care which, just that the current behavior (which is neither) is buggy.\n\nThat said, if this bit rots forever that would be bad.  I would almost rather have the buggy patch than no patch at all, since even with the bug it's pretty nice functionality.\n\nIt would however by nice if there were a way to turn it off.  That will have to wait until Timothy Clemans user management features get in.",
    "created_at": "2008-11-27T17:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32577",
    "user": "https://github.com/williamstein"
}
```

REVIEW

This is *REALLY* nice and *almost* works.  It has one bug, which is that if you enter a blank line, the auto-indent is off by one.  E.g., I got the following when I entered a blank line after the first print statement:

```
if True:
    print "hi"
    
   print "mom"
```

I should have got either

```
if True:
    print "hi"
    
    print "mom"
```
or 

```
if True:
    print "hi"

print "mom"
```

Which is a design decision.  To be more like the Python/Ipython command line, one would get the latter.  To be more like an IDE, maybe the former.  I don't care which, just that the current behavior (which is neither) is buggy.

That said, if this bit rots forever that would be bad.  I would almost rather have the buggy patch than no patch at all, since even with the bug it's pretty nice functionality.

It would however by nice if there were a way to turn it off.  That will have to wait until Timothy Clemans user management features get in.



---

archive/issue_comments_032578.json:
```json
{
    "body": "Attachment [4440.2.patch](tarball://root/attachments/some-uuid/ticket4440/4440.2.patch) by boothby created at 2009-01-21 23:56:24",
    "created_at": "2009-01-21T23:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32578",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [4440.2.patch](tarball://root/attachments/some-uuid/ticket4440/4440.2.patch) by boothby created at 2009-01-21 23:56:24



---

archive/issue_comments_032579.json:
```json
{
    "body": "I fixed the bug was reported.  I've tested this in firefox on windows only.  Also, I made the regexp significantly uglier to make it more robust (sadly), and so commented the snot out of it.",
    "created_at": "2009-01-21T23:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32579",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I fixed the bug was reported.  I've tested this in firefox on windows only.  Also, I made the regexp significantly uglier to make it more robust (sadly), and so commented the snot out of it.



---

archive/issue_events_010029.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-01-22T17:21:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4440#event-10029"
}
```



---

archive/issue_comments_032580.json:
```json
{
    "body": "Notes from Tom:\n* Fold the patches into one patch\n* Make the iphone check *after* the resize code",
    "created_at": "2009-01-22T19:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32580",
    "user": "https://github.com/jasongrout"
}
```

Notes from Tom:
* Fold the patches into one patch
* Make the iphone check *after* the resize code



---

archive/issue_comments_032581.json:
```json
{
    "body": "This feature seems to work well.  I can see it being annoying if there happens to be a semi-colon at the end of the line for a language other than python.  For that reason, there should be a way to turn this off.  I think it's probably not going to be a huge problem, though, so I think this ought to go in (after the two fixes above are done), and a feature ticket created to make an option for the user to turn this off.",
    "created_at": "2009-01-22T19:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32581",
    "user": "https://github.com/jasongrout"
}
```

This feature seems to work well.  I can see it being annoying if there happens to be a semi-colon at the end of the line for a language other than python.  For that reason, there should be a way to turn this off.  I think it's probably not going to be a huge problem, though, so I think this ought to go in (after the two fixes above are done), and a feature ticket created to make an option for the user to turn this off.



---

archive/issue_comments_032582.json:
```json
{
    "body": "Positive review pending the above changes in \"Notes from Tom\"",
    "created_at": "2009-01-22T19:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32582",
    "user": "https://github.com/jasongrout"
}
```

Positive review pending the above changes in "Notes from Tom"



---

archive/issue_comments_032583.json:
```json
{
    "body": "Replaces previous two patches",
    "created_at": "2009-01-23T09:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32583",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Replaces previous two patches



---

archive/issue_comments_032584.json:
```json
{
    "body": "Attachment [4440-indentation.patch](tarball://root/attachments/some-uuid/ticket4440/4440-indentation.patch) by boothby created at 2009-01-23 09:29:36",
    "created_at": "2009-01-23T09:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32584",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [4440-indentation.patch](tarball://root/attachments/some-uuid/ticket4440/4440-indentation.patch) by boothby created at 2009-01-23 09:29:36



---

archive/issue_comments_032585.json:
```json
{
    "body": "Very nice.  This addresses wstein's comment above and now does the second option.\n\nPositive review.",
    "created_at": "2009-01-28T17:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32585",
    "user": "https://github.com/jasongrout"
}
```

Very nice.  This addresses wstein's comment above and now does the second option.

Positive review.



---

archive/issue_comments_032586.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T18:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32586",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032587.json:
```json
{
    "body": "Merged 4440-indentation.patch in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T18:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32587",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4440-indentation.patch in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_events_010030.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T18:04:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4440#event-10030"
}
```



---

archive/issue_comments_032588.json:
```json
{
    "body": "This causes a serious bug: #5293.  I vote we remove this patch from 3.3 and work on it.",
    "created_at": "2009-02-17T23:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32588",
    "user": "https://github.com/jasongrout"
}
```

This causes a serious bug: #5293.  I vote we remove this patch from 3.3 and work on it.



---

archive/issue_comments_032589.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-17T23:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32589",
    "user": "https://github.com/jasongrout"
}
```

Changing status from closed to reopened.



---

archive/issue_events_010031.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-02-17T23:03:30Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4440#event-10031"
}
```



---

archive/issue_comments_032590.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-17T23:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32590",
    "user": "https://github.com/jasongrout"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_032591.json:
```json
{
    "body": "mabshoff says that he will revert this patch for now.  I hope that it is fixed and gets back in soon!  It's a great piece of functionality!",
    "created_at": "2009-02-17T23:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32591",
    "user": "https://github.com/jasongrout"
}
```

mabshoff says that he will revert this patch for now.  I hope that it is fixed and gets back in soon!  It's a great piece of functionality!



---

archive/issue_comments_032592.json:
```json
{
    "body": "(to get a positive review, we need to fix the issue at #5293)",
    "created_at": "2009-02-17T23:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32592",
    "user": "https://github.com/jasongrout"
}
```

(to get a positive review, we need to fix the issue at #5293)



---

archive/issue_comments_032593.json:
```json
{
    "body": "Reinstated due to positive review of the fix at #5293.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T06:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32593",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Reinstated due to positive review of the fix at #5293.

Cheers,

Michael



---

archive/issue_comments_032594.json:
```json
{
    "body": "Merged in Sage 3.3.rc3 again :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32594",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc3 again :)

Cheers,

Michael



---

archive/issue_events_010032.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T07:24:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4440#event-10032"
}
```



---

archive/issue_comments_032595.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T07:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4440#issuecomment-32595",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
