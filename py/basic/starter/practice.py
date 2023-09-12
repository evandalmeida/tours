def sum_odds(l: list[int]) -> int:
    """
    Returns the sum of all of the odd numbers of a list
    [1,2,3,4,5] -->
    9
    """
    pass


print("sum_odds")
# print(sum_odds([1,2,3,4,5]))


def list_of_squares(n: int) -> list[int]:
    """
    Returns a list of square numbers from 1 to n (inclusive)
    n = 5 -->
    [1,4,9,16,25]
    """
    pass


print("list_of_squares")
# print(list_of_squares(5))


def count_letter(string: str, letter: str) -> int:
    """
       Returns the number of times the given letter occurs in
       the string
    """
    assert len(letter) == 1, "letter parameter should be a string of length 1"
    pass


print("count_letter")
# print(count_letter('Computers are good at following instructions, but not at reading your mind.', 'o'))


def swap_min_max(l: list[int]) -> list[int]:
    """
    Given a list of unique numbers, swap the positions
    of the smallest and largest elements
    [1,2,3,4] -->
    [4,2,3,1]
    """
    pass


print("swap_min_max")
# print(swap_min_max([5,2,7,8,4,9]))

authors: list[dict] = [
    {"id": 2, "name": "author 2"},
    {"id": 1, "name": "author 1"},
    {"id": 3, "name": "author 3"},
]

posts: list[dict] = [
    {"id": 1, "content": "post 1 by author 1", "year": 2014, "author_id": 1},
    {"id": 2, "content": "post 2 by author 1", "year": 2015, "author_id": 1},
    {"id": 3, "content": "post 1 by author 2", "year": 2008, "author_id": 2},
    {"id": 4, "content": "post 2 by author 2", "year": 2015, "author_id": 2},
]


def get_author_by_id(id: int) -> dict:
    """
    Returns the author dictionary that contains the id parameter
    """
    pass


print("get_author_by_id")
# print(get_author_by_id(2))


def get_authors_that_posted_in_year(year: int) -> list[dict]:
    """
    Returns a list of author dicts who posted in a given year
    (hint: you'll need to traverse the posts list first, then
    traverse the authors list)
    """
    pass


print("get_authors_that_posted_in_year")
# print(get_authors_that_posted_in_year(2015))
