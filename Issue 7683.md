# Issue 7683: sphinx reference manual documentation has a *major* issues: in some cases the input parameters to functions are completely omitted causing great confusion!

archive/issues_007683.json:
```json
{
    "body": "Assignee: mvngu\n\nSee\n\nhttp://sagemath.org/doc/reference/sage/rings/integer.html#sage.rings.integer.Integer.jacobi\n\nNotice that the input parameter b is simply totally omitted from the function signature. In sharp contrast, if you type\n\n```\nsage: a = 5\nsage: a.jacobi(<tab>\n```\n\nin the notebook, then you'll see the correct sphinx-rendered documentation *with* the other input argument.  This is very bad and confusing for some users who trust reference manuals, especially because evidently the use of INPUT/OUTPUT blocks to describe parameters of functions is not being used nearly as much as it should be (there will be another ticket about that).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7683\n\n",
    "created_at": "2009-12-15T02:01:17Z",
    "labels": [
        "component: documentation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "sphinx reference manual documentation has a *major* issues: in some cases the input parameters to functions are completely omitted causing great confusion!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7683",
    "user": "https://github.com/williamstein"
}
```
Assignee: mvngu

See

http://sagemath.org/doc/reference/sage/rings/integer.html#sage.rings.integer.Integer.jacobi

Notice that the input parameter b is simply totally omitted from the function signature. In sharp contrast, if you type

```
sage: a = 5
sage: a.jacobi(<tab>
```

in the notebook, then you'll see the correct sphinx-rendered documentation *with* the other input argument.  This is very bad and confusing for some users who trust reference manuals, especially because evidently the use of INPUT/OUTPUT blocks to describe parameters of functions is not being used nearly as much as it should be (there will be another ticket about that).



Issue created by migration from https://trac.sagemath.org/ticket/7683





---

archive/issue_comments_065820.json:
```json
{
    "body": "Is this only with .pyx files, or are there problems with .py files, too?  A random search through a few files suggests that it's only .pyx files (and perhaps all .pyx files) which cause problems.  I don't know what this means, but maybe someone can figure it out.",
    "created_at": "2009-12-15T02:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65820",
    "user": "https://github.com/jhpalmieri"
}
```

Is this only with .pyx files, or are there problems with .py files, too?  A random search through a few files suggests that it's only .pyx files (and perhaps all .pyx files) which cause problems.  I don't know what this means, but maybe someone can figure it out.



---

archive/issue_comments_065821.json:
```json
{
    "body": "The problem is that Sphinx needs to use the functions in sage.misc.sageinspect to get the function signature as inspect.getargspec doesn't work with Cython modules.",
    "created_at": "2009-12-15T03:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65821",
    "user": "https://github.com/mwhansen"
}
```

The problem is that Sphinx needs to use the functions in sage.misc.sageinspect to get the function signature as inspect.getargspec doesn't work with Cython modules.



---

archive/issue_comments_065822.json:
```json
{
    "body": "Attachment [trac_7683.patch](tarball://root/attachments/some-uuid/ticket7683/trac_7683.patch) by @mwhansen created at 2009-12-15 10:06:02",
    "created_at": "2009-12-15T10:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65822",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7683.patch](tarball://root/attachments/some-uuid/ticket7683/trac_7683.patch) by @mwhansen created at 2009-12-15 10:06:02



---

archive/issue_comments_065823.json:
```json
{
    "body": "Attachment [sphinx-0.6.3.p3.patch](tarball://root/attachments/some-uuid/ticket7683/sphinx-0.6.3.p3.patch) by @mwhansen created at 2009-12-15 10:06:59",
    "created_at": "2009-12-15T10:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65823",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sphinx-0.6.3.p3.patch](tarball://root/attachments/some-uuid/ticket7683/sphinx-0.6.3.p3.patch) by @mwhansen created at 2009-12-15 10:06:59



---

archive/issue_comments_065824.json:
```json
{
    "body": "I've attached a patch for the Sage library which uses the new spkg at http://sage.math.washington.edu/home/mhansen/sphinx-0.6.3.p3.spkg .  The changes in this spkg are at sphinx-0.6.3.p3.patch .",
    "created_at": "2009-12-15T10:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65824",
    "user": "https://github.com/mwhansen"
}
```

I've attached a patch for the Sage library which uses the new spkg at http://sage.math.washington.edu/home/mhansen/sphinx-0.6.3.p3.spkg .  The changes in this spkg are at sphinx-0.6.3.p3.patch .



---

archive/issue_comments_065825.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-15T10:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65825",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065826.json:
```json
{
    "body": "It looks good to me, and I understand the general principle behind the patch, but not necessarily the details.  (For instance, and this has more to do with Sphinx than the patch, why is essentially the same code repeated four times?)\n\nThe output seems to fix the complaint, too.  Is this worth reporting to the Sphinx people as a suggested addition to their code?",
    "created_at": "2009-12-15T17:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65826",
    "user": "https://github.com/jhpalmieri"
}
```

It looks good to me, and I understand the general principle behind the patch, but not necessarily the details.  (For instance, and this has more to do with Sphinx than the patch, why is essentially the same code repeated four times?)

The output seems to fix the complaint, too.  Is this worth reporting to the Sphinx people as a suggested addition to their code?



---

archive/issue_comments_065827.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-15T17:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65827",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065828.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> It looks good to me, and I understand the general principle behind the patch, but not necessarily the details.  (For instance, and this has more to do with Sphinx than the patch, why is essentially the same code repeated four times?)\n\n(Well, twice, not four times, but still.)",
    "created_at": "2009-12-15T17:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65828",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:5 jhpalmieri]:
> It looks good to me, and I understand the general principle behind the patch, but not necessarily the details.  (For instance, and this has more to do with Sphinx than the patch, why is essentially the same code repeated four times?)

(Well, twice, not four times, but still.)



---

archive/issue_comments_065829.json:
```json
{
    "body": "One place is for methods and the other is for functions.  \n\nI sent Georg a message about it, but I haven't heard back from him.  I'll try to push this upstream",
    "created_at": "2009-12-15T17:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65829",
    "user": "https://github.com/mwhansen"
}
```

One place is for methods and the other is for functions.  

I sent Georg a message about it, but I haven't heard back from him.  I'll try to push this upstream



---

archive/issue_comments_065830.json:
```json
{
    "body": "I also give this a positive review.  I tested the code and also read it, and it makes sense to me and works.",
    "created_at": "2009-12-15T18:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65830",
    "user": "https://github.com/williamstein"
}
```

I also give this a positive review.  I tested the code and also read it, and it makes sense to me and works.



---

archive/issue_events_007900.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-16T02:23:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7683#event-7900"
}
```



---

archive/issue_comments_065831.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-16T02:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7683#issuecomment-65831",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
