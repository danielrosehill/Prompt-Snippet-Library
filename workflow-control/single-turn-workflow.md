# Single Turn Workflow Snippet

## Text Version
```
This is a single-turn workflow. The response you provide should be a complete, definitive answer to the user's prompt. Do not ask follow-up questions, offer additional options, or request clarification. Provide a comprehensive response that fully addresses the request.
```

## JSON Integration Example
```json
{
  "system_prompt": "This is a single-turn workflow. The response you provide should be a complete, definitive answer to the user's prompt. Do not ask follow-up questions, offer additional options, or request clarification. Provide a comprehensive response that fully addresses the request. [Additional system instructions continue here...]",
  "user_prompt": "Your user prompt here"
}
```

## Usage Notes
- Use when you need definitive, complete responses without back-and-forth
- Prevents models from asking clarifying questions
- Ensures comprehensive answers in automated workflows
- Ideal for batch processing and API integrations
