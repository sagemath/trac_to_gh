# Issue 5396: Wrapping lcalc library

Issue created by migration from https://trac.sagemath.org/ticket/5396

Original creator: rishi

Original creation time: 2009-02-27 20:29:50

Assignee: Rishi

CC:  craigcitro cremona bober mrubinst@math.uwaterloo.ca mvngu

Keywords: lcalc

I am wrapping lcalc library. It is working but still needs some work.


---

Comment by rishi created at 2009-02-27 20:30:28

Changing component from algebra to number theory.


---

Comment by mabshoff created at 2009-02-27 23:11:23

Hi Rishi,

No patch, not relevant for 3.4 ;)

Cheers,

Michael


---

Attachment


---

Comment by rishi created at 2009-08-12 15:44:26

I am attaching a lcalc library wrapper and a sage worksheet showing how to use it. It needs the latest lcalc release. Please see http://www.math.uwaterloo.ca/~mrubinst 

Copy all the include files from lcalc/include to $SAGE_ROOT/local/include . Copy the libLfunction.so from lcalc/src to $SAGE_ROOT/local/lib 
Then you can compile the wrapper. 

The attached worksheet gives examples


---

Comment by rishi created at 2009-08-12 15:52:34

I am writing some functions which will generate lcalc objects for Dirichlet L functions, Elliptic Curve L functions, Cuspform L functions, which I am putting in sage/lfunctions/lcalc.py. Please let me know if you want something specific. To see what is needed by lcalc please look at page 18 of the following paper.


---

Comment by rishi created at 2009-08-12 15:53:09

Replying to [comment:4 rishi]:
I forgot the link to paper.

http://arxiv.org/abs/math/0412181

See p.18


---

Comment by cremona created at 2009-08-23 16:47:44

I was asked to review this so took a look, but I have no idea what is going on here.  Isn't lcalc already in Sage?  Or are only some of the functions already in Sage?

What on earth does the instruction "Copy all the include files from lcalc/include to $SAGE_ROOT/local/include . Copy the libLfunction.so from lcalc/src to $SAGE_ROOT/local/lib Then you can compile the wrapper." mean?  Should that not be done when Sage is built, so is not the right thing to do to change the existing lcalc spkg in Sage (lcalc-20080205.p2) to a new spkg?  Then the reviewer should install this new experimental spkg, apply a patch, and proceed as normal.

I also do not find it helpful to attach a worksheet with examples, because I do not use the notebook and so it's just one more complication.

Because of the above I changed the tag from "needs review" to "needs work", since I do not think this is ready for review.


---

Attachment


---

Comment by rishi created at 2009-08-23 18:04:22

I have attached the spkg file. 


The lcalc in sage uses the command line version of lcalc. The lcalc library lot richer than what the command line exposes. For example, you cannot find the zeros of a Dirichlet L function or Modular form L function without writing a lcalc file in appropriate format and calling the command line version. Using this patch, it is possible to forgo the lcalc file. In fact, in one of the example, I have written a function which given a primitive Dirichlet character, generates a Lcalc object, say L



```
#This code is only for example, It will not execute
chi=DirichletGroup(5)[1]
L =dirLFuncGenerator(chi)
L.value(2+3*I) #gives value
L.find_zeros_via_N(10) # finds the first 10 zeros of this L function. (ordered by distance from real axis)
```



I will repost the code in the sage notebook again


---

Comment by rishi created at 2009-08-23 18:23:36

Here I am reproducing what the sage worksheet does.


```
sage: import sage.libs.lcalc.for_testing
sage: from sage.libs.lcalc.for_testing import *
sage: D=DirichletGroup(5)
sage: chi=D[1]
sage: chi.values()
[0, 1, zeta4, -zeta4, -1]
sage: L=dirLFuncGenerator(chi)
sage: L.find_zeros_via_N(5)

[-4.13290370521285,
 6.18357819545085,
 8.45722917442324,
 -9.44293112972852,
 -11.2828964415816]


#Following Code produces the lowest zeros of Dirichlet L functions of Cubic Characters with modulus up to 10
sage: for k in srange(3,10):
    for chi in DirichletGroup(k,CyclotomicField(3)):
        if chi.is_primitive() and chi.order()==3:
            L=dirLFuncGenerator(chi)
            print k, L.find_zeros_via_N(1)[0]
....:             
7 4.35640162473628
7 -4.35640162473628
9 -3.44409315514895
9 3.44409315514895

#Here we create a L function corresponding to Elliptic Curve and find its zeros
sage: E=EllipticCurve('11a')
sage: L=elLFuncGenerator(E)
sage: L.find_zeros_via_N(5)

[6.36261389471309,
 8.60353961929075,
 10.0355090971811,
 11.4512586103452,
 13.5686390571300]


#Another example related to Elliptic Curves

sage: E=EllipticCurve('37')
sage: L2=elLFuncGenerator(E)
sage: print L2.value(.5), L2.value(.5,derivative=1)
0 0.305999824716000 elliptic curve

```



---

Comment by cremona created at 2009-08-23 19:26:30

Thanks for the explanation.

I successfully installed the new lcalc spkg;  then I successfully applied the patch and rebuilt sage.

Now testing sage/libs/lcalc gives this:

```
sage -t  "devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx"
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 411:
    sage: L.value(.6)
Expected:
    0.274633355856348 - 6.59869267328213e-18*I
Got:
    0.274633355856341 - 6.59869267328188e-18*I
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 413:
    sage: L.value(.6+1*I)
Expected:
    0.362258705721100 + 0.433888250620852*I
Got:
    0.362258705721102 + 0.433888250620855*I
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 450:
    sage: L.find_zeros(1,15,.1)
Expected:
    [6.64845334472771, 9.83144443288668, 11.9588456260835]
Got:
    [6.64845334472771, 9.83144443288667, 11.9588456260835]
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 491:
    sage: L.find_zeros_via_N(3)
Expected:
    [6.64845334472771, 9.83144443288668, 11.9588456260835]
Got:
    [6.64845334472772, 9.83144443288667, 11.9588456260835]
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 642:
    sage: L.value(.5)
Expected:
    0.763747880117299 + 0.216964767518864*I
Got:
    0.763747880117295 + 0.216964767518863*I
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 644:
    sage: L.value(.6+5*I)
Expected:
    0.702723260619684 - 1.10178575243940*I
Got:
    0.702723260619682 - 1.10178575243940*I
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 789:
    sage: lcalc_zeta.value(CC(.4,.5))
Expected:
    -0.450728958517113 - 0.780511403019070*I
Got:
    -0.450728958517121 - 0.780511403019071*I
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 852:
    sage: lcalc_zeta.find_zeros_via_N(3)
Expected:
    [14.1347251417347, 21.0220396387715, 25.0108575801457]
Got:
    [14.1347251417347, 21.0220396387716, 25.0108575801457]
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 174:
    sage: L.value(.5)
Expected:
    0.231750947504015 + 5.75329642226134e-18*I
Got:
    0.231750947504012 + 5.75329642226126e-18*I
**********************************************************************
File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 176:
    sage: L.value(CC(.2,.4))
Expected:
    0.102558603193338 + 0.190840777924700*I
Got:
    0.102558603193336 + 0.190840777924703*I
**********************************************************************
7 items had failures:
```


-- that is all just numerical noise probably because I'm testing on a 32-bit system and you made the tests on a 64-bit system (is that right?)  That is not serious (though will need to be fixed).

In the "testing" file, are the functions intended for inclusion in Sage?  If so, they need doctesting (and the names are a little strange) and they should perhaps be made into member functions of the appropriate classes (e.g. ell_rational_field).

In the docstrings explaining all the parameters, I don't think it is enough to just refer to the lcacl documentation.  These are Sage functions and the inputs need to be documented withing Sage (however tedious that might be!)

There are quite a few typos in the documentation.

Would it be possible to have a base class and have the various L-series classes derive from it?  That might reduce the code a little and make the structure clearer.

You have some input parameters which I think would more natually be True/False instead of 1/0 as now.

This has clearly been a huge amount of work and will be very useful.  The things I mentioned above are all minor, but still they should be considered, so I have left the tag as "needs work", but I think this is quite close to being includable.


---

