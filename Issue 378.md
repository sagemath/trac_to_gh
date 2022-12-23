# Issue 378: user-specified sage load path

Issue created by migration from https://trac.sagemath.org/ticket/378

Original creator: was

Original creation time: 2007-05-25 16:28:34

Assignee: was

CC:  rossk


```
Utpal Sarkar <doetoe@gmail.com> 	
to sage-support
	
show details
	 9:17 am (7 minutes ago) 

I thought it could work something like this:
As a command line option it could be like an include path or a library
path to gcc, i.e. every option "-I path" (or any other name of the
switch, this is the one for includes in gcc) is added to the existing
default list of paths. This could be useful e.g. when calling sage
from a launcher, in which case you could put these options in the
launcher so that it will always be called with these paths when ran
from the launcher.
As an environment variable it could work just like LD_LIBRARY_PATH,
PYTHONPATH or MAGMA_PATH: a list of paths separated by colons (or some
other separator) whose constituents are also added to the existing
list of paths. For reasons of implementation, maybe it is easier to
just use PYTHONPATH for sage files as well.
If this list would be directly accessible from sage, as in python
where it is stored in sys.path (which is read/write), and moreover
there were the possibility to specify a startup script which would be
executed just before entering the session (like in magma when called
with -s, or in bash and many other linux programs where it is a
standard file .bashrc), then you could also append your paths to the
standard list in the startup script.
When calling "load" or "attach" from sage with a non-absolute path, it
would cycle through this list, concatenating the paths with the string
passed to load or attach, until it finds the file.
If you consider this useful, and you could implement any of these in
sage, that would be great!

Thanks,

Utpal


```



---

Comment by mpatel created at 2010-01-20 11:20:05

#1484 is related.


---

Comment by mpatel created at 2010-01-22 04:08:42

So is #516.


---

Comment by mpatel created at 2010-01-22 04:09:24

That should be #5169.


---

Comment by mpatel created at 2010-02-16 00:14:05

First take on load / attach path.  sage repo.


---

Comment by mpatel created at 2010-02-16 00:22:23

Changing status from new to needs_review.


---

Attachment

Feel free to improve the patch!


---

Comment by mpatel created at 2010-02-16 00:22:23

Changing priority from minor to major.


---

Comment by mpatel created at 2010-02-18 02:33:12

We should skip the search, if the given filename is an absolute path.


---

Comment by mpatel created at 2010-02-18 02:33:12

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-02-18 03:08:19

Should we add an option (`recurse=False`?) that makes `load` and `attach` search the entire directory tree under each search path?


---

Attachment

More examples.  Handle absolute paths.  Replaces previous.


---

Comment by mpatel created at 2010-02-20 23:54:06

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-20 23:54:06

With V2, we skip the search if given an absolute path.  I've also added some examples.


---

Comment by timdumol created at 2010-04-17 18:36:47

Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?


---

Comment by AlexGhitza created at 2010-06-05 00:02:15

Changing status from needs_review to needs_info.


---

Comment by mpatel created at 2010-06-23 01:23:50

Replying to [comment:10 timdumol]:
> Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?

Both ideas sound great.  I can't make the changes immediately, but I'll try to attach a new patch soon.


---

Comment by mpatel created at 2010-06-23 01:23:50

Changing status from needs_info to needs_work.


---

Comment by rossk created at 2010-07-10 04:41:57

Available as another reviewer if you need one.


---

Comment by jsrn created at 2010-10-21 09:21:01

Is this still alive? I found myself in need of this functionality today and was surprised it is not there; how does anyone use the notebook locally without it?

Anyway, I'd like to help out fixing or reviewing if necessary.
I've only glanced at the current patch but found this anomaly: Shouldn't line 1399 be changed to 

```
while '' in _load_attach_path:
```

so as to remove any number of empty entries (e.g. if user wrote SAGE_LOAD_ATTACH_PATH = ":::::foo::")

Cheers, Johan


---

Comment by mpatel created at 2010-10-21 09:25:54

Thanks for the interest!  Unfortunately, I've been busy with other tasks (Sage and non-Sage) and haven't had the time to rework the patch to incorporate Tim's suggestions.  Is anyone willing to do that?


---

Comment by flawrence created at 2010-11-04 05:11:17

Replying to [comment:10 timdumol]:
> Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?

