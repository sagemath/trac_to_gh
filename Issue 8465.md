# Issue 8465: move the document "Python Functional Programming for Mathematicians" to the classification "Sage HOWTOs"

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-03-07 02:03:10

Assignee: mvngu

CC:  leif mpatel

Keywords: Sage HOWTOs

The new document classification "Sage HOWTOs" aims to include various in-depth documentation/tutorials on specific topics. Here, we move the chapter [Python Functional Programming for Mathematicians](http://www.sagemath.org/doc/constructions/functional_programming.html) to the "Sage HOWTOs" classification. The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).


---

Comment by mvngu created at 2010-03-10 02:29:44

Changing status from new to needs_review.


---

Attachment

based on Sage 4.3.4.alpha1


---

Comment by schilly created at 2010-03-21 20:30:54

i hope that's the correct place to point out some ideas i have:
(at least, i found them
very useful to know when i coded something recently)

1. reduce will be part of the functools module in python 3. might be
helpful to import it from there to make it forward compatible
http://docs.python.org/library/functools.html <- or at least you might
wanna add a link to that module in the bottom section.

2. http://docs.python.org/library/itertools.html#itertools.starmap is
quite cool if you have "izip"ed values for the function arguments.
i.e.
starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000. it's like f(a,b) vs. f(*c)

3. Besides that, have you explained the generator concept with the
"yield" keyword? I'm not sure if that counts as functional programming
but it is a nice topic in that context.


---

Comment by mjordan7 created at 2010-05-04 06:10:56

Tested well, and looks good on Boxen. In the styles of programming section, the object-oriented example seemed a little contrived, and I would say was bad style to make an object for adding two things. I believe a better example would to use comparison instead of adding. Something procedural

def compare(a, b)
   return a - b;

versus like this for object-oriented

def class Comparable
   def compare(b)
     return self - b;

~Mark


---

Comment by malb created at 2010-07-21 14:32:59

Minh, I'm setting this to needs work in light of the comments by Mark. If you don't feel this is justified could you briefly explain why here and then change it back to needs review?


---

Comment by malb created at 2010-07-21 14:32:59

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-07-27 20:20:44

Two other comments: I don't think we need the file `doc/en/thematic_tutorials/Makefile`.  Also, the file `index.rst` should include a line for the `group_theory` document.


---

Comment by jhpalmieri created at 2010-07-27 20:56:52

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-07-27 20:56:52

Here is a new patch.  This removes the file `Makefile` and adds `group_theory` and a descriptive sentence to `index.rst`.

As far as the comments above, they are beyond the scope of this ticket.  The point of this ticket was to move the file `functional_programming.rst` from the constructions document to the thematic tutorials document.  I think that some of the comments have some merit, but they involve revising that document.  I've opened #9612 for those revisions.

So I'm returning this to "needs review".  I'm actually happy with the original ticket, so the only things that need reviewing are the changes I made to index.rst, as well as the removal of Makefile.


---

Comment by leif created at 2010-07-27 21:34:45

Changing type from enhancement to defect.


---

Comment by leif created at 2010-07-27 21:34:45


```
sphinx-build -b html -d /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/doctrees/en/constructions    /home/leif/sage-4.5.2.alpha1/devel/sage/doc/en/constructions /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/html/en/constructions
Running Sphinx v0.6.3
...
/home/leif/sage-4.5.2.alpha1/devel/sage/doc/en/constructions/index.rst:28: (WARNING/2) toctree references unknown document u'functional_programming'
...
build succeeded, 1 warning.

...

sphinx-build -b html -d /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/doctrees/en/thematic_tutorials    /home/leif/sage-4.5.2.alpha1/devel/sage/doc/en/thematic_tutorials /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/html/en/thematic_tutorials
Running Sphinx v0.6.3
loading pickled environment... not found
building [html]: targets for 3 source files that are out of date
updating environment: 3 added, 0 changed, 0 removed
reading sources... [ 33%] functional_programming
reading sources... [ 66%] group_theory
reading sources... [100%] index

looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [ 33%] functional_programming
writing output... [ 66%] group_theory
writing output... [100%] index

writing additional files... genindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded.
Build finished.  The built documents can be found in /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/html/en/thematic_tutorials

...
```

(The bottom part is just informational.)

So just little work needed (dangling reference).

Thanks though for fixing this "eternal" error... ;-)


Changing this to "critical" and "defect", since actually this patch fixes a Sphinx build error.


---

Comment by leif created at 2010-07-27 21:34:45

Changing priority from major to critical.


---

Comment by leif created at 2010-07-27 21:34:45

Changing status from needs_review to needs_work.


---

Attachment

based on 4.5.2.alpha1.  apply only this patch.


---

Comment by jhpalmieri created at 2010-07-27 22:00:05

This patch should fix that problem.  (Only change: remove one line in `doc/en/constructions/index.rst`.)


---

Comment by jhpalmieri created at 2010-07-27 22:00:05

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-07-28 00:08:22

Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index `devel/sage/doc/output/html/en/index.html`.

Sorry, didn't look for that before...

The (re)build of the HTML documents now works as expected (without new warnings).


---

Comment by jhpalmieri created at 2010-07-28 00:14:01

> Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index devel/sage/doc/output/html/en/index.html. 

I think it gets added in #8442.


---

Comment by leif created at 2010-07-28 00:24:25

Replying to [comment:15 jhpalmieri]:
> > Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index devel/sage/doc/output/html/en/index.html. 
> 
> I think it gets added in #8442.

So can you merge the patch to `doc/en/website/templates/index.html` from http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-config.patch (if that's the correct one)?


---

Comment by jhpalmieri created at 2010-07-28 01:31:05

apply on top of trac_8465-v2.patch


---

Attachment

Okay, here you go.


---

Comment by jhpalmieri created at 2010-07-28 01:33:58

I should have renamed the new patch.  Despite its name, it *does* belong on this ticket, #8465.  The commit message has the correct ticket number.

If this is merged, we'll need to rebase some of the patches related to #8470, since some of those include the same changes to conf.py and to website/templates/index.html.


---

Comment by leif created at 2010-07-28 02:18:54

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-07-28 02:18:54

Cool!


## Note to the release managers

*Apply only trac_8465-v2.patch and* (despite its name) *trac_8442-config.patch.*

(The latter is only _a part of_ http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-config.patch)


---

Comment by ddrake created at 2010-07-28 05:06:51

Making a blocker so this gets into 4.5.2; it fixes a documentation build error.


---

Comment by ddrake created at 2010-07-28 05:06:51

Changing priority from critical to blocker.


---

Comment by mpatel created at 2010-07-29 04:43:50

Fix website `index.html` typo.  Apply on top of other two patches.


---

Comment by mpatel created at 2010-07-29 04:47:16

Resolution: fixed


---

Attachment

Replying to [comment:19 leif]:
> == Note to the release managers ==
 
> *Apply only trac_8465-v2.patch and* (despite its name) *trac_8442-config.patch.*

I'm merging these and a new [attachment:trac_8465-fix_typo.patch] into 4.5.2.rc0.  Can someone please check the latter?  There's no need to add me as an author.


---

Comment by jhpalmieri created at 2010-07-29 04:51:02

The typo patch is fine.