Comment by rishi created at 2009-08-23 20:00:11

Replying to [comment:13 cremona]:
> Thanks for the explanation.
> 
> I successfully installed the new lcalc spkg;  then I successfully applied the patch and rebuilt sage.
> 
> Now testing sage/libs/lcalc gives this:
> {{{
> sage -t  "devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx"
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 411:
>     sage: L.value(.6)
> Expected:
>     0.274633355856348 - 6.59869267328213e-18*I
> Got:
>     0.274633355856341 - 6.59869267328188e-18*I
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 413:
>     sage: L.value(.6+1*I)
> Expected:
>     0.362258705721100 + 0.433888250620852*I
> Got:
>     0.362258705721102 + 0.433888250620855*I
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 450:
>     sage: L.find_zeros(1,15,.1)
> Expected:
>     [6.64845334472771, 9.83144443288668, 11.9588456260835]
> Got:
>     [6.64845334472771, 9.83144443288667, 11.9588456260835]
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 491:
>     sage: L.find_zeros_via_N(3)
> Expected:
>     [6.64845334472771, 9.83144443288668, 11.9588456260835]
> Got:
>     [6.64845334472772, 9.83144443288667, 11.9588456260835]
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 642:
>     sage: L.value(.5)
> Expected:
>     0.763747880117299 + 0.216964767518864*I
> Got:
>     0.763747880117295 + 0.216964767518863*I
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 644:
>     sage: L.value(.6+5*I)
> Expected:
>     0.702723260619684 - 1.10178575243940*I
> Got:
>     0.702723260619682 - 1.10178575243940*I
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 789:
>     sage: lcalc_zeta.value(CC(.4,.5))
> Expected:
>     -0.450728958517113 - 0.780511403019070*I
> Got:
>     -0.450728958517121 - 0.780511403019071*I
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 852:
>     sage: lcalc_zeta.find_zeros_via_N(3)
> Expected:
>     [14.1347251417347, 21.0220396387715, 25.0108575801457]
> Got:
>     [14.1347251417347, 21.0220396387716, 25.0108575801457]
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 174:
>     sage: L.value(.5)
> Expected:
>     0.231750947504015 + 5.75329642226134e-18*I
> Got:
>     0.231750947504012 + 5.75329642226126e-18*I
> **********************************************************************
> File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 176:
>     sage: L.value(CC(.2,.4))
> Expected:
>     0.102558603193338 + 0.190840777924700*I
> Got:
>     0.102558603193336 + 0.190840777924703*I
> **********************************************************************
> 7 items had failures:
> }}}
> 
> -- that is all just numerical noise probably because I'm testing on a 32-bit system and you made the tests on a 64-bit system (is that right?)  That is not serious (though will need to be fixed).
> 
> In the "testing" file, are the functions intended for inclusion in Sage?  If so, they need doctesting (and the names are a little strange) and they should perhaps be made into member functions of the appropriate classes (e.g. ell_rational_field).
> 
> In the docstrings explaining all the parameters, I don't think it is enough to just refer to the lcacl documentation.  These are Sage functions and the inputs need to be documented withing Sage (however tedious that might be!)
> 
> There are quite a few typos in the documentation.
> 
> Would it be possible to have a base class and have the various L-series classes derive from it?  That might reduce the code a little and make the structure clearer.
> 
> You have some input parameters which I think would more natually be True/False instead of 1/0 as now.
> 
> This has clearly been a huge amount of work and will be very useful.  The things I mentioned above are all minor, but still they should be considered, so I have left the tag as "needs work", but I think this is quite close to being includable.


---

Comment by rishi created at 2009-08-23 20:07:32

Replying to [comment:14 rishi]:


Thanks John for your feedback.  I was looking at the patch again, I am indeed seeing the typos, and places where documentation is far from clear. 

While I was writing, I did think of having a base class and have various L series derive from it, but it had taken me several weeks of manipulation just to get a compilable code out of cython, so I balked. I will go back and see how to reduce the clutter.

Rishi
> Replying to [comment:13 cremona]:
> > Thanks for the explanation.
> > 
> > I successfully installed the new lcalc spkg;  then I successfully applied the patch and rebuilt sage.
> > 
> > Now testing sage/libs/lcalc gives this:
> > {{{
> > sage -t  "devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx"
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 411:
> >     sage: L.value(.6)
> > Expected:
> >     0.274633355856348 - 6.59869267328213e-18*I
> > Got:
> >     0.274633355856341 - 6.59869267328188e-18*I
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 413:
> >     sage: L.value(.6+1*I)
> > Expected:
> >     0.362258705721100 + 0.433888250620852*I
> > Got:
> >     0.362258705721102 + 0.433888250620855*I
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 450:
> >     sage: L.find_zeros(1,15,.1)
> > Expected:
> >     [6.64845334472771, 9.83144443288668, 11.9588456260835]
> > Got:
> >     [6.64845334472771, 9.83144443288667, 11.9588456260835]
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 491:
> >     sage: L.find_zeros_via_N(3)
> > Expected:
> >     [6.64845334472771, 9.83144443288668, 11.9588456260835]
> > Got:
> >     [6.64845334472772, 9.83144443288667, 11.9588456260835]
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 642:
> >     sage: L.value(.5)
> > Expected:
> >     0.763747880117299 + 0.216964767518864*I
> > Got:
> >     0.763747880117295 + 0.216964767518863*I
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 644:
> >     sage: L.value(.6+5*I)
> > Expected:
> >     0.702723260619684 - 1.10178575243940*I
> > Got:
> >     0.702723260619682 - 1.10178575243940*I
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 789:
> >     sage: lcalc_zeta.value(CC(.4,.5))
> > Expected:
> >     -0.450728958517113 - 0.780511403019070*I
> > Got:
> >     -0.450728958517121 - 0.780511403019071*I
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 852:
> >     sage: lcalc_zeta.find_zeros_via_N(3)
> > Expected:
> >     [14.1347251417347, 21.0220396387715, 25.0108575801457]
> > Got:
> >     [14.1347251417347, 21.0220396387716, 25.0108575801457]
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 174:
> >     sage: L.value(.5)
> > Expected:
> >     0.231750947504015 + 5.75329642226134e-18*I
> > Got:
> >     0.231750947504012 + 5.75329642226126e-18*I
> > **********************************************************************
> > File "/home/john/sage-4.1.1/devel/sage-tests/sage/libs/lcalc/lcalc_Lfunction.pyx", line 176:
> >     sage: L.value(CC(.2,.4))
> > Expected:
> >     0.102558603193338 + 0.190840777924700*I
> > Got:
> >     0.102558603193336 + 0.190840777924703*I
> > **********************************************************************
> > 7 items had failures:
> > }}}
> > 
> > -- that is all just numerical noise probably because I'm testing on a 32-bit system and you made the tests on a 64-bit system (is that right?)  That is not serious (though will need to be fixed).
> > 
> > In the "testing" file, are the functions intended for inclusion in Sage?  If so, they need doctesting (and the names are a little strange) and they should perhaps be made into member functions of the appropriate classes (e.g. ell_rational_field).
> > 
> > In the docstrings explaining all the parameters, I don't think it is enough to just refer to the lcacl documentation.  These are Sage functions and the inputs need to be documented withing Sage (however tedious that might be!)
> > 
> > There are quite a few typos in the documentation.
> > 
> > Would it be possible to have a base class and have the various L-series classes derive from it?  That might reduce the code a little and make the structure clearer.
> > 
> > You have some input parameters which I think would more natually be True/False instead of 1/0 as now.
> > 
> > This has clearly been a huge amount of work and will be very useful.  The things I mentioned above are all minor, but still they should be considered, so I have left the tag as "needs work", but I think this is quite close to being includable.


---

Comment by rishi created at 2009-10-01 00:42:34

basic lcalc wrapper


---

Attachment

The new patch adds lot of documentation, and clean few typos. There are three functions where True or False is more natural as parameter, and I am going to change it. That is pretty much the only change left. Any program written using this patch will continue to work when I make those changes, so this patch can still be included. I will probably post the patch by tomorrow. Today I received an email that someone wants to use this program so I am uploading this patch.


---

Comment by mvngu created at 2009-10-01 04:19:41

