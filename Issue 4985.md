# Issue 4985: Expand documentation for list_plot to point out the utility of zip

archive/issues_004985.json:
```json
{
    "body": "Assignee: was\n\nCC:  jhpalmieri\n\nWe should expand the documentation for list_plot so that questions like on the latter half of this thread don't happen:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/e523b8ade175746c\n\nBasically, we should explain how to use zip like thus:\n\nlist_plot(zip(list of x-coords, list of y-coords))\n\nso that people from Matlab don't get confused by the very unhelpful error message.  Maybe the error message ought to be changed too.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4985\n\n",
    "created_at": "2009-01-16T02:50:47Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Expand documentation for list_plot to point out the utility of zip",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4985",
    "user": "jason"
}
```
Assignee: was

CC:  jhpalmieri

We should expand the documentation for list_plot so that questions like on the latter half of this thread don't happen:

http://groups.google.com/group/sage-support/browse_thread/thread/e523b8ade175746c

Basically, we should explain how to use zip like thus:

list_plot(zip(list of x-coords, list of y-coords))

so that people from Matlab don't get confused by the very unhelpful error message.  Maybe the error message ought to be changed too.

Issue created by migration from https://trac.sagemath.org/ticket/4985





---

archive/issue_comments_038019.json:
```json
{
    "body": "Good idea, IMHO. \nI wonder if it also a good idea to add plot_list as an alias to the namespace so people who hunt for plot commands (and the documentation for them) using tab completion can find this more easily?",
    "created_at": "2009-01-16T02:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38019",
    "user": "wdj"
}
```

Good idea, IMHO. 
I wonder if it also a good idea to add plot_list as an alias to the namespace so people who hunt for plot commands (and the documentation for them) using tab completion can find this more easily?



---

archive/issue_comments_038020.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-03-22T23:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38020",
    "user": "jhpalmieri"
}
```

Changing priority from major to minor.



---

archive/issue_comments_038021.json:
```json
{
    "body": "Here's a patch, adding to the list_plot docstring.  I feel neutral, or maybe a little negative, about the suggestion to add plot_list as an alias.  Would we then need to do the same for list_plot3d?  Anyway, that can be dealt with as a separate ticket.\n\nBy the way, I wasn't sure what \"the very unhelpful error message\" is. We might consider testing whether the second argument to list_plot (which is \"plotjoined\", should be boolean) is a list or tuple, and then print a warning, because perhaps someone ran \"list_plot([list1], [list2])\" without meaning to.  Opinions?",
    "created_at": "2009-03-22T23:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38021",
    "user": "jhpalmieri"
}
```

Here's a patch, adding to the list_plot docstring.  I feel neutral, or maybe a little negative, about the suggestion to add plot_list as an alias.  Would we then need to do the same for list_plot3d?  Anyway, that can be dealt with as a separate ticket.

By the way, I wasn't sure what "the very unhelpful error message" is. We might consider testing whether the second argument to list_plot (which is "plotjoined", should be boolean) is a list or tuple, and then print a warning, because perhaps someone ran "list_plot([list1], [list2])" without meaning to.  Opinions?



---

archive/issue_comments_038022.json:
```json
{
    "body": "Attachment\n\nNice!  Positive review.",
    "created_at": "2009-03-23T21:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38022",
    "user": "jason"
}
```

Attachment

Nice!  Positive review.



---

archive/issue_comments_038023.json:
```json
{
    "body": "(applies cleanly to 3.4, doctests in plot.py pass, and the plot looks right).",
    "created_at": "2009-03-23T21:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38023",
    "user": "jason"
}
```

(applies cleanly to 3.4, doctests in plot.py pass, and the plot looks right).



---

archive/issue_comments_038024.json:
```json
{
    "body": "#5594 is for the suggestion by jhpalmieri above.",
    "created_at": "2009-03-23T21:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38024",
    "user": "jason"
}
```

#5594 is for the suggestion by jhpalmieri above.



---

archive/issue_comments_038025.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T06:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38025",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_038026.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T06:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4985#issuecomment-38026",
    "user": "mabshoff"
}
```

Resolution: fixed
