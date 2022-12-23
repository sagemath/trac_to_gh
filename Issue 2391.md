# Issue 2391: module docstring bug running filename.sage from the command line

archive/issues_002391.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\n\nOn Thu, Feb 28, 2008 at 9:36 AM, Kate <kate01123@gmail.com> wrote:\n> \n>  What gives with the following session below?\n>  More specifically, what happens to the file docstring\n>  when the file has a .sage extension?\n\nThere is a bug in the .sage --> .py conversion process that\nyour example below illustrates.  We are tracking this at\n\n\n>  \n>  =============== begin shell session ===============\n>  \n>  $ cat > sanity\n>  #!/usr/bin/env sage\n>  r\"\"\"Here is a docstring for this file.\"\"\"\n>  print __doc__\n>  <control-d>\n>  $ cat sanity\n>  #!/usr/bin/env sage\n>  r\"\"\"Here is a docstring for this file.\"\"\"\n>  print __doc__\n>  $ chmod +x sanity\n>  $ ./sanity\n>  Here is a docstring for this file.\n>  $ cp sanity madness.sage\n>  $ ./madness.sage\n>  None\n>  $\n>  \n>  =============== end shell session ===============\n>  \n>  Kate\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2391\n\n",
    "created_at": "2008-03-05T00:41:57Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "module docstring bug running filename.sage from the command line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2391",
    "user": "was"
}
```
Assignee: was


```


On Thu, Feb 28, 2008 at 9:36 AM, Kate <kate01123@gmail.com> wrote:
> 
>  What gives with the following session below?
>  More specifically, what happens to the file docstring
>  when the file has a .sage extension?

There is a bug in the .sage --> .py conversion process that
your example below illustrates.  We are tracking this at


>  
>  =============== begin shell session ===============
>  
>  $ cat > sanity
>  #!/usr/bin/env sage
>  r"""Here is a docstring for this file."""
>  print __doc__
>  <control-d>
>  $ cat sanity
>  #!/usr/bin/env sage
>  r"""Here is a docstring for this file."""
>  print __doc__
>  $ chmod +x sanity
>  $ ./sanity
>  Here is a docstring for this file.
>  $ cp sanity madness.sage
>  $ ./madness.sage
>  None
>  $
>  
>  =============== end shell session ===============
>  
>  Kate

```


Issue created by migration from https://trac.sagemath.org/ticket/2391





---

archive/issue_comments_016130.json:
```json
{
    "body": "Attachment\n\nthis fixes the bug and vastly improves the documentation of sage-preparse",
    "created_at": "2008-03-05T01:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2391#issuecomment-16130",
    "user": "was"
}
```

Attachment

this fixes the bug and vastly improves the documentation of sage-preparse



---

archive/issue_comments_016131.json:
```json
{
    "body": "Works for me against 2.10.3.rc1.  Apply to hg_scripts.",
    "created_at": "2008-03-05T05:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2391#issuecomment-16131",
    "user": "mhansen"
}
```

Works for me against 2.10.3.rc1.  Apply to hg_scripts.



---

archive/issue_comments_016132.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T05:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2391#issuecomment-16132",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc2



---

archive/issue_comments_016133.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T05:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2391#issuecomment-16133",
    "user": "mabshoff"
}
```

Resolution: fixed
