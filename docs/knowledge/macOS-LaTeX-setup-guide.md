# macOS LaTeX Setup Guide for Linear Algebra Slides

**Purpose:** Complete guide for Mac users to set up LaTeX environment for compiling the Linear Algebra Beamer slides.

**Target Audience:** Mac users (macOS 11+) who need to compile `.tex` files from this repository.

---

## Quick Start (TL;DR)

```bash
# Install BasicTeX (recommended for most users)
brew install basictex

# Update PATH (restart terminal after this)
echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.zshrc

# Install required packages
sudo tlmgr update --self
sudo tlmgr install beamer metropolis pgfopts tcolorbox tikz \
  environ trimspaces etoolbox appendixnumberbeamer

# Compile a slide file
cd /path/to/Linear-Algebra-Slides
pdflatex rowoperation.tex
```

---

## Understanding Your Options

### Option 1: BasicTeX (Recommended)

**Pros:**
- ✅ Small download (~100MB)
- ✅ Fast installation
- ✅ Installs only what you need via `tlmgr`
- ✅ Perfect for this project
- ✅ Official TeX Live distribution

**Cons:**
- ⚠️ Requires manual package installation
- ⚠️ Need to configure PATH

**Best for:** Developers who want a lean installation and don't mind installing packages as needed.

### Option 2: MacTeX (Full Distribution)

**Pros:**
- ✅ Everything included (~4.5GB)
- ✅ No package management needed
- ✅ Comes with GUI editors (TeXShop, BibDesk)
- ✅ Automatic PATH configuration

**Cons:**
- ⚠️ Very large download (4.5GB)
- ⚠️ Installs many packages you won't use

**Best for:** Users who want a "batteries included" solution and have disk space to spare.

### Recommendation for This Project

**Use BasicTeX** unless you're already using LaTeX for other projects that need the full distribution.

---

## Installation Instructions

### Method 1: BasicTeX via Homebrew (Recommended)

#### Step 1: Install Homebrew (if not installed)

```bash
# Check if Homebrew is installed
brew --version

# If not installed, install it:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install BasicTeX

```bash
brew install basictex
```

**Wait time:** 2-5 minutes

#### Step 3: Configure PATH

BasicTeX installs to `/Library/TeX/texbin/`, which needs to be in your PATH.

**For macOS 10.15+ (Catalina and later) using zsh:**

```bash
# Add to ~/.zshrc
echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc
```

**For older macOS using bash:**

```bash
# Add to ~/.bash_profile
echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.bash_profile

# Reload shell configuration
source ~/.bash_profile
```

#### Step 4: Verify Installation

```bash
# Close and reopen your terminal, then:
pdflatex --version

# Expected output:
# pdfTeX 3.141592653-2.6-1.40.XX (TeX Live 2024)
```

If you see "command not found", restart your terminal or computer.

#### Step 5: Update TeX Live Manager

```bash
sudo tlmgr update --self
sudo tlmgr update --all
```

**Note:** Use `sudo` for BasicTeX installations. MacTeX (full) may not require sudo.

#### Step 6: Install Required Packages

For the Linear Algebra slides, you need these packages:

```bash
sudo tlmgr install \
  beamer \
  metropolis \
  pgfopts \
  tcolorbox \
  environ \
  tikz \
  etoolbox \
  appendixnumberbeamer \
  booktabs \
  ccicons \
  mathrsfs \
  chngcntr
```

**Wait time:** 3-5 minutes

#### Step 7: Install Additional Packages (as needed)

Some slides may require additional packages. Install them on-demand:

```bash
# If you get "xyz.sty not found" errors:
sudo tlmgr install xyz
```

Common additional packages for this project:

```bash
sudo tlmgr install \
  unicode-math \
  qrcode \
  colortbl \
  xy \
  ytableau \
  cancel \
  polynom
```

---

### Method 2: MacTeX (Full Distribution)

#### Step 1: Download MacTeX

Visit: https://www.tug.org/mactex/

Download: `MacTeX.pkg` (~4.5GB)

#### Step 2: Install

1. Open the downloaded `.pkg` file
2. Follow the installer prompts
3. Installation takes 10-20 minutes

#### Step 3: Verify

```bash
# Open a new terminal window
pdflatex --version
```

**PATH is automatically configured** - no manual setup needed.

**All packages are pre-installed** - skip Step 6 from Method 1.

---

## Compiling Your First Slide

### Navigate to the Repository

```bash
cd ~/path/to/Linear-Algebra-Slides
```

### Compile a Slide File

```bash
pdflatex rowoperation.tex
```

**Expected output:**
```
This is pdfTeX, Version 3.141592653-2.6-1.40.XX (TeX Live 2024)
...
Output written on rowoperation.pdf (42 pages, XXXXX bytes).
Transcript written on rowoperation.log.
```

### View the PDF

```bash
# Open in default PDF viewer (Preview)
open rowoperation.pdf

