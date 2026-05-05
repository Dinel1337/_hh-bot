from typing import List
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

class KeyboardBuilder:
    """Универсальный строитель клавиатур."""
    def __init__(self):
        self._inline: List[List[InlineKeyboardButton]] = []
        self._reply: List[List[KeyboardButton]] = []

    def inline(self, text: str, callback_data: str = None, url: str = None, row: int = -1) -> 'KeyboardBuilder':
        btn = InlineKeyboardButton(text=text, callback_data=callback_data, url=url)
        if row == -1:
            self._inline.append([btn])
        else:
            while len(self._inline) <= row:
                self._inline.append([])
            self._inline[row].append(btn)
        return self

    def inline_row(self, *buttons: InlineKeyboardButton) -> 'KeyboardBuilder':
        self._inline.append(list(buttons))
        return self

    def reply(self, text: str, row: int = -1) -> 'KeyboardBuilder':
        btn = KeyboardButton(text=text)
        if row == -1:
            self._reply.append([btn])
        else:
            while len(self._reply) <= row:
                self._reply.append([])
            self._reply[row].append(btn)
        return self

    def reply_row(self, *buttons: KeyboardButton) -> 'KeyboardBuilder':
        self._reply.append(list(buttons))
        return self

    def as_inline(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=self._inline)

    def as_reply(self, resize: bool = True, placeholder: str = None) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(keyboard=self._reply, resize_keyboard=resize,
                                   input_field_placeholder=placeholder)

    def clear(self):
        self._inline.clear()
        self._reply.clear()
        return self
