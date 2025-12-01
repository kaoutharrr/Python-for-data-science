from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    """visually tracks how much of a task is done"""

    total = len(lst)
    for i, item in enumerate(lst):
        percent = (i+1)/total
        term_width = get_terminal_size().columns
        reserved = len(f"{100}%|[]| {total}/{total}")
        bar_width = term_width - reserved
        filled = int(percent * bar_width)
        bar = '=' * filled + ' ' * (bar_width - filled)
        print(f"\r{percent * 100:.0f}%|[{bar}]|{i + 1}/{total}", end='')
        yield item

    print()
