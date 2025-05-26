# ================================================
# Step 1: Prepare Training Data
# ================================================
import collections
import os

corpus = open((os.getcwd() +
               "/data/small-corpus.txt"), "r").readlines()

print("Training Corpus:")
for doc in corpus:
    print(f'"{doc.rstrip()}"')

# ================================================
# Step 2: Initialize Vocabulary and Pre-tokenize
# ================================================
unique_chars = set()
for doc in corpus:
    for char in doc:
        unique_chars.add(char)

vocab = list(unique_chars)
vocab.sort()

# Add a special end-of-word token
end_of_word = "</w>"
vocab.append(end_of_word)

print("\nInitial Vocabulary:")
print(vocab)
print(f"Vocabulary Size: {len(vocab)}")

# Pre-tokenize the corpus
word_splits = {}
for doc in corpus:
    words = doc.split(' ')
    for word in words:
        if word:
            char_list = list(word) + [end_of_word]
            word_tuple = tuple(char_list)
            if word_tuple not in word_splits:
                word_splits[word_tuple] = 0
            word_splits[word_tuple] += 1

print("\nPre-tokenized Word Frequencies:")
print(word_splits)

# Count the frequnecy of adjacent pairs in the word splits.


def get_pair_stats(splits):
    pair_counts = collections.defaultdict(int)
    for word_tuple, freq in splits.items():
        symbols = list(word_tuple)
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            pair_counts[pair] += freq
    return pair_counts

# Merge the specific pair in the word splits.


def merge_pair(pair_to_merge, splits):
    new_splits = {}
    (first, second) = pair_to_merge
    merged_token = first + second
    for word_tuple, freq in splits.items():
        symbols = list(word_tuple)
        new_symbols = []
        i = 0
        while i < len(symbols):
            if i < len(symbols) - 1 and symbols[i] == first and symbols[i + 1] == second:
                new_symbols.append(merged_token)
                i += 2
            else:
                new_symbols.append(symbols[i])
                i += 1
        new_splits[tuple(new_symbols)] = freq
    return new_splits

# ================================================
# Step 3: Interative BPE Merging Loop
# ================================================
num_merges = 15
merges = {}
current_splits = word_splits.copy()

print("\n--- Starting BPE Merges ---")
print(f"Initial Splits: {current_splits}")
print("-" * 30)

for i in range(num_merges):
    print(f"\nMerge Interation {i + 1}/{num_merges}")

    # 1. Caluclate Pair Frequencies
    pair_stats = get_pair_stats(current_splits)
    if not pair_stats:
        print("No more pairs to merge.")
        break

    # Optional: Print the top 5 pairs for inspection
    sorted_pairs = sorted(pair_stats.items(), key=lambda item: item[1], reverse=True)
    print(f"Top 5 Pair Frequencies: {sorted_pairs[:5]}")
    
    # 2. Find Best Pair
    best_pair = max(pair_stats, key=pair_stats.get)
    best_freq = pair_stats[best_pair]
    print(f"Found Best Pair: {best_pair} with Frequency: {best_freq}")
    
    # 3. Merge the Best Pair
    current_splits = merge_pair(best_pair, current_splits)
    new_token = best_pair[0] + best_pair[1]
    print(f"Merged {best_pair} into {new_token}")
    print(f"Splits after merge: {current_splits}")
    
    # 4. Update Vocabulary
    vocab.append(new_token)
    print(f"Updated Vocabulary: {vocab}")
    
    # 5. Store Merge Rule
    merges[best_pair] = new_token
    print(f"Updated Merges: {merges}")
    print("-" * 30)
    
# ================================================
# Step 4: Review Final Results
# ================================================

print("\n--- BPE Merges Complete ---")
print(f"Final Vocabulary Size: {len(vocab)}")
print(f"\nLearned Merges (Pair -> New Token):")
# Pretty print the merges
for pair, token in merges.items():
    print(f"{pair} -> {token}")

print("\nFinal Word Splits after all merges:")
print(current_splits)

print("\nFinal Vocabulary (sorted):")
final_vocab_sorted = sorted(list(set(vocab)))
print(final_vocab_sorted)
