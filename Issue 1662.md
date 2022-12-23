# Issue 1662: gnuplot issues (with something that can probably easily be made into a patch)

Issue created by migration from https://trac.sagemath.org/ticket/1662

Original creator: was

Original creation time: 2008-01-02 23:56:46

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



---

Comment by wdj created at 2008-01-03 11:33:05

More reply from Max Randor:
	

Don't use the changes I made, something much cleverer is needed to
actually fix it, my changes break what worked to make what I wanted to
work work. So it plots 3D datafiles, but not 3D functions.
The function needs to decide whether it is a datafile or a function
(or perhaps an array or something else) and do different things
depending on what it is passed.


---

Comment by was created at 2008-01-04 09:47:22


```

Don't use the changes I made, something much cleverer is needed to
actually fix it, my changes break what worked to make what I wanted to
work work. So it plots 3D datafiles, but not 3D functions.
The function needs to decide whether it is a datafile or a function
(or perhaps an array or something else) and do different things
depending on what it is passed.
```



---

Comment by craigcitro created at 2008-06-20 04:37:47

Changing keywords from "" to "editor_wstein".


---

Comment by was created at 2008-06-20 08:20:53

Resolution: invalid


---

Comment by was created at 2008-06-20 08:20:53

gnuplot is no longer included in sage, and I have no interest in supporting it now that sage has much
better 3d graphics.  Also, this patch doesn't work.
