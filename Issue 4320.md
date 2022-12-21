# Issue 4320: linear codes improvements

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-10-18 20:31:09

Assignee: rlm

This is a patch which incorporates several changes in linear_codes.py which should speed up (and in some cases do:-) some coding theory computations considerably. It adds interfaces to Cython and C functions of Robert Miller, CJ Tjhal, and Jeffery Leon. 
Speed up of minimum_distance (for codes over GF(2) and GF(3)), the spectrum (=weight_distribution), and permutation_automorphism_group are expected and in most cases achieved. (Also a new function is_permutation_equivalent was added, which interfaces with Robert Miller's double coset partition refinement code.) 

A few points that the referee might want to look at in particular. 
(1) At least one of the functions (code2leon) opens, reads and writes, and closes files. I think I did it correctly, but I read keeping files open is a bad thing, so I hope it was done correctly.
(2) There is a ridiculously slow line which lists the codewords of a given weight. For some reason, GAP (and Guava) is much much faster. It occurs in the permutation_automorphism_group and is commented so you can find it easily. Maybe I am creating the list wrong?

In any case, it passes sage -testall and optional methods were added to the problematical methods, so one always has the option of using the fastest method.



---

Comment by wdj created at 2008-10-18 20:32:08

based on 3.1.4


---

Attachment


---

Comment by rlm created at 2008-10-20 17:51:23

David,

The code here looks pretty good. I think it's ready to merge except for one thing: When you create a file to be read by Leon's programs (or for any other reason, really), you should be creating it in a temp directory which gets automatically cleaned up. You can get one by doing `from sage.misc.misc import SAGE_TMP`.


---

Comment by mabshoff created at 2008-10-20 17:56:27

Another thing: SAGE_ROOT can also easily be accessed and things like

```
rt = commands.getoutput("echo $SAGE_ROOT")
```

are bad. Another thing is the hard coding of the executable name since one has to append ".exe" on Cygwin for example.

Cheers,

Michael


---

Comment by was created at 2008-10-20 19:52:47

Here's a session that illustrates several of the things you need to change
in this patch, evidently:

```
sage: sage.misc.misc.SAGE_ROOT        # sage root dir
'/home/was/build/sage-3.1.3.alpha3'
sage: sage.misc.misc.SAGE_TMP         # location of sage tmp dir; deleted on sage exit
'/home/was/.sage//temp/sage/21351/'
sage: sage.misc.misc.tmp_filename()   # a temp filename, which you can use
'/home/was/.sage//temp/sage/21351//tmp_0'
sage: sage.misc.misc.tmp_dir()
'/home/was/.sage/temp/sage/21351/dir_0'  # creates a temp directory for you
```



---

Comment by wdj created at 2008-10-23 00:10:56

Thanks for all these great comments. 
I have had the patch ready for a day or so now but am having trouble with the process. Problem: I run sage -t on linear_codes.py and code_constructions.py. They pass. sage -testall fails every time with this:


```
 sage -t  devel/sage/sage/coding/linear_code.py              **********************************************************************
File "/home/wdj/sagefiles/sage-3.2.alpha0/tmp/linear_code.py", line 1950:
    sage: C.spectrum(method="leon")
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_44[10]>", line 1, in <module>
        C.spectrum(method="leon")###line 1950:
    sage: C.spectrum(method="leon")
      File "/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 2009, in spectrum
        Wts[x[0]]=x[1]
    IndexError: list assignment index out of range
**********************************************************************
```

I cannot figure this one out.

Any ideas?

The new patch is rebased on 3.2.alpha0 and does not (I'm pretty sure) depend on the other patch.


---

Comment by wdj created at 2008-10-23 00:11:55

based on 3.2.alpha0 and is a stand-alone patch.


---

Attachment

I wonder if this is somehow because of the fact that if you run the Leon code command wtdist on the command line directly you get "smash stack" and (memory errors resulting in?) traceback messages? This is a known issue (discovered by Robert Miller and Tom Boothby) and I have added a warning line to the docstring.
I don't understand when this does not arise for sage -t and does for sage -testall though, so easily could be completely wrong.


---

Comment by wdj created at 2008-10-24 09:55:00

This patch also has this property for 3.1.4 (ie, patch applies cleanly, sage -testall fails for linear_code but sage -t passes for linear_code):


```
wdj`@`hera:~/sagefiles/sage-3.1.4$ ./sage -testall       

<snip>

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/coding/linear_code.py
Total time for all tests: 5448.1 seconds
Please see /home/wdj/sagefiles/sage-3.1.4/tmp/test.log for the complete log from this test.
wdj`@`hera:~/sagefiles/sage-3.1.4$ ./sage -t  devel/sage/sage/coding/linear_code.py
sage -t  devel/sage/sage/coding/linear_code.py
         [17.8 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 17.8 seconds

```

Has anyone seen this kind of behaviour before?


---

Comment by wdj created at 2008-10-25 01:49:57

I installed sage-3.2.alpha0 on an intel macbook, OS10.4, and pretty much the same thing happened. (linear_code failed sage -testall but passed sage -t.) 
However, this time group_algebra also failed, though it seems completely unrelated. (I don't use that module in this version - but it's on the TODO list!)


---

Comment by wdj created at 2008-10-26 14:29:54

I think I might have a vague clue why this latest patch passes sage -t but not sage -testall (this happens for different versions of sage and on both ubuntu and mac OS10.4, as well). The main different in this case between sage -t and sage -testall is that sage -testall records the results in a logfile and sage -t does not. The command line version of the spectrum(method="leon") method has a traceback. Somehow I think this messes with the buffer and then logging is screwed up.

In any case, the attached patch (which is to be applied *after* the patch number 2) fixes the docstrings so that (1) the tests pass (sage -testall as well as sage -t) and (2) I didn't just delete test computations (which I thought would be "cheating":-), but just rephrased them.


---

Attachment

also based on 3.2.alpha0. To be applied after trac_4320-linear-codes2.patch


---

Comment by mabshoff created at 2008-10-26 14:37:23

Replying to [comment:6 wdj]:
> I wonder if this is somehow because of the fact that if you run the Leon code command wtdist on the command line directly you get "smash stack" and (memory errors resulting in?) traceback messages?

I am not really sure we want to support this code as long as it seemingly does not work correctly, i.e. smashing the stack and heaps of memory errors do not really bode well for that code. IIRC the code has been GPLed and sooner or later the code by rlm will cover most of the functionality, so I would highly recommend that we dump wtdist as soon as possible unless someone fixes it.

Cheers,

Michael


---

Comment by wdj created at 2008-10-26 14:48:13

(1) I basically agree. But please note method="leon" is not the default - only one option. Since Leon's code is hard to use directly, the sage interface for it is useful I hope.

(2) I was not aware Robert Miller was working on weight distribution code. The Cython code he wrote for automorphism groups uses totally different ideas, so that would be a completely separate project. I would be very happy to be corrected on that though!

(3) I hope everything is okay for now though.


---

Comment by mabshoff created at 2008-10-26 15:31:25

Replying to [comment:12 wdj]:
> (1) I basically agree. But please note method="leon" is not the default - only one option. Since Leon's code is hard to use directly, the sage interface for it is useful I hope.

Yes, I know :)

> (2) I was not aware Robert Miller was working on weight distribution code. The Cython code he wrote for automorphism groups uses totally different ideas, so that would be a completely separate project. I would be very happy to be corrected on that though!

Ok, I am might be totally wrong here. In the end the hope is that the code can either be ported to Sage or fixed. Either way, I just want to avoid adding dependencies to crappy code where I will end up holding the short stick on the platforms I am porting to.

> (3) I hope everything is okay for now though.

Yeah, let's hope someone does review this patch quickly then.

Cheers,

Michael


---

Comment by rlm created at 2008-11-11 21:15:14

See also #4495


---

Comment by wdj created at 2008-11-11 23:02:40

I'd be happy to add a patch to link to #4495 once it is implemented!


---

Comment by mabshoff created at 2008-11-21 06:20:23

rlm gave this a positive review off-list providing doctests pass and I am happy with it.

Cheers,

Michael


---

Attachment

based on 3.1.4 but applies to 3.2 as well. Goes on top of patches 2 and 3


---

Comment by wdj created at 2008-11-22 13:17:35

I got an off-trac review of Dan Gordan last night, who had a couple of complaints (one about the optional method "gap+verbose" for a non-binary code and another was that is_permutation_equivalent did not first check that the lengths of the 2 codes were equal). These were easy fixes, so I hope it s okay to add them as well. Applies okay and passes tests on my macbook.
Michael: hope this is not an inconvenience.


---

Comment by mabshoff created at 2008-11-25 13:09:12

Hi David,

One more thing to fix after all: code2leon creates the file "output" into the cwd:

```
sage: open("output").close()
```

I will take another look to make sure there is no other case like that and then this can go in. Doctests pass for me.

Sorry for the tardy review :(

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 13:11:16

And I saw two more cases of 'open("output")' in the first file, so please make sure to fix all three cases. Pending those fixes this patch finally gets a positive review from my end. You might also want to consider posting a cumulative patch.

Cheers,

Michael


---

Comment by wdj created at 2008-11-25 13:13:05

Better late than never:-) However, I don't know what this means:
"One more thing to fix after all: code2leon creates the file "output" into the cwd: ..."
cwd? Once I know this, possibly I can figure out how to fix it...


---

Comment by mabshoff created at 2008-11-25 13:15:45

Hi David,

cwd == current working directory. The problem is that the user who doctests might not have write permission in the Sage tree. So if you create any files they should always reside in $SAGE_TMP.

Cheers,

Michael


---

Comment by wdj created at 2008-11-25 13:36:36

Okay, no problem - that I can fix.

It is it easy to create a cumulative patch (short of retyping all the changes into a new clone)?


---

Comment by mabshoff created at 2008-11-25 13:38:28

If you have a fresh tree just just use GNU patch to apply all three patches, then fix the issue, commit and export. If that is trouble just post a patch on top and I will merge all four patches. To review the changes a new patch would be better, so do it the way you prefer.

Cheers,

Michael


---

Attachment

to be applied on top of patches 2, 3, and 4


---

Comment by wdj created at 2008-11-26 01:54:23

I just made a small patch with the changes you suggested. This makes it easier for you to read, me to create and test, and i have more confidence that it is the desired patch.

Applies okay and passes tests on my intel macbook.


---

Comment by mabshoff created at 2008-11-26 01:56:51

The last patch is still not 100% fool proof since doctesting the same file in parallel introduces race conditions, but that does not stop me from giving the cumulative four patches a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-26 09:35:59

Resolution: fixed


---

Comment by mabshoff created at 2008-11-26 09:35:59

Merged trac_4320-linear-codes2.patch through trac_4320-linear-codes5.patch in Sage 3.2.1.alpha1

Cheers,

Michael
