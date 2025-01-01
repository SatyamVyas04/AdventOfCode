from collections import defaultdict


def left_right_divides(lines):
    left = []
    right = []
    for line in lines:
        l = line[0]
        r = line[-1]
        left.append(l)
        right.append(r)
    return left, right


def pair_difference(left, right):
    '''Solves the first part of the problem'''
    left = sorted(left)
    right = sorted(right)
    l, r = 0, 0
    ans = 0
    while l < len(left) and r < len(right):
        ans += abs(left[l] - right[r])
        l += 1
        r += 1
    return ans


def hashmap_generation(right):
    hashmap = defaultdict(int)
    for r in right:
        hashmap[r] += 1
    return hashmap


def return_similarity_score(left, hashmap):
    '''Solves the second part of the problem'''
    ans = 0
    for l in left:
        ans += l * hashmap[l]
    return ans


def main():
    file = "input.txt"
    with open(file) as f:
        lines = f.read().split("\n")
        for idx in range(len(lines)):
            lines[idx] = list(map(int, lines[idx].split("   ")))

        left, right = left_right_divides(lines)
        print("Total distance between the lists is:",
              pair_difference(left, right))

        hashmap = hashmap_generation(right)
        print("The similarity score is:",
              return_similarity_score(left, hashmap))


if __name__ == "__main__":
    main()
