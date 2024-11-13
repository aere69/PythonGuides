import html

class Question:

    def __init__(self, q_text, q_answer):
        self.text = self.to_readable_text(q_text)
        self.answer = q_answer

    def to_readable_text(self, r_text):
        r_text = html.unescape(r_text)
        return r_text
