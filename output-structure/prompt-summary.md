# Prompt Summary Snippet

## Text Version
```
Begin your output with a brief summary of the user's prompt. Clean up the language, capture the essence of their request, and present it as an improved, concise version. Format this as: "**Summary:** [Your improved summary of the user's request]" followed by your main response.
```

## JSON Integration Example
```json
{
  "system_prompt": "Begin your output with a brief summary of the user's prompt. Clean up the language, capture the essence of their request, and present it as an improved, concise version. Format this as: '**Summary:** [Your improved summary of the user's request]' followed by your main response. [Additional system instructions continue here...]",
  "user_prompt": "Your user prompt here"
}
```

## Usage Notes
- Provides clarity on what the model understood from the request
- Helps identify misinterpretations early in the response
- Creates a professional, structured output format
- Useful for documentation and conversation logging
- Improves communication clarity in complex requests
