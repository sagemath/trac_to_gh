# Issue 2341: vector subs over symbolic does not work

archive/issues_002341.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\n\n```\nRicardo Massaro to sage-devel\n\t\nshow details 8:28 PM (18 minutes ago)\n\t\n\t\nReply\n\t\n\t\n\nHello all,\n\nFirst of all, I'd like to thank you for Sage, it's really helping me a\nlot.\n\nI found a strange behavior that i *think* it's a bug, but I'm not\nsure, since I'm a completely newbie to Sage and Python:\n\nsage: a = var('a')\nsage: m = matrix(SR, 2, [a,a,a,a])\nsage: v = vector(SR, 2, [a,a])\n\nThen,\n\nsage: m.subs(a=1)\n[1 1]\n[1 1]\n\nbut\n\nsage: v.subs(a=1)\n(a, a)\n\nI *think* the problem is in the Element.subs() method in devel/sage/\nsage/structure/element.pyx. It seems to assume that the generators are\nsymbols, which is not true in the example vector.\n\nAm I missing something, or is it really a bug?\n\nHere's a dirty fix that apparently fixes this problem, but will likely\nbeak something else:\n\n   def subs(self, in_dict=None, **kwds):\n       v = [a.subs(in_dict, **kwds) for a in self.list()]\n       return self.parent()(v)\n\nThanks,\nRicardo\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2341\n\n",
    "created_at": "2008-02-28T04:51:09Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "vector subs over symbolic does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2341",
    "user": "was"
}
```
Assignee: was

CC:  jason


```
Ricardo Massaro to sage-devel
	
show details 8:28 PM (18 minutes ago)
	
	
Reply
	
	

Hello all,

First of all, I'd like to thank you for Sage, it's really helping me a
lot.

I found a strange behavior that i *think* it's a bug, but I'm not
sure, since I'm a completely newbie to Sage and Python:

sage: a = var('a')
sage: m = matrix(SR, 2, [a,a,a,a])
sage: v = vector(SR, 2, [a,a])

Then,

sage: m.subs(a=1)
[1 1]
[1 1]

but

sage: v.subs(a=1)
(a, a)

I *think* the problem is in the Element.subs() method in devel/sage/
sage/structure/element.pyx. It seems to assume that the generators are
symbols, which is not true in the example vector.

Am I missing something, or is it really a bug?

Here's a dirty fix that apparently fixes this problem, but will likely
beak something else:

   def subs(self, in_dict=None, **kwds):
       v = [a.subs(in_dict, **kwds) for a in self.list()]
       return self.parent()(v)

Thanks,
Ricardo
```


Issue created by migration from https://trac.sagemath.org/ticket/2341





---

archive/issue_comments_015672.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-10T04:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15672",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015673.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-04-10T04:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15673",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_015674.json:
```json
{
    "body": "Fixed in symbolics rewrite.",
    "created_at": "2008-05-21T16:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15674",
    "user": "gfurnish"
}
```

Fixed in symbolics rewrite.



---

archive/issue_comments_015675.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-06-04T21:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15675",
    "user": "mhansen"
}
```

Changing status from assigned to new.



---

archive/issue_comments_015676.json:
```json
{
    "body": "Changing assignee from gfurnish to mhansen.",
    "created_at": "2009-06-04T21:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15676",
    "user": "mhansen"
}
```

Changing assignee from gfurnish to mhansen.



---

archive/issue_comments_015677.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T21:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15677",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015678.json:
```json
{
    "body": "Based on 4.1.2.alpha4",
    "created_at": "2009-09-29T17:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15678",
    "user": "kcrisman"
}
```

Based on 4.1.2.alpha4



---

archive/issue_comments_015679.json:
```json
{
    "body": "Attachment [trac_2341-vector-subs.patch](tarball://root/attachments/some-uuid/ticket2341/trac_2341-vector-subs.patch) by kcrisman created at 2009-09-29 17:30:46\n\nThis patch should fix the issue - long overdue!  The fix is to do exactly as the OP suggests, but only in the free module elements - which is precisely what is already done for matrices as well.",
    "created_at": "2009-09-29T17:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15679",
    "user": "kcrisman"
}
```

Attachment [trac_2341-vector-subs.patch](tarball://root/attachments/some-uuid/ticket2341/trac_2341-vector-subs.patch) by kcrisman created at 2009-09-29 17:30:46

This patch should fix the issue - long overdue!  The fix is to do exactly as the OP suggests, but only in the free module elements - which is precisely what is already done for matrices as well.



---

archive/issue_comments_015680.json:
```json
{
    "body": "Nice!  Thanks for taking care of this.\n\ndoctests pass on the free_module_element.pyx file.",
    "created_at": "2009-09-29T20:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15680",
    "user": "jason"
}
```

Nice!  Thanks for taking care of this.

doctests pass on the free_module_element.pyx file.



---

archive/issue_comments_015681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T05:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2341#issuecomment-15681",
    "user": "mhansen"
}
```

Resolution: fixed
