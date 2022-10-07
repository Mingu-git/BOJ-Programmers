

from itertools import combinations
"""
combination ,permutaion에 대한 이해



"""

가끔 모든 경우를 탐색해야 하는 상황이 있습니다. 대표적으로 이런 문제가 있겠네요?

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하시오.

일반적으로 백트래킹을 활용해서 문제를 풉니다. 그렇지만, 다음과 같은 기능을 공부하면 굳이 백트래킹을 할 필요가 없습니다.

import itertools
_list = [1, 2, 3, 4]
iter = itertools.combinations(_list, 2) # 12 13 14 23 24 34

iter = itertools.permutations(_list, 2) # 12 13 14 21 23 24 31 32 34 41 42 43

iter = itertools.combinations_with_replacement(_list, 2) # 11 12 13 14 22 23 24 33 34 44

iter = itertools.product(_list, repeat=2) # 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44
combination은 모든 조합을 출력합니다. 즉, 중복이 없고, 순서를 구분하지 않습니다. permutation은 순열입니다. 중복은 없지만, 순서를 구분합니다.

combination_with_replacement는 중복이 가능한 조합입니다. 그래서 combination과 구분하여 11, 22, 33, 44가 새로 들어오죠. 마지막으로 product는 모든 가능한 경우의 수를 출력합니다. (Cartesian Product라고 합니다!)

combination을 활용하면 다음과 같은 문제도 해결할 수 있습니다.

전체 리스트에서 3개를 추출하여 곱했을 때, 그 곱의 최댓값을 출력하는 프로그램을 작성하시오.

방법은 굳이 알려드리지 않아도 알겠죠?

이처럼 단순히 순열, 조합을 구하는 것이 아닌, 다양한 완전탐색 상황에서 사용될 수 있으니 꼭 기억해두길 바라요.