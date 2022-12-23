# Issue 4721: [with patch; needs review] Indefinite integration for piecewise functions

Issue created by migration from https://trac.sagemath.org/ticket/4721

Original creator: pbutler

Original creation time: 2008-12-05 22:37:17

Assignee: burcin

CC:  mhansen

It would be nice to be able to do indefinite integration of piecewise functions in Sage.

I've created a patch which does this. I have made the default behavior of the integral() function of a piecewise function be to return the indefinite integral, and the definite integral is returned only when definite=True is supplied.


```
sage: pw = Piecewise([[(0,1), x*2], [(1,2), x + 3]])
sage: pw.integral()
Piecewise defined function with 2 parts, [[(0, 1), x^2], [(1, 2), (x^2 + 6*x)/2 - 5/2]]
sage: pw.integral(definite=True)
11/2
```





---

Comment by wdj created at 2008-12-05 22:43:58

I don't agree that this should be the default. First, how is the indefinite integral of piecewise function even well-defined? Assuming it somehow makes sense, the definite integral should be the default and the indefinite one (which should be very well documented) should require options. Also, my vote is that one should require the optional "method=indefinite" as opposed to "definite=True". I think "method" is more of a Sage standard.


---

Attachment


---

Comment by pbutler created at 2008-12-05 23:12:55

I made integration the default for consistency with other functions. For example,


```
sage: f(x)=3
sage: f.integral()
x |--> 3*x
sage: (x*8).integral()
4*x^2
sage: sin(x).integral()
-cos(x)
```


When integrating a piecewise function in Maple, the result is the indefinite integral. The only difference between the Maple result and the patched Sage code is that Maple defines the integral outside the bounds of the original piecewise function, which my code does not.


---

Comment by wdj created at 2008-12-05 23:24:08

Okay. It makes good sense to usually copy the default, or implement an idea used in Maple's interface design. 

But in this case, the indefinite integral of a piecewise defined function is not well-defined. I have no idea why Maple implemented it. I'm sure they had some reason. But IMHO Sage should not be implementing methods which so not have a well-defined mathematical meaning as a default. As an option (which is very well-documented), I have no objection because whoever would be using it presumably know what it means. However, I don't know what it means to indefinitely integrate a piecewise defined function and your code does not explain it.

It might be useful for some, so could you please revise it a bit?


---

Comment by pbutler created at 2008-12-06 01:02:12

Interestingly, Mathematica Online Integrator gives an answer too, but chops off the constant in each piece. You still get a valid antiderivative, but it is not useful as an indefinite integral. (Since it is discontinuous, it doesn't have to satisfy the conclusion of the FTC.)

I do see the value of keeping to mathematically well-defined results, but there is also value in consistency. integrate(f) returning an antiderivative in some cases and a definite integral in others doesn't feel intuitive to me.

In any case, I'll clean this code up so that it can be included. It should be useful for people working with continuous probability distributions, if nothing else. (Actually, there must be some other use for it too, because Mathematica does it and their results would not be useful for probability.)


---

Comment by mabshoff created at 2008-12-06 01:06:55

Hi Paul,

design discussions like this should not be done in trac since the number of people actually getting emails from this is minuscule compared to the audience on sage-devel. So please send an email with a summary what is proposed and what has been discussed so far to sage-devel. Also mention the ticket and that there are some more details there.

Thanks and keep up the good work.

Cheers,

Michael


---

Attachment


---

Comment by pbutler created at 2008-12-11 16:47:39

I've made some changes and added a new patch. Changing from needs work to needs review.


---

Comment by boothby created at 2009-01-24 11:24:03

Works as advertised.  I don't care about any design / structure details of calculus, so I think somebody else should look at it.


---

Comment by wdj created at 2009-01-24 13:54:19

Sorry, I didn't see this earlier or I would've reviewed it.

This does not seem to work as advertised. There was a long thread in sage-devel which I though settled some design issues. One of them was that the FTC should be true for this indefinite integral. For example, the indef int F of the function f defined on (-4,3) 


```

 sage: f1(y) = -1
 sage: f2(y) = y + 3
 sage: f3(y) = -y - 1
 sage: f4(y) = y^2 - 1
 sage: f5(y) = 3
 sage: f = Piecewise([[(-4,-3),f1],[(-3,-2),f2],[(-2,0),f3],[(0,2),f4],[(2,3),f5]])
 sage: F = f.integral(y)

```


should have the property that F(3)-F(-4) is the area under the curve.
This *is* true, as the following shows:


```
sage: f.integral(y,(-4,3))
19/6
sage: F(3)-F(-4)
19/6
```


This is not tested. In my option, this needs to be added to the docstring.

*However*, what the docstring says is "If definite=True is given, returns the definite integral."
I don't know what the output


```
sage: f.integral(definite=True)
2*(y^2 - 1) + y + 2*(-y - 1) + 5
```


means. I would expect it to be 19/6. Don't you assume the function is 0 outside 
(-4,3)? In any case, the definite integral seems incorrect, and is not consistenet
with the old behaviour, as you said it would be in the thread referred to above.


---

Comment by pbutler created at 2009-01-24 22:41:55

It works as expected if you specify the variable:


```
sage: f.integral(definite=True)
2*(y^2 - 1) + y + 2*(-y - 1) + 5
sage: f.integral(y,definite=True)
19/6
```


I suppose in functions of one variable it would be more consistent (within Sage) to figure out the variable automatically, though?


---

Comment by wdj created at 2009-01-24 22:48:08

Yes. Can you please do that and add the FTC example to the docstring?


---

Attachment


---

Comment by pbutler created at 2009-01-25 02:09:21

I've added a patch with the changes requested.


---

Comment by wdj created at 2009-01-25 02:41:32

Can you explain how to apply the patches? The third one does not apply cleanly on top of the second one, in 3.3.alpha1.


---

Comment by wdj created at 2009-01-25 02:52:53

I did manage to apply patch #3 and apply it to 3.3.alpha1 but sage -t timed out on my machine. 

I'll try this on my macbook but this will take awhile since it's very slow. If the patch is as described then I hope to (finally) give it a positive review.


---

Attachment

I should have mentioned that the patches are not meant to be applied on top of each other. I kept the old ones up simply for comparison. Sorry for the confusion.

For comparison, my (fairly modest) laptop finishes the tests in 126s. Looking through the code again, I realized that I didn't make `default_variable()` cache the results, so I've prepared a patch (`default_variable.patch`) to be applied on top of `piecewise_integration3.patch`.


---

Comment by wdj created at 2009-01-25 15:32:07

The last two patches together (first patch #3 then the "default" patch) apply cleanly to 3.3.alpha2. They also pass sage -t.

A few comments:

1) You have 


```
            sage: f1(y) = (x+3)^2
            sage: f2(y) = x+3
            sage: f3(y) = 3
            sage: f = Piecewise([[(-infinity, -3), f1], [(-3, 0), f2], [(0, infinity), f3]])
            sage: f.integral()
            Piecewise defined function with 3 parts, [[(-Infinity, -3), (x^3 + 9*x^2 + 27*x)/3 + 9],
            [(-3, 0), (x^2 + 6*x)/2 + 9/2], [(0, +Infinity), 3*x + 9/2]]
```

in the docstring. Is this mixing of x's and y's intended or a typo? If intended, why?

2) I would have perferred that you add yourself to the AUTHR field at the top and add 


