with open('tag.txt', 'r') as f:
    tags = ''.join(f.readlines())

print(tags.replace('\n', ',')[:-2])
