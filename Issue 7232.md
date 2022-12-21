# Issue 7232: fix tachyon segfault introduced by #6542

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-16 03:40:38

Assignee: was

CC:  mhampton niles


```


---

Comment by was created at 2009-10-16 03:41:51


```


On Thu, Oct 15, 2009 at 7:59 PM, Elliott <elliottbrossard`@`gmail.com> wrote:
>
> Hello, I was going to use sagenb.org today to verify a plot for my
> math homework, but I kept getting segmentation faults for some odd
> (and rather scary) reason. I made a mistake and used "typeof" instead
> of "type" and got
>
> typeof((1, 2, 3))
> ///
> Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>  File "_sage_input_5.py", line 4, in <module>
>    _sage_const_3 = Integer(3); _sage_const_2 = Integer(2);
> _sage_const_1 = Integer(1)
> NameError: name 'Integer' is not defined
>
> Then I tried "type?" and got a segmentation fault, which does not
> appear in the log. Trying again gave me the same segfault. Also, I
> became unable to evaluate 1 + 1:
>
> 1 + 1
> ///
> Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>  File "_sage_input_2.py", line 6, in <module>
>    _sage_const_1 = Integer(1)
> NameError: name 'Integer' is not defined
>
> I logged out and then logged back in, same issue with segfaulting and
> names being undefined. Just now (a few hours later) I logged in, but
> could not reproduce the error. 

I was upgrading Sage on sagenb.org to the new version (sage-4.1.2)., which took about an hour today.  Unfortunately, I didn't do the rather complicated dance of upgrading a different install, shutting down sagenb.org, starting it with the other install, etc.   This meant that sagenb.org was unstable for about 30 minutes. 

> However, when I try to plot the 3D
> parametric function I was going to plot earlier, I get a less verbose
> segfault, but one that does show up in the log.

>
> a = 1
> b = 0
> c = 0
>
> f = lambda t: ((a*c*cos(t) - b*sin(t))/sqrt(a^2+b^2), (b*c*cos(t) +
> a*sin(t))/sqrt(a^2+b^2), cos(t)*sqrt(a^2+b^2))
> t = Tachyon(camera_center=(0,0,0))
> t.texture('t')
> t.light((-20,-20,40), 0.2, (1,1,1))
> t.parametric_plot(f,0,2*pi,'t',min_depth=6)
>
> t.show()
> ///
> Segmentation fault

This is not Sage segfaulting but the Tachyon subprocess.
I.e., the Sage process is not segfaulting.  It is running the Tachyon ray tracer on a certain input file, and that ray tracer is crashing.  
    
As a workaround, you can use Sage's own parametric_plot command instead of using the Tachyon object: 

a = 1; b = 0; c = 0
var('t')

f = ((a*c*cos(t) - b*sin(t))/sqrt(a^2+b^2), 
     (b*c*cos(t) + a*sin(t))/sqrt(a^2+b^2), cos(t)*sqrt(a^2+b^2))

parametric_plot(f, (t,0,2*pi))

If you want it rendered with Tachyon, you can do:

parametric_plot(f, (t,0,2*pi), viewer='tachyon')

Regarding the Tachyon segfault, it's not special to the notebook -- it happens on my other Sage installs and even happens on OS X:
...
sage: t.show()
sh: line 1:  2106 Segmentation fault      tachyon /Users/wstein/.sage//temp/flat.local/2053//tmp_2.dat -format PNG -o /Users/wstein/.sage//temp/flat.local/2053//tmp_1.png > /dev/null

This is a bug that was introduced in the Sage-4.1 --> Sage-4.1.1 release cycle (so 2-3 months ago).   It doesn't happen in sage-4.1, but it does in sage-4.1.1.   The Tachyon spkg 

   tachyon-0.98beta.p9.spkg

is the same in all cases, so the problem must be with the input that is being sent to Tachyon.   Indeed, the script being fed into Tachyon is totally different in sage-4.1.1 than in sage-4.1. Diffing them:

< = "old one that worked" and > = "new one":

<               center None
<               viewdir None
<               updir None
---
>               center  0.0 0.0 0.0 
>               viewdir  0.0 0.0 0.0 
>               updir  0.0 0.0 1.0 
20c20
<         color None texfunc 0
---
>         color  1.0 0.0 0.5  texfunc 0
23c23
<         light center None
---
>         light center  -20.0 -20.0 40.0 
25c25
<               color None
---
>               color  1.0 1.0 1.0 
28c28
<         sphere center None rad 0.1 t
---
>         sphere center  0.0 0.0 1.0  rad 0.1 t

...

Checking trac we find ticket #6542 (http://trac.sagemath.org/sage_trac/ticket/6542) which has a ticket with basically a 1-line patch by Marshall Hampton refereed by Tim Dumol that introduced these changes. 

So, Marshall -- I hope you will fix that you broken Sage's Tachyon ASAP. 
And Elliott, you get a chocolate for finding and reporting a bug!  :-)
```



---

Comment by leif created at 2013-03-07 23:13:34

(Still) Reproducible with Sage 5.8.beta3... :-)


---

Comment by leif created at 2013-03-08 01:43:13

Interestingly, it segfaults _after_ having read the whole input file (and also with just one thread):

```sh

