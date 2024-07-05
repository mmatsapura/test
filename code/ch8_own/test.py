import pytest


#def test_string_input(stringinput):
 #   assert stringinput.isalpha()



@pytest.mark.parametrize('test_eval, expected',[('5+8',13),('7*8', 56),('-1-0',-1), pytest.param('6*9', 11, marks=pytest.mark.xfail)])
def test_eval_func(test_eval, expected):
    assert eval(test_eval) == expected

class TestClasses:
    def test_simple_implemintation(self, test_eval, expected):
        assert eval(test_eval) == expected

    def test_weird_implementation(self, test_eval, expected):
        assert eval(test_eval) == 1 * expected - 2 + 2
