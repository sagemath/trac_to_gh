# Issue 3342: bizarre source code introspection output

archive/issues_003342.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @dandrake\n\nI observed the following in sage-3.0.2 on both Linux and OS X.\nNote the very bizarre output of x.is_zero??\n\n```\nsage: R.<x,y> = QQ[]; S.<x,y> = Frac(R)\nsage: x.is_zero??\nType:builtin_function_or_method\nBase Class:<type 'builtin_function_or_method'>\nString Form:<built-in method is_zero of FractionFieldElement object at 0x2afd954b16e0>\nNamespace:Interactive\nSource:\n    def is_zero(self):\n        \"\"\"\n        Return True if self equals self.parent()(0). The default\n        implementation is to fall back to 'not self.__nonzero__'.\n\n        NOTE: Do not re-implement this method in your subclass but\n        implement __nonzero__ instead.\n        \"\"\"\n        return not selfClass Docstring:\n    <attribute '__doc__' of 'builtin_function_or_method' objects>\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3342\n\n",
    "closed_at": "2010-07-27T02:30:23Z",
    "created_at": "2008-05-31T17:44:28Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "bizarre source code introspection output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3342",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

CC:  @dandrake

I observed the following in sage-3.0.2 on both Linux and OS X.
Note the very bizarre output of x.is_zero??

```
sage: R.<x,y> = QQ[]; S.<x,y> = Frac(R)
sage: x.is_zero??
Type:builtin_function_or_method
Base Class:<type 'builtin_function_or_method'>
String Form:<built-in method is_zero of FractionFieldElement object at 0x2afd954b16e0>
Namespace:Interactive
Source:
    def is_zero(self):
        """
        Return True if self equals self.parent()(0). The default
        implementation is to fall back to 'not self.__nonzero__'.

        NOTE: Do not re-implement this method in your subclass but
        implement __nonzero__ instead.
        """
        return not selfClass Docstring:
    <attribute '__doc__' of 'builtin_function_or_method' objects>