# Or use a specific PDF viewer
open -a "Skim" rowoperation.pdf  # If you have Skim installed
```

---

## Troubleshooting

### Issue 1: `pdflatex: command not found`

**Cause:** PATH not configured or terminal not restarted.

**Solution:**

```bash
# Verify TeX installation location
ls /Library/TeX/texbin/

# Manually add to PATH (temporary)
export PATH="/Library/TeX/texbin:$PATH"

# Permanent fix: Add to ~/.zshrc (see Step 3 above)
echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.zshrc
source ~/.zshrc
```

**Still not working?** Restart your terminal or computer.

---

### Issue 2: `beamer.cls not found` or `xyz.sty not found`

**Cause:** Required package not installed (BasicTeX only).

**Solution:**

```bash
# Install the missing package
sudo tlmgr install beamer  # Or whatever package is missing

# If tlmgr says "unknown package", search for it:
tlmgr search --global --file beamer.cls

# Then install the package name shown
```

**For MacTeX users:** This should never happen - all packages are pre-installed.

---

### Issue 3: `tlmgr: command not found`

**Cause:** BasicTeX not properly installed or PATH issue.

**Solution:**

```bash
# Check if tlmgr exists
ls /Library/TeX/texbin/tlmgr

# If it exists, fix PATH (see Issue 1)
# If not, reinstall BasicTeX:
brew reinstall basictex
```

---

### Issue 4: Permission Denied When Running `tlmgr`

**Error:**
```
You don't have permission to change the TeX Live installation
```

**Solution:**

```bash
# Use sudo for BasicTeX installations
sudo tlmgr install packagename

# Check ownership of TeX directories
ls -la /usr/local/texlive/

# If needed, fix permissions (rarely necessary)
sudo chown -R $(whoami) /usr/local/texlive/
```

---

### Issue 5: `natwidth` / `natheight` Errors

**Error:**
```
! Package pdftex.def Error: Options `natwidth', `natheight' not supported.
```

**Cause:** Deprecated `\includegraphics` parameters (already fixed in this repo).

**Solution:** If you see this in other files, remove `natwidth=XX,natheight=XX` from `\includegraphics` commands.

**Before:**
```latex
\includegraphics[scale=0.07,natwidth=10,natheight=10]{Pictures/bean.png}
```

**After:**
```latex
\includegraphics[scale=0.07]{Pictures/bean.png}
```

---

### Issue 6: Metropolis Theme Warning

**Warning:**
```
Package beamerthememetropolis Warning: You need to compile with XeLaTeX or LuaLaTeX
```

**Explanation:** Metropolis theme is optimized for XeLaTeX/LuaLaTeX but **works fine with pdflatex**.

**Action:** Ignore this warning. The PDF will compile correctly.

**Optional:** If you prefer, compile with XeLaTeX for better font rendering:

```bash
xelatex rowoperation.tex
```

---

### Issue 7: Pictures Not Found

**Error:**
```
! Package pdftex.def Error: File `Pictures/bean.png' not found.
```

**Cause:** Running `pdflatex` from wrong directory.

**Solution:**

```bash
# Make sure you're in the repository root
cd ~/path/to/Linear-Algebra-Slides

# Then compile
pdflatex rowoperation.tex

# The Pictures/ directory must be in the same location as the .tex file
```

---

## Recommended Editors and IDEs

### Option 1: VS Code (Recommended)

**Best for:** Modern development workflow

**Setup:**
1. Install VS Code: https://code.visualstudio.com/
2. Install extension: **LaTeX Workshop** by James Yu
3. Open the repository in VS Code
4. Click on a `.tex` file
5. Press `Cmd+Option+B` to build
6. PDF preview appears automatically

**Advantages:**
- ✅ Integrated PDF preview
- ✅ Syntax highlighting
- ✅ Auto-completion
- ✅ Error highlighting
- ✅ Git integration

---

### Option 2: TeXShop (Comes with MacTeX)

**Best for:** Traditional LaTeX workflow

**Setup:**
1. Installed automatically with MacTeX (not with BasicTeX)
2. Open `.tex` file in TeXShop
3. Click "Typeset" button

**Advantages:**
- ✅ Simple and focused
- ✅ Built-in PDF viewer
- ✅ Mac-native interface

**Download separately for BasicTeX users:**
- https://pages.uoregon.edu/koch/texshop/

---

### Option 3: Overleaf (Cloud-Based)

**Best for:** No local installation needed

**Setup:**
1. Go to https://www.overleaf.com/
2. Create account (free tier available)
3. Upload your `.tex` files
4. Compile in browser

**Advantages:**
- ✅ No installation required
- ✅ Collaboration features
- ✅ Works on any device

**Disadvantages:**
- ⚠️ Requires internet
- ⚠️ Free tier has limitations
- ⚠️ Need to upload Pictures/ directory

---

### Option 4: Vim/Emacs (For Power Users)

**Best for:** Terminal-based workflow

**Vim:**
```bash
brew install vim
vim rowoperation.tex

# Install vimtex plugin for LaTeX support
```

**Emacs:**
```bash
brew install emacs
emacs rowoperation.tex

# Install AUCTeX for LaTeX support
```

