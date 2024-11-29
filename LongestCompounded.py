import time
from typing import List, Tuple


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def is_compounded(word: str, word_set: set, memo: dict) -> bool:
    if word in memo:
        return memo[word]

    for i in range(1, len(word)):
        pre = word[:i]
        suf = word[i:]
        if pre in word_set and (suf in word_set or is_compounded(suf, word_set, memo)):
            memo[word] = True
            return True

    memo[word] = False
    return False


def find_longest_words(words: List[str]) -> Tuple[str, str]:
    word_set = set(words)
    memo = {}
    compounded_words = []

    for word in words:
        if is_compounded(word, word_set, memo):
            compounded_words.append(word)

    compounded_words.sort(key=len, reverse=True)
    longest = compounded_words[0] if compounded_words else ""
    second_longest = compounded_words[1] if len(compounded_words) > 1 else ""

    return longest, second_longest


def process_file(file_path: str):
    print(f"Processing file: {file_path}")
    start = time.time()
    words = read_file(file_path)
    longest, second_longest = find_longest_words(words)
    end = time.time()
    elapsed_time = end - start
    print(f"Longest compounded word: {longest}")
    print(f"Second longest compounded word: {second_longest}")
    print(f"Time taken to process: {elapsed_time:.2f} seconds")
    print("\n")


def main():
    file_1 = "Input_01.txt"
    file_2 = "Input_02.txt"
    process_file(file_1)
    process_file(file_2)


if __name__ == "__main__":
    main()
