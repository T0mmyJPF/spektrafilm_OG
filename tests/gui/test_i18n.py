from __future__ import annotations

import importlib
import os

from qtpy import QtWidgets


def test_translation_defaults_to_simplified_chinese_when_selected(monkeypatch) -> None:
    monkeypatch.setenv("SPEKTRAFILM_LANGUAGE", "zh_CN")
    from spektrafilm_gui import i18n

    importlib.reload(i18n)
    assert i18n.tr("MAIN") == "主界面"
    assert i18n.tr("White balance") == "白平衡"
    assert i18n.tr("as_shot") == "拍摄时设置"


def test_english_mode_returns_original_interface_strings(monkeypatch) -> None:
    monkeypatch.setenv("SPEKTRAFILM_LANGUAGE", "en")
    from spektrafilm_gui import i18n

    importlib.reload(i18n)
    assert i18n.tr("White balance") == "White balance"
    assert i18n.enum_label("as_shot") == "as_shot"
    assert i18n.tr_action("PREVIEW") == "PREVIEW"


def test_enum_editor_keeps_original_value_while_showing_chinese(monkeypatch) -> None:
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    monkeypatch.setenv("SPEKTRAFILM_LANGUAGE", "zh_CN")
    from spektrafilm_gui import i18n
    importlib.reload(i18n)

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