---

## Advanced: Makefile for Batch Compilation

Create a `Makefile` in the repository root:

```makefile
# Makefile for Linear Algebra Slides

.PHONY: all clean

# Compile all .tex files (excluding backups)
all:
	@for file in *.tex; do \
		if [ "$$file" != "main.tex" ] && [ "$$file" != "*-old-dsl.tex" ]; then \
			echo "Compiling $$file..."; \
			pdflatex -interaction=nonstopmode "$$file" > /dev/null; \
		fi \
	done
	@echo "All slides compiled!"

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Compile specific file
%.pdf: %.tex
	pdflatex -interaction=nonstopmode $<
```

**Usage:**

```bash
# Compile all slides
make all

# Compile specific slide
make rowoperation.pdf

# Clean auxiliary files
make clean
```

---

## Continuous Compilation (Auto-Rebuild on Save)

### Using latexmk

```bash
# Install latexmk (if not included)
sudo tlmgr install latexmk

# Watch and auto-compile
latexmk -pvc -pdf rowoperation.tex
```

This will:
- ✅ Watch the `.tex` file for changes
- ✅ Auto-recompile when you save
- ✅ Keep the PDF viewer updated

**Stop with:** `Ctrl+C`

---

## Package Management Cheat Sheet

```bash
# Update tlmgr itself
sudo tlmgr update --self

# Update all installed packages
sudo tlmgr update --all

# Search for a package
tlmgr search --global packagename

# Install a package
sudo tlmgr install packagename

# Remove a package
sudo tlmgr remove packagename

# List installed packages
tlmgr list --only-installed

# Show package info
tlmgr info packagename
```

---

## Performance Tips

### Speed Up Compilation

1. **Use `-interaction=nonstopmode`** to skip error prompts:
   ```bash
   pdflatex -interaction=nonstopmode rowoperation.tex
   ```

2. **Use `-halt-on-error`** to stop immediately on errors:
   ```bash
   pdflatex -halt-on-error rowoperation.tex
   ```

3. **Use `-output-directory`** to keep directory clean:
   ```bash
   pdflatex -output-directory=build rowoperation.tex
   ```

### Reduce Disk Usage

```bash
# Clean LaTeX auxiliary files
rm *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Or use latexmk
latexmk -c  # Clean auxiliary files
latexmk -C  # Clean all generated files including PDF
```

---

## FAQ

### Q: Should I use BasicTeX or MacTeX?

**A:** Use **BasicTeX** if:
- You only need LaTeX for this project
- You want a small installation (~100MB)
- You're comfortable with command-line package management

Use **MacTeX** if:
- You use LaTeX for multiple projects
- You want a GUI editor (TeXShop)
- You prefer "batteries included" setup
- Disk space isn't a concern (4.5GB)

---

### Q: Can I use XeLaTeX or LuaLaTeX instead of pdflatex?

**A:** Yes! The slides compile with any LaTeX engine:

```bash
xelatex rowoperation.tex   # Better Unicode support
lualatex rowoperation.tex  # Lua scripting support
```

XeLaTeX is recommended for Metropolis theme (better font rendering).

---

### Q: Do I need to install all packages at once?

**A:** No. You can install packages on-demand when you get "xyz.sty not found" errors:

```bash
sudo tlmgr install xyz
```

This is the recommended approach for BasicTeX.

---

### Q: How do I uninstall BasicTeX or MacTeX?

**BasicTeX (via Homebrew):**
```bash
brew uninstall basictex
```

**MacTeX or BasicTeX (manual):**
```bash
sudo rm -rf /usr/local/texlive/
sudo rm -rf /Library/TeX/
```

---

### Q: Can I have both BasicTeX and MacTeX installed?

**A:** Not recommended. They conflict. Uninstall one before installing the other.

---

### Q: Where are packages installed?

**BasicTeX/MacTeX location:**
```
/usr/local/texlive/2024/texmf-dist/
```

**Your custom packages go in:**
```
~/Library/texmf/
```

---

## Summary: Quick Setup Checklist

- [ ] Install BasicTeX via Homebrew: `brew install basictex`
- [ ] Configure PATH: `echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.zshrc`
- [ ] Restart terminal
- [ ] Verify: `pdflatex --version`
- [ ] Update tlmgr: `sudo tlmgr update --self`
- [ ] Install packages: `sudo tlmgr install beamer metropolis pgfopts tcolorbox tikz ...`
- [ ] Navigate to repo: `cd ~/path/to/Linear-Algebra-Slides`
- [ ] Compile: `pdflatex rowoperation.tex`
- [ ] View PDF: `open rowoperation.pdf`

---

## Related Documents

- **LaTeX-installation-minimal.md** - Cross-platform minimal installation guide
- **ADR-0001** - Migration from custom DSL to standalone standard LaTeX
- **DR-0001** - rowoperation.tex migration design rationale

---

**Last Updated:** 2026-02-24
**Maintainer:** Engineer team
**Feedback:** Report issues or improvements via GitHub issues
