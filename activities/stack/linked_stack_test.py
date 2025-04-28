from linked_stack import LinkedStack

def test_empty():
    s = LinkedStack()
    assert s.is_empty()

def test_push_pop():
    s = LinkedStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert not s.is_empty()
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()

def test_polymorphic():
    s = LinkedStack()
    s.push('a')
    assert s.pop() == 'a'
