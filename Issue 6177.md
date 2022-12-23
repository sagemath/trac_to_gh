# Issue 6177: [with patch, needs work] Update PolyBoRi to newest upstream release

Issue created by migration from https://trac.sagemath.org/ticket/6177

Original creator: malb

Original creation time: 2009-06-01 09:35:19

Assignee: malb

CC:  polybori burcin rlm boothby

Keywords: M4RI, PolyBoRi


```
2009/04/06 The first release candidate of PolyBoRi 0.6 is available for download. It comes with a PEP8-conforming python interface and new algorithms: FGLM and (experimental) parallel processing of Gröbner basis variants. In addition, the documentation was improved considerably: the tutorial is more extensive, and the TeX4ht-Support has been improved. Finally, built-in support for plotting the underlying decision diagrams has been added.
```


This version also allows bigger systems to be solved using the M4RI library (due to an updated M4RI) and makes use of M4RI in shared library mode.

This ticket depends on #5510


---

Comment by malb created at 2009-06-01 09:36:42

The SPKG is here:

   http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.spkg


---

Comment by malb created at 2009-06-04 09:57:49

TODO:

 * write more documentation
 * fix FGLM (it doesn't do anything right now)
 * expose PolyBoRi ZDD plots


---

Comment by malb created at 2009-06-04 09:59:51

Michael's notes on the docs:


```
all_spolys_in_next_degree()
pops all spolys with next sugar degree from the strategy 

clean_top_by_chain_criterion()

contains_one()
1 \in generating system?

faugere_step_dense()
reduces a vector of polynomials using linear algebra

implications()
computes useful implied polynomials of i-th generator, and adds them  to the strategy, if it finds any.

ll_reduce_all()
uses the build in ll-encoded BooleSet of polynomials with linear lexicographical leading term, which coincides  
with leading term in current ordering, to reduce the tails of all polynomials in the strategy

minimalize()
returns a vector of all polynomials with minimal leading terms use that if strat contains a GB

minimalize_and_tail_reduce()
returns a vector of all polynomials with minimal leading terms and does tail reductions use that if strat contains a GB and you want a reduced GB

next_spoly()

nf()

npairs()
Number of pairs in the pair queue

reduction_strategy
ReductionStrategy member of GroebnerStrategy, does all the reductions

small_spolys_in_next_degree()
I am not sure, if it is still used, similar to the next one

some_spolys_in_next_degree(n)

fetches upto n s-polynomials from the strategy, having all a sugar  
value <= the sugar value of the first polynomial/pair in the queue.

suggest_plugin_variable()
some heuristic to suggest a variable, which could be plugged with 0 and 1 to branch the computation

symmGB_F2()
out of date C++ implementation of symmgb, will revived at some point of time

top_sugar()
sugar value of the first "pair" in the queue. Sugar is "some estimated degree".

variable_has_value()
Computes, whether, there exists some polynomial of the form $v+c$ in the Strategy, where c is a constant
in the list of generators

elength()
x+y*z -> 3
for lp (x>y>z)
the interesting case

Note

If this function is called repeatedly with the same I then it is  
advised to use PolyBoRi’s GroebnerStrategy object directly, since that  
will be faster. See the source code of this function for details.

-> ReductionStrategy, as it is smaller and contains everything needed  
for reductions.
```



---

Comment by malb created at 2009-06-04 10:01:09

More notes by Michael:


```
Can you please link: http://polybori.sourceforge.net/zdd.html

A picture says more, than 1000 words.

2. How is the pickling of Boolean polynomials done?

Have a look at parallel.py:

def to_fast_pickable(l):
     """
     to_fast_pickable(l) converts a list of polynomials into a builtin  
Python value, which is fast pickable and compact.
     INPUT:
         - a list of Boolean polynomials
     OUTPUT:
         It is converted to a tuple consisting of
         - codes referring to the polynomials
         - list of conversions of nodes.
             The nodes are sorted, that
             n occurs before n.else_branch(), n.then_branch()
             Nodes are only listed, if they are not constant.

         A node is converted in this way:
             0 -> 0
             1 -> 1
             if_then_else(v,t,e) -> (v, index of then branch +2, index of else branch +2)
             The shift of +2 is for the constant values implicitly   contained in the list.
         Each code c refers to the c-2-th position in the conversion   list, if c >=2, else to
         the corresponding Boolean constant if c in {0, 1}
     EXAMPLES:
         >>> from polybori.PyPolyBoRi import Ring, Variable
         >>> r=Ring(1000)
         >>> x=Variable
         >>> to_fast_pickable([Polynomial(1)])
         [[1], []]
         >>> to_fast_pickable([Polynomial(0)])
         [[0], []]
         >>> to_fast_pickable([x(0)])
         [[2], [(0, 1, 0)]]
         >>> to_fast_pickable([x(0)*x(1)+x(1)])
         [[2], [(0, 3, 3), (1, 1, 0)]]
         >>> to_fast_pickable([x(1)])
         [[2], [(1, 1, 0)]]
         >>> to_fast_pickable([x(0)+1])
         [[2], [(0, 1, 1)]]
         >>> to_fast_pickable([x(0)*x(1)])
         [[2], [(0, 3, 0), (1, 1, 0)]]
         >>> to_fast_pickable([x(0)*x(1)+x(1)])
         [[2], [(0, 3, 3), (1, 1, 0)]]
         >>> to_fast_pickable([x(0)*x(1)+x(2)])
         [[2], [(0, 3, 4), (1, 1, 0), (2, 1, 0)]]
         >>> p=x(5)*x(23) + x(5)*x(24)*x(59) + x(5) + x(6)*x(23)*x(89)   + x(6)*x(60)*x(89) + x(23) + x(24)*x(89) + x(24) + x(60)*x(89) + x(89)   + 1
         >>> from_fast_pickable(to_fast_pickable([p]))==[p]
         True
         >>> to_fast_pickable([x(0)*x(1), Polynomial(0), Polynomial(1), x(3)])
         [[2, 0, 1, 4], [(0, 3, 0), (1, 1, 0), (3, 1, 0)]]
     """
```



---

Comment by malb created at 2009-06-04 10:02:02

Btw. I'm posting this all here because I might not get around to do the last required steps in the next 2 weeks.


---

Comment by malb created at 2009-06-05 11:18:27

Burcin, I came across the `RingProxy` class which we add to `PyPolyBori.py`. I don't understand why we need this.


---

Comment by burcin created at 2009-06-05 11:34:57

AFAIR, the `global_ring()` function you see in that file is expected to return an object which has a `.set()` method. This method should change the ordering of the current ring. I didn't want to add a `.set()` method to the `BooleanPolynomialRing`, so decided to wrap it in a `RingProxy` class.

Of course, this was centuries ago, and it's possible that I'm making up all that I wrote above. :)


