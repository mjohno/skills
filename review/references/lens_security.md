# Lens: Security

Migrated from `design/references/persona_review_security.md`.

## Criteria

### 1. Authentication & Authorization
- Are authN and authZ properly designed?
- Are there any privilege escalation risks?

### 2. Data Protection
- Is sensitive data encrypted in transit and at rest?
- Are there any data leakage vectors?

### 3. Input Validation
- Are all external inputs validated and sanitized?
- Are there injection risks?

### 4. API Security
- Are endpoints protected?
- Are rate limiting, CORS, and CSRF considerations addressed?

### 5. Secrets Management
- Are API keys, tokens, and credentials handled securely?

### 6. Threat Model
- Has the design considered relevant threats (e.g., MITM, replay attacks, data exfiltration)?

### 7. Compliance
- Does the design align with relevant compliance requirements (e.g., GDPR, HIPAA, SOC2)?
