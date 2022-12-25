# Issue 7448: Improve sphinx rendering of categories in reference manual.

archive/issues_007448.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  @mwhansen @nthiery @jhpalmieri\n\nKeywords: Sphinx categories.\n\nSince #7443, categories now appear in the reference manual. But Sphinx rendering in very poor. In particular, I can't manage to get nested class appearing in the doc though I've read that they are supported by Sphinx. Once someone (Mike ?) explain me the solution, I'll be glad to implement it. \n\nCheers,\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/7448\n\n",
    "created_at": "2009-11-12T20:45:17Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Improve sphinx rendering of categories in reference manual.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7448",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  @mwhansen @nthiery @jhpalmieri

Keywords: Sphinx categories.

Since #7443, categories now appear in the reference manual. But Sphinx rendering in very poor. In particular, I can't manage to get nested class appearing in the doc though I've read that they are supported by Sphinx. Once someone (Mike ?) explain me the solution, I'll be glad to implement it. 

Cheers,

Florent

Issue created by migration from https://trac.sagemath.org/ticket/7448





---

archive/issue_comments_062584.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-11-12T20:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62584",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_062585.json:
```json
{
    "body": "See #6664.  We need to figure out how to resolve the issues there.",
    "created_at": "2009-11-13T06:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62585",
    "user": "https://github.com/mwhansen"
}
```

See #6664.  We need to figure out how to resolve the issues there.



---

archive/issue_comments_062586.json:
```json
{
    "body": "Mistaking inner classes for aliased attributes seems likely to be a Sphinx bug that we should report upstream, e.g., to [sphinx-dev](http://groups.google.com/group/sphinx-dev).\n\nIs there a minimal example we can submit that reproduces the problem?",
    "created_at": "2010-02-16T22:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62586",
    "user": "https://github.com/qed777"
}
```

