class TextProcessor:
    def find_token_under_cursor(self, tokens, cursor_x, cursor_y):
        for token in tokens:
            right = token.x + token.width
            bottom = token.y + token.height
            top = token.y
            left = token.x

            if left <= cursor_x <= right and top <= cursor_y <= bottom:
                return token

        return None

    def get_token_text(self, token):
        if token is None:
            return None

        return token.text

    def get_context(self, ocr_result):
        if ocr_result is None:
            return None

        return ocr_result.full_text

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
        if tokens is None:
            return ""
        sorted_tokens = sorted(tokens, key=lambda token: token.x)
        text = ""
        for token in sorted_tokens:
            text = text + token.text
        return text
