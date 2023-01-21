# Please run each problem's code separately.


# Problem 1
# Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։
# Տրված n֊ի համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։


def math_prog_elem(a1, a2, k):
    diff = a2 - a1
    return a1 + (k-1)*diff


print(math_prog_elem(1, 5, 3))
print(math_prog_elem(2.5, 3, 5))


# Problem 2
# CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների չեկը
# և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների ընդհանուր թիվը:
# Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր,
# որը կամփոփի բոլոր թվերը, որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում հայտնված թվերի գումարը։


def ratiorg_sum(s):
    word_l = s.split()
    result = 0
    for elem in word_l:
        if elem.isdigit():
            result += int(elem)
    return result


print(ratiorg_sum("2 apples, 12 oranges"))


# Problem 3
# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
# ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ դեփքում:


# We can replace the return call by a print function if we want is_sorted to print every time.
def is_sorted(a1, a2, a3):
    if a1 <= a2 <= a3 or a1 >= a2 >= a3:
        return "Sorted"
        # print("Sorted")
        # return
    return "Unsorted"
    # print("Unsorted")
    # return


print(is_sorted(1, 2, 3))
print(is_sorted(1, 3, 2))
print(is_sorted(5, 0, -4))


# Problem 4
# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն կատարյալ թիվ է, թե ոչ։
# Հ․Գ Թիվը կոչվում է կատարյալ, եթե այն հավասար է իր բաժանարարների գումարին։


def is_perfect(n):
    dev_sum = 0
    for i in range(1, n):
        if n % i == 0:
            dev_sum += i
    if dev_sum == n:
        return True
    return False


print(is_perfect(6))
print(is_perfect(12))


# Problem 5
# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա էլեմենտների գումարը։


def list_sum(l):
    if len(l) == 0:
        return
    result = 0
    for elem in l:
        result += elem
    return result


print(list_sum([26, 867, 46, 985, 75]))
print(sum([26, 867, 46, 985, 75]))


# Problem 6
# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ ցուցակի ամենամեծ էլեմենտը։


def max_elem(l):
    if len(l) == 0:
        return
    maximum = l[0]
    for elem in l:
        if elem > maximum:
            maximum = elem
    return maximum


print(max_elem([26, 867, 46, 985, 75]))
print(max([26, 867, 46, 985, 75]))


# Problem 7
# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր էլեմենտները։


def remove_from_list(l, a):
    n = l.count(a)
    for i in range(n):
        l.remove(a)
    return l


print(remove_from_list([7, 1, 5, 8, 7, 9, 7], 7))


# Problem 8
# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր էլեմենտների արտադրյալը։


def multiplier(l):
    result = 1
    for elem in l:
        result *= elem
    return result


print(multiplier([1, 6, 8, 4, 5]))
print(1*6*8*4*5)


# Problem 9
# Գրեք  ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի բազմապատիկ է։


def reverser(s):
    return s[::-1]


print(reverser("jakfakjaf324JIO2398DJ"))


# Problem 10
# Գրեք  ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ անդամը։
# Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։


def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_iter(n):
    a1, a2 = 1, 1
    for i in range(n):
        a1, a2 = a2, a1 + a2
    return a1


