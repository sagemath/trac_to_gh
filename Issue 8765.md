# Issue 8765: Huffman Encoding

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-04-25 10:03:59

Assignee: wdj

CC:  wdj mvngu leif

This is a basic implementation of Huffman's encoding. May it be useful to teach ! :-)

Nathann


---

Comment by leif created at 2010-04-25 11:22:36

Much room for extensions, e.g.: ;-)

 * accept (also) list of symbols of arbitrary alphabet
  (type should be checked anyway)
 * binary file (stream) I/O..., with or without encoding table
 * *generate* encoding/decoding functions

There's actually a possible application within Sage itself: compression of prime_pi and nth_prime tables. (The table-based functions are still work in progress.)

OT:
 - I could perhaps contribute FAX G3 en/decoding, too, if I'm able to find my dead old implementation... :)
 - Another nice thing is encoding and decoding of machine instructions (assembling, disassembling).

-Leif


---

Comment by ncohen created at 2010-04-25 11:24:27

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-04-25 11:26:07

To think I just needed a function for Huffmann encoding yesterday to test something.. Sounds like this file will soon be out of my reach :-D

Nathann


---

Comment by leif created at 2010-04-25 12:03:58

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-04-25 12:03:58

Replying to [comment:3 ncohen]:
Haven't tested yet, but there are at least some typos.
(I could fix them, but most probably not today.)

I'd also add [more] type checks on the inputs.


---

Comment by ylchapuy created at 2010-04-27 09:47:55

Hi, I only had a very quick look and I'm a bit concerned about where to put this code in the library.

`sage.coding` is about channel coding (error correcting code) but this ticket is about source coding (data compression) and I think it's a bad idea to mix those in the library and in the doc.

I would feel a lot more confortable with `sage.coding.source_coding.huffman`.

     Yann


---

Comment by ncohen created at 2010-04-27 09:56:15

Changing status from needs_work to needs_info.


---

Comment by ncohen created at 2010-04-27 09:56:15

Sounds sensible enough ! I just moved the file in a source_coding subdirectory, but I can not import sage.coding.source_coding.huffman, as sage does not find the source_coding module... Where should I tell it it exists ? :-)

Nathann


---

Comment by wdj created at 2010-04-27 18:52:17

Replying to [comment:7 ncohen]:
> Sounds sensible enough ! I just moved the file in a source_coding subdirectory, but I can not import sage.coding.source_coding.huffman, as sage does not find the source_coding module... Where should I tell it it exists ? :-)
> 
> Nathann

Maybe you could try to add an (empty) __init__.py file to it before adding huffman.py?


---

Comment by ncohen created at 2010-04-28 07:36:26

Hmmm... I added this empty __init__.py file in source_coding/, but it made no difference... Is that what you meant ? :-/

Nathann


---

Comment by mvngu created at 2010-04-28 07:40:29

Replying to [comment:9 ncohen]:
> Hmmm... I added this empty __init__.py file in source_coding/, but it made no difference... Is that what you meant ? :-/

Try putting a comment in that `__init__.py` file. For example, the content of that init file might be:

```
# Just a comment so that __init__.py is not an empty file.
```



---

Comment by ncohen created at 2010-04-28 07:46:32

I just tried it (you were right, the file I created was empty), but noticed no difference... In the end, is it really worth creating a directory anyway ? I could just rename the file to source_coding.py and let this Huffman class stay inside ?..

But I still would like to understand how to get this directory detected :-/

anything to do in modules_list.py even though it is not a Cython file ? 

Nathann


---

Comment by ncohen created at 2010-04-28 08:16:30

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2010-04-28 08:16:30

What about this version (no directory, but a file source_coding.py ) ? :-)


---

Comment by wdj created at 2010-04-29 14:21:32

This applies to 4.4.rc0 fine and passes sage -testall.
I have not checked if the documentation builds okay.
Are the other reviewers satisfied with the changes in this last patch?


---

Comment by leif created at 2010-04-29 15:20:07

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-04-29 15:20:07

Replying to [comment:13 wdj]:
> This applies to 4.4.rc0 fine and passes sage -testall.
> I have not checked if the documentation builds okay.
We _should_ do that before giving a positive review, I guess... :)

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
  It's not tested if *both* `string` and `frequencies` are given (=> error).

And as I said before I'd prefer type checks on the parameters (rather than relying on _automatically_ raised exceptions later in the code).

I also prefer having the return type documented at the top rather than (more or less) implicitly in the examples (e.g. in `frequency_table()`; `tree()` actually returns a `DiGraph` which happens to also be a tree.)


Doctests?

(Still haven't tested the code, just read the patches, sorry.)

-Leif


---

Comment by ncohen created at 2010-04-30 07:56:59

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-04-30 07:56:59

Updated ! :-)

Nathann


---

Attachment

`from operator import xor`... ;-)

I'll test it this evening.


---

Attachment

new module sage.coding.source_coding.huffman


---

Comment by mvngu created at 2010-05-02 07:54:47

The patch [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch) replaces the earlier one [trac_8765.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765.patch). Now the Huffman module is in the directory `source_coding/`. Nothing has changed in the replacement patch, except for changes to get Sage to recognize this new module.


---

Comment by leif created at 2010-05-02 09:52:13

Replying to [comment:17 mvngu]:
I guess `frequency_table` should be imported in `all.py` as well.

Have to clone again and import the new patch... ;-)

-Leif


---

Attachment

Changes in the reviewer patch include:

 1. Add substantially more documentation to the module.
 1. Clean-ups in accordance with [PEP 008](http://www.python.org/dev/peps/pep-0008/).
 1. Don't use the module `string` nor its `join` function. These have been deprecated. You should now use `str` and the function `"".join`.
 1. Get the whole module to 100% coverage.

This means I have reviewed [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch), so only my patch needs review by anyone but me.


---

Comment by leif created at 2010-05-02 19:15:35

Replying to [comment:19 mvngu]:
> This means I have reviewed [trac_8765-huffman.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8765/trac_8765-huffman.patch), so only my patch needs review by anyone but me.

That patch looks *very* good.
(I wished all module documentations had that quality.)

I'll only add some more doctests and perhaps edit some comments.

I think improvements to the algorithm can be done on another ticket.

-Leif


---

Comment by ncohen created at 2010-05-09 16:41:43

The only reason why I still read your patches, apply them, check they are correct, check the docstrings, build the documentation and read it, is that I fear some God may be watching over my shoulder.

Another perfect patch from Minh :-D

Thank you very much !

Nathann


---

Comment by ncohen created at 2010-05-09 16:41:43

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 08:24:27

Resolution: fixed
