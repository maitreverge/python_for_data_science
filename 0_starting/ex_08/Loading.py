def ft_tqdm(lst: range):

    percentage = 0
    len_lst = len(lst)

    for i in lst:
        yield i
        percentage += 1
        print(f"{percentage}% | |",end="", flush=True)