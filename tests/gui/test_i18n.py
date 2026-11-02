from __future__ import annotations

from qtpy import QtWidgets


def test_translation_defaults_to_simplified_chinese_when_selected(monkeypatch) -> None:
    from spektrafilm_gui import i18n
    monkeypatch.setattr(i18n, "LANGUAGE", "zh_CN")
    assert i18n.tr("MAIN") == "主界面"
    assert i18n.tr("White balance") == "白平衡"
    assert i18n.tr("as_shot") == "拍摄时设置"


def test_english_mode_returns_original_interface_strings(monkeypatch) -> None:
    from spektrafilm_gui import i18n
    monkeypatch.setattr(i18n, "LANGUAGE", "en")
    assert i18n.tr("White balance") == "White balance"
    assert i18n.enum_label("as_shot") == "as_shot"
    assert i18n.tr_action("PREVIEW") == "PREVIEW"


def test_enum_editor_keeps_original_value_while_showing_chinese(monkeypatch) -> None:
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    from spektrafilm_gui import i18n
    monkeypatch.setattr(i18n, "LANGUAGE", "zh_CN")
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    from spektrafilm_gui.widget_editors import EnumEditor

    editor = EnumEditor(["as_shot", "daylight"])
    assert editor.itemText(0) == "拍摄时设置"
    assert editor.itemText(1) == "日光"
    assert editor.value == "as_shot"
    editor.value = "daylight"
    assert editor.currentText() == "日光"
    assert editor.value == "daylight"
    assert app is not None


def test_all_manifest_labels_and_tooltips_are_localized(monkeypatch) -> None:
    from spektrafilm_gui import i18n
    from spektrafilm_gui import param_manifest

    monkeypatch.setattr(i18n, "LANGUAGE", "zh_CN")
    specs = []
    for value in vars(param_manifest).values():
        if hasattr(value, "fields") and hasattr(value, "title"):
            specs.extend(value.fields)
        elif isinstance(value, tuple):
            specs.extend(item for item in value if hasattr(item, "leaf") and hasattr(item, "tooltip"))

    assert specs
    for spec in specs:
        label = spec.label or spec.leaf.replace("_", " ")
        assert i18n.tr(label) != label, f"Untranslated GUI label: {label}"
        if spec.tooltip:
            assert i18n.tr(spec.tooltip) != spec.tooltip, f"Untranslated tooltip: {spec.tooltip}"
