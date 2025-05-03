def match_words(words):
    ctr = 0
    st = []
    for word in words:
        if len(word)> 1 and word[0] == word[-1]:
            ctr += 1
            st.append(words)

    print("list of words with first and last character same are\n", list)
    return ctr
count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having first and last characters same:", count)