Replying to [comment:16 rishi]:
> The new patch adds lot of documentation, and clean few typos.
With the patch `lcalc_wrapper.patch`, you create a new empty file called `sage/libs/lcalc/__init__.py`. It's dangerous to create empty files in the Sage library. Such files are known to result in missing files (hence corrupt the "main" repository) when creating a new source distribution of Sage. A solution is to put a comment in `sage/libs/lcalc/__init__.py`. The comment can just be something like:

```
# A comment here so this file is picked up when creating a new source distribution.
```



---

Comment by mvngu created at 2009-10-01 06:18:04

I assume `L-1.23.spkg` is version 1.23 of lcalc. Then the package must use the name `lcalc-1.23.spkg`; the current version in Sage 4.1.1 is `lcalc-20080205.p3.spkg`. A name for the lcalc package like `L-1.23.spkg` can result in errors building or upgrading Sage. If this ticket is closed, then ticket #4793 should be closed as "wontfix".


---

Attachment


---

Attachment

standalone patch, based on 4.3.alpha0


---

Attachment

I hope you won't mind, but I refactored a little bit your code to address reviewers comments.

In the provided patch:

 * the different L-functions derive from a base class
 * all doctests are protected against numerical noise
 * I removed the file for_testing.py and incorporated the (renamed) functions in the main file
   ( they could be moved to better places though )
 * added a __repr__ method (which is minimalistic)

After spkg install, only my patch needs to be applied.

Please let me know your opinion about all these.


---

Comment by rishi created at 2009-11-27 12:23:14

Replying to [comment:19 ylchapuy]:

Wonderfull!! I am looking at the code which has changed a lot, and it is impressive. I had written this as the lowest layer of a three layered interface to lcalc library. It was dirty, but it has taken me so long to add the necessary patches to lcalc itself, and then getting this thing to work with sage, that I balked when my attempts to derive the L-functions from a base class failed. 

I am still absorbing the changes. I will write more later.

Rishi


---

Comment by ylchapuy created at 2009-12-15 11:20:57

Any move on this?


---

Comment by rishi created at 2009-12-15 21:38:51

I apologise. I was busy with a gap which had popped up in my thesis. I will write by Sunday.


---

Comment by rishi created at 2009-12-21 14:20:46

Replying to [comment:21 ylchapuy]:
> Any move on this?

I had a closer look, and I like what I see. The code is beautiful. I would like it to be included as it is. It does address everything which John Cremona had raised.

The last 2 functions which generate L functions for Dirichlet characters and Elliptic Curves were supposed to be there for testing and as example.  For the time being I feel we can leave it like this till an improved version comes. 


Craig: Can I give it a positive review? I am not sure how the reviewing process works in this case.


Rishi


---

Comment by cremona created at 2009-12-21 14:46:07

Now there is code here from both rishi and ylchapuy it would be possible for each to review the other's code (since they both now know more about it than anyone else!) but it would be even better to have a third party do the job.  I volunteer to do that, in the next day or so.


---

Comment by rishi created at 2009-12-21 16:20:36

Thanks John.


Replying to [comment:24 cremona]:
> Now there is code here from both rishi and ylchapuy it would be possible for each to review the other's code (since they both now know more about it than anyone else!) but it would be even better to have a third party do the job.  I volunteer to do that, in the next day or so.


---

Comment by cremona created at 2009-12-23 20:14:43

Here's what I did:  made a fresh clone of 4.3.rc0, installed the spkg (sage -i lcalc-1.23.spkg), applied the latch, rebuilt.  Then sage -t gives this:

```
john@ubuntu%sage -t sage-4.3.rc0/devel/sage-lcalc/sage/libs/lcalc/ 
sage -t  "devel/sage-lcalc/sage/libs/lcalc/__init__.py"     
	 [0.1 s]
sage -t  "devel/sage-lcalc/sage/libs/lcalc/lcalc_Lfunction.pyx"
Exception NotImplementedError in 'sage.libs.lcalc.lcalc_Lfunction.Lfunction.__init_fun' ignored
-----------------------------------------------

Name of L_function: 
number of dirichlet coefficients = 5
coefficients are periodic
b[1] = 1
b[2] = -1
b[3] = -1
b[4] = 1
b[5] = 0

Q = 1.26156626101
OMEGA = (1,4.96506830649e-17)
a = 1 (the quasi degree)
gamma[1] =0.5    lambda[1] =(0,0)


number of poles (of the completed L function) = 0
-----------------------------------------------

-----------------------------------------------

Name of L_function: 
number of dirichlet coefficients = 5
coefficients are periodic
b[1] = (1,0)
b[2] = (6.12323399574e-17,1)
b[3] = (-6.12323399574e-17,-1)
b[4] = (-1,0)
b[5] = (0,0)

Q = 1.26156626101
OMEGA = (0.850650808352,0.525731112119)
a = 1 (the quasi degree)
gamma[1] =0.5    lambda[1] =(0.5,0)


number of poles (of the completed L function) = 0
-----------------------------------------------

**********************************************************************
File "/home/john/sage-4.3.rc0/devel/sage-lcalc/sage/libs/lcalc/lcalc_Lfunction.pyx", line 780:
    sage: L.value(0.5, derivative=1)
Expected:
    0.305999824716...
Got:
    0.305999723948232
-----------------------------------------------

Name of L_function: 
number of dirichlet coefficients = 5
coefficients are periodic
b[1] = 1
b[2] = -1
b[3] = -1
b[4] = 1
b[5] = 0

Q = 1.26156626101
OMEGA = (1,4.96506830649e-17)
a = 1 (the quasi degree)
gamma[1] =0.5    lambda[1] =(0,0)


number of poles (of the completed L function) = 0
-----------------------------------------------

**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_24
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/john/.sage//tmp/.doctest_lcalc_Lfunction.py
	 [2.2 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-lcalc/sage/libs/lcalc/lcalc_Lfunction.pyx"
Total time for all tests: 2.2 seconds
```

I cannot really tell what is going on here, sorry.


---

Comment by cremona created at 2009-12-23 20:14:43

Changing status from needs_review to needs_work.


---

Comment by ylchapuy created at 2009-12-23 20:55:20

The only lines really corresponding to the failure are:

```
File "/home/john/sage-4.3.rc0/devel/sage-lcalc/sage/libs/lcalc/lcalc_Lfunction.pyx", line 780:
    sage: L.value(0.5, derivative=1)
Expected:
    0.305999824716...
Got:
    0.305999723948232
```


The other ones comes from the doctesting of the `_print_data_to_standard_output` functions. I don't know how to deal with standard output easily in this case.

The problem is thus a numerical one. I don't know if it's normal to get such a difference in the result though. Should we just test for `0.305999...` ?


---

Comment by ylchapuy created at 2009-12-23 20:56:20

Oh, I just noticed the Exception at the beginning. I don't know where it comes from.


---

Comment by ylchapuy created at 2009-12-23 21:11:58

Ok, the (ignored) Exception comes from the very first doctest where I try to create an instance of the `Lfunction` class which is intended to be virtual.

The attached patch correct this, reals with the numerical noise (should we?) as stated above, and also correct a small typo.


---

Attachment


---

Comment by ylchapuy created at 2009-12-23 21:12:53

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-12-23 22:52:51

Replying to [comment:30 ylchapuy]:
Not sure when I'll get back to this -- family calls, and it might be a few days.  It's a pity if the numerical accuracy depends so much on platform though.


---

Comment by ylchapuy created at 2009-12-23 22:59:20

Replying to [comment:31 cremona]:
> Not sure when I'll get back to this -- family calls, and it might be a few days.

No problem of course; Happy Christmas!


---

Comment by cremona created at 2009-12-24 15:50:40

OK, so I found a few minutes.  New extra patch looks fine to me.  Successfully applied and tested on 32 and 64 bit machines.

I guess that we'll next want to change, or add to, the interface to command-line lcalc in sage/lfunctions/lcalc.py -- but that's for another ticket.


---

Comment by cremona created at 2009-12-24 15:50:40

Changing status from needs_review to positive_review.


---

Comment by rishi created at 2009-12-24 19:23:21

