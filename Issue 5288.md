# Issue 5288: cython gray code iterator for k-combinations of a set

Issue created by migration from Trac.

Original creator: dgordon

Original creation time: 2009-02-16 16:52:18

Assignee: mhansen

CC:  sage-combinat

The default iterator for k-combinations of a set in combination.py is too slow for some applications, such as the `is_covering()` function in ticket #4859.  This code defines a new class, which uses an efficient cython implementation of Chase's gray code sequence.

There is currently a discussion going on in [http://groups.google.com/group/sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel) about the right way to implement combinatorial classes with different iterators.  Once a method has been decided on, code can be added to make this patch conform to it.


---

Attachment

Hi Dan,

any ticket in trac should result in an indicator for the ticket that there is a patch together with its current review status. In this case it seems to be not ready for review.

This makes it much easier to find tickets with patches for example. 

Cheers,

Michael


---

Comment by ppurka created at 2011-11-21 09:46:41

I think this patch should get merged, whether or not the generic iterator gets written. It's already been three years since this patch was submitted. `combinations()` in Sage-4.7.2 is pretty broken and gives arcane errors. For example like this:

```
sage: combinations([vector([1,1]), vector([2,2]), vector([3,3])], 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_81.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("Y29tYmluYXRpb25zKFt2ZWN0b3IoWzEsMV0pLCB2ZWN0b3IoWzIsMl0pLCB2ZWN0b3IoWzMsM10pXSwgMik="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpNUZznv/___code___.py", line 3, in <module>
    exec compile(u'combinations([vector([_sage_const_1 ,_sage_const_1 ]), vector([_sage_const_2 ,_sage_const_2 ]), vector([_sage_const_3 ,_sage_const_3 ])], _sage_const_2 )
  File "", line 1, in <module>
    
  File "/home/punarbasu/Installations/sage-4.7.2/local/lib/python2.6/site-packages/sage/combinat/combinat.py", line 2016, in combinations
    ans=gap.eval("Combinations(%s,%s)"%(mset,ZZ(k))).replace("\n","")
  File "/home/punarbasu/Installations/sage-4.7.2/local/lib/python2.6/site-packages/sage/interfaces/gap.py", line 374, in eval
    result = Expect.eval(self, input_line, **kwds)
  File "/home/punarbasu/Installations/sage-4.7.2/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 1039, in eval
    for L in code.split('\n') if L != ''])
  File "/home/punarbasu/Installations/sage-4.7.2/local/lib/python2.6/site-packages/sage/interfaces/gap.py", line 518, in _eval_line
    raise RuntimeError, message
RuntimeError: Gap produced error output
Permutation: cycles must be disjoint and duplicate-free

   executing Combinations([(1, 1), (2, 2), (3, 3)],2);
```

And like this:

```
sage: F.<a> = GF(4, 'a'); V = list(VectorSpace(F, 2)); combinations(V, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_78.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("Ri48YT4gPSBHRig0LCAnYScpOyBWID0gbGlzdChWZWN0b3JTcGFjZShGLCAyKSk7IGNvbWJpbmF0aW9ucyhWLCAxKQ=="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpXtx6m9/___code___.py", line 3, in <module>
    exec compile(u"F = GF(_sage_const_4 , 'a', names=('a',)); (a,) = F._first_ngens(1); V = list(VectorSpace(F, _sage_const_2 )); combinations(V, _sage_const_1 )" + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "/home/punarbasu/Installations/sage-4.7.2/local/lib/python2.6/site-packages/sage/combinat/combinat.py", line 2017, in combinations
    return eval(ans)
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
```

Something as simple as this works with both examples because it doesn't care what the items inside the list are:

```
def binom(S, k):
    # S is a list, k is a number
    def _binom(S, k):
        if len(S) < k:
            return
        elif len(S) == k:
            yield S
        elif k == 1:
            for s in S:
                yield [s]
        else:    
            for i,s in enumerate(S):
                for ss in binom(S[(i+1):], k-1):
                    yield [s]+ss
    return list(_binom(S, k))
```


I suppose the above implementation in cython will be already faster than this python code, and it also seems to use a very specific algorithm which is meant to be fast.


---

Comment by ppurka created at 2011-11-21 09:49:10

Sorry, small typo above (but the code is to just give an idea  of a working example):

`for ss in binom(S[(i+1):], k-1):`  should be 

`for ss in _binom(S[(i+1):], k-1):`


---

Comment by jason created at 2013-01-02 19:22:32

What's the current status?

Just the other day, I would have loved an iterator that would iterate through a gray code and tell me just the element that changed and by how much, so I could do:


```
for i in myiter():
    # i is the thing that changed, so I can update my data structure accordingly, and just have to change one thing
    # some other code depending on the current status of my data structure
```



---

Comment by ppurka created at 2013-01-03 01:13:30

The original purpose of the patch - to write an efficient `combinations` is now already present. See #13821 for a patch to deprecate `combinations`.

As for a gray code iterator, I don't know the status of this one. Has anything been done about the "generic iterators"? I am not aware of any such construct in Sage.
