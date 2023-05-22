#!/usr/bin/env python3

class MyString:
  def __init__(self, string=123):
    self.string = string
    if not isinstance(string, str):
      print("The value must be a string.")

  def is_sentence(self):
    return self.string.endswith('.')
  
  def is_question(self):
    return self.string.endswith('?')
  
  def is_exclamation(self):
    return self.string.endswith('!')
  
  def count_sentences(self):
    import re
    pattern = r'\b\w[^\.\?\!]*[\.\?\!]'
    sentence_list = re.findall(pattern, str(self.string))
    return len(sentence_list)
  
string = MyString("This, well, is a sentence. This too!! And so is this, I think? Woo...")
