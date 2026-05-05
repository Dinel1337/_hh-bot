from src.domain.keyboards.builder import KeyboardBuilder

def main_menu_inline():
    return (KeyboardBuilder()
            .inline("🔍 Поиск вакансий", "search_start")
            .inline("📋 Все вакансии", "show_all")
            .inline("⚙️ Настройки", "settings")
            .inline("ℹ️ Помощь", "help")
            .as_inline())

def main_menu_reply():
    return (KeyboardBuilder()
            .reply("🔍 Поиск вакансий")
            .reply("📋 Все вакансии")
            .reply("⚙️ Настройки")
            .reply("ℹ️ Помощь")
            .as_reply(placeholder="Выберите действие"))