I did not check my email in the last 24 hours. Yes the derivatives will not be accurate. In fact it gets progressively wrong with higher derivatives. I will add a patch later to add to documentation to this fact. The derivative is calculated by calculating L function at two points very close and using the definition of derivative. It is not accurate at all.

The following error message is from lcalc library. It is debugging info which Mike uses when things go wrong.


```
----------------------------------------------

Name of L_function: 
number of dirichlet coefficients = 5
coefficients are periodic
b[1] = 1
b[2] = -1
b[3] = -1
b[4] = 1
b[5] = 0

Q = 1.26156626101
OMEGA = (1,4.96506830649e-17)
a = 1 (the quasi degree)
gamma[1] =0.5    lambda[1] =(0,0)


number of poles (of the completed L function) = 0
-----------------------------------------------


```



---

Comment by rishi created at 2009-12-24 19:34:20

I was wrong in the previous message. The print_data_to_standard_output is used for debugging in developing lcalc, and I used it to debug the wrapper initially when things were going totally awry. Although I rewrote few functions in lcalc to return values instead of printing in standard output, this function still prints everything out in standard output.


---

Comment by cremona created at 2009-12-30 16:17:43

NB See also #7788 for some minor docstring changes which should be merged when this is.


---

Comment by mhansen created at 2010-01-04 01:59:32

What all do I need apply for this?  I get the following failure:


```
cd "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage" && hg qser
cd "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage" && hg qimport /home/mhansen/.sage/temp/boxen/29343/release_0/trac_5396-refactor.patch
cd "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage" && hg qpush
cd "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage" && hg qimport /home/mhansen/.sage/temp/boxen/29343/release_0/trac_5396-review.patch
cd "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage" && hg qpush

=========================
 >>> Rebuilding Sage <<< 
=========================

cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from sage/libs/lcalc/lcalc_Lfunction.cpp:149:
sage/libs/lcalc/lcalc_sage.h:1:15: error: L.h: No such file or directory
In file included from sage/libs/lcalc/lcalc_Lfunction.cpp:149:
sage/libs/lcalc/lcalc_sage.h:27: error: expected constructor, destructor, or type conversion before ‘*’ token
sage/libs/lcalc/lcalc_sage.h:33: error: variable or field ‘del_Complexes’ declared void
sage/libs/lcalc/lcalc_sage.h:33: error: ‘Complex’ was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:33: error: ‘A’ was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:38: error: ‘Complex’ does not name a type
sage/libs/lcalc/lcalc_sage.h:44: error: variable or field ‘testL’ declared void
sage/libs/lcalc/lcalc_sage.h:44: error: ‘L_function’ was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:44: error: ‘Complex’ was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:44: error: ‘L’ was not declared in this scope
In file included from /usr/include/c++/4.2/ios:44,
                 from /usr/include/c++/4.2/ostream:45,
                 from /usr/include/c++/4.2/iostream:45,
                 from /virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local//include/NTL/tools.h:14,
                 from /virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local//include/NTL/ZZ.h:19,
                 from /virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local//include/csage/ntl_wrap.h:2,
                 from sage/libs/lcalc/lcalc_Lfunction.cpp:151:
/usr/include/c++/4.2/exception:40: error: expected declaration before end of line
```



---

Comment by rishi created at 2010-01-04 03:23:08

Replying to [comment:37 mhansen]:
> What all do I need apply for this?  I get the following failure:

Are you using the spkg in this ticket?


---

Comment by rlm created at 2010-01-13 07:01:17

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 07:01:17

After building `lcalc-1.23.spkg` and applying `trac_5396-refactor.patch` and `trac_5396-review.patch`, I get the following failures:

```
        sage -t -long devel/sage-main/sage/plot/line.py # 1 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/lseries_ell.py # 6 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py # 3 doctests failed
        sage -t -long devel/sage-main/sage/lfunctions/lcalc.py # 3 doctests failed
```


For example:

```
sage -t -long sage/plot/line.py
**********************************************************************
File "/virtual/scratch/rlm/sage-4.3.1.alpha2/devel/sage-main/sage/plot/line.py", line 375:
    sage: vals = E.lseries().values_along_line(1-I, 1+10*I, 100) # critical line
Expected nothing
Got:
    lcalc:  You need to uncomment the line: PARI_DEFINE = -DINCLUDE_PARI
    lcalc:  in the Makefile and do: 'make clean', then 'make' if you wish to use
    lcalc:  elliptic curve L-functions. Requires that you already have pari installed
    lcalc:  on your machine.
**********************************************************************
```



---

Comment by cremona created at 2010-01-13 09:35:59

This suggests to me that the build script in the spkg needs attention.


---

Attachment


---

Comment by rishi created at 2010-01-13 15:54:56

I have uncommented the appropriate line in the Makefile. lcalc uses pari to generate the dirichlet coefficients. If we use the wrapper, we can use sage to generate the dirichlet coefficients and feed it to lcalc.


---

Comment by rishi created at 2010-01-13 15:54:56

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-13 17:13:37

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-01-13 17:13:37

rishi, I could not install this version of lcalc.  I'll paste in below the error message I got.  Before that, two comments:  (1) the spkg should contain more than it does (an install script and the src directory).  See http://www.sagemath.org/doc/developer/producing_spkgs.html: there should be a file SPKG.txt, and there should be mercurial files, and an check script.... (2) When you make new versions of the spkg it's helpful for the name to change sp people can tell them apart:  here you could have called the first version lcalc-1.23.spkg, then lcalc-1.23.p1.spkg, etc.  The changes in each version should be docuemtned in SPKG.txt.

Here's the error I got installing it:

```
...
g++ -Wa,-W -O3  -Wno-deprecated  -ffast-math -fPIC  -I../include -I/usr/local/include/pari  -DINCLUDE_PARI -c Lcommandline_elliptic.cc
Lcommandline_elliptic.cc: In function ‘void data_E(char*, char*, char*, char*, char*, int, Double*)’:
Lcommandline_elliptic.cc:124: error: ‘lgeti’ was not declared in this scope
make[1]: *** [Lcommandline_elliptic.o] Error 1
make[1]: Leaving directory `/home/john/sage-4.3.1.alpha1/spkg/build/lcalc-1.23/src/src'
make: *** [all] Error 2
Error building lcalc
cp: cannot stat `lcalc': No such file or directory

real	0m17.528s
user	0m16.449s
sys	0m0.564s
sage: An error occurred while installing lcalc-1.23
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/john/sage-4.3.1.alpha1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/home/john/sage-4.3.1.alpha1/spkg/build/lcalc-1.23 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/home/john/sage-4.3.1.alpha1/spkg/build/lcalc-1.23' && '/home/john/sage-4.3.1.alpha1/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
```



---

Comment by bober created at 2010-01-13 21:56:22

This problem has to do with the makefile for lcalc, which needs work. Note that it includes the following, which explains why it didn't compile after that INCLUDE_PARI line was uncommented.


```
ifeq ($(PARI_DEFINE),-DINCLUDE_PARI)
    #location of pari.h.
    LOCATION_PARI_H = /usr/local/include/pari #usual location

    #location of libpari.a or of libpari.so
    #depending on whether static or dynamic libraries are being used.
    #On mac os x it's the former, on linux I think usually the latter.
    LOCATION_PARI_LIBRARY = /usr/local/lib #usual location
else
    #supplied as a dummy so as to avoid more ifeq's below
    LOCATION_PARI_H = .
    LOCATION_PARI_LIBRARY = .
endif
```



---

Comment by bober created at 2010-01-13 22:11:38

Suggestion: in the function Lfunction_from_character, instead of calling chi.gauss_sum(), call chi.gauss_sum_numerical(). It is much faster, and in the end we are only interested in the numerical approximation anyway.


```
sage: G = DirichletGroup(101)            
sage: chi = G[1]
sage: time A = chi.gauss_sum()
CPU times: user 19.05 s, sys: 0.02 s, total: 19.07 s
Wall time: 19.07 s
sage: time B = chi.gauss_sum_numerical()
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06 s
```



---

Comment by rishi created at 2010-01-14 00:48:55

Thanks Bober for the comment about compiling lcalc.

 I wrote the two functions to generate L functions of Dirichlet characters and Elliptic Curves exclusively for testing of wrapper. It was not supposed to be for end users at all. I wrote very simple function whose sole purpose was to not introduce any bugs. In fact they were in a file called for_testing.py till the refactor of code.

