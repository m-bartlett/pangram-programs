# Pangram Programs
This is a collection of hololexical, symbol-exhaustive, and/or language-feature saturated codes implemented in various languages. This is where programming languages, semantic completionism, and maybe even a hint of poetry converge.

Source code contributed to this repository should be what ["The quick brown fox jumped over the lazy dog."](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog) is to English. For the uninitiated, this is a "pangram" and uses all 26 alphabetical English letter at least once.  But, what of English's operators? It features quite puncuation marks! Here is a punctional equivalent pangram for english:
>While he was writing his book, Magic: the Tittle Known World! he stated, “I always… wanted to ask a magishin [sic], ‘How do you do it?’”; he luckily got the chance while he was living above a shop (where he lived from 1993 — 1997).

<sub>_Slightly modified [this original version.](https://www.quora.com/What-is-the-English-Sentence-which-contains-all-14-punctuation-marks)_</sub>

Now imagine trying to use every letter and punctuation mark in as short of prose as possible--quite a poetic challenge. And similarly, what's the shortest grammatically valid prose that uses all English words? Such a problem is a bit nebulous, but luckily we have languages which are unambiguous where such a solution is likely to exist: those which are computed.

In essence, code here should be thought of as such a "grand touer" of its respective language. Specifically, this may manifest as a script that uses all reserved words and functional operators in the language, every parsible symbol, every block structure--this list goes on.

For the practically inclined, think of codes here as a demonstrative cheatsheet. Rather than a list of all functions and keywords, why not show their usage comprehensively in one piece of code? The challenge is what you make it

The only requirement is that some aspect of the laguage the code should be executed with is comprehensively represented.

An example, here is Python's reserved words:
```python
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
Perhaps try to write a python script which uses all of these.
And don't forget all their operator friends: `+ - * / % ** // = += -= *= /= %= //= **= &= |= ^= >>= <<= == != > < >= <= & | ^ ~ << >>`
