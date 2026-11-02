from __future__ import annotations

import json
from typing import Any, Callable

from spektrafilm_gui.i18n import tr


def save_current_as_default(
    *,
    viewer: Any,
    widgets: Any,
    collect_gui_state_fn: Callable[..., Any],
    save_default_gui_state_fn: Callable[[Any], None],
    set_status_fn: Callable[..., None],
    dialog_parent_fn: Callable[[Any], Any],
    message_box: Any,
) -> None:
    gui_state = collect_gui_state_fn(widgets=widgets)
    try:
        save_default_gui_state_fn(gui_state)
    except (OSError, ValueError) as exc:
        message_box.critical(dialog_parent_fn(viewer), tr('Save current as default'), f'{tr("保存默认界面设置失败。")}\n\n{exc}')
        return

    set_status_fn(viewer, tr('当前界面设置已保存为启动默认设置'))


def save_current_state_to_file(
    *,
    viewer: Any,
    widgets: Any,
    file_dialog: Any,
    collect_gui_state_fn: Callable[..., Any],
    save_gui_state_to_path_fn: Callable[[Any, str], None],
    set_status_fn: Callable[..., None],
    dialog_parent_fn: Callable[[Any], Any],
    message_box: Any,
) -> None:
    filepath, _ = file_dialog.get_save_file_name(
        dialog_parent_fn(viewer),
        tr('Save GUI state'),
        'gui_state.json',
        'JSON (*.json)',
    )
    if not filepath:
        return

    gui_state = collect_gui_state_fn(widgets=widgets)
    try:
        save_gui_state_to_path_fn(gui_state, filepath)
    except (OSError, ValueError) as exc:
        message_box.critical(dialog_parent_fn(viewer), tr('Save GUI state'), f'{tr("保存界面设置失败。")}\n\n{exc}')
        return

    set_status_fn(viewer, f'{tr("界面设置已保存至")} {filepath}')


def load_state_from_file(
    *,
    viewer: Any,
    widgets: Any,
    file_dialog: Any,
    load_gui_state_from_path_fn: Callable[[str], Any],
    apply_gui_state_fn: Callable[..., None],
    sync_canvas_background_fn: Callable[[], None],
    set_status_fn: Callable[..., None],
    dialog_parent_fn: Callable[[Any], Any],
    message_box: Any,
) -> None:
    filepath, _ = file_dialog.get_open_file_name(
        dialog_parent_fn(viewer),
        tr('Load GUI state'),
        '',
        'JSON (*.json)',
    )
    if not filepath:
        return

    try:
        gui_state = load_gui_state_from_path_fn(filepath)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        message_box.critical(dialog_parent_fn(viewer), tr('Load GUI state'), f'{tr("加载界面设置失败。")}\n\n{exc}')
        return

    apply_gui_state_fn(gui_state, widgets=widgets)
    sync_canvas_background_fn()
    set_status_fn(viewer, f'{tr("已从文件加载界面设置")}：{filepath}')


def restore_factory_default(
    *,
    viewer: Any,
    widgets: Any,
    project_default_gui_state: Any,
    clear_saved_default_gui_state_fn: Callable[[], None],
    apply_gui_state_fn: Callable[..., None],
    sync_canvas_background_fn: Callable[[], None],
    set_status_fn: Callable[..., None],
    dialog_parent_fn: Callable[[Any], Any],
    message_box: Any,
) -> None:
    try:
        clear_saved_default_gui_state_fn()
    except OSError as exc:
        message_box.critical(
            dialog_parent_fn(viewer),
            tr('Restore factory default'),
            f'{tr("清除已保存的启动默认设置失败。")}\n\n{exc}',
        )
        return

    apply_gui_state_fn(project_default_gui_state, widgets=widgets)
    sync_canvas_background_fn()
    set_status_fn(viewer, tr('已恢复出厂默认界面设置'))