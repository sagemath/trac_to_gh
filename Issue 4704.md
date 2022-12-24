# Issue 4704: Use jquery to make the javascript code nicer

archive/issues_004704.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  boothby tclemans robertwb\n\nThis ticket splits off part of #4267.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4704\n\n",
    "created_at": "2008-12-05T01:11:07Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Use jquery to make the javascript code nicer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4704",
    "user": "jason"
}
```
Assignee: boothby

CC:  boothby tclemans robertwb

This ticket splits off part of #4267.



Issue created by migration from https://trac.sagemath.org/ticket/4704





---

archive/issue_comments_035435.json:
```json
{
    "body": "Attachment [jquery-javascript-cleanup.patch](tarball://root/attachments/some-uuid/ticket4704/jquery-javascript-cleanup.patch) by jason created at 2008-12-05 01:11:54\n\nThis depends on the patch at #4700.",
    "created_at": "2008-12-05T01:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35435",
    "user": "jason"
}
```

Attachment [jquery-javascript-cleanup.patch](tarball://root/attachments/some-uuid/ticket4704/jquery-javascript-cleanup.patch) by jason created at 2008-12-05 01:11:54

This depends on the patch at #4700.



---

archive/issue_comments_035436.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2008-12-05T01:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35436",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_035437.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-05T01:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35437",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035438.json:
```json
{
    "body": "Ignore the dependency on #4700.  Instead, this depends on #3767.",
    "created_at": "2008-12-05T10:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35438",
    "user": "jason"
}
```

Ignore the dependency on #4700.  Instead, this depends on #3767.



---

archive/issue_comments_035439.json:
```json
{
    "body": "This definitely needs to be commented on by Tom Boothby, since this patch simply deletes the entire optimized-for-us javascript AJAX \"framework\" he wrote, and replaces it by jQuery's.  Is jQuery's actually better?",
    "created_at": "2008-12-06T23:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35439",
    "user": "was"
}
```

This definitely needs to be commented on by Tom Boothby, since this patch simply deletes the entire optimized-for-us javascript AJAX "framework" he wrote, and replaces it by jQuery's.  Is jQuery's actually better?



---

archive/issue_comments_035440.json:
```json
{
    "body": "Yep, I agree.  CCing boothby.",
    "created_at": "2008-12-06T23:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35440",
    "user": "jason"
}
```

Yep, I agree.  CCing boothby.



---

archive/issue_comments_035441.json:
```json
{
    "body": "I'm not sure I see the point of this.  I'm inclined to say, \"If it ain't broke, don't fix it.\"  One might accuse me of being biased... but I really don't think I am here -- I'd be happy to see my code go if it made the rest of the notebook code significantly better.\n\nThere's one benefit that I see: \n\n```\n'newcell=0' + '&id=' + id + '&input='+escape0('%__sage_interact__\\n' + input))\n```\n\n\nbecomes\n\n\n```\n{newcell: 0, id: id, input: '%__sage_interact__\\n' + input}\n```\n\n\nand this is more readable (I'm hoping that the escape0 functionality is preserved).  I'd like to see what was, bradshaw, and tclemans say about this.  I'll test after finals are over.",
    "created_at": "2008-12-07T06:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35441",
    "user": "boothby"
}
```

I'm not sure I see the point of this.  I'm inclined to say, "If it ain't broke, don't fix it."  One might accuse me of being biased... but I really don't think I am here -- I'd be happy to see my code go if it made the rest of the notebook code significantly better.

There's one benefit that I see: 

```
'newcell=0' + '&id=' + id + '&input='+escape0('%__sage_interact__\n' + input))
```


becomes


```
{newcell: 0, id: id, input: '%__sage_interact__\n' + input}
```


and this is more readable (I'm hoping that the escape0 functionality is preserved).  I'd like to see what was, bradshaw, and tclemans say about this.  I'll test after finals are over.



---

archive/issue_comments_035442.json:
```json
{
    "body": "I like the cleaner syntax.  The other thing that may be nice about jquery is that it offloads maintaining to a third party that presumably has more time to focus on it.  That may be a non-issue for our code right now, though.",
    "created_at": "2008-12-09T09:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35442",
    "user": "jason"
}
```

I like the cleaner syntax.  The other thing that may be nice about jquery is that it offloads maintaining to a third party that presumably has more time to focus on it.  That may be a non-issue for our code right now, though.



---

archive/issue_comments_035443.json:
```json
{
    "body": "If there isn't any behavior or performance degradation, I think cleaner syntax is worth having, especially if it makes it easier for more people to work on the notebook code. Also, assuming that jquery can do all we need it to, the more we can offload javascript ajax and browser compatibility code to a larger community the more time we can focus on writing interesting stuff.",
    "created_at": "2008-12-10T02:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35443",
    "user": "robertwb"
}
```

If there isn't any behavior or performance degradation, I think cleaner syntax is worth having, especially if it makes it easier for more people to work on the notebook code. Also, assuming that jquery can do all we need it to, the more we can offload javascript ajax and browser compatibility code to a larger community the more time we can focus on writing interesting stuff.



---

archive/issue_comments_035444.json:
```json
{
    "body": "boothby: could you test this patch now that finals are over?",
    "created_at": "2008-12-20T21:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35444",
    "user": "jason"
}
```

boothby: could you test this patch now that finals are over?



---

archive/issue_comments_035445.json:
```json
{
    "body": "boothby: I should mention that everything is automatically escaped, so the escape0 functionality is preserved, but is way more transparent to the user.",
    "created_at": "2008-12-20T21:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35445",
    "user": "jason"
}
```

boothby: I should mention that everything is automatically escaped, so the escape0 functionality is preserved, but is way more transparent to the user.



---

archive/issue_comments_035446.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-12-20T21:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35446",
    "user": "TimothyClemans"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_035447.json:
```json
{
    "body": "Jason asked me to comment. I don't know Javascript, but I like the idea of outsourcing to an actively developed library.",
    "created_at": "2008-12-20T21:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35447",
    "user": "TimothyClemans"
}
```

Jason asked me to comment. I don't know Javascript, but I like the idea of outsourcing to an actively developed library.



---

archive/issue_comments_035448.json:
```json
{
    "body": "Positive review due to #4705. Jason commented that Tom gave his thumbs up to this patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T06:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35448",
    "user": "mabshoff"
}
```

Positive review due to #4705. Jason commented that Tom gave his thumbs up to this patch.

Cheers,

Michael



---

archive/issue_comments_035449.json:
```json
{
    "body": "Merged jquery-javascript-cleanup.patch in Sage 3.3.alpha0",
    "created_at": "2009-01-19T08:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35449",
    "user": "mabshoff"
}
```

Merged jquery-javascript-cleanup.patch in Sage 3.3.alpha0



---

archive/issue_comments_035450.json:
```json
{
    "body": "Merged jquery-javascript-cleanup.patch in Sage 3.3.alpha0. Oops :)",
    "created_at": "2009-01-19T08:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35450",
    "user": "mabshoff"
}
```

Merged jquery-javascript-cleanup.patch in Sage 3.3.alpha0. Oops :)



---

archive/issue_comments_035451.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T08:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35451",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035452.json:
```json
{
    "body": "When did I comment that Tom gave his thumbs up?  I don't remember that.",
    "created_at": "2009-01-19T13:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35452",
    "user": "jason"
}
```

When did I comment that Tom gave his thumbs up?  I don't remember that.



---

archive/issue_comments_035453.json:
```json
{
    "body": "Replying to [comment:17 jason]:\n> When did I comment that Tom gave his thumbs up?  I don't remember that.\n\nIt come up in IRC, but I am no longer 100% sure it was you who told me or of it was Tom directly. Either way, the code is in and while it might have slipped in somewhat below standards SD 12 will see some pounding of the new code, so things should turn out ok :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T14:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4704#issuecomment-35453",
    "user": "mabshoff"
}
```

Replying to [comment:17 jason]:
> When did I comment that Tom gave his thumbs up?  I don't remember that.

It come up in IRC, but I am no longer 100% sure it was you who told me or of it was Tom directly. Either way, the code is in and while it might have slipped in somewhat below standards SD 12 will see some pounding of the new code, so things should turn out ok :)

Cheers,

Michael
