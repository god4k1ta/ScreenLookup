import string


class TextProcessor:
    def find_token_under_cursor(self, tokens, cursor_x, cursor_y):
        for token in tokens:
            left = token.x
            right = token.x + token.width
            top = token.y
            bottom = token.y + token.height

            if left <= cursor_x <= right and top <= cursor_y <= bottom:
                return token

        return None

    def get_token_text(self, token):
        if token is None:
            return None

        return token.text

    def get_context(self, tokens, target_token):
        if target_token is None:
            return ""

        same_line_tokens = self.get_tokens_on_same_line(
            tokens,
            target_token
        )

        return self.build_line_text(same_line_tokens)

    def get_tokens_on_same_line(self, tokens, target_token, tolerance=3):
        if target_token is None:
            return []

        same_line_tokens = []

        for token in tokens:
            diff_y = abs(token.y - target_token.y)

            if diff_y <= tolerance:
                same_line_tokens.append(token)

        return same_line_tokens

    def build_line_text(self, tokens):
        if not tokens:
            return ""

        sorted_tokens = sorted(tokens, key=lambda token: token.x)

        text = sorted_tokens[0].text

        for previous, current in zip(
            sorted_tokens,
            sorted_tokens[1:]
        ):
            if self._needs_space(previous, current):
                text += " "

            text += current.text

        return text

    def _needs_space(self, previous, current):
        previous_right = previous.x + previous.width
        gap = current.x - previous_right

        if gap <= 0:
            return False

        if current.text in string.punctuation:
            return False

        if previous.text in "([{":
            return False

        return self._has_word_gap(previous, current, gap)

    def _has_word_gap(self, previous, current, gap):
        reference_height = min(
            previous.height,
            current.height
        )

        threshold = reference_height * 0.2

        return gap >= threshold

    def process(self, ocr_result, cursor_x, cursor_y):
        tokens = ocr_result.tokens

        target_token = self.find_token_under_cursor(
            tokens,
            cursor_x,
            cursor_y
        )

        word = self.get_token_text(target_token)
        context = self.get_context(tokens, target_token)

        return word, context