# Issue 5359: Block matrix viewing is broken

archive/issues_005359.json:
```json
{
    "body": "Assignee: cwitty\n\nFrom sage-support:\n\nViewing block matrices \"nicely\" seems to be difficult in Sage. \n\n```\nsage: A=matrix([[1]]) \nsage: B=matrix([[2]]) \nsage: C=matrix([[3]]) \nsage: D=matrix([[4]]) \nsage: BM=block_matrix([A,B,C,D]) \nsage: BM \n[1|2] \n[-+-] \n[3|4] \n```\n\nOkay, this is fine but a little clunky.  Let's try something nicer: \n\n```\nsage: show(BM) \n```\n\nUpon which a dvi viewer opens up, unfortunately not a very nice one... \nand shows the block matrix with only a vertical dividing line, not a \nhorizontal one! \nOkay, let's try the notebook: \n\n\n```\nA=matrix([[1]]) \nB=matrix([[2]]) \nC=matrix([[3]]) \nD=matrix([[4]]) \n\nBM=block_matrix([A,B,C,D]);BM \n\n[1|2] \n[-+-] \n[3|4] \n```\n \n\nSo far so good, but when I click \"Typeset\" to get a LaTeXed matrix... \n\n```\nBM=block_matrix([A,B,C,D]);BM \n\n<html><span class=\"math\">\\left(\\begin{array}{r|r} \n1 & 2 \\\\ \n3 & 4 \n\\end{array}\\right)</span></html> \n```\n \nWhich as you can see does NOT have any \"blockiness\" to it at all. \nVery pretty, but not a block matrix, at least not identifiably so. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5359\n\n",
    "created_at": "2009-02-24T17:55:14Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "Block matrix viewing is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5359",
    "user": "kcrisman"
}
```
Assignee: cwitty

From sage-support:

Viewing block matrices "nicely" seems to be difficult in Sage. 

```
sage: A=matrix([[1]]) 
sage: B=matrix([[2]]) 
sage: C=matrix([[3]]) 
sage: D=matrix([[4]]) 
sage: BM=block_matrix([A,B,C,D]) 
sage: BM 
[1|2] 
[-+-] 
[3|4] 
```

Okay, this is fine but a little clunky.  Let's try something nicer: 

```
sage: show(BM) 
```

Upon which a dvi viewer opens up, unfortunately not a very nice one... 
and shows the block matrix with only a vertical dividing line, not a 
horizontal one! 
Okay, let's try the notebook: 


```
A=matrix([[1]]) 
B=matrix([[2]]) 
C=matrix([[3]]) 
D=matrix([[4]]) 

BM=block_matrix([A,B,C,D]);BM 

[1|2] 
[-+-] 
[3|4] 
```
 

So far so good, but when I click "Typeset" to get a LaTeXed matrix... 

```
BM=block_matrix([A,B,C,D]);BM 

