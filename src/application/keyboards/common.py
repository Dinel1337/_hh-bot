from src.domain.keyboards.builder import KeyboardBuilder

def back_button(target: str = "main_menu"):
    return (KeyboardBuilder()
            .inline("⬅️ Назад", target)
            .as_inline())

def confirm_cancel():
    return (KeyboardBuilder()
            .inline("✅ Подтвердить", "confirm_yes")
            .inline("❌ Отмена", "confirm_no")
            .as_inline())
