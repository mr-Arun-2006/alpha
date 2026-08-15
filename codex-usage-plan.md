# 🤖 Codex Integration Plan

## 🎯 Objective
Use Codex to accelerate development of the stock analytics system while keeping strong validation and review steps.

## 🔧 High-Value Use Cases

### 1. Code Generation
Prompt examples:
- "Generate a FastAPI endpoint for stock prediction with input validation."
- "Create a Python module for RSI + moving average features."

### 2. Debugging
Prompt examples:
- "Fix NaN-handling bug in this Pandas preprocessing function."
- "Why does this scikit-learn model crash on empty split?"

### 3. Refactoring
Prompt examples:
- "Refactor this pipeline into modular services with clean interfaces."
- "Reduce API latency in this endpoint without changing output."

### 4. Test + Docs Generation
Prompt examples:
- "Generate pytest tests for these API routes."
- "Write docstrings and README section for this module."

## 🧠 Workflow Integration
Developer → Codex draft → Human review → Local tests → Commit/PR → Deploy

## ✅ Best Practices
- Keep prompts focused on one module at a time.
- Always run tests on generated code.
- Ask for edge-case handling explicitly (missing values, API errors, empty datasets).
- Prefer small iterative prompts over one giant prompt.

## 🔒 Security Guardrails
- Never include raw API secrets in prompts.
- Use `.env` + environment variables.
- Review generated code for unsafe shell/db operations before merge.
