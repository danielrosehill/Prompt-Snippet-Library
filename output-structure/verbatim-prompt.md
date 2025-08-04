# Verbatim Prompt Snippet

## Text Version
```
Begin your output by reproducing the user's prompt exactly as they wrote it. Format this as: "**User Prompt:** [Exact verbatim reproduction of the user's prompt]" followed by your response. Maintain all original spelling, punctuation, and formatting.
```

## JSON Integration Example
```json
{
  "system_prompt": "Begin your output by reproducing the user's prompt exactly as they wrote it. Format this as: '**User Prompt:** [Exact verbatim reproduction of the user's prompt]' followed by your response. Maintain all original spelling, punctuation, and formatting. [Additional system instructions continue here...]",
  "user_prompt": "Your user prompt here"
}
```

## Usage Notes
- Creates a complete record of the original request
- Useful for audit trails and conversation logging
- Prevents ambiguity about what was actually asked
- Helpful for debugging prompt interpretation issues
- Maintains accountability in automated systems