# Runs in log(n)
def fib_fast(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        k = n//2 + 1
        a = fib_fast(k)
        b = fib_fast(n-k)
        c = fib_fast(k-1)
        d = fib_fast(n-k+1)
        return a*b + c*(d-b)


print(fib_rec(10))
print(fib_iter(10))
print(fib_fast(10))


# Problem 11
# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց ամենափոքր ընդհանուր բազմապատիկը։


def least_common_mult(a, b):
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            return i


print(least_common_mult(255, 15))


# Problem 12
# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:


def next_palindrome(n):
    k = n
    while True:
        k += 1
        if str(k) == str(k)[::-1]:
            return k


print(next_palindrome(119))


# Problem 13
# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0, Y0):
# Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման հրամաններ:
# Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման ստանալուց հետո
# ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե ռոբոտը սխալ հրաման է ստանում,
# նա պարզապես անտեսում է այն: Որտե՞ղ է գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
# Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։


def final_coordinates(l):
    x = 0
    y = 0
    for elem in l:
        if elem == "Right":
            x += 1
        elif elem == "Left":
            x -= 1
        elif elem == "Up":
            y += 1
        elif elem == "Down":
            y -= 1
    return x, y


# Also included a wrong command to see if it will be ignored or cause an error
print(final_coordinates(["Right", "Right", "Up", "Left", "Down", "sdg", "Up"]))


# Problem 14
# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ  ցիկլիկ են:


def is_one_cyclic(l1, l2):
    if len(l1) != len(l2):
        return False
    cyclic_right = True
    for i in range(len(l1)):
        if l1[i] != l2[i-1]:
            cyclic_right = False
    cyclic_left = True
    for i in range(len(l1)):
        if l2[i] != l1[i-1]:
            cyclic_left = False
    return cyclic_right or cyclic_left


print(is_one_cyclic([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 4, 5]))


# Problem 15
# Գրել ծրագիր,  որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝ ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:


def largest_subnumber(n):
    n_str = str(n)
    sub_list = []
    for i in range(len(n_str)):
        sub = n_str[:i] + n_str[i+1:]
        sub_list.append(int(sub))
    return max(sub_list)


print(largest_subnumber(152))
print(largest_subnumber(1001))


# Problem 16
# Գրեք  ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple բաղկացած միայն առաջին tuple֊ի թվերից։


import random


def tuplemaker(t):
    tuple_list = []
    new_length = random.randint(0, len(t)-1)
    for i in range(new_length):
        elem_position = random.randint(0, len(t)-1)
        tuple_list.append(t[elem_position])
    return tuple(tuple_list)


print(tuplemaker((3, 7, 20, 25, 65, 1)))


# Problem 17
# Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում է ստացած արժեքը tuple մեջ։


def tuple_append(t, a):
    t_list = list(t)
    t_list.append(a)
    return tuple(t_list)


print(tuple_append((3, 7, 20, 25, 65, 1), 100))


# Problem 18
# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։
# Tuplex֊ի էլեմենտները ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։


def tuplex(t):
    result = ""
    for elem in t:
        result += "-" + str(elem)
    return result[1:]


print(tuplex((3, 7, 20, "World", 25, 65, 1, "Hello")))


# Problem 19
# Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց len() ֆունկցիա֊ի օգտագորձմամբ։


def length_list(l):
    counter = 0
    for elem in l:
        counter += 1
    return counter


print(length_list([1, 5, 7, 3, "Hello", 9, 10, "World"]))


# Problem 20
# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half of the digits
# is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not.
# Not using: string, list, tuple, set types.


def is_lucky(n):
    k = n
    digit_sum = 0
    length = 0
    while k != 0:
        digit_sum += k % 10
        k = k // 10
        length += 1
    midpoint = int(length/2)
    half = 0
    k = n
    for _ in range(midpoint):
        half += k % 10
        k = k // 10
    return half == digit_sum/2


print(is_lucky(1230))
print(is_lucky(239017))


# Problem 21
# Euler function is return a count of numbers not great than N, which are mutualy simple with N.
# Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6.
# Write a function which return count of numbers mutually simple with given N.


def is_mutually_simple(a, b):
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def euler_function(n):
    counter = 0
    for i in range(1, n):
        if is_mutually_simple(i, n):
            counter += 1
    return counter


print(euler_function(6))


# Problem 22
# You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
# In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams,
# and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies
# the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for each
# operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all
# the original letters exactly once. For example, "dacb" is an anagram of "abdc".
# Example:
# Input: words = ["abba","baba","bbaa","cd","cd"]
# Output: ["abba","cd"]
# Explanation:
# One of the ways we can obtain the resultant array is by using the following operations:
# - Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
#    Now words = ["abba","baba","cd","cd"].
# - Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
#    Now words = ["abba","cd","cd"].
# - Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
#    Now words = ["abba","cd"].
# We can no longer perform any operations, so ["abba","cd"] is the final answer.
# Example 2:
# Input: words = ["a","b","c","d","e"]
# Output: ["a","b","c","d","e"]
# Explanation:
# No two adjacent strings in words are anagrams of each other, so no operations are performed.
# Constraints:
# 1) 1 <= words.length <= 100
# 2) 1 <= words[i].length <= 10
# 3) words[i] consists of lowercase English letters.


def is_anagram(a, b):
    b_list = list(b)
    for char in a:
        if char not in b_list:
            return False
        b_list.remove(char)
    if not b_list:
        return True
    return False


def delete_anagrams(l):
    i = 1
    while len(l) > i:
        if is_anagram(l[i-1], l[i]):
            l.pop(i)
        i += 1
    return l


word1 = ["abba", "baba", "bbaa", "cd", "cd"]
word2 = ["a", "b", "c", "d", "e"]
print(delete_anagrams(word1))
print(delete_anagrams(word2))


# Problem 23
# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n. For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.
# Example 1:
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
# Constraints:
# 1)  n == names.length == heights.length
# 2) 1 <= n <= 10^3
# 3) 1 <= names[i].length <= 20
# 4) 1 <= heights[i] <= 10^5
# 5) names[i] consists of lower and upper case English letters.
# 6) All the values of heights are distinct.


def height_sort(names, heights):
    heights_dict = {}
    for i in range(len(names)):
        heights_dict[heights[i]] = names[i]
    sorted_heights = sorted(heights, reverse=True)
    sorted_names = []
    for elem in sorted_heights:
        sorted_names.append(heights_dict[elem])
    return sorted_names


print(height_sort(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(height_sort(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))


# Problem 24
# In a special ranking system, each voter gives a rank from highest to lowest to all teams participating
# in the competition. The ordering of teams is decided by who received the most position-one votes.
# If two or more teams tie in the first position, we consider the second position to resolve the conflict,
# if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied
# after considering all positions, we rank them alphabetically based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking systems.
# Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.
# Example 1:
# Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
# Output: "ACB"
# Explanation:
# Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
# Team B was ranked second by 2 voters and ranked third by 3 voters.
# Team C was ranked second by 3 voters and ranked third by 2 voters.
# As most of the voters ranked C second, team C is the second team, and team B is the third.
#
# Example 2:
# Input: votes = ["WXYZ","XYZW"]
# Output: "XWYZ"
# Explanation:
# X is the winner due to the tie-breaking rule. X has the same votes as W for the first position,
# but X has one vote in the second position, while W does not have any votes in the second position.
# Example 3:
# Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
# Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
# Explanation: Only one voter, so their votes are used for the ranking.
# Constraints:
# 1) 1 <= votes.length <= 1000
# 2) 1 <= votes[i].length <= 26
# 3) votes[i].length == votes[j].length for 0 <= i, j < votes.length.
# 4) votes[i][j] is an English uppercase letter.
# 5) All characters of votes[i] are unique.
# 6) All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.


def who_takes_pos(dict, pos):
    dict_new = dict.copy()
    teams_list = list(dict_new.keys())
    teams_list = sorted(teams_list)
    votes_list = []
    for team in teams_list:
        votes_list.append(dict_new[team][pos])
    max_votes = max(votes_list)
    for team in teams_list:
        if dict_new[team][pos] != max_votes:
            dict_new.pop(team)
    if len(dict_new) == 1:
        return list(dict_new.keys())[0]
    elif pos == len(dict_new[teams_list[0]]):
        return list(dict_new.keys())[0]
    else:
        return who_takes_pos(dict_new, pos+1)


def ranking(votes):
    votes_dict = {}
    ranks = len(votes[0])
    empty_ranks = {}
    for i in range(1, ranks+1):
        empty_ranks[i] = 0
    for team in votes[0]:
        votes_dict[team] = empty_ranks.copy()
    for vote in votes:
        for pos, team in enumerate(vote):
            votes_dict[team][pos+1] += 1
    result = ""
    for _ in range(1, ranks+1):
        stage_winner = who_takes_pos(votes_dict, 1)
        result += stage_winner
        votes_dict.pop(stage_winner)
    return result


print(ranking(["ABC", "ACB", "ABC", "ACB", "ACB"]))
print(ranking(["WXYZ", "XYZW"]))
print(ranking(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