```

Issue created by migration from https://trac.sagemath.org/ticket/3342





---

archive/issue_comments_023157.json:
```json
{
    "body": "I'm not sure which part is bizarre -- maybe the lack of any white space or line break between \"return not self\" and \"Class Docstring\"?  As far as I can tell, this is an IPython issue.  If you change line 520 of OInspect.py (in SAGEROOT/local/lib/python/site-packages/IPython/) from \n\n```\n                    out.writeln(header('Class Docstring:\\n') +\n```\nto\n\n```\n                    out.writeln(header('\\n\\nClass Docstring:\\n') +\n```\nit fixes this problem.\n\nShould we patch the IPython to incorporate this change?  I've put a new spkg [here](http://sage.math.washington.edu/home/palmieri/SPKG/ipython-0.9.1.spkg), but I don't know if this is the right solution.",
    "created_at": "2009-06-10T21:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23157",
    "user": "https://github.com/jhpalmieri"
}
```

I'm not sure which part is bizarre -- maybe the lack of any white space or line break between "return not self" and "Class Docstring"?  As far as I can tell, this is an IPython issue.  If you change line 520 of OInspect.py (in SAGEROOT/local/lib/python/site-packages/IPython/) from 

```
                    out.writeln(header('Class Docstring:\n') +
```
to

```
                    out.writeln(header('\n\nClass Docstring:\n') +
```
it fixes this problem.

Should we patch the IPython to incorporate this change?  I've put a new spkg [here](http://sage.math.washington.edu/home/palmieri/SPKG/ipython-0.9.1.spkg), but I don't know if this is the right solution.



---

archive/issue_comments_023158.json:
```json
{
    "body": "By the way, there are similar problems with other docstrings and source code retrieval: type `GroupAlgebra??` or `SteenrodAlgebra??`.  The former yields lines looking like this:\n\n```\n        return GroupAlgebras(self.base_ring())\nConstructor information:\n```\n(not too bad, but there should be an extra blank line before \"Constructor information:\") while the latter gives\n\n```\n            return SteenrodAlgebra_generic(p=p, basis=basis_name)Call docstring:\n```\nThere should be two blank lines before \"Call docstring\".  \n\nThe new version of the spkg has a slight disadvantage: if you ask for docstrings, not source, in situations like these (`x.is_zero?`, `GroupAlgebra?`, `SteenrodAlgebra?`), then there are maybe two new blank lines between the main part of the docstring and \"Class docstring\", \"Constructor information\", or \"Call docstring\".  We could get rid of these with yet more tinkering, but I'm not sure it's worth it.\n\nWhen refereeing, the only new thing in the ipython spkg is the patch to OInspect.py.",
    "created_at": "2009-06-12T05:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23158",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, there are similar problems with other docstrings and source code retrieval: type `GroupAlgebra??` or `SteenrodAlgebra??`.  The former yields lines looking like this:

```
        return GroupAlgebras(self.base_ring())
Constructor information:
```
(not too bad, but there should be an extra blank line before "Constructor information:") while the latter gives

```
            return SteenrodAlgebra_generic(p=p, basis=basis_name)Call docstring:
```
There should be two blank lines before "Call docstring".  

The new version of the spkg has a slight disadvantage: if you ask for docstrings, not source, in situations like these (`x.is_zero?`, `GroupAlgebra?`, `SteenrodAlgebra?`), then there are maybe two new blank lines between the main part of the docstring and "Class docstring", "Constructor information", or "Call docstring".  We could get rid of these with yet more tinkering, but I'm not sure it's worth it.

When refereeing, the only new thing in the ipython spkg is the patch to OInspect.py.



---

archive/issue_comments_023159.json:
```json
{
    "body": "It looks like the new spkg is in fact at http://sage.math.washington.edu/home/palmieri/SPKG/ipython-0.9.1.p0.spkg rather than at the link given.\n\nAlso, independent from this ticket there is another 0.9.1.p0 spkg in sage-4.1, so these versions will have to be merged. I'll merge and review later today.",
    "created_at": "2009-07-16T09:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23159",
    "user": "https://github.com/wjp"
}
```

It looks like the new spkg is in fact at http://sage.math.washington.edu/home/palmieri/SPKG/ipython-0.9.1.p0.spkg rather than at the link given.

Also, independent from this ticket there is another 0.9.1.p0 spkg in sage-4.1, so these versions will have to be merged. I'll merge and review later today.



---

archive/issue_comments_023160.json:
```json
{
    "body": "I think this patch is not the right way to approach this. Maybe replacing the `write` in `out.write(header('Source:\\n')+source.rstrip())` by `writeln` is a cleaner approach. I'd feel a lot more confident about changing that if I would understand why some of the writes in the `pinfo` function use `write` while others use `writeln`, though...\n\nAnother thing is that this particular class docstring \"<attribute '__doc__' of 'builtin_function_or_method' objects>\" looks like a good candidate for inclusion in the \"Skip Python's auto-generated docstring\" list in that function, because it doesn't seem to add much (if any) useful information.\n(That seems to be caused by it being in a Cython class, which is probably why IPython doesn't already list it.)",
    "created_at": "2009-07-16T13:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23160",
    "user": "https://github.com/wjp"
}
```

I think this patch is not the right way to approach this. Maybe replacing the `write` in `out.write(header('Source:\n')+source.rstrip())` by `writeln` is a cleaner approach. I'd feel a lot more confident about changing that if I would understand why some of the writes in the `pinfo` function use `write` while others use `writeln`, though...

Another thing is that this particular class docstring "<attribute '__doc__' of 'builtin_function_or_method' objects>" looks like a good candidate for inclusion in the "Skip Python's auto-generated docstring" list in that function, because it doesn't seem to add much (if any) useful information.
(That seems to be caused by it being in a Cython class, which is probably why IPython doesn't already list it.)



---

archive/issue_comments_023161.json:
```json
{
    "body": "I did some more research:\n\nIn 'vanilla' IPython, the `<attribute '__doc__' of 'builtin_function_or_method' objects>` output is suppressed because `inspect.getdoc(object)` checks if `object.__doc__` is an instance of `types.StringTypes`.\n\nOur replacement `sage.misc.sageinspect.sage_getdoc` doesn't have this check. We can probably add it, but I'll (or someone else) will have to test that doesn't break introspection in other places such as the notebook.\n\n\nI also reported the missing whitespace between `Source` and `Class Docstring` upstream to the ipython developers.",
    "created_at": "2010-07-09T20:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23161",
    "user": "https://github.com/wjp"
}
```

I did some more research:

In 'vanilla' IPython, the `<attribute '__doc__' of 'builtin_function_or_method' objects>` output is suppressed because `inspect.getdoc(object)` checks if `object.__doc__` is an instance of `types.StringTypes`.

Our replacement `sage.misc.sageinspect.sage_getdoc` doesn't have this check. We can probably add it, but I'll (or someone else) will have to test that doesn't break introspection in other places such as the notebook.


I also reported the missing whitespace between `Source` and `Class Docstring` upstream to the ipython developers.



---

archive/issue_comments_023162.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-09T20:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23162",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023163.json:
```json
{
    "body": "I added a patch that adds the extra check I mentioned to `sage_getdoc`. It seems to work both on the command line and in the notebook.",
    "created_at": "2010-07-09T20:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23163",
    "user": "https://github.com/wjp"
}
```

I added a patch that adds the extra check I mentioned to `sage_getdoc`. It seems to work both on the command line and in the notebook.



---

archive/issue_comments_023164.json:
```json
{
    "body": "Attachment [trac_3342_builtin_introspection.patch](tarball://root/attachments/some-uuid/ticket3342/trac_3342_builtin_introspection.patch) by @wjp created at 2010-07-09 20:26:21",
    "created_at": "2010-07-09T20:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23164",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_3342_builtin_introspection.patch](tarball://root/attachments/some-uuid/ticket3342/trac_3342_builtin_introspection.patch) by @wjp created at 2010-07-09 20:26:21



---

archive/issue_comments_023165.json:
```json
{
    "body": "Small addendum: I failed to notice that the sagenb package has its own sage_getdoc, so it's not surprising this didn't break the notebook.",
    "created_at": "2010-07-09T20:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23165",
    "user": "https://github.com/wjp"
}
```

Small addendum: I failed to notice that the sagenb package has its own sage_getdoc, so it's not surprising this didn't break the notebook.



---

archive/issue_comments_023166.json:
```json
{
    "body": "the same change to duplicated code in sagenb",
    "created_at": "2010-07-09T20:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23166",
    "user": "https://github.com/wjp"
}
```

the same change to duplicated code in sagenb



---

archive/issue_comments_023167.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-10T02:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23167",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023168.json:
```json
{
    "body": "Attachment [sagenb_3342_builtin_introspection.patch](tarball://root/attachments/some-uuid/ticket3342/sagenb_3342_builtin_introspection.patch) by @jhpalmieri created at 2010-07-10 02:53:34\n\nIt looks okay and seems to behave well.  For some reason, I only see the original problem from the command line, not the notebook, so the sagenb patch may not strictly be needed; however, I think the two sageinspect files are supposed to synchronized as much as possible.\n\nI didn't know about `types.StringTypes` before; that looks useful.",
    "created_at": "2010-07-10T02:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23168",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [sagenb_3342_builtin_introspection.patch](tarball://root/attachments/some-uuid/ticket3342/sagenb_3342_builtin_introspection.patch) by @jhpalmieri created at 2010-07-10 02:53:34

It looks okay and seems to behave well.  For some reason, I only see the original problem from the command line, not the notebook, so the sagenb patch may not strictly be needed; however, I think the two sageinspect files are supposed to synchronized as much as possible.

I didn't know about `types.StringTypes` before; that looks useful.



---

archive/issue_comments_023169.json:
```json
{
    "body": "I've merged the sagenb repository patch into SageNB 0.8.2 at #9572.",
    "created_at": "2010-07-23T07:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23169",
    "user": "https://github.com/qed777"
}
```

I've merged the sagenb repository patch into SageNB 0.8.2 at #9572.



---

archive/issue_events_007489.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-27T02:30:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3342#event-7489"
}
```



---

archive/issue_comments_023170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-27T02:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23170",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_023171.json:
```json
{
    "body": "The remaining whitespace issue has just been fixed upstream in ipython by https://github.com/ipython/ipython/commit/ab3257a1428fa7e61a3f0b25d8410653ec42aa35",
    "created_at": "2011-03-22T16:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3342#issuecomment-23171",
    "user": "https://github.com/wjp"
}
```

The remaining whitespace issue has just been fixed upstream in ipython by https://github.com/ipython/ipython/commit/ab3257a1428fa7e61a3f0b25d8410653ec42aa35
