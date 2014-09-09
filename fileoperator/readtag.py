# coding = utf-8


def get_tag():
    tags = []
    with open('tag.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tags.append(line)
    return tags


if __name__ == '__main__':
    taglist = get_tag()
    for tag in taglist:
        if tag.startswith('v11'):
            print tag
