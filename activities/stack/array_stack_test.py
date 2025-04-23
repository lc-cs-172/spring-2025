from array_stack import ArrayStack

def test_empty():
    s = ArrayStack()
    assert s.is_empty()

def test_push_pop():
    s = ArrayStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert not s.is_empty()
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()

def test_polymorphic():
    s = ArrayStack()
    s.push('a')
    assert s.pop() == 'a'

def test_large():
    s = ArrayStack()
    for i in range(1000):
        s.push(i)
    for i in range(999, -1, -1):
        assert s.pop() == i
