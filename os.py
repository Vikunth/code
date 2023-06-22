import random

memory_size = 100
time_units = 10
memory = [None] * memory_size
free_blocks = [(0, memory_size)]

def allocate(size):
    for i, block in enumerate(free_blocks):
        if block[1] - block[0] >= size:
            allocated_block = (block[0], block[0] + size)
            free_block = (block[0] + size, block[1])
            memory[allocated_block[0]:allocated_block[1]] = [0] * size
            free_blocks[i] = free_block
            return
    return

def deallocate(block):
    free_block = block
    for i, block in enumerate(free_blocks):
        if block[1] == free_block[0]:
            free_block = (block[0], free_block[1])
            del free_blocks[i]
            break
        elif block[0] == free_block[1]:
            free_block = (free_block[0], block[1])
            del free_blocks[i]
            break
    free_blocks.append(free_block)
    memory[free_block[0]:free_block[1]] = [None] * (free_block[1] - free_block[0])

def simulate():
    frag = []
    wasted = []
    for t in range(time_units):
        req_type = random.choice(['allocate', 'deallocate'])
        if req_type == 'allocate':
            size = random.randint(1, 10)
            allocate(size)
        else:
            allocated_blocks = [(i, block) for i, block in enumerate(free_blocks) if block[0] is not None]
            if allocated_blocks:
                i, block = random.choice(allocated_blocks)
                deallocate(block)
        frag.append(sum([block[1] - block[0] for block in free_blocks]) / len(free_blocks))
        wasted.append(len([block for block in free_blocks if block[1] - block[0] > 0]))
    print(f"Average fragmentation: {sum(frag) / len(frag)}")
    print(f"Number of wasted blocks: {sum(wasted)}")

simulate()