<html><span class="math">\left(\begin{array}{r|r} 
1 & 2 \\ 
3 & 4 
\end{array}\right)</span></html> 
```
 
Which as you can see does NOT have any "blockiness" to it at all. 
Very pretty, but not a block matrix, at least not identifiably so. 

Issue created by migration from https://trac.sagemath.org/ticket/5359





---

archive/issue_comments_041288.json:
```json
{
    "body": "I think this is partly a bug and partly a defect in jsmath: the `_latex_` method for matrices completely ignores any subdivisions in the rows, and this is a bug. The right way to do this would be to add `\\hline` between the rows where you want lines, but jsmath doesn't seem to support this command.  It also seems to ignore the vertical line specifier in the array argument.\n\nSo I know how to fix this so that it works from the command line, but not from the notebook.  I'll attach a patch.\n\nAny ideas on what to do in the notebook?",
    "created_at": "2009-02-24T19:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41288",
    "user": "jhpalmieri"
}
```

I think this is partly a bug and partly a defect in jsmath: the `_latex_` method for matrices completely ignores any subdivisions in the rows, and this is a bug. The right way to do this would be to add `\hline` between the rows where you want lines, but jsmath doesn't seem to support this command.  It also seems to ignore the vertical line specifier in the array argument.

So I know how to fix this so that it works from the command line, but not from the notebook.  I'll attach a patch.

Any ideas on what to do in the notebook?



---

archive/issue_comments_041289.json:
```json
{
    "body": "Attachment [5359.patch](tarball://root/attachments/some-uuid/ticket5359/5359.patch) by jhpalmieri created at 2009-02-24 20:00:18\n\n(will have to be rebased against sage 3.4)",
    "created_at": "2009-02-24T20:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41289",
    "user": "jhpalmieri"
}
```

Attachment [5359.patch](tarball://root/attachments/some-uuid/ticket5359/5359.patch) by jhpalmieri created at 2009-02-24 20:00:18

(will have to be rebased against sage 3.4)



---

archive/issue_comments_041290.json:
```json
{
    "body": "I won't be able to review this in the near future but if it works this seems appropriate.  \n\nAccording to the jsmath future features page, [http://www.math.union.edu/~dpvc/jsMath/future.html](http://www.math.union.edu/~dpvc/jsMath/future.html), one of the future goals is \n\n```\nAdd more control over entries in arrays and matrices (something like the array option control provided by WebTeX)\n```\n\nso perhaps this ticket should be closed once the command line piece is given a positive review, and then a new ticket opened and/or a report sent to the jsmath author.  In any case we should at least have Sage as one of the sites using jsmath on his gallery!  \n\nThere *is* an example of a pseudo-block matrix in his examples section, [http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html](http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html) Exercise 18.42.  I don't know if that would be a satisfactory solution, though.",
    "created_at": "2009-02-25T01:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41290",
    "user": "kcrisman"
}
```

I won't be able to review this in the near future but if it works this seems appropriate.  

According to the jsmath future features page, [http://www.math.union.edu/~dpvc/jsMath/future.html](http://www.math.union.edu/~dpvc/jsMath/future.html), one of the future goals is 

```
Add more control over entries in arrays and matrices (something like the array option control provided by WebTeX)
```

so perhaps this ticket should be closed once the command line piece is given a positive review, and then a new ticket opened and/or a report sent to the jsmath author.  In any case we should at least have Sage as one of the sites using jsmath on his gallery!  

There *is* an example of a pseudo-block matrix in his examples section, [http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html](http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html) Exercise 18.42.  I don't know if that would be a satisfactory solution, though.



---

archive/issue_comments_041291.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n\n> There *is* an example of a pseudo-block matrix in his examples section, \n> [http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html](http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html) Exercise 18.42.  I \n> don't know if that would be a satisfactory solution, though.\n\nI don't know if it is satisfactory, either, but I couldn't come up with anything better, so I've implemented this for the notebook version.  This ignores repeated subdivisions, because I couldn't come up with a good way to display them: in the notebook, if you do\n\n```\nB = matrix(2,2)\nB.subdivide([1], [])\nC = matrix(2,2)\nC.subdivide([1,1], [])\n```\n\nthen B and C will be typeset identically.  The command-line versions look different, though.",
    "created_at": "2009-02-25T20:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41291",
    "user": "jhpalmieri"
}
```

Replying to [comment:2 kcrisman]:

> There *is* an example of a pseudo-block matrix in his examples section, 
> [http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html](http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html) Exercise 18.42.  I 
> don't know if that would be a satisfactory solution, though.

I don't know if it is satisfactory, either, but I couldn't come up with anything better, so I've implemented this for the notebook version.  This ignores repeated subdivisions, because I couldn't come up with a good way to display them: in the notebook, if you do

```
B = matrix(2,2)
B.subdivide([1], [])
C = matrix(2,2)
C.subdivide([1,1], [])
```

then B and C will be typeset identically.  The command-line versions look different, though.



---

archive/issue_comments_041292.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-05T20:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41292",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041293.json:
```json
{
    "body": "Changing assignee from cwitty to jhpalmieri.",
    "created_at": "2009-03-05T20:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41293",
    "user": "jhpalmieri"
}
```

Changing assignee from cwitty to jhpalmieri.



---

archive/issue_comments_041294.json:
```json
{
    "body": "rebased against 3.4; apply only this patch",
    "created_at": "2009-03-12T21:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41294",
    "user": "jhpalmieri"
}
```

rebased against 3.4; apply only this patch



---

archive/issue_comments_041295.json:
```json
{
    "body": "Attachment [5359-new.patch](tarball://root/attachments/some-uuid/ticket5359/5359-new.patch) by robertwb created at 2009-03-16 23:56:43\n\nI think your solution for block matrices in the notebook is a good idea, at least until jsmath supports the standard way.",
    "created_at": "2009-03-16T23:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41295",
    "user": "robertwb"
}
```

Attachment [5359-new.patch](tarball://root/attachments/some-uuid/ticket5359/5359-new.patch) by robertwb created at 2009-03-16 23:56:43

I think your solution for block matrices in the notebook is a good idea, at least until jsmath supports the standard way.



---

archive/issue_comments_041296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T08:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41296",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041297.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T08:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5359#issuecomment-41297",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
