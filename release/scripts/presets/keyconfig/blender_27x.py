keyconfig_data = [
    (
        "Window",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("wm.window_new", {"type": 'W', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("wm.read_homefile", {"type": 'N', "value": 'PRESS', "ctrl": True}, None),
                ("wm.save_homefile", {"type": 'U', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'O', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", 'INFO_MT_file_open_recent'),
                        ],
                    }
                ),
                ("wm.open_mainfile", {"type": 'O', "value": 'PRESS', "ctrl": True}, None),
                ("wm.open_mainfile", {"type": 'F1', "value": 'PRESS'}, None),
                ("wm.link", {"type": 'O', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("wm.append", {"type": 'F1', "value": 'PRESS', "shift": True}, None),
                ("wm.save_mainfile", {"type": 'S', "value": 'PRESS', "ctrl": True}, None),
                ("wm.save_mainfile", {"type": 'W', "value": 'PRESS', "ctrl": True}, None),
                ("wm.save_as_mainfile", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("wm.save_as_mainfile", {"type": 'F2', "value": 'PRESS'}, None),
                (
                    "wm.save_as_mainfile",
                    {"type": 'S', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("copy", True),
                        ],
                    }
                ),
                ("wm.window_fullscreen_toggle", {"type": 'F11', "value": 'PRESS', "alt": True}, None),
                ("wm.quit_blender", {"type": 'Q', "value": 'PRESS', "ctrl": True}, None),
                ("wm.doc_view_manual_ui_context", {"type": 'F1', "value": 'PRESS', "alt": True}, None),
                ("wm.redraw_timer", {"type": 'T', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("wm.debug_menu", {"type": 'D', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'NDOF_BUTTON_MENU', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'USERPREF_MT_ndof_settings'),
                        ],
                    }
                ),
                ("wm.search_menu", {"type": 'SPACE', "value": 'PRESS'}, None),
                (
                    "wm.context_set_enum",
                    {"type": 'F3', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'NODE_EDITOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F4', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'CONSOLE'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F5', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'VIEW_3D'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F6', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'GRAPH_EDITOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F7', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'PROPERTIES'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F8', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'SEQUENCE_EDITOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F9', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'OUTLINER'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F10', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'IMAGE_EDITOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F11', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'TEXT_EDITOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'F12', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'area.type'),
                            ("value", 'DOPESHEET_EDITOR'),
                        ],
                    }
                ),
                (
                    "wm.context_scale_float",
                    {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'user_preferences.inputs.ndof_sensitivity'),
                            ("value", 1.1),
                        ],
                    }
                ),
                (
                    "wm.context_scale_float",
                    {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'user_preferences.inputs.ndof_sensitivity'),
                            ("value", 1.0),
                        ],
                    }
                ),
                (
                    "wm.context_scale_float",
                    {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'user_preferences.inputs.ndof_sensitivity'),
                            ("value", 1.5),
                        ],
                    }
                ),
                (
                    "wm.context_scale_float",
                    {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'user_preferences.inputs.ndof_sensitivity'),
                            ("value", 0.6666667),
                        ],
                    }
                ),
                ("info.reports_display_update", {"type": 'TIMER_REPORT', "value": 'ANY', "any": True}, None),
            ],
        },
    ),
    (
        "Screen",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("screen.animation_step", {"type": 'TIMER0', "value": 'ANY', "any": True}, None),
                ("screen.region_blend", {"type": 'TIMERREGION', "value": 'ANY', "any": True}, None),
                (
                    "screen.screen_set",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "screen.screen_set",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                ("screen.screen_full_area", {"type": 'SPACE', "value": 'PRESS', "shift": True}, None),
                (
                    "screen.screen_full_area",
                    {"type": 'SPACE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_hide_panels", True),
                        ],
                    }
                ),
                ("screen.screenshot", {"type": 'F3', "value": 'PRESS', "ctrl": True}, None),
                ("screen.screencast", {"type": 'F3', "value": 'PRESS', "alt": True}, None),
                (
                    "screen.space_context_cycle",
                    {"type": 'TAB', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'NEXT'),
                        ],
                    }
                ),
                (
                    "screen.space_context_cycle",
                    {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'PREV'),
                        ],
                    }
                ),
                ("screen.region_quadview", {"type": 'Q', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("screen.repeat_history", {"type": 'F3', "value": 'PRESS'}, None),
                ("screen.repeat_last", {"type": 'R', "value": 'PRESS', "shift": True}, None),
                ("screen.region_flip", {"type": 'F5', "value": 'PRESS'}, None),
                ("screen.redo_last", {"type": 'F6', "value": 'PRESS'}, None),
                ("script.reload", {"type": 'F8', "value": 'PRESS'}, None),
                ("file.execute", {"type": 'RET', "value": 'PRESS'}, None),
                ("file.execute", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
                ("file.cancel", {"type": 'ESC', "value": 'PRESS'}, None),
                ("ed.undo", {"type": 'Z', "value": 'PRESS', "ctrl": True}, None),
                ("ed.redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("ed.undo_history", {"type": 'Z', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                (
                    "render.render",
                    {"type": 'F12', "value": 'PRESS'},
                    {
                        "properties": [
                            ("use_viewport", True),
                        ],
                    }
                ),
                (
                    "render.render",
                    {"type": 'F12', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("animation", True),
                            ("use_viewport", True),
                        ],
                    }
                ),
                ("render.view_cancel", {"type": 'ESC', "value": 'PRESS'}, None),
                ("render.view_show", {"type": 'F11', "value": 'PRESS'}, None),
                ("render.play_rendered_anim", {"type": 'F11', "value": 'PRESS', "ctrl": True}, None),
                ("screen.userpref_show", {"type": 'U', "value": 'PRESS', "ctrl": True, "alt": True}, None),
            ],
        },
    ),
    (
        "User Interface",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("ui.eyedropper_color", {"type": 'E', "value": 'PRESS'}, None),
                ("ui.eyedropper_colorband", {"type": 'E', "value": 'PRESS'}, None),
                ("ui.eyedropper_colorband_point", {"type": 'E', "value": 'PRESS', "alt": True}, None),
                ("ui.eyedropper_id", {"type": 'E', "value": 'PRESS'}, None),
                ("ui.eyedropper_depth", {"type": 'E', "value": 'PRESS'}, None),
                ("ui.copy_data_path_button", {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "ui.copy_data_path_button",
                    {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("full_path", True),
                        ],
                    }
                ),
                ("anim.keyframe_insert_button", {"type": 'I', "value": 'PRESS'}, None),
                ("anim.keyframe_delete_button", {"type": 'I', "value": 'PRESS', "alt": True}, None),
                ("anim.keyframe_clear_button", {"type": 'I', "value": 'PRESS', "shift": True, "alt": True}, None),
                ("anim.driver_button_add", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
                ("anim.driver_button_remove", {"type": 'D', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("anim.keyingset_button_add", {"type": 'K', "value": 'PRESS'}, None),
                ("anim.keyingset_button_remove", {"type": 'K', "value": 'PRESS', "alt": True}, None),
            ],
        },
    ),
    (
        "View2D",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("view2d.scroller_activate", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("view2d.scroller_activate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("view2d.pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("view2d.pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
                ("view2d.pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("view2d.scroll_right", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("view2d.scroll_left", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("view2d.scroll_down", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
                ("view2d.scroll_up", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
                ("view2d.ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
                ("view2d.zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
                ("view2d.zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
                ("view2d.zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS'}, None),
                ("view2d.zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS'}, None),
                ("view2d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
                ("view2d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
                ("view2d.scroll_down", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
                ("view2d.scroll_up", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
                ("view2d.scroll_right", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
                ("view2d.scroll_left", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
                ("view2d.zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("view2d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
                ("view2d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
            ],
        },
    ),
    (
        "Header",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("screen.header_toolbox", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "View2D Buttons List",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("view2d.scroller_activate", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("view2d.scroller_activate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("view2d.pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("view2d.pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("view2d.scroll_down", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
                ("view2d.scroll_up", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
                (
                    "view2d.scroll_down",
                    {"type": 'PAGE_DOWN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("page", True),
                        ],
                    }
                ),
                (
                    "view2d.scroll_up",
                    {"type": 'PAGE_UP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("page", True),
                        ],
                    }
                ),
                ("view2d.zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("view2d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
                ("view2d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
                ("view2d.zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS'}, None),
                ("view2d.zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS'}, None),
                ("view2d.reset", {"type": 'HOME', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Frames",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "screen.frame_offset",
                    {"type": 'UP_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("delta", 10),
                        ],
                    }
                ),
                (
                    "screen.frame_offset",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("delta", -10),
                        ],
                    }
                ),
                (
                    "screen.frame_offset",
                    {"type": 'LEFT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                (
                    "screen.frame_offset",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "screen.frame_offset",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "screen.frame_offset",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                (
                    "screen.frame_jump",
                    {"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("end", True),
                        ],
                    }
                ),
                (
                    "screen.frame_jump",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("end", False),
                        ],
                    }
                ),
                (
                    "screen.frame_jump",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("end", True),
                        ],
                    }
                ),
                (
                    "screen.frame_jump",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("end", False),
                        ],
                    }
                ),
                (
                    "screen.keyframe_jump",
                    {"type": 'UP_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("next", True),
                        ],
                    }
                ),
                (
                    "screen.keyframe_jump",
                    {"type": 'DOWN_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("next", False),
                        ],
                    }
                ),
                (
                    "screen.keyframe_jump",
                    {"type": 'MEDIA_LAST', "value": 'PRESS'},
                    {
                        "properties": [
                            ("next", True),
                        ],
                    }
                ),
                (
                    "screen.keyframe_jump",
                    {"type": 'MEDIA_FIRST', "value": 'PRESS'},
                    {
                        "properties": [
                            ("next", False),
                        ],
                    }
                ),
                ("screen.animation_play", {"type": 'A', "value": 'PRESS', "alt": True}, None),
                (
                    "screen.animation_play",
                    {"type": 'A', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("reverse", True),
                        ],
                    }
                ),
                ("screen.animation_cancel", {"type": 'ESC', "value": 'PRESS'}, None),
                ("screen.animation_play", {"type": 'MEDIA_PLAY', "value": 'PRESS'}, None),
                ("screen.animation_cancel", {"type": 'MEDIA_STOP', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Property Editor",
        {"space_type": 'PROPERTIES', "region_type": 'WINDOW'},
        {
            "items": [
                ("buttons.toolbox", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Info",
        {"space_type": 'INFO', "region_type": 'WINDOW'},
        {
            "items": [
                ("info.select_pick", {"type": 'SELECTMOUSE', "value": 'PRESS'}, None),
                ("info.select_all_toggle", {"type": 'A', "value": 'PRESS'}, None),
                ("info.select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("info.report_replay", {"type": 'R', "value": 'PRESS'}, None),
                ("info.report_delete", {"type": 'X', "value": 'PRESS'}, None),
                ("info.report_delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("info.report_copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Outliner",
        {"space_type": 'OUTLINER', "region_type": 'WINDOW'},
        {
            "items": [
                ("outliner.highlight_update", {"type": 'MOUSEMOVE', "value": 'ANY', "any": True}, None),
                ("outliner.item_rename", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
                (
                    "outliner.item_activate",
                    {"type": 'LEFTMOUSE', "value": 'CLICK'},
                    {
                        "properties": [
                            ("extend", False),
                            ("recursive", False),
                        ],
                    }
                ),
                (
                    "outliner.item_activate",
                    {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("recursive", False),
                        ],
                    }
                ),
                (
                    "outliner.item_activate",
                    {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("recursive", True),
                        ],
                    }
                ),
                (
                    "outliner.item_activate",
                    {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("recursive", True),
                        ],
                    }
                ),
                ("outliner.select_border", {"type": 'B', "value": 'PRESS'}, None),
                (
                    "outliner.item_openclose",
                    {"type": 'RET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    }
                ),
                (
                    "outliner.item_openclose",
                    {"type": 'RET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("all", True),
                        ],
                    }
                ),
                ("outliner.item_rename", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("outliner.operation", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
                ("outliner.item_drag_drop", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
                ("outliner.show_hierarchy", {"type": 'HOME', "value": 'PRESS'}, None),
                ("outliner.show_active", {"type": 'PERIOD', "value": 'PRESS'}, None),
                ("outliner.show_active", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                (
                    "outliner.scroll_page",
                    {"type": 'PAGE_DOWN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("up", False),
                        ],
                    }
                ),
                (
                    "outliner.scroll_page",
                    {"type": 'PAGE_UP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("up", True),
                        ],
                    }
                ),
                ("outliner.show_one_level", {"type": 'NUMPAD_PLUS', "value": 'PRESS'}, None),
                (
                    "outliner.show_one_level",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("open", False),
                        ],
                    }
                ),
                (
                    "outliner.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                ("outliner.expanded_toggle", {"type": 'A', "value": 'PRESS', "shift": True}, None),
                ("outliner.keyingset_add_selected", {"type": 'K', "value": 'PRESS'}, None),
                ("outliner.keyingset_remove_selected", {"type": 'K', "value": 'PRESS', "alt": True}, None),
                ("anim.keyframe_insert", {"type": 'I', "value": 'PRESS'}, None),
                ("anim.keyframe_delete", {"type": 'I', "value": 'PRESS', "alt": True}, None),
                ("outliner.drivers_add_selected", {"type": 'D', "value": 'PRESS'}, None),
                ("outliner.drivers_delete_selected", {"type": 'D', "value": 'PRESS', "alt": True}, None),
                ("outliner.collection_new", {"type": 'C', "value": 'PRESS'}, None),
                ("outliner.collection_delete", {"type": 'X', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "3D View Generic",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("view3d.properties", {"type": 'N', "value": 'PRESS'}, None),
                ("view3d.toolshelf", {"type": 'T', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Grease Pencil",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "gpencil.draw",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "key_modifier": 'D'},
                    {
                        "properties": [
                            ("mode", 'DRAW'),
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "gpencil.draw",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True, "key_modifier": 'D'},
                    {
                        "properties": [
                            ("mode", 'DRAW_STRAIGHT'),
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "gpencil.draw",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "key_modifier": 'D'},
                    {
                        "properties": [
                            ("mode", 'DRAW_POLY'),
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "gpencil.draw",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "key_modifier": 'D'},
                    {
                        "properties": [
                            ("mode", 'ERASER'),
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "gpencil.draw",
                    {"type": 'ERASER', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'ERASER'),
                            ("wait_for_input", False),
                        ],
                    }
                ),
                ("gpencil.editmode_toggle", {"type": 'TAB', "value": 'PRESS', "key_modifier": 'D'}, None),
                (
                    "wm.call_menu_pie",
                    {"type": 'Q', "value": 'PRESS', "key_modifier": 'D'},
                    {
                        "properties": [
                            ("name", 'GPENCIL_MT_pie_tool_palette'),
                        ],
                    }
                ),
                (
                    "wm.call_menu_pie",
                    {"type": 'W', "value": 'PRESS', "key_modifier": 'D'},
                    {
                        "properties": [
                            ("name", 'GPENCIL_MT_pie_settings_palette'),
                        ],
                    }
                ),
                ("gpencil.blank_frame_add", {"type": 'B', "value": 'PRESS', "key_modifier": 'D'}, None),
                ("gpencil.active_frames_delete_all", {"type": 'X', "value": 'PRESS', "key_modifier": 'D'}, None),
            ],
        },
    ),
    (
        "Grease Pencil Stroke Edit Mode",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("gpencil.editmode_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
                (
                    "wm.call_menu_pie",
                    {"type": 'E', "value": 'PRESS', "key_modifier": 'D'},
                    {
                        "properties": [
                            ("name", 'GPENCIL_MT_pie_sculpt'),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path_primary", 'user_preferences.edit.grease_pencil_eraser_radius'),
                        ],
                    }
                ),
                ("gpencil.interpolate", {"type": 'E', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("gpencil.interpolate_sequence", {"type": 'E', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "gpencil.brush_paint",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "key_modifier": 'E'},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "gpencil.brush_paint",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True, "key_modifier": 'E'},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "gpencil.brush_paint",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "key_modifier": 'E'},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.gpencil_sculpt.brush.strength'),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.gpencil_sculpt.brush.size'),
                        ],
                    }
                ),
                (
                    "gpencil.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "gpencil.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("gpencil.select_circle", {"type": 'C', "value": 'PRESS'}, None),
                ("gpencil.select_border", {"type": 'B', "value": 'PRESS'}, None),
                (
                    "gpencil.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "gpencil.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                (
                    "gpencil.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "gpencil.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("gpencil.select", {"type": 'SELECTMOUSE', "value": 'PRESS'}, None),
                (
                    "gpencil.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "gpencil.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("entire_strokes", True),
                        ],
                    }
                ),
                ("gpencil.select_linked", {"type": 'L', "value": 'PRESS'}, None),
                ("gpencil.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
                ("gpencil.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                ("gpencil.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("gpencil.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("gpencil.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_gpencil_delete'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_gpencil_delete'),
                        ],
                    }
                ),
                ("gpencil.dissolve", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
                ("gpencil.dissolve", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
                ("gpencil.active_frames_delete_all", {"type": 'X', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'GPENCIL_MT_gpencil_edit_specials'),
                        ],
                    }
                ),
                ("gpencil.stroke_join", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
                (
                    "gpencil.stroke_join",
                    {"type": 'J', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'JOINCOPY'),
                        ],
                    }
                ),
                ("gpencil.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("gpencil.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'S', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'GPENCIL_MT_snap'),
                        ],
                    }
                ),
                ("gpencil.convert", {"type": 'C', "value": 'PRESS', "alt": True}, None),
                ("gpencil.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                (
                    "gpencil.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "gpencil.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("gpencil.selection_opacity_toggle", {"type": 'H', "value": 'PRESS', "ctrl": True}, None),
                ("gpencil.layer_isolate", {"type": 'NUMPAD_ASTERIX', "value": 'PRESS'}, None),
                ("gpencil.move_to_layer", {"type": 'M', "value": 'PRESS'}, None),
                (
                    "gpencil.brush_select",
                    {"type": 'ONE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 0),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'TWO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 1),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'THREE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 2),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'FOUR', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 3),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'FIVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 4),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'SIX', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 5),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'SEVEN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 6),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'EIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 7),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'NINE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 8),
                        ],
                    }
                ),
                (
                    "gpencil.brush_select",
                    {"type": 'ZERO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("index", 9),
                        ],
                    }
                ),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                ("transform.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
                ("transform.bend", {"type": 'W', "value": 'PRESS', "shift": True}, None),
                ("transform.tosphere", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True}, None),
                ("transform.shear", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'GPENCIL_SHRINKFATTEN'),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'ENABLED'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'CONNECTED'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Face Mask",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "paint.face_select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "paint.face_select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                (
                    "paint.face_select_hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "paint.face_select_hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("paint.face_select_reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                ("paint.face_select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
                (
                    "paint.face_select_linked_pick",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "paint.face_select_linked_pick",
                    {"type": 'L', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Weight Paint Vertex Selection",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "paint.vert_select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "paint.vert_select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("view3d.select_border", {"type": 'B', "value": 'PRESS'}, None),
                (
                    "view3d.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "view3d.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("view3d.select_circle", {"type": 'C', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Pose",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("object.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'INFO_MT_add'),
                        ],
                    }
                ),
                (
                    "pose.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "pose.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("pose.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_pose_apply'),
                        ],
                    }
                ),
                ("pose.rot_clear", {"type": 'R', "value": 'PRESS', "alt": True}, None),
                ("pose.loc_clear", {"type": 'G', "value": 'PRESS', "alt": True}, None),
                ("pose.scale_clear", {"type": 'S', "value": 'PRESS', "alt": True}, None),
                ("pose.quaternions_flip", {"type": 'F', "value": 'PRESS', "alt": True}, None),
                ("pose.rotation_mode_set", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
                ("pose.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                (
                    "pose.paste",
                    {"type": 'V', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("flipped", False),
                        ],
                    }
                ),
                (
                    "pose.paste",
                    {"type": 'V', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    }
                ),
                (
                    "pose.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "pose.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("pose.select_parent", {"type": 'P', "value": 'PRESS', "shift": True}, None),
                (
                    "pose.select_hierarchy",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'PARENT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "pose.select_hierarchy",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'PARENT'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "pose.select_hierarchy",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'CHILD'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "pose.select_hierarchy",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'CHILD'),
                            ("extend", True),
                        ],
                    }
                ),
                ("pose.select_linked", {"type": 'L', "value": 'PRESS'}, None),
                ("pose.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                ("pose.select_mirror", {"type": 'F', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("pose.constraint_add_with_targets", {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("pose.constraints_clear", {"type": 'C', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("pose.ik_add", {"type": 'I', "value": 'PRESS', "shift": True}, None),
                ("pose.ik_clear", {"type": 'I', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'G', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_pose_group'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_bone_options_toggle'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_bone_options_enable'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_bone_options_disable'),
                        ],
                    }
                ),
                ("armature.layers_show_all", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True}, None),
                ("armature.armature_layers", {"type": 'M', "value": 'PRESS', "shift": True}, None),
                ("pose.bone_layers", {"type": 'M', "value": 'PRESS'}, None),
                ("pose.toggle_bone_selection_overlay", {"type": 'Z', "value": 'PRESS'}, None),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'BONE_SIZE'),
                        ],
                    }
                ),
                ("anim.keyframe_insert_menu", {"type": 'I', "value": 'PRESS'}, None),
                ("anim.keyframe_delete_v3d", {"type": 'I', "value": 'PRESS', "alt": True}, None),
                ("anim.keying_set_active_set", {"type": 'I', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                ("poselib.browse_interactive", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
                ("poselib.pose_add", {"type": 'L', "value": 'PRESS', "shift": True}, None),
                ("poselib.pose_remove", {"type": 'L', "value": 'PRESS', "alt": True}, None),
                ("poselib.pose_rename", {"type": 'L', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("pose.push", {"type": 'E', "value": 'PRESS', "ctrl": True}, None),
                ("pose.relax", {"type": 'E', "value": 'PRESS', "alt": True}, None),
                ("pose.breakdown", {"type": 'E', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_pose_specials'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'P', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_pose_propagate'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Object Mode",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_proportional_edit_objects'),
                        ],
                    }
                ),
                (
                    "object.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "object.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("object.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("object.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("object.select_linked", {"type": 'L', "value": 'PRESS', "shift": True}, None),
                ("object.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                ("object.select_mirror", {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "object.select_hierarchy",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'PARENT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "object.select_hierarchy",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'PARENT'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "object.select_hierarchy",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'CHILD'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "object.select_hierarchy",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'CHILD'),
                            ("extend", True),
                        ],
                    }
                ),
                ("object.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                ("object.parent_no_inverse_set", {"type": 'P', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("object.parent_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
                ("object.track_set", {"type": 'T', "value": 'PRESS', "ctrl": True}, None),
                ("object.track_clear", {"type": 'T', "value": 'PRESS', "alt": True}, None),
                ("object.constraint_add_with_targets", {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("object.constraints_clear", {"type": 'C', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                (
                    "object.location_clear",
                    {"type": 'G', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("clear_delta", False),
                        ],
                    }
                ),
                (
                    "object.rotation_clear",
                    {"type": 'R', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("clear_delta", False),
                        ],
                    }
                ),
                (
                    "object.scale_clear",
                    {"type": 'S', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("clear_delta", False),
                        ],
                    }
                ),
                ("object.origin_clear", {"type": 'O', "value": 'PRESS', "alt": True}, None),
                (
                    "object.delete",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("use_global", False),
                        ],
                    }
                ),
                (
                    "object.delete",
                    {"type": 'X', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("use_global", True),
                        ],
                    }
                ),
                (
                    "object.delete",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("use_global", False),
                        ],
                    }
                ),
                (
                    "object.delete",
                    {"type": 'DEL', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("use_global", True),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'INFO_MT_add'),
                        ],
                    }
                ),
                ("object.duplicates_make_real", {"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_object_apply'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'U', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_make_single_user'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'L', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_make_links'),
                        ],
                    }
                ),
                ("object.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("object.duplicate_move_linked", {"type": 'D', "value": 'PRESS', "alt": True}, None),
                ("object.join", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
                ("object.convert", {"type": 'C', "value": 'PRESS', "alt": True}, None),
                ("object.proxy_make", {"type": 'P', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("object.make_local", {"type": 'L', "value": 'PRESS'}, None),
                ("anim.keyframe_insert_menu", {"type": 'I', "value": 'PRESS'}, None),
                ("anim.keyframe_delete_v3d", {"type": 'I', "value": 'PRESS', "alt": True}, None),
                ("anim.keying_set_active_set", {"type": 'I', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                ("collection.create", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
                ("collection.objects_remove", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("collection.objects_remove_all", {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                ("collection.objects_add_active", {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("collection.objects_remove_active", {"type": 'G', "value": 'PRESS', "shift": True, "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_object_specials'),
                        ],
                    }
                ),
                ("object.data_transfer", {"type": 'T', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "object.subdivision_set",
                    {"type": 'ZERO', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 0),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'ONE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 1),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'TWO', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 2),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'THREE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 3),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'FOUR', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 4),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'FIVE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 5),
                        ],
                    }
                ),
                ("object.move_to_collection", {"type": 'M', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Paint Curve",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("paintcurve.add_point_slide", {"type": 'ACTIONMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("paintcurve.select", {"type": 'SELECTMOUSE', "value": 'PRESS'}, None),
                (
                    "paintcurve.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                ("paintcurve.slide", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                (
                    "paintcurve.slide",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("align", True),
                        ],
                    }
                ),
                (
                    "paintcurve.select",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    }
                ),
                ("paintcurve.cursor", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                ("paintcurve.delete_point", {"type": 'X', "value": 'PRESS'}, None),
                ("paintcurve.delete_point", {"type": 'DEL', "value": 'PRESS'}, None),
                ("paintcurve.draw", {"type": 'RET', "value": 'PRESS'}, None),
                ("paintcurve.draw", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Curve",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'INFO_MT_edit_curve_add'),
                        ],
                    }
                ),
                ("curve.handle_type_set", {"type": 'V', "value": 'PRESS'}, None),
                ("curve.vertex_add", {"type": 'ACTIONMOUSE', "value": 'CLICK', "ctrl": True}, None),
                (
                    "curve.draw",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "curve.draw",
                    {"type": 'PEN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    }
                ),
                (
                    "curve.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "curve.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("curve.select_row", {"type": 'R', "value": 'PRESS', "shift": True}, None),
                ("curve.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("curve.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("curve.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
                ("curve.select_similar", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                (
                    "curve.select_linked_pick",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "curve.select_linked_pick",
                    {"type": 'L', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("curve.shortest_path_pick", {"type": 'SELECTMOUSE', "value": 'CLICK', "ctrl": True}, None),
                ("curve.separate", {"type": 'P', "value": 'PRESS'}, None),
                ("curve.split", {"type": 'Y', "value": 'PRESS'}, None),
                ("curve.extrude_move", {"type": 'E', "value": 'PRESS'}, None),
                ("curve.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("curve.make_segment", {"type": 'F', "value": 'PRESS'}, None),
                ("curve.cyclic_toggle", {"type": 'C', "value": 'PRESS', "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_curve_delete'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_curve_delete'),
                        ],
                    }
                ),
                ("curve.dissolve_verts", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
                ("curve.dissolve_verts", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
                ("curve.tilt_clear", {"type": 'T', "value": 'PRESS', "alt": True}, None),
                ("transform.tilt", {"type": 'T', "value": 'PRESS', "ctrl": True}, None),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'CURVE_SHRINKFATTEN'),
                        ],
                    }
                ),
                ("curve.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                (
                    "curve.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "curve.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("curve.normals_make_consistent", {"type": 'N', "value": 'PRESS', "ctrl": True}, None),
                ("object.vertex_parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_curve_specials'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'H', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_hook'),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'ENABLED'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'CONNECTED'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Image Paint",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "paint.image_paint",
                    {"type": 'LEFTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'NORMAL'),
                        ],
                    }
                ),
                (
                    "paint.image_paint",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'INVERT'),
                        ],
                    }
                ),
                ("paint.brush_colors_flip", {"type": 'X', "value": 'PRESS'}, None),
                ("paint.grab_clone", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
                ("paint.sample_color", {"type": 'S', "value": 'PRESS'}, None),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 0),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 1),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 2),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 3),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 4),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 5),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 6),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 7),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 8),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 9),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 10),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 11),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 12),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 13),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 14),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 15),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 16),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 17),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 18),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'image_paint'),
                            ("index", 19),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 0.9),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 1.1111112),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.image_paint.brush.size'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.size'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),
                            ("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
                            ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
                            ("fill_color_path", 'tool_settings.image_paint.brush.color'),
                            ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
                            ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
                            ("zoom_path", 'space_data.zoom'),
                            ("image_id", 'tool_settings.image_paint.brush'),
                            ("secondary_tex", True),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.image_paint.brush.strength'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),
                            ("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
                            ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
                            ("fill_color_path", 'tool_settings.image_paint.brush.color'),
                            ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
                            ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.image_paint.brush'),
                            ("secondary_tex", True),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.image_paint.brush.texture_slot.angle'),
                            ("data_path_secondary", ''),
                            ("use_secondary", ''),
                            ("rotation_path", 'tool_settings.image_paint.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
                            ("fill_color_path", 'tool_settings.image_paint.brush.color'),
                            ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
                            ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.image_paint.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
                            ("data_path_secondary", ''),
                            ("use_secondary", ''),
                            ("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
                            ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
                            ("fill_color_path", 'tool_settings.image_paint.brush.color'),
                            ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
                            ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.image_paint.brush'),
                            ("secondary_tex", True),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'SCALE'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'ROTATION'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'SCALE'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'ROTATION'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'M', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'image_paint_object.data.use_paint_mask'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'S', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.image_paint.brush.use_smooth_stroke'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'R', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_angle_control'),
                        ],
                    }
                ),
                (
                    "wm.context_menu_enum",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.image_paint.brush.stroke_method'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Vertex Paint",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("paint.vertex_paint", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("paint.brush_colors_flip", {"type": 'X', "value": 'PRESS'}, None),
                ("paint.sample_color", {"type": 'S', "value": 'PRESS'}, None),
                ("paint.vertex_color_set", {"type": 'K', "value": 'PRESS', "shift": True}, None),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 0),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 1),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 2),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 3),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 4),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 5),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 6),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 7),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 8),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 9),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 10),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 11),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 12),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 13),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 14),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 15),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 16),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 17),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 18),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'vertex_paint'),
                            ("index", 19),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 0.9),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 1.1111112),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.vertex_paint.brush.size'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.size'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),
                            ("rotation_path", 'tool_settings.vertex_paint.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.vertex_paint.brush.cursor_color_add'),
                            ("fill_color_path", 'tool_settings.vertex_paint.brush.color'),
                            ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
                            ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.vertex_paint.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.vertex_paint.brush.strength'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),
                            ("rotation_path", 'tool_settings.vertex_paint.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.vertex_paint.brush.cursor_color_add'),
                            ("fill_color_path", 'tool_settings.vertex_paint.brush.color'),
                            ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
                            ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.vertex_paint.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.vertex_paint.brush.texture_slot.angle'),
                            ("data_path_secondary", ''),
                            ("use_secondary", ''),
                            ("rotation_path", 'tool_settings.vertex_paint.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.vertex_paint.brush.cursor_color_add'),
                            ("fill_color_path", 'tool_settings.vertex_paint.brush.color'),
                            ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
                            ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.vertex_paint.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'SCALE'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'ROTATION'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'SCALE'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'ROTATION'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'M', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'vertex_paint_object.data.use_paint_mask'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'S', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.vertex_paint.brush.use_smooth_stroke'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'R', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_angle_control'),
                        ],
                    }
                ),
                (
                    "wm.context_menu_enum",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.vertex_paint.brush.stroke_method'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Weight Paint",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("paint.weight_paint", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("paint.weight_sample", {"type": 'ACTIONMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("paint.weight_sample_group", {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True}, None),
                (
                    "paint.weight_gradient",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("type", 'LINEAR'),
                        ],
                    }
                ),
                (
                    "paint.weight_gradient",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("type", 'RADIAL'),
                        ],
                    }
                ),
                ("paint.weight_set", {"type": 'K', "value": 'PRESS', "shift": True}, None),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 0),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 1),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 2),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 3),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 4),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 5),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 6),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 7),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 8),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 9),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 10),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 11),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 12),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 13),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 14),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 15),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 16),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 17),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 18),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'weight_paint'),
                            ("index", 19),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 0.9),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 1.1111112),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.weight_paint.brush.size'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.size'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),
                            ("rotation_path", 'tool_settings.weight_paint.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.weight_paint.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.weight_paint.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.weight_paint.brush.strength'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),
                            ("rotation_path", 'tool_settings.weight_paint.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.weight_paint.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.weight_paint.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.weight_paint.brush.weight'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.weight'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_weight'),
                            ("rotation_path", 'tool_settings.weight_paint.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.weight_paint.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.weight_paint.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.context_menu_enum",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.vertex_paint.brush.stroke_method'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'M', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'weight_paint_object.data.use_paint_mask'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'V', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'weight_paint_object.data.use_paint_mask_vertex'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'S', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.weight_paint.brush.use_smooth_stroke'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Sculpt",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "sculpt.brush_stroke",
                    {"type": 'LEFTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'NORMAL'),
                        ],
                    }
                ),
                (
                    "sculpt.brush_stroke",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'INVERT'),
                        ],
                    }
                ),
                (
                    "sculpt.brush_stroke",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'SMOOTH'),
                        ],
                    }
                ),
                (
                    "paint.hide_show",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("action", 'SHOW'),
                            ("area", 'INSIDE'),
                        ],
                    }
                ),
                (
                    "paint.hide_show",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'HIDE'),
                            ("area", 'INSIDE'),
                        ],
                    }
                ),
                (
                    "paint.hide_show",
                    {"type": 'H', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("action", 'SHOW'),
                            ("area", 'ALL'),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'ZERO', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 0),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'ONE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 1),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'TWO', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 2),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'THREE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 3),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'FOUR', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 4),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'FIVE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 5),
                        ],
                    }
                ),
                (
                    "paint.mask_flood_fill",
                    {"type": 'M', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'VALUE'),
                            ("value", 0.0),
                        ],
                    }
                ),
                (
                    "paint.mask_flood_fill",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'INVERT'),
                        ],
                    }
                ),
                ("paint.mask_lasso_gesture", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "wm.context_toggle",
                    {"type": 'M', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'scene.tool_settings.sculpt.show_mask'),
                        ],
                    }
                ),
                ("sculpt.dynamic_topology_toggle", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
                ("sculpt.set_detail_size", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                (
                    "object.subdivision_set",
                    {"type": 'PAGE_UP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("level", 1),
                            ("relative", True),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'PAGE_DOWN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("level", -1),
                            ("relative", True),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 0),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 1),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 2),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 3),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 4),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 5),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 6),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 7),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 8),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 9),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ONE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 10),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'TWO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 11),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'THREE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 12),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FOUR', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 13),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'FIVE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 14),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SIX', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 15),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'SEVEN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 16),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'EIGHT', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 17),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'NINE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 18),
                        ],
                    }
                ),
                (
                    "brush.active_index_set",
                    {"type": 'ZERO', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'sculpt'),
                            ("index", 19),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 0.9),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 1.1111112),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.sculpt.brush.size'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.size'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),
                            ("rotation_path", 'tool_settings.sculpt.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.sculpt.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.sculpt.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.sculpt.brush.strength'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),
                            ("rotation_path", 'tool_settings.sculpt.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.sculpt.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.sculpt.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.sculpt.brush.texture_slot.angle'),
                            ("data_path_secondary", ''),
                            ("use_secondary", ''),
                            ("rotation_path", 'tool_settings.sculpt.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.sculpt.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.sculpt.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'SCALE'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'ROTATION'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'SCALE'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "brush.stencil_control",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'ROTATION'),
                            ("texmode", 'SECONDARY'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'DRAW'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'S', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'SMOOTH'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'P', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'PINCH'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'I', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'INFLATE'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'G', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'GRAB'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'LAYER'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'T', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'FLATTEN'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'C', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'CLAY'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'C', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'CREASE'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'K', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'SNAKE_HOOK'),
                        ],
                    }
                ),
                (
                    "paint.brush_select",
                    {"type": 'M', "value": 'PRESS'},
                    {
                        "properties": [
                            ("paint_mode", 'SCULPT'),
                            ("sculpt_tool", 'MASK'),
                            ("toggle", True),
                            ("create_missing", True),
                        ],
                    }
                ),
                (
                    "wm.context_menu_enum",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.sculpt.brush.stroke_method'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'S', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.sculpt.brush.use_smooth_stroke'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'R', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_angle_control'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Mesh",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("mesh.loopcut_slide", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
                ("mesh.offset_edge_loops_slide", {"type": 'R', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("mesh.inset", {"type": 'I', "value": 'PRESS'}, None),
                ("mesh.poke", {"type": 'P', "value": 'PRESS', "alt": True}, None),
                (
                    "mesh.bevel",
                    {"type": 'B', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("vertex_only", False),
                        ],
                    }
                ),
                (
                    "mesh.bevel",
                    {"type": 'B', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("vertex_only", True),
                        ],
                    }
                ),
                (
                    "mesh.loop_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                        ],
                    }
                ),
                (
                    "mesh.loop_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "mesh.edgering_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                        ],
                    }
                ),
                (
                    "mesh.edgering_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "mesh.shortest_path_pick",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("use_fill", False),
                        ],
                    }
                ),
                (
                    "mesh.shortest_path_pick",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_fill", True),
                        ],
                    }
                ),
                (
                    "mesh.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "mesh.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("mesh.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("mesh.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("mesh.select_next_item", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("mesh.select_prev_item", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("mesh.select_non_manifold", {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                ("mesh.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
                (
                    "mesh.select_linked_pick",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "mesh.select_linked_pick",
                    {"type": 'L', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("mesh.faces_select_linked_flat", {"type": 'F', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'G', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_select_similar'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'TAB', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_select_mode'),
                        ],
                    }
                ),
                (
                    "mesh.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "mesh.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("mesh.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                (
                    "mesh.normals_make_consistent",
                    {"type": 'N', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("inside", False),
                        ],
                    }
                ),
                (
                    "mesh.normals_make_consistent",
                    {"type": 'N', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("inside", True),
                        ],
                    }
                ),
                ("view3d.edit_mesh_extrude_move_normal", {"type": 'E', "value": 'PRESS'}, None),
                (
                    "wm.call_menu",
                    {"type": 'E', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_extrude'),
                        ],
                    }
                ),
                ("transform.edge_crease", {"type": 'E', "value": 'PRESS', "shift": True}, None),
                ("mesh.spin", {"type": 'R', "value": 'PRESS', "alt": True}, None),
                ("mesh.fill", {"type": 'F', "value": 'PRESS', "alt": True}, None),
                ("mesh.beautify_fill", {"type": 'F', "value": 'PRESS', "shift": True, "alt": True}, None),
                (
                    "mesh.quads_convert_to_tris",
                    {"type": 'T', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("quad_method", 'BEAUTY'),
                            ("ngon_method", 'BEAUTY'),
                        ],
                    }
                ),
                (
                    "mesh.quads_convert_to_tris",
                    {"type": 'T', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("quad_method", 'FIXED'),
                            ("ngon_method", 'CLIP'),
                        ],
                    }
                ),
                ("mesh.tris_convert_to_quads", {"type": 'J', "value": 'PRESS', "alt": True}, None),
                (
                    "mesh.rip_move",
                    {"type": 'V', "value": 'PRESS'},
                    {
                        "properties": [
                            (
                                "MESH_OT_rip",
                                [
                                    ("use_fill", False),
                                ],
                            ),
                        ],
                    }
                ),
                (
                    "mesh.rip_move",
                    {"type": 'V', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            (
                                "MESH_OT_rip",
                                [
                                    ("use_fill", True),
                                ],
                            ),
                        ],
                    }
                ),
                ("mesh.rip_edge_move", {"type": 'D', "value": 'PRESS', "alt": True}, None),
                ("mesh.merge", {"type": 'M', "value": 'PRESS', "alt": True}, None),
                ("transform.shrink_fatten", {"type": 'S', "value": 'PRESS', "alt": True}, None),
                ("mesh.edge_face_add", {"type": 'F', "value": 'PRESS'}, None),
                ("mesh.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'INFO_MT_mesh_add'),
                        ],
                    }
                ),
                ("mesh.separate", {"type": 'P', "value": 'PRESS'}, None),
                ("mesh.split", {"type": 'Y', "value": 'PRESS'}, None),
                ("mesh.vert_connect_path", {"type": 'J', "value": 'PRESS'}, None),
                ("transform.vert_slide", {"type": 'V', "value": 'PRESS', "shift": True}, None),
                (
                    "mesh.dupli_extrude_cursor",
                    {"type": 'ACTIONMOUSE', "value": 'CLICK', "ctrl": True},
                    {
                        "properties": [
                            ("rotate_source", True),
                        ],
                    }
                ),
                (
                    "mesh.dupli_extrude_cursor",
                    {"type": 'ACTIONMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("rotate_source", False),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_delete'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_delete'),
                        ],
                    }
                ),
                ("mesh.dissolve_mode", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
                ("mesh.dissolve_mode", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
                (
                    "mesh.knife_tool",
                    {"type": 'K', "value": 'PRESS'},
                    {
                        "properties": [
                            ("use_occlude_geometry", True),
                            ("only_selected", False),
                        ],
                    }
                ),
                (
                    "mesh.knife_tool",
                    {"type": 'K', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("use_occlude_geometry", False),
                            ("only_selected", True),
                        ],
                    }
                ),
                ("object.vertex_parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_specials'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'F', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_faces'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'E', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_edges'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'V', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_mesh_vertices'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'H', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_hook'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'U', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_uv_map'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'G', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_vertex_group'),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'ZERO', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 0),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'ONE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 1),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'TWO', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 2),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'THREE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 3),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'FOUR', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 4),
                        ],
                    }
                ),
                (
                    "object.subdivision_set",
                    {"type": 'FIVE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("level", 5),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'ENABLED'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'CONNECTED'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Armature",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "armature.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "armature.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("armature.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                ("armature.align", {"type": 'A', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("armature.calculate_roll", {"type": 'N', "value": 'PRESS', "ctrl": True}, None),
                ("armature.roll_clear", {"type": 'R', "value": 'PRESS', "alt": True}, None),
                ("armature.switch_direction", {"type": 'F', "value": 'PRESS', "alt": True}, None),
                ("armature.bone_primitive_add", {"type": 'A', "value": 'PRESS', "shift": True}, None),
                ("armature.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                ("armature.parent_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
                (
                    "armature.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "armature.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                (
                    "armature.select_mirror",
                    {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "armature.select_hierarchy",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'PARENT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "armature.select_hierarchy",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'PARENT'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "armature.select_hierarchy",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'CHILD'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "armature.select_hierarchy",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'CHILD'),
                            ("extend", True),
                        ],
                    }
                ),
                ("armature.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("armature.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("armature.select_similar", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                ("armature.select_linked", {"type": 'L', "value": 'PRESS'}, None),
                ("armature.shortest_path_pick", {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_armature_delete'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_edit_armature_delete'),
                        ],
                    }
                ),
                ("armature.dissolve", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
                ("armature.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("armature.extrude_move", {"type": 'E', "value": 'PRESS'}, None),
                ("armature.extrude_forked", {"type": 'E', "value": 'PRESS', "shift": True}, None),
                ("armature.click_extrude", {"type": 'ACTIONMOUSE', "value": 'CLICK', "ctrl": True}, None),
                ("armature.fill", {"type": 'F', "value": 'PRESS'}, None),
                ("armature.merge", {"type": 'M', "value": 'PRESS', "alt": True}, None),
                ("armature.split", {"type": 'Y', "value": 'PRESS'}, None),
                ("armature.separate", {"type": 'P', "value": 'PRESS'}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_bone_options_toggle'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_bone_options_enable'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_bone_options_disable'),
                        ],
                    }
                ),
                ("armature.layers_show_all", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True}, None),
                ("armature.armature_layers", {"type": 'M', "value": 'PRESS', "shift": True}, None),
                ("armature.bone_layers", {"type": 'M', "value": 'PRESS'}, None),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", 'BONE_SIZE'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'BONE_ENVELOPE'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'R', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'BONE_ROLL'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_armature_specials'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Metaball",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("object.metaball_add", {"type": 'A', "value": 'PRESS', "shift": True}, None),
                ("mball.reveal_metaelems", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                (
                    "mball.hide_metaelems",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "mball.hide_metaelems",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("mball.delete_metaelems", {"type": 'X', "value": 'PRESS'}, None),
                ("mball.delete_metaelems", {"type": 'DEL', "value": 'PRESS'}, None),
                ("mball.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                (
                    "mball.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "mball.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("mball.select_similar", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'ENABLED'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'CONNECTED'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Lattice",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "lattice.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "lattice.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("lattice.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("lattice.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("object.vertex_parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                ("lattice.flip", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'H', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_hook'),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'ENABLED'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Particle",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "particle.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "particle.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("particle.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("particle.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                (
                    "particle.select_linked",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "particle.select_linked",
                    {"type": 'L', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("particle.delete", {"type": 'X', "value": 'PRESS'}, None),
                ("particle.delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("particle.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                (
                    "particle.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "particle.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("particle.brush_edit", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("particle.brush_edit", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.particle_edit.brush.size'),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.particle_edit.brush.strength'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_particle_specials'),
                        ],
                    }
                ),
                ("particle.weight_set", {"type": 'K', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'ENABLED'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Font",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "font.style_toggle",
                    {"type": 'B', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("style", 'BOLD'),
                        ],
                    }
                ),
                (
                    "font.style_toggle",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("style", 'ITALIC'),
                        ],
                    }
                ),
                (
                    "font.style_toggle",
                    {"type": 'U', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("style", 'UNDERLINE'),
                        ],
                    }
                ),
                (
                    "font.style_toggle",
                    {"type": 'P', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("style", 'SMALL_CAPS'),
                        ],
                    }
                ),
                (
                    "font.delete",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_OR_SELECTION'),
                        ],
                    }
                ),
                (
                    "font.delete",
                    {"type": 'DEL', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "font.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_OR_SELECTION'),
                        ],
                    }
                ),
                (
                    "font.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_OR_SELECTION'),
                        ],
                    }
                ),
                (
                    "font.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'HOME', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LINE_BEGIN'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'END', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LINE_END'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'LEFT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_CHARACTER'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'UP_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_LINE'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'DOWN_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_LINE'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'PAGE_UP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_PAGE'),
                        ],
                    }
                ),
                (
                    "font.move",
                    {"type": 'PAGE_DOWN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_PAGE'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'HOME', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'LINE_BEGIN'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'END', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'LINE_END'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'NEXT_CHARACTER'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'UP_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_LINE'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'NEXT_LINE'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'PAGE_UP', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_PAGE'),
                        ],
                    }
                ),
                (
                    "font.move_select",
                    {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'NEXT_PAGE'),
                        ],
                    }
                ),
                (
                    "font.change_spacing",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                (
                    "font.change_spacing",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "font.change_character",
                    {"type": 'UP_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "font.change_character",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                ("font.select_all", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
                ("font.text_copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("font.text_cut", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
                ("font.text_paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                ("font.line_break", {"type": 'RET', "value": 'PRESS'}, None),
                ("font.text_insert", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),
                (
                    "font.text_insert",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("accent", True),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Object Non-modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "object.mode_set",
                    {"type": 'TAB', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'EDIT'),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "object.mode_set",
                    {"type": 'TAB', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'POSE'),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "object.mode_set",
                    {"type": 'V', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'VERTEX_PAINT'),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "object.mode_set",
                    {"type": 'TAB', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'WEIGHT_PAINT'),
                            ("toggle", True),
                        ],
                    }
                ),
                ("object.origin_set", {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
            ],
        },
    ),
    (
        "3D View",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("view3d.cursor3d", {"type": 'ACTIONMOUSE', "value": 'CLICK'}, None),
                ("view3d.rotate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("view3d.move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
                ("view3d.zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("view3d.dolly", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "view3d.view_selected",
                    {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                        ],
                    }
                ),
                (
                    "view3d.view_selected",
                    {"type": 'NUMPAD_PERIOD', "value": 'PRESS'},
                    {
                        "properties": [
                            ("use_all_regions", False),
                        ],
                    }
                ),
                ("view3d.view_lock_to_active", {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "shift": True}, None),
                ("view3d.view_lock_clear", {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "alt": True}, None),
                ("view3d.navigate", {"type": 'F', "value": 'PRESS', "shift": True}, None),
                ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
                ("view3d.rotate", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("view3d.rotate", {"type": 'MOUSEROTATE', "value": 'ANY'}, None),
                ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
                ("view3d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
                ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
                (
                    "view3d.zoom",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "view3d.zoom",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                (
                    "view3d.zoom",
                    {"type": 'EQUAL', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "view3d.zoom",
                    {"type": 'MINUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                (
                    "view3d.zoom",
                    {"type": 'WHEELINMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "view3d.zoom",
                    {"type": 'WHEELOUTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                (
                    "view3d.dolly",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "view3d.dolly",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                (
                    "view3d.dolly",
                    {"type": 'EQUAL', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    }
                ),
                (
                    "view3d.dolly",
                    {"type": 'MINUS', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    }
                ),
                ("view3d.zoom_camera_1_to_1", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "shift": True}, None),
                ("view3d.view_center_camera", {"type": 'HOME', "value": 'PRESS'}, None),
                ("view3d.view_center_lock", {"type": 'HOME', "value": 'PRESS'}, None),
                ("view3d.view_center_cursor", {"type": 'HOME', "value": 'PRESS', "alt": True}, None),
                ("view3d.view_center_pick", {"type": 'F', "value": 'PRESS', "alt": True}, None),
                (
                    "view3d.view_all",
                    {"type": 'HOME', "value": 'PRESS'},
                    {
                        "properties": [
                            ("center", False),
                        ],
                    }
                ),
                (
                    "view3d.view_all",
                    {"type": 'HOME', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                            ("center", False),
                        ],
                    }
                ),
                (
                    "view3d.view_all",
                    {"type": 'C', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("center", True),
                        ],
                    }
                ),
                ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_1', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'FRONT'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'NUMPAD_2', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'ORBITDOWN'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_3', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'RIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'NUMPAD_4', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'ORBITLEFT'),
                        ],
                    }
                ),
                ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS'}, None),
                (
                    "view3d.view_orbit",
                    {"type": 'NUMPAD_6', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'ORBITRIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_7', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'TOP'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'NUMPAD_8', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'ORBITUP'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'BACK'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'LEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'BOTTOM'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PANDOWN'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PANLEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PANRIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PANUP'),
                        ],
                    }
                ),
                (
                    "view3d.view_roll",
                    {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'LEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_roll",
                    {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'RIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'NUMPAD_9', "value": 'PRESS'},
                    {
                        "properties": [
                            ("angle", 3.1415927),
                            ("type", 'ORBITRIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PANRIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PANLEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PANUP'),
                        ],
                    }
                ),
                (
                    "view3d.view_pan",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PANDOWN'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("type", 'ORBITLEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("type", 'ORBITRIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("type", 'ORBITUP'),
                        ],
                    }
                ),
                (
                    "view3d.view_orbit",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("type", 'ORBITDOWN'),
                        ],
                    }
                ),
                (
                    "view3d.view_roll",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'LEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_roll",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'RIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'FRONT'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'RIGHT'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'TOP'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'BACK'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'LEFT'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'BOTTOM'),
                            ("align_active", True),
                        ],
                    }
                ),
                ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
                ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
                ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
                ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
                (
                    "view3d.view_selected",
                    {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("use_all_regions", False),
                        ],
                    }
                ),
                (
                    "view3d.view_roll",
                    {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_roll",
                    {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'RIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'FRONT'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'BACK'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LEFT'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'RIGHT'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'TOP'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'BOTTOM'),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'FRONT'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'RIGHT'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.view_axis",
                    {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'TOP'),
                            ("align_active", True),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'ACCENT_GRAVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("nr", 0),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'ONE', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 1),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'TWO', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 2),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'THREE', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 3),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'FOUR', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 4),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'FIVE', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 5),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'SIX', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 6),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'SEVEN', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 7),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'EIGHT', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 8),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'NINE', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 9),
                        ],
                    }
                ),
                (
                    "view3d.layers",
                    {"type": 'ZERO', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("nr", 10),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'Z', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.shading.type'),
                            ("value_1", 'SOLID'),
                            ("value_2", 'TEXTURED'),
                        ],
                    }
                ),
                ("view3d.toggle_render", {"type": 'Z', "value": 'PRESS', "shift": True}, None),
                ("view3d.toggle_xray_draw_option", {"type": 'Z', "value": 'PRESS'}, None),
                (
                    "wm.context_toggle",
                    {"type": 'Z', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.use_occlude_geometry'),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                            ("center", False),
                            ("enumerate", False),
                            ("object", False),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", True),
                            ("center", False),
                            ("enumerate", False),
                            ("object", False),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                            ("center", True),
                            ("enumerate", False),
                            ("object", True),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                            ("center", False),
                            ("enumerate", True),
                            ("object", False),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect", False),
                            ("toggle", True),
                            ("center", True),
                            ("enumerate", False),
                            ("object", False),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                            ("center", True),
                            ("enumerate", True),
                            ("object", False),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", True),
                            ("center", False),
                            ("enumerate", True),
                            ("object", False),
                        ],
                    }
                ),
                (
                    "view3d.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", True),
                            ("center", True),
                            ("enumerate", True),
                            ("object", False),
                        ],
                    }
                ),
                ("view3d.select_border", {"type": 'B', "value": 'PRESS'}, None),
                (
                    "view3d.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "view3d.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("view3d.select_circle", {"type": 'C', "value": 'PRESS'}, None),
                ("view3d.clip_border", {"type": 'B', "value": 'PRESS', "alt": True}, None),
                ("view3d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
                (
                    "view3d.render_border",
                    {"type": 'B', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("camera_only", True),
                        ],
                    }
                ),
                (
                    "view3d.render_border",
                    {"type": 'B', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("camera_only", False),
                        ],
                    }
                ),
                ("view3d.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("view3d.camera_to_view", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("view3d.object_as_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'S', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'VIEW3D_MT_snap'),
                        ],
                    }
                ),
                ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.context_set_enum",
                    {"type": 'COMMA', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.transform_pivot_point'),
                            ("value", 'BOUNDING_BOX_CENTER'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'COMMA', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.transform_pivot_point'),
                            ("value", 'MEDIAN_POINT'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'COMMA', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_transform_pivot_point_align'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.transform_pivot_point'),
                            ("value", 'CURSOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.transform_pivot_point'),
                            ("value", 'INDIVIDUAL_ORIGINS'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.transform_pivot_point'),
                            ("value", 'ACTIVE_ELEMENT'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'SPACE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.show_manipulator'),
                        ],
                    }
                ),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                ("transform.bend", {"type": 'W', "value": 'PRESS', "shift": True}, None),
                ("transform.tosphere", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True}, None),
                ("transform.shear", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                ("transform.select_orientation", {"type": 'SPACE', "value": 'PRESS', "alt": True}, None),
                (
                    "transform.create_orientation",
                    {"type": 'SPACE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("use", True),
                        ],
                    }
                ),
                ("transform.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.context_toggle",
                    {"type": 'TAB', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_snap'),
                        ],
                    }
                ),
                (
                    "wm.context_menu_enum",
                    {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.snap_element'),
                        ],
                    }
                ),
                ("object.transform_axis_target", {"type": 'T', "value": 'PRESS', "shift": True}, None),
                (
                    "transform.translate",
                    {"type": 'T', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("texture_space", True),
                        ],
                    }
                ),
                (
                    "transform.resize",
                    {"type": 'T', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("texture_space", True),
                        ],
                    }
                ),
                ("transform.skin_resize", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Manipulators",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
            ],
        },
    ),
    (
        "Backdrop Transform Widget",
        {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Backdrop Transform Widget Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Backdrop Crop Widget",
        {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Backdrop Crop Widget Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Sun Beams Widget",
        {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Sun Beams Widget Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Corner Pin Widget",
        {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Corner Pin Widget Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "UV Transform Manipulator",
        {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "UV Transform Manipulator Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Spot Light Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Spot Light Widgets Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Area Light Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Area Light Widgets Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Target Light Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Target Light Widgets Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Force Field Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Force Field Widgets Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Camera Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Camera Widgets Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Camera View Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Camera View Widgets Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Armature Spline Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Armature Spline Widgets Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Navigate",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Navigate Tweak Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("PRECISION_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Gesture Circle",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
                ("SELECT", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("DESELECT", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
                ("NOP", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
                ("DESELECT", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("NOP", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
                ("SUBTRACT", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
                ("SUBTRACT", {"type": 'NUMPAD_MINUS', "value": 'PRESS'}, None),
                ("ADD", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
                ("ADD", {"type": 'NUMPAD_PLUS', "value": 'PRESS'}, None),
                ("SIZE", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
            ],
        },
    ),
    (
        "Gesture Border",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("SELECT", {"type": 'RIGHTMOUSE', "value": 'RELEASE', "any": True}, None),
                ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
                ("DESELECT", {"type": 'LEFTMOUSE', "value": 'RELEASE', "shift": True}, None),
                ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("SELECT", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
                ("BEGIN", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("DESELECT", {"type": 'MIDDLEMOUSE', "value": 'RELEASE'}, None),
            ],
        },
    ),
    (
        "Gesture Zoom Border",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
                ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("IN", {"type": 'LEFTMOUSE', "value": 'RELEASE'}, None),
                ("BEGIN", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("OUT", {"type": 'MIDDLEMOUSE', "value": 'RELEASE'}, None),
            ],
        },
    ),
    (
        "Gesture Straight Line",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
                ("BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("SELECT", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Standard Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("APPLY", {"type": 'LEFTMOUSE', "value": 'ANY', "any": True}, None),
                ("APPLY", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("APPLY", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("SNAP", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Animation",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("anim.change_frame", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                (
                    "wm.context_toggle",
                    {"type": 'T', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.show_seconds'),
                        ],
                    }
                ),
                ("anim.previewrange_set", {"type": 'P', "value": 'PRESS'}, None),
                ("anim.previewrange_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
            ],
        },
    ),
    (
        "Animation Channels",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("anim.channels_click", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                (
                    "anim.channels_click",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "anim.channels_click",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("children_only", True),
                        ],
                    }
                ),
                ("anim.channels_rename", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("anim.channels_rename", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
                ("anim.channel_select_keys", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
                (
                    "anim.channel_select_keys",
                    {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
                (
                    "anim.channels_select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "anim.channels_select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("anim.channels_select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("anim.channels_select_border", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
                ("anim.channels_delete", {"type": 'X', "value": 'PRESS'}, None),
                ("anim.channels_delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("anim.channels_setting_toggle", {"type": 'W', "value": 'PRESS', "shift": True}, None),
                ("anim.channels_setting_enable", {"type": 'W', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("anim.channels_setting_disable", {"type": 'W', "value": 'PRESS', "alt": True}, None),
                ("anim.channels_editable_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
                ("anim.channels_expand", {"type": 'NUMPAD_PLUS', "value": 'PRESS'}, None),
                ("anim.channels_collapse", {"type": 'NUMPAD_MINUS', "value": 'PRESS'}, None),
                (
                    "anim.channels_expand",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    }
                ),
                (
                    "anim.channels_collapse",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    }
                ),
                (
                    "anim.channels_move",
                    {"type": 'PAGE_UP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'UP'),
                        ],
                    }
                ),
                (
                    "anim.channels_move",
                    {"type": 'PAGE_DOWN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'DOWN'),
                        ],
                    }
                ),
                (
                    "anim.channels_move",
                    {"type": 'PAGE_UP', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'TOP'),
                        ],
                    }
                ),
                (
                    "anim.channels_move",
                    {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'BOTTOM'),
                        ],
                    }
                ),
                ("anim.channels_group", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
                ("anim.channels_ungroup", {"type": 'G', "value": 'PRESS', "alt": True}, None),
            ],
        },
    ),
    (
        "Knife Tool Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("PANNING", {"type": 'MIDDLEMOUSE', "value": 'ANY', "any": True}, None),
                ("CANCEL", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "any": True}, None),
                ("ADD_CUT", {"type": 'LEFTMOUSE', "value": 'ANY', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'SPACE', "value": 'PRESS', "any": True}, None),
                ("NEW_CUT", {"type": 'E', "value": 'PRESS'}, None),
                ("SNAP_MIDPOINTS_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_MIDPOINTS_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_MIDPOINTS_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_MIDPOINTS_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("IGNORE_SNAP_ON", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("IGNORE_SNAP_OFF", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("IGNORE_SNAP_ON", {"type": 'RIGHT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("IGNORE_SNAP_OFF", {"type": 'RIGHT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("ANGLE_SNAP_TOGGLE", {"type": 'C', "value": 'PRESS'}, None),
                ("CUT_THROUGH_TOGGLE", {"type": 'Z', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "UV Editor",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": 'Q', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_uv_sculpt'),
                        ],
                    }
                ),
                ("uv.mark_seam", {"type": 'E', "value": 'PRESS', "ctrl": True}, None),
                (
                    "uv.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "uv.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "uv.select_loop",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "uv.select_loop",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                ("uv.select_split", {"type": 'Y', "value": 'PRESS'}, None),
                (
                    "uv.select_border",
                    {"type": 'B', "value": 'PRESS'},
                    {
                        "properties": [
                            ("pinned", False),
                        ],
                    }
                ),
                (
                    "uv.select_border",
                    {"type": 'B', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("pinned", True),
                        ],
                    }
                ),
                ("uv.circle_select", {"type": 'C', "value": 'PRESS'}, None),
                (
                    "uv.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "uv.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                (
                    "uv.select_linked",
                    {"type": 'L', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "uv.select_linked_pick",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "uv.select_linked",
                    {"type": 'L', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", True),
                        ],
                    }
                ),
                (
                    "uv.select_linked_pick",
                    {"type": 'L', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", True),
                        ],
                    }
                ),
                ("uv.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("uv.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                (
                    "uv.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "uv.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("uv.select_pinned", {"type": 'P', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'IMAGE_MT_uvs_weldalign'),
                        ],
                    }
                ),
                ("uv.stitch", {"type": 'V', "value": 'PRESS'}, None),
                (
                    "uv.pin",
                    {"type": 'P', "value": 'PRESS'},
                    {
                        "properties": [
                            ("clear", False),
                        ],
                    }
                ),
                (
                    "uv.pin",
                    {"type": 'P', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("clear", True),
                        ],
                    }
                ),
                ("uv.unwrap", {"type": 'E', "value": 'PRESS'}, None),
                ("uv.minimize_stretch", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                ("uv.pack_islands", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                ("uv.average_islands_scale", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
                (
                    "uv.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "uv.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("uv.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                ("uv.cursor_set", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                (
                    "wm.call_menu",
                    {"type": 'S', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'IMAGE_MT_uvs_snap'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'TAB', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("name", 'IMAGE_MT_uvs_select_mode'),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit'),
                            ("value_1", 'DISABLED'),
                            ("value_2", 'ENABLED'),
                        ],
                    }
                ),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                ("transform.shear", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                ("transform.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.context_toggle",
                    {"type": 'TAB', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_snap'),
                        ],
                    }
                ),
                (
                    "wm.context_menu_enum",
                    {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.snap_uv_element'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Transform Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("TRANSLATE", {"type": 'G', "value": 'PRESS'}, None),
                ("ROTATE", {"type": 'R', "value": 'PRESS'}, None),
                ("RESIZE", {"type": 'S', "value": 'PRESS'}, None),
                ("SNAP_TOGGLE", {"type": 'TAB', "value": 'PRESS', "shift": True}, None),
                ("SNAP_INV_ON", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_INV_OFF", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("SNAP_INV_ON", {"type": 'RIGHT_CTRL', "value": 'PRESS', "any": True}, None),
                ("SNAP_INV_OFF", {"type": 'RIGHT_CTRL', "value": 'RELEASE', "any": True}, None),
                ("ADD_SNAP", {"type": 'A', "value": 'PRESS'}, None),
                ("REMOVE_SNAP", {"type": 'A', "value": 'PRESS', "alt": True}, None),
                ("PROPORTIONAL_SIZE_UP", {"type": 'PAGE_UP', "value": 'PRESS'}, None),
                ("PROPORTIONAL_SIZE_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS'}, None),
                ("PROPORTIONAL_SIZE_UP", {"type": 'PAGE_UP', "value": 'PRESS', "shift": True}, None),
                ("PROPORTIONAL_SIZE_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True}, None),
                ("PROPORTIONAL_SIZE_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'}, None),
                ("PROPORTIONAL_SIZE_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS'}, None),
                ("PROPORTIONAL_SIZE_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
                ("PROPORTIONAL_SIZE_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
                ("PROPORTIONAL_SIZE", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("EDGESLIDE_EDGE_NEXT", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "alt": True}, None),
                ("EDGESLIDE_PREV_NEXT", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "alt": True}, None),
                ("AUTOIK_CHAIN_LEN_UP", {"type": 'PAGE_UP', "value": 'PRESS', "shift": True}, None),
                ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True}, None),
                ("AUTOIK_CHAIN_LEN_UP", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True}, None),
                ("AUTOIK_CHAIN_LEN_DOWN", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True}, None),
                ("INSERTOFS_TOGGLE_DIR", {"type": 'T', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "UV Sculpt",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": 'Q', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_uv_sculpt'),
                        ],
                    }
                ),
                (
                    "sculpt.uv_sculpt_stroke",
                    {"type": 'LEFTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'NORMAL'),
                        ],
                    }
                ),
                (
                    "sculpt.uv_sculpt_stroke",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'INVERT'),
                        ],
                    }
                ),
                (
                    "sculpt.uv_sculpt_stroke",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'RELAX'),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 0.9),
                        ],
                    }
                ),
                (
                    "brush.scale_size",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("scalar", 1.1111112),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.uv_sculpt.brush.size'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.size'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),
                            ("rotation_path", 'tool_settings.uv_sculpt.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.uv_sculpt.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.uv_sculpt.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "wm.radial_control",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path_primary", 'tool_settings.uv_sculpt.brush.strength'),
                            ("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),
                            ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),
                            ("rotation_path", 'tool_settings.uv_sculpt.brush.texture_slot.angle'),
                            ("color_path", 'tool_settings.uv_sculpt.brush.cursor_color_add'),
                            ("fill_color_path", ''),
                            ("fill_color_override_path", ''),
                            ("fill_color_override_test_path", ''),
                            ("zoom_path", ''),
                            ("image_id", 'tool_settings.uv_sculpt.brush'),
                            ("secondary_tex", False),
                        ],
                    }
                ),
                (
                    "brush.uv_sculpt_tool_set",
                    {"type": 'S', "value": 'PRESS'},
                    {
                        "properties": [
                            ("tool", 'RELAX'),
                        ],
                    }
                ),
                (
                    "brush.uv_sculpt_tool_set",
                    {"type": 'P', "value": 'PRESS'},
                    {
                        "properties": [
                            ("tool", 'PINCH'),
                        ],
                    }
                ),
                (
                    "brush.uv_sculpt_tool_set",
                    {"type": 'G', "value": 'PRESS'},
                    {
                        "properties": [
                            ("tool", 'GRAB'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Paint Stroke Modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Mask Editing",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("mask.new", {"type": 'N', "value": 'PRESS', "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'MASK_MT_add'),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_enum",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.proportional_edit_falloff'),
                            ("wrap", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_proportional_edit_mask'),
                        ],
                    }
                ),
                ("mask.add_vertex_slide", {"type": 'ACTIONMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("mask.add_feather_vertex_slide", {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True}, None),
                ("mask.delete", {"type": 'X', "value": 'PRESS'}, None),
                ("mask.delete", {"type": 'DEL', "value": 'PRESS'}, None),
                (
                    "mask.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", False),
                        ],
                    }
                ),
                (
                    "mask.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("deselect", False),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "mask.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "mask.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("mask.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
                (
                    "mask.select_linked_pick",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "mask.select_linked_pick",
                    {"type": 'L', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("mask.select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("mask.select_circle", {"type": 'C', "value": 'PRESS'}, None),
                (
                    "mask.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "mask.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("mask.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("mask.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("mask.hide_view_clear", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                (
                    "mask.hide_view_set",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "mask.hide_view_set",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                (
                    "clip.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                ("mask.cyclic_toggle", {"type": 'C', "value": 'PRESS', "alt": True}, None),
                ("mask.slide_point", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                ("mask.slide_spline_curvature", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                ("mask.handle_type_set", {"type": 'V', "value": 'PRESS'}, None),
                ("mask.normals_make_consistent", {"type": 'N', "value": 'PRESS', "ctrl": True}, None),
                ("mask.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                ("mask.parent_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
                ("mask.shape_key_insert", {"type": 'I', "value": 'PRESS'}, None),
                ("mask.shape_key_clear", {"type": 'I', "value": 'PRESS', "alt": True}, None),
                ("mask.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("mask.copy_splines", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("mask.paste_splines", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                ("uv.cursor_set", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'MASK_SHRINKFATTEN'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Markers",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {
            "items": [
                ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
                ("marker.move", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("marker.duplicate", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("marker.select", {"type": 'SELECTMOUSE', "value": 'PRESS'}, None),
                (
                    "marker.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "marker.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("camera", True),
                        ],
                    }
                ),
                (
                    "marker.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("camera", True),
                        ],
                    }
                ),
                ("marker.select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("marker.select_all", {"type": 'A', "value": 'PRESS'}, None),
                ("marker.delete", {"type": 'X', "value": 'PRESS'}, None),
                ("marker.delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
                ("marker.move", {"type": 'G', "value": 'PRESS'}, None),
                ("marker.camera_bind", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Eyedropper Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("SAMPLE_CONFIRM", {"type": 'RET', "value": 'RELEASE', "any": True}, None),
                ("SAMPLE_CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'RELEASE', "any": True}, None),
                ("SAMPLE_CONFIRM", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
                ("SAMPLE_BEGIN", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
                ("SAMPLE_RESET", {"type": 'SPACE', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Eyedropper ColorBand PointSampling Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'BACK_SPACE', "value": 'PRESS', "any": True}, None),
                ("SAMPLE_CONFIRM", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("SAMPLE_CONFIRM", {"type": 'RET', "value": 'RELEASE', "any": True}, None),
                ("SAMPLE_CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'RELEASE', "any": True}, None),
                ("SAMPLE_SAMPLE", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
                ("SAMPLE_RESET", {"type": 'SPACE', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "Outliner Item Drag & Drop Modal Map",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'RELEASE', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'RELEASE', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Fly Modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
                ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'ANY', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'SPACE', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("ACCELERATE", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "any": True}, None),
                ("DECELERATE", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "any": True}, None),
                ("ACCELERATE", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "any": True}, None),
                ("DECELERATE", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("PAN_ENABLE", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "any": True}, None),
                ("PAN_DISABLE", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
                ("FORWARD", {"type": 'W', "value": 'PRESS'}, None),
                ("BACKWARD", {"type": 'S', "value": 'PRESS'}, None),
                ("LEFT", {"type": 'A', "value": 'PRESS'}, None),
                ("RIGHT", {"type": 'D', "value": 'PRESS'}, None),
                ("UP", {"type": 'E', "value": 'PRESS'}, None),
                ("DOWN", {"type": 'Q', "value": 'PRESS'}, None),
                ("UP", {"type": 'R', "value": 'PRESS'}, None),
                ("DOWN", {"type": 'F', "value": 'PRESS'}, None),
                ("FORWARD", {"type": 'UP_ARROW', "value": 'PRESS'}, None),
                ("BACKWARD", {"type": 'DOWN_ARROW', "value": 'PRESS'}, None),
                ("LEFT", {"type": 'LEFT_ARROW', "value": 'PRESS'}, None),
                ("RIGHT", {"type": 'RIGHT_ARROW', "value": 'PRESS'}, None),
                ("AXIS_LOCK_X", {"type": 'X', "value": 'PRESS'}, None),
                ("AXIS_LOCK_Z", {"type": 'Z', "value": 'PRESS'}, None),
                ("PRECISION_ENABLE", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_DISABLE", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
                ("PRECISION_ENABLE", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("PRECISION_DISABLE", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("FREELOOK_ENABLE", {"type": 'LEFT_CTRL', "value": 'PRESS', "any": True}, None),
                ("FREELOOK_DISABLE", {"type": 'LEFT_CTRL', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Walk Modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CANCEL", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("CANCEL", {"type": 'RIGHTMOUSE', "value": 'ANY', "any": True}, None),
                ("CONFIRM", {"type": 'LEFTMOUSE', "value": 'ANY', "any": True}, None),
                ("CONFIRM", {"type": 'RET', "value": 'PRESS', "any": True}, None),
                ("CONFIRM", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "any": True}, None),
                ("FAST_ENABLE", {"type": 'LEFT_SHIFT', "value": 'PRESS', "any": True}, None),
                ("FAST_DISABLE", {"type": 'LEFT_SHIFT', "value": 'RELEASE', "any": True}, None),
                ("SLOW_ENABLE", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True}, None),
                ("SLOW_DISABLE", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
                ("FORWARD", {"type": 'W', "value": 'PRESS', "any": True}, None),
                ("BACKWARD", {"type": 'S', "value": 'PRESS', "any": True}, None),
                ("LEFT", {"type": 'A', "value": 'PRESS', "any": True}, None),
                ("RIGHT", {"type": 'D', "value": 'PRESS', "any": True}, None),
                ("UP", {"type": 'E', "value": 'PRESS', "any": True}, None),
                ("DOWN", {"type": 'Q', "value": 'PRESS', "any": True}, None),
                ("FORWARD_STOP", {"type": 'W', "value": 'RELEASE', "any": True}, None),
                ("BACKWARD_STOP", {"type": 'S', "value": 'RELEASE', "any": True}, None),
                ("LEFT_STOP", {"type": 'A', "value": 'RELEASE', "any": True}, None),
                ("RIGHT_STOP", {"type": 'D', "value": 'RELEASE', "any": True}, None),
                ("UP_STOP", {"type": 'E', "value": 'RELEASE', "any": True}, None),
                ("DOWN_STOP", {"type": 'Q', "value": 'RELEASE', "any": True}, None),
                ("FORWARD", {"type": 'UP_ARROW', "value": 'PRESS'}, None),
                ("BACKWARD", {"type": 'DOWN_ARROW', "value": 'PRESS'}, None),
                ("LEFT", {"type": 'LEFT_ARROW', "value": 'PRESS'}, None),
                ("RIGHT", {"type": 'RIGHT_ARROW', "value": 'PRESS'}, None),
                ("FORWARD_STOP", {"type": 'UP_ARROW', "value": 'RELEASE', "any": True}, None),
                ("BACKWARD_STOP", {"type": 'DOWN_ARROW', "value": 'RELEASE', "any": True}, None),
                ("LEFT_STOP", {"type": 'LEFT_ARROW', "value": 'RELEASE', "any": True}, None),
                ("RIGHT_STOP", {"type": 'RIGHT_ARROW', "value": 'RELEASE', "any": True}, None),
                ("GRAVITY_TOGGLE", {"type": 'TAB', "value": 'PRESS'}, None),
                ("GRAVITY_TOGGLE", {"type": 'G', "value": 'PRESS'}, None),
                ("JUMP", {"type": 'V', "value": 'PRESS', "any": True}, None),
                ("JUMP_STOP", {"type": 'V', "value": 'RELEASE', "any": True}, None),
                ("TELEPORT", {"type": 'SPACE', "value": 'PRESS', "any": True}, None),
                ("TELEPORT", {"type": 'MIDDLEMOUSE', "value": 'ANY', "any": True}, None),
                ("ACCELERATE", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "any": True}, None),
                ("DECELERATE", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "any": True}, None),
                ("ACCELERATE", {"type": 'WHEELUPMOUSE', "value": 'PRESS', "any": True}, None),
                ("DECELERATE", {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Rotate Modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
                ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
                ("AXIS_SNAP_ENABLE", {"type": 'LEFT_ALT', "value": 'PRESS', "any": True}, None),
                ("AXIS_SNAP_DISABLE", {"type": 'LEFT_ALT', "value": 'RELEASE', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Move Modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
                ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Zoom Modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
                ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "View3D Dolly Modal",
        {"space_type": 'EMPTY', "region_type": 'WINDOW', "modal": True},
        {
            "items": [
                ("CONFIRM", {"type": 'MIDDLEMOUSE', "value": 'RELEASE', "any": True}, None),
                ("CONFIRM", {"type": 'ESC', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Graph Editor Generic",
        {"space_type": 'GRAPH_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("graph.properties", {"type": 'N', "value": 'PRESS'}, None),
                ("graph.extrapolation_type", {"type": 'E', "value": 'PRESS', "shift": True}, None),
                ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
                (
                    "graph.hide",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "graph.hide",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("graph.reveal", {"type": 'H', "value": 'PRESS', "alt": True}, None),
            ],
        },
    ),
    (
        "Graph Editor",
        {"space_type": 'GRAPH_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": 'H', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.show_handles'),
                        ],
                    }
                ),
                ("graph.cursor_set", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                (
                    "graph.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", False),
                            ("curves", False),
                        ],
                    }
                ),
                (
                    "graph.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", True),
                            ("curves", False),
                        ],
                    }
                ),
                (
                    "graph.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("curves", False),
                        ],
                    }
                ),
                (
                    "graph.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", True),
                            ("curves", False),
                        ],
                    }
                ),
                (
                    "graph.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", False),
                            ("curves", True),
                        ],
                    }
                ),
                (
                    "graph.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("curves", True),
                        ],
                    }
                ),
                (
                    "graph.select_leftright",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CHECK'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "graph.select_leftright",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CHECK'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "graph.select_leftright",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'LEFT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "graph.select_leftright",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'RIGHT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "graph.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "graph.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                (
                    "graph.select_border",
                    {"type": 'B', "value": 'PRESS'},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("include_handles", False),
                        ],
                    }
                ),
                (
                    "graph.select_border",
                    {"type": 'B', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                            ("include_handles", False),
                        ],
                    }
                ),
                (
                    "graph.select_border",
                    {"type": 'B', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("axis_range", False),
                            ("include_handles", True),
                        ],
                    }
                ),
                (
                    "graph.select_border",
                    {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                            ("include_handles", True),
                        ],
                    }
                ),
                (
                    "graph.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "graph.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("graph.select_circle", {"type": 'C', "value": 'PRESS'}, None),
                (
                    "graph.select_column",
                    {"type": 'K', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'KEYS'),
                        ],
                    }
                ),
                (
                    "graph.select_column",
                    {"type": 'K', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CFRA'),
                        ],
                    }
                ),
                (
                    "graph.select_column",
                    {"type": 'K', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'MARKERS_COLUMN'),
                        ],
                    }
                ),
                (
                    "graph.select_column",
                    {"type": 'K', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'MARKERS_BETWEEN'),
                        ],
                    }
                ),
                ("graph.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("graph.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("graph.select_linked", {"type": 'L', "value": 'PRESS'}, None),
                ("graph.frame_jump", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
                ("graph.snap", {"type": 'S', "value": 'PRESS', "shift": True}, None),
                ("graph.mirror", {"type": 'M', "value": 'PRESS', "shift": True}, None),
                ("graph.handle_type", {"type": 'V', "value": 'PRESS'}, None),
                ("graph.interpolation_type", {"type": 'T', "value": 'PRESS'}, None),
                ("graph.easing_type", {"type": 'E', "value": 'PRESS', "ctrl": True}, None),
                ("graph.smooth", {"type": 'O', "value": 'PRESS', "alt": True}, None),
                ("graph.sample", {"type": 'O', "value": 'PRESS', "shift": True}, None),
                ("graph.bake", {"type": 'C', "value": 'PRESS', "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'GRAPH_MT_delete'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'GRAPH_MT_delete'),
                        ],
                    }
                ),
                ("graph.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("graph.keyframe_insert", {"type": 'I', "value": 'PRESS'}, None),
                (
                    "graph.click_insert",
                    {"type": 'ACTIONMOUSE', "value": 'CLICK', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "graph.click_insert",
                    {"type": 'ACTIONMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                ("graph.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("graph.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                (
                    "graph.paste",
                    {"type": 'V', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    }
                ),
                ("graph.previewrange_set", {"type": 'P', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("graph.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                ("graph.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("graph.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                ("graph.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
                (
                    "graph.fmodifier_add",
                    {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("only_active", False),
                        ],
                    }
                ),
                ("anim.channels_editable_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                (
                    "transform.transform",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TIME_EXTEND'),
                        ],
                    }
                ),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                (
                    "wm.context_toggle",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_proportional_fcurve'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'COMMA', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'BOUNDING_BOX_CENTER'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'CURSOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'INDIVIDUAL_ORIGINS'),
                        ],
                    }
                ),
                ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
                ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Image Generic",
        {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("image.new", {"type": 'N', "value": 'PRESS', "alt": True}, None),
                ("image.open", {"type": 'O', "value": 'PRESS', "alt": True}, None),
                ("image.reload", {"type": 'R', "value": 'PRESS', "alt": True}, None),
                ("image.read_viewlayers", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
                ("image.save", {"type": 'S', "value": 'PRESS', "alt": True}, None),
                ("image.save_as", {"type": 'F3', "value": 'PRESS'}, None),
                ("image.properties", {"type": 'N', "value": 'PRESS'}, None),
                ("image.toolshelf", {"type": 'T', "value": 'PRESS'}, None),
                ("image.cycle_render_slot", {"type": 'J', "value": 'PRESS'}, None),
                (
                    "image.cycle_render_slot",
                    {"type": 'J', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("reverse", True),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Image",
        {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("image.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                (
                    "image.view_all",
                    {"type": 'HOME', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("fit_view", True),
                        ],
                    }
                ),
                ("image.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                ("image.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("image.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
                ("image.view_pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("image.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("image.view_ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
                ("image.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
                ("image.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
                ("image.view_zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS'}, None),
                ("image.view_zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS'}, None),
                ("image.view_zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("image.view_zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
                ("image.view_zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
                ("image.view_zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_8', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_2', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_1', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_2', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 0.5),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_4', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 0.25),
                        ],
                    }
                ),
                (
                    "image.view_zoom_ratio",
                    {"type": 'NUMPAD_8', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 0.125),
                        ],
                    }
                ),
                ("image.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("image.sample", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                (
                    "image.curves_point_set",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("point", 'BLACK_POINT'),
                        ],
                    }
                ),
                (
                    "image.curves_point_set",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("point", 'WHITE_POINT'),
                        ],
                    }
                ),
                (
                    "object.mode_set",
                    {"type": 'TAB', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'EDIT'),
                            ("toggle", True),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'ONE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 0),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'TWO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 1),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'THREE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 2),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'FOUR', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 3),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'FIVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 4),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'SIX', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 5),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'SEVEN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 6),
                        ],
                    }
                ),
                (
                    "wm.context_set_int",
                    {"type": 'EIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.image.render_slots.active_index'),
                            ("value", 7),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'COMMA', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'CENTER'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'COMMA', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'MEDIAN'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'CURSOR'),
                        ],
                    }
                ),
                ("image.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
                ("image.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
            ],
        },
    ),
    (
        "Node Generic",
        {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("node.properties", {"type": 'N', "value": 'PRESS'}, None),
                ("node.toolbar", {"type": 'T', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Node Editor",
        {"space_type": 'NODE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'ACTIONMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select_border",
                    {"type": 'EVT_TWEAK_S', "value": 'ANY'},
                    {
                        "properties": [
                            ("tweak", True),
                        ],
                    }
                ),
                (
                    "node.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "node.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("node.select_circle", {"type": 'C', "value": 'PRESS'}, None),
                (
                    "node.link",
                    {"type": 'LEFTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("detach", False),
                        ],
                    }
                ),
                (
                    "node.link",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("detach", True),
                        ],
                    }
                ),
                ("node.resize", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("node.add_reroute", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True}, None),
                ("node.links_cut", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("node.select_link_viewer", {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("node.backimage_move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None),
                (
                    "node.backimage_zoom",
                    {"type": 'V', "value": 'PRESS'},
                    {
                        "properties": [
                            ("factor", 0.8333333),
                        ],
                    }
                ),
                (
                    "node.backimage_zoom",
                    {"type": 'V', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("factor", 1.2),
                        ],
                    }
                ),
                ("node.backimage_fit", {"type": 'HOME', "value": 'PRESS', "alt": True}, None),
                ("node.backimage_sample", {"type": 'ACTIONMOUSE', "value": 'PRESS', "alt": True}, None),
                (
                    "node.link_make",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("replace", False),
                        ],
                    }
                ),
                (
                    "node.link_make",
                    {"type": 'F', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("replace", True),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'NODE_MT_add'),
                        ],
                    }
                ),
                ("node.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("node.duplicate_move_keep_inputs", {"type": 'D', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("node.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
                ("node.detach", {"type": 'P', "value": 'PRESS', "alt": True}, None),
                ("node.join", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
                ("node.hide_toggle", {"type": 'H', "value": 'PRESS'}, None),
                ("node.mute_toggle", {"type": 'M', "value": 'PRESS'}, None),
                ("node.preview_toggle", {"type": 'H', "value": 'PRESS', "shift": True}, None),
                ("node.hide_socket_toggle", {"type": 'H', "value": 'PRESS', "ctrl": True}, None),
                ("node.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                ("node.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("node.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                (
                    "node.select_border",
                    {"type": 'B', "value": 'PRESS'},
                    {
                        "properties": [
                            ("tweak", False),
                        ],
                    }
                ),
                ("node.delete", {"type": 'X', "value": 'PRESS'}, None),
                ("node.delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("node.delete_reconnect", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
                (
                    "node.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "node.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("node.select_linked_to", {"type": 'L', "value": 'PRESS', "shift": True}, None),
                ("node.select_linked_from", {"type": 'L', "value": 'PRESS'}, None),
                (
                    "node.select_grouped",
                    {"type": 'G', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "node.select_grouped",
                    {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "node.select_same_type_step",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("prev", False),
                        ],
                    }
                ),
                (
                    "node.select_same_type_step",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("prev", True),
                        ],
                    }
                ),
                ("node.find_node", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
                ("node.group_make", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
                ("node.group_ungroup", {"type": 'G', "value": 'PRESS', "alt": True}, None),
                ("node.group_separate", {"type": 'P', "value": 'PRESS'}, None),
                (
                    "node.group_edit",
                    {"type": 'TAB', "value": 'PRESS'},
                    {
                        "properties": [
                            ("exit", False),
                        ],
                    }
                ),
                (
                    "node.group_edit",
                    {"type": 'TAB', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("exit", True),
                        ],
                    }
                ),
                ("node.read_viewlayers", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
                ("node.render_changed", {"type": 'Z', "value": 'PRESS'}, None),
                ("node.clipboard_copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("node.clipboard_paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                ("node.viewer_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
                ("node.clear_viewer_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("node.translate_attach", {"type": 'G', "value": 'PRESS'}, None),
                ("node.translate_attach", {"type": 'EVT_TWEAK_A', "value": 'ANY'}, None),
                ("node.translate_attach", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                (
                    "transform.translate",
                    {"type": 'G', "value": 'PRESS'},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    }
                ),
                (
                    "transform.translate",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY'},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    }
                ),
                (
                    "transform.translate",
                    {"type": 'EVT_TWEAK_S', "value": 'ANY'},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    }
                ),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                ("node.move_detach_links", {"type": 'D', "value": 'PRESS', "alt": True}, None),
                ("node.move_detach_links_release", {"type": 'EVT_TWEAK_A', "value": 'ANY', "alt": True}, None),
                ("node.move_detach_links", {"type": 'EVT_TWEAK_S', "value": 'ANY', "alt": True}, None),
                (
                    "wm.context_toggle",
                    {"type": 'TAB', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_snap'),
                        ],
                    }
                ),
                (
                    "wm.context_menu_enum",
                    {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.snap_node_element'),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "File Browser",
        {"space_type": 'FILE_BROWSER', "region_type": 'WINDOW'},
        {
            "items": [
                ("file.parent", {"type": 'UP_ARROW', "value": 'PRESS', "alt": True}, None),
                ("file.previous", {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True}, None),
                ("file.next", {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True}, None),
                ("file.refresh", {"type": 'R', "value": 'PRESS'}, None),
                ("file.parent", {"type": 'P', "value": 'PRESS'}, None),
                ("file.previous", {"type": 'BACK_SPACE', "value": 'PRESS'}, None),
                ("file.next", {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.context_toggle",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.params.show_hidden'),
                        ],
                    }
                ),
                ("file.directory_new", {"type": 'I', "value": 'PRESS'}, None),
                ("file.delete", {"type": 'X', "value": 'PRESS'}, None),
                ("file.delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("file.smoothscroll", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
                ("file.bookmark_toggle", {"type": 'T', "value": 'PRESS'}, None),
                ("file.bookmark_add", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "File Browser Main",
        {"space_type": 'FILE_BROWSER', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "file.execute",
                    {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'},
                    {
                        "properties": [
                            ("need_active", True),
                        ],
                    }
                ),
                ("file.refresh", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                ("file.select", {"type": 'LEFTMOUSE', "value": 'CLICK'}, None),
                (
                    "file.select",
                    {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "file.select",
                    {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("fill", True),
                        ],
                    }
                ),
                (
                    "file.select",
                    {"type": 'RIGHTMOUSE', "value": 'CLICK'},
                    {
                        "properties": [
                            ("open", False),
                        ],
                    }
                ),
                (
                    "file.select",
                    {"type": 'RIGHTMOUSE', "value": 'CLICK', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("open", False),
                        ],
                    }
                ),
                (
                    "file.select",
                    {"type": 'RIGHTMOUSE', "value": 'CLICK', "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("fill", True),
                            ("open", False),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'UP_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'UP'),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'UP_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'UP'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'UP'),
                            ("extend", True),
                            ("fill", True),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'DOWN_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'DOWN'),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'DOWN'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'DOWN'),
                            ("extend", True),
                            ("fill", True),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'LEFT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'LEFT'),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'LEFT'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'LEFT'),
                            ("extend", True),
                            ("fill", True),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("direction", 'RIGHT'),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("direction", 'RIGHT'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "file.select_walk",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'RIGHT'),
                            ("extend", True),
                            ("fill", True),
                        ],
                    }
                ),
                ("file.previous", {"type": 'BUTTON4MOUSE', "value": 'CLICK'}, None),
                ("file.next", {"type": 'BUTTON5MOUSE', "value": 'CLICK'}, None),
                ("file.select_all_toggle", {"type": 'A', "value": 'PRESS'}, None),
                ("file.select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("file.select_border", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
                ("file.rename", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("file.highlight", {"type": 'MOUSEMOVE', "value": 'ANY', "any": True}, None),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("increment", 1),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("increment", 10),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("increment", 100),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("increment", -1),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("increment", -10),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("increment", -100),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "File Browser Buttons",
        {"space_type": 'FILE_BROWSER', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "file.filenum",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("increment", 1),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("increment", 10),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("increment", 100),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS'},
                    {
                        "properties": [
                            ("increment", -1),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("increment", -10),
                        ],
                    }
                ),
                (
                    "file.filenum",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("increment", -100),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "Dopesheet Generic",
        {"space_type": 'DOPESHEET_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("action.properties", {"type": 'N', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Dopesheet",
        {"space_type": 'DOPESHEET_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "action.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", False),
                            ("channel", False),
                        ],
                    }
                ),
                (
                    "action.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", True),
                            ("channel", False),
                        ],
                    }
                ),
                (
                    "action.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("channel", False),
                        ],
                    }
                ),
                (
                    "action.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", True),
                            ("channel", False),
                        ],
                    }
                ),
                (
                    "action.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("column", False),
                            ("channel", True),
                        ],
                    }
                ),
                (
                    "action.clickselect",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", False),
                            ("channel", True),
                        ],
                    }
                ),
                (
                    "action.select_leftright",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CHECK'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "action.select_leftright",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CHECK'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "action.select_leftright",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'LEFT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "action.select_leftright",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'RIGHT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "action.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "action.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                (
                    "action.select_border",
                    {"type": 'B', "value": 'PRESS'},
                    {
                        "properties": [
                            ("axis_range", False),
                        ],
                    }
                ),
                (
                    "action.select_border",
                    {"type": 'B', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                        ],
                    }
                ),
                (
                    "action.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "action.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("action.select_circle", {"type": 'C', "value": 'PRESS'}, None),
                (
                    "action.select_column",
                    {"type": 'K', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'KEYS'),
                        ],
                    }
                ),
                (
                    "action.select_column",
                    {"type": 'K', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CFRA'),
                        ],
                    }
                ),
                (
                    "action.select_column",
                    {"type": 'K', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'MARKERS_COLUMN'),
                        ],
                    }
                ),
                (
                    "action.select_column",
                    {"type": 'K', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("mode", 'MARKERS_BETWEEN'),
                        ],
                    }
                ),
                ("action.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("action.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                ("action.select_linked", {"type": 'L', "value": 'PRESS'}, None),
                ("action.frame_jump", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
                ("action.snap", {"type": 'S', "value": 'PRESS', "shift": True}, None),
                ("action.mirror", {"type": 'M', "value": 'PRESS', "shift": True}, None),
                ("action.handle_type", {"type": 'V', "value": 'PRESS'}, None),
                ("action.interpolation_type", {"type": 'T', "value": 'PRESS'}, None),
                ("action.extrapolation_type", {"type": 'E', "value": 'PRESS', "shift": True}, None),
                ("action.keyframe_type", {"type": 'R', "value": 'PRESS'}, None),
                ("action.sample", {"type": 'O', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'X', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'DOPESHEET_MT_delete'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'DOPESHEET_MT_delete'),
                        ],
                    }
                ),
                ("action.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("action.keyframe_insert", {"type": 'I', "value": 'PRESS'}, None),
                ("action.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("action.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                (
                    "action.paste",
                    {"type": 'V', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    }
                ),
                ("action.previewrange_set", {"type": 'P', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("action.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                ("action.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("action.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                ("action.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
                ("anim.channels_editable_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
                ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
                (
                    "transform.transform",
                    {"type": 'G', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TIME_TRANSLATE'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'EVT_TWEAK_S', "value": 'ANY'},
                    {
                        "properties": [
                            ("mode", 'TIME_TRANSLATE'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TIME_EXTEND'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TIME_SCALE'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'T', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("mode", 'TIME_SLIDE'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'tool_settings.use_proportional_action'),
                        ],
                    }
                ),
                ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
                ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "NLA Generic",
        {"space_type": 'NLA_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("nla.properties", {"type": 'N', "value": 'PRESS'}, None),
                ("nla.tweakmode_enter", {"type": 'TAB', "value": 'PRESS'}, None),
                ("nla.tweakmode_exit", {"type": 'TAB', "value": 'PRESS'}, None),
                (
                    "nla.tweakmode_enter",
                    {"type": 'TAB', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("isolate_action", True),
                        ],
                    }
                ),
                (
                    "nla.tweakmode_exit",
                    {"type": 'TAB', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("isolate_action", True),
                        ],
                    }
                ),
                ("anim.channels_find", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "NLA Channels",
        {"space_type": 'NLA_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "nla.channels_click",
                    {"type": 'LEFTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "nla.channels_click",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "nla.tracks_add",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("above_selected", False),
                        ],
                    }
                ),
                (
                    "nla.tracks_add",
                    {"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("above_selected", True),
                        ],
                    }
                ),
                ("nla.tracks_delete", {"type": 'X', "value": 'PRESS'}, None),
                ("nla.tracks_delete", {"type": 'DEL', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "NLA Editor",
        {"space_type": 'NLA_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "nla.click_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "nla.click_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "nla.select_leftright",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CHECK'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "nla.select_leftright",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("mode", 'CHECK'),
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "nla.select_leftright",
                    {"type": 'LEFT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'LEFT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "nla.select_leftright",
                    {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'RIGHT'),
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "nla.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "nla.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                (
                    "nla.select_border",
                    {"type": 'B', "value": 'PRESS'},
                    {
                        "properties": [
                            ("axis_range", False),
                        ],
                    }
                ),
                (
                    "nla.select_border",
                    {"type": 'B', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                        ],
                    }
                ),
                ("nla.previewrange_set", {"type": 'P', "value": 'PRESS', "ctrl": True, "alt": True}, None),
                ("nla.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                ("nla.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("nla.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                ("nla.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
                ("nla.actionclip_add", {"type": 'A', "value": 'PRESS', "shift": True}, None),
                ("nla.transition_add", {"type": 'T', "value": 'PRESS', "shift": True}, None),
                ("nla.soundclip_add", {"type": 'K', "value": 'PRESS', "shift": True}, None),
                ("nla.meta_add", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                ("nla.meta_remove", {"type": 'G', "value": 'PRESS', "alt": True}, None),
                (
                    "nla.duplicate",
                    {"type": 'D', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("linked", False),
                        ],
                    }
                ),
                (
                    "nla.duplicate",
                    {"type": 'D', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("linked", True),
                        ],
                    }
                ),
                ("nla.make_single_user", {"type": 'U', "value": 'PRESS'}, None),
                ("nla.delete", {"type": 'X', "value": 'PRESS'}, None),
                ("nla.delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("nla.split", {"type": 'Y', "value": 'PRESS'}, None),
                ("nla.mute_toggle", {"type": 'H', "value": 'PRESS'}, None),
                ("nla.swap", {"type": 'F', "value": 'PRESS', "alt": True}, None),
                ("nla.move_up", {"type": 'PAGE_UP', "value": 'PRESS'}, None),
                ("nla.move_down", {"type": 'PAGE_DOWN', "value": 'PRESS'}, None),
                ("nla.apply_scale", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
                ("nla.clear_scale", {"type": 'S', "value": 'PRESS', "alt": True}, None),
                ("nla.snap", {"type": 'S', "value": 'PRESS', "shift": True}, None),
                ("nla.fmodifier_add", {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "transform.transform",
                    {"type": 'G', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'EVT_TWEAK_S', "value": 'ANY'},
                    {
                        "properties": [
                            ("mode", 'TRANSLATION'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TIME_EXTEND'),
                        ],
                    }
                ),
                (
                    "transform.transform",
                    {"type": 'S', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TIME_SCALE'),
                        ],
                    }
                ),
                ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
                ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Text Generic",
        {"space_type": 'TEXT_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("text.start_find", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
                ("text.jump", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
                ("text.find", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
                ("text.replace", {"type": 'H', "value": 'PRESS', "ctrl": True}, None),
                ("text.properties", {"type": 'T', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Text",
        {"space_type": 'TEXT_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "wm.context_cycle_int",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", False),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_int",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", True),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_int",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", False),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_int",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", True),
                        ],
                    }
                ),
                ("text.new", {"type": 'N', "value": 'PRESS', "ctrl": True}, None),
                ("text.open", {"type": 'O', "value": 'PRESS', "alt": True}, None),
                ("text.reload", {"type": 'R', "value": 'PRESS', "alt": True}, None),
                ("text.save", {"type": 'S', "value": 'PRESS', "alt": True}, None),
                ("text.save_as", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
                ("text.run_script", {"type": 'P', "value": 'PRESS', "alt": True}, None),
                ("text.cut", {"type": 'X', "value": 'PRESS', "ctrl": True}, None),
                ("text.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("text.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                ("text.cut", {"type": 'DEL', "value": 'PRESS', "shift": True}, None),
                ("text.copy", {"type": 'INSERT', "value": 'PRESS', "ctrl": True}, None),
                ("text.paste", {"type": 'INSERT', "value": 'PRESS', "shift": True}, None),
                ("text.duplicate_line", {"type": 'D', "value": 'PRESS', "ctrl": True}, None),
                ("text.select_all", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
                ("text.select_line", {"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("text.select_word", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
                (
                    "text.move_lines",
                    {"type": 'UP_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'UP'),
                        ],
                    }
                ),
                (
                    "text.move_lines",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("direction", 'DOWN'),
                        ],
                    }
                ),
                ("text.indent", {"type": 'TAB', "value": 'PRESS'}, None),
                ("text.unindent", {"type": 'TAB', "value": 'PRESS', "shift": True}, None),
                ("text.uncomment", {"type": 'D', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                (
                    "text.move",
                    {"type": 'HOME', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LINE_BEGIN'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'END', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LINE_END'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'E', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'LINE_END'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'E', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'LINE_END'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'LEFT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_CHARACTER'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'UP_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_LINE'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'DOWN_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_LINE'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'PAGE_UP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_PAGE'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'PAGE_DOWN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_PAGE'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'HOME', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'FILE_TOP'),
                        ],
                    }
                ),
                (
                    "text.move",
                    {"type": 'END', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'FILE_BOTTOM'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'HOME', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'LINE_BEGIN'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'END', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'LINE_END'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'NEXT_CHARACTER'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'UP_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_LINE'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'DOWN_ARROW', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'NEXT_LINE'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'PAGE_UP', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_PAGE'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'PAGE_DOWN', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'NEXT_PAGE'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'HOME', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'FILE_TOP'),
                        ],
                    }
                ),
                (
                    "text.move_select",
                    {"type": 'END', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", 'FILE_BOTTOM'),
                        ],
                    }
                ),
                (
                    "text.delete",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_CHARACTER'),
                        ],
                    }
                ),
                (
                    "text.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "text.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "text.delete",
                    {"type": 'DEL', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "text.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                ("text.overwrite_toggle", {"type": 'INSERT', "value": 'PRESS'}, None),
                ("text.scroll_bar", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("text.scroll_bar", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("text.scroll", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("text.scroll", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("text.selection_set", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
                ("text.cursor_set", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                (
                    "text.selection_set",
                    {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("select", True),
                        ],
                    }
                ),
                (
                    "text.scroll",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("lines", -1),
                        ],
                    }
                ),
                (
                    "text.scroll",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("lines", 1),
                        ],
                    }
                ),
                ("text.line_break", {"type": 'RET', "value": 'PRESS'}, None),
                ("text.line_break", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
                (
                    "wm.call_menu",
                    {"type": 'RIGHTMOUSE', "value": 'PRESS', "any": True},
                    {
                        "properties": [
                            ("name", 'TEXT_MT_toolbox'),
                        ],
                    }
                ),
                ("text.autocomplete", {"type": 'SPACE', "value": 'PRESS', "ctrl": True}, None),
                ("text.line_number", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),
                ("text.insert", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),
            ],
        },
    ),
    (
        "SequencerCommon",
        {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("sequencer.properties", {"type": 'N', "value": 'PRESS'}, None),
                (
                    "wm.context_toggle",
                    {"type": 'O', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("data_path", 'scene.sequence_editor.show_overlay'),
                        ],
                    }
                ),
                ("sequencer.view_toggle", {"type": 'TAB', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Sequencer",
        {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "sequencer.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "sequencer.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                (
                    "sequencer.cut",
                    {"type": 'K', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'SOFT'),
                        ],
                    }
                ),
                (
                    "sequencer.cut",
                    {"type": 'K', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'HARD'),
                        ],
                    }
                ),
                (
                    "sequencer.mute",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "sequencer.mute",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                (
                    "sequencer.unmute",
                    {"type": 'H', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "sequencer.unmute",
                    {"type": 'H', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("sequencer.lock", {"type": 'L', "value": 'PRESS', "shift": True}, None),
                ("sequencer.unlock", {"type": 'L', "value": 'PRESS', "shift": True, "alt": True}, None),
                ("sequencer.reassign_inputs", {"type": 'R', "value": 'PRESS'}, None),
                ("sequencer.reload", {"type": 'R', "value": 'PRESS', "alt": True}, None),
                (
                    "sequencer.reload",
                    {"type": 'R', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("adjust_length", True),
                        ],
                    }
                ),
                ("sequencer.offset_clear", {"type": 'O', "value": 'PRESS', "alt": True}, None),
                ("sequencer.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
                ("sequencer.delete", {"type": 'X', "value": 'PRESS'}, None),
                ("sequencer.delete", {"type": 'DEL', "value": 'PRESS'}, None),
                ("sequencer.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("sequencer.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                ("sequencer.images_separate", {"type": 'Y', "value": 'PRESS'}, None),
                ("sequencer.meta_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
                ("sequencer.meta_make", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
                ("sequencer.meta_separate", {"type": 'G', "value": 'PRESS', "alt": True}, None),
                ("sequencer.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                ("sequencer.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("sequencer.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                ("sequencer.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
                (
                    "sequencer.strip_jump",
                    {"type": 'PAGE_UP', "value": 'PRESS'},
                    {
                        "properties": [
                            ("next", True),
                            ("center", False),
                        ],
                    }
                ),
                (
                    "sequencer.strip_jump",
                    {"type": 'PAGE_DOWN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("next", False),
                            ("center", False),
                        ],
                    }
                ),
                (
                    "sequencer.strip_jump",
                    {"type": 'PAGE_UP', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("next", True),
                            ("center", True),
                        ],
                    }
                ),
                (
                    "sequencer.strip_jump",
                    {"type": 'PAGE_DOWN', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("next", False),
                            ("center", True),
                        ],
                    }
                ),
                (
                    "sequencer.swap",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("side", 'LEFT'),
                        ],
                    }
                ),
                (
                    "sequencer.swap",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("side", 'RIGHT'),
                        ],
                    }
                ),
                (
                    "sequencer.gap_remove",
                    {"type": 'BACK_SPACE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    }
                ),
                (
                    "sequencer.gap_remove",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("all", True),
                        ],
                    }
                ),
                ("sequencer.gap_insert", {"type": 'EQUAL', "value": 'PRESS', "shift": True}, None),
                ("sequencer.snap", {"type": 'S', "value": 'PRESS', "shift": True}, None),
                ("sequencer.swap_inputs", {"type": 'S', "value": 'PRESS', "alt": True}, None),
                (
                    "sequencer.cut_multicam",
                    {"type": 'ONE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 1),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'TWO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 2),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'THREE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 3),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'FOUR', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 4),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'FIVE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 5),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'SIX', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 6),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'SEVEN', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 7),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'EIGHT', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 8),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'NINE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 9),
                        ],
                    }
                ),
                (
                    "sequencer.cut_multicam",
                    {"type": 'ZERO', "value": 'PRESS'},
                    {
                        "properties": [
                            ("camera", 10),
                        ],
                    }
                ),
                (
                    "sequencer.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                            ("linked_handle", False),
                            ("left_right", 'NONE'),
                            ("linked_time", False),
                        ],
                    }
                ),
                (
                    "sequencer.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_handle", False),
                            ("left_right", 'NONE'),
                            ("linked_time", False),
                        ],
                    }
                ),
                (
                    "sequencer.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("linked_handle", True),
                            ("left_right", 'NONE'),
                            ("linked_time", False),
                        ],
                    }
                ),
                (
                    "sequencer.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_handle", True),
                            ("left_right", 'NONE'),
                            ("linked_time", False),
                        ],
                    }
                ),
                (
                    "sequencer.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("extend", False),
                            ("linked_handle", False),
                            ("left_right", 'MOUSE'),
                            ("linked_time", True),
                        ],
                    }
                ),
                (
                    "sequencer.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_handle", False),
                            ("left_right", 'NONE'),
                            ("linked_time", True),
                        ],
                    }
                ),
                ("sequencer.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
                ("sequencer.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
                (
                    "sequencer.select_linked_pick",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "sequencer.select_linked_pick",
                    {"type": 'L', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                ("sequencer.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
                ("sequencer.select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("sequencer.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'A', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'SEQUENCER_MT_add'),
                        ],
                    }
                ),
                (
                    "wm.call_menu",
                    {"type": 'C', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'SEQUENCER_MT_change'),
                        ],
                    }
                ),
                ("sequencer.slip", {"type": 'S', "value": 'PRESS'}, None),
                (
                    "wm.context_set_int",
                    {"type": 'O', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'scene.sequence_editor.overlay_frame'),
                            ("value", 0),
                        ],
                    }
                ),
                ("transform.seq_slide", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.seq_slide", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                (
                    "transform.transform",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("mode", 'TIME_EXTEND'),
                        ],
                    }
                ),
                ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
                ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "SequencerPreview",
        {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("sequencer.view_all_preview", {"type": 'HOME', "value": 'PRESS'}, None),
                ("sequencer.view_all_preview", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("sequencer.view_ghost_border", {"type": 'O', "value": 'PRESS'}, None),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": 'NUMPAD_1', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                    }
                ),
                ("sequencer.sample", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Console",
        {"space_type": 'CONSOLE', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "console.move",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                (
                    "console.move",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "console.move",
                    {"type": 'HOME', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LINE_BEGIN'),
                        ],
                    }
                ),
                (
                    "console.move",
                    {"type": 'END', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'LINE_END'),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_int",
                    {"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", False),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_int",
                    {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", True),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_int",
                    {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", False),
                        ],
                    }
                ),
                (
                    "wm.context_cycle_int",
                    {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.font_size'),
                            ("reverse", True),
                        ],
                    }
                ),
                (
                    "console.move",
                    {"type": 'LEFT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "console.move",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_CHARACTER'),
                        ],
                    }
                ),
                (
                    "console.history_cycle",
                    {"type": 'UP_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("reverse", True),
                        ],
                    }
                ),
                (
                    "console.history_cycle",
                    {"type": 'DOWN_ARROW', "value": 'PRESS'},
                    {
                        "properties": [
                            ("reverse", False),
                        ],
                    }
                ),
                (
                    "console.delete",
                    {"type": 'DEL', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'NEXT_CHARACTER'),
                        ],
                    }
                ),
                (
                    "console.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "console.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_CHARACTER'),
                        ],
                    }
                ),
                (
                    "console.delete",
                    {"type": 'DEL', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'NEXT_WORD'),
                        ],
                    }
                ),
                (
                    "console.delete",
                    {"type": 'BACK_SPACE', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("type", 'PREVIOUS_WORD'),
                        ],
                    }
                ),
                ("console.clear_line", {"type": 'RET', "value": 'PRESS', "shift": True}, None),
                ("console.clear_line", {"type": 'NUMPAD_ENTER', "value": 'PRESS', "shift": True}, None),
                (
                    "console.execute",
                    {"type": 'RET', "value": 'PRESS'},
                    {
                        "properties": [
                            ("interactive", True),
                        ],
                    }
                ),
                (
                    "console.execute",
                    {"type": 'NUMPAD_ENTER', "value": 'PRESS'},
                    {
                        "properties": [
                            ("interactive", True),
                        ],
                    }
                ),
                ("console.autocomplete", {"type": 'SPACE', "value": 'PRESS', "ctrl": True}, None),
                ("console.copy_as_script", {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("console.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("console.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
                ("console.select_set", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                ("console.select_word", {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK'}, None),
                (
                    "console.insert",
                    {"type": 'TAB', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("text", '\t'),
                        ],
                    }
                ),
                ("console.indent", {"type": 'TAB', "value": 'PRESS'}, None),
                ("console.unindent", {"type": 'TAB', "value": 'PRESS', "shift": True}, None),
                ("console.insert", {"type": 'TEXTINPUT', "value": 'ANY', "any": True}, None),
            ],
        },
    ),
    (
        "Clip",
        {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("clip.open", {"type": 'O', "value": 'PRESS', "alt": True}, None),
                ("clip.tools", {"type": 'T', "value": 'PRESS'}, None),
                ("clip.properties", {"type": 'N', "value": 'PRESS'}, None),
                (
                    "clip.track_markers",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("backwards", True),
                            ("sequence", False),
                        ],
                    }
                ),
                (
                    "clip.track_markers",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("backwards", False),
                            ("sequence", False),
                        ],
                    }
                ),
                (
                    "clip.track_markers",
                    {"type": 'T', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("backwards", False),
                            ("sequence", True),
                        ],
                    }
                ),
                (
                    "clip.track_markers",
                    {"type": 'T', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("backwards", True),
                            ("sequence", True),
                        ],
                    }
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": 'TAB', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.mode'),
                            ("value_1", 'TRACKING'),
                            ("value_2", 'MASK'),
                        ],
                    }
                ),
                ("clip.solve_camera", {"type": 'S', "value": 'PRESS', "shift": True}, None),
                (
                    "clip.set_solver_keyframe",
                    {"type": 'Q', "value": 'PRESS'},
                    {
                        "properties": [
                            ("keyframe", 'KEYFRAME_A'),
                        ],
                    }
                ),
                (
                    "clip.set_solver_keyframe",
                    {"type": 'E', "value": 'PRESS'},
                    {
                        "properties": [
                            ("keyframe", 'KEYFRAME_B'),
                        ],
                    }
                ),
                ("clip.prefetch", {"type": 'P', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Clip Editor",
        {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("clip.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
                ("clip.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
                ("clip.view_pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
                ("clip.view_zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("clip.view_zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
                ("clip.view_zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
                ("clip.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
                ("clip.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
                ("clip.view_zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS'}, None),
                ("clip.view_zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS'}, None),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_8', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_2', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_1', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_2', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 0.5),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_4', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 0.25),
                        ],
                    }
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": 'NUMPAD_8', "value": 'PRESS'},
                    {
                        "properties": [
                            ("ratio", 0.125),
                        ],
                    }
                ),
                ("clip.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                (
                    "clip.view_all",
                    {"type": 'F', "value": 'PRESS'},
                    {
                        "properties": [
                            ("fit_view", True),
                        ],
                    }
                ),
                ("clip.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                ("clip.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("clip.view_ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
                (
                    "clip.frame_jump",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("position", 'PATHSTART'),
                        ],
                    }
                ),
                (
                    "clip.frame_jump",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("position", 'PATHEND'),
                        ],
                    }
                ),
                (
                    "clip.frame_jump",
                    {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("position", 'FAILEDPREV'),
                        ],
                    }
                ),
                (
                    "clip.frame_jump",
                    {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("position", 'PATHSTART'),
                        ],
                    }
                ),
                ("clip.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                (
                    "clip.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "clip.select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "clip.select_all",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "clip.select_all",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("clip.select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("clip.select_circle", {"type": 'C', "value": 'PRESS'}, None),
                (
                    "wm.call_menu",
                    {"type": 'G', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("name", 'CLIP_MT_select_grouped'),
                        ],
                    }
                ),
                (
                    "clip.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    }
                ),
                (
                    "clip.select_lasso",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY', "shift": True, "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    }
                ),
                ("clip.add_marker_slide", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True}, None),
                ("clip.delete_marker", {"type": 'DEL', "value": 'PRESS', "shift": True}, None),
                ("clip.delete_marker", {"type": 'X', "value": 'PRESS', "shift": True}, None),
                ("clip.slide_marker", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
                (
                    "clip.disable_markers",
                    {"type": 'D', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                ("clip.delete_track", {"type": 'DEL', "value": 'PRESS'}, None),
                ("clip.delete_track", {"type": 'X', "value": 'PRESS'}, None),
                (
                    "clip.lock_tracks",
                    {"type": 'L', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'LOCK'),
                        ],
                    }
                ),
                (
                    "clip.lock_tracks",
                    {"type": 'L', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("action", 'UNLOCK'),
                        ],
                    }
                ),
                (
                    "clip.hide_tracks",
                    {"type": 'H', "value": 'PRESS'},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    }
                ),
                (
                    "clip.hide_tracks",
                    {"type": 'H', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    }
                ),
                ("clip.hide_tracks_clear", {"type": 'H', "value": 'PRESS', "alt": True}, None),
                ("clip.slide_plane_marker", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                ("clip.keyframe_insert", {"type": 'I', "value": 'PRESS'}, None),
                ("clip.keyframe_delete", {"type": 'I', "value": 'PRESS', "alt": True}, None),
                ("clip.join_tracks", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": 'W', "value": 'PRESS'},
                    {
                        "properties": [
                            ("name", 'CLIP_MT_tracking_specials'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.lock_selection'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'D', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.show_disabled'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'S', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.show_marker_search'),
                        ],
                    }
                ),
                (
                    "wm.context_toggle",
                    {"type": 'M', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.use_mute_footage'),
                        ],
                    }
                ),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
                (
                    "clip.clear_track_path",
                    {"type": 'T', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("action", 'REMAINED'),
                            ("clear_active", False),
                        ],
                    }
                ),
                (
                    "clip.clear_track_path",
                    {"type": 'T', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("action", 'UPTO'),
                            ("clear_active", False),
                        ],
                    }
                ),
                (
                    "clip.clear_track_path",
                    {"type": 'T', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("action", 'ALL'),
                            ("clear_active", False),
                        ],
                    }
                ),
                ("clip.cursor_set", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                (
                    "wm.context_set_enum",
                    {"type": 'COMMA', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'BOUNDING_BOX_CENTER'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'COMMA', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'MEDIAN_POINT'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'CURSOR'),
                        ],
                    }
                ),
                (
                    "wm.context_set_enum",
                    {"type": 'PERIOD', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("data_path", 'space_data.pivot_point'),
                            ("value", 'INDIVIDUAL_ORIGINS'),
                        ],
                    }
                ),
                ("clip.copy_tracks", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
                ("clip.paste_tracks", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
            ],
        },
    ),
    (
        "Clip Graph Editor",
        {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                ("clip.change_frame", {"type": 'ACTIONMOUSE', "value": 'PRESS'}, None),
                (
                    "clip.graph_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", False),
                        ],
                    }
                ),
                (
                    "clip.graph_select",
                    {"type": 'SELECTMOUSE', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": 'A', "value": 'PRESS'},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": 'I', "value": 'PRESS', "ctrl": True},
                    {
                        "properties": [
                            ("action", 'INVERT'),
                        ],
                    }
                ),
                ("clip.graph_select_border", {"type": 'B', "value": 'PRESS'}, None),
                ("clip.graph_delete_curve", {"type": 'DEL', "value": 'PRESS'}, None),
                ("clip.graph_delete_curve", {"type": 'X', "value": 'PRESS'}, None),
                ("clip.graph_delete_knot", {"type": 'DEL', "value": 'PRESS', "shift": True}, None),
                ("clip.graph_delete_knot", {"type": 'X', "value": 'PRESS', "shift": True}, None),
                ("clip.graph_view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                ("clip.graph_view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
                ("clip.graph_center_current_frame", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
                (
                    "wm.context_toggle",
                    {"type": 'L', "value": 'PRESS'},
                    {
                        "properties": [
                            ("data_path", 'space_data.lock_time_cursor'),
                        ],
                    }
                ),
                (
                    "clip.clear_track_path",
                    {"type": 'T', "value": 'PRESS', "alt": True},
                    {
                        "properties": [
                            ("action", 'REMAINED'),
                            ("clear_active", True),
                        ],
                    }
                ),
                (
                    "clip.clear_track_path",
                    {"type": 'T', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("action", 'UPTO'),
                            ("clear_active", True),
                        ],
                    }
                ),
                (
                    "clip.clear_track_path",
                    {"type": 'T', "value": 'PRESS', "shift": True, "alt": True},
                    {
                        "properties": [
                            ("action", 'ALL'),
                            ("clear_active", True),
                        ],
                    }
                ),
                (
                    "clip.graph_disable_markers",
                    {"type": 'D', "value": 'PRESS', "shift": True},
                    {
                        "properties": [
                            ("action", 'TOGGLE'),
                        ],
                    }
                ),
                ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
                ("transform.translate", {"type": 'EVT_TWEAK_S', "value": 'ANY'}, None),
                ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
                ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "Clip Dopesheet Editor",
        {"space_type": 'CLIP_EDITOR', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "clip.dopesheet_select_channel",
                    {"type": 'LEFTMOUSE', "value": 'PRESS'},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    }
                ),
                ("clip.dopesheet_view_all", {"type": 'HOME', "value": 'PRESS'}, None),
                ("clip.dopesheet_view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
            ],
        },
    ),
    (
        "3D View Tool:  OBJECT, Move",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "transform.translate",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY'},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "3D View Tool:  OBJECT, Rotate",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "transform.rotate",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY'},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "3D View Tool:  OBJECT, Scale",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                (
                    "transform.resize",
                    {"type": 'EVT_TWEAK_A', "value": 'ANY'},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    }
                ),
            ],
        },
    ),
    (
        "3D View Tool:  OBJECT, Ruler/Protractor",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("view3d.ruler_add", {"type": 'EVT_TWEAK_A', "value": 'ANY'}, None),
            ],
        },
    ),
    (
        "3D View Tool:  PARTICLE, Cursor Click",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("view3d.cursor3d", {"type": 'ACTIONMOUSE', "value": 'CLICK'}, None),
            ],
        },
    ),
    (
        "Spot Lamp Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Area Lamp Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
    (
        "Target Lamp Widgets",
        {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
        {
            "items": [
                ("manipulatorgroup.manipulator_tweak", {"type": 'LEFTMOUSE', "value": 'PRESS', "any": True}, None),
            ],
        },
    ),
]


if __name__ == "__main__":
    import os
    from bpy_extras.keyconfig_utils import keyconfig_import_from_data
    keyconfig_import_from_data(os.path.splitext(os.path.basename(__file__))[0], keyconfig_data)
