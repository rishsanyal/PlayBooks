export const InputTypes = {
  TEXT: "TEXT_FT",
  MULTILINE: "MULTILINE_FT",
  BUTTON: "BUTTON_FT",
  IFRAME_RENDER: "IFRAME_RENDER_FT",
  DROPDOWN: "DROPDOWN_FT",
  TYPING_DROPDOWN: "TYPING_DROPDOWN_FT",
  TYPING_DROPDOWN_MULTIPLE: "TYPING_DROPDOWN_MULTIPLE_FT",
  WYISWYG: "WYSIWYG_FT",
  COMPOSITE: "COMPOSITE_FT",
  DATE: "DATE_FT",
  STRING_ARRAY: "STRING_ARRAY_FT",
  TYPING_DROPDOWN_MULTIPLE_SELECTION: "TYPING_DROPDOWN_MULTIPLE_SELECTION_FT",
  TEXT_BUTTON: "TEXT_BUTTON_FT",
  CRON: "CRON_FT",
} as const;

export type InputType = (typeof InputTypes)[keyof typeof InputTypes];
