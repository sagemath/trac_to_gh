# Issue 7820: upgrade gfan to latest release (0.4plus)

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-01-02 23:04:14

Assignee: tbd

CC:  mhampton was

See
http://www.math.tu-berlin.de/~jensen/software/gfan/gfan.html

Release 0.4plus has improved performance and a lot of new functionality.

Ccing Marshall and William since they are the package maintainers.


---

Comment by AlexGhitza created at 2010-01-03 03:28:03

An updated spkg is up at

http://sage.math.washington.edu/home/ghitza/gfan-0.4plus.spkg

Some fixes are needed in the Sage library because of the upgrade.  I am attaching a patch that deals with the most obvious one, but there are some doctest failures left:


```
sage -t -long "devel/sage-main/sage/rings/polynomial/groebner_fan.py"
**********************************************************************
File "/virtual/scratch/ghitza/sage-4.3/devel/sage-main/sage/rings/polynomial/groebner_fan.py", line 301:
    sage: pf.rays()
Expected:
    [[1, 0, 0], [-2, -1, 0], [1, 1, 0], [0, -1, 0], [-1, 1, 0]]
Got:
    [[-1, 0, 1], [-1, 1, 0], [1, -2, 1], [1, 1, -2], [2, -1, -1]]
**********************************************************************
File "/virtual/scratch/ghitza/sage-4.3/devel/sage-main/sage/rings/polynomial/groebner_fan.py", line 354:
    sage: pf._str_()
Expected:
    '_application PolyhedralFan\n_version 2.2\n_type PolyhedralFan\n\nAMBIENT_DIM\n3\n\nDIM\n3\n\nLINEALITY_DIM\n0\n\nRAYS\n1 0 0\t# 0\n0 1 0\t# 1\n0 0 1\t# 2\n\nN_RAYS\n3\n\nLINEALITY_SPACE\n\nORTH_LINEALITY_SPACE\n0 0 1\n0 1 0\n1 0 0\n\nF_VECTOR\n1 3 3 1\n\nCONES\n{}\t# Dimension 0\n{0}\t# Dimension 1\n{1}\n{2}\n{0 1}\t# Dimension 2\n{0 2}\n{1 2}\n{0 1 2}\t# Dimension 3\n\nMAXIMAL_CONES\n{0 1 2}\t# Dimension 3\n\nPURE\n1\n'
Got:
    '_application PolyhedralFan\n_version 2.2\n_type PolyhedralFan\n\nAMBIENT_DIM\n3\n\nDIM\n3\n\nLINEALITY_DIM\n0\n\nRAYS\n0 0 1\t# 0\n0 1 0\t# 1\n1 0 0\t# 2\n\nN_RAYS\n3\n\nLINEALITY_SPACE\n\nORTH_LINEALITY_SPACE\n1 0 0\n0 1 0\n0 0 1\n\nF_VECTOR\n1 3 3 1\n\nMY_EULER\n0\n\nSIMPLICIAL\n1\n\nPURE\n1\n\nCONES\n{}\t# Dimension 0\n{0}\t# Dimension 1\n{1}\n{2}\n{0 1}\t# Dimension 2\n{0 2}\n{1 2}\n{0 1 2}\t# Dimension 3\n\nMAXIMAL_CONES\n{0 1 2}\t# Dimension 3\n'
**********************************************************************
File "/virtual/scratch/ghitza/sage-4.3/devel/sage-main/sage/rings/polynomial/groebner_fan.py", line 413:
    sage: pf.rays()
Expected:
    [[1, 0, 0], [-2, -1, 0], [1, 1, 0], [0, -1, 0], [-1, 1, 0]]
Got:
    [[-1, 0, 1], [-1, 1, 0], [1, -2, 1], [1, 1, -2], [2, -1, -1]]
**********************************************************************
File "/virtual/scratch/ghitza/sage-4.3/devel/sage-main/sage/rings/polynomial/groebner_fan.py", line 138:
    sage: _cone_parse(tstr.fan_dict['CONES'])
Expected:
    {1: [[0], [1], [3], [2], [4]], 2: [This is the Trac macro *2, 4* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 4-macro)}
Got:
    {1: [[0], [1], [2], [3], [4]], 2: [This is the Trac macro *2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 3-macro)}
**********************************************************************
File "/virtual/scratch/ghitza/sage-4.3/devel/sage-main/sage/rings/polynomial/groebner_fan.py", line 824:
    sage: pf.rays()
Expected:
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
Got:
    [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
**********************************************************************
File "/virtual/scratch/ghitza/sage-4.3/devel/sage-main/sage/rings/polynomial/groebner_fan.py", line 1243:
    sage: G.tropical_basis()
Exception raised:
    Traceback (most recent call last):
      File "/virtual/scratch/ghitza/sage-4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/virtual/scratch/ghitza/sage-4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/virtual/scratch/ghitza/sage-4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_48[5]>", line 1, in <module>
        G.tropical_basis()###line 1243:
    sage: G.tropical_basis()
      File "/virtual/scratch/ghitza/sage-4.3/local/lib/python/site-packages/sage/rings/polynomial/groebner_fan.py", line 1267, in tropical_basis
        X = [S(f) for f in B]
      File "multi_polynomial_libsingular.pyx", line 608, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:5471)
        raise TypeError
    TypeError
**********************************************************************
File "/virtual/scratch/ghitza/sage-4.3/devel/sage-main/sage/rings/polynomial/groebner_fan.py", line 1294:
    sage: pf.rays()
Expected:
    [This is the Trac macro *-1, 0, 0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-1, 0, 0-macro)
Got:
    [This is the Trac macro *-2, 1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-2, 1, 1-macro)
**********************************************************************
7 items had failures:
   1 of   7 in __main__.example_11
   1 of   6 in __main__.example_13
   1 of   7 in __main__.example_17
   1 of   8 in __main__.example_3
   1 of   6 in __main__.example_35
   1 of   6 in __main__.example_48
   1 of   7 in __main__.example_50
***Test Failed*** 7 failures.
For whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_groebner_fan.py
	 [8.1 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/rings/polynomial/groebner_fan.py"
Total time for all tests: 8.2 seconds
```