---

Comment by PolyBoRi created at 2009-06-23 06:13:20

I just ported the plotting to the jinja template engine, which is contained in Sage.
The only missing dependency is graphviz, which is an optional package.
I hope that helps integrating it. I really would wish to be able to plot ZDDs in the Sage notebook.
That would be a nice extra feature and would probably help much about the understanding of ZDDs.


---

Comment by PolyBoRi created at 2009-06-23 06:14:53

plot.py patch for jinja, to be contained in a 0.6.2 release (hopefully soon)


---

Attachment

CCing Robert Miller since he is the resident graph expert and is sitting like two seats next to me. Robert, the last two comments are about printing the decision diagrams used by PolyBoRi to represent polynomials, cf. http://polybori.sourceforge.net/zdd.html


---

Comment by malb created at 2009-06-23 10:11:34

Burcin, I just uploaded my current PolyBoRi SPKG to /home/malb/spkgs so all you should need is the this SPKG + the patch `polybori_0_6_1.patch`


---

Attachment

most recent version of the patch


---

Comment by rlm created at 2009-06-23 10:12:52

CCing Tom Boothby, because he loves decision diagrams for polynomials.


---

Comment by PolyBoRi created at 2009-06-23 11:17:18

Hi!
Just as a further motivation :-) :
That is, how the diagrams will look like.
http://polybori.sourceforge.net/zdd.html
Michael


---

Comment by malb created at 2009-07-28 15:23:59

The requires SPKG is available at

   http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3-20090728.spkg

Only apply `polybori-0-6-3.patch`.


---

Comment by malb created at 2009-08-04 10:52:09

See http://groups.google.com/group/sage-support/browse_thread/thread/fa3afaeff5444cf3 for a problem description.


---

Comment by PolyBoRi created at 2009-08-05 12:44:04

doesn't build for me (Mac OS X, 64 BIT, but it's not an 64 BIT issue).
I have to set FORCE_HASH_MAP=True via custom.py or construct argument.

```
g++ -o groebner/src/groebner.o -c -m64 -O3 -Wno-long-long -Wreturn-type -g -fPIC -ftemplate-depth-100 -g -fPIC -m64 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DSIZEOF_VOID_P=8 -DSIZEOF_LONG=8 -DHAVE_IEEE_754 -I/Applications/sage/spkg/build/polybori-0.6.3-20090728/src/boost_1_34_1.cropped -I/Applications/sage/local/include -I/Applications/sage/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd groebner/src/groebner.cc
/usr/include/c++/4.0.0/tr1/hashtable: In member function 'typename std::tr1::hashtable<Key, Value, Allocator, ExtractKey, Equal, H1, H2, H, RehashPolicy, cache_hash_code, mutable_iterators, unique_keys>::const_iterator std::tr1::hashtable<Key, Value, Allocator, ExtractKey, Equal, H1, H2, H, RehashPolicy, cache_hash_code, mutable_iterators, unique_keys>::find(const Key&) const [with Key = polybori::BooleExponent, Value = std::pair<const polybori::BooleExponent, int>, Allocator = std::allocator<std::pair<const polybori::BooleExponent, int> >, ExtractKey = Internal::extract1st<std::pair<const polybori::BooleExponent, int> >, Equal = std::equal_to<polybori::BooleExponent>, H1 = polybori::hashes<polybori::BooleExponent>, H2 = Internal::mod_range_hashing, H = Internal::default_ranged_hash, RehashPolicy = Internal::prime_rehash_policy, bool cache_hash_code = false, bool mutable_iterators = true, bool unique_keys = true]':
groebner/src/groebner_alg.h:267:   instantiated from here
/usr/include/c++/4.0.0/tr1/hashtable:1135: error: passing 'const std::tr1::hashtable<polybori::BooleExponent, std::pair<const polybori::BooleExponent, int>, std::allocator<std::pair<const polybori::BooleExponent, int> >, Internal::extract1st<std::pair<const polybori::BooleExponent, int> >, std::equal_to<polybori::BooleExponent>, polybori::hashes<polybori::BooleExponent>, Internal::mod_range_hashing, Internal::default_ranged_hash, Internal::prime_rehash_policy, false, true, true>' as 'this' argument of 'typename std::tr1::hashtable<Key, Value, Allocator, ExtractKey, Equal, H1, H2, H, RehashPolicy, cache_hash_code, mutable_iterators, unique_keys>::node* std::tr1::hashtable<Key, Value, Allocator, ExtractKey, Equal, H1, H2, H, RehashPolicy, cache_hash_code, mutable_iterators, unique_keys>::find_node(Internal::hash_node<Value, cache_hash_code>*, const Key&, typename std::tr1::hashtable<Key, Value, Allocator, ExtractKey, Equal, H1, H2, H, RehashPolicy, cache_hash_code, mutable_iterators, unique_keys>::hash_code_t) [with Key = polybori::BooleExponent, Value = std::pair<const polybori::BooleExponent, int>, Allocator = std::allocator<std::pair<const polybori::BooleExponent, int> >, ExtractKey = Internal::extract1st<std::pair<const polybori::BooleExponent, int> >, Equal = std::equal_to<polybori::BooleExponent>, H1 = polybori::hashes<polybori::BooleExponent>, H2 = Internal::mod_range_hashing, H = Internal::default_ranged_hash, RehashPolicy = Internal::prime_rehash_policy, bool cache_hash_code = false, bool mutable_iterators = true, bool unique_keys = true]' discards qualifiers
scons: *** [groebner/src/groebner.o] Error 1
```



---

Comment by malb created at 2009-08-05 13:35:09

fixes the issue


---

Attachment

The attached patch fixes the wrong GB issue.


---

Comment by malb created at 2009-08-05 13:36:28

Replying to [comment:16 PolyBoRi]:
> doesn't build for me (Mac OS X, 64 BIT, but it's not an 64 BIT issue).
> I have to set FORCE_HASH_MAP=True via custom.py or construct argument.

Is that a bug in PolyBoRi or how we build it?


---

Comment by malb created at 2009-08-05 16:41:21

It seems some `const` is dropped somewhere which makes the C++ compiler choke?


```
passing 'const std::tr1::hashtable<... as 'this' argument of 'typename std::tr1::hashtable<Key, Valu ...  discards qualifiers
```



---

Comment by malb created at 2009-08-06 14:33:07

Michael suggested to pass

```
scons  FORCE_HASH_MAP=True
```

on OSX *only* to work around this issue.

I can't work on this in the near future and would appreciate if someone else could take care of this.


---

Comment by PolyBoRi created at 2009-08-06 15:24:50

