from pacman.backend.errors import ConfigError

_ALL_COMMENTS = ['#', '//', '/*', '*/']

def strip_comments(text):
    if not text:
        raise ConfigError("File must not be empty.")
    
    if text.strip() in _ALL_COMMENTS:
        raise ConfigError("File must contain actual content.")

    result = []

    in_string = False
    in_block_comment = False
    escaped = False

    i = 0
    while i < len(text):
        char = text[i]
        next_char = text[i + 1] if i + 1 < len(text) else ""

        if in_string:
            result.append(char)
            if char == '"':
                in_string = False
                i += 1
                continue

            if escaped:
                escaped = False
            if char == "\\":
                escaped = True

            i += 1
            continue
            

        if char == '"':
            in_string = True


        if char == "/" and next_char == "*":
            in_block_comment = True
            i += 2
            while i < len(text) and text[i] != "\n":
                i += 1
            continue

        if char == "*" and next_char == "/":
            in_block_comment = False
            i += 2
            continue

        if char == "#":
            i += 1
            while i < len(text) and text[i] != "\n":
                i += 1
            continue

        if char == "/" and next_char == "/":
            i += 2
            while i < len(text) and text[i] != "\n":
                i += 1
            continue
        
        result.append(char)
        i += 1

    # if in_block_comment:
    #     raise ValueError("Unterminated block comment")

    return "".join(result)
