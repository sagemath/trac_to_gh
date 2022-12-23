# Issue 9275: 2 Bugs related to Simple Sage Server API

Issue created by migration from https://trac.sagemath.org/ticket/9275

Original creator: was

Original creation time: 2010-06-19 18:16:11

Assignee: jason, was

This is from a user:


```

Hi.

I was recently trying to use the Simple Sage Server API as described here:
http://www.sagemath.org/doc/reference/sagenb/simple/twist.html
I am using the opensuse-64bit build of Sage-4.4.

Well it didn't work (always got an error when I tried to compute
something), so I started to follow the error.

On my way I found to Bugs:

File sage.server.notebook.worksheet, Line 3497, in def preparse(self, s)
replace:   s = preparse_file(s, magic=False, do_time=True,
ignore_prompts=False)
with   :   s = preparse_file(s)
(The arguments magic and do_time do not exist in preparse_file)

File sage.server.notebook.worksheet, Line 2871, in def
start_next_comp(self) before:    input +=
'sage.server.notebook.interact.SAGE_CELL_ID=%s\n'%(C.id())
insert:    input += 'import sage.server.notebook.interact\n'
(You need to import the module before using it)

When I applied those two patches the tutorial worked out for me.

greetings,
David Poetzsch-Heffter
```



---

Comment by dpoetzsch created at 2010-06-24 10:37:26

The bugfixes mentioned above as a patch file


---

Comment by kcrisman created at 2013-06-14 17:11:40

Changing status from new to needs_review.


---

Attachment

The simple server does not currently work at all; however, the [Sage cell server](https://github.com/sagemath/sagecell) should fit most of those needs.


---

Comment by kcrisman created at 2013-06-14 17:11:52

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-06-14 18:36:50

Changing status from positive_review to needs_info.


---

Comment by kcrisman created at 2014-09-17 02:36:23

Changing status from needs_info to positive_review.


---

Comment by vbraun created at 2014-09-18 18:01:30

Resolution: wontfix