Hi!
I have put a new spkg here:

http://sage.math.washington.edu/home/bricken/polybori-0.6.3-20090806.spkg
I have adjusted the custom.py.
Actually, I needed most time, until I noticed, that the patched SConstruct was outdated, which I have fixed.

May I ask, what you have fixed about the wrong results due to some interface issues?

Michael


---

Comment by malb created at 2009-08-06 15:27:06

I added a new term ordering "deglex_asc" which is used instead of "degrevlex" if a Sage ring is constructed from a C++ ring. Also, I changed the hash to include the term ordering.


---

Comment by PolyBoRi created at 2009-08-06 17:03:55

`'sage.rings.polynomial.pbori.BooleanPolynomialRing' object has no attribute 'clone'`
The clone method is not wrapped, which does not give us access to our new ll-stuff, which is also very relevant to crypto.
I just had a look at the present stuff and tried to speed it up.


---

Comment by malb created at 2009-08-07 08:19:43

I checked in Michael's changes in the SPKG in 

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3-20090807.spkg

under Michael's name.

*My Todo List*
* wrap `clone`
* wrap `ll_red_nf_noredsb_single_recursive_call`
* speed-up `Polynomial(p)` if `p` is a boolean polynomial
* check for memory leaks with crypo scripts from bitbucket


---

Attachment

The latest patch links in gd


---

Comment by PolyBoRi created at 2009-08-07 08:38:44

I have to add that also substitute_variables(vec, poly) is missing, which is
an instantiation of
substitute_variables<std::vector<BoolePolynomial>, BoolePolynomial>

var(i) (our polybori indices) is replaced by vec[i] in poly.

docs:

BoolePolyRing::clone is a flat copy of the ring, as well as the normal copy constructor.
In contrast to using the constructor, the new ring will contain its own vector of variable names,
so changing a variable name via `set_variable_name`
won't modify the original ring.

ll_red_nf_noredsb_single_recursive call has the same specification as ll_red_nf_noredsb, but a different implementation:
This is described in my PHD thesis, the corresponding chapter is available on demand.
It is very sensitive to the ordering of variables, however it has the very nice property, that it needs just one recursive call.
We provide utilities for determing an appropriate var ordering. It is a matter of research, to find good heuristics here.
But I think, that I have a good solution.


---

Attachment

adds the requested functions


---

Comment by malb created at 2009-08-10 17:17:57

The new patch in combination with http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3-20090810.spkg provides the following additional features:
 * `Polynomial(p)` much faster if `p` is a `BooleanPolynomial`
 * added `substitute_variables`
 * added `BooleanPolynomialRing.clone`
 * added `ll_red_nf_noredsb_single_recursive`


---

Comment by malb created at 2009-08-10 19:42:24

the latest patch swallowed the 'gd' in modules_list.py, this one adds it back


---

Attachment

speeds up comparison with zero and fixes a doctest failure


---

Comment by malb created at 2009-08-16 00:16:25

If one doesn't have #6628 applied one hunk will fail which can safely be ignored.


---

Comment by drkirkby created at 2009-08-16 04:12:05

This appears to suffer the same issue earlier releases of PolyBoRi had on Solaris. Even if the Sun Studio compiler is not in the path, and CC, CXX are not set, so this attempts to use the Sun C++ compiler. That fails miserably. 

Changes had to be made to the earlier PolyBoRi code to allow this to build with gcc on Solaris if the Sun compiler was present. I assume those changes will need to be reintegrated. 

Here you can see CC and CXX are not set

```
drkirkby@smudge:[~/sage/sage-4.1.1] $ echo $CC

drkirkby@smudge:[~/sage/sage-4.1.1] $ echo $CXX

drkirkby@smudge:[~/sage/sage-4.1.1] $
```


But still the package uses Sun's C++ compiler. 


