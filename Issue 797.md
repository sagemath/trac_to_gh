# Issue 797: timeit doesn't recognize [1..10] syntax

archive/issues_000797.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: %time [1..10]\n------------------------------------------------------------\n   File \"<timed exec>\", line 1\n     [1..10]\n          ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n\nsage: %timeit [1..10]\n------------------------------------------------------------\n   File \"<magic-timeit>\", line 6\n     [1..10]\n          ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n\nsage: %timeit xrange(11)\n1000000 loops, best of 3: 392 ns per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/797\n\n",
    "created_at": "2007-10-03T00:26:36Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "timeit doesn't recognize [1..10] syntax",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/797",
    "user": "@jasongrout"
}
```
Assignee: @williamstein


```
sage: %time [1..10]
------------------------------------------------------------
   File "<timed exec>", line 1
     [1..10]
          ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage: %timeit [1..10]
------------------------------------------------------------
   File "<magic-timeit>", line 6
     [1..10]
          ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage: %timeit xrange(11)
1000000 loops, best of 3: 392 ns per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/797





---

archive/issue_comments_004789.json:
```json
{
    "body": "The workaround now is to use the timeit command, which does send things to the preparser.\n\n\n```\nsage: timeit('[1..10]')\n625 loops, best of 3: 220 \u00b5s per loop\n```\n",
    "created_at": "2009-01-14T08:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4789",
    "user": "@jasongrout"
}
```

The workaround now is to use the timeit command, which does send things to the preparser.


```
sage: timeit('[1..10]')
625 loops, best of 3: 220 µs per loop
```




---

archive/issue_comments_004790.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-01-14T08:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4790",
    "user": "@jasongrout"
}
```

Resolution: wontfix



---

archive/issue_comments_004791.json:
```json
{
    "body": "Just because there is a workaround doesn't mean this should be closed.  I reported this problem to Fernando Perez of Ipython and he \"admitted\" that it is a bug, and was working on fixing it at that last sage days.  I'm re-opening this.\n\nBy the way, it's generally very bad for anybody but me or Michael Abshoff to close tickets on trac!",
    "created_at": "2009-01-14T16:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4791",
    "user": "@williamstein"
}
```

Just because there is a workaround doesn't mean this should be closed.  I reported this problem to Fernando Perez of Ipython and he "admitted" that it is a bug, and was working on fixing it at that last sage days.  I'm re-opening this.

By the way, it's generally very bad for anybody but me or Michael Abshoff to close tickets on trac!



---

archive/issue_comments_004792.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2009-01-14T16:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4792",
    "user": "@williamstein"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_004793.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-01-14T16:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4793",
    "user": "@williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_004794.json:
```json
{
    "body": "I only closed it after mabshoff gave his okay on IRC.  I guess I should have posted the IRC log.",
    "created_at": "2009-01-14T17:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4794",
    "user": "@jasongrout"
}
```

I only closed it after mabshoff gave his okay on IRC.  I guess I should have posted the IRC log.



---

archive/issue_comments_004795.json:
```json
{
    "body": "Replying to [ticket:797 jason]:\n\nHere is some account of what happens in Sage 3.2.3:\n\n\n```\nsage: %time [1..10]\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n```\n\n\nSo, the first problem is not a problem anymore.\n\n```\nsage: %timeit [1..10]\n------------------------------------------------------------\n   File \"<magic-timeit>\", line 6\n     [1..10]\n          ^\nSyntaxError: invalid syntax\n```\n\n\nSo, that is the only remaining issue. I am now looking at `sage/misc/sage_timeit.py`.",
    "created_at": "2009-01-21T19:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4795",
    "user": "@simon-king-jena"
}
```

Replying to [ticket:797 jason]:

Here is some account of what happens in Sage 3.2.3:


```
sage: %time [1..10]
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```


So, the first problem is not a problem anymore.

```
sage: %timeit [1..10]
------------------------------------------------------------
   File "<magic-timeit>", line 6
     [1..10]
          ^
