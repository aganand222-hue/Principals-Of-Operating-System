def calculate_movement(sequence, head):
    movement = 0
    current = head

    for request in sequence:
        movement += abs(current - request)
        current = request

    return movement


def fcfs(requests, head):
    sequence = requests.copy()
    movement = calculate_movement(sequence, head)
    return sequence, movement


def sstf(requests, head):
    remaining = requests.copy()
    sequence = []
    current = head

    while remaining:
        closest = min(remaining, key=lambda x: abs(x - current))
        sequence.append(closest)
        current = closest
        remaining.remove(closest)

    movement = calculate_movement(sequence, head)
    return sequence, movement


def c_scan(requests, head, disk_size=200):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = []
    sequence.extend(right)

    if right and right[-1] != disk_size - 1:
        sequence.append(disk_size - 1)

    if left:
        sequence.append(0)
        sequence.extend(left)

    movement = calculate_movement(sequence, head)
    return sequence, movement


def c_look(requests, head):
    left = sorted([x for x in requests if x < head])
    right = sorted([x for x in requests if x >= head])

    sequence = []
    sequence.extend(right)
    sequence.extend(left)

    movement = calculate_movement(sequence, head)
    return sequence, movement


def rss(requests, head):
    sequence = requests.copy()
    movement = calculate_movement(sequence, head)
    return sequence, movement


def disk_scheduling():
    print("\n" + "=" * 60)
    print("             DISK SCHEDULING SIMULATION")
    print("=" * 60)

    try:
        requests = list(map(int, input(
            "\nEnter disk request queue (space separated): "
        ).split()))

        head = int(input("Enter initial head position: "))
        disk_size = int(input("Enter disk size (e.g., 200): "))

    except ValueError:
        print("Invalid input!")
        return

    print("\nRequest Queue:", requests)
    print("Initial Head :", head)

    sequence, movement = fcfs(requests, head)
    print("\n--- FCFS ---")
    print("Sequence       :", [head] + sequence)
    print("Total Movement :", movement)

    sequence, movement = sstf(requests, head)
    print("\n--- SSTF ---")
    print("Sequence       :", [head] + sequence)
    print("Total Movement :", movement)

    sequence, movement = c_scan(requests, head, disk_size)
    print("\n--- C-SCAN ---")
    print("Sequence       :", [head] + sequence)
    print("Total Movement :", movement)

    sequence, movement = c_look(requests, head)
    print("\n--- C-LOOK ---")
    print("Sequence       :", [head] + sequence)
    print("Total Movement :", movement)

    sequence, movement = rss(requests, head)
    print("\n--- RSS ---")
    print("Sequence       :", [head] + sequence)
    print("Total Movement :", movement)


class SimpleFileSystem:

    def __init__(self, total_blocks=20):
        self.total_blocks = total_blocks
        self.blocks = [False] * total_blocks
        self.directory = {}

    def create_file(self, filename, data):

        if filename in self.directory:
            print("\nFile already exists!")
            return

        required_blocks = max(1, (len(data) + 49) // 50)

        free_blocks = [
            i for i in range(self.total_blocks)
            if not self.blocks[i]
        ]

        if len(free_blocks) < required_blocks:
            print("\nNot enough free blocks!")
            return

        allocated_blocks = free_blocks[:required_blocks]

        for block in allocated_blocks:
            self.blocks[block] = True

        self.directory[filename] = {
            "size": len(data),
            "blocks": allocated_blocks,
            "data": data
        }

        print("\nFile created successfully!")
        print("File Name       :", filename)
        print("File Size       :", len(data), "bytes")
        print("Allocated Blocks:", allocated_blocks)

    def read_file(self, filename):

        if filename not in self.directory:
            print("\nFile not found!")
            return

        file_info = self.directory[filename]

        print("\nFile Name:", filename)
        print("File Size:", file_info["size"], "bytes")
        print("Blocks   :", file_info["blocks"])
        print("Content  :", file_info["data"])

    def delete_file(self, filename):

        if filename not in self.directory:
            print("\nFile not found!")
            return

        file_info = self.directory[filename]

        for block in file_info["blocks"]:
            self.blocks[block] = False

        del self.directory[filename]

        print("\nFile deleted successfully!")

    def display_directory(self):

        print("\n" + "=" * 70)
        print("                    DIRECTORY")
        print("=" * 70)

        if not self.directory:
            print("Directory is empty.")
            return

        print(
            f"{'File Name':<20}"
            f"{'Size':<10}"
            f"{'Blocks':<30}"
        )

        print("-" * 70)

        for filename, info in self.directory.items():
            print(
                f"{filename:<20}"
                f"{info['size']:<10}"
                f"{str(info['blocks']):<30}"
            )

    def display_blocks(self):

        print("\n" + "=" * 60)
        print("                  BLOCK STATUS")
        print("=" * 60)

        for i in range(self.total_blocks):

            status = "ALLOCATED" if self.blocks[i] else "FREE"

            print(f"Block {i:02d} : {status}")


def file_system_menu():

    fs = SimpleFileSystem(20)

    while True:

        print("\n" + "=" * 60)
        print("              SIMPLE FILE SYSTEM")
        print("=" * 60)

        print("1. Create File")
        print("2. Read File")
        print("3. Delete File")
        print("4. Display Directory")
        print("5. Display Block Status")
        print("6. Return to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            filename = input("Enter file name: ")
            data = input("Enter file content: ")

            fs.create_file(filename, data)

        elif choice == "2":

            filename = input("Enter file name: ")
            fs.read_file(filename)

        elif choice == "3":

            filename = input("Enter file name: ")
            fs.delete_file(filename)

        elif choice == "4":

            fs.display_directory()

        elif choice == "5":

            fs.display_blocks()

        elif choice == "6":

            print("\nReturning to Main Menu...")
            break

        else:

            print("\nInvalid choice!")


def main():

    while True:

        print("\n")
        print("=" * 60)
        print("        DISK SCHEDULING AND FILE SYSTEM")
        print("=" * 60)

        print("1. Disk Scheduling")
        print("2. Simple File System")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            disk_scheduling()

        elif choice == "2":
            file_system_menu()

        elif choice == "3":
            print("\nProgram terminated.")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()

print("S117 Shravan Ramesh Vishwakarma")