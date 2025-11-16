class TestEx10:
    def test_phrase_length(self):
        phrase = input("Set a phrase: ")
        phrase_len = len(phrase)
        expected_len = 15

        assert phrase_len < expected_len, f"The phrase length = {phrase_len}, but expected length = {expected_len}"