```
AUTHOR:
  P Butler
```

in the docstring of the function itself. Not crutial, but it will help others in the future know which part is whose.

3) You have the comment:



```
            # if this piece starts at negative infinity, we won't
            # try to compute the definite integral of the piece.
```

yet you have the definite integral

```

            sage: f1(x) = e^(-abs(x))
            sage: f = Piecewise([[(-infinity, infinity), f1]])
            sage: f.integral(definite=True)
            2
```

Could you explain this please? I think maybe you meant to say 
"...try to compute the indefinite...":

```
sage: f.integral()
Piecewise defined function with 1 parts, [[(-Infinity, +Infinity), -integrate(e^(-abs(x)), x, x, +Infinity)]]
```

If so, could you add this example and comment to the docstring please?


If you agree to all this, could you just make a small patch to go on top of the previous 2 so I can just apply it in my clone, run sage -t, and give this a positive review?


---

Attachment

I've attached `docstring.patch` which fixes these issues.


---

Comment by wdj created at 2009-01-25 20:05:01

These last three patches apply cleanly to 3.3.alpha2 and sage -t passes.

I'm giving this a positive review, finally, Thanks Paul for making the changes.


---

Comment by mabshoff created at 2009-01-28 16:30:26

I am seeing two doctests failure:

```
sage -t -long "devel/doc/const/const.tex"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha3/devel/doc/const/const.tex", line 525:
    : f.integral()
Expected:
    3
Got:
    Piecewise defined function with 2 parts, [[(0, 1), x^3/3], [(1, 2), (15*x - x^3)/3 - 13/3]]
**********************************************************************
```

and

```
sage -t -long "devel/sage/sage/calculus/wester.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha3/devel/sage/sage/calculus/wester.py", line 454:
    : f.integral()
Expected:
    100
Got:
    Piecewise defined function with 2 parts, [[(-10, 0), 50 - x^2/2], [(0, 10), x^2/2 + 50]]
**********************************************************************
```


If someone posts additional patches please also fold the patches together.

Cheers,

Michael


---

Attachment


---

Attachment

Ok, I've added the patches.

`piecewise_all_patches.patch` fixes the problem in `calculus/wester.py` and _replaces all previous patches_ that are part of this ticket.

`const_doctest.patch` fixes the problem in `doc/const/const.tex`.


---

Comment by wdj created at 2009-01-29 21:42:51

Two strange things:

(1) For some reason, I cannot apply the const patch to 3.3.alpha2. However, the diff looks good to me.

