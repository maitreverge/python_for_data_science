FULL_BLOCK = "█"
# Since we can't use any module to get the terminal size,
# I hardcoded the total progress_bar_lenght
PROGRESS_BAR_LENGHT = 80


def ft_tqdm(lst: range):
    """
    Implementation of a light tqdm function from scratch.
    This custom implemetation has an hardcoded progress bar of 80 chars long.
    """

    percentage = 0
    len_lst = len(lst)

    progress_bar = " " * PROGRESS_BAR_LENGHT
    for i in lst:
        percentage += (1 / len_lst) * 100

        full_blocks = (
            percentage * PROGRESS_BAR_LENGHT / 100 / (PROGRESS_BAR_LENGHT / 80)
        )

        # for _ in full_blocks:
        progress_bar = (FULL_BLOCK * int(full_blocks)) + (
            " " * (PROGRESS_BAR_LENGHT - int(full_blocks))
        )

        print(
            f"\r{percentage:.0f}%|{progress_bar}| {i + 1}/{len_lst}",
            end="", flush=True
        )
        yield i