Mistaking inner classes for aliased attributes seems likely to be a Sphinx bug that we should report upstream, e.g., to [sphinx-dev](http://groups.google.com/group/sphinx-dev).

Is there a minimal example we can submit that reproduces the problem?



---

archive/issue_comments_062587.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Mistaking inner classes for aliased attributes seems likely to be a Sphinx bug that we should report upstream, e.g., to [sphinx-dev](http://groups.google.com/group/sphinx-dev).\n> \n> Is there a minimal example we can submit that reproduces the problem?\n\n\nI've made some experiments. Actually it seems that the problem is a bad interaction between sphinx and the particular metaclass `NestedMetaclass` we have to use to work around the nested class pickling bug of python. If you apply the attached patch, you'll see that `TestParent1` is correctly rendered whereas the other parent are not. I think this is a lead which should be followed.",
    "created_at": "2010-02-17T20:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62587",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:3 mpatel]:
> Mistaking inner classes for aliased attributes seems likely to be a Sphinx bug that we should report upstream, e.g., to [sphinx-dev](http://groups.google.com/group/sphinx-dev).
> 
> Is there a minimal example we can submit that reproduces the problem?


I've made some experiments. Actually it seems that the problem is a bad interaction between sphinx and the particular metaclass `NestedMetaclass` we have to use to work around the nested class pickling bug of python. If you apply the attached patch, you'll see that `TestParent1` is correctly rendered whereas the other parent are not. I think this is a lead which should be followed.



---

archive/issue_comments_062588.json:
```json
{
    "body": "Patch to experiment the interaction Sphinx/NestedMetaclass",
    "created_at": "2010-02-17T20:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62588",
    "user": "https://github.com/hivert"
}
```

Patch to experiment the interaction Sphinx/NestedMetaclass



---

archive/issue_comments_062589.json:
```json
{
    "body": "Attachment [trac_7448-nested_class_sphinx_exper-fh.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx_exper-fh.patch) by @hivert created at 2010-02-17 21:21:55\n\n> I've made some experiments. Actually it seems that the problem is a bad interaction between sphinx and the particular metaclass `NestedMetaclass` we have to use to work around the nested class pickling bug of python. If you apply the attached patch, you'll see that `TestParent1` is correctly rendered whereas the other parent are not. I think this is a lead which should be followed. \n\n\nMore info on this: to workaround python's nested class pickle bug we put any class which contain a nested class into `NestedMetaclass`. The main purpose of this metaclass is to change the class `__name__` with the help of the function\n`modify_for_nested_pickle`. As a result sphinx has the impression that the class is an alias. Demonstration: if I comment line 112 of nested_class.py\n\n```\ndiff --git a/sage/misc/nested_class.py b/sage/misc/nested_class.py\n--- a/sage/misc/nested_class.py\n+++ b/sage/misc/nested_class.py\n@@ -108,7 +108,7 @@ def modify_for_nested_pickle(cls, name_p\n             if v.__name__ == name and v.__module__ == module.__name__ and getattr(module, name, None) is not v:\n                 # OK, probably this is a nested class.\n                 dotted_name = name_prefix + '.' + name\n-                v.__name__ = dotted_name\n+                # v.__name__ = dotted_name\n                 setattr(module, dotted_name, v)\n                 modify_for_nested_pickle(v, dotted_name, module)\n```\nThen everything works fine. Any idea to solve this ?",
    "created_at": "2010-02-17T21:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62589",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7448-nested_class_sphinx_exper-fh.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx_exper-fh.patch) by @hivert created at 2010-02-17 21:21:55

> I've made some experiments. Actually it seems that the problem is a bad interaction between sphinx and the particular metaclass `NestedMetaclass` we have to use to work around the nested class pickling bug of python. If you apply the attached patch, you'll see that `TestParent1` is correctly rendered whereas the other parent are not. I think this is a lead which should be followed. 


More info on this: to workaround python's nested class pickle bug we put any class which contain a nested class into `NestedMetaclass`. The main purpose of this metaclass is to change the class `__name__` with the help of the function
`modify_for_nested_pickle`. As a result sphinx has the impression that the class is an alias. Demonstration: if I comment line 112 of nested_class.py

```
diff --git a/sage/misc/nested_class.py b/sage/misc/nested_class.py
--- a/sage/misc/nested_class.py
+++ b/sage/misc/nested_class.py
@@ -108,7 +108,7 @@ def modify_for_nested_pickle(cls, name_p
             if v.__name__ == name and v.__module__ == module.__name__ and getattr(module, name, None) is not v:
                 # OK, probably this is a nested class.
                 dotted_name = name_prefix + '.' + name
-                v.__name__ = dotted_name
+                # v.__name__ = dotted_name
                 setattr(module, dotted_name, v)
                 modify_for_nested_pickle(v, dotted_name, module)
```
Then everything works fine. Any idea to solve this ?



---

archive/issue_comments_062590.json:
```json
{
    "body": "Things are progressing with the help of Mike Hansen on irc: The submitted patch to autodoc.py partially solve the problem. Now each nested class is documented twice ! I'm trying to remove one.",
    "created_at": "2010-02-17T22:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62590",
    "user": "https://github.com/hivert"
}
```

Things are progressing with the help of Mike Hansen on irc: The submitted patch to autodoc.py partially solve the problem. Now each nested class is documented twice ! I'm trying to remove one.



---

archive/issue_comments_062591.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-02-17T22:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62591",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_062592.json:
```json
{
    "body": "This should solve the problem:\nApplying\n\n```\nautodoc.py.patch\n``` \nto\n\n```\nSphinx-0.6.3-py2.6.egg/sphinx/ext/autodoc.py\n```\nand `trac_7448-nested_class_sphinx-fh.patch`\nshould solve the problem.",
    "created_at": "2010-02-17T23:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62592",
    "user": "https://github.com/hivert"
}
```

This should solve the problem:
Applying

```
autodoc.py.patch
``` 
to

```
Sphinx-0.6.3-py2.6.egg/sphinx/ext/autodoc.py
```
and `trac_7448-nested_class_sphinx-fh.patch`
should solve the problem.



---

archive/issue_comments_062593.json:
```json
{
    "body": "Changing component from categories to documentation.",
    "created_at": "2010-02-17T23:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62593",
    "user": "https://github.com/hivert"
}
```

Changing component from categories to documentation.



---

archive/issue_comments_062594.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-17T23:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62594",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062595.json:
```json
{
    "body": "Two remarks:\n\n- Thanks to Mike Hansen for its help on IRC.\n- Since I'm patching the sources of sphinx, I probably need something like rebuilding sphinx spkg. Unfortunately, I don't know how to do this. Help welcome ! \n\nFlorent, off to bed :-)",
    "created_at": "2010-02-18T00:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62595",
    "user": "https://github.com/hivert"
}
```

Two remarks:

- Thanks to Mike Hansen for its help on IRC.
- Since I'm patching the sources of sphinx, I probably need something like rebuilding sphinx spkg. Unfortunately, I don't know how to do this. Help welcome ! 

Florent, off to bed :-)



---

archive/issue_comments_062596.json:
```json
{
    "body": "Replying to [comment:9 hivert]:\n> Since I'm patching the sources of sphinx, I probably need something like rebuilding sphinx spkg. Unfortunately, I don't know how to do this. Help welcome ! \n\n\nHere's a new spkg:\n\n- [http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p5.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p5.spkg)\n\n(I haven't tested the patch here, just implemented it and built the spkg.  Please check the file autodoc.py to make sure I patched it right.)",
    "created_at": "2010-02-18T04:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62596",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:9 hivert]:
> Since I'm patching the sources of sphinx, I probably need something like rebuilding sphinx spkg. Unfortunately, I don't know how to do this. Help welcome ! 


Here's a new spkg:

- [http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p5.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p5.spkg)

(I haven't tested the patch here, just implemented it and built the spkg.  Please check the file autodoc.py to make sure I patched it right.)



---

archive/issue_comments_062597.json:
```json
{
    "body": "To test this, do we need to add sage.misc.nested_class and/or sage.misc.nested_class_test to the reference manual?",
    "created_at": "2010-02-18T04:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62597",
    "user": "https://github.com/jhpalmieri"
}
```

To test this, do we need to add sage.misc.nested_class and/or sage.misc.nested_class_test to the reference manual?



---

archive/issue_comments_062598.json:
```json
{
    "body": "Hi John,\n\nReplying to [comment:12 jhpalmieri]:\n> (I haven't tested the patch here, just implemented it and built the spkg. Please check the file autodoc.py to make sure I patched it right.)  \n\n\nThank for this. Is this normal that the file\n\n```\n./patches/autodoc.py\n```\ncontains the modifications, whereas\n\n```\n./src/sphinx/ext/autodoc.py\n```\ndoesn't ? It seems that the answer is yes and that the former replace the later during build. Everthing seems to be ok. \n\n> To test this, do we need to add sage.misc.nested_class and/or sage.misc.nested_class_test to the reference manual?\n\n\nNo you don't ! Moreover, sage.misc.nested_class has already been added since #8250 merged in sage-4.3.3.alpha1. If you want to see the result pick a random file with nested class. They are plenty of them in categories, see eg\n\n```\nsage/categories/semigroups.py\n```\nwhich has many thing implemented in nested classes. \n\nNote that now that we do see nested classes, we find out that they are plenty of room for improvement in those docs. It will be the purpose of an (or more probably several) other ticket.",
    "created_at": "2010-02-18T07:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62598",
    "user": "https://github.com/hivert"
}
```

Hi John,

Replying to [comment:12 jhpalmieri]:
> (I haven't tested the patch here, just implemented it and built the spkg. Please check the file autodoc.py to make sure I patched it right.)  


Thank for this. Is this normal that the file

```
./patches/autodoc.py
```
contains the modifications, whereas

```
./src/sphinx/ext/autodoc.py
```
doesn't ? It seems that the answer is yes and that the former replace the later during build. Everthing seems to be ok. 

> To test this, do we need to add sage.misc.nested_class and/or sage.misc.nested_class_test to the reference manual?


No you don't ! Moreover, sage.misc.nested_class has already been added since #8250 merged in sage-4.3.3.alpha1. If you want to see the result pick a random file with nested class. They are plenty of them in categories, see eg

```
sage/categories/semigroups.py
```
which has many thing implemented in nested classes. 

Note that now that we do see nested classes, we find out that they are plenty of room for improvement in those docs. It will be the purpose of an (or more probably several) other ticket.



---

archive/issue_comments_062599.json:
```json
{
    "body": "Summary of discussion with Florent over the phone:\n- the patch to autodoc could be made more robust and include an analysis of the problem\n- we have an example where Sphinx screws up, with plain Python nested classes (without NestedClassMetaclass), and has no chance to do any better without fixing nested class names as does NestedClassMetaclass.\n\nFlorent will post an improved patch, but not right away. So if there is an emergency to get this into 4.4, I give a positive review on that particular patch to get in as is.",
    "created_at": "2010-02-18T10:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62599",
    "user": "https://github.com/nthiery"
}
```

Summary of discussion with Florent over the phone:
- the patch to autodoc could be made more robust and include an analysis of the problem
- we have an example where Sphinx screws up, with plain Python nested classes (without NestedClassMetaclass), and has no chance to do any better without fixing nested class names as does NestedClassMetaclass.

Florent will post an improved patch, but not right away. So if there is an emergency to get this into 4.4, I give a positive review on that particular patch to get in as is.



---

archive/issue_comments_062600.json:
```json
{
    "body": "Replying to [comment:13 hivert]:\n> Thank for this. Is this normal that the file ./patches/autodoc.py\n> contains the modifications, whereas\n> ./src/sphinx/ext/autodoc.py\n> doesn't ? It seems that the answer is yes and that the former replace the later during build. Everthing seems to be ok. \n\n\nYes, it's normal: in a typical spkg, the \"src\" directory is supposed to contain the original unmodified source, and then it gets patched by running spkg-install.  \n\nI noticed that the nested classes in categories/coxeter_groups seem to be rendered correctly, so I guess that's good evidence that it's working.",
    "created_at": "2010-02-18T16:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62600",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:13 hivert]:
> Thank for this. Is this normal that the file ./patches/autodoc.py
> contains the modifications, whereas
> ./src/sphinx/ext/autodoc.py
> doesn't ? It seems that the answer is yes and that the former replace the later during build. Everthing seems to be ok. 


Yes, it's normal: in a typical spkg, the "src" directory is supposed to contain the original unmodified source, and then it gets patched by running spkg-install.  

I noticed that the nested classes in categories/coxeter_groups seem to be rendered correctly, so I guess that's good evidence that it's working.



---

archive/issue_comments_062601.json:
```json
{
    "body": "> Yes, it's normal: in a typical spkg, the \"src\" directory is supposed to contain the original unmodified source, and then it gets patched by running spkg-install.  \n\n\nSo that if I want to update the spkg, I only need to update the file in `patch/autodoc.py` file, commit it with hg and tar the whole thing, am I right ? \n \n> I noticed that the nested classes in categories/coxeter_groups seem to be rendered correctly, so I guess that's good evidence that it's working.\n\n\nCool !",
    "created_at": "2010-02-18T16:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62601",
    "user": "https://github.com/hivert"
}
```

> Yes, it's normal: in a typical spkg, the "src" directory is supposed to contain the original unmodified source, and then it gets patched by running spkg-install.  


So that if I want to update the spkg, I only need to update the file in `patch/autodoc.py` file, commit it with hg and tar the whole thing, am I right ? 
 
> I noticed that the nested classes in categories/coxeter_groups seem to be rendered correctly, so I guess that's good evidence that it's working.


Cool !



---

archive/issue_comments_062602.json:
```json
{
    "body": "Replying to [comment:16 hivert]:\n> So that if I want to update the spkg, I only need to update the file in `patch/autodoc.py` file, commit it with hg and tar the whole thing, am I right ? \n\n\nYou should update `patches/autodoc.py` and also `patches/autodoc.patch`: this one never gets used, but it's helpful to see how autodoc.py was actually changed.  While in the patches directory, I just do something like `diff -u ../src/sphinx/ext/autodoc.py autodoc.py > autodoc.patch`.\n\nYou might also update SPKG.txt, which includes the change log.  I put your name down for the new patch to autodoc.py, for example.  You also need to decide if you need to bump the patch level up: just keep the directory as it is, sphinx-0.6.3.p5, or rename it to sphinx-0.6.3.p6.  I think if you're just tinkering with this patch, keep it as \"p5\".\n\nFinally, going to the directory containing sphinx-0.6.3.p5, you run \"sage -pkg sphinx-0.6.3.p5\" to create the spkg file.",
    "created_at": "2010-02-18T17:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62602",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:16 hivert]:
> So that if I want to update the spkg, I only need to update the file in `patch/autodoc.py` file, commit it with hg and tar the whole thing, am I right ? 


You should update `patches/autodoc.py` and also `patches/autodoc.patch`: this one never gets used, but it's helpful to see how autodoc.py was actually changed.  While in the patches directory, I just do something like `diff -u ../src/sphinx/ext/autodoc.py autodoc.py > autodoc.patch`.

You might also update SPKG.txt, which includes the change log.  I put your name down for the new patch to autodoc.py, for example.  You also need to decide if you need to bump the patch level up: just keep the directory as it is, sphinx-0.6.3.p5, or rename it to sphinx-0.6.3.p6.  I think if you're just tinkering with this patch, keep it as "p5".

Finally, going to the directory containing sphinx-0.6.3.p5, you run "sage -pkg sphinx-0.6.3.p5" to create the spkg file.



---

archive/issue_comments_062603.json:
```json
{
    "body": "Attachment [trac_7448-nested_class_sphinx-fh.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.patch) by @hivert created at 2010-02-20 00:05:09",
    "created_at": "2010-02-20T00:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62603",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7448-nested_class_sphinx-fh.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.patch) by @hivert created at 2010-02-20 00:05:09



---

archive/issue_comments_062604.json:
```json
{
    "body": "patch to sphinx autodoc.py",
    "created_at": "2010-02-20T00:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62604",
    "user": "https://github.com/hivert"
}
```

patch to sphinx autodoc.py



---

archive/issue_comments_062605.json:
```json
{
    "body": "Attachment [autodoc.py.patch](tarball://root/attachments/some-uuid/ticket7448/autodoc.py.patch) by @hivert created at 2010-02-20 00:14:14\n\nI should have reached a final state for this ticket. I've added a lot of comment explaining what's happening. Please review.\n\nI uploaded a new patch for sphinx and for autodoc.py. Do *not* apply `trac_7448-nested_class_sphinx_exper-fh.patch` which was used for experiments. \n\nmpatel told on #8258 he will take care or building the spkg. Many thanks to him.",
    "created_at": "2010-02-20T00:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62605",
    "user": "https://github.com/hivert"
}
```

Attachment [autodoc.py.patch](tarball://root/attachments/some-uuid/ticket7448/autodoc.py.patch) by @hivert created at 2010-02-20 00:14:14

I should have reached a final state for this ticket. I've added a lot of comment explaining what's happening. Please review.

I uploaded a new patch for sphinx and for autodoc.py. Do *not* apply `trac_7448-nested_class_sphinx_exper-fh.patch` which was used for experiments. 

mpatel told on #8258 he will take care or building the spkg. Many thanks to him.



---

archive/issue_comments_062606.json:
```json
{
    "body": "Combined patch rebased vs. #8244.  Apply *only* this patch.  sage repo.",
    "created_at": "2010-02-20T21:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62606",
    "user": "https://github.com/qed777"
}
```

Combined patch rebased vs. #8244.  Apply *only* this patch.  sage repo.



---

archive/issue_comments_062607.json:
```json
{
    "body": "Attachment [trac_7448-nested_class_sphinx-fh.2.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.2.patch) by @qed777 created at 2010-02-20 21:11:08\n\nI've attached a combined patch that's rebased against #8244.  That ticket adds a custom `sage_autodoc` extension to the sage repository.  We don't need to update the Sphinx spkg here.\n\nPlease check that I did this correctly.  Thanks!",
    "created_at": "2010-02-20T21:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62607",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7448-nested_class_sphinx-fh.2.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.2.patch) by @qed777 created at 2010-02-20 21:11:08

I've attached a combined patch that's rebased against #8244.  That ticket adds a custom `sage_autodoc` extension to the sage repository.  We don't need to update the Sphinx spkg here.

Please check that I did this correctly.  Thanks!



---

archive/issue_comments_062608.json:
```json
{
    "body": "After this ticket is reviewed, I'll rebase #7549.",
    "created_at": "2010-02-20T21:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62608",
    "user": "https://github.com/qed777"
}
```

After this ticket is reviewed, I'll rebase #7549.



---

archive/issue_comments_062609.json:
```json
{
    "body": "An off-topic note about\n\n```\ncombinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object\ncombinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object\n```\nI think we can suppress these by using `import random` and calling `random.random()`.",
    "created_at": "2010-02-21T00:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62609",
    "user": "https://github.com/qed777"
}
```

An off-topic note about

```
combinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object
combinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object
```
I think we can suppress these by using `import random` and calling `random.random()`.



---

archive/issue_comments_062610.json:
```json
{
    "body": "Replying to [comment:21 mpatel]:\n> I think we can suppress these by using `import random` and calling `random.random()`.\n\nSee #8326.",
    "created_at": "2010-02-22T06:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62610",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:21 mpatel]:
> I think we can suppress these by using `import random` and calling `random.random()`.

See #8326.



---

archive/issue_comments_062611.json:
```json
{
    "body": "After some discussion I've found a better logic for raising warning. I'm working again on it.",
    "created_at": "2010-02-23T00:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62611",
    "user": "https://github.com/hivert"
}
```

After some discussion I've found a better logic for raising warning. I'm working again on it.



---

archive/issue_comments_062612.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-23T00:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62612",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062613.json:
```json
{
    "body": "Attachment [autodoc.py.2.patch](tarball://root/attachments/some-uuid/ticket7448/autodoc.py.2.patch) by @hivert created at 2010-02-23 20:12:01",
    "created_at": "2010-02-23T20:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62613",
    "user": "https://github.com/hivert"
}
```

Attachment [autodoc.py.2.patch](tarball://root/attachments/some-uuid/ticket7448/autodoc.py.2.patch) by @hivert created at 2010-02-23 20:12:01



---

archive/issue_comments_062614.json:
```json
{
    "body": "Attachment [trac_7448-nested_class_sphinx-fh.3.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.3.patch) by @hivert created at 2010-02-23 20:20:28\n\nHi there ! I just uploaded what should be the final version of this patch:\n`autodoc.py` and `autodoc.py.2.patch` and ` trac_7448-nested_class_sphinx-fh.3.patch`. If you wan't to test the rendering you can comment\n\n```\n__all__ = [] # Don't document any parents\n``` \nat the beginning of `nested_class_test.py`.",
    "created_at": "2010-02-23T20:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62614",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7448-nested_class_sphinx-fh.3.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.3.patch) by @hivert created at 2010-02-23 20:20:28

Hi there ! I just uploaded what should be the final version of this patch:
`autodoc.py` and `autodoc.py.2.patch` and ` trac_7448-nested_class_sphinx-fh.3.patch`. If you wan't to test the rendering you can comment

```
__all__ = [] # Don't document any parents
``` 
at the beginning of `nested_class_test.py`.



---

archive/issue_comments_062615.json:
```json
{
    "body": "Changing keywords from \"Sphinx categories.\" to \"Sphinx, nested classes\".",
    "created_at": "2010-02-23T20:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62615",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "Sphinx categories." to "Sphinx, nested classes".



---

archive/issue_comments_062616.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-23T20:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62616",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062617.json:
```json
{
    "body": "Rebased for queue in comment.  Apply only this patch.",
    "created_at": "2010-02-24T04:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62617",
    "user": "https://github.com/qed777"
}
```

Rebased for queue in comment.  Apply only this patch.



---

archive/issue_comments_062618.json:
```json
{
    "body": "Attachment [trac_7448-nested_class_sphinx-fh.4.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.4.patch) by @qed777 created at 2010-02-24 04:32:56\n\nV4 is rebased for the following queue:\n\n```\ntrac_8244-slot_wrapper_argspec.patch\ntrac_8244-conf-autodoc.2.patch\ntrac_8244-sagedoc.patch\ntrac_7448-nested_class_sphinx-fh.4.patch\n```\nWith #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].\n\nQuestions:\n\n* Are there objections to making the unpicklable class check optional?  We could add a command-line option. \n* Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:\n\n```diff\ndiff --git a/doc/common/sage_autodoc.py b/doc/common/sage_autodoc.py\n--- a/doc/common/sage_autodoc.py\n+++ b/doc/common/sage_autodoc.py\n@@ -848,7 +848,9 @@ class ClassDocumenter(ModuleLevelDocumen\n         # as data/attribute\n         if ret:\n             if hasattr(self.object, '__name__'):\n-                self.doc_as_attr = (self.objpath[-1] != self.object.__name__)\n+                name = self.object.__name__\n+                self.doc_as_attr = (self.objpath != name.split('.') and \n+                                    self.check_module())\n             else:\n                 self.doc_as_attr = True\n         return ret\n```\n  and make it easier to upgrade to newer Sphinx versions.\n\nNote: We have made changes to `environment.py` and `highlighting.py` and other changes to `autodoc.py`.  But Georg Brandl has recently committed a [change](http://bitbucket.org/birkenfeld/sphinx/changeset/ee86e8563c6f/) --- requested by Mike Hansen? --- that should allow us to revert to the upstream `enviroment.py` and `autodoc.py`, modulo this ticket.  Actually, I think we can avoid patching `highlighting.py`, too, if we [subclass Pygments' Python lexer](http://pygments.org/docs/lexerdevelopment/).",
    "created_at": "2010-02-24T04:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62618",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7448-nested_class_sphinx-fh.4.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.4.patch) by @qed777 created at 2010-02-24 04:32:56

V4 is rebased for the following queue:

```
trac_8244-slot_wrapper_argspec.patch
trac_8244-conf-autodoc.2.patch
trac_8244-sagedoc.patch
trac_7448-nested_class_sphinx-fh.4.patch
```
With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].

Questions:

* Are there objections to making the unpicklable class check optional?  We could add a command-line option. 
* Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:

```diff
diff --git a/doc/common/sage_autodoc.py b/doc/common/sage_autodoc.py
--- a/doc/common/sage_autodoc.py
+++ b/doc/common/sage_autodoc.py
@@ -848,7 +848,9 @@ class ClassDocumenter(ModuleLevelDocumen
         # as data/attribute
         if ret:
             if hasattr(self.object, '__name__'):
-                self.doc_as_attr = (self.objpath[-1] != self.object.__name__)
+                name = self.object.__name__
+                self.doc_as_attr = (self.objpath != name.split('.') and 
+                                    self.check_module())
             else:
                 self.doc_as_attr = True
         return ret
```
  and make it easier to upgrade to newer Sphinx versions.

Note: We have made changes to `environment.py` and `highlighting.py` and other changes to `autodoc.py`.  But Georg Brandl has recently committed a [change](http://bitbucket.org/birkenfeld/sphinx/changeset/ee86e8563c6f/) --- requested by Mike Hansen? --- that should allow us to revert to the upstream `enviroment.py` and `autodoc.py`, modulo this ticket.  Actually, I think we can avoid patching `highlighting.py`, too, if we [subclass Pygments' Python lexer](http://pygments.org/docs/lexerdevelopment/).



---

archive/issue_comments_062619.json:
```json
{
    "body": "Replying to [comment:26 mpatel]:\n> V4 is rebased for the following queue:\n\n{{{\ntrac_8244-slot_wrapper_argspec.patch\ntrac_8244-conf-autodoc.2.patch\ntrac_8244-sagedoc.patch\ntrac_7448-nested_class_sphinx-fh.4.patch\n}}}\n\nThanks for this !\n> With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].\n\n\nWhat do you mean by refresh here ? \n\n> Questions:\n> \n> * Are there objections to making the unpicklable class check optional?  We could add a command-line option.\n\n\nNo objection ! Actually I think this has nothing to do with sphinx and it should be tested during the import. I put it here because if a class is detected as unpicklable, there is a very good chance it ends up typeset incorrectly by sphinx.  \n\n>  * Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:\n>    and make it easier to upgrade to newer Sphinx versions.\n\n\nSure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.",
    "created_at": "2010-02-28T08:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62619",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:26 mpatel]:
> V4 is rebased for the following queue:

{{{
trac_8244-slot_wrapper_argspec.patch
trac_8244-conf-autodoc.2.patch
trac_8244-sagedoc.patch
trac_7448-nested_class_sphinx-fh.4.patch
}}}

Thanks for this !
> With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].


What do you mean by refresh here ? 

> Questions:
> 
> * Are there objections to making the unpicklable class check optional?  We could add a command-line option.


No objection ! Actually I think this has nothing to do with sphinx and it should be tested during the import. I put it here because if a class is detected as unpicklable, there is a very good chance it ends up typeset incorrectly by sphinx.  

>  * Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:
>    and make it easier to upgrade to newer Sphinx versions.


Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.



---

archive/issue_comments_062620.json:
```json
{
    "body": "Replying to [comment:27 hivert]:\n> > With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].\n\n> What do you mean by refresh here ? \n\nJust that I suggest any further changes be updates to that patch, via `hg qrefresh`, if it's appropriate.\n\n> >  * Are there objections to making the unpicklable class check optional?  We could add a command-line option.\n \n> No objection ! Actually I think this has nothing to do with sphinx and it should be \n> tested during the import. I put it here because if a class is detected as unpicklable, there is a very good chance it ends up typeset incorrectly by sphinx.  \n\n\nSince it doesn't seem to belong in the docbuild system, can we put this check elsewhere, e.g., in the unit/doc-testing system?  And restrict this ticket to nested class rendering?\n\n> >  * Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:\n> >    and make it easier to upgrade to newer Sphinx versions.\n \n> Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  \n\nI tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.\n\nI may be overreacting.  Thoughts?",
    "created_at": "2010-03-03T00:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62620",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:27 hivert]:
> > With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].

> What do you mean by refresh here ? 

Just that I suggest any further changes be updates to that patch, via `hg qrefresh`, if it's appropriate.

> >  * Are there objections to making the unpicklable class check optional?  We could add a command-line option.
 
> No objection ! Actually I think this has nothing to do with sphinx and it should be 
> tested during the import. I put it here because if a class is detected as unpicklable, there is a very good chance it ends up typeset incorrectly by sphinx.  


Since it doesn't seem to belong in the docbuild system, can we put this check elsewhere, e.g., in the unit/doc-testing system?  And restrict this ticket to nested class rendering?

> >  * Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:
> >    and make it easier to upgrade to newer Sphinx versions.
 
> Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  

I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.

I may be overreacting.  Thoughts?



---

archive/issue_comments_062621.json:
```json
{
    "body": "Only fix rendering of nested classes.",
    "created_at": "2010-03-05T15:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62621",
    "user": "https://github.com/qed777"
}
```

Only fix rendering of nested classes.



---

archive/issue_comments_062622.json:
```json
{
    "body": "Attachment [trac_7448-nested_class_sphinx-fh.5.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.5.patch) by @qed777 created at 2010-03-06 00:47:04\n\nReplying to [comment:28 mpatel]:\n> > Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  \n\n> I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.\n\nI've attached V5, which should \"just\" fix Sphinx's rendering of nested classes.  To the extent it counts, my review is positive.  Could someone please review V5 for this ticket?  I've opened #8452 for the nested class pickling check and will make a patch for that.",
    "created_at": "2010-03-06T00:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62622",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7448-nested_class_sphinx-fh.5.patch](tarball://root/attachments/some-uuid/ticket7448/trac_7448-nested_class_sphinx-fh.5.patch) by @qed777 created at 2010-03-06 00:47:04

Replying to [comment:28 mpatel]:
> > Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  

> I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.

I've attached V5, which should "just" fix Sphinx's rendering of nested classes.  To the extent it counts, my review is positive.  Could someone please review V5 for this ticket?  I've opened #8452 for the nested class pickling check and will make a patch for that.



---

archive/issue_events_017662.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2010-03-06T10:15:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "milestone": "sage-4.3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7448#event-17662"
}
```



---

archive/issue_comments_062623.json:
```json
{
    "body": "Replying to [comment:29 mpatel]:\n> Replying to [comment:28 mpatel]:\n> > > Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  \n\n> > I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.\n> \n> I've attached V5, which should \"just\" fix Sphinx's rendering of nested classes.  To the extent it counts, my review is positive.  Could someone please review V5 for this ticket?  I've opened #8452 for the nested class pickling check and will make a patch for that.\n\n\nHi Mitesh,\n\nThanks for taking care of this ! I'm Ok with the change you made to my patches so that I suppose I'm allowed to put a positive review on this ticket.",
    "created_at": "2010-03-06T10:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62623",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:29 mpatel]:
> Replying to [comment:28 mpatel]:
> > > Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  

> > I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.
> 
> I've attached V5, which should "just" fix Sphinx's rendering of nested classes.  To the extent it counts, my review is positive.  Could someone please review V5 for this ticket?  I've opened #8452 for the nested class pickling check and will make a patch for that.


Hi Mitesh,

Thanks for taking care of this ! I'm Ok with the change you made to my patches so that I suppose I'm allowed to put a positive review on this ticket.



---

archive/issue_comments_062624.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T10:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62624",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017663.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-06T23:55:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7448#event-17663"
}
```



---

archive/issue_comments_062625.json:
```json
{
    "body": "Merged just trac_7448-nested_class_sphinx-fh.5.patch",
    "created_at": "2010-03-06T23:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62625",
    "user": "https://github.com/mwhansen"
}
```

Merged just trac_7448-nested_class_sphinx-fh.5.patch



---

archive/issue_comments_062626.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T23:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7448#issuecomment-62626",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
