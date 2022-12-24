# Issue 4293: reload(sage.combinat.crystals)

archive/issues_004293.json:
```json
{
    "body": "Assignee: @williamstein\n\nI would love to have the following feature:\n\n  reload(sage.combinat.crystals)\n\nwhich would triggers an immediate reload recursively of all the files within the sage.combinat.crystals module.\n\nFor my personal debugging cycle, this would be more practical than attach:\n- I don't mind having to ask for the reload; actually having control over when the files is reloaded\n  would be safer\n- I often modify many  files in a given module simultaneously, and not having to specify each file\n  separately is handy\n- I prefer to just specify a module name rather than a file name\n\nThanks in advance!\n\nIssue created by migration from https://trac.sagemath.org/ticket/4293\n\n",
    "created_at": "2008-10-15T11:30:51Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "reload(sage.combinat.crystals)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4293",
    "user": "@nthiery"
}
```
Assignee: @williamstein

I would love to have the following feature:

  reload(sage.combinat.crystals)

which would triggers an immediate reload recursively of all the files within the sage.combinat.crystals module.

For my personal debugging cycle, this would be more practical than attach:
- I don't mind having to ask for the reload; actually having control over when the files is reloaded
  would be safer
- I often modify many  files in a given module simultaneously, and not having to specify each file
  separately is handy
- I prefer to just specify a module name rather than a file name

Thanks in advance!

Issue created by migration from https://trac.sagemath.org/ticket/4293


