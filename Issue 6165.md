# Issue 6165: new maxima spkg that enhances eigenvector results so they can be useable from symbolics

Issue created by migration from https://trac.sagemath.org/ticket/6165

Original creator: jason

Original creation time: 2009-05-31 04:35:49

Assignee: mabshoff

CC:  mhansen mvngu

The spkg applies the patch given by Robert Dodier in this thread: http://www.math.utexas.edu/pipermail/maxima/2009/017242.html

Basically, it makes Maxima return eigenvectors associated with each eigenvalue separately, rather than just returning a list of eigenvectors.  It makes it possible to determine the eigenvector associated with an eigenvalue when algebraic multiplicities do not match up with geometric multiplicities.  See the mailing list thread above for an example.

The new spkg is here: http://sage.math.washington.edu/home/jason/maxima-5.16.3.p3.spkg


---

Comment by jason created at 2009-05-31 04:41:07

The reason for this is to make it trivial to have eigenvector and eigenmatrix functions for symbolic matrices.


---

Comment by was created at 2009-05-31 05:03:51


```
21:59 < wstein> wstein@sage:~/tmp/maxima-5.16.3.p3$ hg status
21:59 < wstein> ? patches/eigen.mac
21:59 < wstein> yep, that pynac segfault looks *very* serious.
21:59 < wstein> ouch.
21:59 < jason> oh, grr, I forgot to add that file.
21:59 < wstein> but it is inevitable.
21:59 < jason> hang on.
22:00 < jason> it'd be nice if -spkg ran hg status and reported any funny things.
22:01 < wstein> good idea.  implement it and send me a patch.
22:01 < wstein> it's easy.
22:01 < jason> yeah, I know.
22:02 < wstein> my only concern about 6165 -- is this going to be upstreamed to maxima?
22:02 < wstein> i.e., or have you just made it so for the first time ever when debian sage tries to use the systemwide maxima
22:02 < wstein> it'll just totally break no matter what forever when doing eigenvectors.
22:02 < wstein> Just curious.
22:02 < wstein> As long as robert dodier is putting that patch into maxima, no prob.
22:03 < wstein> but he doesn't say so in the thread as far as I can tell.
```



---

Comment by was created at 2009-05-31 05:05:30

Positive review pending a statement from Dodier on this.


---

Comment by jason created at 2009-05-31 05:08:20

I've posted a reply to the thread mentioned above asking that the patch be included in maxima.  I'll check on this later.


---

Comment by AlexGhitza created at 2009-08-24 09:28:19

Jason, I think this has now been integrated in Maxima 5.19.1.  You can have a look at #6699 to double-check.


---

Comment by kcrisman created at 2009-09-15 13:34:28

Replying to [comment:6 AlexGhitza]:
> Jason, I think this has now been integrated in Maxima 5.19.1.  You can have a look at #6699 to double-check.

Yes, this is the case:

```
Maxima 5.19.1 http://maxima.sourceforge.netUsing Lisp SBCL 1.0.30Distributed under the GNU Public License. See the file COPYING.Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) M1 : matrix ([0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]);
                                [ 0  1  0  0 ]
                                [            ]
                                [ 0  0  0  0 ]
(%o1)                           [            ]
                                [ 0  0  2  0 ]
                                [            ]
                                [ 0  0  0  2 ]
(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[0, 2], [2, 2]], [[[1, 0, 0, 0]], [[0, 0, 1, 0], [0, 0, 0, 1]]]]
(%i3) for i thru length (vals) do disp (val[i] = vals[i][1], mult[i] =
vals[i][2], vec[i] = vecs[i]);
                                   val  = 0
                                      1

                                   mult  = 2
                                       1

                             vec  = [[1, 0, 0, 0]]
                                1

                                   val  = 2
                                      2

                                   mult  = 2
                                       2

                      vec  = [[0, 0, 1, 0], [0, 0, 0, 1]]
                         2

(%o3)                                done
```



---

Comment by jason created at 2009-09-25 06:00:43

From the above comments, it sounds like this ticket can be closed, as it has been superseded.


---

Comment by mvngu created at 2009-09-25 06:04:14

Closing this ticket as a duplicate of #6699.


---

Comment by mvngu created at 2009-09-25 06:04:14

Resolution: duplicate
