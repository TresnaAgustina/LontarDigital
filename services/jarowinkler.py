class JaroWinkler:
    def __init__(self, threshold=0.9):
        self.threshold = threshold

    def jaro_similarity(self, s1, s2):
        if not s1 and not s2:
            return 1.0  # Kedua string kosong, dianggap sempurna cocok.

        # Hitung panjang string dan batas pencarian
        len1 = len(s1)
        len2 = len(s2)
        search_range = max(len1, len2) // 2 - 1

        # Inisialisasi variabel yang diperlukan
        match_counter = 0
        s1_matches = [False] * len1
        s2_matches = [False] * len2

        # Hitung jumlah karakter yang cocok
        for i in range(len1):
            start = max(0, i - search_range)
            end = min(i + search_range + 1, len2)

            for j in range(start, end):
                if not s2_matches[j] and s1[i] == s2[j]:
                    s1_matches[i] = True
                    s2_matches[j] = True
                    match_counter += 1
                    break

        if match_counter == 0:
            return 0.0

        # Hitung jumlah transposisi
        transpositions = 0
        j = 0
        for i in range(len1):
            if s1_matches[i]:
                while not s2_matches[j]:
                    j += 1
                if s1[i] != s2[j]:
                    transpositions += 1
                j += 1

        transpositions /= 2.0

        # Hitung Jaro Similarity
        jaro_similarity = (match_counter / len1 + match_counter / len2 +
                           (match_counter - transpositions) / match_counter) / 3.0

        return jaro_similarity

    def jaro_winkler_similarity(self, s1, s2):
        jaro_similarity = self.jaro_similarity(s1, s2)

        if jaro_similarity < self.threshold:
            return jaro_similarity

        # Hitung common prefix length (maksimal 4 karakter)
        prefix_length = 0
        for i in range(min(len(s1), len(s2), 4)):
            if s1[i] == s2[i]:
                prefix_length += 1
            else:
                break

        # Hitung faktor peningkatan (0.1 * common prefix length * (1 - Jaro Similarity))
        winkler_factor = 0.1 * prefix_length * (1 - jaro_similarity)

        # Hitung Jaro-Winkler Similarity
        jaro_winkler_similarity = jaro_similarity + winkler_factor

        return min(jaro_winkler_similarity, 1.0)
