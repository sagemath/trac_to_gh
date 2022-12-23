# Issue 9191: Running pyx files from the command line doesn't work anymore

archive/issues_009191.json:
```json
{
    "body": "Assignee: jason\n\nCreate a file like this:\n\n```\nflat:tmp wstein$ cat a.spyx\nprint \"hello\"\n```\n\n\nWe have:\n\n```\nflat:tmp wstein$ sage a.spyx\nTraceback (most recent call last):\n  File \"/Users/wstein/sage/build/sage/local/bin/sage-sagex\", line 5, in <module>\n    from sage.misc.interpreter import load_sagex\nImportError: cannot import name load_sagex\n```\n\n\nNote that .pyx files work fine:\n\n\n```\nflat:x wstein$ cp a.spyx a.pyx\nflat:x wstein$ sage a.pyx\nhello\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9191\n\n",
    "created_at": "2010-06-09T02:02:52Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Running pyx files from the command line doesn't work anymore",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9191",
    "user": "was"
}
```
Assignee: jason

Create a file like this:

```
flat:tmp wstein$ cat a.spyx
print "hello"
```


We have:

```
flat:tmp wstein$ sage a.spyx
Traceback (most recent call last):
  File "/Users/wstein/sage/build/sage/local/bin/sage-sagex", line 5, in <module>
    from sage.misc.interpreter import load_sagex
ImportError: cannot import name load_sagex
```


Note that .pyx files work fine:


```
flat:x wstein$ cp a.spyx a.pyx
flat:x wstein$ sage a.pyx
hello
```


Issue created by migration from https://trac.sagemath.org/ticket/9191





---

archive/issue_comments_085993.json:
```json
{
    "body": "Well, no surprise!\n\n```\nsage: sage.misc.interpreter.loa[tab]\nsage.misc.interpreter.load_a_file\nsage.misc.interpreter.load_cython\nsage.misc.interpreter.load_startup_file\nsage.misc.interpreter.load_wrap\n```\n\nThis is a very easy fix, as it turns out.  I haven't got a clue how to doctest it, though.",
    "created_at": "2012-09-25T19:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-85993",
    "user": "kcrisman"
}
```

Well, no surprise!

```
sage: sage.misc.interpreter.loa[tab]
sage.misc.interpreter.load_a_file
sage.misc.interpreter.load_cython
sage.misc.interpreter.load_startup_file
sage.misc.interpreter.load_wrap
```

This is a very easy fix, as it turns out.  I haven't got a clue how to doctest it, though.



---

archive/issue_comments_085994.json:
```json
{
    "body": "\n```\nGC04855:sage-5.4.beta1-again $ ./sage a.spyx \nCompiling a.spyx...\nhello\n```\n\nIt works.  Needs review.",
    "created_at": "2012-09-25T19:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-85994",
    "user": "kcrisman"
}
```


```
GC04855:sage-5.4.beta1-again $ ./sage a.spyx 
Compiling a.spyx...
hello
```

It works.  Needs review.



---

archive/issue_comments_085995.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-25T20:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-85995",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085996.json:
```json
{
    "body": "Attachment\n\nI expanded on your patch, added a doctest, renamed `sage-sagex` to `sage-run-cython`.",
    "created_at": "2012-09-27T12:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-85996",
    "user": "jdemeyer"
}
```

Attachment

I expanded on your patch, added a doctest, renamed `sage-sagex` to `sage-run-cython`.



---

archive/issue_comments_085997.json:
```json
{
    "body": "Wow, nice work!  Very minor concerns below.\n\n----\n\nI'm a little concerned about why .pyx files worked before anyway.  Did it just make it to the \n\n```\nos.execv(os.path.join(binpath, 'sage-python'), ['sage-python', fn] + opts)\n```\n\nline and `sage -python` (which is all `sage-python` is) just knew what to do with it?  And this is better for some reason for pyx files, right?\n\nAlso, any reason for making the messages print to stderr when they aren't errors?  As well as for changing things to the 'new' print statements?  I guess you did the work so I shouldn't complain :) but it always means I worry about missing some small detail.\n\nFinally, if you're going to add pyx files to those which this command does, you should probably add a testing part to the doctest patch for that as well...",
    "created_at": "2012-09-27T15:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-85997",
    "user": "kcrisman"
}
```

Wow, nice work!  Very minor concerns below.

----

I'm a little concerned about why .pyx files worked before anyway.  Did it just make it to the 

```
os.execv(os.path.join(binpath, 'sage-python'), ['sage-python', fn] + opts)
```

line and `sage -python` (which is all `sage-python` is) just knew what to do with it?  And this is better for some reason for pyx files, right?

Also, any reason for making the messages print to stderr when they aren't errors?  As well as for changing things to the 'new' print statements?  I guess you did the work so I shouldn't complain :) but it always means I worry about missing some small detail.

Finally, if you're going to add pyx files to those which this command does, you should probably add a testing part to the doctest patch for that as well...



---

archive/issue_comments_085998.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> I'm a little concerned about why .pyx files worked before anyway.\nThey worked only because they were treated as plain Python files.  No Cython was involved.  Treating them like `.spyx` files is the logical thing to do.\n\n> Also, any reason for making the messages print to stderr when they aren't errors?\nThese kind of diagnostic messages are often printed to `stderr` in Unix-land.  For example, `gcc -v` will output what it's doing to `stderr`.  This makes it much easier to use the output of the script non-interactively: if I want to run a `.spyx` file in a shell script, I have to manually remove the \"Compiling...\" line if its output to `stdout`.\n\nI'm happy with simply removing the \"Compiling...\" line also.\n\n> As well as for changing things to the 'new' print statements?\nI really dislike the\n\n```\nprint >>file\n```\n\nsyntax in Python 2.  Besides, it doesn't hurt to be more compatible with Python 3.\n\n> Finally, if you're going to add pyx files to those which this command does, you should probably add a testing part to the doctest patch for that as well...\nI'm not sure, because running `.pyx` files from the command line is not documented.  The documentation suggests using `.spyx` files, not `.pyx` files.",
    "created_at": "2012-09-27T16:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-85998",
    "user": "jdemeyer"
}
```

