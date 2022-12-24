# Issue 7232: fix tachyon segfault introduced by #6542

archive/issues_007232.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mhampton @nilesjohnson\n\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7232\n\n",
    "created_at": "2009-10-16T03:40:38Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "fix tachyon segfault introduced by #6542",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7232",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  mhampton @nilesjohnson


```

Issue created by migration from https://trac.sagemath.org/ticket/7232





---

archive/issue_comments_059981.json:
```json
{
    "body": "\n```\n\n\nOn Thu, Oct 15, 2009 at 7:59 PM, Elliott <elliottbrossard@gmail.com> wrote:\n>\n> Hello, I was going to use sagenb.org today to verify a plot for my\n> math homework, but I kept getting segmentation faults for some odd\n> (and rather scary) reason. I made a mistake and used \"typeof\" instead\n> of \"type\" and got\n>\n> typeof((1, 2, 3))\n> ///\n> Traceback (most recent call last):\n>  File \"<stdin>\", line 1, in <module>\n>  File \"_sage_input_5.py\", line 4, in <module>\n>    _sage_const_3 = Integer(3); _sage_const_2 = Integer(2);\n> _sage_const_1 = Integer(1)\n> NameError: name 'Integer' is not defined\n>\n> Then I tried \"type?\" and got a segmentation fault, which does not\n> appear in the log. Trying again gave me the same segfault. Also, I\n> became unable to evaluate 1 + 1:\n>\n> 1 + 1\n> ///\n> Traceback (most recent call last):\n>  File \"<stdin>\", line 1, in <module>\n>  File \"_sage_input_2.py\", line 6, in <module>\n>    _sage_const_1 = Integer(1)\n> NameError: name 'Integer' is not defined\n>\n> I logged out and then logged back in, same issue with segfaulting and\n> names being undefined. Just now (a few hours later) I logged in, but\n> could not reproduce the error. \n\nI was upgrading Sage on sagenb.org to the new version (sage-4.1.2)., which took about an hour today.  Unfortunately, I didn't do the rather complicated dance of upgrading a different install, shutting down sagenb.org, starting it with the other install, etc.   This meant that sagenb.org was unstable for about 30 minutes. \n\n> However, when I try to plot the 3D\n> parametric function I was going to plot earlier, I get a less verbose\n> segfault, but one that does show up in the log.\n\n>\n> a = 1\n> b = 0\n> c = 0\n>\n> f = lambda t: ((a*c*cos(t) - b*sin(t))/sqrt(a^2+b^2), (b*c*cos(t) +\n> a*sin(t))/sqrt(a^2+b^2), cos(t)*sqrt(a^2+b^2))\n> t = Tachyon(camera_center=(0,0,0))\n> t.texture('t')\n> t.light((-20,-20,40), 0.2, (1,1,1))\n> t.parametric_plot(f,0,2*pi,'t',min_depth=6)\n>\n> t.show()\n> ///\n> Segmentation fault\n\nThis is not Sage segfaulting but the Tachyon subprocess.\nI.e., the Sage process is not segfaulting.  It is running the Tachyon ray tracer on a certain input file, and that ray tracer is crashing.  \n    \nAs a workaround, you can use Sage's own parametric_plot command instead of using the Tachyon object: \n\na = 1; b = 0; c = 0\nvar('t')\n\nf = ((a*c*cos(t) - b*sin(t))/sqrt(a^2+b^2), \n     (b*c*cos(t) + a*sin(t))/sqrt(a^2+b^2), cos(t)*sqrt(a^2+b^2))\n\nparametric_plot(f, (t,0,2*pi))\n\nIf you want it rendered with Tachyon, you can do:\n\nparametric_plot(f, (t,0,2*pi), viewer='tachyon')\n\nRegarding the Tachyon segfault, it's not special to the notebook -- it happens on my other Sage installs and even happens on OS X:\n...\nsage: t.show()\nsh: line 1:  2106 Segmentation fault      tachyon /Users/wstein/.sage//temp/flat.local/2053//tmp_2.dat -format PNG -o /Users/wstein/.sage//temp/flat.local/2053//tmp_1.png > /dev/null\n\nThis is a bug that was introduced in the Sage-4.1 --> Sage-4.1.1 release cycle (so 2-3 months ago).   It doesn't happen in sage-4.1, but it does in sage-4.1.1.   The Tachyon spkg \n\n   tachyon-0.98beta.p9.spkg\n\nis the same in all cases, so the problem must be with the input that is being sent to Tachyon.   Indeed, the script being fed into Tachyon is totally different in sage-4.1.1 than in sage-4.1. Diffing them:\n\n< = \"old one that worked\" and > = \"new one\":\n\n<               center None\n<               viewdir None\n<               updir None\n---\n>               center  0.0 0.0 0.0 \n>               viewdir  0.0 0.0 0.0 \n>               updir  0.0 0.0 1.0 \n20c20\n<         color None texfunc 0\n---\n>         color  1.0 0.0 0.5  texfunc 0\n23c23\n<         light center None\n---\n>         light center  -20.0 -20.0 40.0 \n25c25\n<               color None\n---\n>               color  1.0 1.0 1.0 \n28c28\n<         sphere center None rad 0.1 t\n---\n>         sphere center  0.0 0.0 1.0  rad 0.1 t\n\n...\n\nChecking trac we find ticket #6542 (http://trac.sagemath.org/sage_trac/ticket/6542) which has a ticket with basically a 1-line patch by Marshall Hampton refereed by Tim Dumol that introduced these changes. \n\nSo, Marshall -- I hope you will fix that you broken Sage's Tachyon ASAP. \nAnd Elliott, you get a chocolate for finding and reporting a bug!  :-)\n```\n",
    "created_at": "2009-10-16T03:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59981",
    "user": "@williamstein"
}
```


```


