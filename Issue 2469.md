# Issue 2469: fix readline extra space issue in sage (ipython)

archive/issues_002469.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n>  > On Mon, Mar 10, 2008 at 1:27 PM, Nikos Apostolakis <nikos.ap@gmail.com> wrote:\n>  >  >\n>  >  >  Hello group,\n>  >  >\n>  >  >  the following is not terribly important but it bothers me.  When\n>  >  >  using the cli to SAGE the completion adds extra space after the\n>  >  >  name of functions or methods. For example if I hit den[tab] in the\n>  >  >  sage prompt I get denominator *, where the star stands for the\n>  >  >  cursor, that is there is an extra space after \"denominator\".   I am\n>  >  >  then forced to either have a space between a function and the\n>  >  >  parenthesis enclosing its arguments or to move the cursor back one\n>  >  >  space.  The former annoys me aesthetically and the latter wastes my\n>  >  >  time (albeit a small fraction of it).\n>  >  >\n>  >  >  Is there a way to turn this off? some configuration option perhaps?\n>  >  >\n>  >\n>  >  (1) This is an Ipython problem.  Probably Sage itself has little to do\n>  >  with it.  Hence I've cc'd this message to Fernando Perez (author\n>  >  of IPython).\n>  >\n>  >  (2) I just checked on a bunch of machines.  The behavior you mention\n>  >  above does *not* occur on any of my OS X machines.  It also does\n>  >  not occur for me on sage.math (a Debian 64-bit machine).  It does\n>  >  occur on several 32-bit and 64-bit Linux installs that I have handy.\n>  >  Sage builds its own readline and uses exact the same config files\n>  >  on all machines, so I'm fairly puzzled by all this.\n>\n>  I'm afraid it's not really an ipython problem, but how readline ends\n>  up built on any given box.  I've fought this particular one before:\n>\n>  http://projects.scipy.org/pipermail/ipython-user/2005-April/002617.html\n>\n>  As you can see, the python readline doesn't expose the necessary\n>  functionality at all:\n>\n>  http://mail.python.org/pipermail/python-list/2002-December/176942.html\n>\n>  So the actual behavior will be hardcoded by however readline ends up\n>  built.  You may be able to tweak *your* readline build so that\n>  HAVE_RL_COMPLETION_APPEND_CHARACTER is defined at build time and hence\n>  you get the null completion character.\n\nExcellent.  Since Sage builds its own readline, we can do what it takes\nto make sure this works.\n\nThanks!\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2469\n\n",
    "created_at": "2008-03-11T06:30:40Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "fix readline extra space issue in sage (ipython)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2469",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
>  > On Mon, Mar 10, 2008 at 1:27 PM, Nikos Apostolakis <nikos.ap@gmail.com> wrote:
>  >  >
>  >  >  Hello group,
>  >  >
>  >  >  the following is not terribly important but it bothers me.  When
>  >  >  using the cli to SAGE the completion adds extra space after the
>  >  >  name of functions or methods. For example if I hit den[tab] in the
>  >  >  sage prompt I get denominator *, where the star stands for the
>  >  >  cursor, that is there is an extra space after "denominator".   I am
>  >  >  then forced to either have a space between a function and the
>  >  >  parenthesis enclosing its arguments or to move the cursor back one
>  >  >  space.  The former annoys me aesthetically and the latter wastes my
>  >  >  time (albeit a small fraction of it).
>  >  >
>  >  >  Is there a way to turn this off? some configuration option perhaps?
>  >  >
>  >
>  >  (1) This is an Ipython problem.  Probably Sage itself has little to do
>  >  with it.  Hence I've cc'd this message to Fernando Perez (author
>  >  of IPython).
>  >
>  >  (2) I just checked on a bunch of machines.  The behavior you mention
>  >  above does *not* occur on any of my OS X machines.  It also does
>  >  not occur for me on sage.math (a Debian 64-bit machine).  It does
>  >  occur on several 32-bit and 64-bit Linux installs that I have handy.
>  >  Sage builds its own readline and uses exact the same config files
>  >  on all machines, so I'm fairly puzzled by all this.
>
>  I'm afraid it's not really an ipython problem, but how readline ends
>  up built on any given box.  I've fought this particular one before:
>
>  http://projects.scipy.org/pipermail/ipython-user/2005-April/002617.html
>
>  As you can see, the python readline doesn't expose the necessary
>  functionality at all:
>
>  http://mail.python.org/pipermail/python-list/2002-December/176942.html
>
>  So the actual behavior will be hardcoded by however readline ends up
>  built.  You may be able to tweak *your* readline build so that
>  HAVE_RL_COMPLETION_APPEND_CHARACTER is defined at build time and hence
>  you get the null completion character.

Excellent.  Since Sage builds its own readline, we can do what it takes
to make sure this works.

Thanks!

```


Issue created by migration from https://trac.sagemath.org/ticket/2469





---

archive/issue_comments_016725.json:
```json
{
    "body": "Another ticket for this issue is at #2306",
    "created_at": "2008-08-21T23:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2469#issuecomment-16725",
    "user": "@jasongrout"
}
```

Another ticket for this issue is at #2306



---

archive/issue_comments_016726.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-28T00:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2469#issuecomment-16726",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016727.json:
```json
{
    "body": "I just checked and on all my builds I get the following:\n\n```\nsage-3.1.3.alpha2/local/include$ grep -r HAVE_RL_COMPLETION_APPEND_CHARACTER *\npython2.5/pyconfig.h:#define HAVE_RL_COMPLETION_APPEND_CHARACTER 1\n```\n\nIn #3947 we fixed the python.spkg LDFLAGS to pick up Sage's python, so I consider this issue resolved. I checked about 8 different Linux builds and cannot reproduce this problem. So unless someone comes up with a broken system I am closing this as fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-28T00:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2469#issuecomment-16727",
    "user": "mabshoff"
}
```

I just checked and on all my builds I get the following:

```
sage-3.1.3.alpha2/local/include$ grep -r HAVE_RL_COMPLETION_APPEND_CHARACTER *
python2.5/pyconfig.h:#define HAVE_RL_COMPLETION_APPEND_CHARACTER 1
```

In #3947 we fixed the python.spkg LDFLAGS to pick up Sage's python, so I consider this issue resolved. I checked about 8 different Linux builds and cannot reproduce this problem. So unless someone comes up with a broken system I am closing this as fixed.

Cheers,

Michael