Can we do optimization outside the wrapper itself. 

Maybe we can write new functions in the lfunctions directory to generate elliptic curve, modular forms and dirichlet lfunctions.

Replying to [comment:44 bober]:
> Suggestion: in the function Lfunction_from_character, instead of calling chi.gauss_sum(), call chi.gauss_sum_numerical(). It is much faster, and in the end we are only interested in the numerical approximation anyway.
> 
> {{{
> sage: G = DirichletGroup(101)            
> sage: chi = G[1]
> sage: time A = chi.gauss_sum()
> CPU times: user 19.05 s, sys: 0.02 s, total: 19.07 s
> Wall time: 19.07 s
> sage: time B = chi.gauss_sum_numerical()
> CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
> Wall time: 0.06 s
> }}}


---

Attachment

For lcalc wrapper. This should work with the old code based on command line version of lcalc


---

Comment by rishi created at 2010-01-14 03:55:39

I am attaching another spkg. This is based on the earlier lcalc spkg. This should work. This also follows the instructions of http://www.sagemath.org/doc/developer/producing_spkgs.html

Special thanks to John from whom I have learnt a lot during this review process.


---

Comment by rishi created at 2010-01-14 03:55:39

Changing status from needs_work to needs_review.


---

Comment by rishi created at 2010-01-14 17:18:52

I realized that instead of having Makefile.sage, having just a patch file will make it more robust to changes in Makefile by Mike later.


---

Comment by drkirkby created at 2010-01-31 05:59:14

Changing status from needs_review to needs_work.


---

Attachment

William said the other day he does not want to see patches used. One reason cited was the fact that not all systems have a patch command, though I pointed out 'patch' was a requirement for POSIX. 

As such, I think you should rename this to a makefile.patch, and go back to your original solution of a patched makefile in the patches directory.


---

Comment by rishi created at 2010-02-02 14:26:58

Following David Kirby's comment, I have removed the changes from p2. This is exactly the same as lcalc-1.23.p1


---

Comment by rishi created at 2010-02-02 14:28:40

Changing status from needs_work to needs_review.


---

Attachment

I have removed the patch file, and gone back to the version 1.23.p1. This works on boxen. All the tests passed.


---

Comment by drkirkby created at 2010-02-02 17:53:30

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-02-02 17:53:30

I'm a bit concerned about the need to change the doctest to check for a result which is very different from the original, so the doctest chances from 


```
0.305999824716... 

to 

0.305999..
```


I know numerical noise does occur in calculations, but this seems a lot of it. Is there independant verification the new result is correct (in which case let's use it, and not all the dots), or is there independant verification the old result is correct, in which case it is doubtful this should be put in. 

I've expressed concern before about the way lcalc hides compiler warnings, which happened to be in a way that it stopped the Solaris build  #6609. It basically added a compiler flag, which was supposed to be sent to the gnu assembler, to suppress warnings. 

There are also #7178 and #7065 which I've raised. 

The fact this is so such a different result to the previous one, deserves some explanation I feel. I'd like to see an independent check with Mathematica. 

I'm marking it as 'needs info', as I think we should not just ignore the different result, but understand why it is so different. 

Dave


---

Comment by drkirkby created at 2010-02-02 19:11:13

I'm not a mathematician, but do have access to Mathematica. Can anyone tell me what this means, so I can compute this value in Mathematica? If I increase the precision, I should be able to get an accurate result. 

I have a comment regarding the remark by John Cremona about a different numerical value, and whether this could be due to his use of a 32-bit computer. This looks all like floating point maths to me, so the result would depend only on the IEEE floating point standard, which should give identical results on any Intel or AMD CPU,. as they both use 64-bits for the result, but work at 80 bits internally. This makes me even more concerned, and believe this needs addressing. 

Dave


---

Comment by cremona created at 2010-02-02 20:30:52

I don't think Mathematica will be much help here:  evaluating derivatives of L-series of elliptic curves. 

I tried Magma, but as far as I can see they don't do derivatives.  They can evaluate the L-series, and I did a "poor man's derivative" evaluating (L(0.5+e)-L(0.5))/e for small e and the result seemed to converge to  0.017188297766 and not anything like 0.305.

So Dave's question about what's going on here does need to be answered.


---

Comment by mhansen created at 2010-02-02 20:33:19

0.305... looks more like the value of L.derivative(1).


---

Comment by cremona created at 2010-02-02 20:41:50

Replying to [comment:52 mhansen]:
> 0.305... looks more like the value of L.derivative(1).

You're right!  That's the value I have in my database, anyway.  It is possible that lcalc normalises the functions so that the centre of the critical strip is 0.5 and not 1.

So I can verify with my own program that the value to around 50 decimals is

0.305999773834052301820483683321676474452637774590


---

Comment by cremona created at 2010-02-02 20:51:53

And in Magma (once I read the manual):

```
> E := EllipticCurve([0,0,1,-1,0]);
> CremonaReference(E);             
37a1
> L := LSeries(E);                 
> Evaluate(L,1 : Derivative:=1);
0.305999773834052301820483683322
```



---

Comment by drkirkby created at 2010-02-02 22:42:52

As you can tell, this is outside my Mathematical knowledge, but just a few comments. 

 * If this behaves differently to what someone might expect, then it should be documented how it works. I believe John is an expert in this area and he was surprised by the behavior, then clearly it could cause confusion. 
 * Since John's computed an computed a result with high precision, I would put that as a comment in the test code. 
 * I recall William once saying lcalc was very fast, but to me at least, this is not computing a very accurate result. I would suggest that should also be documented too. along with slower, but more accurate alternatives. 



Dave


---

Comment by rishi created at 2010-02-03 02:04:44

Yes it does normalize so that the center is at 0.5. The derivatives are not precise. I have added Mike to the discussion list so that he can give more details.


---

Comment by rishi created at 2010-02-03 02:17:10

I should have mentioned it in the last posting. I was planning to create another layer of python lfuntion class which will have the standard center (for general newforms).


---

Comment by rishi created at 2010-02-03 02:47:46

Replying to [comment:55 drkirkby]:
> As you can tell, this is outside my Mathematical knowledge, but just a few comments. 
> 
>  * If this behaves differently to what someone might expect, then it should be documented how it works. I believe John is an expert in this area and he was surprised by the behavior, then clearly it could cause confusion. 

The center being at half is documented. The key line is
 \Lambda(s) = \omega Q^s \overline{\Lambda(1-\bar s)} 

>  * Since John's computed an computed a result with high precision, I would put that as a comment in the test code. 

lcalc uses double to compute. The high precision is not possible. There is another ticket which contains documentation about loss of precision when calculating derivatives.


>  * I recall William once saying lcalc was very fast, but to me at least, this is not computing a very accurate result. I would suggest that should also be documented too. along with slower, but more accurate alternatives. 

Using double makes things fast, but they will not be as accurate as using a multiprecision library.

> 
> Dave


---

Comment by cremona created at 2010-02-03 09:24:15

I think it is important to note here that lcalc can handle a vastly larger assortment of L-functions than the opposition.  For example, the one value I recomputed independently is of the only kind I can handle with my code (and I can only compute the value at the centre, not anywhere else!).  So we should not leave the impression that lcalc is inferior just because it only uses double precision and not multi.


---

Comment by cremona created at 2010-02-03 09:24:15

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-02-03 11:44:36

Replying to [comment:59 cremona]:
> I think it is important to note here that lcalc can handle a vastly larger assortment of L-functions than the opposition.  For example, the one value I recomputed independently is of the only kind I can handle with my code (and I can only compute the value at the centre, not anywhere else!).  So we should not leave the impression that lcalc is inferior just because it only uses double precision and not multi.

I agree, but there is significant precision loss - perhaps more than some might expect, so personally I would have thought that worth documenting. Of course, anyone should know hardware floating point will be less accurate (but faster) than extended precision in software.  

Given for simple computations, 16 digits of precision are possible, but here only 9, I would have thought that work documenting. 

The fact lcalc can handle a vastly larger assortment of L-functions than anything else should also be noted! 

Dave


---

Comment by mrubinst created at 2010-02-03 15:26:04

Replying to [comment:60 drkirkby]:
> Replying to [comment:59 cremona]:
> > I think it is important to note here that lcalc can handle a vastly larger assortment of L-functions than the opposition.  For example, the one value I recomputed independently is of the only kind I can handle with my code (and I can only compute the value at the centre, not anywhere else!).  So we should not leave the impression that lcalc is inferior just because it only uses double precision and not multi.
> 
> I agree, but there is significant precision loss - perhaps more than some might expect, so personally I would have thought that worth documenting. Of course, anyone should know hardware floating point will be less accurate (but faster) than extended precision in software.  
> 
> Given for simple computations, 16 digits of precision are possible, but here only 9, I would have thought that work documenting. 
> 
> The fact lcalc can handle a vastly larger assortment of L-functions than anything else should also be noted! 
> 
> Dave


---

Comment by mrubinst created at 2010-02-03 15:33:31

I plan to release version L-1.3 in a couple of weeks, and also to
have Rishi update his cython wrapper during our march workshop (I made
a handful of changes that will need him to update).

There are a number of key improvements.

Precision-

I've spent quite a bit of effort getting a multiprecision version
of lcalc to work. I now have it working with Bailey's double double
and quad double (about 30 and 60 digits respectively) and also MPFR,
though the latter seems quite slow, perhaps because of the c++ wrapper that I am using... haven't dug too deep with the latter since
Bailey's dd and qd works quite nicely, and 60 digits is quite reasonable. Nonetheless,
it does work to higher precision with mpfr.

I am also developing a test suite to be run at compile time to check on accuracy of many of the routines and do various timing tests.

Output precision-

Rishi needs to handle this carefully since I have a parameter
which describes how many digits of the working digits are accurate.
I use this parameter when outputting my results. Not sure how
or if Rishi makes use of this extra info, or just passes the double results
of my routines.

At the same time I am wiring in better control of output precision
based on the explicit formula and also on using the smooth approximate
functional equation with a couple of different test functions.

Derivatives-

the version in L-1.23 is very crummy and I fixed that up too
in version L-1.3. I initially just wanted to get that functionality in there, and I now use (version L-1.3 to be released) higher central differences for the derivatives that gives an accuracy of about Digits*4/(n+4) for the nth derivative. So for the 1st derivative,
my new version is accurate to about 4/5 the working precision, so roughly 12-13 digits with double precision and 24-25 digits with Bailey's dd.


Zeros-

I fixed a subtle bug that would on rare occasion cause some zeros to be omitted
and other zeros to be duplicated in their place.

I'm also finishing to wire in a test of the explicit formula (based on a prototype that Kevin McGown helped me with in our kickoff frg coding sprint) that will prevent
such bugs from going unnoticed!

Trivial zeros-

I built in knowledge of the trivial zeros so that correct output is displayed there.
This allowed me to apply the functional equation correctly, so that the new version
works throughout the complex plane (previously it gave nonsense results left of 0).

Band limited interpolation-

I'm wiring in some code of ghaith Hiary for computing zeta using band limited
interpolation. This will give a significant speedup in, for example, computing zeros of zeta.

Start at Nth zero-

Ability to start searching for zeros from the Nth zero onward (rather than
always starting from the real axis). This one was long overdue!


Many small improvements that have a big impact-

For example I coded up my own trig functions that are about 4 times faster than
the machines (for double precision) and also faster than Bailey's and MPFR's.

Anyhow, my package definitely needs a companion paper and much better
documentation. Something to work on...

Other planned improvements for version L-1.4:

1) broader use of openmp in some of the key routines
2) fft algorithms- will lead to orders of magnitude improvement
especially for higher degree L-funcitons
3) L-functions of number fields and symmetric powers


