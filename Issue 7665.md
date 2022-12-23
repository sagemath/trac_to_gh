# Issue 7665: Make support for R graphics

Issue created by migration from https://trac.sagemath.org/ticket/7665

Original creator: kcrisman

Original creation time: 2009-12-11 20:23:06

Assignee: was

CC:  jason schilly drkirkby jverzani@gmail.com

Keywords: plot, R, graphics, statistics

This is probably hard.  It would increase our potential user base, though, as well as make it possible for people to use Sage in virtually any college course very easily (with the exception of most geometry courses, but a Geogebra plugin would do that).

Examples from the recommended (not currently installed) MASS package; one can certainly come up with one's own examples, this just shows what isn't supported and the current error messages.

```
sage: r.bwplot('MPG.highway ~ Origin', data = 'Cars93')

Warning message:
In grid.newpage() : No png support in this version of R

sage: r.histogram('~ MPG.highway',data='Cars93')


(process:46382): Pango-WARNING **: failed to create cairo scaled font, expect ugly output. the offending font is 'Helvetica 9'

(process:46382): Pango-WARNING **: font_font status is: out of memory

(process:46382): Pango-WARNING **: scaled_font status is: out of memory

(process:46382): Pango-WARNING **: shaping failure, expect ugly output. shape-engine='BasicEngineFc', font='Helvetica 9', text='M'

(process:46382): Pango-WARNING **: failed to create cairo scaled font, expect ugly output. the offending font is 'Helvetica 7.1982421875'

(process:46382): Pango-WARNING **: font_font status is: out of memory

(process:46382): Pango-WARNING **: scaled_font status is: out of memory

(process:46382): Pango-WARNING **: shaping failure, expect ugly output. shape-engine='BasicEngineFc', font='Helvetica 7.1982421875', text='0'

sage: r.plot('MPG.highway ~ Weight', data='Cars93')
NULL
```



---

Comment by kcrisman created at 2010-02-09 14:09:02

Okay, I have dug into this, and here are some preliminary thoughts.

We have a function r.png, which only works if capabilities('png') returns TRUE.  In the default build on Mac, we get

```
> capabilities()
    jpeg      png     tiff    tcltk      X11     aqua http/ftp  sockets 
   FALSE    FALSE    FALSE     TRUE    FALSE    FALSE     TRUE     TRUE 
  libxml     fifo   cledit    iconv      NLS  profmem    cairo 
    TRUE     TRUE     TRUE     TRUE     TRUE    FALSE    FALSE 
```