```
/opt/sunstudio12.1/bin/CC -o polybori/src/BoolePolyRing.o -c -O3 -Wno-long-long -Wreturn-type -g -fPIC -ftemplate-depth-100 -g -fPIC -O3 -Wno-long-long -Wreturn -type -g -fPIC -DNDEBUG -DHAVE_GD -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754  -DBSD -I/export/home/drkirkby/sage/sage-4.1.1/spkg/build/polybori-0.6.3-2009081 0/src/boost_1_34_1.cropped -I/export/home/drkirkby/sage/sage-4.1.1/local/include  -I/export/home/drkirkby/sage/sage-4.1.1/local/include/python2.6 -Ipolybori/incl ude -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd polybori/ src/BoolePolyRing.cc
CC: Warning: Option -Wno-long-long passed to ld, if ld is invoked, ignored other wise
CC: Warning: Option -Wreturn-type passed to ld, if ld is invoked, ignored otherw ise
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -ftemplate-depth-100 passed to ld, if ld is invoked, ignored  otherwise
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -Wno-long-long passed to ld, if ld is invoked, ignored other wise
CC: Warning: Option -Wreturn-type passed to ld, if ld is invoked, ignored otherw ise
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
"polybori/include/CDDManager.h", line 103: Warning: Last line in file "polybori/ include/cacheopts.h" is not terminated with a newline.
"polybori/include/CCuddZDD.h", line 308: Warning (Anachronism): Formal argument func of type DdNode*(*)(DdManager*,DdNode*,int) in call to polybori::CCuddDDBase <polybori::CCuddZDD>::apply(DdNode*(*)(DdManager*,DdNode*,int), int) const is be ing passed extern "C" DdNode*(*)(DdManager*,DdNode*,int).
"polybori/include/CCuddZDD.h", line 308: Warning (Anachronism): Formal argument func of type DdNode*(*)(DdManager*,DdNode*,int) in call to polybori::CCuddDDBase <polybori::CCuddZDD>::apply(DdNode*(*)(DdManager*,DdNode*,int), int) const is be ing passed extern "C" DdNode*(*)(DdManager*,DdNode*,int).
"polybori/include/CCuddZDD.h", line 308: Warning (Anachronism): Formal argument func of type DdNode*(*)(DdManager*,DdNode*,int) in call to polybori::CCuddDDBase <polybori::CCuddZDD>::apply(DdNode*(*)(DdManager*,DdNode*,int), int) const is be ing passed extern "C" DdNode*(*)(DdManager*,DdNode*,int).
"polybori/include/CCuddZDD.h", line 313: Warning (Anachronism): Formal argument func of type DdNode*(*)(DdManager*,DdNode*,DdNode*,DdNode*) in call to polybori: :CCuddDDBase<polybori::CCuddZDD>::apply(DdNode*(*)(DdManager*,DdNode*,DdNode*,Dd Node*), const polybori::CCuddZDD&, const polybori::CCuddZDD&) const is being pas sed extern "C" DdNode*(*)(DdManager*,DdNode*,DdNode*,DdNode*).
"polybori/include/CCuddZDD.h", line 322: Warning (Anachronism): Formal argument func of type int(*)(DdManager*,DdNode*) in call to polybori::CCuddDDBase<polybor i::CCuddZDD>::apply(int(*)(DdManager*,DdNode*)) const is being passed extern "C"  int(*)(DdManager*,DdNode*).
"polybori/include/CCuddZDD.h", line 323: Warning (Anachronism): Formal argument func of type int(*)(DdManager*,DdNode*) in call to polybori::CCuddDDBase<polybor i::CCuddZDD>::apply(int(*)(DdManager*,DdNode*)) const is being passed extern "C"  int(*)(DdManager*,DdNode*).
"polybori/include/CCuddZDD.h", line 327: Warning (Anachronism): Formal argument func of type int(*)(DdManager*,DdNode*) in call to polybori::CCuddDDBase<polybor i::CCuddZDD>::memApply<int>(int(*)(DdManager*,DdNode*)) const is being passed ex tern "C" int(*)(DdManager*,DdNode*).
"polybori/include/CCuddZDD.h", line 330: Warning (Anachronism): Formal argument func of type double(*)(DdManager*,DdNode*) in call to polybori::CCuddDDBase<poly bori::CCuddZDD>::memApply<double>(double(*)(DdManager*,DdNode*)) const is being passed extern "C" double(*)(DdManager*,DdNode*).
"polybori/include/CCuddInterface.h", line 192: Warning (Anachronism): Formal arg ument func of type DdNode*(*)(DdManager*,int) in call to polybori::CCuddInterfac e::apply(DdNode*(*)(DdManager*,int), int) const is being passed extern "C" DdNod e*(*)(DdManager*,int).
"polybori/include/CCuddInterface.h", line 195: Warning (Anachronism): Formal arg ument func of type DdNode*(*)(DdManager*,int) in call to polybori::CCuddInterfac e::apply(DdNode*(*)(DdManager*,int), int) const is being passed extern "C" DdNod e*(*)(DdManager*,int).
"polybori/include/CCuddInterface.h", line 198: Warning (Anachronism): Formal arg ument func of type DdNode*(*)(DdManager*) in call to polybori::CCuddInterface::a pply(DdNode*(*)(DdManager*)) const is being passed extern "C" DdNode*(*)(DdManag er*).
"polybori/include/CCuddNavigator.h", line 157: Error: iterator_traits is not a m ember of std.
"polybori/include/CCuddNavigator.h", line 157: Error: A declaration does not spe cify a tag or an identifier.
"polybori/include/CCuddNavigator.h", line 157: Error: Use ";" to terminate decla rations.
"polybori/include/CCuddNavigator.h", line 157: Error: "}" expected instead of "< ".
"polybori/include/CCuddNavigator.h", line 157: Error: Use ";" to terminate decla rations.
"polybori/include/CCuddNavigator.h", line 157: Error: A declaration was expected  instead of "<".
"polybori/include/CCuddNavigator.h", line 157: Error: "," expected instead of "> ".
"polybori/include/CCuddNavigator.h", line 159: Error: value_type is not defined.
"polybori/include/CCuddNavigator.h", line 163: Error: There must be an identifie r to declare.
"polybori/include/CCuddNavigator.h", line 171: Error: "explicit" is not allowed here.
"polybori/include/CCuddNavigator.h", line 171: Error: ")" expected instead of "& ".
"polybori/include/CCuddNavigator.h", line 174: Error: ")" expected instead of "& ".
"polybori/include/CCuddNavigator.h", line 177: Error: Type name expected instead  of "CCuddNavigator".
"polybori/include/CCuddNavigator.h", line 177: Error: Illegal number of argument s for ~file level().
"polybori/include/CCuddNavigator.h", line 180: Error: "," expected instead of "& ".
"polybori/include/CCuddNavigator.h", line 183: Error: self is not defined.
"polybori/include/CCuddNavigator.h", line 183: Error: The function "thenBranch()  const" cannot be declared const.
"polybori/include/CCuddNavigator.h", line 183: Error: Can only use this within a  non-static member function.
"polybori/include/CCuddNavigator.h", line 183: Error: Only a function may be cal led.
"polybori/include/CCuddNavigator.h", line 183: Error: Only a function may be cal led.
"polybori/include/CCuddNavigator.h", line 186: Error: Multiple declaration for s elf.
"polybori/include/CCuddNavigator.h", line 186: Error: "," expected instead of "& ".
"polybori/include/CCuddNavigator.h", line 189: Error: self is not defined.
"polybori/include/CCuddNavigator.h", line 189: Error: The function "elseBranch()  const" cannot be declared const.
"polybori/include/CCuddNavigator.h", line 189: Error: Can only use this within a  non-static member function.
Compilation aborted, too many Error messages.
scons: *** [polybori/src/BoolePolyRing.o] Error 1
scons: building terminated because of errors.
Error building PolyBoRi.

real    0m22.968s
user    0m17.385s
sys     0m4.811s
sage: An error occurred while installing polybori-0.6.3-20090810
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /export/home/drkirkby/sage/sage-4.1.1/install.log.  Describe your computer, o perating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/export/home/drkirkby/sage/sage-4.1.1/spkg/build/polybori-0.6.3-20090810 and typ e 'make'.
Instead type "/export/home/drkirkby/sage/sage-4.1.1/sage -sh"
in order to set all environment variables correctly, then cd to
/export/home/drkirkby/sage/sage-4.1.1/spkg/build/polybori-0.6.3-20090810
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/polybori-0.6.3-20090810] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.1/spkg'
```



---

Comment by drkirkby created at 2009-08-16 08:38:33

If you are updating PolyBoRi, take a look at #6582 too.


---

Comment by PolyBoRi created at 2009-08-17 07:21:49

I remember, that I used the SConstruct.patch to regenerate the patched SConstruct from a current version. Maybe someone has just hacked the fix into the patched SConstruct and ignored the patch?

Michael


---

Comment by PolyBoRi created at 2009-08-18 08:35:07

Hi!

First of all,
it is difficult to test the Sage-Wrapper using our tests, since Sage checks the variable names from time to time.



```
/Applications/sage/local/lib/python2.6/site-packages/polybori/gbcore.pyc in clean_polys(I)
    156     return make_wrapper
    157 def clean_polys(I):
--> 158     zero=Polynomial(0)
    159     I=list(set((Polynomial(p) for p in I if p!=zero)))
    160     return I

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.PolynomialFactory.__call__ (sage/rings/polynomial/pbori.cpp:24232)()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.get_cring (sage/rings/polynomial/pbori.cpp:36518)()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialRing_from_PBRing (sage/rings/polynomial/pbori.cpp:37213)()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ring_generic.so in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.__init__ (sage/rings/polynomial/multi_polynomial_ring_generic.c:1913)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.__init__ (sage/structure/parent_gens.c:2342)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:2830)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2068)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens._certify_names (sage/structure/parent_gens.c:1601)()
```


