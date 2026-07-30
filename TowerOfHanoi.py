def tower(n, source, auxiliary, destination):
    if n == 1:
        print("Move Disk 1 from", source, "to", destination)
        return

    tower(n - 1, source, destination, auxiliary)
    print("Move Disk", n, "from", source, "to", destination)
    tower(n - 1, auxiliary, source, destination)

# Number of disks
n = 3

tower(n, "A", "B", "C")
