# Issue 839: write pexpect interface to R

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-10-07 18:55:13

Assignee: mhansen

CC:  mhansen schilly




---

Comment by mhansen created at 2007-10-07 18:55:21

Changing status from new to assigned.


---

Comment by mhampton created at 2007-10-31 15:52:59

This is of huge importance to the wider adoption of sage.  Thank you for working on it.


---

Comment by mabshoff created at 2008-01-26 14:45:19

Is this still relevant or doe rpy take care of all of this?

Cheers,

Michael


---

Comment by was created at 2008-01-27 04:00:24

This is *definitely* still very relevant.  It would, e.g., make it possible to have an R mode in the notebook.


---

Attachment

Add notebook support for R


---

Comment by schilly created at 2008-03-20 20:53:45

old but still relevant: [The R language – a short companion](http://cran.r-project.org/doc/manuals/R-lang.pdf) .. summarizes much of the specific aspects and ideas behind the R language.


---

Comment by schilly created at 2008-03-25 01:25:03

attached bundle for a first "working" version. this is still not stable to use, but: 

i've setup a wiki page to show its functionality: [http://wiki.sagemath.org/R](http://wiki.sagemath.org/R)

still missing:
 * documentation + tests
 * plotting (just started something, but i don't understand how it should be done)
 * latex (see source for comments)


---

Comment by schilly created at 2008-03-25 01:25:03

Changing type from defect to enhancement.


---

Attachment

based on previous patches, somewhat working version. see comment no. 9


---

Comment by was created at 2008-03-25 05:29:55

This is AWESOME!!!!


---

Comment by was created at 2008-03-25 05:38:20

The second thing I try -- use R's install.packages -- leads to problems:

```
sage: r.inst[tab key]
r.install_packages    r.installed_packages  
sage: r.install_packages('HSAUR')
Error: object "sage3" not found
sage: r.install.packages('HSAUR')
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/was/edu/2007-2008/sage/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'RFunction' object has no attribute 'packages'
```


This *does* start to work, but eventually fails (that this fails may be my fault -- maybe HSAUR is not longer at CRAN):

```
sage: r.eval('install.packages("HSAUR")')
[GUI select mirror]
sage: r.eval('install.packages("HSAUR")')
"--- Please select a CRAN mirror for use in this session ---\n\x1b[1mLoading Tcl/Tk interface ... \x1b[0m\x1b[1mdone\n\x1b[0m\x1b[1malso installing the dependencies \xe2\x80\x98lattice\xe2\x80\x99, \xe2\x80\x98VR\xe2\x80\x99, \xe2\x80\x98scatterplot3d\xe2\x80\x99\n\n\x1b[0m\x1b[1mtrying URL 'http://cran.wustl.edu/bin/macosx/universal/contrib/2.6/lattice_0.17-6.tgz'\n\x1b[0m\x1b[1mContent type 'application/x-tar'\x1b[0m\x1b[1m length 572946 bytes (559 Kb)\n\x1b[0m\x1b[1mopened URL\n\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m\n\x1b[0m\x1b[1mdownloaded 559 Kb\n\n\x1b[0m\x1b[1mtrying URL 'http://cran.wustl.edu/bin/macosx/universal/contrib/2.6/VR_7.2-41.tgz'\n\x1b[0m\x1b[1mContent type 'application/x-tar'\x1b[0m\x1b[1m length 969063 bytes (946 Kb)\n\x1b[0m\x1b[1mopened URL\n\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m\n\x1b[0m\x1b[1mdownloaded 946 Kb\n\n\x1b[0m\x1b[1mtrying URL 'http://cran.wustl.edu/bin/macosx/universal/contrib/2.6/scatterplot3d_0.3-25.tgz'\n\x1b[0m\x1b[1mContent type 'application/x-tar'\x1b[0m\x1b[1m length 516685 bytes (504 Kb)\n\x1b[0m\x1b[1mopened URL\n\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m\n\x1b[0m\x1b[1mdownloaded 504 Kb\n\n\x1b[0m\x1b[1mtrying URL 'http://cran.wustl.edu/bin/macosx/universal/contrib/2.6/HSAUR_1.2-2.tgz'\n\x1b[0m\x1b[1mContent type 'application/x-tar'\x1b[0m\x1b[1m length 3750559 bytes (3.6 Mb)\n\x1b[0m\x1b[1mopened URL\n\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m=\x1b[0m\x1b[1m\n\x1b[0m\x1b[1mdownloaded 3.6 Mb\n\n\x1b[0m\nThe downloaded packages are in\n\t/var/folders/lH/lHHJUEtmHlmUGwLs8K2fdE+++TI/-Tmp-//RtmpNYdywT/downloaded_packages\n\x1b[1mWarning message:\n\x1b[0m\x1b[1mdependency \xe2\x80\x98MASS\xe2\x80\x99 is not available "
```



---

Comment by schilly created at 2008-03-25 23:11:37

Replying to [comment:10 was]:
> This is AWESOME!!!!

thx for the flowers ;)

----

*some ideas* and what i'm trying next: (help welcome)

i think installing packages is rather difficult. at my computer, i even don't see the GUI selector or anything else, just hangs. your output, last line, says: `dependency MASS  is not available`. .. but MASS should be pretty standard ...

i'll add a default mirror in the options, but this alone solves nothing. there is a command line option when calling R itself: ` R CMD INSTALL ... ` maybe it's easier to work on that level? separate process and different cmd window...

a good solution could be to avoid installing + local compilation and just ship more packages with R (in standard) and repack additional libraries of packages into optional SPKGs. i think this should be pretty straightforward (R could be easily convinced to search in multiple paths for packages if necessary ...)

i've also not figured out how to plot and why there are missing sage<number> objects. there are certainly many bugs. i'll also try to introduce my custom prompt (appending a command to each line of code) and running R in full silent mode (no prompt, no questions, no nothing, reduced warnings level, ...). restore from last session and searching directories for stored configurations was also enabled --- disabling all this should give much less surprises ;)

