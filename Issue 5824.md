# Issue 5824: Move DSage to its own spkg

Issue created by migration from https://trac.sagemath.org/ticket/5824

Original creator: mabshoff

Original creation time: 2009-04-19 07:46:30

Assignee: yi

DSage isn't actively maintained and not working too well. Since its coverage is basically zero (0.7%) move it to its own spkg and provide hooks that make current code work. These hooks should be deprecated instantly. 

Note the effect on coverage for 3.4.1.rc4:

Before:

```
Overall weighted coverage score:  68.2%
Total number of functions:  22947
We need  401 more function to get to 70% coverage.
We need 1549 more function to get to 75% coverage.
We need 2696 more function to get to 80% coverage.
```

After:

```
Overall weighted coverage score:  69.8%
Total number of functions:  22432
We need   45 more function to get to 70% coverage.
We need 1166 more function to get to 75% coverage.
We need 2288 more function to get to 80% coverage.
```


Cheers,

Michael


---

Comment by was created at 2009-04-19 19:47:06

> To do the move one must also pay careful attention to the unit tests, -sdist, -bdist and setup.py.


Alternatively it could be removed, but have its setup.py configured so it installs into exactly the same place as now.  Then all testing code would work exactly the same as before.  The main difference is that one would no longer see this when starting Sage:

```
changing mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/dsage_setup.py to 755
changing mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/spkg-debian-maybe to 755
changing mode of /scratch/wstein/build/sage-3.4.1.rc2/local/bin/dsage_worker.py to 755
```



---

Comment by was created at 2009-04-19 19:59:54

patch to apply to main sage library (hg_sage.apply(...)); this deletes all of dsage from the main library


---

Attachment

this is dsage as a complete self-contained spkg


---

Attachment

replace SAGE_ROOT/spkg/install by the attached file


---

Attachment

replace SAGE_ROOT/spkg/standard/deps by the attached file


---

Comment by jhpalmieri created at 2009-04-19 20:21:59

If we're deprecating dsage, I think we should remove its section from the tutorial.  (Remove the file 'distributed.rst' and delete the appropriate line from 'index.rst'.) I can provide a patch if you think it's a good idea.

I've never been convinced that it belonged there anyway, but that's another issue...


---

Comment by mabshoff created at 2009-04-19 23:33:45

I would prefer to install the DSage.spkg outside the tree for various reasons:

 * As is it still counts against our coverage.
 * Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.
 * Sage 4.0 seems to be a good point to have the separation, so I am all for it getting done in the next 4 weeks :)

Cheers,

Michael


---

Comment by was created at 2009-04-19 23:43:19

>    * As is it still counts against our coverage.

No it doesn't.  It's *not* installed in devel/sage/sage, so it does not count against our coverage.

>    * Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.

I strongly disagree. They can still do development, though a repo would be needed if one wanted to trade patches.  This is totally orthogonal to anything I just did.


---

Comment by was created at 2009-04-19 23:50:29

Michael did have one interesting point in chat, which is that if you do

```
rm -rf devel/sage/build
```

then dsage is gone too, so it has to be reinstalled.

Note that `sage -ba` does not do `rm -rf devel/sage/build`, but instead just touches all cython files.


---

Comment by mabshoff created at 2009-04-20 00:12:12

Replying to [comment:6 was]:
> >    * As is it still counts against our coverage.
> 
> No it doesn't.  It's *not* installed in devel/sage/sage, so it does not count against our coverage.

Yes, I am wrong on that point.

> >    * Now you cannot commit patches against DSage any more since it isn't in the repo. If someone wants to do development they should do so in a different python package.
> 
> I strongly disagree. They can still do development, though a repo would be needed if one wanted to trade patches.  This is totally orthogonal to anything I just did.
> 

I had assumed wrongly as above that the DSage code would end up in devel/sage which it clearly doesn't, so I am wrong again. 

What I do not like is subpackages installing into a tree in site-packages, i.e. the latest twisted does that with web2 I believe. 

The main question whether we do this or not is:

 * Are we going to fix/rewrite DSage? In that case it should stay in the tree.
 * If we are going to deprecate it we should move it to its own spkg and add deprecation warnings. The question then is what is going to happen after DSage and I don't think there is a clear answer to that question yet.

Cheers,

Michael


---

Attachment

apply this to the hg_sage repo right after trac_5824.patch; it updates setup.py


---

Comment by mabshoff created at 2009-04-30 09:56:37

Positive review. Some of the files removed had some slight rejects, but I rebased the patch :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 10:25:57

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 10:25:57

Merged in Sage 3.4.2.rc0.

Cheers,

Michael
