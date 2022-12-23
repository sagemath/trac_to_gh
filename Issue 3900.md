# Issue 3900: make testing an official pickle jar a part of "make check"

Issue created by migration from https://trac.sagemath.org/ticket/3900

Original creator: was

Original creation time: 2008-08-19 17:50:54

Assignee: tbd

See #3482 and #3899.

Each copy of Sage should include an official pickle jar that gets tested.  This should go in the data directory. 


---

Comment by AlexGhitza created at 2008-09-08 08:36:46

Changing assignee from tbd to mabshoff.


---

Comment by AlexGhitza created at 2008-09-08 08:36:46

Changing component from algebra to build.


---

Attachment


---

Comment by was created at 2008-10-23 21:26:54

You must place this tarball in SAGE_ROOT/data and *leave* it compressed.


---

Attachment


---

Comment by was created at 2008-10-23 21:40:52

Changing priority from critical to blocker.


---

Comment by jsp created at 2008-11-18 15:36:27

I applied the patch, but got


```
sage -t  devel/sage/sage/structure/sage_object.pyx          **********************************************************************
File "/home/jaap/downloads/sage-3.2.rc1/devel/sage/sage/structure/sage_object.pyx", line 750:
    sage: sage.structure.sage_object.unpickle_all(std)
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[6]>", line 1, in <module>
        sage.structure.sage_object.unpickle_all(std)###line 750:
    sage: sage.structure.sage_object.unpickle_all(std)
      File "sage_object.pyx", line 764, in sage.structure.sage_object.unpickle_all (sage/structure/sage_object.c:7475)
    IndexError: list index out of range
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_18
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.rc1/tmp/.doctest_sage_object.pybunzip2: /home/jaap/downloads/sage-3.2.rc1/data/pickle_jar.tar.bz2 is not a bzip2 file.
tar: This does not look like a tar archive
tar: Error exit delayed from previous errors

	 [3.7 s]

```


Jaap


---

Comment by jsp created at 2008-11-18 15:42:29

Sorry for the noise.

Now I put in the correct file and all's well



```
[jaap@paix sage-3.2.rc1]$ ./sage -t  devel/sage/sage/structure/sage_object.pyx
sage -t  devel/sage/sage/structure/sage_object.pyx          
	 [6.6 s]
 
----------------------------------------------------------------------
All tests passed!

So positive review.


```



---

Comment by mabshoff created at 2008-11-18 18:11:18

We need to deal with -sdist and -bdist copying pickle_jar.tar.bz2. One way to do this would be to check the file into the repo, but that seems like a bad idea. 

Thoughts?

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-19 21:19:42

Hi folks,

there does not seem to be any problem with binary distributions, once that file "pickle_jar.tar.bz2" exists. See line 52 of the "sage-bdist" script, where among others the complete subtree under /data is copied over.

As for source distributions, essentially the distribution of the file "pickle_jar.tar.bz2" is not necessary --- it can be (re-)produced from any source distribution by a (very) short sequence of commands that does not change. In that sense it's a "build output". For convenience, one might think about having a make target "make pickle_jar".

But since the doctest introduced by this patch requires the prior existence of this file "pickle_jar.tar.bz2", and since maybe we don't want to produce updated pickle jars for each and every Sage version in say the alpha release cycles, a simplistic spkg could be the solution:

"sage_pickle_jar-X.Y.Z.spkg" containing just the three files "spkg-install", "SPKG.txt", and "pickle_jar.tar.bz2"; and spkg-install just issue a single "cp" command.
Then, e.g. Sage version 3.3.2.alpha4 could still contain the spkg "sage_pickle_jar-3.3.1.spkg".

To make the creation of updated versions of this simplistic spkg easier, using the existing scripts machinery, it would be advisable not to use the directory "data/" to store the file "pickle_jar.tar.bz2", but instead the directory "data/sage_pickle_jar/",
and storing there all these three files. (So a simple "spkg -pkg ..." does the job of creating the updated spkg.)

Of course the naming could also be "std_pickle_jar" instead, or similar.

I'd volunteer to create and test the needed script "spkg-install" resp. that simplistic spkg, opening another ticket for it, if someone gives me a "Yep. Good idea. Go for it!". Then the usual review process would take its course, and this ticket would depend on that other ticket. 

Cheers,

gsw


---

Comment by mabshoff created at 2008-11-19 21:31:02

Replying to [comment:9 GeorgSWeber]:
> Hi folks,
> 
> there does not seem to be any problem with binary distributions, once that file "pickle_jar.tar.bz2" exists. See line 52 of the "sage-bdist" script, where among others the complete subtree under /data is copied over.

Maybe, but in which spkg does the data directory end up? I can see the content of extcode, but not the data directory itself.

> As for source distributions, essentially the distribution of the file "pickle_jar.tar.bz2" is not necessary --- it can be (re-)produced from any source distribution by a (very) short sequence of commands that does not change. In that sense it's a "build output". For convenience, one might think about having a make target "make pickle_jar".

The point is that the *old* pickle jar works.

> But since the doctest introduced by this patch requires the prior existence of this file "pickle_jar.tar.bz2", and since maybe we don't want to produce updated pickle jars for each and every Sage version in say the alpha release cycles, a simplistic spkg could be the solution:
> 
> "sage_pickle_jar-X.Y.Z.spkg" containing just the three files "spkg-install", "SPKG.txt", and "pickle_jar.tar.bz2"; and spkg-install just issue a single "cp" command.
> Then, e.g. Sage version 3.3.2.alpha4 could still contain the spkg "sage_pickle_jar-3.3.1.spkg".
> 
> To make the creation of updated versions of this simplistic spkg easier, using the existing scripts machinery, it would be advisable not to use the directory "data/" to store the file "pickle_jar.tar.bz2", but instead the directory "data/sage_pickle_jar/",
> and storing there all these three files. (So a simple "spkg -pkg ..." does the job of creating the updated spkg.)

We don't want another spkg - that idea was rejected. I am not 100% clear why, but that is what lead to this problem in the first place.

> Of course the naming could also be "std_pickle_jar" instead, or similar.
> 
> I'd volunteer to create and test the needed script "spkg-install" resp. that simplistic spkg, opening another ticket for it, if someone gives me a "Yep. Good idea. Go for it!". Then the usual review process would take its course, and this ticket would depend on that other ticket. 
> 
> Cheers,

> gsw

The easiest solution IMHO would be to check the archive into $SAGE_ROOT/data/extcode/pickle_jar and adjust the path in the patch here.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-19 21:34:47

On closer inspection: we don't even have to check in the pickle jar into the ext repo, so I will just put it in there.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-19 21:43:17

Resolution: fixed


---

Comment by mabshoff created at 2008-11-19 21:43:17

Merged in Sage 3.2.rc2
