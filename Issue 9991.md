# Issue 9991: Python scripts try to run before Python is built.

Issue created by migration from https://trac.sagemath.org/ticket/9992

Original creator: drkirkby

Original creation time: 2010-09-23 23:24:10

Assignee: GeorgSWeber

CC:  jhpalmieri

As discussed [here](http://groups.google.com/group/sage-devel/browse_thread/thread/9788a6ad6fe03ab9), the Python script `$SAGE_ROOT/spkg/base/sage-make_relative` is run before Python is built in Sage. On a system that do not have Python installed (like a fresh install of IBM's AIX operating system),  this generates an error message message as this script is run. 


```
Making Sage/Python scripts relocatable...
python: No such file or directory 
```


This could be quite worrying, to find that an important program like Python is missing.

The bottom of the file `$SAGE_ROOT/spkg/base/sage-spkg` has this:


```
echo "Making Sage/Python scripts relocatable..."

cd "$SAGE_LOCAL"/bin
./sage-make_relative

echo "Finished installing $PKG_NAME.spkg" 

# It's OK if the above fails -- in fact it will until Python
# itself gets installed. That's fine. 
exit 0   
```


which indicates a failure of {{{sage-make_relative
}}} is unimportant. But still it is annoying and led me to believe there was a more serious bug. 

It does not seem appropriate to let {{{sage-make_relative
}}} fail, but it would be much better if {{{sage-make_relative
}}} can be removed, and its functionality moved to the script that calls it, which is `$SAGE_ROOT/spkg/base/sage-spkg`

I've attached a copy of `$SAGE_ROOT/spkg/base/sage-make_relative`, which I believe could be written much better. I'm attaching it, since I will want to create an external link to this file. 

Dave


---

Attachment

Attached only so I can provide a link to this - for most practical purposes this can be ignored.


---

Comment by leif created at 2010-09-24 02:31:52

Well, perhaps one should simply suppress (or avoid) the error message in case no Python is (yet) installed, but the script is really odd.

 * It should only test (and modify) scripts that are executable.
 * It "rewrites" *every* file that contains `python` and `#!` in its first line, so even already correct (and already modified) files starting with
   {{{#!/usr/bin/env python
}}}
   will get rewritten.
 * It makes all these files writable (but only for the owner).

I don't agree moving its functionality into `sage-spkg` is a good idea. (IIRC it is called by other scripts as well, and `sage-spkg` shouldn't be blown up too much.)


---

Comment by drkirkby created at 2010-09-24 04:06:15

Replying to [comment:1 leif]:
> Well, perhaps one should simply suppress (or avoid) the error message in case no Python is (yet) installed, but the script is really odd.

Or just not check if python is not run. 

>  * It should only test (and modify) scripts that are executable.

Yes. At the minute it tests binaries too. 

>  * It "rewrites" *every* file that contains `python` and `#!` in its first line, so even already correct (and already modified) files starting with
>    {{{
> #!/usr/bin/env python
> }}}
>    will get rewritten.

That's not such a big deal. 

>  * It makes all these files writable (but only for the owner).


 
> I don't agree moving its functionality into `sage-spkg` is a good idea. (IIRC it is called by other scripts as well, and `sage-spkg` shouldn't be blown up too much.)

OK, well this is easy to fix by putting an 

if [ -f '$SAGE_LOCAL/bin/python" ] ; then
   # Run the python script. 
fi

I'll leave you to modify the python script if you want to.


---

Comment by leif created at 2010-09-24 11:31:38

Replying to [comment:3 drkirkby]:
> Replying to [comment:1 leif]:
> >  * It "rewrites" *every* file that contains `python` and `#!` in its first line [...]
> That's not such a big deal.

I think it should skip files matching `sage-*` and those whose first line already starts with `#!/usr/bin/env ...`.

> > I don't agree moving its functionality into `sage-spkg` is a good idea. (IIRC it is called by other scripts as well, and `sage-spkg` shouldn't be blown up too much.)
> 
> OK, well this is easy to fix by putting an 

```sh
if [ -f '$SAGE_LOCAL/bin/python" ] ; then
    # Run the python script. 
fi
```


That's an improvement, though it is not clear if we in the near future make Python a prerequisite (or intentionally use a system Python for such if one is present).

> I'll leave you to modify the python script if you want to. 

I thought you were going to rewrite it as a shell script (which could as well be called from `sage-spkg`).


---

Comment by drkirkby created at 2010-09-24 12:52:39

Replying to [comment:4 leif]:
> Replying to [comment:3 drkirkby]:

> > OK, well this is easy to fix by putting an 
> {{{
> #!sh
> if [ -f '$SAGE_LOCAL/bin/python" ] ; then
>     # Run the python script. 
> fi
> }}}
> 
> That's an improvement, though it is not clear if we in the near future make Python a prerequisite (or intentionally use a system Python for such if one is present).

I hope we don't. 
 * We rely on someone's Python working right. It was a failure of Python on William's machine which cased a headache recently with `sage_fortran`. Though he had Python, his version was not working in a way necessary to perform the task it was asked to do. That's why he was the only one to see the bug - not everyone else. 

 * It would be even harder to justify shipping a large tarfile to maintainers of Debian or similar when we say Python is a prequiste, but also we include the Python source. I think that gets a bit silly. 

 * On platforms like AIX, or the smaller cut-down Linux distributions, they may well not include Python. Some have tried building Sage on a mobile phone. I doubt that is as practical if we make Python a prerequisite and still ship the source code. 

> > I'll leave you to modify the python script if you want to. 
> 
> I thought you were going to rewrite it as a shell script (which could as well be called from `sage-spkg`).

No, I think it will be easier to leave it untouched, but only call it if `$SAGE_ROOT/local/bin/python` exists. The script appears to work and if it is called from multiple places, I'd have to duplicate its functionality accurately - even though I think they are a bit dumb. 

Dave


---

Attachment

SCRIPTS repo. Changes `sage-spkg` to only run `sage-make_relative` if Sage's Python is already installed. Based on Sage 4.7.2.alpha4.


---

Comment by leif created at 2011-10-13 12:19:49

Changing status from new to needs_review.


---

Comment by leif created at 2011-10-13 12:19:49

Attached patch only runs `sage-make_relative` if *Sage's* Python is installed (which Dave wanted).

If we want to allow other `python`s as well, we'd have to change it to e.g.

```sh
if command -v python >/dev/null; then
    ...
```


I've left the `exit 0` at the end (which is in principle superfluous since `echo` is unlikely to fail), as it clarifies that this part is (hopefully ;-) ) only reached if no errors occurred previously.


---

Comment by leif created at 2011-10-13 12:19:49

Changing keywords from "" to "sage-make_relative sage-spkg".


---

Comment by jhpalmieri created at 2011-10-14 20:26:20

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2011-10-14 20:26:20

The code makes sense and it works: I applied that patch and made a new source distribution.  When building that from scratch, the first 50 or so spkgs didn't run sage-make_relative.  Once the python spkg was installed, they did run it.

I also tried after temporarily getting rid of my system's python.  Installing before the patch yields a possibly confusing error message (before the python spkg is installed, anyway), and after the patch there is no such error message.


---

Comment by jdemeyer created at 2011-10-19 18:52:35

Resolution: fixed


---

Comment by jdemeyer created at 2011-11-03 16:14:43

Milestone sage-4.7.3 deleted
