# Issue 4693: [with patch, needs review] cleanup work in sage/functions/piecewise.py

archive/issues_004693.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nAfter looking at #4690, I realized that a lot could be done to \"update\" piecewise.py.  This includes not explicitly using Maxima where we don't need to in order to take advantage of pynac in the future.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4693\n\n",
    "created_at": "2008-12-04T10:06:23Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, needs review] cleanup work in sage/functions/piecewise.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4693",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @wdjoyner

After looking at #4690, I realized that a lot could be done to "update" piecewise.py.  This includes not explicitly using Maxima where we don't need to in order to take advantage of pynac in the future.

Issue created by migration from https://trac.sagemath.org/ticket/4693





---

archive/issue_comments_035299.json:
```json
{
    "body": "I'll review this today I hope. I've read through the code. It is mostly a much more elegant rewrite of the code I wrote long ago. Maybe 85% is just using clever Python constructions I should have thought about but didn't for some reason. The rest of it uses the more modern machinery of SR classes which wasn't available when the module was first written. At first read, it looks like a really excellent patch - thanks very much Mike for this (my students and I literally use this every semester).   \nI need to do some testing though and need to read the file itself (and not just the diff) to check for possible docstring problems.",
    "created_at": "2008-12-04T12:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4693#issuecomment-35299",
    "user": "https://github.com/wdjoyner"
}
```

I'll review this today I hope. I've read through the code. It is mostly a much more elegant rewrite of the code I wrote long ago. Maybe 85% is just using clever Python constructions I should have thought about but didn't for some reason. The rest of it uses the more modern machinery of SR classes which wasn't available when the module was first written. At first read, it looks like a really excellent patch - thanks very much Mike for this (my students and I literally use this every semester).   
I need to do some testing though and need to read the file itself (and not just the diff) to check for possible docstring problems.



---

archive/issue_comments_035300.json:
```json
{
    "body": "Thanks David. I can doctest this patch shortly and will then let you know if there are any doctest problems. Also note #4690 which already has a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T12:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4693#issuecomment-35300",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks David. I can doctest this patch shortly and will then let you know if there are any doctest problems. Also note #4690 which already has a positive review.

Cheers,

Michael



---

archive/issue_comments_035301.json:
```json
{
    "body": "Attachment [trac_4693.2.patch](tarball://root/attachments/some-uuid/ticket4693/trac_4693.2.patch) by @wdjoyner created at 2008-12-04 14:35:35\n\nI cannot apply this patch. I've tried various things (adding the 4690 patch first, not adding it, using different Sage releases, ...). As I said, I read through it and it looks very good. I wanted to read through the docstring descriptions to see if they still made sense. (For example, from the diff file, it seemed as though the docstring description for laplace needed a small rewording.) I also was hoping Mike added himself to the AUTHOR list at the top of the file. Since the diff doesn't contain that info and I can't apply the patch, I can't tell. \nStill these are very minor issues that can be taken care of later and should not prevent this from going into Sage. So, I give this a positive review, pending doctesting. Thanks again, Mike!",
    "created_at": "2008-12-04T14:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4693#issuecomment-35301",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4693.2.patch](tarball://root/attachments/some-uuid/ticket4693/trac_4693.2.patch) by @wdjoyner created at 2008-12-04 14:35:35

I cannot apply this patch. I've tried various things (adding the 4690 patch first, not adding it, using different Sage releases, ...). As I said, I read through it and it looks very good. I wanted to read through the docstring descriptions to see if they still made sense. (For example, from the diff file, it seemed as though the docstring description for laplace needed a small rewording.) I also was hoping Mike added himself to the AUTHOR list at the top of the file. Since the diff doesn't contain that info and I can't apply the patch, I can't tell. 
Still these are very minor issues that can be taken care of later and should not prevent this from going into Sage. So, I give this a positive review, pending doctesting. Thanks again, Mike!



---

archive/issue_comments_035302.json:
```json
{
    "body": "This applies without any problem to Sage 3.2.1 and my current 3.2.2.alpha0 merge tree. I am also quite certain that this patch applies against 3.2 since piecewise.py hasn't been touched in a while.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T15:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4693#issuecomment-35302",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This applies without any problem to Sage 3.2.1 and my current 3.2.2.alpha0 merge tree. I am also quite certain that this patch applies against 3.2 since piecewise.py hasn't been touched in a while.

Cheers,

Michael



---

archive/issue_comments_035303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T15:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4693#issuecomment-35303",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035304.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T15:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4693#issuecomment-35304",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_events_004938.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-04T15:36:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4693#event-4938"
}
```



---

archive/issue_comments_035305.json:
```json
{
    "body": "One more thing: I know we added doctests, but the slow down seems larger than it should be:\n\n3.2.1:\n\n```\nsage -t -long \"devel/sage/sage/functions/piecewise.py\"      \n\t [87.8 s]\n```\n \nvs. 3.2.2.alpha0\n\n```\nsage -t -long \"devel/sage/sage/functions/piecewise.py\"      \n\t [145.3 s]\n```\n\nIt might be the cleanup for plotting, but I have not investigated.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T07:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4693#issuecomment-35305",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One more thing: I know we added doctests, but the slow down seems larger than it should be:

3.2.1:

```
sage -t -long "devel/sage/sage/functions/piecewise.py"      
	 [87.8 s]
```
 
vs. 3.2.2.alpha0

```
sage -t -long "devel/sage/sage/functions/piecewise.py"      
	 [145.3 s]
```

It might be the cleanup for plotting, but I have not investigated.

Cheers,

Michael
