def ft_tqdm(lst: range):

    percentage = 0
    len_lst = len(lst)

    for i in lst:
        yield i
        percentage += (1 / len_lst) * 100
        print(f"\r{percentage:.0f}% | | {i + 1}/{len_lst}",end="", flush=True)