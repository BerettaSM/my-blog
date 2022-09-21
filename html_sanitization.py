import bleach


def strip_invalid_html(content: str) -> str:
    allowed_tags = ('a', 'abbr', 'acronym', 'address',
                    'b', 'br', 'div', 'dl', 'dt', 'em',
                    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                    'hr', 'i', 'img', 'li', 'ol', 'p',
                    'pre', 'q', 's', 'small', 'strike',
                    'span', 'sub', 'sup', 'table',
                    'tbody', 'td', 'tfoot', 'th', 'thead',
                    'tr', 'tt', 'u', 'ul')
    allowed_attrs = {
        'a': ('href', 'target', 'title'),
        'img': ('src', 'alt', 'width', 'height')
    }
    sanitized_content = bleach.clean(
        text=content,
        tags=allowed_tags,
        attributes=allowed_attrs,
        strip=True
    )
    return sanitized_content
