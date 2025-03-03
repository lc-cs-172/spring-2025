"""Recursion exercises adapted from the CodingBat code practice web
pages https://codingbat.com/java/Recursion-1 developed by Nick
Parlante.
"""

import recursion2

def test_count_pairs():
    assert recursion2.count_pairs('axa') == 1
    assert recursion2.count_pairs('axax') == 2
    assert recursion2.count_pairs('axbx') == 1
    assert recursion2.count_pairs('hi') == 0
    assert recursion2.count_pairs('hihih') == 3
    assert recursion2.count_pairs('ihihhh') == 3
    assert recursion2.count_pairs('ihjxhh') == 0
    assert recursion2.count_pairs('') == 0
    assert recursion2.count_pairs('a') == 0
    assert recursion2.count_pairs('aa') == 0
    assert recursion2.count_pairs('aaa') == 1

def test_count_abc():
    assert recursion2.count_abc('abc') == 1
    assert recursion2.count_abc('abcxxabc') == 2
    assert recursion2.count_abc('abaxxaba') == 2
    assert recursion2.count_abc('ababc') == 2
    assert recursion2.count_abc('abxbc') == 0
    assert recursion2.count_abc('aaabc') == 1
    assert recursion2.count_abc('hello') == 0
    assert recursion2.count_abc('') == 0
    assert recursion2.count_abc('ab') == 0
    assert recursion2.count_abc('aba') == 1
    assert recursion2.count_abc('aca') == 0
    assert recursion2.count_abc('aaa') == 0

def test_count_11():
    assert recursion2.count_11('11abc11') == 2
    assert recursion2.count_11('abc11x11x11') == 3
    assert recursion2.count_11('111') == 1
    assert recursion2.count_11('1111') == 2
    assert recursion2.count_11('1') == 0
    assert recursion2.count_11('') == 0
    assert recursion2.count_11('hi') == 0
    assert recursion2.count_11('11x111x1111') == 4
    assert recursion2.count_11('1x111') == 1
    assert recursion2.count_11('1Hello1') == 0
    assert recursion2.count_11('Hello') == 0

def test_string_clean():
    assert recursion2.string_clean('yyzzza') == 'yza'
    assert recursion2.string_clean('abbbcdd') == 'abcd'
    assert recursion2.string_clean('Hello') == 'Helo'
    assert recursion2.string_clean('XXabcYY') == 'XabcY'
    assert recursion2.string_clean('112ab445') == '12ab45'
    assert recursion2.string_clean('Hello Bookkeeper') == 'Helo Bokeper'

def test_count_hi2():
    assert recursion2.count_hi2('ahixhi') == 1
    assert recursion2.count_hi2('ahibhi') == 2
    assert recursion2.count_hi2('xhixhi') == 0
    assert recursion2.count_hi2('hixhi') == 1
    assert recursion2.count_hi2('hixhhi') == 2
    assert recursion2.count_hi2('hihihi') == 3
    assert recursion2.count_hi2('hihihix') == 3
    assert recursion2.count_hi2('xhihihix') == 2
    assert recursion2.count_hi2('xxhi') == 0
    assert recursion2.count_hi2('hixxhi') == 1
    assert recursion2.count_hi2('hi') == 1
    assert recursion2.count_hi2('xxxx') == 0
    assert recursion2.count_hi2('h') == 0
    assert recursion2.count_hi2('x') == 0
    assert recursion2.count_hi2('') == 0
    assert recursion2.count_hi2('Hellohi') == 1

def test_paren_bit():
    assert recursion2.paren_bit('xyz(abc)123') == '(abc)'
    assert recursion2.paren_bit('x(hello)') == '(hello)'
    assert recursion2.paren_bit('(xy)1') == '(xy)'
    assert recursion2.paren_bit('not really (possible)') == '(possible)'
    assert recursion2.paren_bit('(abc)') == '(abc)'
    assert recursion2.paren_bit('(abc)xyz') == '(abc)'
    assert recursion2.paren_bit('(abc)x') == '(abc)'
    assert recursion2.paren_bit('(x)') == '(x)'
    assert recursion2.paren_bit('()') == '()'
    assert recursion2.paren_bit('res (ipsa) loquitor') == '(ipsa)'
    assert recursion2.paren_bit('hello(not really)there') == '(not really)'
    assert recursion2.paren_bit('ab(ab)ab') == '(ab)'