I've had a bit of a hack at exposing the array itself, but there are problems making it sufficiently global.  `sys.path` works for the stdlib because `path` is a variable in the `sys` module.  The logical thing to do here is to create a `load_attach_path` variable in the preparser module, but following the stdlib analogy this would require the user to edit `sage.misc.preparser.load_attach_path`, which is not very user friendly.

Failing this, it looks like the best you can do is a `from sage.misc.preparser import load_attach_path`, but this is a fragile state of affairs: if you reassign `load_attach_path` anywhere, either from sage's command line or by calling some function like `sage.misc.preparser.reset_load_attach_path()`, you end up with a situation where `load_attach_path` and `sage.misc.preparser.load_attach_path` are different objects.

This requires caution on the part of the user and the programmer.  For example, `reset_load_attach_path()` can't include

```
load_attach_path = ['.']
```


instead it has to do

```
while load_attach_path != []:
    load_attach_path.pop()
load_attach_path.append('.')
```


If the user accidentally reassigns `load_attach_path` in the command line, they'll have to re-run `from sage.misc.preparser import load_attach_path`.  I don't think that this step can be included in a `reset_load_attach_path()` function due to the different scopes.

So it's possible to expose the `load_attach_path` array to the user, and I've written most of a patch that does this, but there's lots of things that could go wrong so I'd suggest sticking to the existing patch's approach of hiding behind a function.  If others think that the pros outweigh the cons then I'll tidy up the patch and upload it.

Thoughts?


---

Attachment

use os.path.userexpand on load, separate reset function, also use paths for detach. replaces previous.


---

Comment by flawrence created at 2010-11-04 06:21:47

Changing status from needs_work to needs_review.


---

Comment by flawrence created at 2010-11-04 06:21:47

Assuming that no-one comes up with a robust and convenient way to expose the array, I've uploaded a patch that addresses Tim's other idea, Johan's comment, and two other main changes:

* You can now use paths with `detach`

* `reset_load_attach_path` is now a function on its own, which gets called upon startup.  Note that it now resets the path to '.' plus the contents of the path environment variable `SAGE_LOAD_ATTACH_PATH`, rather than to '.' alone.


---

Comment by rossk created at 2010-11-05 02:09:42

Reviewing this on 4.6.1.alpha1 - should I be using 4.6?


```
/scratch/rossk/sage-4.6.1/devel/sage$ hg qpush
applying trac_378-load_attach_path.2.1.patch
patching file sage/misc/all.py
Hunk #1 FAILED at 57
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/all.py.rej
patching file sage/misc/preparser.py
Hunk #1 FAILED at 1390
Hunk #2 FAILED at 1488
Hunk #3 FAILED at 1497
Hunk #4 FAILED at 1533
Hunk #5 FAILED at 1568
Hunk #6 FAILED at 1582
Hunk #7 FAILED at 1593
Hunk #8 FAILED at 1608
Hunk #9 FAILED at 1618
Hunk #10 FAILED at 1771
10 out of 10 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_378-load_attach_path.2.1.patch
```



---

Attachment

use os.path.userexpand on load, separate reset function, also use paths for detach. actually replaces previous this time..


---

Comment by flawrence created at 2010-11-05 02:48:52

Sorry, I'm new to mercurial queues and stuffed up the patch (it did rely on the other patch after all).  The new patch I just uploaded should work on 4.6 without mpatel's patch, and hopefully 4.6.alpha1 too.


---

Comment by rossk created at 2010-11-05 08:08:02

Replying to [comment:19 flawrence]:
> Sorry, I'm new to mercurial queues and stuffed up the patch (it did rely on the other patch after all).  The new patch I just uploaded should work on 4.6 without mpatel's patch, and hopefully 4.6.alpha1 too.

Im new to mercurial queues too (and much more :-). Thought youd like to know your new patch was error free. (Ill test over the weekend and report back when I can - sorry it cant be sooner).


---

Comment by jsrn created at 2010-11-05 08:54:58