On Thu, Oct 15, 2009 at 7:59 PM, Elliott <elliottbrossard@gmail.com> wrote:
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

archive/issue_comments_059982.json:
```json
{
    "body": "(Still) Reproducible with Sage 5.8.beta3... :-)",
    "created_at": "2013-03-07T23:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59982",
    "user": "@nexttime"
}
```

(Still) Reproducible with Sage 5.8.beta3... :-)



---

archive/issue_comments_059983.json:
```json
{
    "body": "Interestingly, it segfaults *after* having read the whole input file (and also with just one thread):\n\n```sh\n\n(sage-sh) $ tachyon tachyon-example.dat +V -numthreads 1 -format PNG -o tachyon-example.png\nTachyon Parallel/Multiprocessor Ray Tracer   Version 0.98.9   \nCopyright 1994-2010,    John E. Stone <john.stone@gmail.com> \n------------------------------------------------------------ \nScene Parsing Time:     0.0052 seconds\nCPU Information:\n  Node    0:  2 CPUs, CPU Speed 1.00, Node Speed   2.00 Name: sleepless\n  Total CPUs: 2\n  Total Speed: 2.000000\n\nScene contains 514 objects.\nGlobal bounds: -0.1 -1.1 -1.1 -> 0.1 1.1 1.1\nCreating top level grid: X:12 Y:12 Z:12\nGrid:  X: 12  Y: 12  Z: 12  Cells:     1728  Obj:      513  Obj/Cell:   0.297\nScene contains 1 non-gridded objects\n\nAllocating Image Buffer.\nPreprocessing Time:     0.0088 seconds\nSegmentation fault:         0% complete            \n```\n\n\n(But the segfault actually completes. ;-) )",
    "created_at": "2013-03-08T01:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59983",
    "user": "@nexttime"
}
```

Interestingly, it segfaults *after* having read the whole input file (and also with just one thread):

