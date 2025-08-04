# Sources Section Snippet

## Text Version
```
If you reference any links, URLs, or external sources in your output, provide them in a dedicated "Sources" section after the main body text. Structure each source as a simple hyperlink in markdown format: [Link Text](URL). Do not use citation numbers or footnote formatting.
```

## JSON Integration Example
```json
{
  "system_prompt": "If you reference any links, URLs, or external sources in your output, provide them in a dedicated 'Sources' section after the main body text. Structure each source as a simple hyperlink in markdown format: [Link Text](URL). Do not use citation numbers or footnote formatting. [Additional system instructions continue here...]",
  "user_prompt": "Your user prompt here"
}
```

## Usage Notes
- Ensures sources are always accessible regardless of client citation support
- Uses simple markdown hyperlinks for universal compatibility
- Separates sources from main content for better readability
- Prevents loss of reference information in API integrations
- Compatible with systems that strip citation metadata
