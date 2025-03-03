import recursion1

def test_factorial():
    assert recursion1.factorial(1) == 1
    assert recursion1.factorial(2) == 2
    assert recursion1.factorial(3) == 6
    assert recursion1.factorial(4) == 24
    assert recursion1.factorial(5) == 120
    assert recursion1.factorial(6) == 720
    assert recursion1.factorial(7) == 5040
    assert recursion1.factorial(8) == 40320
    assert recursion1.factorial(12) == 479001600

def test_bunny_ears():
    assert recursion1.bunny_ears(1) == 2
    assert recursion1.bunny_ears(2) == 4
    assert recursion1.bunny_ears(3) == 6
    assert recursion1.bunny_ears(4) == 8
    assert recursion1.bunny_ears(5) == 10
    assert recursion1.bunny_ears(12) == 24
    assert recursion1.bunny_ears(50) == 100
    assert recursion1.bunny_ears(234) == 468

def test_fibonacci():
    assert recursion1.fibonacci(0) == 0
    assert recursion1.fibonacci(1) == 1
    assert recursion1.fibonacci(2) == 1
    assert recursion1.fibonacci(3) == 2
    assert recursion1.fibonacci(4) == 3
    assert recursion1.fibonacci(5) == 5
    assert recursion1.fibonacci(6) == 8
    assert recursion1.fibonacci(7) == 13	

def test_bunny_ears2():
    assert recursion1.bunny_ears2(0) == 0
    assert recursion1.bunny_ears2(1) == 2
    assert recursion1.bunny_ears2(2) == 5
    assert recursion1.bunny_ears2(3) == 7
    assert recursion1.bunny_ears2(4) == 10
    assert recursion1.bunny_ears2(5) == 12
    assert recursion1.bunny_ears2(6) == 15
    assert recursion1.bunny_ears2(10) == 25

def test_triangle():
    assert recursion1.triangle(0) == 0
    assert recursion1.triangle(1) == 1
    assert recursion1.triangle(2) == 3
    assert recursion1.triangle(3) == 6
    assert recursion1.triangle(4) == 10
    assert recursion1.triangle(5) == 15
    assert recursion1.triangle(6) == 21
    assert recursion1.triangle(7) == 28

def test_sum_digits():
    assert recursion1.sum_digits(126) == 9
    assert recursion1.sum_digits(49) == 13
    assert recursion1.sum_digits(12) == 3
    assert recursion1.sum_digits(10) == 1
    assert recursion1.sum_digits(1) == 1
    assert recursion1.sum_digits(0) == 0
    assert recursion1.sum_digits(730) == 10
    assert recursion1.sum_digits(1111) == 4
    assert recursion1.sum_digits(11111) == 5
    assert recursion1.sum_digits(10110) == 3
    assert recursion1.sum_digits(235) == 10

def test_count_7():
    assert recursion1.count_7(717) == 2
    assert recursion1.count_7(7) == 1
    assert recursion1.count_7(123) == 0
    assert recursion1.count_7(77) == 2
    assert recursion1.count_7(7123) == 1
    assert recursion1.count_7(771237) == 3
    assert recursion1.count_7(771737) == 4
    assert recursion1.count_7(47571) == 2
    assert recursion1.count_7(777777) == 6
    assert recursion1.count_7(70701277) == 4
    assert recursion1.count_7(777576197) == 5
    assert recursion1.count_7(99999) == 0
    assert recursion1.count_7(99799) == 1

def test_power_n():
    assert recursion1.power_n(3, 1) == 3
    assert recursion1.power_n(3, 2) == 9
    assert recursion1.power_n(3, 3) == 27
    assert recursion1.power_n(2, 1) == 2
    assert recursion1.power_n(2, 2) == 4
    assert recursion1.power_n(2, 3) == 8
    assert recursion1.power_n(2, 4) == 16
    assert recursion1.power_n(2, 5) == 32
    assert recursion1.power_n(10, 1) == 10
    assert recursion1.power_n(10, 2) == 100
    assert recursion1.power_n(10, 3) == 1000

def test_change_xy():
    assert recursion1.change_xy('codex') == 'codey'
    assert recursion1.change_xy('xxhixx') == 'yyhiyy'
    assert recursion1.change_xy('xhixhix') == 'yhiyhiy'
    assert recursion1.change_xy('hiy') == 'hiy'
    assert recursion1.change_xy('h') == 'h'
    assert recursion1.change_xy('x') == 'y'
    assert recursion1.change_xy('') == ''
    assert recursion1.change_xy('xxx') == 'yyy'
    assert recursion1.change_xy('yyhxyi') == 'yyhyyi'
    assert recursion1.change_xy('hihi') == 'hihi'

def test_no_x():
    assert recursion1.no_x('xaxb') == 'ab'
    assert recursion1.no_x('abc') == 'abc'
    assert recursion1.no_x('xx') == ''
    assert recursion1.no_x('') == ''
    assert recursion1.no_x('axxbxx') == 'ab'
    assert recursion1.no_x('Hellox') == 'Hello'

def test_array_6():
    assert recursion1.array_6([1, 6, 4]) == True
    assert recursion1.array_6([1, 4]) == False
    assert recursion1.array_6([6]) == True
    assert recursion1.array_6([]) == False
    assert recursion1.array_6([6, 2, 2]) == True
    assert recursion1.array_6([2, 5]) == False
    assert recursion1.array_6([1, 9, 4, 6, 6]) == True
    assert recursion1.array_6([2, 5, 6]) == True

def test_array_220():
    assert recursion1.array_220([1, 2, 20]) == True
    assert recursion1.array_220([3, 30]) == True
    assert recursion1.array_220([3]) == False
    assert recursion1.array_220([]) == False
    assert recursion1.array_220([3, 3, 30, 4]) == True
    assert recursion1.array_220([2, 19, 4]) == False
    assert recursion1.array_220([20, 2, 21]) == False
    assert recursion1.array_220([20, 2, 21, 210]) == True
    assert recursion1.array_220([2, 200, 2000]) == True
    assert recursion1.array_220([0, 0]) == True
    assert recursion1.array_220([1, 2, 3, 4, 5, 6]) == False
    assert recursion1.array_220([1, 2, 3, 4, 5, 50, 6]) == True
    assert recursion1.array_220([1, 2, 3, 4, 5, 51, 6]) == False
    assert recursion1.array_220([1, 2, 3, 4, 4, 50, 500, 6]) == True

def test_all_star():
    assert recursion1.all_star('hello') == 'h*e*l*l*o'
    assert recursion1.all_star('abc') == 'a*b*c'
    assert recursion1.all_star('ab') == 'a*b'
    assert recursion1.all_star('a') == 'a'
    assert recursion1.all_star('') == ''
    assert recursion1.all_star('3.14') == '3*.*1*4'
    assert recursion1.all_star('Chocolate') == 'C*h*o*c*o*l*a*t*e'
    assert recursion1.all_star('1234') == '1*2*3*4'

def test_pair_star():
    assert recursion1.pair_star('hello') == 'hel*lo'
    assert recursion1.pair_star('xxyy') == 'x*xy*y'
    assert recursion1.pair_star('aaaa') == 'a*a*a*a'
    assert recursion1.pair_star('aaab') == 'a*a*ab'
    assert recursion1.pair_star('aa') == 'a*a'
    assert recursion1.pair_star('a') == 'a'
    assert recursion1.pair_star('') == ''
    assert recursion1.pair_star('noadjacent') == 'noadjacent'
    assert recursion1.pair_star('abba') == 'ab*ba'
    assert recursion1.pair_star('abbba') == 'ab*b*ba'
