# Simplified Chinese interface

The desktop GUI defaults to Simplified Chinese. The localization layer is
presentation-only: film and paper profile IDs, enum values, project JSON keys,
parameter values, and image data remain in their original form.

## Switch language

Windows PowerShell, current session:

```powershell
$env:SPEKTRAFILM_LANGUAGE = "zh_CN"
spektrafilm
```

Restore the original English interface:

```powershell
$env:SPEKTRAFILM_LANGUAGE = "en"
spektrafilm
```

To make the choice persistent for the current Windows user, set the
`SPEKTRAFILM_LANGUAGE` user environment variable to `zh_CN` or `en`,
then restart the terminal/application.

## Localization boundary

Only user-facing GUI presentation strings are translated. RAW, RGB, sRGB,
CCTF, EV, LUT, brand names, and film/paper stock names remain recognizable.
Errors, exception details, stack traces, and developer diagnostics may remain
in English. No film simulation algorithm, profile data, default parameter,
or user image is modified by localization.