```sh

(sage-sh) $ tachyon tachyon-example.dat +V -numthreads 1 -format PNG -o tachyon-example.png
Tachyon Parallel/Multiprocessor Ray Tracer   Version 0.98.9   
Copyright 1994-2010,    John E. Stone <john.stone@gmail.com> 
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

archive/issue_comments_059984.json:
```json
{
    "body": "Attachment [tachyon-example.dat](tarball://root/attachments/some-uuid/ticket7232/tachyon-example.dat) by @nexttime created at 2013-03-08 01:47:05\n\nTachyon input file for the example given in the ticket's description.  (Plain text)",
    "created_at": "2013-03-08T01:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59984",
    "user": "@nexttime"
}
```

Attachment [tachyon-example.dat](tarball://root/attachments/some-uuid/ticket7232/tachyon-example.dat) by @nexttime created at 2013-03-08 01:47:05

Tachyon input file for the example given in the ticket's description.  (Plain text)



---

archive/issue_comments_059985.json:
```json
{
    "body": "Attachment [tachyon-doctest.490.dat](tarball://root/attachments/some-uuid/ticket7232/tachyon-doctest.490.dat) by @nexttime created at 2013-03-08 07:51:06\n\nTachyon input file generated by the example in `sage/plot/plot3d/tachyon.py`, around line 490 (as of Sage 5.8.beta3).  (Plain text)",
    "created_at": "2013-03-08T07:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59985",
    "user": "@nexttime"
}
```

Attachment [tachyon-doctest.490.dat](tarball://root/attachments/some-uuid/ticket7232/tachyon-doctest.490.dat) by @nexttime created at 2013-03-08 07:51:06

Tachyon input file generated by the example in `sage/plot/plot3d/tachyon.py`, around line 490 (as of Sage 5.8.beta3).  (Plain text)



---

archive/issue_comments_059986.json:
```json
{
    "body": "Tachyon seems to bomb out on the original example in the limit as camera_center->(0,0,0). Then, from tachyon.py viewdir=(0,0,0), which may not make sense; although on other examples I've tried when camera_center and viewdir are the zero vector then Tachyon returns an empty image. For the given example using\n\n```\nt = Tachyon(camera_center=(1.e-30,1.e-30,1.e-30))\n```\n\ndoes give, a not very interesting, image. How small vector_center can be and not cause Tachyon to bomb out my be hardware/software specific. With\n\n```\nt = Tachyon(camera_center=(-3,3,0))\n```\n\nI get an image similar to the parametric_plot() output. This sounds like a Tachyon bug.",
    "created_at": "2013-03-13T02:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59986",
    "user": "@strogdon"
}
```

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

archive/issue_comments_059987.json:
```json
{
    "body": "Just built Sage 5.8.rc0 on a Linux x86 box (Pentium4 Prescott, GCC 4.7.2), and there testing `sage/interfaces/tachyon.py` doesn't give a (silent) segfault, but instead:\n\n\n```\nTachyon Parallel/Multiprocessor Ray Tracer   Version 0.98.9\nCopyright 1994-2010,    John E. Stone <john.stone@gmail.com>\n------------------------------------------------------------\nScene Parsing Time:     0.0002 seconds\nScene contains 1 objects.\nPreprocessing Time:     0.0000 seconds\nRendering Progress:       100% complete\n  Ray Tracing Time:     0.0523 seconds\nwritetgaregion: file ptr out of range!!!\n\n    Image I/O Time:     0.0036 seconds\n```\n\n\n(One only sees this with `--verbose`.)",
    "created_at": "2013-03-15T04:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59987",
    "user": "@nexttime"
}
```

Just built Sage 5.8.rc0 on a Linux x86 box (Pentium4 Prescott, GCC 4.7.2), and there testing `sage/interfaces/tachyon.py` doesn't give a (silent) segfault, but instead:


```
Tachyon Parallel/Multiprocessor Ray Tracer   Version 0.98.9
Copyright 1994-2010,    John E. Stone <john.stone@gmail.com>
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

