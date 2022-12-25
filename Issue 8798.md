# Issue 8798: Duplicate version of feedback_arc_set and feedback_vertex_set

archive/issues_008798.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  mvngu\n\nHere is the problem :\n\n\n```\n~/sage/sage-doc/sage/graphs$ grep -e \"def.*eedback\" *\ndigraph.py:    def feedback_edge_set(self,value_only=False):\ndigraph.py:    def feedback_vertex_set(self,value_only=False):\ngeneric_graph.py:    def feedback_edge_set(self,value_only=False):\ngeneric_graph.py:    def feedback_vertex_set(self,value_only=False):\n~/sage/sage-doc/sage/graphs$ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8798\n\n",
    "created_at": "2010-04-28T08:08:21Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Duplicate version of feedback_arc_set and feedback_vertex_set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8798",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  mvngu

Here is the problem :


```
~/sage/sage-doc/sage/graphs$ grep -e "def.*eedback" *
digraph.py:    def feedback_edge_set(self,value_only=False):
digraph.py:    def feedback_vertex_set(self,value_only=False):
generic_graph.py:    def feedback_edge_set(self,value_only=False):
generic_graph.py:    def feedback_vertex_set(self,value_only=False):
~/sage/sage-doc/sage/graphs$ 
```


Issue created by migration from https://trac.sagemath.org/ticket/8798





---

archive/issue_comments_080451.json:
```json
{
    "body": "Attachment [trac_8798.patch](tarball://root/attachments/some-uuid/ticket8798/trac_8798.patch) by @nathanncohen created at 2010-04-28 08:12:59",
    "created_at": "2010-04-28T08:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80451",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_8798.patch](tarball://root/attachments/some-uuid/ticket8798/trac_8798.patch) by @nathanncohen created at 2010-04-28 08:12:59



---

archive/issue_comments_080452.json:
```json
{
    "body": "And here is the patch ! This code would not work for undirected graphs anyway :-)\n\nNathann",
    "created_at": "2010-04-28T08:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80452",
    "user": "https://github.com/nathanncohen"
}
```

And here is the patch ! This code would not work for undirected graphs anyway :-)

Nathann



---

archive/issue_comments_080453.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-28T08:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80453",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080454.json:
```json
{
    "body": "Attachment [trac_8798-rebased.patch](tarball://root/attachments/some-uuid/ticket8798/trac_8798-rebased.patch) by mvngu created at 2010-04-28 14:20:31\n\nThe patch [trac_8798.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798.patch) is OK by me. However, it would likely conflict with #8786. So [trac_8798-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798-rebased.patch) is a rebase of [trac_8798.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798.patch) on top of #8786. Someone other than myself needs to check the rebased patch. If it's OK, then the whole ticket is good to go.",
    "created_at": "2010-04-28T14:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80454",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8798-rebased.patch](tarball://root/attachments/some-uuid/ticket8798/trac_8798-rebased.patch) by mvngu created at 2010-04-28 14:20:31

The patch [trac_8798.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798.patch) is OK by me. However, it would likely conflict with #8786. So [trac_8798-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798-rebased.patch) is a rebase of [trac_8798.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798.patch) on top of #8786. Someone other than myself needs to check the rebased patch. If it's OK, then the whole ticket is good to go.



---

archive/issue_comments_080455.json:
```json
{
    "body": "Checked ! Thank you for your help ! :-)\n\nNathann",
    "created_at": "2010-04-29T16:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80455",
    "user": "https://github.com/nathanncohen"
}
```

Checked ! Thank you for your help ! :-)

Nathann



---

archive/issue_comments_080456.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-29T16:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80456",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080457.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80457",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_021457.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-08T21:58:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8798#event-21457"
}
```



---

archive/issue_comments_080458.json:
```json
{
    "body": "Merged [trac_8798-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798-rebased.patch).",
    "created_at": "2010-05-08T21:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8798#issuecomment-80458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8798-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8798/trac_8798-rebased.patch).