Furthermore the ring wrapper has no method n_variables, which is equivalent to ngens.

Michael


---

Comment by PolyBoRi created at 2009-08-18 09:51:57

Hi!
The following gives me a segfault:

```
from polybori import *
data=load_file("data/cook.py")

change_ordering(block_dp_asc)
append_ring_block(25)
groebner_basis(data.ideal, prot=True, heuristic=False)
```


```
------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

sage.bin(2141) malloc: *** error for object 0x10ad1f000: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug
sage.bin(2141) malloc: *** error for object 0x10ad52000: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug
sage.bin(2141) malloc: *** error for object 0x10ad53800: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug
```


Used it on Mac OS X 10.5 64BIT.

I attach the example file


---

Comment by PolyBoRi created at 2009-08-18 09:52:54

example for segfault


---

Attachment

adds n_variables and fixes segfault


---

Attachment

The newest version of the patch fixes the segfault and adds `n_variables`. Note that both Michael and myself are using this patch for more than two weeks now in our research (see above for issues discovered and fixed this way), so it should be (almost) good to go. It mainly needs a review from the Sage side.


---

Comment by PolyBoRi created at 2009-08-18 11:53:27

Replying to [comment:34 malb]:
> The newest version of the patch fixes the segfault and adds `n_variables`. Note that both Michael and myself are using this patch for more than two weeks now in our research (see above for issues discovered and fixed this way), so it should be (almost) good to go. It mainly needs a review from the Sage side.

This is also my point of view.
Thanks for the update.
Michael


---

Comment by PolyBoRi created at 2009-08-18 12:33:34

I have found another subtle bug.
This is due to, that we are in the quite slow progress to make PolyBoRi more Pythonic:
Since Python is dynamically typed,
len should be the same on polynomials and monomials, so it's the constant 1-function for us now.


```python
P=BooleanPolynomialRing(3,"x")
sage: m=P.gen(1)*P.gen(2)
sage: m.lead()
x1*x2
sage: len(m.lead())
2
sage: 
Exiting SAGE (CPU time 0m0.13s, Wall time 0m20.23s).
```


```python
ginkgo:downloads michael$ ipbori

In [1]: p=x(1)*x(2)

In [2]: p.__class__
Out[2]: <class 'polybori.dynamic.PyPolyBoRi.Monomial'>

In [3]: len(p)
Out[3]: 1
```


Fixing that will break the anf2cnf converter here:

```python
 isinstance(m, BooleanPolynomial):
            if len(m) == 1:
                m = m.lm()
            else:
                raise TypeError, "Input must be monomial."

        if m == 1:
            monomial = self._cnf_literal()
            return (monomial,), ((monomial,),) # adding the clause that 1
                                            # has to be True
```


Just use .deg instead of len there


---

Comment by malb created at 2009-08-18 13:15:48

changes len(m) to be constant 1 if m is a monomial


---

Attachment

The attached patch fixes the issue (`len(m) == 1` if `m` is a monomial). I don't see how it breaks anf2cnf but I'll check now (this is orthogonal to accepting this patch anyway)


---

Comment by malb created at 2009-08-18 13:27:28

Alright, I saw and fixed it on bitbucket (th anf2ncf issue)


---

Comment by PolyBoRi created at 2009-08-19 12:42:59

Hi!

In a similar way as the polynomial constructor, Variable is really slow:

```
timeit("Variable(0)")
25 loops, best of 3: 8.68 ms per loop
```


This is no release blocker,

but the following is a bug:

```python
 BooleSet([Monomial()])
Out[1]: {}
```

correct would be

```
In [1]: BooleSet([Monomial()])
Out[1]: {{}}
```


This is implemented in PyPolyBoRi.py


---

Attachment

rebased and bugfix


---

Comment by malb created at 2009-08-20 13:49:37

The new SPKG 

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3-20090820.spkg

and the new patch `polybori-0.6.3.patch` improve the performance and fix the bug described above. However, I couldn't make `Variable(0)` faster because the main bottleneck for some reason is `BooleEnv::ring()` which we call to get the current ring. The code


```c
  BoolePolyRing __pyx_v__pbring;
  //... some more other Cython stuff
  __pyx_v__pbring = BooleEnv::ring();
```


seems to be the bottleneck. Any ideas?


---

Comment by PolyBoRi created at 2009-08-20 14:02:46

Hi!
It's damn hot here.
At the moment, I don't know any more, why you shouldn't just use the
constructor Variable(i).
Is it, as you have to attach the parent?
Unluckily, we use use Variable(i) in a lot of places from python.
Of course, it would be cleaner to do something like ring.gen(i).
Michael


---

Comment by malb created at 2009-08-20 14:04:24

Replying to [comment:41 PolyBoRi]:
> Is it, as you have to attach the parent?

Yep, it is still somewhat strange that the code above is so slow.


---

Comment by PolyBoRi created at 2009-08-20 14:06:06

I think, we should wait for Alexander having a look on it, who might have an idea,
what happens.
Michael


---

Comment by PolyBoRi created at 2009-08-20 14:07:37

By the way, there happen at least two things:
the call BooleEnv::ring and

```C++
static ring_type& ring(){
      return active_ring;
  }
```

the assigment operator.


---

Comment by malb created at 2009-08-20 14:09:23

It must be the assignment operator (or the dummy constructor) then.


---

Comment by PolyBoRi created at 2009-08-20 14:13:04

Thanks, a lot, you did it.
I didn't remember this Cython thingy.
It is the dummy constructor. The assignment doesn't do anything.
It is isn't defined. So it is the standard c++ behaviour.
However the dummy constructors of the ring should construct a CuddManager, which means something like allocating a memory pool.
Michael


---

Comment by malb created at 2009-08-20 14:42:43

faster Variable(i)


---

Attachment

The attached patch fixes the bottleneck by avoiding the dummy constructor. Note, that we still need to take care of that Solaris issue Dave reported where scons would pick up the Sun compiler instead of gcc.


---

Attachment

Solaris fix for patches/custom.py


---

Comment by PolyBoRi created at 2009-08-21 07:10:04

I added some lines to custom.py, s.th. C and C++ compiler are picked from the Sage environment (if any). This fixes the Solaris issue.

Regards,
  Alexander


---

Comment by malb created at 2009-08-25 10:13:27

