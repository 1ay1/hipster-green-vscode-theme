# Hipster Green Theme for VS Code

An enhanced port of Tabby/iTerm2's Hipster Green color scheme - a vibrant terminal-inspired theme with classic green-on-black aesthetic, modern syntax highlighting, semantic tokens, and comprehensive IDE integration.

## 📸 Screenshots

### Main Editor View
![Main Editor](images/Screenshot.png)
*The enhanced Hipster Green theme showcasing syntax highlighting, bracket colorization, and the distinctive green-on-black aesthetic*

## ✨ Features

- **🎨 Enhanced Dark Theme** with retro terminal aesthetic
- **🌈 Comprehensive Syntax Highlighting** with semantic tokens for TypeScript, Python, Rust, and more
- **🔗 Bracket Pair Colorization** with 6 distinct colors for nested brackets
- **🔍 Git Integration** with enhanced diff visualization and merge conflict colors
- **🐛 Debugging Experience** with colored breakpoints, call stack, and console output
- **🗺️ Minimap & Overview Ruler** with enhanced indicators for better navigation
- **🔎 Search & Replace** styling with improved result highlighting
- **📍 Breadcrumb Navigation** for better file path visibility
- **💬 Notification Styling** for consistent user feedback
- **🖥️ Terminal Integration** with matching colors and cursor styling

## Installation

### From VS Code Marketplace

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Hipster Green Theme"
4. Click Install

### Manual Installation

1. Download the latest release from [GitHub](https://github.com/1ay1/hipster-green-vscode-theme)
2. Extract the files to your VS Code extensions directory:
   - **Windows**: `%USERPROFILE%\.vscode\extensions\`
   - **macOS**: `~/.vscode/extensions/`
   - **Linux**: `~/.vscode/extensions/`
3. Restart VS Code

### From Source

```bash
git clone https://github.com/1ay1/hipster-green-vscode-theme.git
cd hipster-green-vscode-theme
npm install @vscode/vsce
npx vsce package
code --install-extension hipster-green-theme-1.1.0.vsix
```

## Activation

1. Open VS Code
2. Go to File → Preferences → Color Theme (Ctrl+K Ctrl+T)
3. Select "Hipster Green Dark"

## 🎨 Color Palette

The theme uses a carefully selected palette of greens and complementary colors, now enhanced with semantic token support:

### Primary Colors
- **Primary Green**: `#84c138` - Main text and UI elements
- **Bright Green**: `#23ff18` - Accents and highlights  
- **Background**: `#100a05` - Deep dark brown-black
- **Secondary Background**: `#1a1510` - Lighter panels

### Syntax Colors
- **Comments**: `#5a6a50` - Muted green (italic)
- **Strings**: `#00a600` - Vivid green
- **Keywords**: `#b200b2` - Magenta for contrast (bold)
- **Functions**: `#00a6b2` - Cyan-blue (bold)
- **Classes/Types**: `#e5e500` - Yellow (bold)
- **Numbers/Constants**: `#b200b2` - Magenta
- **Operators**: `#86a93e` - Olive green
- **Variables**: `#84c138` - Primary green

### UI Enhancement Colors
- **Error**: `#e50000` - Bright red for errors and breakpoints
- **Warning**: `#e5e500` - Yellow for warnings and modifications
- **Info**: `#00a6b2` - Cyan for information and links
- **Git Added**: `#00a600` - Green for additions
- **Git Deleted**: `#e50000` - Red for deletions
- **Git Modified**: `#e5e500` - Yellow for changes

##  Development

To contribute to this theme:

1. **Clone the repository**
   ```bash
   git clone https://github.com/1ay1/hipster-green-vscode-theme.git
   cd hipster-green-vscode-theme
   ```

2. **Make your changes** 
   - Edit `themes/hipster-green-color-theme.json` for colors and syntax highlighting
   - Edit `package.json` for metadata and version updates

3. **Test your changes**
   - Press `F5` in VS Code to open a new Extension Development Host window
   - Use `Ctrl+K Ctrl+T` to switch to your modified theme

4. **Package and test**
   ```bash
   npm install @vscode/vsce
   npx vsce package
   code --install-extension *.vsix
   ```

5. **Submit a pull request**

### Adding Screenshots

To add more screenshots showcasing specific features:

1. **Capture screenshots** showing:
   - Different language syntax highlighting (Python, TypeScript, Rust, etc.)
   - Debugging session with colored breakpoints
   - Git diff view with enhanced colors
   - Bracket pair colorization in action
   - Minimap and overview ruler indicators

2. **Save images** in the `images/` folder with descriptive names:
   - `syntax-typescript.png`
   - `debugging-session.png` 
   - `git-diff-view.png`
   - `bracket-colorization.png`

3. **Update README.md** to reference the new images

4. **Keep images optimized** - use PNG format and compress for web

### 🚀 Creating Releases

This project uses GitHub Actions for automated releases:

1. **Update version**: `npm version minor` (or patch/major)
2. **Push changes**: `git push origin main`  
3. **Create tag**: `git tag v1.1.0 && git push origin v1.1.0`
4. **Automatic release**: GitHub Actions builds and publishes VSIX

See [RELEASE.md](RELEASE.md) for detailed release instructions.

### Theme Structure

- **`colors`**: UI element colors (sidebars, tabs, status bar, etc.)
- **`tokenColors`**: Traditional syntax highlighting rules
- **`semanticTokenColors`**: Enhanced language-specific highlighting (new in v1.1.0)

### Adding New Language Support

To add semantic token support for a new language:
1. Add language-specific semantic token colors in the `semanticTokenColors` section
2. Use the pattern `"property.language"` for language-specific overrides
3. Test with actual code files in that language

## 📋 What's New in v1.1.0

- ✨ **Semantic Token Support**: Enhanced highlighting for TypeScript, Python, Rust, and C/C++
- 🌈 **Bracket Pair Colorization**: 6 distinct colors for better code structure visibility  
- 🔍 **Enhanced Git Integration**: Better diff visualization and merge conflict resolution
- 🐛 **Improved Debugging**: Color-coded breakpoints, call stack, and console output
- 🗺️ **Better Navigation**: Enhanced minimap, overview ruler, and breadcrumbs
- 💡 **Symbol Icons**: Color-coded icons for different code elements in outline view
- 🎯 **Search & Replace**: Improved styling for find/replace operations
- 🔧 **Technical**: Modern VS Code API support with comprehensive theme coverage

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- Original Hipster Green color scheme from Tabby/iTerm2
- Ported to VS Code by [Ayush Bhat](https://github.com/1ay1)

## Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/1ay1/hipster-green-vscode-theme/issues) on GitHub.

---

**Enjoy coding with the Hipster Green theme!** 🟢