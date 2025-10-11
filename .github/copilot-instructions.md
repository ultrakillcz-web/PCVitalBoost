# GitHub Copilot Instructions for PCVitalBoost

## Project Overview

PCVitalBoost is a multi-platform application (Windows, macOS, Linux, Android, iOS) for PC optimization, driver/program updates, and system cleaning. The project is written in Python 3.8+ using Kivy/KivyMD for the UI framework.

## Code Style and Standards

### Python

- **Follow PEP 8** style guide strictly
- Use 4 spaces for indentation (not tabs)
- Maximum line length: 100 characters
- Use UTF-8 encoding for all Python files
- Always include docstrings for functions, classes, and modules
- Write self-documenting, readable code with clear variable names
- Keep functions small and focused on a single responsibility

### Docstring Format

Use the following format for docstrings:

```python
def function_name(param1, param2):
    """
    Brief description of the function
    
    Args:
        param1 (type): Description of parameter 1
        param2 (type): Description of parameter 2
        
    Returns:
        type: Description of return value
        
    Raises:
        ExceptionType: Description of when this exception is raised
    """
    pass
```

### Imports

- Group imports in the following order:
  1. Standard library imports
  2. Third-party imports (kivy, kivymd, plyer, psutil, requests)
  3. Local application imports
- Use absolute imports for project modules
- Avoid wildcard imports (`from module import *`)

## Multi-Platform Considerations

- **Always consider multi-platform compatibility** when writing code
- Use `os.path` or `pathlib.Path` for file system operations
- Test platform-specific code with `platform.system()` checks
- Supported platforms: Windows, macOS, Linux, Android, iOS
- Use Plyer for cross-platform system integration
- Handle platform-specific functionality gracefully with try/except or platform checks

Example:
```python
import platform

if platform.system() == 'Windows':
    # Windows-specific code
elif platform.system() == 'Darwin':
    # macOS-specific code
elif platform.system() == 'Linux':
    # Linux-specific code
```

## Security and Privacy

- **Never collect or send user data** to external servers
- Ensure all operations respect user privacy
- Always request appropriate permissions before system modifications
- Use secure practices for file operations (no arbitrary file deletion)
- Validate all user inputs to prevent security vulnerabilities
- When cleaning files, always verify paths before deletion
- Log all system-modifying operations for transparency

## Testing

- Write unit tests for all new modules and functions
- Place tests in the `tests/` directory
- Use Python's built-in `unittest` framework
- Test across multiple Python versions (3.8, 3.9, 3.10, 3.11)
- Include platform-specific test cases when applicable
- Aim for meaningful test coverage, not just high percentages
- Run tests before submitting pull requests: `python -m unittest discover tests -v`

## UI Development

- Use **Kivy 2.3.0+** and **KivyMD 1.2.0+** for UI components
- Follow Material Design principles for consistency
- Ensure UI is responsive across different screen sizes
- Support both desktop and mobile form factors
- Use KivyMD widgets for a modern, consistent look
- Keep UI code in the `src/ui/` directory
- Separate business logic from UI code

## Project Structure

```
PCVitalBoost/
├── src/                      # Source code
│   ├── main.py              # Entry point
│   ├── auto_updater.py      # Auto-update system
│   ├── context_menu.py      # Context menu integration
│   ├── modules/             # Core functionality
│   │   ├── driver_updater.py
│   │   ├── program_updater.py
│   │   ├── system_optimizer.py
│   │   └── system_cleaner.py
│   └── ui/                  # User interface
│       └── main_window.py
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── examples/                # Usage examples
└── .github/                 # GitHub configuration
```

## Commit Messages

Use clear, descriptive commit messages following this format:

- `feat: Add new feature X` - New features
- `fix: Resolve bug in Y` - Bug fixes
- `docs: Update documentation for Z` - Documentation updates
- `test: Add tests for W` - Test additions
- `refactor: Improve code structure in V` - Code refactoring
- `style: Format code according to PEP 8` - Style/formatting
- `perf: Optimize performance of U` - Performance improvements
- `chore: Update dependencies` - Maintenance tasks

## Dependencies

When adding new dependencies:
- Add them to `requirements.txt`
- Ensure they are compatible with Python 3.8+
- Verify cross-platform compatibility
- Prefer well-maintained, stable libraries
- Document the purpose of the dependency

Current core dependencies:
- kivy >= 2.3.0
- kivymd >= 1.2.0
- plyer >= 2.1.0
- psutil >= 5.9.0
- requests >= 2.31.0
- packaging >= 23.0

## Logging

- Use Python's `logging` module for all logging
- Log to both file (`pcvitalboost.log`) and console
- Use appropriate log levels:
  - `DEBUG`: Detailed diagnostic information
  - `INFO`: General informational messages
  - `WARNING`: Warning messages for non-critical issues
  - `ERROR`: Error messages for failures
  - `CRITICAL`: Critical issues that may crash the application
- Include context in log messages for easier debugging

Example:
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Starting driver update process")
```

## Documentation

- Update `README.md` for user-facing changes
- Update `CONTRIBUTING.md` for contribution guideline changes
- Update `docs/API.md` for API changes
- Update `CHANGELOG.md` for version releases
- Document all public APIs and modules
- Include examples in documentation when helpful
- Keep documentation in Portuguese (project's primary language) unless specified otherwise

## License

- All contributions are licensed under **LGPL-2.1**
- Include license headers in new files when appropriate
- Respect third-party licenses in dependencies
- Do not introduce GPL-incompatible code

## Code Review Checklist

Before submitting code, ensure:
- [ ] Code follows PEP 8 standards
- [ ] All functions have docstrings
- [ ] Multi-platform compatibility is considered
- [ ] Security and privacy guidelines are followed
- [ ] Unit tests are written and passing
- [ ] No warnings from linters
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] No hardcoded paths or credentials
- [ ] Logging is appropriate and informative

## Performance

- Optimize for responsiveness and efficiency
- Avoid blocking the UI thread with long operations
- Use threading or async operations for time-consuming tasks
- Monitor memory usage, especially for file operations
- Clean up resources properly (close files, release handles)
- Test performance on older hardware when possible

## Internationalization (Future)

- Prepare for future multilingual support (English, Spanish planned)
- Use string constants that can be easily localized
- Avoid hardcoding UI text in code
- Keep user-facing strings separate from logic

## Build and Distribution

- Use **PyInstaller** for desktop executables (Windows, macOS, Linux)
- Use **Buildozer** for mobile builds (Android, iOS)
- Test builds on all target platforms before release
- Follow configuration in `PCVitalBoost.spec` and `buildozer.spec`
- Ensure all dependencies are included in builds
- Test executables on clean systems without Python installed

## Additional Guidelines

- **Be respectful and professional** in all communications
- **Ask questions** if requirements are unclear
- **Test thoroughly** before submitting changes
- **Keep changes focused** - one feature or fix per PR
- **Consider backward compatibility** when making changes
- **Document breaking changes** clearly
- **Provide examples** for new features
