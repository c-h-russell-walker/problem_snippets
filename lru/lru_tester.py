from lru import LruCache
from lru import CacheMiss


def test_lru():
    key_one = 'b12'
    key_two = 'sodium'
    key_three = 'fat'
    small_cache = LruCache(max_size=2)

    # Not in cache yet
    assert small_cache.get(key_one) is CacheMiss

    small_cache.add(key_one, 'vitamin')

    # Now in cache
    assert small_cache.get(key_one) == 'vitamin'

    small_cache.add(key_two, 'salty')

    # Still in cache
    assert small_cache.get(key_one) == 'vitamin'

    small_cache.add(key_three, 'avocado')

    # No longer in cache
    assert small_cache.get(key_one) is CacheMiss

    print('All tests passed.')


if __name__ == '__main__':
    test_lru()
