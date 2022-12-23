# Issue 9351: deps for sagetex with SAGE_CHECK='yes'

Issue created by migration from https://trac.sagemath.org/ticket/9351

Original creator: jhpalmieri

Original creation time: 2010-06-27 16:37:43

Assignee: AlexGhitza

CC:  ddrake drkirkby mpatel

The prerequisites (given in spkg/standard/deps)  for building the sagetex package are just python, but if you build Sage with SAGE_CHECK="yes", then it tries to run the test suite for sagetex, which requires that all of Sage be installed.  This will fail unless you get lucky and sagetex is installed after Sage. With the new parallel spkg building (#8306), I frequently see sagetex built before Sage.

To fix this, let's make gap a prerequisite for sagetex.  Since sage is a prerequisite for gap, this should work.  (I don't know if anything in the sagetex test suite uses gap, but it might.)



---

Comment by drkirkby created at 2010-06-27 16:45:47

Changing component from algebra to spkg-check.


---

Comment by drkirkby created at 2010-06-27 16:45:47

Changing assignee from AlexGhitza to tbd.


---

Comment by drkirkby created at 2010-06-27 17:14:04

I understand how this is a problem - I'm a bit puzzled at the solution though:) 

Is there any reason not to make sage a prerequisite for sagetex directly, rather than via gap? I realise in practice it achieve the same thing, but it is far more confusing for someone to understand if they read deps. 

Would this not work, but be more informative and less confusing? 

```
# Sagetex does not require Sage in order that it may be built, but it does require 
# Sage in order that it may be tested using SAGE_CHECK=yes.
$(INST)/$(SAGETEX): $(INST)/$(PYTHON) $(INST)/$(SAGE)
241	        $(INSTALL) "$(SAGE_SPKG) $(SAGETEX) 2>&1" "tee -a $(SAGE_LOGS)/$(SAGETEX).log"
```


We might in fact find other dependencies that we don't know about. Building packages in parallel will force deps to be more accurate. There may be other packages which can only be tested after something else is built. So as we had spkg-check files, there might be other similar issues arise. 

Dave


---

Comment by jhpalmieri created at 2010-06-27 18:02:42

Well, I don't know if spkg-check in sagetex uses anything from gap: various calls in Sage end up calling gap in the background.  We could add sage as a dependency, but unless ddrake says otherwise, I'd like to keep gap there as well.


---

Comment by jhpalmieri created at 2010-06-27 18:02:42

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-03 16:12:52

Replying to [comment:3 jhpalmieri]:
> Well, I don't know if spkg-check in sagetex uses anything from gap: various calls in Sage end up calling gap in the background.  We could add sage as a dependency, but unless ddrake says otherwise, I'd like to keep gap there as well.

I've got no doubt this will work what you are proposing. But given you say the problem is sagetex calls Sage for testing, I can't understand the logic of listing gap as a dependency. Why gap? 

There is no reference to gap anywhere in the Sagetex source files


```
drkirkby@hawk:~/SAGE-4.5.alpha1/spkg/standard/sagetex-2.2.5$ ggrep -Ri gap *
drkirkby@hawk:~/SAGE-4.5.alpha1/spkg/standard/sagetex-2.2.5$ 
```


Without an explanation in the 'deps' file, one could easily envisage someone coming along one day and saying "Sagetex is a typesetting program, and does not need gap, so lets remove gap as a dependency". That would break, as the real dependency is Sage, but that fact is obscured. I would have thought it much safer to explicitly list Sage as a dependency, and adding a comment like I put above would ensure nobody updating deps would be under any illusion why Sage is a dependency. 

BTW, in SPKG.txt, it says:


```
## Dependencies

To install, nothing more than a standard Sage install. The
`spkg-check` script will exit without actually testing anything if
it cannot find "latex" in your path, or if it cannot find tkz-berge.sty,
a TikZ add-on required for typesetting some graphs.
```



again, no mention of gap. So I can't see the logic of explicitly listing gap - it just appears to add confusion, though I would agree that technically it does achieve the requirement, but via an obscure way. 

Dave


---

Attachment

the file SAGE_ROOT/spkg/standard/deps


---

Comment by jhpalmieri created at 2010-07-03 17:39:56

diff between original deps and new one


