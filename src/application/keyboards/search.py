from src.domain.keyboards.builder import KeyboardBuilder

def search_start():
    return (KeyboardBuilder()
            .inline("Ввести запрос", "prompt_query")
            .inline("Последние результаты", "latest_results")
            .inline("⬅️ Назад", "main_menu")
            .as_inline())

def after_search():
    return (KeyboardBuilder()
            .inline("🔄 Обновить", "refresh_search")
            .inline("📋 Все вакансии", "show_all")
            .inline("⬅️ Назад", "main_menu")
            .as_inline())