I have added this fix to the newest SPKG available at:

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3-20090825.spkg


---

Comment by AlexGhitza created at 2009-08-27 02:20:34

There seems to be a pickling problem, try the following on sage.math:


```
sage -t -long devel/sage/sage/structure/sage_object.pyx
```



---

Comment by drkirkby created at 2009-08-27 06:08:02

I've found another Solaris issue. I tried a build of Sage from scratch on my Solaris machine, which has Sun Studio 12 update 1 in /opt/sunstudio12.1

You will note below that SCons can't write to the file sage-4.1.1/local/share/polybori/flags.conf, as it does not exist. 

It strikes me the build process of this leaves a bit to be desired. Note in the following line, -fPIC is twice used as a flag (... -g -fPIC -fPIC -DNDEBUG), and the 'gd' library is linked no less than four times in the line following that (...-Lgroebner -LCudd -lm -lgd -lgd -lgd -lgd). Looking at install.log I see numerous instances of this. 

Another thing that I believe would be helpful is if there was a space between the '-h' flag and the library name, which appears below as  "-Wl,-hlibpboriCudd-0.6.3.so.0". Although the Sun linker will accept that, I think having "-Wl,-h libpboriCudd-0.6.3.so.0" would be a bit neater. But all these are minor points compared to the fact polybori fails as it can't write to a file which does not exist. 