archive/issue_comments_059988.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> Just built Sage 5.8.rc0 on a Linux x86 box (Pentium4 Prescott, GCC 4.7.2), and there testing `sage/interfaces/tachyon.py` doesn't give a (silent) segfault, but [...]\n\nOoops, perhaps more importantly, verbosely testing `sage/plot/plot3d/tachyon.py` doesn't show any errors.",
    "created_at": "2013-03-15T04:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59988",
    "user": "@nexttime"
}
```

Replying to [comment:6 leif]:
> Just built Sage 5.8.rc0 on a Linux x86 box (Pentium4 Prescott, GCC 4.7.2), and there testing `sage/interfaces/tachyon.py` doesn't give a (silent) segfault, but [...]

Ooops, perhaps more importantly, verbosely testing `sage/plot/plot3d/tachyon.py` doesn't show any errors.



---

archive/issue_comments_059989.json:
```json
{
    "body": "... after 75+ minutes CPU time, this Tachyon is still at 0% rendering progress for the example from the description ... 8-/",
    "created_at": "2013-03-15T06:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59989",
    "user": "@nexttime"
}
```

... after 75+ minutes CPU time, this Tachyon is still at 0% rendering progress for the example from the description ... 8-/



---

archive/issue_comments_059990.json:
```json
{
    "body": "... while [attachment:tachyon-doctest.490.dat the example from the doctest] renders quick and well.",
    "created_at": "2013-03-15T06:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59990",
    "user": "@nexttime"
}
```

... while [attachment:tachyon-doctest.490.dat the example from the doctest] renders quick and well.



---

archive/issue_comments_059991.json:
```json
{
    "body": "Changing keywords from \"\" to \"tachyon\".",
    "created_at": "2014-07-25T14:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59991",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "tachyon".



---

archive/issue_comments_059992.json:
```json
{
    "body": "Here is a proposal, that simply check that the camera is not looking at itself.\n\nThis should be applied after #16226 (maybe it will need rebasing).\n----\nNew commits:",
    "created_at": "2014-08-02T20:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59992",
    "user": "@fchapoton"
}
```

Here is a proposal, that simply check that the camera is not looking at itself.

This should be applied after #16226 (maybe it will need rebasing).
----
New commits:



---

archive/issue_comments_059993.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-03T17:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59993",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059994.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-10T11:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59994",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_059995.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-10T11:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59995",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_059996.json:
```json
{
    "body": "I think this is a reasonably way to handle this given how long it's been, and a good doctest, but a brief reminder here about what the *default* camera center and look at are might be helpful.",
    "created_at": "2014-08-14T17:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59996",
    "user": "@kcrisman"
}
```

I think this is a reasonably way to handle this given how long it's been, and a good doctest, but a brief reminder here about what the *default* camera center and look at are might be helpful.



---

archive/issue_comments_059997.json:
```json
{
    "body": "Replying to [comment:20 kcrisman]:\n> I think this is a reasonably way to handle this given how long it's been, and a good doctest, but a brief reminder here about what the *default* camera center and look at are might be helpful.\n\nActually, I think I like the error message better the way it is.  Listing the defaults will be hard to maintain (in the unlikely case that they change later), unless we print them from some attribute.  But that makes printing the error depend on successfully determining the value of the attribute, making it slower and more prone to error itself.  I think the error message currently gives all the necessary information with a minimum of overhead and complication.\n\nMaybe as a compromise, if necessary, print \"see init method for default values\"  ?",
    "created_at": "2014-08-14T17:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59997",
    "user": "@nilesjohnson"
}
```

Replying to [comment:20 kcrisman]:
> I think this is a reasonably way to handle this given how long it's been, and a good doctest, but a brief reminder here about what the *default* camera center and look at are might be helpful.

Actually, I think I like the error message better the way it is.  Listing the defaults will be hard to maintain (in the unlikely case that they change later), unless we print them from some attribute.  But that makes printing the error depend on successfully determining the value of the attribute, making it slower and more prone to error itself.  I think the error message currently gives all the necessary information with a minimum of overhead and complication.

Maybe as a compromise, if necessary, print "see init method for default values"  ?



---

archive/issue_comments_059998.json:
```json
{
    "body": "> Actually, I think I like the error message better the way it is.  Listing the defaults will be hard to maintain (in the unlikely case that they change later), unless we print them from some attribute.  But that makes printing the error depend on successfully determining the value of the attribute, making it slower and more prone to error itself.  I think the error message currently gives all the necessary information with a minimum of overhead and complication.\nFair enough, okay.\n> Maybe as a compromise, if necessary, print \"see init method for default values\"  ?\nWell, it's actually in the `Tachyon?` documentation, not even just init, so I think then you've convinced me this is fine.",
    "created_at": "2014-08-15T03:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59998",
    "user": "@kcrisman"
}
```

> Actually, I think I like the error message better the way it is.  Listing the defaults will be hard to maintain (in the unlikely case that they change later), unless we print them from some attribute.  But that makes printing the error depend on successfully determining the value of the attribute, making it slower and more prone to error itself.  I think the error message currently gives all the necessary information with a minimum of overhead and complication.
Fair enough, okay.
> Maybe as a compromise, if necessary, print "see init method for default values"  ?
Well, it's actually in the `Tachyon?` documentation, not even just init, so I think then you've convinced me this is fine.



---

archive/issue_comments_059999.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-15T03:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-59999",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-16T07:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7232#issuecomment-60000",
    "user": "@vbraun"
}
```

Resolution: fixed
