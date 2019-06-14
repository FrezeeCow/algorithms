"""
Implement Flatten Arrays.
Given an array that may contain nested arrays, give a single resultant array.

Example:

Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]]
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]

Input: var input = (2, 1, (3, (4, 5), 6), 7, (8))
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""

# 基于递归的实现方法，isinstance 用于判断参数a是否属于(list, tuple)中的类型的一种，返回bool类型，与type的区别在于会继承判断类型。
def list_flat(l, a=None):
    # 如果a为None,创建一个空列表；否则将列表转为List类型
    a = list(a) if isinstance(a, (list, tuple)) else []
    # 遍历列表项中的元素
    for i in l:
        # 遇到仍然是列表项的进行递归
        if isinstance(i, (list, tuple)):
            a = list_flat(i, a)
        # 遇到单个元素的加入到列表a
        else:
            a.append(i)
    return a

a = [2, 1, [3, [4, 5], 6], 7, [8]]
print(list_flatten(a))
