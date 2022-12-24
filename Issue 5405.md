# Issue 5405: [with patch, needs review] create a decorator for adding default keyword arguments to a function

archive/issues_005405.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mhansen jason\n\nThe typical usage of this decorator would be to be applied above a\n:obj:`cached_method` or :obj:`cached_function` decorator so that\nthe correct cached object is returned.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5405\n\n",
    "created_at": "2009-02-28T23:14:31Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] create a decorator for adding default keyword arguments to a function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5405",
    "user": "mhansen"
}
```
Assignee: cwitty

CC:  mhansen jason

The typical usage of this decorator would be to be applied above a
:obj:`cached_method` or :obj:`cached_function` decorator so that
the correct cached object is returned.

Issue created by migration from https://trac.sagemath.org/ticket/5405





---

archive/issue_comments_041765.json:
```json
{
    "body": "Attachment [trac_5405.patch](tarball://root/attachments/some-uuid/ticket5405/trac_5405.patch) by nthiery created at 2009-03-18 08:51:37\n\nHi Mike!\n\nI am not so sure about the name, although I can't propose much better than\ndefault_values, or set_default_values.\n\nCould it be generalized to handle both positional and non positional arguments?\n\nI'd suggest to have the doc by starting with what the thing actually does, followed by the typical usage.\nSpeaking of which: could you add an example of this typical usage? (it was not clear to me).",
    "created_at": "2009-03-18T08:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41765",
    "user": "nthiery"
}
```

Attachment [trac_5405.patch](tarball://root/attachments/some-uuid/ticket5405/trac_5405.patch) by nthiery created at 2009-03-18 08:51:37

Hi Mike!

I am not so sure about the name, although I can't propose much better than
default_values, or set_default_values.

Could it be generalized to handle both positional and non positional arguments?

I'd suggest to have the doc by starting with what the thing actually does, followed by the typical usage.
Speaking of which: could you add an example of this typical usage? (it was not clear to me).



---

archive/issue_comments_041766.json:
```json
{
    "body": "Oops, should have set the subject to needs work. Done.",
    "created_at": "2009-04-13T23:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41766",
    "user": "nthiery"
}
```

Oops, should have set the subject to needs work. Done.



---

archive/issue_comments_041767.json:
```json
{
    "body": "Sorry if I don't get this right, but doesn't functools.partial already fulfill this purpose?",
    "created_at": "2009-10-23T15:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41767",
    "user": "timdumol"
}
```

Sorry if I don't get this right, but doesn't functools.partial already fulfill this purpose?



---

archive/issue_comments_041768.json:
```json
{
    "body": "Do you mean something like this?\n\n\n```\nfrom functools import partial\n\ndef partial_dec(*args, **kwds):\n    def p(f):\n        return partial(f,*args,**kwds)\n    return p\n    \n@partial_dec(b=2)\ndef f(a,b):\n    return 10*a+b\n\nf(4)\n```\n",
    "created_at": "2009-10-23T17:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41768",
    "user": "jason"
}
```

Do you mean something like this?


```
from functools import partial

def partial_dec(*args, **kwds):
    def p(f):
        return partial(f,*args,**kwds)
    return p
    
@partial_dec(b=2)
def f(a,b):
    return 10*a+b

f(4)
```




---

archive/issue_comments_041769.json:
```json
{
    "body": "Actually I meant something like this:\n\n\n```\nfrom functools import partial\n\n@partial(partial, b=4)\ndef f(a,b):\n    return 10*a + b\n\nf(4)\n```\n",
    "created_at": "2009-10-23T21:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41769",
    "user": "timdumol"
}
```

Actually I meant something like this:


```
from functools import partial

@partial(partial, b=4)
def f(a,b):
    return 10*a + b

