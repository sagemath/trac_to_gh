# Issue 8765: Huffman Encoding

archive/issues_008765.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nCC:  @wdjoyner mvngu @nexttime\n\nThis is a basic implementation of Huffman's encoding. May it be useful to teach ! :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8765\n\n",
    "created_at": "2010-04-25T10:03:59Z",
    "labels": [
        "component: coding theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Huffman Encoding",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8765",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @wdjoyner

CC:  @wdjoyner mvngu @nexttime

This is a basic implementation of Huffman's encoding. May it be useful to teach ! :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8765





---

archive/issue_comments_080066.json:
```json
{
    "body": "Much room for extensions, e.g.: ;-)\n\n* accept (also) list of symbols of arbitrary alphabet\n  (type should be checked anyway)\n* binary file (stream) I/O..., with or without encoding table\n* **generate** encoding/decoding functions\n\nThere's actually a possible application within Sage itself: compression of prime_pi and nth_prime tables. (The table-based functions are still work in progress.)\n\nOT:\n- I could perhaps contribute FAX G3 en/decoding, too, if I'm able to find my dead old implementation... :)\n- Another nice thing is encoding and decoding of machine instructions (assembling, disassembling).\n\n-Leif",
    "created_at": "2010-04-25T11:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80066",
    "user": "https://github.com/nexttime"
}
```

Much room for extensions, e.g.: ;-)

* accept (also) list of symbols of arbitrary alphabet
  (type should be checked anyway)
* binary file (stream) I/O..., with or without encoding table
* **generate** encoding/decoding functions

There's actually a possible application within Sage itself: compression of prime_pi and nth_prime tables. (The table-based functions are still work in progress.)

OT:
- I could perhaps contribute FAX G3 en/decoding, too, if I'm able to find my dead old implementation... :)
- Another nice thing is encoding and decoding of machine instructions (assembling, disassembling).

-Leif



---

archive/issue_comments_080067.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-25T11:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80067",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080068.json:
```json
{
    "body": "To think I just needed a function for Huffmann encoding yesterday to test something.. Sounds like this file will soon be out of my reach :-D\n\nNathann",
    "created_at": "2010-04-25T11:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80068",
    "user": "https://github.com/nathanncohen"
}
```

To think I just needed a function for Huffmann encoding yesterday to test something.. Sounds like this file will soon be out of my reach :-D

Nathann



---

archive/issue_comments_080069.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-25T12:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80069",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080070.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\nHaven't tested yet, but there are at least some typos.\n(I could fix them, but most probably not today.)\n\nI'd also add [more] type checks on the inputs.",
    "created_at": "2010-04-25T12:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80070",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:3 ncohen]:
Haven't tested yet, but there are at least some typos.
(I could fix them, but most probably not today.)

I'd also add [more] type checks on the inputs.



---

