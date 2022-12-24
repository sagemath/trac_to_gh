# Issue 1662: gnuplot issues (with something that can probably easily be made into a patch)

archive/issues_001662.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\nBackground:\nFor the analysis of some experimental data I am using sage's notebook.\nseveral functions that I have written work together to turn the input\ndatafile from a silly propitiatory program into a nice simple text\nfile of x, y and z values separated by 1 space\ne.g.\n17 17 17\n17 17 18\n17 18 19\n18 19 16\n19 16 16\n16 16 18\n16 18 18\n18 18 20\nfor that particular dataset it goes on for 668 lines in the same vein.\n\nAfter coaxing these files into existence with their nice simple\ncoordinates, I want to plot them using gnuplot. Because I know this\nworks with both the version of gnuplot I have installed on my Ubuntu\n7.10 computer and the version contained in the optional sage package.\ngnuplot creates nice interactive 3D XYZ scatter graphs using these\nfiles that have been created through the sage notebook.\nthe command: splot '/home/user/dropexp/xyz_8.txt'\ntyped at the interactive gnuplot command line causes the nice\ninteractive graph to be displayed.\nNow I want to do this from the sage notebook and I can almost do it.\nby modifying ~/bin/sage-2.8.15/devel/sage-main/sage/interfaces/\ngnuplot.py\nhttp://max.randor.googlepages.com/gnuplot.py\nhttp://max.randor.googlepages.com/gnuplot.patch\nand replacing a %s with a '%s' (This stops it doing what it normally\ndoes and _should_ make it do what I want it to do (I hope))\nI can do:\n\"\ng = Gnuplot()\ng.plot3d('/home/user/dropexp/xyz_8.txt')\n\ngnuplot> splot '/home/user/dropexp/xyz_8.txt'\n                                              ^\n        \"/home/user/.sage//temp/computer/13838//gnuplot\", line 15:\nAll points z value undefined\n\"\nhowever as you can see from: http://max.randor.googlepages.com/xyz_8.txt\nthere are z values, and exactly the same command (splot '/home/user/\ndropexp/xyz_8.txt') works when used at the gnuplot command line.\nsomewhere along the line perhaps in the options that gnuplot uses the\nz values have been removed or ignored.\nbefore I modified gnuplot.py I got an error message telling me that my\nfile was not a function, my change fixed that error to give me another\none.\nSo it does not work.\nwhich is _annoying_\n\nI was wondering if anyone has any ideas that might help?\n\nThank You\n\n---\n\nShortly after posting I worked out how to fix it myself.\nSorry.\nAs a consequence of editing the wrong file I can no be sure that the\npatch file is for the same file as sear distributes, but it is close.\n```\n\n\nhttp://max.randor.googlepages.com/gnuplot1.py\n\nhttp://max.randor.googlepages.com/gnuplot1.patch\n\n\n```\nTo make it work I just had to do a few more modifications to the\ngnuplot.py file to make it capable of taking x,y and z values.\nHurray for open source.\n\nThank you.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1662\n\n",
    "created_at": "2008-01-02T23:56:46Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gnuplot issues (with something that can probably easily be made into a patch)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1662",
    "user": "was"
}
```
Assignee: was


```

Background:
For the analysis of some experimental data I am using sage's notebook.
several functions that I have written work together to turn the input
datafile from a silly propitiatory program into a nice simple text
file of x, y and z values separated by 1 space
e.g.
17 17 17
17 17 18
17 18 19
18 19 16
19 16 16
16 16 18
16 18 18
18 18 20
for that particular dataset it goes on for 668 lines in the same vein.