```

gcc -o M4RI/brilliantrussian.pic.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -fPIC -DNDEBUG -DHAVE_GD -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/export/home/drkirkby/sage/tmp/sage-4.1.1/spkg/build/polybori-0.6.3-20090825/src/boost_1_34_1.cropped -I/export/home/drkirkby/sage/tmp/sage-4.1.1/local/include -I/export/home/drkirkby/sage/tmp/sage-4.1.1/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/brilliantrussian.c
g++ -o groebner/libgroebner-0.6.3.so.0.0.0 -G -Wl,-hlibgroebner-0.6.3.so.0 Cudd/obj/cuddObj.pic.o Cudd/util/cpu_time.pic.o Cudd/util/state.pic.o Cudd/util/datalimit.pic.o Cudd/util/texpand.pic.o Cudd/util/pipefork.pic.o Cudd/util/strsav.pic.o Cudd/util/ptime.pic.o Cudd/util/tmpfile.pic.o Cudd/util/stub.pic.o Cudd/util/cpu_stats.pic.o Cudd/util/safe_mem.pic.o Cudd/util/getopt.pic.o Cudd/util/prtime.pic.o Cudd/util/pathsearch.pic.o Cudd/cudd/cuddApprox.pic.o Cudd/cudd/cuddRead.pic.o Cudd/cudd/cuddLevelQ.pic.o Cudd/cudd/cuddCof.pic.o Cudd/cudd/cuddGenetic.pic.o Cudd/cudd/cuddZddPort.pic.o Cudd/cudd/cuddMatMult.pic.o Cudd/cudd/cuddZddIsop.pic.o Cudd/cudd/cuddAPI.pic.o Cudd/cudd/cuddZddGroup.pic.o Cudd/cudd/cuddZddSymm.pic.o Cudd/cudd/cuddRef.pic.o Cudd/cudd/cuddZddMisc.pic.o Cudd/cudd/cuddDecomp.pic.o Cudd/cudd/cuddZddUtil.pic.o Cudd/cudd/cuddLiteral.pic.o Cudd/cudd/cuddAddNeg.pic.o Cudd/cudd/cuddPriority.pic.o Cudd/cudd/cuddAnneal.pic.o Cudd/cudd/cuddInit.pic.o Cudd/cudd/cuddZddSetop.pic.o Cudd/cudd/cuddReorder.pic.o Cudd/cudd/cuddSolve.pic.o Cudd/cudd/cuddBddCorr.pic.o Cudd/cudd/cuddAddFind.pic.o Cudd/cudd/cuddAddInv.pic.o Cudd/cudd/cuddWindow.pic.o Cudd/cudd/cuddAddIte.pic.o Cudd/cudd/cuddAddAbs.pic.o Cudd/cudd/cuddZddReord.pic.o Cudd/cudd/cuddBddAbs.pic.o Cudd/cudd/cuddBddIte.pic.o Cudd/cudd/cuddLinear.pic.o Cudd/cudd/cuddSign.pic.o Cudd/cudd/cuddCheck.pic.o Cudd/cudd/cuddZddCount.pic.o Cudd/cudd/cuddZddFuncs.pic.o Cudd/cudd/cuddEssent.pic.o Cudd/cudd/cuddGroup.pic.o Cudd/cudd/cuddSplit.pic.o Cudd/cudd/cuddSat.pic.o Cudd/cudd/cuddAddApply.pic.o Cudd/cudd/cuddLCache.pic.o Cudd/cudd/cuddCache.pic.o Cudd/cudd/cuddAndAbs.pic.o Cudd/cudd/cuddHarwell.pic.o Cudd/cudd/cuddBridge.pic.o Cudd/cudd/cuddUtil.pic.o Cudd/cudd/cuddExport.pic.o Cudd/cudd/cuddSubsetHB.pic.o Cudd/cudd/cuddAddWalsh.pic.o Cudd/cudd/cuddSymmetry.pic.o Cudd/cudd/cuddTable.pic.o Cudd/cudd/cuddApa.pic.o Cudd/cudd/cuddCompose.pic.o Cudd/cudd/cuddZddLin.pic.o Cudd/cudd/cuddExact.pic.o Cudd/cudd/cuddSubsetSP.pic.o Cudd/cudd/cuddGenCof.pic.o Cudd/cudd/cuddClip.pic.o Cudd/cudd/cuddInteract.pic.o Cudd/mtr/mtrBasic.pic.o Cudd/mtr/mtrGroup.pic.o Cudd/st/st.pic.o Cudd/epd/epd.pic.o polybori/src/BoolePolyRing.pic.o polybori/src/BooleEnv.pic.o polybori/src/BoolePolynomial.pic.o polybori/src/BooleVariable.pic.o polybori/src/CErrorInfo.pic.o polybori/src/PBoRiError.pic.o polybori/src/CCuddFirstIter.pic.o polybori/src/CCuddNavigator.pic.o polybori/src/BooleMonomial.pic.o polybori/src/BooleSet.pic.o polybori/src/LexOrder.pic.o polybori/src/CCuddLastIter.pic.o polybori/src/CCuddGetNode.pic.o polybori/src/BooleExponent.pic.o polybori/src/DegLexOrder.pic.o polybori/src/DegRevLexAscOrder.pic.o polybori/src/pbori_routines.pic.o polybori/src/BlockDegLexOrder.pic.o polybori/src/BlockDegRevLexAscOrder.pic.o groebner/src/groebner.pic.o groebner/src/literal_factorization.pic.o groebner/src/randomset.pic.o groebner/src/pairs.pic.o groebner/src/groebner_alg.pic.o groebner/src/fglm.pic.o groebner/src/polynomial_properties.pic.o groebner/src/lexbuckets.pic.o groebner/src/dlex4data.pic.o groebner/src/dp_asc4data.pic.o groebner/src/lp4data.pic.o groebner/src/nf.pic.o groebner/src/interpolate.pic.o M4RI/grayflex.pic.o M4RI/permutation.pic.o M4RI/packedmatrix.pic.o M4RI/strassen.pic.o M4RI/misc.pic.o M4RI/brilliantrussian.pic.o -L/export/home/drkirkby/sage/tmp/sage-4.1.1/local/lib -L/export/home/drkirkby/sage/tmp/sage-4.1.1/local/lib/python2.6/config -Lpolybori -Lgroebner -LCudd -lm -lgd -lgd -lgd -lgd
g++ -o Cudd/libpboriCudd-0.6.3.so.0.0.0 -G -Wl,-hlibpboriCudd-0.6.3.so.0 Cudd/obj/cuddObj.pic.o Cudd/util/cpu_time.pic.o Cudd/util/state.pic.o Cudd/util/datalimit.pic.o Cudd/util/texpand.pic.o Cudd/util/pipefork.pic.o Cudd/util/strsav.pic.o Cudd/util/ptime.pic.o Cudd/util/tmpfile.pic.o Cudd/util/stub.pic.o Cudd/util/cpu_stats.pic.o Cudd/util/safe_mem.pic.o Cudd/util/getopt.pic.o Cudd/util/prtime.pic.o Cudd/util/pathsearch.pic.o Cudd/cudd/cuddApprox.pic.o Cudd/cudd/cuddRead.pic.o Cudd/cudd/cuddLevelQ.pic.o Cudd/cudd/cuddCof.pic.o Cudd/cudd/cuddGenetic.pic.o Cudd/cudd/cuddZddPort.pic.o Cudd/cudd/cuddMatMult.pic.o Cudd/cudd/cuddZddIsop.pic.o Cudd/cudd/cuddAPI.pic.o Cudd/cudd/cuddZddGroup.pic.o Cudd/cudd/cuddZddSymm.pic.o Cudd/cudd/cuddRef.pic.o Cudd/cudd/cuddZddMisc.pic.o Cudd/cudd/cuddDecomp.pic.o Cudd/cudd/cuddZddUtil.pic.o Cudd/cudd/cuddLiteral.pic.o Cudd/cudd/cuddAddNeg.pic.o Cudd/cudd/cuddPriority.pic.o Cudd/cudd/cuddAnneal.pic.o Cudd/cudd/cuddInit.pic.o Cudd/cudd/cuddZddSetop.pic.o Cudd/cudd/cuddReorder.pic.o Cudd/cudd/cuddSolve.pic.o Cudd/cudd/cuddBddCorr.pic.o Cudd/cudd/cuddAddFind.pic.o Cudd/cudd/cuddAddInv.pic.o Cudd/cudd/cuddWindow.pic.o Cudd/cudd/cuddAddIte.pic.o Cudd/cudd/cuddAddAbs.pic.o Cudd/cudd/cuddZddReord.pic.o Cudd/cudd/cuddBddAbs.pic.o Cudd/cudd/cuddBddIte.pic.o Cudd/cudd/cuddLinear.pic.o Cudd/cudd/cuddSign.pic.o Cudd/cudd/cuddCheck.pic.o Cudd/cudd/cuddZddCount.pic.o Cudd/cudd/cuddZddFuncs.pic.o Cudd/cudd/cuddEssent.pic.o Cudd/cudd/cuddGroup.pic.o Cudd/cudd/cuddSplit.pic.o Cudd/cudd/cuddSat.pic.o Cudd/cudd/cuddAddApply.pic.o Cudd/cudd/cuddLCache.pic.o Cudd/cudd/cuddCache.pic.o Cudd/cudd/cuddAndAbs.pic.o Cudd/cudd/cuddHarwell.pic.o Cudd/cudd/cuddBridge.pic.o Cudd/cudd/cuddUtil.pic.o Cudd/cudd/cuddExport.pic.o Cudd/cudd/cuddSubsetHB.pic.o Cudd/cudd/cuddAddWalsh.pic.o Cudd/cudd/cuddSymmetry.pic.o Cudd/cudd/cuddTable.pic.o Cudd/cudd/cuddApa.pic.o Cudd/cudd/cuddCompose.pic.o Cudd/cudd/cuddZddLin.pic.o Cudd/cudd/cuddExact.pic.o Cudd/cudd/cuddSubsetSP.pic.o Cudd/cudd/cuddGenCof.pic.o Cudd/cudd/cuddClip.pic.o Cudd/cudd/cuddInteract.pic.o Cudd/mtr/mtrBasic.pic.o Cudd/mtr/mtrGroup.pic.o Cudd/st/st.pic.o Cudd/epd/epd.pic.o -L/export/home/drkirkby/sage/tmp/sage-4.1.1/local/lib -L/export/home/drkirkby/sage/tmp/sage-4.1.1/local/lib/python2.6/config -Lpolybori -Lgroebner -LCudd -lm -lgd -lgd -lgd -lgd
build_symlink(["polybori/libpolybori-0.6.3.so.0"], ["polybori/libpolybori-0.6.3.so.0.0.0"])
Symlinking from libpolybori-0.6.3.so.0.0.0 to polybori/libpolybori-0.6.3.so.0
build_symlink(["polybori/libpolybori-0.6.3.so"], ["polybori/libpolybori-0.6.3.so.0"])
Symlinking from libpolybori-0.6.3.so.0 to polybori/libpolybori-0.6.3.so
build_symlink(["polybori/libpolybori.so"], ["polybori/libpolybori-0.6.3.so"])
Symlinking from libpolybori-0.6.3.so to polybori/libpolybori.so
build_symlink(["groebner/libgroebner-0.6.3.so.0"], ["groebner/libgroebner-0.6.3.so.0.0.0"])
Symlinking from libgroebner-0.6.3.so.0.0.0 to groebner/libgroebner-0.6.3.so.0
build_symlink(["groebner/libgroebner-0.6.3.so"], ["groebner/libgroebner-0.6.3.so.0"])
Symlinking from libgroebner-0.6.3.so.0 to groebner/libgroebner-0.6.3.so
build_symlink(["groebner/libgroebner.so"], ["groebner/libgroebner-0.6.3.so"])
Symlinking from libgroebner-0.6.3.so to groebner/libgroebner.so
build_symlink(["Cudd/libpboriCudd-0.6.3.so.0"], ["Cudd/libpboriCudd-0.6.3.so.0.0.0"])
Symlinking from libpboriCudd-0.6.3.so.0.0.0 to Cudd/libpboriCudd-0.6.3.so.0
build_symlink(["Cudd/libpboriCudd-0.6.3.so"], ["Cudd/libpboriCudd-0.6.3.so.0"])
Symlinking from libpboriCudd-0.6.3.so.0 to Cudd/libpboriCudd-0.6.3.so
build_symlink(["Cudd/libpboriCudd.so"], ["Cudd/libpboriCudd-0.6.3.so"])
Symlinking from libpboriCudd-0.6.3.so to Cudd/libpboriCudd.so
scons: done building targets.
Done build_polybori.
Installing PolyBoRi...
scons: Reading SConscript files ...
Sun linker detected.
Checking for C header file gd.h... (cached) yes
Checking for C library gd... (cached) yes
Checking for C++ header file unordered_map... (cached) no
Checking for C++ header file tr1/unordered_map... (cached) yes
Warning: No LaTeX to html converter found, Tutorial will not be installed
Checking for C library m4ri... (cached) no
Checking for C header file gd.h... (cached) yes
Checking for C library gd... (cached) yes
no python extension
setting umask to 022 (was 022)

scons: *** Error writing options to file: /export/home/drkirkby/sage/tmp/sage-4.1.1/local/share/polybori/flags.conf
[Errno 2] No such file or directory: '/export/home/drkirkby/sage/tmp/sage-4.1.1/local/share/polybori/flags.conf'
File "/export/home/drkirkby/sage/tmp/sage-4.1.1/spkg/build/polybori-0.6.3-20090825/src/polybori-0.6/SConstruct", line 1281, in <module>
Error installing PolyBoRi.

real    18m9.386s
user    16m29.417s
sys     1m23.875s
sage: An error occurred while installing polybori-0.6.3-20090825

```



