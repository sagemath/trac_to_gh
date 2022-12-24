# Issue 386: Enhance "attach <file>" in the notebook

archive/issues_000386.json:
```json
{
    "body": "Assignee: boothby\n\nI noticed that the natural progression for someone who starts to work with sage is that they start with using the notebook exclusively. Any \"def\"d functions are simply defined in a cell in the worksheet (with all scrollbar problems that go with it). As they progress, and want to test their routine in different situations, this method becomes cumbersome: they have to copy the cell content to other worksheets if they want to run tests in other worksheets and the usual problems arise by having several copies lying around: Edits in one version are not propagated to the other.\n\nThis would be the natural moment to explain that the user should put his/her routines in, say, file.sage instead and attach it in any worksheet that is used. Ultimately, the user should probably learn how to use an independent, high quality source code editor to work with the files, but it would be nice if there were an intermediate step: An easy way to create, edit and attach a file within the scope of the notebook, but accessible from all worksheets, much like the \"saved objects\".\n\nA hackish way is the following, assuming that /home/nobody is writable for the notebook UID:\n\n```\n%sh\ncat > /home/nobody/file.sage <<EOFEOFEOF\n#######################################\n## file.sage\ndef facto(n):\n  if n == 1:\n    return 1\n  else:\n    return n*facto(n-1)\n\nEOFEOFEOF \n```\n\nThis causes all kinds of interesting errors, since the cell directory may not exist or may have been deleted by the system for, to me, no apparent reason. In all cases, however, the code has the desired effect of creating the file.\n\nNow, after\n\n```\nattach \"/home/nobody/file.sage\"\n```\n\n\nthe user can use the routine \"facto\" in the worksheet and in fact, editing the %sh cell and executing it will lead to sage rereading file.sage the next time around, effecting the edit in the worksheet.\n\nWould it be possible to have a less hackish way of establishing this? In fact, once a full force source code editor is part of sage, perhaps the most useful thing would be if one could open a tab/window on one of those \"attach\" files rather than having to do the editing in cells.\n\nI understand that the security implications of stuff like this are even worse than just the shielded environment and may require some serious thinking to resolve, but lowering the threshold of doing actual programming in sage should increase the number of developers/contributors.\n\nWhile you're at it, why not put the files under mercurial control as well and provide some nice tools in the notebook to view the various revisions?\n\nIssue created by migration from https://trac.sagemath.org/ticket/386\n\n",
    "created_at": "2007-06-07T19:24:48Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Enhance \"attach <file>\" in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/386",
    "user": "nbruin"
}
```
Assignee: boothby

I noticed that the natural progression for someone who starts to work with sage is that they start with using the notebook exclusively. Any "def"d functions are simply defined in a cell in the worksheet (with all scrollbar problems that go with it). As they progress, and want to test their routine in different situations, this method becomes cumbersome: they have to copy the cell content to other worksheets if they want to run tests in other worksheets and the usual problems arise by having several copies lying around: Edits in one version are not propagated to the other.

This would be the natural moment to explain that the user should put his/her routines in, say, file.sage instead and attach it in any worksheet that is used. Ultimately, the user should probably learn how to use an independent, high quality source code editor to work with the files, but it would be nice if there were an intermediate step: An easy way to create, edit and attach a file within the scope of the notebook, but accessible from all worksheets, much like the "saved objects".

A hackish way is the following, assuming that /home/nobody is writable for the notebook UID:

```
%sh
cat > /home/nobody/file.sage <<EOFEOFEOF
#######################################
## file.sage
def facto(n):
  if n == 1:
    return 1
  else:
    return n*facto(n-1)

EOFEOFEOF 
```

This causes all kinds of interesting errors, since the cell directory may not exist or may have been deleted by the system for, to me, no apparent reason. In all cases, however, the code has the desired effect of creating the file.

Now, after

```
attach "/home/nobody/file.sage"
```


the user can use the routine "facto" in the worksheet and in fact, editing the %sh cell and executing it will lead to sage rereading file.sage the next time around, effecting the edit in the worksheet.

Would it be possible to have a less hackish way of establishing this? In fact, once a full force source code editor is part of sage, perhaps the most useful thing would be if one could open a tab/window on one of those "attach" files rather than having to do the editing in cells.

I understand that the security implications of stuff like this are even worse than just the shielded environment and may require some serious thinking to resolve, but lowering the threshold of doing actual programming in sage should increase the number of developers/contributors.

While you're at it, why not put the files under mercurial control as well and provide some nice tools in the notebook to view the various revisions?

Issue created by migration from https://trac.sagemath.org/ticket/386





---

archive/issue_comments_001895.json:
```json
{
    "body": "I implemented this already... via the DATA --> Upload or Create File function.  That does exactly what this ticket is about.  Of course, this ticket has some vague revision control stuff, but that's too vague for a single ticket.  So I'm closing this.",
    "created_at": "2009-11-19T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/386#issuecomment-1895",
    "user": "was"
}
```

I implemented this already... via the DATA --> Upload or Create File function.  That does exactly what this ticket is about.  Of course, this ticket has some vague revision control stuff, but that's too vague for a single ticket.  So I'm closing this.



---

archive/issue_comments_001896.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/386#issuecomment-1896",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_001897.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> So I'm closing this. \n\nDo you know in which version of Sage was the feature described in this ticket was merged? If it was merged in Sage 4.3, was it alpha0 or alpha1?",
    "created_at": "2009-12-08T23:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/386#issuecomment-1897",
    "user": "mvngu"
}
```

Replying to [comment:2 was]:
> So I'm closing this. 

Do you know in which version of Sage was the feature described in this ticket was merged? If it was merged in Sage 4.3, was it alpha0 or alpha1?



---

archive/issue_comments_001898.json:
```json
{
    "body": "> Do you know in which version of Sage was the feature described in this ticket was \n> merged? If it was merged in Sage 4.3, was it alpha0 or alpha1? \n\nIt was back in 2008 sometime...",
    "created_at": "2009-12-09T05:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/386#issuecomment-1898",
    "user": "was"
}
```

> Do you know in which version of Sage was the feature described in this ticket was 
> merged? If it was merged in Sage 4.3, was it alpha0 or alpha1? 

It was back in 2008 sometime...