I can try to figure out what's happening, but Marshall is likely to be better at it.


---

Comment by AlexGhitza created at 2010-01-03 03:28:03

Changing status from new to needs_work.


---

Comment by mhampton created at 2010-01-03 17:15:57

Yes, I can try to work on fixing those issues.  This relates a little bit to some major refactoring of the polyhedron class over at ticket #7109.  If you could review that I'd  greatly appreciate it.

Thanks very much for working on the gfan upgrade.


---

Comment by mhampton created at 2010-01-03 23:18:56

I'm starting to think that rays doctest might have exposed a bug in gfan itself, I'll check with Anders.


---

Comment by mhampton created at 2010-01-04 21:18:48

The new output is correct; the rays for that example are not uniquely determined.  So the doctests just need to be changed to match the new output.


---

Comment by drkirkby created at 2010-01-05 05:05:15

It would be good if the Makefile could be changed so that the C compiler is set by CC and the C++ compiler by CXX, and the flags CFLAGS and CXXFLAGS used. 

The Sun compiler was not happy with the earlier version. 

I dont mind trying to sort the makefile out if you want. 

Dave


---

Comment by AlexGhitza created at 2010-01-05 10:49:11

Replying to [comment:6 drkirkby]:
> It would be good if the Makefile could be changed so that the C compiler is set by CC and the C++ compiler by CXX, and the flags CFLAGS and CXXFLAGS used. 
> 
> The Sun compiler was not happy with the earlier version. 
> 
> I dont mind trying to sort the makefile out if you want. 

Sure!  That would make it easier for me.


---

Comment by drkirkby created at 2010-01-05 11:09:17

I'll do that today, by 1800 GMT today (7 hours from now). 

It was coincidental, but I'd just hit the problem on version 0.3 and posted something to sage-devel about this. William was willing to remove gfan, as he was no aware of anyone using it. You might want to put a comment on sage-devel about it.  

Dave


---

Comment by drkirkby created at 2010-01-05 14:06:22

I'm a bit concerned about the number of compiler warnings here from g++, even though  -Wall was *not* added. 

On the 0.3 release, the Sun compiler rejected some code, saying things were masking others, and functions expected to return something did not. 

I'll get the Makefile fixed so gfan 0.4plus it at least attempts a build with Sun's compiler, but I suspect Sun's will reject some of the code as being invalid. 

Dave


---

Comment by drkirkby created at 2010-01-05 15:08:58

The 'src' directory at 

http://sage.math.washington.edu/home/ghitza/gfan-0.4plus.spkg

has no 'makefile' yet when I download the source code from 

http://www.math.tu-berlin.de/~jensen/software/gfan/gfan0.4plus.tar.gz

there is a makefile. 

I think we should keep that, then overwrite it with a patch, so there is a record of the actual source code. i.e. something like 

cp patches/makefile src/makefile

