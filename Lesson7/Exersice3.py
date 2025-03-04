# Дан список строк. С помощью filter() получить список
# тех строк из исходного списка, которые являются
# палиндромами (читаются в обе стороны одинаково, например, ’abcсba’)

words = ["sun", "milk", "cat", "level", "stats", "abcсba"]
palindromes = list(filter(lambda words: words == words[::-1], words))
print("Слова палиндромы: ", list(palindromes))
