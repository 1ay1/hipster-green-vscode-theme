# 🚀 Release Guide

This guide explains how to create releases for the Hipster Green VS Code theme using GitHub Actions.

## 📋 Prerequisites

### 1. Repository Setup
- Ensure your code is pushed to the main branch
- GitHub repository should be public (for marketplace publishing)

### 2. VS Code Marketplace (Optional)
To publish to the VS Code Marketplace, you'll need:
1. **Azure DevOps Account**: Sign up at [dev.azure.com](https://dev.azure.com)
2. **Personal Access Token (PAT)**:
   - Go to User Settings → Personal Access Tokens
   - Create new token with **Marketplace (manage)** scope
   - Save this token securely

### 3. GitHub Secrets Setup
Add the following secrets to your GitHub repository:

1. Go to your GitHub repo → Settings → Secrets and variables → Actions
2. Add repository secrets:
   - `VSCE_PAT`: Your Azure DevOps Personal Access Token (for marketplace publishing)

## 🏷️ Creating a Release

### Automatic Release Process

1. **Update Version**: Ensure `package.json` has the correct version number
   ```bash
   # Update version in package.json to your target version (e.g., 1.1.0)
   npm version patch   # for patch releases (1.0.0 → 1.0.1)
   npm version minor   # for minor releases (1.0.0 → 1.1.0)  
   npm version major   # for major releases (1.0.0 → 2.0.0)
   ```

2. **Create and Push Tag**: This triggers the release workflow
   ```bash
   git add .
   git commit -m "Release v1.1.0"
   git tag v1.1.0
   git push origin main
   git push origin v1.1.0
   ```

3. **Automatic Process**: GitHub Actions will:
   - ✅ Validate the theme files
   - ✅ Build the VSIX package  
   - ✅ Create a GitHub Release
   - ✅ Upload the VSIX file as a release asset
   - ✅ Publish to VS Code Marketplace (if PAT is configured)

### Manual Release Steps (if needed)

If you need to create a release manually:

```bash
# 1. Install dependencies
npm install

# 2. Package the extension
npx vsce package

# 3. Test the package locally
code --install-extension hipster-green-theme-1.1.0.vsix

# 4. Create GitHub release manually and upload the VSIX
# Go to GitHub → Releases → Create new release
```

## 🔄 Workflow Details

### Release Workflow (`release.yml`)
**Triggers**: When you push a tag starting with `v` (e.g., `v1.1.0`)

**Process**:
1. Checkout code and setup Node.js
2. Install dependencies and VSCE
3. Verify package.json version matches the git tag
4. Build VSIX package
5. Create GitHub release with changelog
6. Upload VSIX as release asset
7. Publish to VS Code Marketplace (if configured)

### CI Workflow (`ci.yml`)
**Triggers**: Push to main/develop branches, Pull Requests

**Process**:
1. Validate package.json structure
2. Validate theme file JSON
3. Test VSIX packaging
4. Verify package contents
5. Upload test artifacts

## 📦 Release Checklist

Before creating a release:

- [ ] **Version updated** in `package.json`
- [ ] **Changelog updated** with new features/fixes
- [ ] **README updated** if needed
- [ ] **Tests passing** (CI workflow green)
- [ ] **Theme tested** in VS Code manually
- [ ] **Screenshots updated** if UI changes
- [ ] **No lint errors** in theme JSON file

## 🐛 Troubleshooting

### Version Mismatch Error
```
Version mismatch! Package.json version (1.1.0) doesn't match tag (1.0.0)
```
**Solution**: Ensure your package.json version exactly matches your git tag (without the 'v' prefix)

### VSIX Missing Files Error
```
Theme file missing from VSIX
```
**Solution**: Check your `.vscodeignore` file isn't excluding required theme files

### Marketplace Publishing Failed
**Common issues**:
- Invalid or expired VSCE_PAT token
- Publisher name doesn't match your Azure DevOps organization
- Extension name already exists

### Permission Denied
**Solution**: Check repository permissions and ensure secrets are properly configured

## 📊 Release Artifacts

Each successful release creates:

1. **GitHub Release**: With version notes and changelog
2. **VSIX File**: Downloadable extension package
3. **VS Code Marketplace**: Published extension (if configured)
4. **Git Tag**: Version reference point

## 🔍 Monitoring Releases

- **GitHub Actions**: Check workflow runs under Actions tab
- **Releases**: Monitor downloads and feedback in Releases section  
- **Marketplace**: Track installs/ratings on marketplace.visualstudio.com
- **Issues**: Watch for user feedback in GitHub Issues

---

## 🎯 Quick Release Commands

```bash
# Quick patch release
npm version patch && git push origin main && git push origin --tags

# Quick minor release  
npm version minor && git push origin main && git push origin --tags

# Quick major release
npm version major && git push origin main && git push origin --tags
```

The GitHub Actions will handle the rest automatically! 🚀