double_char = lambda s: ''.join(i * 2 for i in s)

sum_str = lambda a, b: str(int(a or 0) + int(b or 0))

merge_arrays = lambda a, b: sorted(set(a + b))