---

Comment by PolyBoRi created at 2009-08-27 09:25:30

Patched the (patched) patch/SConstruct to fix the "flags.conf" issue


---

Attachment

Indeed, this is not a Solaris issue, but it will occur always, in the case, that PolyBoRi wasn't installed in the corresponding Sage before. Some patch from Sage adds the generation of `flags.conf`, but that goes wrong, if the installation directory does not exist before.  The flags-conf.patch above should fix the problem.

Regards,
  Alexander


---

Comment by PolyBoRi created at 2009-08-27 09:34:42

I would suggest to postpone the minor issues (duplicated arguments, missing, but not mandatory space) to the next release of PolyBoRi.

Alexander


---

Comment by malb created at 2009-08-27 09:51:24

Alright, the new SPKG deals with the flags.conf issue (thanks Alexander)

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3-20090827.spkg

I will postpone the fPIC issue for now and will concentrate on the pickling issue.


---

Attachment

fixes the pickling issue


---

Comment by malb created at 2009-08-27 10:35:43

The attached patch fixes the pickling issue and now all doctests pass on sage.math.


---

Attachment

minor fixes


---

Comment by burcin created at 2009-09-10 09:44:47

I added a patch with minor changes:

 - fix a doctest problem in `sage/crypto/mq/mpolynomialsystem.py`
 - eliminate use of Python `eval()` in `module_list.py`
 - remove commented code for which a newer version seems to be present somewhere else in the file

I give Martin's patch and the package a positive review. Martin, if you're ok with my changes, please mark this positive review.


Only attachment:polybori-0.6.3.3.patch and attachment:trac_6177_reviewer_patch should be applied, with the package linked from comment:54.


---

Comment by malb created at 2009-09-10 12:35:31

Burcin's patch looks good, applies cleanly against 4.1.2.alpha1 and doctests pass.

Its done, finally!


---

Comment by mvngu created at 2009-09-11 16:33:21

Merged patches in this order:

 1. `polybori-0.6.3.3.patch`
 1. `trac_6177_reviewer_patch`

Merged `polybori-0.6.3-20090827.spkg` in the standard packages repository.


---

Comment by mvngu created at 2009-09-11 16:33:21

Resolution: fixed


---

Attachment

repo corrupt-free version


---

Comment by mvngu created at 2009-09-21 03:43:27

with the ".patch" file extension


---

Attachment

I have attached two new patches

 1. `trac_6177-polybori-0.6.3.3.patch` --- This is the same as `polybori-0.6.3.3.patch`. The only change is inserting the comment 
 {{{
# Insert a comment here to prevent repo corruption.
 }}}
 into the empty file `sage/libs/polybori/__init__.py` in order to prevent repository corruption as was reported on IRC by William Stein:
 {{{
20:14 < williamstein> mvngu -- possible problem with alpha2
20:14 < williamstein> i get /scratch/wstein/build/sage-4.1.2.alpha3/devel/sage-main/sage/rings/polynomial/pbori.pxd:10:0: 'sage.libs.polybori.decl.pxd' not found
20:15 < williamstein> "repo corruption"?
20:15 < williamstein> yep
20:15 < williamstein> wstein`@`sage:~/build/sage-4.1.2.alpha3/devel/sage$ hg status
20:15 < williamstein> ! sage/libs/polybori/__init__.py
20:15 < williamstein> I fix it with:
20:15 < williamstein> wstein`@`sage:~/build/sage-4.1.2.alpha3/devel/sage$ hg revert --all
20:15 < williamstein> reverting sage/libs/polybori/__init__.py
20:16 < mvngu> williamstein: yeah, I just do "make" again.
20:16 < williamstein> mvngu -- that always bites you for some reason.
20:17 < mvngu> I have been experiencing that problem on every machine I'm building on.
20:17 < mvngu> It's always about polybori.
 }}}
 1. `trac_6177_reviewer.patch` --- This is the same as `trac_6177_reviewer_patch`. I put in the file extension ".patch" so that the patch would be displayed with colour on trac.


---

Comment by mvngu created at 2009-09-21 04:41:24

*Only merge these:*

 1. `trac_6177-polybori-0.6.3.3.patch`
 1. `trac_6177_reviewer.patch`


---

Comment by mvngu created at 2009-09-21 16:56:14

add files to MANIFEST.in


---

Attachment

The patch `trac_6177-manifest.patch` adds the following files to MANIFEST.in:

 * `sage/libs/polybori/__init__.py`
 * `sage/libs/polybori/decl.pxd`

This way, the files would be picked up when making a source release. By now, patches should be *merged in this order*:

 1. `trac_6177-polybori-0.6.3.3.patch`
 1. `trac_6177_reviewer.patch`
 1. `trac_6177-manifest.patch`