That way, the original source is untouched. I rather start with the original code, and make changes to that, rather than someone elses makefile. 

Dave


---

Comment by drkirkby created at 2010-01-05 18:05:18

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-01-05 18:05:18

Well, I'm 3 minutes late, but I hope you will excuse that. 

I've put a new spkg  at 

http://boxen.math.washington.edu/home/kirkby/portability/gfan-0.4plus/

I used a clean source, and just edited spkg-install and made patches/Makefile. 

Can you check I've note undone anything you have done, and check it works on a couple of systems. I've only checked on Solaris here. 

Dave


---

Comment by AlexGhitza created at 2010-01-05 22:40:48

Replying to [comment:10 drkirkby]:
> The 'src' directory at 
> 
> http://sage.math.washington.edu/home/ghitza/gfan-0.4plus.spkg
> 
> has no 'makefile' yet when I download the source code from 
> 
> http://www.math.tu-berlin.de/~jensen/software/gfan/gfan0.4plus.tar.gz
> 
> there is a makefile. 
> 
> I think we should keep that, then overwrite it with a patch, so there is a record of the actual source code. i.e. something like 
> 
> cp patches/makefile src/makefile
> 
> That way, the original source is untouched. I rather start with the original code, and make changes to that, rather than someone elses makefile. 
> 
> Dave 

I'm not sure what spkg file you're looking at.  I just rechecked the one I gave above and it has the original Makefile in src/ and a modified one in patches/.

Anyway, it's not important.  I'm looking at your spkg now.


---

Comment by drkirkby created at 2010-01-05 22:51:03

Sorry about the confusion.

I can only assume I confused it with the 0.3 version by mistake. I certainly downloaded your one. 

I downloaded the gfan-0.4plus source code, and put that in the package.


---

Comment by AlexGhitza created at 2010-01-05 23:39:25

It looks good, thanks for this!

So far I've tested it on 32-bit archlinux and 64-bit archlinux without problems.  Same on 32-bit MacOSX 10.5.

There are a couple of minor things in your spkg, which I can easily fix today: we normally strip the original sources of documentation and similar things.  In this case, we get rid of src/doc, src/examples, and src/homepage.  This gives an spkg that's 220kb instead of 680kb.  There are also a few typos in Makefile and SPKG.txt.

As I said, this is great, and I can make these minor fixes today.


---

Comment by drkirkby created at 2010-01-05 23:57:43

It's good to hear it was mostly there. 

At least one can to build gfan with Sun's compiler now, even though it soon fails. Before it was impossible to get anything useful done, as gcc was hard-coded in the Makefile. Now at least one can see the error messages. Unfortunately, whilst I know C, I do not know C++, so don't have much clue about how to resolve the issues. I'll forward them upstream. 

Dave


---

Comment by AlexGhitza created at 2010-01-06 13:50:06

apply after the gfan-0.4plus spkg


---

Attachment

OK, I have replaced the spkg with one that has the small fixes to David's version.  See the ticket description for the URL.  This spkg also patches `src/polynomial.cpp` to fix a bug that appeared in gfan-0.4plus and was caught by one of our doctests (YAY for doctests!)

I have also replaced the patch to the Sage library with one that deals with all the issues raised by the upgrade.  All of this is now ready for review.


---

Comment by AlexGhitza created at 2010-01-06 14:03:17

Replying to [comment:17 AlexGhitza]:
> OK, I have replaced the spkg with one that has the small fixes to David's version.  See the ticket description for the URL.  This spkg also patches `src/polynomial.cpp` to fix a bug that appeared in gfan-0.4plus and was caught by one of our doctests (YAY for doctests!)

Forgot to mention that the bug was reported upstream, and Anders Jensen quickly sent us the fix that we are now using.  It will be incorporated in the next version of gfan.


---

Comment by mhampton created at 2010-01-23 15:41:12

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-01-23 15:41:12

I've tested this and I think it looks good.  There are some minor conflicts with 7109 but I am willing to rebase 7109 against this if it is merged first.

I might not have time until this summer to extend the gfan interface but I am interested in doing so.  If anyone beats me to it I am happy to review.


---

Comment by mvngu created at 2010-01-25 14:11:59

Resolution: fixed


---

Comment by mvngu created at 2010-01-25 14:11:59

Merged in this order:

 1. merged [gfan-0.4plus.spkg](http://sage.math.washington.edu/home/ghitza/gfan-0.4plus.spkg) in the standard spkg repository
 1. [trac_7820.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7820/trac_7820.patch)