Replying to [comment:6 kcrisman]:
> I'm a little concerned about why .pyx files worked before anyway.
They worked only because they were treated as plain Python files.  No Cython was involved.  Treating them like `.spyx` files is the logical thing to do.

> Also, any reason for making the messages print to stderr when they aren't errors?
These kind of diagnostic messages are often printed to `stderr` in Unix-land.  For example, `gcc -v` will output what it's doing to `stderr`.  This makes it much easier to use the output of the script non-interactively: if I want to run a `.spyx` file in a shell script, I have to manually remove the "Compiling..." line if its output to `stdout`.

I'm happy with simply removing the "Compiling..." line also.

> As well as for changing things to the 'new' print statements?
I really dislike the

```
print >>file
```

syntax in Python 2.  Besides, it doesn't hurt to be more compatible with Python 3.

> Finally, if you're going to add pyx files to those which this command does, you should probably add a testing part to the doctest patch for that as well...
I'm not sure, because running `.pyx` files from the command line is not documented.  The documentation suggests using `.spyx` files, not `.pyx` files.



---

archive/issue_comments_085999.json:
```json
{
    "body": "Okay, that's all good enough for me.  I'll test it sometime later but it all makes sense and looks nice.",
    "created_at": "2012-09-27T16:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-85999",
    "user": "kcrisman"
}
```

Okay, that's all good enough for me.  I'll test it sometime later but it all makes sense and looks nice.



---

archive/issue_comments_086000.json:
```json
{
    "body": "I confirmed that nontrivial .pyx files did fail before - nice catch.\n\nSomewhat ironically, the second patch doesn't apply to Sage 5.4.beta2.  Does this depend on the patch which does or does not remove gcc optional from Sage?",
    "created_at": "2012-09-28T17:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86000",
    "user": "kcrisman"
}
```

I confirmed that nontrivial .pyx files did fail before - nice catch.

Somewhat ironically, the second patch doesn't apply to Sage 5.4.beta2.  Does this depend on the patch which does or does not remove gcc optional from Sage?



---

archive/issue_comments_086001.json:
```json
{
    "body": "In fact, I guess this patch *must* be based on this assumption, given that all the spyx doctest in cmdline.py has no optional gcc!  Modulo that issue, this is fine, so putting positive review and sage-pending.\n\n----\n\nOn a separate issue, I'm now convinced that gcc doctests shouldn't be optional - reporting further at #12446 where at least one of these showed up.",
    "created_at": "2012-09-28T18:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86001",
    "user": "kcrisman"
}
```

In fact, I guess this patch *must* be based on this assumption, given that all the spyx doctest in cmdline.py has no optional gcc!  Modulo that issue, this is fine, so putting positive review and sage-pending.

----

On a separate issue, I'm now convinced that gcc doctests shouldn't be optional - reporting further at #12446 where at least one of these showed up.



---

archive/issue_comments_086002.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-28T18:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86002",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086003.json:
```json
{
    "body": "Or, if #13540 comes in, then I guess we could use the other patch.  I'm putting a probably illegal dependency listing now.",
    "created_at": "2012-09-28T18:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86003",
    "user": "kcrisman"
}
```

Or, if #13540 comes in, then I guess we could use the other patch.  I'm putting a probably illegal dependency listing now.



---

archive/issue_comments_086004.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> Somewhat ironically, the second patch doesn't apply to Sage 5.4.beta2.  Does this depend on the patch which does or does not remove gcc optional from Sage?\nYou're right, I developed it on top of #13533.",
    "created_at": "2012-09-28T20:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86004",
    "user": "jdemeyer"
}
```

Replying to [comment:10 kcrisman]:
> Somewhat ironically, the second patch doesn't apply to Sage 5.4.beta2.  Does this depend on the patch which does or does not remove gcc optional from Sage?
You're right, I developed it on top of #13533.



---

archive/issue_comments_086005.json:
```json
{
    "body": "This will need to be rebased to #13579.",
    "created_at": "2012-10-13T10:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86005",
    "user": "jdemeyer"
}
```

This will need to be rebased to #13579.



---

archive/issue_comments_086006.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-11-06T19:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86006",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_086007.json:
```json
{
    "body": "Rebased to sage-5.4.rc4.  I assume the positive_review still stands.",
    "created_at": "2012-11-06T19:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86007",
    "user": "jdemeyer"
}
```

Rebased to sage-5.4.rc4.  I assume the positive_review still stands.



---

archive/issue_comments_086008.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-11-12T21:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9191#issuecomment-86008",
    "user": "jdemeyer"
}
```

Resolution: fixed