SyntaxError: invalid syntax
```


So, that is the only remaining issue. I am now looking at `sage/misc/sage_timeit.py`.



---

archive/issue_comments_004796.json:
```json
{
    "body": "We can overwrite the default magic commands in IPython:\n\n\n```\nsage: _ip.expose_magic(\"timeit\", lambda self, s: timeit(s))\nsage: %timeit [1..10]\n625 loops, best of 3: 58.4 \u00b5s per loop\n```\n",
    "created_at": "2009-01-21T20:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4796",
    "user": "@mwhansen"
}
```

We can overwrite the default magic commands in IPython:


```
sage: _ip.expose_magic("timeit", lambda self, s: timeit(s))
sage: %timeit [1..10]
625 loops, best of 3: 58.4 µs per loop
```




---

archive/issue_comments_004797.json:
```json
{
    "body": "I somehow got the impression that it is an issue with preparsing, for the following reason:\n\n```\nsage: timeit('[1..10]',preparse=False)\n------------------------------------------------------------\n   File \"<magic-timeit>\", line 6\n     [1..10]\n          ^\nSyntaxError: invalid syntax\n```\n\n\nThis is the same error as in \n\n```\nsage: %timeit [1..10]\n```\n\n\nIn the code, by default preparsing should be done; namely, in `sage_timer.py` it says\n\n```\ndef sage_timeit(stmt, globals, preparse=None, number = 0, repeat = 3, precision = 3):\n...\n    if preparse is None:\n        preparse = interpreter.do_preparse\n```\n\n\nNow, we also have\n\n```\nsage: from sage.misc import interpreter\nsage: interpreter.do_preparse\nTrue\n```\n\n\nSo, it *should* be with preparsing.\n\nFor testing, I inserted a line in the code that prints the value of `preparse`.\n\nThe curious thing is that this line is executed when doing `timeit('[1..10]')` or `timeit.eval('[1..10]')`, but it is *not* executed when doing `%timeit [1..10]`.\n\nI was just told that `%timeit ...` should do the same as `timeit.eval('...')`, but apparently it doesn't. So, perhaps it is a problem with the `%`?\n\nCan you tell me where the behaviour of `%` is defined?",
    "created_at": "2009-01-21T20:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4797",
    "user": "@simon-king-jena"
}
```

I somehow got the impression that it is an issue with preparsing, for the following reason:

```
sage: timeit('[1..10]',preparse=False)
------------------------------------------------------------
   File "<magic-timeit>", line 6
     [1..10]
          ^
SyntaxError: invalid syntax
```


This is the same error as in 

```
sage: %timeit [1..10]
```


In the code, by default preparsing should be done; namely, in `sage_timer.py` it says

```
def sage_timeit(stmt, globals, preparse=None, number = 0, repeat = 3, precision = 3):
...
    if preparse is None:
        preparse = interpreter.do_preparse
