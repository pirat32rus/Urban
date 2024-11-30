import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def _cleanup_text(self, text):
        translator = str.maketrans('', '', string.punctuation.replace('-', ''))
        return text.lower().translate(translator)

    def get_all_words(self):
        all_words = {}
        
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                cleaned_text = self._cleanup_text(text)
                words_list = cleaned_text.split()
                all_words[file_name] = words_list
        
        return all_words

    def find(self, word):
        word_lower = word.lower()
        result = {}
        all_words = self.get_all_words()
        
        for file_name, words in all_words.items():
            if word_lower in words:
                position = words.index(word_lower) + 1
                result[file_name] = position
        
        return result

    def count(self, word):
        word_lower = word.lower()
        result = {}
        all_words = self.get_all_words()
        
        for file_name, words in all_words.items():
            count = words.count(word_lower)
            if count > 0:
                result[file_name] = count
        
        return result

# Пример использования:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
