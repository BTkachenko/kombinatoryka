import random

# Tutaj są te same definicje funkcji co wcześniej

def generate_random_string_with_probability(n, prob_a):
    return ''.join('a' if random.random() < prob_a else 'b' for _ in range(n))

def is_subsequence(str, pattern):
    return pattern in str

def count_occurrences(str, pattern):
    count = 0
    index = 0
    while (index := str.find(pattern, index)) != -1:
        count += 1
        index += len(pattern)
    return count

def calculate_actual_probabilities(strings):
    total_length = sum(len(s) for s in strings)
    count_a = sum(s.count('a') for s in strings)
    count_b = total_length - count_a
    return count_a / total_length, count_b / total_length

def calculate_single_statistics(number_of_trials, n, prob_a):
    count_aaa = 0
    count_abb = 0
    total_aaa = 0
    generated_strings = []

    for _ in range(number_of_trials):
        str = generate_random_string_with_probability(n, prob_a)
        generated_strings.append(str)

        if is_subsequence(str, "aaa"):
            count_aaa += 1
            total_aaa += count_occurrences(str, "aaa")

        if is_subsequence(str, "abb"):
            count_abb += 1

    actual_prob_a, actual_prob_b = calculate_actual_probabilities(generated_strings)
    average_aaa = total_aaa / number_of_trials
    return (n, count_aaa, count_abb, average_aaa, actual_prob_a, actual_prob_b)

# Stałe parametry
number_of_trials = 10000  # Liczba losowych ciągów do wygenerowania
max_length = 4  # Długość ciągu
prob_a = 0.8  # Prawdopodobieństwo dla 'a'

# Obliczenie statystyk dla pojedynczego n
single_stat = calculate_single_statistics(number_of_trials, max_length, prob_a)

# Wypisanie wyników w czytelnej formie w terminalu
n, count_aaa, count_abb, avg_aaa, actual_prob_a, actual_prob_b = single_stat
print(f"Dla n = {n}, z {number_of_trials} prób:")
print(f"1. Liczba ciągów zawierających wzór aaa: {count_aaa}")
print(f"2. Liczba ciągów zawierających wzór abb: {count_abb}")
print(f"3. Średnia liczba wystąpień wzorca aaa: {avg_aaa:.4f}")
print(f"4. Rzeczywiste prawdopodobieństwo wystąpienia 'a': {actual_prob_a:.4f}")
print(f"   Rzeczywiste prawdopodobieństwo wystąpienia 'b': {actual_prob_b:.4f}")