```


Now, we also have

```
sage: from sage.misc import interpreter
sage: interpreter.do_preparse
True
```


So, it *should* be with preparsing.

For testing, I inserted a line in the code that prints the value of `preparse`.

The curious thing is that this line is executed when doing `timeit('[1..10]')` or `timeit.eval('[1..10]')`, but it is *not* executed when doing `%timeit [1..10]`.

I was just told that `%timeit ...` should do the same as `timeit.eval('...')`, but apparently it doesn't. So, perhaps it is a problem with the `%`?

Can you tell me where the behaviour of `%` is defined?



---

archive/issue_comments_004798.json:
```json
{
    "body": "Are you doing this in the notebook or the command-line?  They're two totally separate things.\n\nCan you hop on IRC?",
    "created_at": "2009-01-21T20:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4798",
    "user": "@mwhansen"
}
```

Are you doing this in the notebook or the command-line?  They're two totally separate things.

Can you hop on IRC?



---

archive/issue_comments_004799.json:
```json
{
    "body": "When you run %timeit from the command-line, it runs code in IPython and does not touch any code in the Sage library.  The issue is that the IPython magic command \"%timeit\" doesn't do the preparsing.  Fernando was working on an upstream fix for this.  An easy downstream fix for this would be to do as I suggested above and overwrite the IPython version of timeit with our own with the expose_magic function.\n\n\n```\nsage: _ip.expose_magic(\"timeit\", lambda self, s: timeit(s))\nsage: %timeit [1..10]\n625 loops, best of 3: 58.4 \u00b5s per loop\n```\n\n\nThe right place to put this would probably be in local/bin/ipy_profile_sage.py.",
    "created_at": "2009-01-21T21:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4799",
    "user": "@mwhansen"
}
```

When you run %timeit from the command-line, it runs code in IPython and does not touch any code in the Sage library.  The issue is that the IPython magic command "%timeit" doesn't do the preparsing.  Fernando was working on an upstream fix for this.  An easy downstream fix for this would be to do as I suggested above and overwrite the IPython version of timeit with our own with the expose_magic function.


```
sage: _ip.expose_magic("timeit", lambda self, s: timeit(s))
sage: %timeit [1..10]
625 loops, best of 3: 58.4 µs per loop
```


The right place to put this would probably be in local/bin/ipy_profile_sage.py.



---

archive/issue_comments_004800.json:
```json
{
    "body": "Replying to [comment:11 mhansen]:\n> When you run %timeit from the command-line, it runs code in IPython and does not touch any code in the Sage library.  The issue is that the IPython magic command \"%timeit\" doesn't do the preparsing.  Fernando was working on an upstream fix for this.  An easy downstream fix for this would be to do as I suggested above and overwrite the IPython version of timeit with our own with the expose_magic function.\n> \n> {{{\n> sage: _ip.expose_magic(\"timeit\", lambda self, s: timeit(s))\n> sage: %timeit [1..10]\n> 625 loops, best of 3: 58.4 \u00b5s per loop\n> }}}\n> \n> The right place to put this would probably be in local/bin/ipy_profile_sage.py.\n\nThank you!\n\nWhile you replied, I tried to post the following:\n\nReplying to [comment:10 mhansen]:\n> Are you doing this in the notebook or the command-line?  They're two totally separate things.\n\nIt is command-line, and I don't know what happens on the notebook. Can you test it?\n\nIf it is in `preparser_ipython`, then the following might be the source of trouble:\n\n```\ndef preparse_ipython(line, reset=True):\n    global num_lines\n    global q_lines\n\n    L = line.lstrip()\n    if L.startswith('%'):\n        # This should be installed as an Ipython magic command,\n        # but I don't know how yet...\n        L = L[1:].strip()\n        import sage.interfaces.all\n        if L.lower() in sage.interfaces.all.interfaces:\n            switch_interface(L.lower())\n            return \"''\"\n        else:\n            # only preparse non-magic lines\n            return line\n```\n\n\nHence, if the line starts with `%` and if the word after `%` is not the name of an interface than simply the line is returned unchanged. \n\nBut what happens afterwards? In the end of the day, `%timeit` gets an interpretation and does call some `timeit` command!\n\n> Can you hop on IRC?\n\nI try (I never used IRC before). So, if it works, see you soon.\n\nCheers\n Simon",
    "created_at": "2009-01-21T21:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4800",
    "user": "@simon-king-jena"
}
```

Replying to [comment:11 mhansen]:
> When you run %timeit from the command-line, it runs code in IPython and does not touch any code in the Sage library.  The issue is that the IPython magic command "%timeit" doesn't do the preparsing.  Fernando was working on an upstream fix for this.  An easy downstream fix for this would be to do as I suggested above and overwrite the IPython version of timeit with our own with the expose_magic function.
> 
> {{{
> sage: _ip.expose_magic("timeit", lambda self, s: timeit(s))
> sage: %timeit [1..10]
> 625 loops, best of 3: 58.4 µs per loop
> }}}
> 
> The right place to put this would probably be in local/bin/ipy_profile_sage.py.

Thank you!

While you replied, I tried to post the following:

Replying to [comment:10 mhansen]:
> Are you doing this in the notebook or the command-line?  They're two totally separate things.

It is command-line, and I don't know what happens on the notebook. Can you test it?

If it is in `preparser_ipython`, then the following might be the source of trouble:

```
def preparse_ipython(line, reset=True):
    global num_lines
    global q_lines

    L = line.lstrip()
    if L.startswith('%'):
        # This should be installed as an Ipython magic command,
        # but I don't know how yet...
        L = L[1:].strip()
        import sage.interfaces.all
        if L.lower() in sage.interfaces.all.interfaces:
            switch_interface(L.lower())
            return "''"
        else:
            # only preparse non-magic lines
            return line
