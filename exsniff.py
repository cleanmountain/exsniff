ALL_FILES = [] # e.g. ["sportscar-out.txt", "mountain-out.txt"]
NUM_OF_FILES = len(ALL_FILES)


def load_file(exif_file):
    with open(exif_file, "r", encoding="utf-16") as f:
        data = [line.strip() for line in f.readlines()]
    
    return data


def get_all_exif_lines():
    all_exif_lines = []

    for exif_file in ALL_FILES:
        exif_file_data = load_file(exif_file)

        for exif_line in exif_file_data:
            all_exif_lines.append(exif_line)
    
    return all_exif_lines


def count_occurences(all_exif_lines):
    line_occurences = {}

    for line in all_exif_lines:
        if line in line_occurences:
            line_occurences[line] += 1
        else:
            line_occurences[line] = 1
    
    return line_occurences


def find_common_lines(line_occurences):
    in_common = []

    for line in line_occurences:
        if line_occurences[line] == NUM_OF_FILES:
            in_common.append(line)

    return in_common


def main():
    all_exif_lines = get_all_exif_lines()
    line_occurences = count_occurences(all_exif_lines)
    common_lines = find_common_lines(line_occurences)

    print("\n".join(common_lines))


main()