---

Attachment

I'll say again:  various calls in Sage end up calling gap in the background -- not explicitly, but in the background.  I haven't looked at the tests in sagetex to know if they use any group theory, for example, but if they do, they could very well try to use gap.  I think other components of Sage use gap as well.

```
## Dependencies

To install, nothing more than a standard Sage install.
```

And a standard Sage install includes gap.  That is, there are plenty of doctests in Sage which would fail if gap were not installed.  I don't know what would happen for the tests in sagetex if gap were not installed.

We could list both Sage and gap as dependencies for sagetex, and also put in a comment about it if you think that's necessary.  What I would really like to guarantee is that all of the other Sage spkgs have been installed before sagetex is, in order to guarantee a "standard Sage install", but I don't know how to do that.

I'm attaching new versions.


---

Comment by drkirkby created at 2010-07-03 19:13:00

Hi John, 

I think that is pretty clear now. This looks good, so positive review. 

#9274 also updates 'deps' but is marked as 'needing work'. 

Dave


---

Comment by drkirkby created at 2010-07-03 19:13:00

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-05 18:16:21

It looks like I missed most of the, uh, fun here, but here's an explanation of why SageTeX's spkg-check may or may not work: all that script does is run LaTeX on the example.tex file included  in the spkg, and then run Sage (with a regular "sage example.sage"). So the exact components that are required depend on what commands we have in example.tex. I would strongly prefer to not need to limit myself in that file, since it is also intended as an example file for SageTeX users, and as John has said, it is hard to avoid commands that completely avoid Gap. (Or other Sage components.)

Because I would like the example.tex file to be very complete, and serve as a nice collection of examples for users, my preference would be to add any and all dependencies that we find are necessary to get the spkg-check to complete successfully. This may ultimately push SageTeX to very near the end of the installation, but since it takes only a couple seconds to install, I doubt that will be a problem.


---

Comment by rlm created at 2010-07-05 22:34:54

Resolution: fixed


---

Comment by rlm created at 2010-07-05 22:34:54

The changes here were merged as part of #9312.

David -- You must stop including changes from one ticket in others. It's in bad form.


---

Comment by jhpalmieri created at 2010-07-05 22:50:54

You know, we really should have spkg/standard/deps and spkg/install under version control...


---

Comment by rlm created at 2010-07-05 22:54:11

I was thinking that while working on this release. It makes me wonder whether they should actually go in `$SAGE_LOCAL/bin`. Even though they don't really quite belong there, that would eliminate the need for another repo. Is it possible to have just these two files under revision control from somewhere else?


---

Comment by drkirkby created at 2010-07-05 23:39:00

Replying to [comment:9 jhpalmieri]:
> You know, we really should have spkg/standard/deps and spkg/install under version control...

Yes, it would make a lot more sense.


---

Comment by drkirkby created at 2010-07-05 23:49:18

Replying to [comment:10 rlm]:
> I was thinking that while working on this release. It makes me wonder whether they should actually go in `$SAGE_LOCAL/bin`. Even though they don't really quite belong there, that would eliminate the need for another repo. Is it possible to have just these two files under revision control from somewhere else?

IMHO it would be good if $SAGE_ROOT under revision control, so things like the 'makefile', README.txt were too. Then $SAGE_ROOT/spkg/install and $SAGE_ROOT/spkg/standard/deps could be part of that repository.

I don't see $SAGE_ROOT/spkg/install would be too out of place in $SAGE_ROOT/local/bin, as it is an executable shell script. $SAGE_ROOT/spkg/standard/deps would seem more out of place I would admit, which is why perhaps another repository would not be a bad idea. I think there are more than just these two files that would be better put under revision control. 

Dave 

Dave


---

Comment by jhpalmieri created at 2010-07-05 23:56:14

The sage_scripts spkg actually includes install, but the file is not under version control.  Could we have them in local/bin but in the spkg-install file, (soft) link them to their current locations, where they actually make sense?  (The current spkg-install file for sage_scripts moves "install" to its current location, which wouldn't be a bad option if there were a file local/bin/install which were under version control.)

I also agree about the text files in SAGE_ROOT being under revision control.


---

Comment by jhpalmieri created at 2010-07-06 00:04:07

See #9433.
