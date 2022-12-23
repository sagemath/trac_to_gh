# Issue 118: Tab completion is too noisy

archive/issues_000118.json:
```json
{
    "body": "Assignee: was\n\nI'd like to see TAB completion work more like 'bash': if I type \"foo[TAB]\", the system should complete up to ambiguity:\n\n```\nfoo[TAB]b\n```\n\nfor example (assuming 'foobar' and 'fooble' are both known).  If I hit tab twice (with no completion), I get the display of the alternatives:\n\n```\nsage: foo[TAB]b[TAB][TAB]\nfoobar  fooble  \nsage: foob\n```\n\nAs it is now, an inadvertent TAB will blow unwanted bits all over my screen.\n\nIs this under SAGE control, or is it an iPython thing?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/118\n\n",
    "created_at": "2006-10-07T20:38:24Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "Tab completion is too noisy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/118",
    "user": "justin"
}
```
Assignee: was

I'd like to see TAB completion work more like 'bash': if I type "foo[TAB]", the system should complete up to ambiguity:

```
foo[TAB]b
```

for example (assuming 'foobar' and 'fooble' are both known).  If I hit tab twice (with no completion), I get the display of the alternatives:

```
sage: foo[TAB]b[TAB][TAB]
foobar  fooble  
sage: foob
```

As it is now, an inadvertent TAB will blow unwanted bits all over my screen.

Is this under SAGE control, or is it an iPython thing?


Issue created by migration from https://trac.sagemath.org/ticket/118





---

archive/issue_comments_000553.json:
```json
{
    "body": "In the notebook we can do anything we want.  In the command line this is entirely\nan IPYthon thing.  It would, of course, be good to keep the behavior of the notebook\nand of Ipython in sync.    I'm not sure I agree with the change you want, since so\nfar I rather like IPython's behavior.   -- William",
    "created_at": "2006-10-14T20:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/118#issuecomment-553",
    "user": "was"
}
```

In the notebook we can do anything we want.  In the command line this is entirely
an IPYthon thing.  It would, of course, be good to keep the behavior of the notebook
and of Ipython in sync.    I'm not sure I agree with the change you want, since so
far I rather like IPython's behavior.   -- William



---

archive/issue_comments_000554.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2006-10-14T20:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/118#issuecomment-554",
    "user": "was"
}
```

Changing priority from major to minor.



---

archive/issue_comments_000555.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-16T05:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/118#issuecomment-555",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000556.json:
```json
{
    "body": "\n```\nJustin,\n\nSee below, regarding tab completion.  \n\n------- Forwarded message -------\nFrom: \"Fernando Perez\" <Fernando.Perez@colorado.edu>\nTo: \"William Stein\" <wstein@gmail.com>\nCc:\nSubject: Re: ipython huge traceback\nDate: Sun, 15 Oct 2006 19:16:32 -0700\n\nJustin Walker suggested changing the tab behavior in ipython to be like\nin bash, which it currently isn't.  Any thoughts about that?\n    http://sage.math.washington.edu:9002/sage_trac/ticket/118\n I like IPython's tab completion behavior and hadn't thought much about\nit differing from bash's until now.\n\nThat's entirely a user customization, and it has nothing to do with Bash: it's purely the behavior of the readline library.  IPython happens to tweak readline one way and bash does it in a different way, but readline is very customizable.\n\nJustin is free to set the readline behavior to his heart's content via the settings in the sage ipythonrc file.  Just look for those called readline_parse_and_bind, which will make calls to the function with that name in Python's readline library.  The meaning of those settings is defined in the readline documentation.\n\nSo this is something users can set as they like it, it's not really a bug.\n\nIn particular, what Justin wants requires changing\n\nreadline_parse_and_bind set show-all-if-ambiguous on\n\nto:\n\nreadline_parse_and_bind set show-all-if-ambiguous off\n\nin his personal config file.\n\nCheers,\n\nf\n\n\n```\n",
    "created_at": "2006-10-16T05:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/118#issuecomment-556",
    "user": "was"
}
```


```
Justin,

See below, regarding tab completion.  

------- Forwarded message -------
From: "Fernando Perez" <Fernando.Perez@colorado.edu>
To: "William Stein" <wstein@gmail.com>
Cc:
Subject: Re: ipython huge traceback
Date: Sun, 15 Oct 2006 19:16:32 -0700

Justin Walker suggested changing the tab behavior in ipython to be like
in bash, which it currently isn't.  Any thoughts about that?
    http://sage.math.washington.edu:9002/sage_trac/ticket/118
 I like IPython's tab completion behavior and hadn't thought much about
it differing from bash's until now.

That's entirely a user customization, and it has nothing to do with Bash: it's purely the behavior of the readline library.  IPython happens to tweak readline one way and bash does it in a different way, but readline is very customizable.

Justin is free to set the readline behavior to his heart's content via the settings in the sage ipythonrc file.  Just look for those called readline_parse_and_bind, which will make calls to the function with that name in Python's readline library.  The meaning of those settings is defined in the readline documentation.

So this is something users can set as they like it, it's not really a bug.

In particular, what Justin wants requires changing

readline_parse_and_bind set show-all-if-ambiguous on

to:

readline_parse_and_bind set show-all-if-ambiguous off

in his personal config file.

Cheers,

f


```

