# Issue 9991: Python scripts try to run before Python is built.

archive/issues_009991.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jhpalmieri\n\nAs discussed [here](http://groups.google.com/group/sage-devel/browse_thread/thread/9788a6ad6fe03ab9), the Python script `$SAGE_ROOT/spkg/base/sage-make_relative` is run before Python is built in Sage. On a system that do not have Python installed (like a fresh install of IBM's AIX operating system),  this generates an error message message as this script is run. \n\n\n```\nMaking Sage/Python scripts relocatable...\npython: No such file or directory \n```\n\n\nThis could be quite worrying, to find that an important program like Python is missing.\n\nThe bottom of the file `$SAGE_ROOT/spkg/base/sage-spkg` has this:\n\n\n```\necho \"Making Sage/Python scripts relocatable...\"\n\ncd \"$SAGE_LOCAL\"/bin\n./sage-make_relative\n\necho \"Finished installing $PKG_NAME.spkg\" \n\n# It's OK if the above fails -- in fact it will until Python\n# itself gets installed. That's fine. \nexit 0   \n```\n\n\nwhich indicates a failure of {{{sage-make_relative\n}}} is unimportant. But still it is annoying and led me to believe there was a more serious bug. \n\nIt does not seem appropriate to let {{{sage-make_relative\n}}} fail, but it would be much better if {{{sage-make_relative\n}}} can be removed, and its functionality moved to the script that calls it, which is `$SAGE_ROOT/spkg/base/sage-spkg`\n\nI've attached a copy of `$SAGE_ROOT/spkg/base/sage-make_relative`, which I believe could be written much better. I'm attaching it, since I will want to create an external link to this file. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9992\n\n",
    "created_at": "2010-09-23T23:24:10Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "Python scripts try to run before Python is built.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9991",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jhpalmieri

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

Issue created by migration from https://trac.sagemath.org/ticket/9992





---

archive/issue_comments_100238.json:
```json
{
    "body": "Attachment [sage-make_relative](tarball://root/attachments/some-uuid/ticket9992/sage-make_relative) by drkirkby created at 2010-09-23 23:28:27\n\nAttached only so I can provide a link to this - for most practical purposes this can be ignored.",
    "created_at": "2010-09-23T23:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100238",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sage-make_relative](tarball://root/attachments/some-uuid/ticket9992/sage-make_relative) by drkirkby created at 2010-09-23 23:28:27

Attached only so I can provide a link to this - for most practical purposes this can be ignored.



---

archive/issue_comments_100239.json:
```json
{
    "body": "Well, perhaps one should simply suppress (or avoid) the error message in case no Python is (yet) installed, but the script is really odd.\n\n* It should only test (and modify) scripts that are executable.\n* It \"rewrites\" **every** file that contains `python` and `#!` in its first line, so even already correct (and already modified) files starting with\n  {{{#!/usr/bin/env python\n}}}\n   will get rewritten.\n* It makes all these files writable (but only for the owner).\n\nI don't agree moving its functionality into `sage-spkg` is a good idea. (IIRC it is called by other scripts as well, and `sage-spkg` shouldn't be blown up too much.)",
    "created_at": "2010-09-24T02:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100239",
    "user": "https://github.com/nexttime"
}
```

Well, perhaps one should simply suppress (or avoid) the error message in case no Python is (yet) installed, but the script is really odd.

* It should only test (and modify) scripts that are executable.
* It "rewrites" **every** file that contains `python` and `#!` in its first line, so even already correct (and already modified) files starting with
  {{{#!/usr/bin/env python
}}}
   will get rewritten.
* It makes all these files writable (but only for the owner).

I don't agree moving its functionality into `sage-spkg` is a good idea. (IIRC it is called by other scripts as well, and `sage-spkg` shouldn't be blown up too much.)



---

archive/issue_comments_100240.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> Well, perhaps one should simply suppress (or avoid) the error message in case no Python is (yet) installed, but the script is really odd.\n\nOr just not check if python is not run. \n\n>  * It should only test (and modify) scripts that are executable.\n\nYes. At the minute it tests binaries too. \n\n>  * It \"rewrites\" **every** file that contains `python` and `#!` in its first line, so even already correct (and already modified) files starting with\n>    {{{\n> #!/usr/bin/env python\n> }}}\n>    will get rewritten.\n\nThat's not such a big deal. \n\n>  * It makes all these files writable (but only for the owner).\n\n\n \n> I don't agree moving its functionality into `sage-spkg` is a good idea. (IIRC it is called by other scripts as well, and `sage-spkg` shouldn't be blown up too much.)\n\nOK, well this is easy to fix by putting an \n\nif [ -f '$SAGE_LOCAL/bin/python\" ] ; then\n   # Run the python script. \nfi\n\nI'll leave you to modify the python script if you want to.",
    "created_at": "2010-09-24T04:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100240",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:1 leif]:
> Well, perhaps one should simply suppress (or avoid) the error message in case no Python is (yet) installed, but the script is really odd.

Or just not check if python is not run. 

>  * It should only test (and modify) scripts that are executable.

Yes. At the minute it tests binaries too. 

>  * It "rewrites" **every** file that contains `python` and `#!` in its first line, so even already correct (and already modified) files starting with
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