(2) I applied the "all" patch. This is what I got (intel macbook running 10.4):


```
...
The following tests failed:


        sage -t  "devel/sage/sage/interfaces/maple.py"
        sage -t  "devel/sage/sage/interfaces/octave.py"
        sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"
```


*However*, I know const.tex fails (see Michael's comment above), so I ran sage -testall and waited for the doctests to finish (which is near the beginning of the process). Sure enough,


```
Testing Sage constructions guide
sage -t  "devel/doc/const/const.tex"                        
**********************************************************************
File "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.3.alpha2/devel/doc/const/const.tex", line 525:
    : f.integral()
Expected:
    3
Got:
    Piecewise defined function with 2 parts, [[(0, 1), x^3/3], [(1, 2), (15*x - x^3)/3 - 13/3]]
**********************************************************************
```

So I think sage -testall is not reporting all the failures on my machine for some reason.

In any case, I would gives this a positive review if I knew it would pass sage -testall. However, it isn't clear to me if the output of sage -testall after this patch is "positive enough" to make a "positive review" appropriate. Any suggestions Michael?


---

Comment by pbutler created at 2009-01-31 22:05:50

When I ran `-testall` on my own install, only one test failed. I don't recall which, but it was a `.tex` file. Oddly enough, when I ran just that file's test it passed.

I'm not sure why the polynomial ring test failed on yours but not on mine. Maybe I'm not working with the latest version of sage. I can understand the interface tests failing, because I don't have those interfaces enabled (unfortunately, I don't have my Maple CD with me so I can't test it, unless the interface works with a remote server).


---

Comment by wdj created at 2009-01-31 22:44:19

If it was a *.tex file then it might have been a doc test failure. Can you please run sage -testall on your machine again? 

I ran my tests on an old intel macbook, which might have it's own oddities.


---

Comment by pbutler created at 2009-02-01 04:29:12

This time, a different test failed. Same as last time, when I ran that test by itself it passed.


```
./sage -testall

[snip]

----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage/sage/rings/qqbar.py"
Total time for all tests: 5392.0 seconds
Please see /home/paul/sage/tmp/test.log for the complete log from this test.
paul@wildcard:~/sage$ ./sage -t "devel/sage/sage/rings/qqbar.py"
sage -t  "devel/sage/sage/rings/qqbar.py"                   
	 [27.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 27.4 seconds
paul@wildcard:~/sage$ 
```


From the log:


```
sage -t  "devel/sage/sage/rings/qqbar.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
     [360.4 s]
```


So it was just a timeout, not a bad value. Is there a way to disable or extend timeouts?


---

Comment by wdj created at 2009-02-01 13:17:50

(a) You can try sage -t -long (see sage -advanced for the details), but that might not help in this case.

(b) Since Michael didn't respond with a suggestion of what I should do in this case, 
based on your tests, and my visual inspection of the doc patch
I couldn't get to apply, I'm giving this a positive review again. It might get kicked back 
though if Michael has problems applying it too. I'm guessing you are using an older version of Sage than I and the problem is someone else made changed since you created your doc patch.


---

Comment by mabshoff created at 2009-02-02 05:10:06

const_doctest.patch applies cleanly for me. The timeout issue will not go away with -long since this is a pexpect problem.

I did not try the patch and I am hesitant to merge it since it changes default behavior. I do remember a discussion about this on sage-devel, so if someone could point me to that and show me that we agreed on this change I am more than happy to merge this patch.

Cheers,

Michael


---

Comment by wdj created at 2009-02-02 12:39:25

The thread was


```
http://groups.google.com/group/sage-devel/browse_thread/thread/f6cb26796d39c67/c19f18e80a65164e?lnk=gst&q=Integral+of+piecewise+functions#c19f18e80a65164e
```

(or search "Integral of piecewise functions" Dec 6, 2008).

I can try to install the patches on my work machine but it will take several days to even
install the latest version of Sage. Recently, they significantly lowered the download speed for 
everyone for some reason.


---

Comment by mabshoff created at 2009-02-05 11:53:16

I checked the above thread and I am not seeing any consensus by a majority of Sage people that this change is a good idea. I still think it should go in, but I would like to see 

 * a discussion on sage-devel where at least a certain number of people sign off on this change
 * a detailed entry that can be added to the Sage 3.3 release notes about this change showing the before and after, changed defaults, etc.

I am sorry to be a pain here, but this is how it is :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 23:17:02

Thanks Paul,

there seems to be a strong consensus to make this go in (and William signed off on it, too), so this will be in 3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 23:17:02

Changing priority from minor to major.


---

Comment by mabshoff created at 2009-02-09 08:26:22

Resolution: fixed


---

Comment by mabshoff created at 2009-02-09 08:26:22

Merged const_doctest.patch and piecewise_all_patches.patch in Sage 3.3.rc0.

Mike: const_doctest.patch touches one doctest in const.tex.

Cheers,

Michael
