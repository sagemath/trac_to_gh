# Issue 1708: missing docs in dmg sage install

Issue created by migration from https://trac.sagemath.org/ticket/1708

Original creator: was

Original creation time: 2008-01-07 09:02:56

Assignee: mabshoff


```
On Jan 6, 2008, at 22:08 , William Stein wrote:
> On Jan 6, 2008 9:52 PM, Justin C. Walker <> wrote:
>> On Jan 6, 2008, at 21:06 , William Stein wrote:
[snip]
>>> Options:
>>>    (1) Add the pure tex files into bdist, or
>>>    (2) Add all of doc-main to bdist (we include sage-main)
>>>    (3) Remove testing the tex files from "make check" for bdist.
>>>
>>> What do you guys think?  I like (2).
>>
>> It costs a mere 80MB or so, right?  How critical is that size
>> difference?
>>
>> I'd think it a good idea to include at least the primary doc set, or
>> maybe just the html set...
>
> The html documentation is included.  It is in SAGE_ROOT/doc/
>
> However, I think the tex files are not in there.

Neither the tex/pdf nor the html doc appear to be in the .dmg's I
downloaded.  'sage-bdist' certainly *looks* like it should copy it,
but there is no 'html' in $SAGE_ROOT.

Here's what I see:

$ ls
COPYING.txt             examples
matplotlibrc            test.log
README.txt              install.log
sage                    tmp
data                    ipython                 sage-2.9.1.txt
devel                   local                   sage-README-osx.txt
example.sage            makefile                spkg

$ find . -name html
./local/LIB/r/doc/html
./local/LIB/r/src/gnuwin32/fixed/html
./local/share/maxima/5.13.0/doc/html
./local/share/maxima/5.13.0/xmaxima/html
./local/share/moin/htdocs/applets/FCKeditor/_samples/html

Justin
```



---

Comment by was created at 2008-02-12 16:15:40

Resolution: duplicate


---

Comment by was created at 2008-02-12 16:15:40

This is a duplicate of #1539
