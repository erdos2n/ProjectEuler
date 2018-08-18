import used_functions as uf

def test_sum_divisors():
    n = 12
    expected = 16
    predicted = uf.sum_divisors(n=12)
    print(expected)
    print(predicted)
    assert expected == predicted