---

Comment by mrubinst created at 2010-02-03 15:44:45

One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables.


---

Comment by drkirkby created at 2010-02-03 16:00:48

Replying to [comment:63 mrubinst]:
> One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables.

That is really *excellent* news. Is there any chance either you or I could check this with the Sun compiler on Solaris, before you make an official release? The Sun compilers more fussy than gcc, but would give us a performance boost on Solaris. 

The fact the compiler is more fussy, also tends to weed out some sort of bugs. On 't2' the Sun C compiler is 

`/opt/sunstudio12.1/bin/cc`

and the C++ compiler is 

`/opt/sunstudio12.1/bin/CC`

On the C++ compiler, you will probably need the option 


```
 -library=stlport4 
```


as that will then implement the latest C++ standard. (The older C++ standard is not compatible with the latest standard. For backwards compatibility Sun's C++ compiler defaults to the old C++ standard.}}} 

Previously I tried building lcalc with the Sun compiler but got lots of warnings and error messages. But if the code has been cleaned up, things have more chance of working. 

The point I made above about storing the exact (or least high precision) result in the test file, would be that is some record of what and should be, even though it is not going to be achieved. 

Then if you bring out a later version of lcalc, which deviates more from the exact result, people will at least know. It would only add 70 or so bytes to a file. 

Dave


---

Comment by drkirkby created at 2010-02-22 00:01:52

Has this been checked on Solaris 10 with gcc? The different floating point processor may well give a different answer and need revisions to the doc test. 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by drkirkby created at 2010-02-22 00:01:52

Changing status from needs_review to needs_info.


---

Comment by rishi created at 2010-02-23 00:45:30

I am unable to decipher the following error message when I try to compile on t2.

```
g++ -Wa,-W -O3  -Wno-deprecated  -ffast-math -fPIC  -I../include Lglobals.o Lgamma.o Lriemannsiegel.o Lriemannsiegel_blfi.o Ldokchitser.o Lcommandline_globals.o Lcommandline_misc.o Lcommandline_numbertheory.o Lcommandline_values_zeros.o Lcommandline_elliptic.o Lcommandline_twist.o Lcommandline.o cmdline.o -Xlinker -export-dynamic  -Xlinker -rpath -Xlinker /scratch/rishi/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/local/lib  -L/scratch/rishi/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/local/lib  -lpari -o lcalc
ld: fatal: option -dn and -P are incompatible
ld: fatal: Flags processing errors
collect2: ld returned 1 exit status
make[1]: *** [lcalc] Error 1
make[1]: Leaving directory `/scratch/rishi/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/spkg/build/lcalc-1.23.p3/src/src'
make: *** [all] Error 2
```


I have not seen -dn or -P options  in anything.


---

Attachment

Changed makefile to compile on solaris


---

Comment by rishi created at 2010-02-23 13:21:03

Changing status from needs_info to needs_review.


---

Comment by rishi created at 2010-02-23 13:21:03

I have attached new spkg. This compiles on solaris and the tests passed on t2.


---

Comment by drkirkby created at 2010-02-24 22:13:21

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-24 22:13:21

Replying to [comment:64 drkirkby]:
> Replying to [comment:63 mrubinst]:
> > One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables.
> 
> That is really *excellent* news. Is there any chance either you or I could check this with the Sun compiler on Solaris, before you make an official release? The Sun compilers more fussy than gcc, but would give us a performance boost on Solaris. 

Having looked at this more closely, you have suppressed warnings, after I'd gone out of the way to enable them. 

You have the options -W and  -Wno-deprecated, which are documented at 

http://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#Warning-Options

as 

```
-w
    Inhibit all warning messages. 

-Wno-deprecated
    Do not warn about usage of deprecated features. See Deprecated Features. 
```


If we follow that link about Deprecated Features, it says "Using the old features might cause a warning in some cases that the feature will be dropped in the future. In other cases, the feature might be gone already."

So this appears to be storing up trouble for the future to me. 

Given I'd noticed some problems before on Solaris, I made an effort to highlight the warnings. Now they have gone, as you have suppressed them. 

As more minor points: 

 * This package is .p4, but the changes for .p3 are not documented in SPKG.txt. If .p3 was never merged into Sage (which I believe is probably the case), then this should be called .p3 and not .p4. You can overwrite your old .p3 version. 
 * It would be useful if the ticket number #5396 was put in SPKG.txt too. 

Dave 

Dave


---

Comment by drkirkby created at 2010-02-24 22:15:26

It would be good if you could at least add -Wall and get rid of the warnings, and optionally -pedantic too. The the code will hopefully not break any time soon. This could easily break with a compiler upgrade. 

Dave


---

Comment by rishi created at 2010-02-24 23:55:31

Changing assignee from Rishi to rishi.


---

Comment by rishi created at 2010-02-24 23:55:31

This version is not what Mike was writing about in his posting. He was giving a preview of a future release of lcalc. This version is not as polished. But then it is better than what is shipping with sage right now.

Regarding overwriting older packages, John Cremona asked that I do exactly the opposite of what you are suggesting. Please see his posting from couple of months ago in this very ticket. I will include a one line description of p3. p3 was just reverting from p2 to p1.

I just made the minimal changes to Mike's makefile so that it compiles on solaris and uses pari library in SAGE_LOCAL. I did not want to make too many changes to the lcalc makefile.

In any case I will make changes you suggested to Makefile.sage in patches directory and post it.


---

Comment by rishi created at 2010-02-25 00:08:32

Replying to [comment:70 rishi]:
> This version is not what Mike was writing about in his posting. He was giving a preview of a future release of lcalc. This version is not as polished. But then it is better than what is shipping with sage right now.
> 

I should clarify that I am talking about lcalc the program, and not the build scripts.


---

Comment by drkirkby created at 2010-03-06 14:07:12

Replying to [comment:70 rishi]:

> Regarding overwriting older packages, John Cremona asked that I do exactly the opposite of what you are suggesting. Please see his posting from couple of months ago in this very ticket. I will include a one line description of p3. p3 was just reverting from p2 to p1.

I'm really confused here. I'm going to cc Minh onto this, as he knows more about version numbers than me, but I believe the version being proposed is incorrect. 

 * 6 months ago you added 'L-1.23.spkg' to this ticket. So was that supposed to be brand new package? Currently there is no package in Sage called 'L'. In any case it should *not* have been attacked to the trac server, but instead a link provided to a place where it could be found. 

 * There are numerous other attachments. Assuming all these changes are based on top of version 1.23 of lcalc, and not a version with a date code of'20080205', then I believe all these changes should be put into lcalc-1.23. There is no need for p0, p1, p2, p3 or p4. Patch levels should be incremented as a result of newer versions committed to Sage - not as a result of reviewer comments. 

 * If all these changes are based on the version of lcalc in Sage, lcalc-20080205.p4.spkg, then the updated version should be called lcalc-20080205.p5.spkg. 

Perhaps you could briefly summerise what this is, and why it should be called a particular version. Why was it orriginally going to be called L? With a highly technical package and 70 comments spanning 6-months, it is hard to decipher it all. But I believe something is wrong here, but would welcome some comments from Minh. 

Dave


---

Comment by rishi created at 2010-03-09 19:22:09

Replying to [comment:72 drkirkby]:

> Replying to [comment:70 rishi]:
> > Regarding overwriting older packages, John Cremona asked that I do exactly the opposite of what you are suggesting. Please see his posting from couple of months ago in this very ticket. I will include a one line description of p3. p3 was just reverting from p2 to p1.
> I'm really confused here. I'm going to cc Minh onto this, as he knows more about version numbers than me, but I believe the version being proposed is incorrect.  * 6 months ago you added 'L-1.23.spkg' to this ticket. So was that supposed to be brand new package? Currently there is no package in Sage called 'L'. In any case it should *not* have been attacked to the trac server, but instead a link provided to a place where it could be found. 

Please read the comments in this ticket. http://trac.sagemath.org/sage_trac/ticket/5396#comment:39

> * There are numerous other attachments. Assuming all these changes are based on top of version 1.23 of lcalc, and not a version with a date code of'20080205', then I believe all these changes should be put into lcalc-1.23. There is no need for p0, p1, p2, p3 or p4. Patch levels should be incremented as a result of newer versions committed to Sage - not as a result of reviewer comments.

> * If all these changes are based on the version of lcalc in Sage, lcalc-20080205.p4.spkg, then the updated version should be called lcalc-20080205.p5.spkg.

It is not based on lcalc-20080205.

> Perhaps you could briefly summerise what this is, and why it should be called a particular version. Why was it orriginally going to be called L? With a highly technical package and 70 comments spanning 6-months, it is hard to decipher it all. But I believe something is wrong here, but would welcome some comments from Minh.

  http://trac.sagemath.org/sage_trac/ticket/5396#comment:39

> Dave


---

Comment by rishi created at 2010-03-09 19:24:01

The links were wrong.

http://trac.sagemath.org/sage_trac/ticket/5396#comment:18


---

Comment by rishi created at 2010-03-09 19:27:01

HOWTO

1. Apply trac_5396-refactor.patch
2. Apply trac_5396-review.patch
3. Use lcalc-1.23.p4 spkg

This patch no longer compiles with the latest version of sage.


---

Comment by ylchapuy created at 2010-03-09 20:58:26

(minor) rebase for sage4.3.3


---

Attachment

You just have to apply the one character patch trac_5396-rebase_sage4.3.3.patch on top of others.


---

Comment by rishi created at 2010-03-09 21:24:06

combined patch rebased to 4.3.3


---

Attachment

Oops! I did not see Yann had already posted a patch.


---

Comment by rishi created at 2010-03-09 22:05:03

Changing status from needs_work to needs_review.


---

Comment by rishi created at 2010-03-09 22:05:03

Another spkg. 

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-1.23.spkg


---

Comment by rishi created at 2010-03-17 19:35:35

This ticket has become too long. I am splitting the lcalc spkg to  a ticket originally by mabshoff  #4793


---

Comment by rishi created at 2010-03-17 19:42:57

Only the last patch  trac_5396_combined_rebasedto_4.3.3.patch is needed. It combines all the work prior to it. This patch depends spkg upgrade in #4793


---

Attachment

The location of header files have changed in the lcalc spkg. This incorporates neccessary changes to compile.


---

Comment by rishi created at 2010-03-29 14:28:43

Since the spkg upgrade this patch depended on has received positive review, can someone reinstate the positive review here.


---

Comment by AlexGhitza created at 2010-06-04 23:59:31

Applied and tested on sage-4.4.2.


---

Comment by AlexGhitza created at 2010-06-04 23:59:31

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 07:33:11

Changing status from positive_review to needs_work.


---

Comment by ddrake created at 2010-07-22 07:33:11

Am I correct that only attachment:trac_5396_combined_rebased_4.3.4.patch should be merged?

If so, please add the ticket number to that patch's commit message and switch this back to positive review!


---

Comment by rishi created at 2010-07-22 17:32:26

Changing status from needs_work to positive_review.


---

Comment by rishi created at 2010-07-22 17:32:26

Replying to [comment:83 ddrake]:
> Am I correct that only attachment:trac_5396_combined_rebased_4.3.4.patch should be merged?
> 
> If so, please add the ticket number to that patch's commit message and switch this back to positive review!


Yes only the last attachment is to be merged.


---

Comment by ddrake created at 2010-07-22 23:49:13

Replying to [comment:84 rishi]:
> Replying to [comment:83 ddrake]:
> > Am I correct that only attachment:trac_5396_combined_rebased_4.3.4.patch should be merged?
> > 
> > If so, please add the ticket number to that patch's commit message and switch this back to positive review!
> 
> 
> Yes only the last attachment is to be merged.

Merged on 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-22 23:49:13

Resolution: fixed


---

Comment by ddrake created at 2010-07-26 06:16:56

Is there a spkg that goes along with the patch? I'm trying to compile from scratch after applying the above patch, and it's failing:

```
In file included from sage/libs/lcalc/lcalc_Lfunction.cpp:163:
sage/libs/lcalc/lcalc_sage.h:27: error: expected constructor, destructor, or type conversion before �*� token
sage/libs/lcalc/lcalc_sage.h:33: error: variable or field �del_Complexes� declared void
sage/libs/lcalc/lcalc_sage.h:33: error: �Complex� was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:33: error: �A� was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:38: error: �Complex� does not name a type
sage/libs/lcalc/lcalc_sage.h:44: error: variable or field �testL� declared void
sage/libs/lcalc/lcalc_sage.h:44: error: �L_function� was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:44: error: �Complex� was not declared in this scope
sage/libs/lcalc/lcalc_sage.h:44: error: �L� was not declared in this scope
```

I have the above patch, and lcalc-20100428-1.23.p0.spkg. If I'm missing a spkg, which one is missing? I see a bunch of spkgs posted here, along with links to others. Which to merge?


---

Comment by ddrake created at 2010-07-26 07:20:01

Replying to [comment:86 ddrake]:
> Is there a spkg that goes along with the patch? I'm trying to compile from scratch after applying the above patch, and it's failing:

Hrm, it seems that the problem was that the lcalc spkg wasn't installed. I see in the spkg/standard/deps file that lcalc isn't a prequisite for the Sage library; should it be? The above problem went away after I installed the spkg with "sage -i".


---

Comment by rishi created at 2010-07-26 11:33:22

Replying to [comment:87 ddrake]:
> Replying to [comment:86 ddrake]:
> > Is there a spkg that goes along with the patch? I'm trying to compile from scratch after applying the above patch, and it's failing:
> 
> Hrm, it seems that the problem was that the lcalc spkg wasn't installed. I see in the spkg/standard/deps file that lcalc isn't a prequisite for the Sage library; should it be? The above problem went away after I installed the spkg with "sage -i". 
> 

Till this patch, lcalc was not require to build sage library. The code William wrote used pexpect  and the command line version of lcalc. Now libLfunction.so is required to compile. I did not know that one has to change spkg/standard/deps also. Can you change it so that the spkg becomes a prerequisite for the sage library


---

Attachment

Updated `spkg/standard/deps` merged into 4.5.2.alpha1.


---

Comment by mpatel created at 2010-07-27 07:46:26

Diff of `spkg/standard/deps` from 4.5.2.alpha0 to 4.5.2.alpha1, minus #9456's  "hunk"


---

Attachment

I've attached the updated `deps` file included in Sage 4.5.2.alpha1.  Please see [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/db2c5f0aa386eebb#db2c5f0aa386eebb) for an explanation.


---

Comment by ddrake created at 2010-07-28 02:43:58

This ticket introduced some doctest failures in 4.5.2.alpha1; see #9615.


---

Comment by mpatel created at 2010-07-29 06:40:03

Replying to [comment:88 rishi]:
> Replying to [comment:87 ddrake]:
> > Replying to [comment:86 ddrake]:
> > > Is there a spkg that goes along with the patch? I'm trying to compile from scratch after applying the above patch, and it's failing:
> > 
> > Hrm, it seems that the problem was that the lcalc spkg wasn't installed. I see in the spkg/standard/deps file that lcalc isn't a prequisite for the Sage library; should it be? The above problem went away after I installed the spkg with "sage -i". 
> > 
> 
> Till this patch, lcalc was not require to build sage library. The code William wrote used pexpect  and the command line version of lcalc. Now libLfunction.so is required to compile. I did not know that one has to change spkg/standard/deps also. Can you change it so that the spkg becomes a prerequisite for the sage library

For the record: This confirms the decision to merge an updated [attachment:deps spkg/standard/deps] file in Sage 4.5.2.alpha1.


---

Comment by mpatel created at 2010-08-06 02:02:47

I'm updating the Author(s) field using the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames).


---

Comment by fbissey created at 2010-08-06 09:32:44

I noticed that you have mpfr in the dep for lcalc and that you include 
mpfr in the library list in module_list.py for the lcalc extension as well.
lcalc doesn't currently depend on mpfr or link against it.
I checked the current spkg and the latest version included in this bug
and neither does. In spkg-install you have

```
if [ "$UNAME" = "SunOS" ]; then
    LCALC_LIBS="-lpari -lmpfr -lgmpxx -lgmp -liberty"
else
    LCALC_LIBS="-lpari -lmpfr -lgmpxx -lgmp"
fi 
export LCALC_LIBS
echo "Using LCALC_LIBS=$LCALC_LIBS"
```

But LCALC_LIBS is not used anywhere in either the original Makefile
or the Makefile provided by sage.
I think it is a remnant from a time where Dave (Kirby) had an extremely
simplified Makefile for lcalc and even then it was a case of overlinking.
If you want to use mpfr in lcalc you need to export

```
PREPROCESSOR_DEFINE=-DUSE_MPFR
```

and on my machine at least lcalc refuse to compile with this.

Francois


---

Comment by drkirkby created at 2010-08-06 15:07:20

Replying to [comment:93 fbissey]:

> I think it is a remnant from a time where Dave (Kirby) had an extremely
> simplified Makefile for lcalc and even then it was a case of overlinking.
> Francois

My logic for changing the Makefile fell into 3 reasons I think. 
 * The original Makefile had a non-portable gcc option -Wa,-W in an attempt to suppress warnings from the assembler. That works with the GNU assembler, but failed with the Sun assembler, as the Sun assembler does not recognise the -W option.   
 * I added -Wall to show the warnings from the code - I think it's good we see what warnings are generated by the compiler, as it is something to look at when getting problems. 
 * The original Makefile defined the compiler to be "gcc" but if we used $CC, we could use any compiler. 

I doubt I would have changed any linking - if I did, it was probably not intentionally. 

I have not checked this code when CC is defined to be a compiler other than gcc, but I did fix it to work with any compiler at one point - I hope a regression has not been introduced. 

Dave


---

Comment by fbissey created at 2010-08-06 19:06:25

Replying to [comment:94 drkirkby]:
> Replying to [comment:93 fbissey]:
> 
> > I think it is a remnant from a time where Dave (Kirby) had an extremely
> > simplified Makefile for lcalc and even then it was a case of overlinking.
> > Francois
> 
> My logic for changing the Makefile fell into 3 reasons I think. 
>  * The original Makefile had a non-portable gcc option -Wa,-W in an attempt to suppress warnings from the assembler. That works with the GNU assembler, but failed with the Sun assembler, as the Sun assembler does not recognise the -W option.   
>  * I added -Wall to show the warnings from the code - I think it's good we see what warnings are generated by the compiler, as it is something to look at when getting problems. 
>  * The original Makefile defined the compiler to be "gcc" but if we used $CC, we could use any compiler. 
> 
> I doubt I would have changed any linking - if I did, it was probably not intentionally. 
> 
> I have not checked this code when CC is defined to be a compiler other than gcc, but I did fix it to work with any compiler at one point - I hope a regression has not been introduced. 
> 
Hi Dave,

the makefile needed some sanity put back into it, especially linker wise.
so that was a job that was needed. I guess my main concern here is:


*lcalc depends on mpfr when it shouldn't.


The rest is just my ramblings about there being an unused variable in
spkg-install - which may lead people to think it is.


Francois


---

Comment by rishi created at 2010-08-06 19:42:16

This ticket is not about lcalc spkg. Please do not add junk to this ticket. I am replying to the latest closed ticket about the spkg  #9665

Replying to [comment:95 fbissey]:
> Replying to [comment:94 drkirkby]:
> > Replying to [comment:93 fbissey]:
> > 
> > > I think it is a remnant from a time where Dave (Kirby) had an extremely
> > > simplified Makefile for lcalc and even then it was a case of overlinking.
> > > Francois
> > 
> > My logic for changing the Makefile fell into 3 reasons I think. 
> >  * The original Makefile had a non-portable gcc option -Wa,-W in an attempt to suppress warnings from the assembler. That works with the GNU assembler, but failed with the Sun assembler, as the Sun assembler does not recognise the -W option.   
> >  * I added -Wall to show the warnings from the code - I think it's good we see what warnings are generated by the compiler, as it is something to look at when getting problems. 
> >  * The original Makefile defined the compiler to be "gcc" but if we used $CC, we could use any compiler. 
> > 
> > I doubt I would have changed any linking - if I did, it was probably not intentionally. 
> > 
> > I have not checked this code when CC is defined to be a compiler other than gcc, but I did fix it to work with any compiler at one point - I hope a regression has not been introduced. 
> > 
> Hi Dave,
> 
> the makefile needed some sanity put back into it, especially linker wise.
> so that was a job that was needed. I guess my main concern here is:

> 
> *lcalc depends on mpfr when it shouldn't.

> 
> The rest is just my ramblings about there being an unused variable in
> spkg-install - which may lead people to think it is.

> 
> Francois
