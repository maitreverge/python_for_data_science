FULL_BLOCK = '█'
# Since we can't use any module to get the terminal size, I hardcoded the total progress_bar_lenght
PROGRESS_BAR_LENGHT = 80

def get_terminal_size():
    ...

def ft_tqdm(lst: range):
    """
    ! DOTO :
    Match the 10 steps of the original function, and implement an optional get_terminal_size function
    """

    percentage = 0
    len_lst = len(lst)

    progress_bar = ' ' * PROGRESS_BAR_LENGHT
    for i in lst:
        percentage += (1 / len_lst) * 100

        full_blocks = percentage * PROGRESS_BAR_LENGHT / 100 / (PROGRESS_BAR_LENGHT / 80)

        # for _ in full_blocks:
        progress_bar = (FULL_BLOCK * int(full_blocks)) + (' ' * (PROGRESS_BAR_LENGHT - int(full_blocks)))

        print(f"\r{percentage:.0f}%|{progress_bar}| {i + 1}/{len_lst}",end="", flush=True)
        yield i