However, to build with X11 (which would enable png and friends) or with aqua on Mac (which would enable the quartz graphics device), we need to build with certain options.  See [http://CRAN.R-project.org/bin/macosx/RMacOSX-FAQ.html](http://CRAN.R-project.org/bin/macosx/RMacOSX-FAQ.html) and [http://cran.r-project.org/doc/manuals/R-admin.html#Configuration-options](http://cran.r-project.org/doc/manuals/R-admin.html#Configuration-options) for some info. 

On sagenb.org, however, we do have png and Cairo TRUE, though X11 FALSE.  The commands that give various errors on my computer in the description instead give the actual data set (!) on sagenb, except the last one which still returns NULL.  However, the following DOES work (from the documentation in interfaces/r.py):

```
r.png('temp.png')
x = r([1,2,3])
y = r([4,5,6])
r.plot(x,y)
r.dev_off()
```

So it seems that one can do this, but it's annoying.  Similarly:

```
r.png('temp2.png')
r.plot('MPG.highway ~ Weight', data='Cars93')
r.dev_off()
```

works on sagenb.  It's very nice, in fact!

So presumably if we enabled X11 on Mac (perhaps on a case-by-case basis for each version of OSX as in the above websites) we would get this at least, and perhaps also enabling aqua would solve this on Mac.  To be continued...


---

Comment by kcrisman created at 2010-02-09 14:31:48

Another idea would be to change r.plot (not r.png or the 'native' ones like r.bwplot or r.histogram) to automatically select a temporary filename and turn off the device.  It is absolutely ridiculous that we can't have at least one of the R plot commands "just work" as opposed to needing this three-step thing (which apparently is universal in R).

Also, if I load the lattice library, I now get

```
sage: r.histogram('~ MPG.highway',data='Cars93')
Error in device.call(...) : X11 is not available
sage: r.bwplot('MPG.highway ~ Origin', data = 'Cars93')
Error in device.call(...) : X11 is not available
```

which is certainly a better error message than before.


---

Comment by kcrisman created at 2010-02-09 14:43:25

Yet another interesting issue for the Mac: in configuring, we get 

```
checking for X... no
configure: error: --with-x=yes (default) and X11 headers/libs are not available
Configuring R with fallback options
```

and indeed

```
$ if [ -f /usr/include/X11/Xwindows.h ]; then
>     XSUPPORT=yes
> else
>     XSUPPORT=no
> fi
$ echo $XSUPPORT
yes
```

but as [http://CRAN.R-project.org/bin/macosx/RMacOSX-FAQ.html#X11-window-server-_0028optional_0029](http://CRAN.R-project.org/bin/macosx/RMacOSX-FAQ.html#X11-window-server-_0028optional_0029) points out, that is not enough on Snow Leopard, and the other versions have their own issues.  If Aqua ends up working for plotting, we will probably want to completely disable X11 support, since it doesn't work the same on each version anyway.


---

Comment by kcrisman created at 2010-02-09 15:36:23

On Snow Leopard (OSX 10.6), re-enabling aqua allows the following:

```
sage: r.quartz(type='png')
NULL # But nice quartz viewer pops up!
sage: x = r([1,2,3])
sage: y = r([4,5,6])
sage: r.plot(x,y) # Nice plot of this pops up!
NULL
sage: r.dev_off() # Turns off the quartz viewer
null device 
          1 
```



---

Comment by kcrisman created at 2010-02-10 03:09:07

With the attached patch and [this spkg](http://sage.math.washington.edu/home/kcrisman/r-2.10.1.p0.spkg), _basic_ plotting should work on both OSX and Linux (if X11 is available).  This should be tested on OSX 10.4, 10.5, preferably also a 64-bit build on 10.5 and 10.6, and then on a few Linux variants and at least the most recent Solaris (to make sure I haven't broken something).  

The functioning of things like bwplot and histogram (which need the lattice package, which we now ship) is more iffy in the notebook, though it seems to work well enough (though apparently delayed by one, perhaps due to not calling dev.off()?) in the command line.  However, I think that dealing with this could legitimately be made a separate ticket; just getting r.plot to work across the board is pretty important.


---

Comment by kcrisman created at 2010-02-10 03:09:07

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-02-12 11:56:27

Changing to 'needs work' based on some discussion with an R developer that might solve the issue completely or provide more options for plotting (separate device, just popping up png as usual, etc.) and allow use of the other plot commands in the notebook.


---

Comment by kcrisman created at 2010-02-12 11:56:27

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-04-13 17:16:07

Since the R skpg has in the meantime moved to p0, the changes are even more minor.  [This](http://sage.math.washington.edu/home/kcrisman/r-2.10.1.p1.spkg) spkg is the updated one, and it applies fine and passes R and stats tests on my Macintel and sage.math.  Since the only change is to add aqua support on uname='Darwin', that is not a surprise.

The patch still should apply, but still needs some work to deal with all the cases we want.  We may also have to add some code to deal with the situation where neither X11 nor aqua is available, to at least gracefully exit with an intelligible error message.


---

Attachment

Removes the chdir in sagenb.notebook.worksheet_eval_cmd. Read comments for more info. Depends on #7997


---

Comment by kcrisman created at 2010-04-13 17:20:30

Umm... what comments?  It looks like this removes a reference to a directory - will this break anything else or cause a security problem?  Unfortunately I don't have an easy way to test this on the sagenb repo, since we still don't have hg_sagenb.

I'm also surprised I was able to make a change to the ticket after you had already made this change!


---

Comment by timdumol created at 2010-04-13 17:22:57

Depends on #7997. Before this patch, non-Sage systems are made to switch to the cell directory, which, aside from being a security vulnerability (I think?), doesn't seem to be possible with server pools. This removes the directory change, so that evaluation is done in the temporary directory.

If you want, I'll post a custom sagenb package with this patch, so you can try it out. (It will have a bunch of other (positively reviewed) patches in the queue, too, though.)


---

Comment by kcrisman created at 2010-04-13 17:32:49

Thanks, Tim, that would be fantastic to have the sagenb package to try this out.  I wish I had access to a GUI to test notebook behavior on sage.math... otherwise I don't have access to a Linux box.


---

Comment by timdumol created at 2010-04-13 17:37:14

The new spkg is here: http://sage.math.washington.edu/home/timdumol/sagenb-0.7.5.3-devel-7665.spkg

You could launch a temporary Sage notebook server, and try that out.


```

sage: notebook(interface="", secure=True, port=10000)

```



---

Comment by kcrisman created at 2010-04-13 18:17:51

The spkg is not downloading properly - Sage says it is empty, then corrupt.

For the other thing, so would I go to sage.math.../home/kcrisman:10000 or something?  Doing the command is taking a looong time due to generating a 2048 bit RSA private key, which I am not sure if it is supposed to do.  Thanks for entertaining my ignorance of how sagenb functions.


---

Comment by kcrisman created at 2010-04-13 18:44:37

Replying to [comment:14 kcrisman]:
> The spkg is not downloading properly - Sage says it is empty, then corrupt.
> 
I think the problem is that the name of the spkg is not the same as the name of the folder once it's unzipped.


---

Comment by kcrisman created at 2010-04-13 19:17:22

I was able to use it, but got a problem:


```
    cmd = self._eval_cmd(system, input)
	exceptions.TypeError: _eval_cmd() takes exactly 4 arguments (3 given)

```


So for instance Shift+Enter just creates a new line in the cell.  In fact, even clicking the 'evaluate' button doesn't work!  Also, for some reason I can no longer evaluate several commands by doing a semicolon between them.  Am I doing something wrong?  Or are these legacies of the other patches?


---

Comment by kcrisman created at 2010-04-13 19:37:19

So maybe 

```
-def _eval_cmd(self, system, cmd, dir): 
+def _eval_cmd(self, system, cmd): 
```

would suffice?  I'll try this out.


---

Comment by kcrisman created at 2010-04-13 20:03:37

Unfortunately, making the changes indicated in the patch along with this change in vanilla Sage-4.3.5 doesn't fix the problem either, though I can now use Shift+Enter again.  So somehow this isn't doing the job.


---

Comment by timdumol created at 2010-04-14 01:11:35

Makes systems change to the current tempdir instead. Depends on #7997.


---

Attachment

Adds a ``chdir`` function to the R interface.


---

Comment by timdumol created at 2010-04-14 01:14:18

Ah, sorrry. I managed to attach and package the incomplete version of the patch (which still didn't work properly). This should do the job. I'll be posting an updated spkg soon.


---

Comment by timdumol created at 2010-04-14 01:22:07

Alright, new spkg up at the same link: http://sage.math.washington.edu/home/timdumol/sagenb-0.7.5.3-devel-7665.spkg


---

Comment by kcrisman created at 2010-04-14 11:38:28

Thanks for all this.  Before I try it, can you just look at sage/interfaces/r.py and and functions png() and plot() - either the original or in the patch on this ticket?  At least one of them (before and after patch) has references to os.path.abspath, but perhaps that is what was causing the conflict with your original patch.  Because I haven't yet had time to try to understand the NB workings, I am not sure if that is part of the problem, but I had forgotten about that until this morning.  Maybe that path finding is no longer necessary.


---

Comment by timdumol created at 2010-04-14 12:29:14

I don't think that's the problem. The problem, as far as I can tell, is that the interpreter is reused between sessions, and so its working directory has to be changed each time to the temp folder used for evaluation.


---

Comment by kcrisman created at 2010-04-14 16:49:53

I'm a little confused about the trac_7633 patch... 

Anyway, very sadly it still doesn't work, and the behavior is still the same as before.  I also tried getting rid of the EMBEDDED_MODE things in interfaces/r.py and that didn't work either.  Any ideas?  The plots are being created, they are just living in those /tmp/ directories and not being accessed.


---

Comment by timdumol created at 2010-04-14 17:49:22

I posted the wrong patch. Let me get the right one.


---

Attachment

Adds a ``chdir`` function to the R interface.


---

Comment by timdumol created at 2010-04-14 17:55:27

This is the right one. trac_7665-sage-library-R-plotting.patch is to be applied to the main Sage library, trac_7655-sagenb-R-plotting.2.patch is to be applied to sagenb, or used via the spkg.


---

Comment by kcrisman created at 2010-04-14 18:53:03

It took me a while to figure out what this was about, but you need this so that syseval in server/support.py works correctly, right?  It works!  Wonderful, and thank you.

Okay, that doesn't mean I'm done with this ticket, but at any rate hopefully within the next day or two I will have resolved this to my satisfaction and then it can be reviewed.  

Incidentally, "know it's ID" should be "know its ID" :-)


---

Comment by timdumol created at 2010-04-15 00:07:28

Sorry :P Was a bit sleepy when I wrote the documentation.


---

Comment by timdumol created at 2010-04-18 07:37:03

Fixes a few doctests. Replaces trac_7655-sagenb-R-plotting.2.patch


---

Attachment

The substantive changes in the sagenb patch make it work on sage.math and my Macintel with OSX 10.6.  I don't know how to doctest sagenb stuff :(  And unfortunately the linked spkg is ... weird, to say the least.  It didn't unpack properly, for instance, and there was something inside I had to use instead - see [http://sage.math.washington.edu/home/kcrisman/sagenb-0.7.5.3.p0.spkg](http://sage.math.washington.edu/home/kcrisman/sagenb-0.7.5.3.p0.spkg) for something that does work, though of course the p0 and the 7.5.3 are not "official" by any means.

I will test this tonight on PPC OSX, and then post an omnibus patch to the Sage library.  Do you know of any way to test %r type commands?  That would be helpful, also for documenting how to use it.


---

Comment by kcrisman created at 2010-04-19 18:44:34

Replying to [comment:27 timdumol]:
> Sorry :P Was a bit sleepy when I wrote the documentation.

It wasn't your fault, it's already in there from someone else... anyway, before all this is done, line 2893 should be fixed with respect to that.


---

Comment by kcrisman created at 2010-04-20 01:10:15

Okay, here is something that should work and doesn't now - probably because of the new cell structure, though perhaps it already didn't work before, or maybe it's the fault of the r.png() setting its own path?  Try the following in the notebook (evaluated in Sage):

```
r.library('lattice')
r.png()
r("print(histogram(~wt | cyl, data=mtcars))")
r.dev_off()
```

Notice that below and to the right of the graphic there is a link for the graphic - but there is no actual graphic at that link, because it's a link to the /tmp directory (the actual evaluation directory), and the file doesn't actually exist there:

```
Crismans-Computer:~ crisman$ ls -al .sage/sage_notebook.sagenb/home/admin/0/cells/2/
total 40
drwx------   4 crisman  crisman    136 Apr 19 20:20 .
drwxr-xr-x   5 crisman  crisman    170 Apr 19 20:14 ..
lrwxr-xr-x   1 crisman  crisman     33 Apr 19 20:20 .Rplot001.png-wZKi -> /tmp/tmp_0wLLV/.Rplot001.png-wZKi
-rwx------   1 crisman  crisman  12769 Apr 19 20:20 Rplot001.png
Crismans-Computer:~ crisman$ ls -al /tmp/tmp_0wLLV/total 16
drwx------    4 crisman  wheel  136 Apr 19 20:20 .
drwxrwxrwt   23 root     wheel  782 Apr 19 20:20 ..
-rw-r--r--    1 crisman  wheel   76 Apr 19 20:20 _tmp__SAGE__CoDe__.py
lrwxr-xr-x    1 crisman  wheel   59 Apr 19 20:20 data -> /Users/crisman/.sage/sage_notebook.sagenb/home/admin/0/data
```

Any clue as to how to fix that?  I don't understand this at all.  I don't know that this should hold things up, though, particularly since one can either drag and drop the picture or just do it from the command line if one wants it.

Otherwise this is all coming together nicely, also works on PPC, so I think sufficiently robust at this point.  Here is some resolution of the original examples in command line.

```
sage: r.library('MASS')
sage: r.library('lattice')
sage: r.bwplot('MPG.highway ~ Origin', data = 'Cars93')
sage: r.dev_off() # Now it should be in the home directory name Rplot001.png or something
sage: r.histogram('~ MPG.highway',data='Cars93')
sage: r.dev_off() # Now it should be in the home directory name Rplot002.png or something
sage: r.plot('MPG.highway ~ Weight', data='Cars93') # Calls dev.off(), so should be in home directory immediately
```

Great!  Putting 'needs review', though presumably we'll have to do a few more things to tie up loose ends.


---

Comment by kcrisman created at 2010-04-20 01:29:58

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-04-20 01:29:58

I get test failures in sagenb/notebook/cell.py and sagenb/notebook/notebook.py which seem unrelated to this ticket on the spkg .p0 I post with above, as well as the sagenb/notebook/worksheet.py errors which are dealt with in timdumol's updated patch.  Having an "official" sagenb package to test would be really great.  Otherwise the following patch is the only one that has to be applied to the Sage library.


---

Attachment

Based on 4.3.5 - this is the only patch to apply to main Sage library


---

Comment by kcrisman created at 2010-04-20 01:41:43

Need to apply new R spkg [http://sage.math.washington.edu/home/kcrisman/r-2.10.1.p1.spkg](http://sage.math.washington.edu/home/kcrisman/r-2.10.1.p1.spkg) and some new version of sagenb package to test this, as well as the Sage library patch.


---

Comment by timdumol created at 2010-04-20 16:14:24

The SageNB package version suitable for testing this is at #8727.


---

Comment by was created at 2010-04-24 23:33:45

1. You need `::` I think in from of several `sage:` blocks in the sage library patch. E.g., 

```
 	976	        lattices package), it is advisable to either use an interactive plotting device 
 	977	        or to use the notebook.  The following examples are not tested, because they 
 	978	        differ depending on operating system. 
                    .... sage:
```


2. In the sagenb patch, there is a spelling error:

```
        # know it's ID. __SAGE_TMP_DIR__ is used in executing in non-Sage systems.
```

But that should be "its".  This is propagated by this patch, but not caused by it.  (This is probably originally my fault, from long ago.)

3.  Tests pass in the SAge library fine on both Linux and OS X (bravo!). 

So I think fixing a few typos, testing a little more in the notebook, and we're good to go.


---

Attachment

I rebased this against the new sagenb-0.8, and fixed the "it's" --> "its" issue.  and tested.


---

Comment by was created at 2010-04-24 23:46:37

Positive review, subject to anybody at all signing off on my referee patch (which is pure documentation) and sagenb rebase.


---

Comment by kcrisman created at 2010-04-25 00:04:15

This is fine - the r.py file was not in fact converted to ReST, so I was very reluctant to start doing so since I didn't have the time to convert the whole file properly to it.  The patch to the sagenb looks fine; assuming the package installs correctly on 4.3.5 and this patch applies and performs as it should, positive review.  I am adding John Verzani to the reviewer list since he provided invaluable help in testing early version of these ideas, esp. in the notebook with %r.


---

Comment by rbeezer created at 2010-04-25 00:13:41

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-04-25 00:13:41

Recent two patches both apply and build, library-part2 is just documentation changes.

I got an r.plot() out just fine, though an r.bwplot() didn't do anything.

So the recent changes by was look just fine, ie this is a sign-off on those, so as mentioned I'm changing this to positive review.


---

Comment by kcrisman created at 2010-04-25 00:16:46

You need to call r.dev_off() to get the r.bwplot() guy.  Great!


---

Comment by kcrisman created at 2010-04-25 00:29:23

To release manager: This depends on the sagenb 0.8 package, and requires the spkg [http://sage.math.washington.edu/home/kcrisman/r-2.10.1.p1.spkg](http://sage.math.washington.edu/home/kcrisman/r-2.10.1.p1.spkg), the Sage library patch trac_7665-r-plotting.patch, and the two reviewer patches from was (one for the Sage library, one for sagenb which will presumably have to be part of sagenb 0.8.1).  At least I think that's right.


---

Comment by was created at 2010-04-29 05:26:14

Merged into sagneb-0.8.p0 in sage-4.4.1.alpha2


---

Comment by was created at 2010-04-29 05:26:14

Resolution: fixed


---

Comment by bascorp created at 2010-04-30 14:38:17

[картинки про животных](http://rapidshare.in.ua/)


---

Comment by mvngu created at 2010-05-14 23:46:32

The updated R spkg

http://sage.math.washington.edu/home/kcrisman/r-2.10.1.p1.spkg

was not merged in Sage 4.4.1 at all. I merged that spkg in Sage 4.4.2.rc0.
