# Issue 8027: change the wiki(...) command to store data in $HOME/.sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-21 16:58:19

Assignee: schilly

Replying to [comment:5 mpatel]:
> Replying to [comment:2 kcrisman]:
> > Also, why is it still in the sage_wiki folder and not in .sage/sage_wiki or something similar to what is now done with the notebook?
> 
> I'm not sure.  We do the same with `trac()` and the [optional] Trac spkg.  It makes sense to use a default directory under `DOT_SAGE`, but I think upgrading existing MoinMoin wikis can be problematic.


When I wrote the wiki and trac command, there was no .sage/* folder, and the SAge notebook was stored in sage_notebook in the current directory.   The notebook has moved over to be in .sage, but nobody moved the wiki and trac yet.   It would be reasonable to do so.  HOWEVER, note that this would break all my wiki's, since a typical situation is:


```
sage`@`sagemath:~/wiki/sage$ ls
nohup.err  nohup.out  sage_wiki  start
sage`@`sagemath:~/wiki/sage$ more start
ulimit -v 2000000; nohup echo "wiki(port=9001, address='')" | sage-new  > nohup.out 2>nohup.err &
sage`@`sagemath:~/wiki/sage$
```


If you change the wiki to be in $HOME/.sage by default, then suddenly all my wiki's will get started on top of each other (hence all but one will fail to start). 

So it might be worth checking if there is a wiki directory "sage_wiki" in the current directory, and only if there isn't then default to $HOME/.sage/moinmoin. 



---

Comment by schilly created at 2010-01-27 12:47:21

Changing assignee from schilly to tbd.


---

Comment by schilly created at 2010-01-27 12:47:21

Changing component from website/wiki to packages.


---

Comment by schilly created at 2010-01-27 12:47:21

the website/wiki component is for the actual sage website and wiki. i file this under packages because it is related to the moin-xyz.spkg.


---

Comment by jdemeyer created at 2013-01-22 08:45:57

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-01-22 08:45:57

MoinMoin is no longer part of Sage.


---

Comment by jdemeyer created at 2013-01-22 08:46:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-23 15:50:09

Resolution: invalid
