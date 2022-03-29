import Prime
import pytest

@pytest.mark.parametrize("num,output",[(3,True),(10,False)])
def test_prime(num,output):
    r = Prime.prime(num)
    assert r==output

@pytest.mark.skip
def test_notPrime():
    x=25
    r = Prime.prime(x)
    assert r==False

@pytest.mark.parametrize("num,output",[(12321,True),(1234,False)])
def test_palindrome(num,output):
    r = Prime.palindrome(num)
    assert r == output
