# Gmail-Safe HTML Formatting Snippet

## Text Version
```
Format your output in HTML that is Gmail-friendly and email client safe. Use only inline CSS styles and basic HTML elements (p, div, span, strong, em, ul, ol, li, br). Do not include outer HTML elements like <html>, <head>, or <body> - provide only the inner content elements that can be injected into email templates.
```

## JSON Integration Example
```json
{
  "system_prompt": "Format your output in HTML that is Gmail-friendly and email client safe. Use only inline CSS styles and basic HTML elements (p, div, span, strong, em, ul, ol, li, br). Do not include outer HTML elements like <html>, <head>, or <body> - provide only the inner content elements that can be injected into email templates. [Additional system instructions continue here...]",
  "user_prompt": "Your user prompt here"
}
```

## Usage Notes
- Compatible with Gmail, Outlook, and other major email clients
- Uses inline CSS to avoid style stripping
- Excludes problematic elements like <script>, <style>, <link>
- Perfect for email marketing templates and automated email generation
- Avoids security issues with email client filtering