Replying to [comment:16 flawrence]:
> Replying to [comment:10 timdumol]:
> > Things work perfectly, but I think it might be better to follow the Python stdlib in exposing the array itself, instead of covering it in a function (`sys.path` instead of `sys.path()`, so similarly, `load_attach_path` instead of `load_attach_path()`). Also, it might be handy to `os.path.expand_user` any paths handed to the function, so you could have load_attach_path.append("~/foo"). What do you think?
> 
> I've had a bit of a hack at exposing the array itself, but there are problems making it sufficiently global.  `sys.path` works for the stdlib because `path` is a variable in the `sys` module.  The logical thing to do here is to create a `load_attach_path` variable in the preparser module, but following the stdlib analogy this would require the user to edit `sage.misc.preparser.load_attach_path`, which is not very user friendly.
> 
> Failing this, it looks like the best you can do is a `from sage.misc.preparser import load_attach_path`, but this is a fragile state of affairs: if you reassign `load_attach_path` anywhere, either from sage's command line or by calling some function like `sage.misc.preparser.reset_load_attach_path()`, you end up with a situation where `load_attach_path` and `sage.misc.preparser.load_attach_path` are different objects.
> 
> This requires caution on the part of the user and the programmer.  For example, `reset_load_attach_path()` can't include
> {{{
> load_attach_path = ['.']
> }}}
> 
> instead it has to do
> {{{
> while load_attach_path != []:
>     load_attach_path.pop()
> load_attach_path.append('.')
> }}}
> 
> If the user accidentally reassigns `load_attach_path` in the command line, they'll have to re-run `from sage.misc.preparser import load_attach_path`.  I don't think that this step can be included in a `reset_load_attach_path()` function due to the different scopes.
> 
> So it's possible to expose the `load_attach_path` array to the user, and I've written most of a patch that does this, but there's lots of things that could go wrong so I'd suggest sticking to the existing patch's approach of hiding behind a function.  If others think that the pros outweigh the cons then I'll tidy up the patch and upload it.
> 
> Thoughts?
 
Very astute! I was almost finished with my own patch, falling into all the same holes as you describe :-) Your concern at least begs the question on whether this is what we want to do, as it might fool some users. However, a possible usage pattern - in case load_attach_path is fully exposed - is the following


```
   import sage.misc.preparser as pre
   pre.load_attach_path = [ ... ]
```


Still, this is not very nice, and doesn't really fit into the "import sage.all" scheme. A third possibility is to "decide" that we might very well need such global variables in other places, stemming from various other foundational modules, and therefore introduce a new module sage.misc.globals to hold these. When Sage launches, it imports this module as "globals", and so, for any global variable - say load_attach_path -, the user would access it and modify it as globals.load_attach_path. I don't think that would be unnatural at all. However, it might be overkill if load_attach_path is the _only_ such conceivable global value, but for some reason (perhaps the sheer size of Sage), I can't really think it is.

If none of these sound compelling, then I vote yes on the current form (I haven't tested the patch, that is). My only comment on the current patch, is that maybe there should be a TODO (or a fix ;-) ) in reset_load_attach_path(), which notes that probably the elements of SAGE_LOAD_ATTACH_PATH should be uniquified while preserving the order (thus, list(set(_load_attach_path)) is no good). After that the while could be reverted to an if again when removing the empty element.

Otherwise good work. I'm looking forward to this patch in Sage, whatever the format :-)
Cheers, Johan


---

Comment by mpatel created at 2010-11-05 10:57:13

Thanks to everyone for working on this ticket!

One question that may relate to how/whether we "expose" the path list:  Would users want Sage to search some paths recursively for files to load or attach?  How would we store this information?  Perhaps as

```python
['/some/path', ('/a/path/to/search/recursively', True), '/another/path']
```

?  Of course, this needn't hold up this ticket.


---

Comment by flawrence created at 2010-11-05 14:29:28

Replying to [comment:21 jsrn]:

>  My only comment on the current patch, is that maybe there should be a TODO (or a fix ;-) ) in reset_load_attach_path(), which notes that probably the elements of SAGE_LOAD_ATTACH_PATH should be uniquified while preserving the order (thus, list(set(_load_attach_path)) is no good). After that the while could be reverted to an if again when removing the empty element.

Do we really need to test for uniqueness at all? It's the user's fault if they get it wrong, and the only negative consequence I see is that attaching/loading files (not the sort of operation that sits deep in a loop) a tiny tiny bit slower.  Python doesn't check for uniqueness in sys.path, BASH doesn't check for uniqueness in $PATH.  AFAIK the main argument for uniqueness is aesthetics; perhaps we can leave this to the user rather than try to tidy up after them (and perhaps do something unexpected in the process)?

Replying to [comment:22 mpatel]:
>One question that may relate to how/whether we "expose" the path list: Would users want Sage to search some paths recursively for files to load or attach? How would we store this information?

This is an interesting question.  I think it would be a nice feature.  Since we don't actually expose the path array, it would be easy to add such features later, so it's probably best as a new ticket.


