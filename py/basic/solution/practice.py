def sum_odds(l: list[int]) -> int:
    """
    Returns the sum of all of the odd numbers of a list
    [1,2,3,4,5] -->
    9
    """
    # total = sum([num for num in l if num % 2 == 1])
    total: int = 0
    for num in l:
        if num % 2 == 1:
            total = total + num
    
    return total


print("sum_odds")
print(sum_odds([1,2,3,4,5]))


def list_of_squares(n: int) -> list[int]:
    """
    Returns a list of square numbers from 1 to n (inclusive)
    n = 5 -->
    [1,4,9,16,25]
    """
    # result = [num**2 for num in range(1, n+1)]
    result = []
    for num in range(1,n+1):
        result.append(num**2)
    
    return result


print("list_of_squares")
print(list_of_squares(5))


def count_letter(string: str, letter: str) -> int:
    """
       Returns the number of times the given letter occurs in
       the string
    """
    assert len(letter) == 1, "letter parameter should be a string of length 1"
    count = 0
    for char in string:
        if char == letter:
            #count = count + 1
            count += 1
    return count


print("count_letters")
print(count_letter('Computers are good at following instructions, but not at reading your mind.', 'o'))


def swap_min_max(l: list[int]) -> list[int]:
    """
    Given a list of unique numbers, swap the positions
    of the smallest and largest elements
    [1,2,3,4] -->
    [4,2,3,1]
    """
    # get the minimum and maximum numbers
    max_num = max(l)
    min_num = min(l)

    # get the indices of the min and max numbers
    index_of_max = l.index(max_num)
    index_of_min = l.index(min_num)

    # set the element at the index of the max number to the min number 
    l[index_of_max] = min_num

    # set the element at the index of the min number to the max number 
    l[index_of_min] = max_num
    return l


print("swap_min_max")
print(swap_min_max([5,2,7,8,4,9]))

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
    for a in authors:
        author_id = a['id']
        if id == author_id:
            return a


print("get_author_by_id")
print(get_author_by_id(2))


def get_authors_that_posted_in_year(year: int) -> list[dict]:
    """
    Returns a list of author dicts who posted in a given year
    (hint: you'll need to traverse the posts list first, then
    traverse the authors list)
    """
    author_id_list = []
    for p in posts:
        if p['year'] == year:
            author_id_list.append(p['author_id'])
    author_dict_list = []

    for a in authors:
        if a['id'] in author_id_list:
            author_dict_list.append(a)
    return author_dict_list 


print("get_authors_that_posted_in_year")
print(get_authors_that_posted_in_year(2015))
