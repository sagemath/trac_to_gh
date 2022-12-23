# Issue 1969: ipython -- update to svn to get this new %hist functionality

archive/issues_001969.json:
```json
{
    "body": "Assignee: was\n\n\n```\n> Something like %history, but which writes the output to a file.\n\nI just put it in SVN, as the new '-f flag'. This is what it looks like:\n\nIn [1]: hist -f foo\nFile 'foo' exists. Overwrite? n\nAborting.\n\nIn [2]: hist\n1: _ip.magic(\"hist -f foo\")\n2: _ip.magic(\"hist \")\n\nIn [3]: hist -r\n1: hist -f foo\n2: hist\n3: hist -r\n\nIn [4]: hist -rn\nhist -f foo\nhist\nhist -r\nhist -rn\n\nIn [5]: hist -rn -f foo\nFile 'foo' exists. Overwrite? y\n\nIn [6]: !cat foo\nhist -f foo\nhist\nhist -r\nhist -rn\nhist -rn -f foo\n\n> By the way, %hist still is preparsed in Sage.  I should have fixed\n> this long ago.  Could you remind me what you recommended I do?\n\nSee above, -r gives you the raw history always, and -n omits line numbers.\n\n\nLet me know how this works for you.\n\n -- Fernando\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1969\n\n",
    "created_at": "2008-01-29T10:54:40Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "ipython -- update to svn to get this new %hist functionality",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1969",
    "user": "was"
}
```
Assignee: was


```
> Something like %history, but which writes the output to a file.

I just put it in SVN, as the new '-f flag'. This is what it looks like:

In [1]: hist -f foo
File 'foo' exists. Overwrite? n
Aborting.

In [2]: hist
1: _ip.magic("hist -f foo")
2: _ip.magic("hist ")

In [3]: hist -r
1: hist -f foo
2: hist
3: hist -r

In [4]: hist -rn
hist -f foo
hist
hist -r
hist -rn

In [5]: hist -rn -f foo
File 'foo' exists. Overwrite? y

In [6]: !cat foo
hist -f foo
hist
hist -r
hist -rn
hist -rn -f foo

> By the way, %hist still is preparsed in Sage.  I should have fixed
> this long ago.  Could you remind me what you recommended I do?

See above, -r gives you the raw history always, and -n omits line numbers.


Let me know how this works for you.

 -- Fernando
```


Issue created by migration from https://trac.sagemath.org/ticket/1969





---

archive/issue_comments_012747.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-08-13T07:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1969#issuecomment-12747",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_012748.json:
```json
{
    "body": "Duplicate, we did update to ipython 0.8.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T07:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1969#issuecomment-12748",
    "user": "mabshoff"
}
```

Duplicate, we did update to ipython 0.8.2.

Cheers,

Michael
