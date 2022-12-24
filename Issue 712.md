# Issue 712: SAGE/Maxima is sometimes unable to solve a linear system

archive/issues_000712.json:
```json
{
    "body": "Assignee: was\n\nI ran into a very strange behavior of SAGE. This has been last verified on 32-bit Ubuntu Linux box using SAGE 2.8.4.1 (but I first encountered it on 2.8.2). In order to reproduce it please do the following. \n\nFirst, save the following script (I used the name bary3test.sage):\n\n```\n# This script tries to compute barycentric coordinates of some points and lines.\n\n#Some routines\n\ndef line_by_2_points(point1,point2):\n    \"\"\"Finds barycentric equation of the line through two given points\"\"\"\n    m = matrix ([[x,y,z],point1,point2])\n    return m.determinant()\n\ndef intersection_of_2_lines(line1,line2):\n    \"\"\"Finds barycentric coordinates of the intersection point of 2 lines\"\"\"\n    solution = solve([x+y+z==1,line1==0,line2==0],x,y,z)[int(0)]\n    tmp_x = solution[int(0)].right()\n    tmp_y = solution[int(1)].right()\n    tmp_z = solution[int(2)].right()\n    return [tmp_x,tmp_y,tmp_z]\n\nvar ('x y z _l1 _l2 _l3')\n\n# This dictionary contains the barycentric coordinates of points and\n# equations for lines.\n\nv = {\n'.B': [0, 1, 0],\n'.C': [0, 0, 1],\n'.Y': [_l2/(2*(_l2 - _l1)), (_l3/(_l3 - _l2) - (_l1/(_l2 - _l1)))/2, - _l2/(2*(_l3 - _l2))],\n'.Z': [_l3/(2*(_l3 - _l1)), _l3/(2*(_l3 - _l2)), (-_l2/(_l3 - _l2) - (_l1/(_l3 - _l1)))/2]\n}\n\nv['_q']=line_by_2_points(v['.B'],v['.Y'])\nv['_r']=line_by_2_points(v['.C'],v['.Z']) \n```\n\n\nNext run SAGE, load this script and try to compute\n\n```\nv['.P']=intersection_of_2_lines(v['_q'],v['_r']) \n```\n\nfor several times (just by pressing the up arrow and enter in the interactive shell). On my computer, I get the correct result (which is [1/2, (_l3 - _l1)/ (2*_l3 - 2*_l2), (_l1 - _l2)/(2*_l3 - 2*_l2)]) every fifth time or so, all the other attempts result in the following error message: \n\n```\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/home/jan/install/sage-2.8.4.1-i686-Linux/<ipython console> in <module>()\n\n/home/jan/install/sage-2.8.4.1-i686-Linux/bary3test.py in intersection_of_2_lines(line1, line2)\n     13 def intersection_of_2_lines(line1,line2):\n     14     \"\"\"Finds barycentric coordinates of the intersection point of 2 lines\"\"\"\n---> 15     solution = solve([x+y+z==Integer(1),line1==Integer(0),line2==Integer(0)],x,y,z)[int(Integer(0))]\n     16     tmp_x = solution[int(Integer(0))].right()\n     17     tmp_y = solution[int(Integer(1))].right()\n\n/home/jan/install/sage-2.8.4.1-i686-Linux/local/lib/python2.5/site-packages/sage/calculus/equations.py in solve(f, *args, **kwds)\n    672             s = m.solve(args)\n    673         except:\n--> 674             raise ValueError, \"Unable to solve %s for %s\"%(f, args)\n    675         a = repr(s)\n    676         return string_to_list_of_solutions(a)\n\n<type 'exceptions.ValueError'>: Unable to solve [z + y + x == 1, -x*_l2/(2*(_l3 - _l2)) - z*_l2/(2*(_l2 - _l1)) == 0, y*_l3/(2*(_l3 - _l1)) - x*_l3/(2*(_l3 - _l2)) == 0] for (x, y, z)\n```\n\n\nThere are some known issues with communicatuin between SAGE and Maxima, but they do not explain why this error occurs only sometimes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/712\n\n",
    "created_at": "2007-09-20T18:20:04Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "SAGE/Maxima is sometimes unable to solve a linear system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/712",
    "user": "janwil"
}
```
Assignee: was

I ran into a very strange behavior of SAGE. This has been last verified on 32-bit Ubuntu Linux box using SAGE 2.8.4.1 (but I first encountered it on 2.8.2). In order to reproduce it please do the following. 

First, save the following script (I used the name bary3test.sage):

```
# This script tries to compute barycentric coordinates of some points and lines.

#Some routines

def line_by_2_points(point1,point2):
    """Finds barycentric equation of the line through two given points"""
    m = matrix ([[x,y,z],point1,point2])
    return m.determinant()

def intersection_of_2_lines(line1,line2):
    """Finds barycentric coordinates of the intersection point of 2 lines"""
    solution = solve([x+y+z==1,line1==0,line2==0],x,y,z)[int(0)]
    tmp_x = solution[int(0)].right()
    tmp_y = solution[int(1)].right()
    tmp_z = solution[int(2)].right()
    return [tmp_x,tmp_y,tmp_z]

var ('x y z _l1 _l2 _l3')

# This dictionary contains the barycentric coordinates of points and
# equations for lines.

