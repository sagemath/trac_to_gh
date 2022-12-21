# Issue 7204: issue building sage docs since notebook moved

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-14 02:19:49

Assignee: tba

CC:  jhpalmieri

{{{>> If nobody finds any serious problems with it, something close to it
>> will get released (though I'm not in a hurry).
>
> Here's a nonserious problem: running "sage -docbuild developer html --
> jsmath" prints an error message.  At the end of the build process, I
> get this error:
>
> copying static files... Exception occurred:
>  File "/Applications/sage_builds/sage-4.1.2.rc2-64-bit/local/lib/
> python2.6/site-packages/Sphinx-0.5.1-py2.6.egg/sphinx/builder.py",
> line 668, in finish
>    for filename in os.listdir(staticdirname):
> OSError: [Errno 2] No such file or directory: '/Applications/
> sage_builds/sage-4.1.2.rc2-64-bit/local/notebook/javascript/jsmath'
> The full traceback has been saved in /var/folders/JV/
> JVYCpshdHd4FFoThuUgD8k+++TI/-Tmp-/sphinx-err-X1Sd6B.log, if you want
> to report the issue to the author.
> Please also report this if it was a user error, so that a better error
> message can be provided next time.
> Send reports to sphinx-dev`@`googlegroups.com. Thanks!
> Build finished.  The built documents can be found in /Applications/
> sage_builds/sage-4.1.2.rc2-64-bit/devel/sage/doc/output/html/en/
> developer
>
> Did the directory "SAGE_ROOT/local/notebook" move some place else?

Yes, it did move -- it's now part of the sagenb spkg, and gets installed into python's site-package using Python's standard package data protocol. 

Is the build OK, but there is an error?  I.e., can this be safely fixed in the next SAge release.  Or do we have to fix it ASAP?



> (Replace "developer" by "tutorial" or "reference" or whatever and the
> same thing happens.  Omit "--jsmath" and it works just fine.  Building
> PDF documentation seems to work fine, too, although I haven't finished
> building the reference manual yet.)
}}}


---

Comment by mpatel created at 2009-10-14 11:34:24

Depends on #7196.


---

Attachment


---

Comment by mpatel created at 2009-10-14 11:34:55

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-15 19:35:58

Note that a version of this was already merged into 4.1.2, though not depending on the #7196.  This will probably necessitate a change in the patch.


---

Attachment

Depends on the released 4.1.2 and #7196.  Apply only this patch.


---

Comment by mpatel created at 2009-10-15 20:07:19

Thanks for pointing that out.  Version 2 applies on top of the patch with no name.


---

Comment by kcrisman created at 2009-10-15 20:12:22

It should also be pointed out that I plan to count this ticket as closed for 4.1.2, but that it should ALSO be counted as being close for 4.2.alpha0 in the official notes; it's silly to open a new ticket for this as long as attribution is somewhere.  I'm changing authorship to indicate this, since I just finished Minh's work on the release announcement for 4.1.2.


---

Comment by mpatel created at 2009-10-21 18:48:01

Patch v3 at #6673 subsumes v2 here.  If/when the former merges, please close this ticket.


---

Comment by mhansen created at 2009-10-31 15:30:36

Resolution: fixed
