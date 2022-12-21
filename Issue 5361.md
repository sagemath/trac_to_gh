# Issue 5361: problems in the sage.rings conversion

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-02-24 18:24:41

Assignee: tba

These are problems I reported in #4925 that did not get fixed in the first go-round:

```
I'm working mostly from the patch source, but occasionally also checking the rendered result, at 
http://sage.math.washington.edu/home/mhansen/sage/devel/sage-old/doc/output/html/en/reference/sage/rings/...
(references to the rendered output refer to this particular version as 
of 2009-01-19)

========== arith.py

the docstring for bernoulli screwed up the INPUT list: "algorithm:" is
the name of an input, and 'default' through 'bernmm' are possible
values for that input

The docstring for bernoulli (in the case 'default') lost a '<' and a
'>' (one each)

in the docstring for bernoulli, the indentation of the tests in TESTS is bad:
three tests are indented relative to the others

in the docstring for bernoulli, it changes a "\note{...}" to 
".. note:", but the result seems not to show up in the formatted manual at all

in the docstring for factorial (INPUT section), 'gmp' and 'pari' are
possible values for algorithm, not separate arguments

in the docstring for is_prime (INPUT section), 0, 1, and 2 should be a
bulleted sublist of the ``flag`` item

in the docstring for is_pseudoprime (INPUT section), 0 and "> 0" should be 
a sublist of ``flag``.  (And the '>' is missing from "> 0".)

in the docstring for is_prime_power (INPUT section), 0, 1, and 2
should be subitems

docstring for previous_prime is missing two '<'

docstring for random_prime is missing two '<' (in the summary section)
and one '>' (in INPUT section)

docstring for xlcm is missing two '|' (in the summary section)

docstring for rational_reconstruction is missing four '<' (one in summary,
one in output section, two in algorithm discussion)

docstring for rational_reconstruction has mangled input section
(should be nested lists, not a single paragraph); output section
should be separate from input section

docstring for mqrr_rational_reconstruction has mangled input/output sections
(should be separate sections, not a single paragraph); input/output section
missing lots of '<' and '>'

trial_division docstring is missing two '<' (one in summary, one in
output section)

trial_division docstring INPUT section is mangled: should have two
items (``n`` and ``bound``)

odd_part docstring lost the "\code{...}" wrapper from $v =
\code{valuation(n,2)}$

is_squarefree docstring is missing '>'

Euler_phi docstring is missing two '<'

kronecker_symbol docstring is missing '|'

legendre_symbol docstring is missing '|'

hilbert_symbol INPUT section: 'pari', 'direct', 'all' should be subitems of
``algorithm``

falling_factorial, rising_factorial INPUT sections: I like the
previous location of the "or"; can we do something to make it more
clear that it's either the first two items or the third item?

========== complex_double.pyx

docstring of method gen: the word "EXAMPLES::" should be on a separate line 
from the summary

docstring of __pow__: "We raise to symbolic powers" section: indentation
of examples is inconsistent

========== complex_number.pyx

docstring of __getitem__: INPUT section is mangled (i=0, i=1 should be a 
sublist, EXAMPLES should be a separate section)

docstring of str: INPUTS section is mangled: should be a list

docstring of __rdiv__: INPUTS section is mangled: should be a list

docstring of eta: EXAMPLES section: "First we compute..." should be a separate
paragraph from the word EXAMPLES

docstring of dilog: "EXAMPLES:" should be a paragraph of its own, not part of
the summary

docstring of log: missing two '<'

docstring of create_ComplexNumber: missing '>' (INPUT section, under ``pad``)

========== finite_field.py

docstring of class FiniteFieldFactory: missing '<' 
(INPUT section, under ``elem_cache``)

========== finite_field_element.py

docstring of polynomial: "EXAMPLES:" should be a paragraph of its own,
not joined with "The default variable is a::"

========== fraction_field.py

AUTHOR section of file docstring: the patch adds Burcin Erocal as an
author.

========== homset.py

"TEST: We test pickling of a homset..." should be two separate paragraphs

========== ideal.py

many docstrings: the word "EXAMPLES:" should be a separate paragraph,
not joined with the next paragraph (same for TESTS:)

========== infinity.py

EXAMPLES: should be separate paragraph, not merged with next paragraph

========== integer.pyx

On the second line of the file, m`\mathbb{Z}` has an extra 'm'

in AUTHORS section, Didier's email address was removed

_digits_internal method: "Parameters:" should become "INPUT:", and should
have a list instead of a muddled paragraph.  Also, this section is missing
two '<' under power_index

__pow__: missing '^' in 
"For consistency with Python and MPFR, 00 is defined to be 1 in"

nth_root: missing '>' in INPUT section, under ``n``

exact_root: missing '>' in INPUT section

is_prime_power: INPUT section: 0, 1, 2 should be sublist of ``flag``
```



---

Comment by mhansen created at 2009-02-28 04:20:13

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-02-28 04:20:13

Changing assignee from tba to mhansen.


---

Comment by mabshoff created at 2009-03-02 03:10:14

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 03:39:40

Resolution: fixed


---

Comment by mabshoff created at 2009-03-02 03:39:40

Merged in Sage 3.4.rc0.

Cheers,

Michael