```


Hence, if the line starts with `%` and if the word after `%` is not the name of an interface than simply the line is returned unchanged. 

But what happens afterwards? In the end of the day, `%timeit` gets an interpretation and does call some `timeit` command!

> Can you hop on IRC?

I try (I never used IRC before). So, if it works, see you soon.

Cheers
 Simon



---

archive/issue_comments_004801.json:
```json
{
    "body": "Attachment [timeit.patch](tarball://root/attachments/some-uuid/ticket797/timeit.patch) by @simon-king-jena created at 2009-01-21 22:05:18\n\nChange preparse_ipython so that %timeit results in calling timeit.eval",
    "created_at": "2009-01-21T22:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4801",
    "user": "@simon-king-jena"
}
```

Attachment [timeit.patch](tarball://root/attachments/some-uuid/ticket797/timeit.patch) by @simon-king-jena created at 2009-01-21 22:05:18

Change preparse_ipython so that %timeit results in calling timeit.eval



---

archive/issue_comments_004802.json:
```json
{
    "body": "In `preparse_ipython`, lines starting with `%` have not been changed unless they refer to some interface. I added support for `%timeit`.\n\nIdea: Call `timeit.eval`\n\nWith the patch, the following examples now work:\n\n```\nsage: %timeit [1..10]\n625 loops, best of 3: 127 \u00c2\u00b5s per loop\nsage: %timeit 'a'==\"a\"\n625 loops, best of 3: 285 ns per loop\n```\n\nand the other ways of calling the timer still work:\n\n```\nsage: %time [1..10]\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nsage: timeit('[1..10]')\n625 loops, best of 3: 127 \u00c2\u00b5s per loop\n```\n",
    "created_at": "2009-01-21T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4802",
    "user": "@simon-king-jena"
}
```

In `preparse_ipython`, lines starting with `%` have not been changed unless they refer to some interface. I added support for `%timeit`.

Idea: Call `timeit.eval`

With the patch, the following examples now work:

```
sage: %timeit [1..10]
625 loops, best of 3: 127 Âµs per loop
sage: %timeit 'a'=="a"
625 loops, best of 3: 285 ns per loop
```

and the other ways of calling the timer still work:

```
sage: %time [1..10]
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
sage: timeit('[1..10]')
625 loops, best of 3: 127 Âµs per loop
```




---

archive/issue_comments_004803.json:
```json
{
    "body": "Changing keywords from \"\" to \"timeit ipython\".",
    "created_at": "2009-01-21T22:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4803",
    "user": "@simon-king-jena"
}
```

Changing keywords from "" to "timeit ipython".



---

archive/issue_comments_004804.json:
```json
{
    "body": "Replying to [comment:13 SimonKing]:\n> In `preparse_ipython`, lines starting with `%` have not been changed unless they refer to some interface. I added support for `%timeit`.\n> \n> Idea: Call `timeit.eval`\n\nProbably I should elaborate more on how it works.\n\nIn the old version of `preparse_ipython`, it was tested whether an input line starts with '%'. If this was the case, then the word after '%' was checked. If that word referred to an interface,  the interface was used. If the word after '%' was differently, the line was returned without a change.\n\nFor the new version, I suggest to test whether the word after '%' is 'timeit'. If it is, `preparse_ipython` returns `timeit.eval(..rest of the input line..)`.",
    "created_at": "2009-01-22T19:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4804",
    "user": "@simon-king-jena"
}
```

Replying to [comment:13 SimonKing]:
> In `preparse_ipython`, lines starting with `%` have not been changed unless they refer to some interface. I added support for `%timeit`.
> 
> Idea: Call `timeit.eval`

Probably I should elaborate more on how it works.

In the old version of `preparse_ipython`, it was tested whether an input line starts with '%'. If this was the case, then the word after '%' was checked. If that word referred to an interface,  the interface was used. If the word after '%' was differently, the line was returned without a change.

For the new version, I suggest to test whether the word after '%' is 'timeit'. If it is, `preparse_ipython` returns `timeit.eval(..rest of the input line..)`.



---

archive/issue_comments_004805.json:
```json
{
    "body": "To emphasize another detail: My suggestion only relates with `%timeit` on the command line, not on the notebook.",
    "created_at": "2009-01-22T19:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4805",
    "user": "@simon-king-jena"
}
```

To emphasize another detail: My suggestion only relates with `%timeit` on the command line, not on the notebook.



---

archive/issue_comments_004806.json:
```json
{
    "body": "This patch works for me, but I think mhansen ought to comment on this approach versus the approach he advocated above using `_ip.expose_magic(\"timeit\", lambda self, s: timeit(s))`",
    "created_at": "2009-01-28T17:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4806",
    "user": "@jasongrout"
}
```

This patch works for me, but I think mhansen ought to comment on this approach versus the approach he advocated above using `_ip.expose_magic("timeit", lambda self, s: timeit(s))`



---

archive/issue_comments_004807.json:
```json
{
    "body": "The _ip.expose_magic approach also seems to work just as well.  I would prefer using the ipython mechanism for doing this, rather than complicating the preparser.\n\nIn fact, I'd suggest using ipython to do all of the %mode functionality as well, if it's a possibility.",
    "created_at": "2009-01-28T17:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4807",
    "user": "@jasongrout"
}
```

The _ip.expose_magic approach also seems to work just as well.  I would prefer using the ipython mechanism for doing this, rather than complicating the preparser.

In fact, I'd suggest using ipython to do all of the %mode functionality as well, if it's a possibility.



---

archive/issue_comments_004808.json:
```json
{
    "body": "Simon,\n\nwhat do you think about the idea of using ipython to do this, like mhansen suggests above?  I think it's cleaner, it keeps the ipython stuff together (i.e., the \"%\" commands with ipython), and avoids making the preparser more complicated.",
    "created_at": "2009-03-24T21:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4808",
    "user": "@jasongrout"
}
```

Simon,

what do you think about the idea of using ipython to do this, like mhansen suggests above?  I think it's cleaner, it keeps the ipython stuff together (i.e., the "%" commands with ipython), and avoids making the preparser more complicated.



---

archive/issue_comments_004809.json:
```json
{
    "body": "Hi Jason,\n\nReplying to [comment:18 jason]:\n> what do you think about the idea of using ipython to do this, like mhansen suggests above?  I think it's cleaner, it keeps the ipython stuff together (i.e., the \"%\" commands with ipython), and avoids making the preparser more complicated.\n\nSure, it makes sense. The problem is that i have no idea about ipython, so, I guess i would not be able to do it in that way. Perhaps i should look at local/bin/ipy_profile_sage.py, but i wouldn't be upset if someone else were faster... :)\n\nCheers,\n          Simon",
    "created_at": "2009-03-25T08:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4809",
    "user": "@simon-king-jena"
}
```

Hi Jason,

Replying to [comment:18 jason]:
> what do you think about the idea of using ipython to do this, like mhansen suggests above?  I think it's cleaner, it keeps the ipython stuff together (i.e., the "%" commands with ipython), and avoids making the preparser more complicated.

Sure, it makes sense. The problem is that i have no idea about ipython, so, I guess i would not be able to do it in that way. Perhaps i should look at local/bin/ipy_profile_sage.py, but i wouldn't be upset if someone else were faster... :)

Cheers,
          Simon



---

archive/issue_comments_004810.json:
```json
{
    "body": "Changing this to \"needs work\" in light of mhansen's solution above.",
    "created_at": "2009-04-22T02:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4810",
    "user": "@jasongrout"
}
```

Changing this to "needs work" in light of mhansen's solution above.



---

archive/issue_comments_004811.json:
```json
{
    "body": "Attachment [trac_797.patch](tarball://root/attachments/some-uuid/ticket797/trac_797.patch) by @mwhansen created at 2010-01-17 07:31:32",
    "created_at": "2010-01-17T07:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4811",
    "user": "@mwhansen"
}
```

Attachment [trac_797.patch](tarball://root/attachments/some-uuid/ticket797/trac_797.patch) by @mwhansen created at 2010-01-17 07:31:32



---

archive/issue_comments_004812.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-17T07:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4812",
    "user": "@mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004813.json:
```json
{
    "body": "I've put a patch up which implements the expose_magic idea.",
    "created_at": "2010-01-17T07:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4813",
    "user": "@mwhansen"
}
```

I've put a patch up which implements the expose_magic idea.



---

archive/issue_comments_004814.json:
```json
{
    "body": "Looks great!  Positive review to Mike's patch.  Only apply Mike's patch (to the local/bin repository!)",
    "created_at": "2010-01-17T08:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4814",
    "user": "@jasongrout"
}
```

Looks great!  Positive review to Mike's patch.  Only apply Mike's patch (to the local/bin repository!)



---

archive/issue_comments_004815.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T08:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4815",
    "user": "@jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T22:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/797#issuecomment-4816",
    "user": "@rlmill"
}
```

Resolution: fixed