v = {
'.B': [0, 1, 0],
'.C': [0, 0, 1],
'.Y': [_l2/(2*(_l2 - _l1)), (_l3/(_l3 - _l2) - (_l1/(_l2 - _l1)))/2, - _l2/(2*(_l3 - _l2))],
'.Z': [_l3/(2*(_l3 - _l1)), _l3/(2*(_l3 - _l2)), (-_l2/(_l3 - _l2) - (_l1/(_l3 - _l1)))/2]
}

v['_q']=line_by_2_points(v['.B'],v['.Y'])
v['_r']=line_by_2_points(v['.C'],v['.Z']) 
```


Next run SAGE, load this script and try to compute

```
v['.P']=intersection_of_2_lines(v['_q'],v['_r']) 
```

for several times (just by pressing the up arrow and enter in the interactive shell). On my computer, I get the correct result (which is [1/2, (_l3 - _l1)/ (2*_l3 - 2*_l2), (_l1 - _l2)/(2*_l3 - 2*_l2)]) every fifth time or so, all the other attempts result in the following error message: 

```
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/jan/install/sage-2.8.4.1-i686-Linux/<ipython console> in <module>()

/home/jan/install/sage-2.8.4.1-i686-Linux/bary3test.py in intersection_of_2_lines(line1, line2)
     13 def intersection_of_2_lines(line1,line2):
     14     """Finds barycentric coordinates of the intersection point of 2 lines"""
---> 15     solution = solve([x+y+z==Integer(1),line1==Integer(0),line2==Integer(0)],x,y,z)[int(Integer(0))]
     16     tmp_x = solution[int(Integer(0))].right()
     17     tmp_y = solution[int(Integer(1))].right()

/home/jan/install/sage-2.8.4.1-i686-Linux/local/lib/python2.5/site-packages/sage/calculus/equations.py in solve(f, *args, **kwds)
    672             s = m.solve(args)
    673         except:
--> 674             raise ValueError, "Unable to solve %s for %s"%(f, args)
    675         a = repr(s)
    676         return string_to_list_of_solutions(a)

<type 'exceptions.ValueError'>: Unable to solve [z + y + x == 1, -x*_l2/(2*(_l3 - _l2)) - z*_l2/(2*(_l2 - _l1)) == 0, y*_l3/(2*(_l3 - _l1)) - x*_l3/(2*(_l3 - _l2)) == 0] for (x, y, z)
```


There are some known issues with communicatuin between SAGE and Maxima, but they do not explain why this error occurs only sometimes.

Issue created by migration from https://trac.sagemath.org/ticket/712





---

archive/issue_comments_003732.json:
```json
{
    "body": "Attachment [maxima_bug](tarball://root/attachments/some-uuid/ticket712/maxima_bug) by was created at 2007-09-20 18:51:39\n\nreplicates bug in Maxima",
    "created_at": "2007-09-20T18:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/712#issuecomment-3732",
    "user": "was"
}
```

Attachment [maxima_bug](tarball://root/attachments/some-uuid/ticket712/maxima_bug) by was created at 2007-09-20 18:51:39

replicates bug in Maxima



---

archive/issue_comments_003733.json:
```json
{
    "body": "Save the attached file to disk, start maxima and \nI think this is a bug in Maxima, not Sage per se:\n\n\n```\n batchload(\"/home/was/tmp/maxima_bug\")\n;\nMaxima encountered a Lisp error:\n\n\nCAR: 1 is not a list\n\nAutomatically continuing.\nTo reenable the Lisp debugger set *debugger-hook* to nil.\n```\n",
    "created_at": "2007-09-20T18:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/712#issuecomment-3733",
    "user": "was"
}
```

Save the attached file to disk, start maxima and 
I think this is a bug in Maxima, not Sage per se:


```
 batchload("/home/was/tmp/maxima_bug")
;
Maxima encountered a Lisp error:


CAR: 1 is not a list

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
```




---

archive/issue_comments_003734.json:
```json
{
    "body": "this actually reproduces the bug",
    "created_at": "2007-09-20T19:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/712#issuecomment-3734",
    "user": "was"
}
```

this actually reproduces the bug



---

archive/issue_comments_003735.json:
```json
{
    "body": "Attachment [j](tarball://root/attachments/some-uuid/ticket712/j) by mabshoff created at 2007-12-04 14:30:20",
    "created_at": "2007-12-04T14:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/712#issuecomment-3735",
    "user": "mabshoff"
}
```

Attachment [j](tarball://root/attachments/some-uuid/ticket712/j) by mabshoff created at 2007-12-04 14:30:20



---

archive/issue_comments_003736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T13:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/712#issuecomment-3736",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_003737.json:
```json
{
    "body": "This is very very likely fix by #1827, and testing this in Sage-2.10 it works fine on my test systems.  I'm closing this unless somebody can replicate it. \n\nNOTE -- the attachments j and maxima_bug I put above are irrelevant and pointless -- they just illustrate that maxima's Solve has lame error messages when given crappy input.",
    "created_at": "2008-01-19T13:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/712#issuecomment-3737",
    "user": "was"
}
```

This is very very likely fix by #1827, and testing this in Sage-2.10 it works fine on my test systems.  I'm closing this unless somebody can replicate it. 

NOTE -- the attachments j and maxima_bug I put above are irrelevant and pointless -- they just illustrate that maxima's Solve has lame error messages when given crappy input.