also there are bugs in the R-2-Sage converter. e.g. i just had to explain python that NA means None ...

i should also check some details inside the bundled R inside the `./sage -sh` environment. possibly there is something wrong with it, too...


---

Comment by schilly created at 2008-04-09 23:41:05

*attention*: I've updated my work status, but something didn't work with the bundle. Just the one [in the middle (click here)](http://trac.sagemath.org/sage_trac/attachment/ticket/839/839-r-pexpect-schilly-2.hg?changeset=9122) is the interesting one. maybe i should not have updated...


---

Attachment

this replaces all patches from above - better working, but still not stable, repaired


---

Comment by schilly created at 2008-04-11 19:43:41

Replying to [comment:13 schilly]:
> *attention*: ...

i've repaired it. i think this should work now. (concerning the patch ;)


---

Attachment


---

Attachment


---

Comment by was created at 2008-04-20 05:21:36

REFEREE REPORT:

  * I fixed most of the issues I have with typos in docs, incompleteness of docs, etc., in 
sage-839-referee1.patch which should be looked over by Mike Hansen and Schilly.

  * There are still some bugs and serious issues, but they are not show stoppers.  They include:
      * Installing optional packages seems completely broken on OS X.  Maybe also on Linux. 
      * Functions that don't exist:

```
sage: r.nonexistfunction(5)
Error: object "sage1" not found
```

That should give a proper error message.  Also, after doing the above, for some reason all the text in the rest of my session is BOLD.


---

Attachment


---

Comment by mhansen created at 2008-04-20 05:35:51

Yay!

Apply 839.2.hg .  It has all of the patches and is based against 3.0.alpha6.


---

Comment by mabshoff created at 2008-04-20 05:39:02

Resolution: fixed


---

Comment by mabshoff created at 2008-04-20 05:39:02

Merged 839.2.hg in Sage 3.0.rc0