archive/issue_comments_080071.json:
```json
{
    "body": "Hi, I only had a very quick look and I'm a bit concerned about where to put this code in the library.\n\n`sage.coding` is about channel coding (error correcting code) but this ticket is about source coding (data compression) and I think it's a bad idea to mix those in the library and in the doc.\n\nI would feel a lot more confortable with `sage.coding.source_coding.huffman`.\n\n     Yann",
    "created_at": "2010-04-27T09:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80071",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Hi, I only had a very quick look and I'm a bit concerned about where to put this code in the library.

`sage.coding` is about channel coding (error correcting code) but this ticket is about source coding (data compression) and I think it's a bad idea to mix those in the library and in the doc.

I would feel a lot more confortable with `sage.coding.source_coding.huffman`.

     Yann



---

archive/issue_comments_080072.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-04-27T09:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80072",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_080073.json:
```json
{
    "body": "Sounds sensible enough ! I just moved the file in a source_coding subdirectory, but I can not import sage.coding.source_coding.huffman, as sage does not find the source_coding module... Where should I tell it it exists ? :-)\n\nNathann",
    "created_at": "2010-04-27T09:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80073",
    "user": "https://github.com/nathanncohen"
}
```

Sounds sensible enough ! I just moved the file in a source_coding subdirectory, but I can not import sage.coding.source_coding.huffman, as sage does not find the source_coding module... Where should I tell it it exists ? :-)

Nathann



---

archive/issue_comments_080074.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> Sounds sensible enough ! I just moved the file in a source_coding subdirectory, but I can not import sage.coding.source_coding.huffman, as sage does not find the source_coding module... Where should I tell it it exists ? :-)\n> \n> Nathann\n\nMaybe you could try to add an (empty) __init__.py file to it before adding huffman.py?",
    "created_at": "2010-04-27T18:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80074",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:7 ncohen]:
> Sounds sensible enough ! I just moved the file in a source_coding subdirectory, but I can not import sage.coding.source_coding.huffman, as sage does not find the source_coding module... Where should I tell it it exists ? :-)
> 
> Nathann

Maybe you could try to add an (empty) __init__.py file to it before adding huffman.py?



---

archive/issue_comments_080075.json:
```json
{
    "body": "Hmmm... I added this empty __init__.py file in source_coding/, but it made no difference... Is that what you meant ? :-/\n\nNathann",
    "created_at": "2010-04-28T07:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80075",
    "user": "https://github.com/nathanncohen"
}
```

Hmmm... I added this empty __init__.py file in source_coding/, but it made no difference... Is that what you meant ? :-/

Nathann



---

archive/issue_comments_080076.json:
```json
{
    "body": "Replying to [comment:9 ncohen]:\n> Hmmm... I added this empty __init__.py file in source_coding/, but it made no difference... Is that what you meant ? :-/\n\nTry putting a comment in that `__init__.py` file. For example, the content of that init file might be:\n\n```\n# Just a comment so that __init__.py is not an empty file.\n```\n",
    "created_at": "2010-04-28T07:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:9 ncohen]:
> Hmmm... I added this empty __init__.py file in source_coding/, but it made no difference... Is that what you meant ? :-/

Try putting a comment in that `__init__.py` file. For example, the content of that init file might be:

```
# Just a comment so that __init__.py is not an empty file.
```




---

archive/issue_comments_080077.json:
```json
{
    "body": "I just tried it (you were right, the file I created was empty), but noticed no difference... In the end, is it really worth creating a directory anyway ? I could just rename the file to source_coding.py and let this Huffman class stay inside ?..\n\nBut I still would like to understand how to get this directory detected :-/\n\nanything to do in modules_list.py even though it is not a Cython file ? \n\nNathann",
    "created_at": "2010-04-28T07:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80077",
    "user": "https://github.com/nathanncohen"
}
```

I just tried it (you were right, the file I created was empty), but noticed no difference... In the end, is it really worth creating a directory anyway ? I could just rename the file to source_coding.py and let this Huffman class stay inside ?..

But I still would like to understand how to get this directory detected :-/

anything to do in modules_list.py even though it is not a Cython file ? 

Nathann



---

archive/issue_comments_080078.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-04-28T08:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80078",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_080079.json:
```json
{
    "body": "What about this version (no directory, but a file source_coding.py ) ? :-)",
    "created_at": "2010-04-28T08:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80079",
    "user": "https://github.com/nathanncohen"
}
```

What about this version (no directory, but a file source_coding.py ) ? :-)



---

archive/issue_comments_080080.json:
```json
{
    "body": "This applies to 4.4.rc0 fine and passes sage -testall.\nI have not checked if the documentation builds okay.\nAre the other reviewers satisfied with the changes in this last patch?",
    "created_at": "2010-04-29T14:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80080",
    "user": "https://github.com/wdjoyner"
}
```

This applies to 4.4.rc0 fine and passes sage -testall.
I have not checked if the documentation builds okay.
Are the other reviewers satisfied with the changes in this last patch?



---

archive/issue_comments_080081.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-29T15:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80081",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080082.json:
```json
{
    "body": "Replying to [comment:13 wdj]:\n> This applies to 4.4.rc0 fine and passes sage -testall.\n> I have not checked if the documentation builds okay.\nWe *should* do that before giving a positive review, I guess... :)\n\n> Are the other reviewers satisfied with the changes in this last patch?\nThere are still typos in the description:\n\n* s/occurence/occurrence/\n* s/frquency/frequency/\n* s/its its/its/ (two times)\n* s/occurencies/occurrences/ (two times)\n* s/eah/each/\n\n`encoding_table()`:\n  s/each letter/each trained letter/\n\n`__init__`:\n  It's not tested if **both** `string` and `frequencies` are given (=> error).\n\nAnd as I said before I'd prefer type checks on the parameters (rather than relying on *automatically* raised exceptions later in the code).\n\nI also prefer having the return type documented at the top rather than (more or less) implicitly in the examples (e.g. in `frequency_table()`; `tree()` actually returns a `DiGraph` which happens to also be a tree.)\n\n\nDoctests?\n\n(Still haven't tested the code, just read the patches, sorry.)\n\n-Leif",
    "created_at": "2010-04-29T15:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80082",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:13 wdj]:
> This applies to 4.4.rc0 fine and passes sage -testall.
> I have not checked if the documentation builds okay.
We *should* do that before giving a positive review, I guess... :)

> Are the other reviewers satisfied with the changes in this last patch?
There are still typos in the description:

* s/occurence/occurrence/
* s/frquency/frequency/
* s/its its/its/ (two times)
* s/occurencies/occurrences/ (two times)
* s/eah/each/

`encoding_table()`:
  s/each letter/each trained letter/

`__init__`:
  It's not tested if **both** `string` and `frequencies` are given (=> error).

And as I said before I'd prefer type checks on the parameters (rather than relying on *automatically* raised exceptions later in the code).

I also prefer having the return type documented at the top rather than (more or less) implicitly in the examples (e.g. in `frequency_table()`; `tree()` actually returns a `DiGraph` which happens to also be a tree.)


Doctests?

(Still haven't tested the code, just read the patches, sorry.)

-Leif



---

archive/issue_comments_080083.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-30T07:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80083",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080084.json:
```json
{
    "body": "Updated ! :-)\n\nNathann",
    "created_at": "2010-04-30T07:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80084",
    "user": "https://github.com/nathanncohen"
}
```

Updated ! :-)

Nathann



---

archive/issue_comments_080085.json:
```json
{
    "body": "Attachment [trac_8765.patch](tarball://root/attachments/some-uuid/ticket8765/trac_8765.patch) by @nexttime created at 2010-04-30 10:33:31\n\n`from operator import xor`... ;-)\n\nI'll test it this evening.",
    "created_at": "2010-04-30T10:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80085",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8765.patch](tarball://root/attachments/some-uuid/ticket8765/trac_8765.patch) by @nexttime created at 2010-04-30 10:33:31

`from operator import xor`... ;-)