def test_nest_paren():
    assert recursion2.nest_paren('(())') == True
    assert recursion2.nest_paren('((()))') == True
    assert recursion2.nest_paren('(((x))') == False
    assert recursion2.nest_paren('((())') == False
    assert recursion2.nest_paren('((()()') == False
    assert recursion2.nest_paren('()') == True
    assert recursion2.nest_paren('') == True
    assert recursion2.nest_paren('(yy)') == False
    assert recursion2.nest_paren('(())') == True
    assert recursion2.nest_paren('(((y))') == False
    assert recursion2.nest_paren('((y)))') == False
    assert recursion2.nest_paren('((()))') == True
    assert recursion2.nest_paren('(())))') == False
    assert recursion2.nest_paren('((yy())))') == False
    assert recursion2.nest_paren('(((())))') == True

def test_str_count():
    assert recursion2.str_count('catcowcat', 'cat') == 2
    assert recursion2.str_count('catcowcat', 'cow') == 1
    assert recursion2.str_count('catcowcat', 'dog') == 0
    assert recursion2.str_count('cacatcowcat', 'cat') == 2
    assert recursion2.str_count('xyx', 'x') == 2
    assert recursion2.str_count('iiiijj', 'i') == 4
    assert recursion2.str_count('iiiijj', 'ii') == 2
    assert recursion2.str_count('iiiijj', 'iii') == 1
    assert recursion2.str_count('iiiijj', 'j') == 2
    assert recursion2.str_count('iiiijj', 'jj') == 1
    assert recursion2.str_count('aaabababab', 'ab') == 4
    assert recursion2.str_count('aaabababab', 'aa') == 1
    assert recursion2.str_count('aaabababab', 'a') == 6
    assert recursion2.str_count('aaabababab', 'b') == 4

def test_str_copies():
    assert recursion2.str_copies('catcowcat', 'cat', 2) == True
    assert recursion2.str_copies('catcowcat', 'cow', 2) == False
    assert recursion2.str_copies('catcowcat', 'cow', 1) == True
    assert recursion2.str_copies('iiijjj', 'i', 3) == True
    assert recursion2.str_copies('iiijjj', 'i', 4) == False
    assert recursion2.str_copies('iiijjj', 'ii', 2) == True
    assert recursion2.str_copies('iiijjj', 'ii', 3) == False
    assert recursion2.str_copies('iiijjj', 'x', 3) == False
    assert recursion2.str_copies('iiijjj', 'x', 0) == True
    assert recursion2.str_copies('iiiiij', 'iii', 3) == True
    assert recursion2.str_copies('iiiiij', 'iii', 4) == False
    assert recursion2.str_copies('ijiiiiij', 'iiii', 2) == True
    assert recursion2.str_copies('ijiiiiij', 'iiii', 3) == False
    assert recursion2.str_copies('dogcatdogcat', 'dog', 2) == True

def test_str_dist():
    assert recursion2.str_dist('catcowcat', 'cat') == 9
    assert recursion2.str_dist('catcowcat', 'cow') == 3
    assert recursion2.str_dist('cccatcowcatxx', 'cat') == 9
    assert recursion2.str_dist('abccatcowcatcatxyz', 'cat') == 12
    assert recursion2.str_dist('xyx', 'x') == 3
    assert recursion2.str_dist('xyx', 'y') == 1
    assert recursion2.str_dist('xyx', 'z') == 0
    assert recursion2.str_dist('z', 'z') == 1
    assert recursion2.str_dist('x', 'z') == 0
    assert recursion2.str_dist('', 'z') == 0
    assert recursion2.str_dist('hiHellohihihi', 'hi') == 13
    assert recursion2.str_dist('hiHellohihihi', 'hih') == 5
    assert recursion2.str_dist('hiHellohihihi', 'o') == 1
    assert recursion2.str_dist('hiHellohihihi', 'll') == 2
