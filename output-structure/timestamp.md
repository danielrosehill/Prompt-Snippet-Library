# Timestamp Snippet

## Text Version
```
Begin your output with the current date and time. Format this as: "**Generated:** [Current date and time in YYYY-MM-DD HH:MM:SS format]" followed by your response. Use your knowledge of the current date and time to provide an accurate timestamp.
```

## JSON Integration Example
```json
{
  "system_prompt": "Begin your output with the current date and time. Format this as: '**Generated:** [Current date and time in YYYY-MM-DD HH:MM:SS format]' followed by your response. Use your knowledge of the current date and time to provide an accurate timestamp. [Additional system instructions continue here...]",
  "user_prompt": "Your user prompt here"
}
```

## Usage Notes
- Provides temporal context for generated content
- Useful for logging and audit purposes
- Helps track when information was generated
- Important for time-sensitive responses
- Note: Accuracy depends on model's current time awareness
- Consider providing current time in system context for better accuracy