I'll test it this evening.



---

archive/issue_comments_080086.json:
```json
{
    "body": "Attachment [trac_8765-huffman.patch](tarball://root/attachments/some-uuid/ticket8765/trac_8765-huffman.patch) by mvngu created at 2010-05-02 07:51:26\n\nnew module sage.coding.source_coding.huffman",
    "created_at": "2010-05-02T07:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8765-huffman.patch](tarball://root/attachments/some-uuid/ticket8765/trac_8765-huffman.patch) by mvngu created at 2010-05-02 07:51:26

new module sage.coding.source_coding.huffman



---

archive/issue_comments_080087.json:
```json
{
    "body": "The patch [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch) replaces the earlier one [trac_8765.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765.patch). Now the Huffman module is in the directory `source_coding/`. Nothing has changed in the replacement patch, except for changes to get Sage to recognize this new module.",
    "created_at": "2010-05-02T07:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch) replaces the earlier one [trac_8765.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765.patch). Now the Huffman module is in the directory `source_coding/`. Nothing has changed in the replacement patch, except for changes to get Sage to recognize this new module.



---

archive/issue_comments_080088.json:
```json
{
    "body": "Replying to [comment:17 mvngu]:\nI guess `frequency_table` should be imported in `all.py` as well.\n\nHave to clone again and import the new patch... ;-)\n\n-Leif",
    "created_at": "2010-05-02T09:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80088",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:17 mvngu]:
I guess `frequency_table` should be imported in `all.py` as well.

Have to clone again and import the new patch... ;-)

-Leif



---

archive/issue_comments_080089.json:
```json
{
    "body": "Attachment [trac_8765-clean-ups.patch](tarball://root/attachments/some-uuid/ticket8765/trac_8765-clean-ups.patch) by mvngu created at 2010-05-02 17:25:09\n\nChanges in the reviewer patch include:\n\n1. Add substantially more documentation to the module.\n2. Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/).\n3. Don't use the module `string` nor its `join` function. These have been deprecated. You should now use `str` and the function `\"\".join`.\n4. Get the whole module to 100% coverage.\n\nThis means I have reviewed [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch), so only my patch needs review by anyone but me.",
    "created_at": "2010-05-02T17:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80089",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8765-clean-ups.patch](tarball://root/attachments/some-uuid/ticket8765/trac_8765-clean-ups.patch) by mvngu created at 2010-05-02 17:25:09

Changes in the reviewer patch include:

1. Add substantially more documentation to the module.
2. Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/).
3. Don't use the module `string` nor its `join` function. These have been deprecated. You should now use `str` and the function `"".join`.
4. Get the whole module to 100% coverage.

This means I have reviewed [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch), so only my patch needs review by anyone but me.



---

archive/issue_comments_080090.json:
```json
{
    "body": "Replying to [comment:19 mvngu]:\n> This means I have reviewed [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch), so only my patch needs review by anyone but me.\n\nThat patch looks **very** good.\n(I wished all module documentations had that quality.)\n\nI'll only add some more doctests and perhaps edit some comments.\n\nI think improvements to the algorithm can be done on another ticket.\n\n-Leif",
    "created_at": "2010-05-02T19:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80090",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:19 mvngu]:
> This means I have reviewed [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch), so only my patch needs review by anyone but me.

That patch looks **very** good.
(I wished all module documentations had that quality.)

I'll only add some more doctests and perhaps edit some comments.

I think improvements to the algorithm can be done on another ticket.

-Leif



---

archive/issue_comments_080091.json:
```json
{
    "body": "The only reason why I still read your patches, apply them, check they are correct, check the docstrings, build the documentation and read it, is that I fear some God may be watching over my shoulder.\n\nAnother perfect patch from Minh :-D\n\nThank you very much !\n\nNathann",
    "created_at": "2010-05-09T16:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80091",
    "user": "https://github.com/nathanncohen"
}
```

The only reason why I still read your patches, apply them, check they are correct, check the docstrings, build the documentation and read it, is that I fear some God may be watching over my shoulder.

Another perfect patch from Minh :-D

Thank you very much !

Nathann



---

archive/issue_comments_080092.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-09T16:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80092",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8765#issuecomment-80093",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