(sage-sh) $ tachyon tachyon-example.dat +V -numthreads 1 -format PNG -o tachyon-example.png
Tachyon Parallel/Multiprocessor Ray Tracer   Version 0.98.9   
Copyright 1994-2010,    John E. Stone <john.stone`@`gmail.com> 
------------------------------------------------------------ 
Scene Parsing Time:     0.0052 seconds
CPU Information:
  Node    0:  2 CPUs, CPU Speed 1.00, Node Speed   2.00 Name: sleepless
  Total CPUs: 2
  Total Speed: 2.000000

Scene contains 514 objects.
Global bounds: -0.1 -1.1 -1.1 -> 0.1 1.1 1.1
Creating top level grid: X:12 Y:12 Z:12
Grid:  X: 12  Y: 12  Z: 12  Cells:     1728  Obj:      513  Obj/Cell:   0.297
Scene contains 1 non-gridded objects

Allocating Image Buffer.
Preprocessing Time:     0.0088 seconds
Segmentation fault:         0% complete            
```


(But the segfault actually completes. ;-) )


---

Attachment

Tachyon input file for the example given in the ticket's description.  (Plain text)


---

Attachment

Tachyon input file generated by the example in `sage/plot/plot3d/tachyon.py`, around line 490 (as of Sage 5.8.beta3).  (Plain text)


---

Comment by strogdon created at 2013-03-13 02:47:11

Tachyon seems to bomb out on the original example in the limit as camera_center->(0,0,0). Then, from tachyon.py viewdir=(0,0,0), which may not make sense; although on other examples I've tried when camera_center and viewdir are the zero vector then Tachyon returns an empty image. For the given example using

```
t = Tachyon(camera_center=(1.e-30,1.e-30,1.e-30))
```

does give, a not very interesting, image. How small vector_center can be and not cause Tachyon to bomb out my be hardware/software specific. With

```
t = Tachyon(camera_center=(-3,3,0))
```

I get an image similar to the parametric_plot() output. This sounds like a Tachyon bug.


---

Comment by leif created at 2013-03-15 04:32:28

Just built Sage 5.8.rc0 on a Linux x86 box (Pentium4 Prescott, GCC 4.7.2), and there testing `sage/interfaces/tachyon.py` doesn't give a (silent) segfault, but instead:


```
Tachyon Parallel/Multiprocessor Ray Tracer   Version 0.98.9
Copyright 1994-2010,    John E. Stone <john.stone`@`gmail.com>
------------------------------------------------------------
Scene Parsing Time:     0.0002 seconds
Scene contains 1 objects.
Preprocessing Time:     0.0000 seconds
Rendering Progress:       100% complete
  Ray Tracing Time:     0.0523 seconds
writetgaregion: file ptr out of range!!!

    Image I/O Time:     0.0036 seconds
```


(One only sees this with `--verbose`.)


---

Comment by leif created at 2013-03-15 04:52:03

Replying to [comment:6 leif]:
> Just built Sage 5.8.rc0 on a Linux x86 box (Pentium4 Prescott, GCC 4.7.2), and there testing `sage/interfaces/tachyon.py` doesn't give a (silent) segfault, but [...]

Ooops, perhaps more importantly, verbosely testing `sage/plot/plot3d/tachyon.py` doesn't show any errors.


---

Comment by leif created at 2013-03-15 06:20:31

... after 75+ minutes CPU time, this Tachyon is still at 0% rendering progress for the example from the description ... 8-/


---

Comment by leif created at 2013-03-15 06:25:25

... while [attachment:tachyon-doctest.490.dat the example from the doctest] renders quick and well.


---

Comment by chapoton created at 2014-07-25 14:28:11

Changing keywords from "" to "tachyon".


---

Comment by chapoton created at 2014-08-02 20:31:27

Here is a proposal, that simply check that the camera is not looking at itself.

This should be applied after #16226 (maybe it will need rebasing).
----
New commits:


---

Comment by chapoton created at 2014-08-03 17:00:33

Changing status from new to needs_review.


---

Comment by git created at 2014-08-10 11:16:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-10 11:18:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-08-14 17:06:43

I think this is a reasonably way to handle this given how long it's been, and a good doctest, but a brief reminder here about what the _default_ camera center and look at are might be helpful.


---

Comment by niles created at 2014-08-14 17:33:37

Replying to [comment:20 kcrisman]:
> I think this is a reasonably way to handle this given how long it's been, and a good doctest, but a brief reminder here about what the _default_ camera center and look at are might be helpful.

Actually, I think I like the error message better the way it is.  Listing the defaults will be hard to maintain (in the unlikely case that they change later), unless we print them from some attribute.  But that makes printing the error depend on successfully determining the value of the attribute, making it slower and more prone to error itself.  I think the error message currently gives all the necessary information with a minimum of overhead and complication.

Maybe as a compromise, if necessary, print "see init method for default values"  ?


---

Comment by kcrisman created at 2014-08-15 03:55:03

> Actually, I think I like the error message better the way it is.  Listing the defaults will be hard to maintain (in the unlikely case that they change later), unless we print them from some attribute.  But that makes printing the error depend on successfully determining the value of the attribute, making it slower and more prone to error itself.  I think the error message currently gives all the necessary information with a minimum of overhead and complication.
Fair enough, okay.
> Maybe as a compromise, if necessary, print "see init method for default values"  ?
Well, it's actually in the `Tachyon?` documentation, not even just init, so I think then you've convinced me this is fine.


---

Comment by kcrisman created at 2014-08-15 03:55:03

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-16 07:52:19

Resolution: fixed