I also noticed that I was fat-fingered typing the name of the new patch - 387 instead of 378.  *sigh*


---

Comment by rossk created at 2010-11-06 03:42:32

Quick question: attached_files() works without an import but load_attach_path() is unknown (raises a "NameError" exception when called). Are we supposed to import it in order to use it?


---

Comment by flawrence created at 2010-11-06 04:11:14

You shouldn't have to import `load_attach_path()` manually.  Applying the patch and rebuilding on 4.6 worked for me.  Maybe you forgot to rebuild sage after applying the most recent patch?


---

Comment by rossk created at 2010-11-06 05:56:32

Replying to [comment:25 flawrence]:
> You shouldn't have to import `load_attach_path()` manually.  Applying the patch and rebuilding on 4.6 worked for me.  Maybe you forgot to rebuild sage after applying the most recent patch?

Doh! Certainly did forget and rebuilding worked - thanks!


---

Comment by rossk created at 2010-11-06 06:19:45

I exercised this reasonably well and the functionality is great. After it passed all the tests I could think of, I renamed the folder that had the attached file (to see what would happen). The error was not unexpected: "OSError: [Errno 2] No such file or directory: ...". But this error persisted no matter what was done afterwards (even just "1+1"!). I had to get out of Sage to start again. Thats the most pressing issue I could find but otherwise looks good! Theres also a couple of ideas I can run by you if you want, now that Ive exercised all the use cases I could think of.


---

Comment by flawrence created at 2010-11-06 13:53:43

Replying to [comment:27 rossk]:
>I renamed the folder that had the attached file (to see what would happen). The error was not unexpected: "OSError: [Errno 2] No such file or directory: ...". But this error persisted no matter what was done afterwards (even just "1+1"!). I had to get out of Sage to start again.

I've checked and this happens even without this patch applied, so it's a separate issue I think.  Not much error checking is done for attached files!  I've started ticket #10229 for this.


---

Comment by rossk created at 2010-11-06 20:12:29

Because the functionality is important, it works as designed, and passed all tests (the path can be set, displayed and modified as intended), this ticket can get a positive review now. If nobody objects, Ill do that after a short wait for any feedback on the next comment.


---

Comment by rossk created at 2010-11-06 20:14:52

It may be too late for the following suggestions but Ill put them forward in case you think they have enough merit to refactor the code now (otherwise ignore them or they can go in another ticket). They are based on the idea that the main things we want to do with a path is: (1) start Sage with a sensible default (2) display what the current path is (3) set the path (4) add a folder to the end/beginning of the path (5) reset the path (6) totally clear the path. (I acknowledge some ideas have come from other packages e.g. matlab). So here's is how the path may be made to work in the future. Please let me know what you think. These are just ideas and doesnt change the good work youve already done - thanks for that!  


```
# display the default attach-path (unless a SAGE_ATTACH_PATH environment variable is set, then the attach-path when Sage starts is the path in SAGE_ATTACH_PATH)
sage: attach_path()
['.']

# set the attach path to a list of folders: ['./folder1','./folder2']
# (Note: if you want the current directory '.' included, you must specify it)
sage: attach_path(['folder1','folder2'])

# append to the (end of) attach path
sage: attach_path_join(attach_path(), ['folder3'])

# display the attach path 
sage: attach_path()
['folder1','folder2','folder3']

# add to the start of the attach path
sage: attach_path_join(['folder0'], attach_path())

# display the attach path again
sage: attach_path()
['folder0','folder1','folder2','folder3']

# append to the (end of) attach path *recursively*
sage: attach_path_join_subfolders(attach_path(), ['folder4'])

# display the attach path 
sage: attach_path()
['folder0','folder1','folder2','folder3','folder4','folder4/dir1','folder4/dir2']

# reset the attach path - sets the attach path to the default 
sage: reset_attach_path()

# clear the attach path - sets it to '' i.e. neither '.' nor SAGE_ATTACH_PATH  are included (when you want to ensure no implicit attaching is done or to rebuild the path from scratch)
sage: clear_attach_path()

# display the attach path 
sage: attach_path()
[]
```



---

Comment by rossk created at 2010-11-07 10:22:16

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-11-07 10:22:16

Time to give this the positive review it deserves. Looking forward to using attach paths!


---

Comment by jdemeyer created at 2010-11-10 22:19:14

Resolution: fixed
