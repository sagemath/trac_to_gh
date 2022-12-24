# Issue 422: hostname's with dashes (?) in them break SAGE interfaces

archive/issues_000422.json:
```json
{
    "body": "Assignee: @williamstein\n\nI discovered live during my SAGE demo at CECM that if the hostname is really weird,\ncomplicated, and has dashes, dots, spaces ? etc., in it, then e.g., \n\n```\n   maple('2+2')\n```\n\nwon't work.\n\nThe fix is to clean the hostname before using it to construct the relevant\ntemp directory in .sage/temp.  By clean, I mean replace any bad characters\nby underscores, say. \n\nIssue created by migration from https://trac.sagemath.org/ticket/422\n\n",
    "created_at": "2007-08-10T20:24:06Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "hostname's with dashes (?) in them break SAGE interfaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/422",
    "user": "@williamstein"
}
```
Assignee: @williamstein

I discovered live during my SAGE demo at CECM that if the hostname is really weird,
complicated, and has dashes, dots, spaces ? etc., in it, then e.g., 

```
   maple('2+2')
```

won't work.

The fix is to clean the hostname before using it to construct the relevant
temp directory in .sage/temp.  By clean, I mean replace any bad characters
by underscores, say. 

Issue created by migration from https://trac.sagemath.org/ticket/422





---

archive/issue_comments_002117.json:
```json
{
    "body": "\n```\n[23:48] <william> anyway, regarding #422, any thoughts?\n[23:48] <william> it's hard to replicate.\n[23:48] <mabshoff> re #422: my host has a dash in it.\n[23:48] <william> i happened to me *during* a big talk, which was pretty crazy.\n[23:48] <mabshoff> you cannot have spaces in names.\n[23:48] <william> there were other symbols, so maybe it wasn't the dash.\n[23:49] <mabshoff> And dots are usually present.\n[23:49] <william> The hostname was really bad.\n[23:49] <william> Maybe a *.\n[23:49] <mabshoff> Yeah, that could screw with things.\n[23:49] <william> this broken *all* interfaces, including gap, etc.\n[23:49] <mabshoff> I think there is a standard, i.e. name \\in [0..9] \\cup [a-Z] \\cup {-,.} or something like that.\n[23:50] <william> it's also possible that the problem wasn't the hostname.\n[23:50] <william> in the talk somebody said it was, and i disabled my network connection, and the problem went away.\n[23:50] <william> the hostname looked very complicated.\n[23:50] <william> I wish I had copied it.\n[23:50] <mabshoff> okay\n[23:51] <william> wait -- they are all in .sage/temp\n[23:51] <william> cleaner-d142-058-050-016.wireless.sfu.ca.pid\n[23:51] <mabshoff> Any thoughts on \"sage -t -gdb foo.py\"?, i.e. #374\n[23:51] <william> d142-058-050-016.wireless.sfu.ca\n[23:51] <william> those hostnames are fine.\n\n```\n",
    "created_at": "2007-08-19T06:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/422#issuecomment-2117",
    "user": "@williamstein"
}
```


```
[23:48] <william> anyway, regarding #422, any thoughts?
[23:48] <william> it's hard to replicate.
[23:48] <mabshoff> re #422: my host has a dash in it.
[23:48] <william> i happened to me *during* a big talk, which was pretty crazy.
[23:48] <mabshoff> you cannot have spaces in names.
[23:48] <william> there were other symbols, so maybe it wasn't the dash.
[23:49] <mabshoff> And dots are usually present.
[23:49] <william> The hostname was really bad.
[23:49] <william> Maybe a *.
[23:49] <mabshoff> Yeah, that could screw with things.
[23:49] <william> this broken *all* interfaces, including gap, etc.
[23:49] <mabshoff> I think there is a standard, i.e. name \in [0..9] \cup [a-Z] \cup {-,.} or something like that.
[23:50] <william> it's also possible that the problem wasn't the hostname.
[23:50] <william> in the talk somebody said it was, and i disabled my network connection, and the problem went away.
[23:50] <william> the hostname looked very complicated.
[23:50] <william> I wish I had copied it.
[23:50] <mabshoff> okay
[23:51] <william> wait -- they are all in .sage/temp
[23:51] <william> cleaner-d142-058-050-016.wireless.sfu.ca.pid
[23:51] <mabshoff> Any thoughts on "sage -t -gdb foo.py"?, i.e. #374
[23:51] <william> d142-058-050-016.wireless.sfu.ca
[23:51] <william> those hostnames are fine.

```




---

archive/issue_comments_002118.json:
```json
{
    "body": "We need to find an actual failure in order to solve this.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-10T05:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/422#issuecomment-2118",
    "user": "mabshoff"
}
```

We need to find an actual failure in order to solve this.

Cheers,

Michael



---

archive/issue_comments_002119.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-02-08T07:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/422#issuecomment-2119",
    "user": "@craigcitro"
}
```

Resolution: invalid



---

archive/issue_comments_002120.json:
```json
{
    "body": "Not reproducible.",
    "created_at": "2008-02-08T07:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/422#issuecomment-2120",
    "user": "@craigcitro"
}
```

Not reproducible.