f(4)
```




---

archive/issue_comments_041770.json:
```json
{
    "body": "Cute.  Very nice!",
    "created_at": "2009-10-23T21:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41770",
    "user": "jason"
}
```

Cute.  Very nice!



---

archive/issue_comments_041771.json:
```json
{
    "body": "So now can you use `@`wraps or something so that g? works correctly below?\n\n\n```\nfrom functools import partial, wraps\n\n@partial(partial, b=4)\ndef g(a,b):\n    \"\"\"Docs\"\"\"\n    return 10*a + b\n\ng?\n```\n",
    "created_at": "2009-10-23T21:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41771",
    "user": "jason"
}
```

So now can you use `@`wraps or something so that g? works correctly below?


```
from functools import partial, wraps

@partial(partial, b=4)
def g(a,b):
    """Docs"""
    return 10*a + b

g?
```




---

archive/issue_comments_041772.json:
```json
{
    "body": "This works, but it certainly isn't obvious:\n\n\n```\n\nfrom functools import partial, wraps\n\n@partial(lambda x: wraps(x)(partial(partial, b = 4))(x))\ndef g(a,b):\n    \"\"\"Docs\"\"\"\n    return 10*a + b\n\nprint(g(5))\n\ng?\n```\n",
    "created_at": "2009-10-23T21:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41772",
    "user": "timdumol"
}
```

This works, but it certainly isn't obvious:


```

from functools import partial, wraps

@partial(lambda x: wraps(x)(partial(partial, b = 4))(x))
def g(a,b):
    """Docs"""
    return 10*a + b

print(g(5))

g?
```




---

archive/issue_comments_041773.json:
```json
{
    "body": "and at that point, I'd say \n\n\n```\n@default_keywords...\ndef g...\n\n```\n\n\nis nicer.  However, one might use partial in the above decorator.  I think our discussion is evidence for the usefulness of the idea on this ticket.",
    "created_at": "2009-10-23T21:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41773",
    "user": "jason"
}
```

and at that point, I'd say 


```
@default_keywords...
def g...

```


is nicer.  However, one might use partial in the above decorator.  I think our discussion is evidence for the usefulness of the idea on this ticket.



---

archive/issue_comments_041774.json:
```json
{
    "body": "Yep. It's certainly much clearer. Using `partial` should deal with the positional and non-positional arguments thing.",
    "created_at": "2009-10-23T22:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41774",
    "user": "timdumol"
}
```

Yep. It's certainly much clearer. Using `partial` should deal with the positional and non-positional arguments thing.



---

archive/issue_comments_041775.json:
```json
{
    "body": "So we've agreed that we should create a `partial` decorator that allows something like:\n\n\n```\nfrom sage.misc.decorators (or wherever) import partial\n\n@partial(*args, **kwds) # Same as calling partial(g, *args, **kwds) and wrapping with @wraps\ndef g(a,b):\n   ...\n\n```\n\n\njust works as expected.",
    "created_at": "2009-10-23T22:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41775",
    "user": "jason"
}
```

So we've agreed that we should create a `partial` decorator that allows something like:


```
from sage.misc.decorators (or wherever) import partial

@partial(*args, **kwds) # Same as calling partial(g, *args, **kwds) and wrapping with @wraps
def g(a,b):
   ...

