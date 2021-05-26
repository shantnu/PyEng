from WordCount.word_count import count_words
from WordCount import word_count

def test_word_count():
    with open("WordCount/birds.txt", "r") as f:
        data = f.read()

        num_words = word_count.count_words(data)
        assert(num_words == 34)

def test_line_count():
     with open("WordCount/birds.txt", "r") as f:
        data = f.read()

        num_lines = word_count.count_lines(data)
        assert(num_lines == 8)
   
