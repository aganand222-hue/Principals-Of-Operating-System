from collections import OrderedDict

def fifo_page_replacement(pages, frames):
    memory = []
    hits = 0
    misses = 0
    steps = []

    for page in pages:
        if page in memory:
            hits += 1
            status = "Hit"
        else:
            misses += 1
            status = "Miss"

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        steps.append((page, memory.copy(), status))

    return hits, misses, steps


def lru_page_replacement(pages, frames):
    memory = OrderedDict()
    hits = 0
    misses = 0
    steps = []

    for page in pages:
        if page in memory:
            hits += 1
            status = "Hit"
            memory.move_to_end(page)
        else:
            misses += 1
            status = "Miss"

            if len(memory) >= frames:
                memory.popitem(last=False)

            memory[page] = True

        steps.append((page, list(memory.keys()), status))

    return hits, misses, steps


def display_result(name, pages, hits, misses, steps):
    total = len(pages)
    hit_ratio = hits / total
    miss_ratio = misses / total

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print(f"{'Page':<10}{'Frames':<25}{'Status':<10}")
    print("-" * 60)

    for page, memory, status in steps:
        print(f"{page:<10}{str(memory):<25}{status:<10}")

    print("-" * 60)
    print(f"Total References : {total}")
    print(f"Hits             : {hits}")
    print(f"Misses           : {misses}")
    print(f"Hit Ratio        : {hit_ratio:.2f}")
    print(f"Miss Ratio       : {miss_ratio:.2f}")


pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))

if frames <= 0:
    print("Number of frames must be greater than 0.")
else:
    fifo_hits, fifo_misses, fifo_steps = fifo_page_replacement(pages, frames)
    lru_hits, lru_misses, lru_steps = lru_page_replacement(pages, frames)

    display_result(
        "FIFO Page Replacement",
        pages,
        fifo_hits,
        fifo_misses,
        fifo_steps
    )

    display_result(
        "LRU Page Replacement",
        pages,
        lru_hits,
        lru_misses,
        lru_steps
    )

    print("\n" + "=" * 60)
    print("COMPARISON")
    print("=" * 60)

    total = len(pages)

    print(f"{'Technique':<15}{'Hits':<10}{'Misses':<10}{'Hit Ratio':<12}{'Miss Ratio'}")
    print("-" * 60)

    print(
        f"{'FIFO':<15}"
        f"{fifo_hits:<10}"
        f"{fifo_misses:<10}"
        f"{fifo_hits / total:.2f}{'':<7}"
        f"{fifo_misses / total:.2f}"
    )

    print(
        f"{'LRU':<15}"
        f"{lru_hits:<10}"
        f"{lru_misses:<10}"
        f"{lru_hits / total:.2f}{'':<7}"
        f"{lru_misses / total:.2f}"
    )

print("S117 Shravan Ramesh Vishwakarma")