After coaxing these files into existence with their nice simple
coordinates, I want to plot them using gnuplot. Because I know this
works with both the version of gnuplot I have installed on my Ubuntu
7.10 computer and the version contained in the optional sage package.
gnuplot creates nice interactive 3D XYZ scatter graphs using these
files that have been created through the sage notebook.
the command: splot '/home/user/dropexp/xyz_8.txt'
typed at the interactive gnuplot command line causes the nice
interactive graph to be displayed.
Now I want to do this from the sage notebook and I can almost do it.
by modifying ~/bin/sage-2.8.15/devel/sage-main/sage/interfaces/
gnuplot.py
http://max.randor.googlepages.com/gnuplot.py
http://max.randor.googlepages.com/gnuplot.patch
and replacing a %s with a '%s' (This stops it doing what it normally
does and _should_ make it do what I want it to do (I hope))
I can do:
"
g = Gnuplot()
g.plot3d('/home/user/dropexp/xyz_8.txt')

gnuplot> splot '/home/user/dropexp/xyz_8.txt'
                                              ^
        "/home/user/.sage//temp/computer/13838//gnuplot", line 15:
All points z value undefined
"
however as you can see from: http://max.randor.googlepages.com/xyz_8.txt
there are z values, and exactly the same command (splot '/home/user/
dropexp/xyz_8.txt') works when used at the gnuplot command line.
somewhere along the line perhaps in the options that gnuplot uses the
z values have been removed or ignored.
before I modified gnuplot.py I got an error message telling me that my
file was not a function, my change fixed that error to give me another
one.
So it does not work.
which is _annoying_

I was wondering if anyone has any ideas that might help?

Thank You

---

Shortly after posting I worked out how to fix it myself.
Sorry.
As a consequence of editing the wrong file I can no be sure that the
patch file is for the same file as sear distributes, but it is close.
```


http://max.randor.googlepages.com/gnuplot1.py

http://max.randor.googlepages.com/gnuplot1.patch


```
To make it work I just had to do a few more modifications to the
gnuplot.py file to make it capable of taking x,y and z values.
Hurray for open source.

Thank you.
```


Issue created by migration from https://trac.sagemath.org/ticket/1662





---

archive/issue_comments_010561.json:
```json
{
    "body": "More reply from Max Randor:\n\t\n\nDon't use the changes I made, something much cleverer is needed to\nactually fix it, my changes break what worked to make what I wanted to\nwork work. So it plots 3D datafiles, but not 3D functions.\nThe function needs to decide whether it is a datafile or a function\n(or perhaps an array or something else) and do different things\ndepending on what it is passed.",
    "created_at": "2008-01-03T11:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1662#issuecomment-10561",
    "user": "wdj"
}
```

More reply from Max Randor:
	

Don't use the changes I made, something much cleverer is needed to
actually fix it, my changes break what worked to make what I wanted to
work work. So it plots 3D datafiles, but not 3D functions.
The function needs to decide whether it is a datafile or a function
(or perhaps an array or something else) and do different things
depending on what it is passed.



---

archive/issue_comments_010562.json:
```json
{
    "body": "\n```\n\nDon't use the changes I made, something much cleverer is needed to\nactually fix it, my changes break what worked to make what I wanted to\nwork work. So it plots 3D datafiles, but not 3D functions.\nThe function needs to decide whether it is a datafile or a function\n(or perhaps an array or something else) and do different things\ndepending on what it is passed.\n```\n",
    "created_at": "2008-01-04T09:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1662#issuecomment-10562",
    "user": "was"
}
```


```

Don't use the changes I made, something much cleverer is needed to
actually fix it, my changes break what worked to make what I wanted to
work work. So it plots 3D datafiles, but not 3D functions.
The function needs to decide whether it is a datafile or a function
(or perhaps an array or something else) and do different things
depending on what it is passed.
```




---

archive/issue_comments_010563.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-20T04:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1662#issuecomment-10563",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_010564.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-06-20T08:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1662#issuecomment-10564",
    "user": "was"
}
```

Resolution: invalid



---

archive/issue_comments_010565.json:
```json
{
    "body": "gnuplot is no longer included in sage, and I have no interest in supporting it now that sage has much\nbetter 3d graphics.  Also, this patch doesn't work.",
    "created_at": "2008-06-20T08:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1662#issuecomment-10565",
    "user": "was"
}
```

gnuplot is no longer included in sage, and I have no interest in supporting it now that sage has much
better 3d graphics.  Also, this patch doesn't work.