archive/issue_comments_100241.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n> Replying to [comment:1 leif]:\n> >  * It \"rewrites\" **every** file that contains `python` and `#!` in its first line [...]\n> That's not such a big deal.\n\nI think it should skip files matching `sage-*` and those whose first line already starts with `#!/usr/bin/env ...`.\n\n> > I don't agree moving its functionality into `sage-spkg` is a good idea. (IIRC it is called by other scripts as well, and `sage-spkg` shouldn't be blown up too much.)\n> \n> OK, well this is easy to fix by putting an \n\n```sh\nif [ -f '$SAGE_LOCAL/bin/python\" ] ; then\n    # Run the python script. \nfi\n```\n\n\nThat's an improvement, though it is not clear if we in the near future make Python a prerequisite (or intentionally use a system Python for such if one is present).\n\n> I'll leave you to modify the python script if you want to. \n\nI thought you were going to rewrite it as a shell script (which could as well be called from `sage-spkg`).",
    "created_at": "2010-09-24T11:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100241",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:3 drkirkby]:
> Replying to [comment:1 leif]:
> >  * It "rewrites" **every** file that contains `python` and `#!` in its first line [...]
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

archive/issue_comments_100242.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> Replying to [comment:3 drkirkby]:\n\n> > OK, well this is easy to fix by putting an \n> {{{\n> #!sh\n> if [ -f '$SAGE_LOCAL/bin/python\" ] ; then\n>     # Run the python script. \n> fi\n> }}}\n> \n> That's an improvement, though it is not clear if we in the near future make Python a prerequisite (or intentionally use a system Python for such if one is present).\n\nI hope we don't. \n* We rely on someone's Python working right. It was a failure of Python on William's machine which cased a headache recently with `sage_fortran`. Though he had Python, his version was not working in a way necessary to perform the task it was asked to do. That's why he was the only one to see the bug - not everyone else. \n\n* It would be even harder to justify shipping a large tarfile to maintainers of Debian or similar when we say Python is a prequiste, but also we include the Python source. I think that gets a bit silly. \n\n* On platforms like AIX, or the smaller cut-down Linux distributions, they may well not include Python. Some have tried building Sage on a mobile phone. I doubt that is as practical if we make Python a prerequisite and still ship the source code. \n\n> > I'll leave you to modify the python script if you want to. \n> \n> I thought you were going to rewrite it as a shell script (which could as well be called from `sage-spkg`).\n\nNo, I think it will be easier to leave it untouched, but only call it if `$SAGE_ROOT/local/bin/python` exists. The script appears to work and if it is called from multiple places, I'd have to duplicate its functionality accurately - even though I think they are a bit dumb. \n\nDave",
    "created_at": "2010-09-24T12:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100242",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_100243.json:
```json
{
    "body": "Attachment [trac_9992-run_sage-make_relative_conditionally.scripts.patch](tarball://root/attachments/some-uuid/ticket9992/trac_9992-run_sage-make_relative_conditionally.scripts.patch) by @nexttime created at 2011-10-13 12:04:14\n\nSCRIPTS repo. Changes `sage-spkg` to only run `sage-make_relative` if Sage's Python is already installed. Based on Sage 4.7.2.alpha4.",
    "created_at": "2011-10-13T12:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100243",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_9992-run_sage-make_relative_conditionally.scripts.patch](tarball://root/attachments/some-uuid/ticket9992/trac_9992-run_sage-make_relative_conditionally.scripts.patch) by @nexttime created at 2011-10-13 12:04:14

SCRIPTS repo. Changes `sage-spkg` to only run `sage-make_relative` if Sage's Python is already installed. Based on Sage 4.7.2.alpha4.



---

archive/issue_comments_100244.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-13T12:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100244",
    "user": "https://github.com/nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100245.json:
```json
{
    "body": "Attached patch only runs `sage-make_relative` if **Sage's** Python is installed (which Dave wanted).\n\nIf we want to allow other `python`s as well, we'd have to change it to e.g.\n\n```sh\nif command -v python >/dev/null; then\n    ...\n```\n\n\nI've left the `exit 0` at the end (which is in principle superfluous since `echo` is unlikely to fail), as it clarifies that this part is (hopefully ;-) ) only reached if no errors occurred previously.",
    "created_at": "2011-10-13T12:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100245",
    "user": "https://github.com/nexttime"
}
```

Attached patch only runs `sage-make_relative` if **Sage's** Python is installed (which Dave wanted).

If we want to allow other `python`s as well, we'd have to change it to e.g.

```sh
if command -v python >/dev/null; then
    ...
```


I've left the `exit 0` at the end (which is in principle superfluous since `echo` is unlikely to fail), as it clarifies that this part is (hopefully ;-) ) only reached if no errors occurred previously.



---

archive/issue_comments_100246.json:
```json
{
    "body": "Changing keywords from \"\" to \"sage-make_relative sage-spkg\".",
    "created_at": "2011-10-13T12:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100246",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "sage-make_relative sage-spkg".



---

archive/issue_comments_100247.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-14T20:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100247",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_100248.json:
```json
{
    "body": "The code makes sense and it works: I applied that patch and made a new source distribution.  When building that from scratch, the first 50 or so spkgs didn't run sage-make_relative.  Once the python spkg was installed, they did run it.\n\nI also tried after temporarily getting rid of my system's python.  Installing before the patch yields a possibly confusing error message (before the python spkg is installed, anyway), and after the patch there is no such error message.",
    "created_at": "2011-10-14T20:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100248",
    "user": "https://github.com/jhpalmieri"
}
```

The code makes sense and it works: I applied that patch and made a new source distribution.  When building that from scratch, the first 50 or so spkgs didn't run sage-make_relative.  Once the python spkg was installed, they did run it.

I also tried after temporarily getting rid of my system's python.  Installing before the patch yields a possibly confusing error message (before the python spkg is installed, anyway), and after the patch there is no such error message.



---

archive/issue_comments_100249.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-19T18:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100249",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_100250.json:
```json
{
    "body": "Milestone sage-4.7.3 deleted",
    "created_at": "2011-11-03T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9991#issuecomment-100250",
    "user": "https://github.com/jdemeyer"
}
```

Milestone sage-4.7.3 deleted
