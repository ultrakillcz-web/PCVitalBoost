# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of PCVitalBoost seriously. If you have discovered a security vulnerability, please report it to us as described below.

### Where to Report

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via:
- Opening a security advisory on GitHub
- Emailing the maintainers (check GitHub profiles for contact info)

### What to Include

Please include the following information:
- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability

### Response Timeline

- We will acknowledge receipt of your report within 48 hours
- We will provide a detailed response within 7 days
- We will keep you informed of progress toward a fix
- We will notify you when the vulnerability is fixed

### Safe Harbor

We consider security research and disclosure conducted under this policy to be:
- Authorized in accordance with applicable laws
- Conducted in good faith
- Valuable to the security of the project

We will not pursue legal action against researchers who follow this policy.

## Security Best Practices

When using PCVitalBoost:

1. **Download from official sources only**
   - GitHub releases
   - Official package repositories

2. **Verify checksums**
   - Compare SHA256 hashes of downloaded files

3. **Run with appropriate permissions**
   - Only grant admin rights when necessary
   - Use standard user account when possible

4. **Keep updated**
   - Enable auto-updates
   - Regularly check for new versions

5. **Review permissions**
   - Check what the app can access
   - Limit unnecessary permissions

## Known Security Considerations

### Admin/Root Access
Some features require elevated privileges:
- Driver updates
- System optimization
- Context menu integration

**We recommend:** Only run with admin when needed, use standard mode for scanning/analysis.

### Network Access
The app makes network requests for:
- Checking updates
- Downloading driver/program updates

**We recommend:** Use firewall rules if you want to restrict network access.

### File Access
The app accesses:
- Temporary files (for cleaning)
- System information
- Installed programs list

**We recommend:** Review cleaned files before deletion, enable backup.

## Third-Party Dependencies

PCVitalBoost uses several third-party libraries. We regularly update dependencies to patch known vulnerabilities.

Current dependencies:
- Kivy
- KivyMD
- Plyer
- psutil
- requests
- packaging

See `requirements.txt` for specific versions.

## Disclosure Policy

We follow coordinated disclosure:
1. Researcher reports vulnerability privately
2. We confirm and develop fix
3. We release patched version
4. After patch is released, we publish security advisory
5. We credit the researcher (unless they prefer anonymity)

---

Thank you for helping keep PCVitalBoost and our users safe!
