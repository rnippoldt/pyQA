from src.myRandom import myRandom


def test_myrandom():
    x = 10

    assert myRandom.zero_to_max(x) <= x

    for num in range(10 + 1):
        randnum = myRandom.zero_to_max(num)
        assert randnum <= x
        # print(num, ':', randnum)