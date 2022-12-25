# Issue 8465: move the document "Python Functional Programming for Mathematicians" to the classification "Sage HOWTOs"

archive/issues_008465.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @nexttime @qed777\n\nKeywords: Sage HOWTOs\n\nThe new document classification \"Sage HOWTOs\" aims to include various in-depth documentation/tutorials on specific topics. Here, we move the chapter [Python Functional Programming for Mathematicians](http://www.sagemath.org/doc/constructions/functional_programming.html) to the \"Sage HOWTOs\" classification. The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8465\n\n",
    "created_at": "2010-03-07T02:03:10Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "move the document \"Python Functional Programming for Mathematicians\" to the classification \"Sage HOWTOs\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @nexttime @qed777

Keywords: Sage HOWTOs

The new document classification "Sage HOWTOs" aims to include various in-depth documentation/tutorials on specific topics. Here, we move the chapter [Python Functional Programming for Mathematicians](http://www.sagemath.org/doc/constructions/functional_programming.html) to the "Sage HOWTOs" classification. The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).

Issue created by migration from https://trac.sagemath.org/ticket/8465





---

archive/issue_comments_076080.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T02:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076081.json:
```json
{
    "body": "Attachment [trac_8465-functional.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8465-functional.patch) by mvngu created at 2010-03-10 05:57:34\n\nbased on Sage 4.3.4.alpha1",
    "created_at": "2010-03-10T05:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8465-functional.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8465-functional.patch) by mvngu created at 2010-03-10 05:57:34

based on Sage 4.3.4.alpha1



---

archive/issue_comments_076082.json:
```json
{
    "body": "i hope that's the correct place to point out some ideas i have:\n(at least, i found them\nvery useful to know when i coded something recently)\n\n1. reduce will be part of the functools module in python 3. might be\nhelpful to import it from there to make it forward compatible\nhttp://docs.python.org/library/functools.html <- or at least you might\nwanna add a link to that module in the bottom section.\n\n2. http://docs.python.org/library/itertools.html#itertools.starmap is\nquite cool if you have \"izip\"ed values for the function arguments.\ni.e.\nstarmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000. it's like f(a,b) vs. f(*c)\n\n3. Besides that, have you explained the generator concept with the\n\"yield\" keyword? I'm not sure if that counts as functional programming\nbut it is a nice topic in that context.",
    "created_at": "2010-03-21T20:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76082",
    "user": "https://github.com/haraldschilly"
}
```

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

archive/issue_comments_076083.json:
```json
{
    "body": "Tested well, and looks good on Boxen. In the styles of programming section, the object-oriented example seemed a little contrived, and I would say was bad style to make an object for adding two things. I believe a better example would to use comparison instead of adding. Something procedural\n\ndef compare(a, b)\n   return a - b;\n\nversus like this for object-oriented\n\ndef class Comparable\n   def compare(b)\n     return self - b;\n\n~Mark",
    "created_at": "2010-05-04T06:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76083",
    "user": "https://trac.sagemath.org/admin/accounts/users/mjordan7"
}
```

Tested well, and looks good on Boxen. In the styles of programming section, the object-oriented example seemed a little contrived, and I would say was bad style to make an object for adding two things. I believe a better example would to use comparison instead of adding. Something procedural

def compare(a, b)
   return a - b;

versus like this for object-oriented

def class Comparable
   def compare(b)
     return self - b;

~Mark



---

archive/issue_comments_076084.json:
```json
{
    "body": "Minh, I'm setting this to needs work in light of the comments by Mark. If you don't feel this is justified could you briefly explain why here and then change it back to needs review?",
    "created_at": "2010-07-21T14:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76084",
    "user": "https://github.com/malb"
}
```

Minh, I'm setting this to needs work in light of the comments by Mark. If you don't feel this is justified could you briefly explain why here and then change it back to needs review?



---

archive/issue_comments_076085.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-21T14:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76085",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076086.json:
```json
{
    "body": "Two other comments: I don't think we need the file `doc/en/thematic_tutorials/Makefile`.  Also, the file `index.rst` should include a line for the `group_theory` document.",
    "created_at": "2010-07-27T20:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76086",
    "user": "https://github.com/jhpalmieri"
}
```

Two other comments: I don't think we need the file `doc/en/thematic_tutorials/Makefile`.  Also, the file `index.rst` should include a line for the `group_theory` document.



---

archive/issue_comments_076087.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-27T20:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76087",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076088.json:
```json
{
    "body": "Here is a new patch.  This removes the file `Makefile` and adds `group_theory` and a descriptive sentence to `index.rst`.\n\nAs far as the comments above, they are beyond the scope of this ticket.  The point of this ticket was to move the file `functional_programming.rst` from the constructions document to the thematic tutorials document.  I think that some of the comments have some merit, but they involve revising that document.  I've opened #9612 for those revisions.\n\nSo I'm returning this to \"needs review\".  I'm actually happy with the original ticket, so the only things that need reviewing are the changes I made to index.rst, as well as the removal of Makefile.",
    "created_at": "2010-07-27T20:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76088",
    "user": "https://github.com/jhpalmieri"
}
```

Here is a new patch.  This removes the file `Makefile` and adds `group_theory` and a descriptive sentence to `index.rst`.

As far as the comments above, they are beyond the scope of this ticket.  The point of this ticket was to move the file `functional_programming.rst` from the constructions document to the thematic tutorials document.  I think that some of the comments have some merit, but they involve revising that document.  I've opened #9612 for those revisions.

So I'm returning this to "needs review".  I'm actually happy with the original ticket, so the only things that need reviewing are the changes I made to index.rst, as well as the removal of Makefile.



---

archive/issue_comments_076089.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-07-27T21:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76089",
    "user": "https://github.com/nexttime"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_076090.json:
```json
{
    "body": "\n```\nsphinx-build -b html -d /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/doctrees/en/constructions    /home/leif/sage-4.5.2.alpha1/devel/sage/doc/en/constructions /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/html/en/constructions\nRunning Sphinx v0.6.3\n...\n/home/leif/sage-4.5.2.alpha1/devel/sage/doc/en/constructions/index.rst:28: (WARNING/2) toctree references unknown document u'functional_programming'\n...\nbuild succeeded, 1 warning.\n\n...\n\nsphinx-build -b html -d /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/doctrees/en/thematic_tutorials    /home/leif/sage-4.5.2.alpha1/devel/sage/doc/en/thematic_tutorials /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/html/en/thematic_tutorials\nRunning Sphinx v0.6.3\nloading pickled environment... not found\nbuilding [html]: targets for 3 source files that are out of date\nupdating environment: 3 added, 0 changed, 0 removed\nreading sources... [ 33%] functional_programming\nreading sources... [ 66%] group_theory\nreading sources... [100%] index\n\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [ 33%] functional_programming\nwriting output... [ 66%] group_theory\nwriting output... [100%] index\n\nwriting additional files... genindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded.\nBuild finished.  The built documents can be found in /home/leif/sage-4.5.2.alpha1/devel/sage/doc/output/html/en/thematic_tutorials\n\n...\n```\n\n(The bottom part is just informational.)\n\nSo just little work needed (dangling reference).\n\nThanks though for fixing this \"eternal\" error... ;-)\n\n\nChanging this to \"critical\" and \"defect\", since actually this patch fixes a Sphinx build error.",
    "created_at": "2010-07-27T21:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76090",
    "user": "https://github.com/nexttime"
}
```


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

archive/issue_comments_076091.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-07-27T21:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76091",
    "user": "https://github.com/nexttime"
}
```

Changing priority from major to critical.



---

archive/issue_comments_076092.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-27T21:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76092",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076093.json:
```json
{
    "body": "Attachment [trac_8465-v2.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8465-v2.patch) by @jhpalmieri created at 2010-07-27 21:41:31\n\nbased on 4.5.2.alpha1.  apply only this patch.",
    "created_at": "2010-07-27T21:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76093",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8465-v2.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8465-v2.patch) by @jhpalmieri created at 2010-07-27 21:41:31

based on 4.5.2.alpha1.  apply only this patch.



---

archive/issue_comments_076094.json:
```json
{
    "body": "This patch should fix that problem.  (Only change: remove one line in `doc/en/constructions/index.rst`.)",
    "created_at": "2010-07-27T22:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76094",
    "user": "https://github.com/jhpalmieri"
}
```

This patch should fix that problem.  (Only change: remove one line in `doc/en/constructions/index.rst`.)



---

archive/issue_comments_076095.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-27T22:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76095",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076096.json:
```json
{
    "body": "Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index `devel/sage/doc/output/html/en/index.html`.\n\nSorry, didn't look for that before...\n\nThe (re)build of the HTML documents now works as expected (without new warnings).",
    "created_at": "2010-07-28T00:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76096",
    "user": "https://github.com/nexttime"
}
```

Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index `devel/sage/doc/output/html/en/index.html`.

Sorry, didn't look for that before...

The (re)build of the HTML documents now works as expected (without new warnings).



---

archive/issue_comments_076097.json:
```json
{
    "body": "> Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index devel/sage/doc/output/html/en/index.html. \n\nI think it gets added in #8442.",
    "created_at": "2010-07-28T00:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76097",
    "user": "https://github.com/jhpalmieri"
}
```

> Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index devel/sage/doc/output/html/en/index.html. 

I think it gets added in #8442.



---

archive/issue_comments_076098.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> > Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index devel/sage/doc/output/html/en/index.html. \n> \n> I think it gets added in #8442.\n\nSo can you merge the patch to `doc/en/website/templates/index.html` from http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-config.patch (if that's the correct one)?",
    "created_at": "2010-07-28T00:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76098",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:15 jhpalmieri]:
> > Hmmm, I might be stupid, but I cannot find the Thematic Tutorials in (or from) the main index devel/sage/doc/output/html/en/index.html. 
> 
> I think it gets added in #8442.

So can you merge the patch to `doc/en/website/templates/index.html` from http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-config.patch (if that's the correct one)?



---

archive/issue_comments_076099.json:
```json
{
    "body": "apply on top of trac_8465-v2.patch",
    "created_at": "2010-07-28T01:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76099",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of trac_8465-v2.patch



---

archive/issue_comments_076100.json:
```json
{
    "body": "Attachment [trac_8442-config.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8442-config.patch) by @jhpalmieri created at 2010-07-28 01:31:40\n\nOkay, here you go.",
    "created_at": "2010-07-28T01:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76100",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8442-config.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8442-config.patch) by @jhpalmieri created at 2010-07-28 01:31:40

Okay, here you go.



---

archive/issue_comments_076101.json:
```json
{
    "body": "I should have renamed the new patch.  Despite its name, it **does** belong on this ticket, #8465.  The commit message has the correct ticket number.\n\nIf this is merged, we'll need to rebase some of the patches related to #8470, since some of those include the same changes to conf.py and to website/templates/index.html.",
    "created_at": "2010-07-28T01:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76101",
    "user": "https://github.com/jhpalmieri"
}
```

I should have renamed the new patch.  Despite its name, it **does** belong on this ticket, #8465.  The commit message has the correct ticket number.

If this is merged, we'll need to rebase some of the patches related to #8470, since some of those include the same changes to conf.py and to website/templates/index.html.



---

archive/issue_comments_076102.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-28T02:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76102",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076103.json:
```json
{
    "body": "Cool!\n\n\n## Note to the release managers\n\n**Apply only trac_8465-v2.patch and** (despite its name) **trac_8442-config.patch.**\n\n(The latter is only *a part of* http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-config.patch)",
    "created_at": "2010-07-28T02:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76103",
    "user": "https://github.com/nexttime"
}
```

Cool!


## Note to the release managers

**Apply only trac_8465-v2.patch and** (despite its name) **trac_8442-config.patch.**

(The latter is only *a part of* http://trac.sagemath.org/sage_trac/attachment/ticket/8442/trac_8442-config.patch)



---

archive/issue_comments_076104.json:
```json
{
    "body": "Making a blocker so this gets into 4.5.2; it fixes a documentation build error.",
    "created_at": "2010-07-28T05:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76104",
    "user": "https://github.com/dandrake"
}
```

Making a blocker so this gets into 4.5.2; it fixes a documentation build error.



---

archive/issue_comments_076105.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-07-28T05:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76105",
    "user": "https://github.com/dandrake"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_076106.json:
```json
{
    "body": "Fix website `index.html` typo.  Apply on top of other two patches.",
    "created_at": "2010-07-29T04:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76106",
    "user": "https://github.com/qed777"
}
```

Fix website `index.html` typo.  Apply on top of other two patches.



---

archive/issue_comments_076107.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T04:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76107",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_076108.json:
```json
{
    "body": "Attachment [trac_8465-fix_typo.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8465-fix_typo.patch) by @qed777 created at 2010-07-29 04:47:16\n\nReplying to [comment:19 leif]:\n> == Note to the release managers ==\n \n> **Apply only trac_8465-v2.patch and** (despite its name) **trac_8442-config.patch.**\n\nI'm merging these and a new [attachment:trac_8465-fix_typo.patch] into 4.5.2.rc0.  Can someone please check the latter?  There's no need to add me as an author.",
    "created_at": "2010-07-29T04:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76108",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8465-fix_typo.patch](tarball://root/attachments/some-uuid/ticket8465/trac_8465-fix_typo.patch) by @qed777 created at 2010-07-29 04:47:16

Replying to [comment:19 leif]:
> == Note to the release managers ==
 
> **Apply only trac_8465-v2.patch and** (despite its name) **trac_8442-config.patch.**

I'm merging these and a new [attachment:trac_8465-fix_typo.patch] into 4.5.2.rc0.  Can someone please check the latter?  There's no need to add me as an author.



---

archive/issue_comments_076109.json:
```json
{
    "body": "The typo patch is fine.",
    "created_at": "2010-07-29T04:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8465#issuecomment-76109",
    "user": "https://github.com/jhpalmieri"
}
```

The typo patch is fine.
