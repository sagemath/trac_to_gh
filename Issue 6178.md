# Issue 6178: Hermite normal form over PID's

archive/issues_006178.json:
```json
{
    "body": "Assignee: was\n\nCC:  was ncalexan\n\nKeywords: echelon form\n\nI've written some code that calculates Hermite normal form over a general PID. I wrote this because I needed it for a particular application; I will now go ahead with that as a means of stress-testing the code I've just written, but this ticket is here to remind me.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6178\n\n",
    "created_at": "2009-06-01T14:18:08Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Hermite normal form over PID's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6178",
    "user": "davidloeffler"
}
```
Assignee: was

CC:  was ncalexan

Keywords: echelon form

I've written some code that calculates Hermite normal form over a general PID. I wrote this because I needed it for a particular application; I will now go ahead with that as a means of stress-testing the code I've just written, but this ticket is here to remind me.

Issue created by migration from https://trac.sagemath.org/ticket/6178





---

archive/issue_comments_049324.json:
```json
{
    "body": "patch against 4.0.1.alpha0",
    "created_at": "2009-06-02T21:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49324",
    "user": "davidloeffler"
}
```

patch against 4.0.1.alpha0



---

archive/issue_comments_049325.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-06-02T21:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49325",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_049326.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-02T21:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49326",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049327.json:
```json
{
    "body": "Attachment [trac_6178.patch](tarball://root/attachments/some-uuid/ticket6178/trac_6178.patch) by davidloeffler created at 2009-06-02 21:50:15\n\nHere's a patch, which adds echelon form (= Hermite normal form) over PID's. I've also added a simple routine for kernel finding over PID's using Smith form (since the algorithm we had before silently assumed that the base ring was a field).\n\nWith this installed, I've done some playing around with free modules over the ring of integers of Q(sqrt(-7)), and it seems to be quite usable. There are unresolved uniqueness issues, because I don't know how to pick a canonical generator for an ideal or a canonical representative for an element modulo an ideal (even in the particular case of number field orders), but I haven't yet found an example where this is a problem :-)\n\nWilliam: I'm CCing you on this, because you seemed interested in the Smith form stuff. In conjunction with your work at #5882 this will mean we can handle all sorts of new kinds of modules.",
    "created_at": "2009-06-02T21:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49327",
    "user": "davidloeffler"
}
```

Attachment [trac_6178.patch](tarball://root/attachments/some-uuid/ticket6178/trac_6178.patch) by davidloeffler created at 2009-06-02 21:50:15

Here's a patch, which adds echelon form (= Hermite normal form) over PID's. I've also added a simple routine for kernel finding over PID's using Smith form (since the algorithm we had before silently assumed that the base ring was a field).

With this installed, I've done some playing around with free modules over the ring of integers of Q(sqrt(-7)), and it seems to be quite usable. There are unresolved uniqueness issues, because I don't know how to pick a canonical generator for an ideal or a canonical representative for an element modulo an ideal (even in the particular case of number field orders), but I haven't yet found an example where this is a problem :-)

William: I'm CCing you on this, because you seemed interested in the Smith form stuff. In conjunction with your work at #5882 this will mean we can handle all sorts of new kinds of modules.



---

archive/issue_comments_049328.json:
```json
{
    "body": "First a remark:  using #6044 (which as of writing has a positive review but has not been closed yet) solves the issue of non-canonical representatives modulo ideals.\n\n1. Applies fine to 4.0.1 and builds ok.\n2. Tests in sage/rings.number_field pass\n3. Tests in sage/modules pass\n4. tests in sage/matrix pass\n5. I tried some examples and they worked fine.\n\nOn the last point it is not much use trying to create random matrices over a number field order OK, since OK.random_element() returns a random integer!  I think that should be changed.",
    "created_at": "2009-06-11T10:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49328",
    "user": "cremona"
}
```

First a remark:  using #6044 (which as of writing has a positive review but has not been closed yet) solves the issue of non-canonical representatives modulo ideals.

1. Applies fine to 4.0.1 and builds ok.
2. Tests in sage/rings.number_field pass
3. Tests in sage/modules pass
4. tests in sage/matrix pass
5. I tried some examples and they worked fine.

On the last point it is not much use trying to create random matrices over a number field order OK, since OK.random_element() returns a random integer!  I think that should be changed.



---

archive/issue_comments_049329.json:
```json
{
    "body": "> On the last point it is not much use trying to create \n> random matrices over a number field order OK, since OK.random_element() \n> returns a random integer! I think that should be changed. \n\nThat's the second complaint I've heard about this missing functionality just this week!\nDefinitely this should get implemented.",
    "created_at": "2009-06-13T09:16:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49329",
    "user": "was"
}
```

> On the last point it is not much use trying to create 
> random matrices over a number field order OK, since OK.random_element() 
> returns a random integer! I think that should be changed. 

That's the second complaint I've heard about this missing functionality just this week!
Definitely this should get implemented.



---

archive/issue_comments_049330.json:
```json
{
    "body": "I've opened a ticket (#6273).",
    "created_at": "2009-06-13T10:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49330",
    "user": "davidloeffler"
}
```

I've opened a ticket (#6273).



---

archive/issue_comments_049331.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T19:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49331",
    "user": "ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_049332.json:
```json
{
    "body": "In case anybody looks at this ticket, and is concerned about speed... I just compared a random 4x4 example over the integers of a quadratic field and it took 3/10 of a second.  In comparison, the code wrapped at #13509 was 1000 times faster.  So watch out.",
    "created_at": "2014-08-26T13:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6178#issuecomment-49332",
    "user": "was"
}
```

In case anybody looks at this ticket, and is concerned about speed... I just compared a random 4x4 example over the integers of a quadratic field and it took 3/10 of a second.  In comparison, the code wrapped at #13509 was 1000 times faster.  So watch out.
