# Issue 712: SAGE/Maxima is sometimes unable to solve a linear system

Issue created by migration from https://trac.sagemath.org/ticket/712

Original creator: janwil

Original creation time: 2007-09-20 18:20:04

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


---

Attachment

replicates bug in Maxima


---

Comment by was created at 2007-09-20 18:52:33

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

Comment by was created at 2007-09-20 19:14:13

this actually reproduces the bug


---

Attachment


---

Comment by was created at 2008-01-19 13:30:13

Resolution: fixed


---

Comment by was created at 2008-01-19 13:30:13

This is very very likely fix by #1827, and testing this in Sage-2.10 it works fine on my test systems.  I'm closing this unless somebody can replicate it. 

NOTE -- the attachments j and maxima_bug I put above are irrelevant and pointless -- they just illustrate that maxima's Solve has lame error messages when given crappy input.
