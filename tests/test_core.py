from mathquiz.core import Question

def test_question():
    q = Question(4, 2, '+', 0)
    assert q.answer() == 6
    q = Question(4.1234, 2.5678, '+', 2)
    assert abs(q.answer() - round(4.12 + 2.57, 2)) < 0.01