```


just works as expected.



---

archive/issue_comments_041776.json:
```json
{
    "body": "Perhaps a name of `curry` [1] would be better, since it prevents name collision with functools.partial? Then again, it supersedes functools.partial anyways.\n\n[1] http://en.wikipedia.org/wiki/Currying",
    "created_at": "2009-10-23T22:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41776",
    "user": "timdumol"
}
```

Perhaps a name of `curry` [1] would be better, since it prevents name collision with functools.partial? Then again, it supersedes functools.partial anyways.

[1] http://en.wikipedia.org/wiki/Currying



---

archive/issue_comments_041777.json:
```json
{
    "body": "Thanks much for pointing out functools.partial and functool.wrapper; I have several other use cases for them!\n\nReplying to [comment:14 timdumol]:\n> Perhaps a name of `curry` [1] would be better, since it prevents name collision with functools.partial? Then again, it supersedes functools.partial anyways.\n> \n> [1] http://en.wikipedia.org/wiki/Currying\n\nI prefer partial, since curry does not really encompass the specialization of named arguments.\nIt's really functools.partial, but made into a decorator.",
    "created_at": "2009-10-23T22:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41777",
    "user": "nthiery"
}
```

Thanks much for pointing out functools.partial and functool.wrapper; I have several other use cases for them!

Replying to [comment:14 timdumol]:
> Perhaps a name of `curry` [1] would be better, since it prevents name collision with functools.partial? Then again, it supersedes functools.partial anyways.
> 
> [1] http://en.wikipedia.org/wiki/Currying

I prefer partial, since curry does not really encompass the specialization of named arguments.
It's really functools.partial, but made into a decorator.



---

archive/issue_comments_041778.json:
```json
{
    "body": "> I prefer partial, since curry does not really encompass the specialization of named arguments.\n> It's really functools.partial, but made into a decorator.\n\nFair enough -- but just to clarify, `functools.partial` *is* a decorator, just that it doesn't update the documentation string.",
    "created_at": "2009-10-24T01:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41778",
    "user": "timdumol"
}
```

> I prefer partial, since curry does not really encompass the specialization of named arguments.
> It's really functools.partial, but made into a decorator.

Fair enough -- but just to clarify, `functools.partial` *is* a decorator, just that it doesn't update the documentation string.



---

archive/issue_comments_041779.json:
```json
{
    "body": "Attachment [trac_5405-decorator-partial.patch](tarball://root/attachments/some-uuid/ticket5405/trac_5405-decorator-partial.patch) by timdumol created at 2009-12-05 09:53:26\n\nAdds module `sage.misc.decorators` with content `specialize`.",
    "created_at": "2009-12-05T09:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41779",
    "user": "timdumol"
}
```

Attachment [trac_5405-decorator-partial.patch](tarball://root/attachments/some-uuid/ticket5405/trac_5405-decorator-partial.patch) by timdumol created at 2009-12-05 09:53:26

Adds module `sage.misc.decorators` with content `specialize`.



---

archive/issue_comments_041780.json:
```json
{
    "body": "Nevermind, `functools.partial` is not a decorator. My apologies.\n\nThis patch should do the trick. I named it `specialize` rather than `partial`, since `partial` conflicts with `functools.partial`.",
    "created_at": "2009-12-05T09:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41780",
    "user": "timdumol"
}
```

Nevermind, `functools.partial` is not a decorator. My apologies.

This patch should do the trick. I named it `specialize` rather than `partial`, since `partial` conflicts with `functools.partial`.



---

archive/issue_comments_041781.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-05T09:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41781",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041782.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-05T19:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41782",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_041783.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-05T19:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41783",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041784.json:
```json
{
    "body": "Attachment [trac_5405-decorator-partial.2.patch](tarball://root/attachments/some-uuid/ticket5405/trac_5405-decorator-partial.2.patch) by mvngu created at 2010-05-08 04:06:27\n\nsame as previous but with username",
    "created_at": "2010-05-08T04:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41784",
    "user": "mvngu"
}
```

Attachment [trac_5405-decorator-partial.2.patch](tarball://root/attachments/some-uuid/ticket5405/trac_5405-decorator-partial.2.patch) by mvngu created at 2010-05-08 04:06:27

same as previous but with username



---

archive/issue_comments_041785.json:
```json
{
    "body": "The patch [trac_5405-decorator-partial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5405/trac_5405-decorator-partial.2.patch) is the same as Tim's patch, but with his username.",
    "created_at": "2010-05-08T04:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41785",
    "user": "mvngu"
}
```

The patch [trac_5405-decorator-partial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5405/trac_5405-decorator-partial.2.patch) is the same as Tim's patch, but with his username.



---

archive/issue_comments_041786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41786",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_041787.json:
```json
{
    "body": "Merged [trac_5405-decorator-partial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5405/trac_5405-decorator-partial.2.patch).",
    "created_at": "2010-05-08T22:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5405#issuecomment-41787",
    "user": "mvngu"
}
```

Merged [trac_5405-decorator-partial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5405/trac_5405-decorator-partial.2.patch).
