## Neovim

```
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
tar -xvf nvim-linux64.tar.gz
sudo mv nvim-linux64/ /opt/nvim/
```

### neovim .profile
```
export PATH=$PATH:/opt/nvim/bin
```

### Neovim Telescope plugin (dependency)
```
git clone https://github.com/nvim-lua/plenary.nvim.git \
  ~/.config/nvim/pack/github/start/plenary.vim
```

### ripgrep tool for live_grep
```
sudo apt install ripgrep
```

### telescope
```
git clone https://github.com/nvim-telescope/telescope.nvim.git \
  ~/.config/nvim/pack/github/start/telescope.vim
```

### Neovim vim-go plugin LSP (dependency)
```
go install golang.org/x/tools/gopls@latest
export PATH=$PATH:$HOME/go/bin
```

### Go plugin
```
git clone https://github.com/fatih/vim-go.git \
  ~/.config/nvim/pack/github/start/vim-go
```

### Copilot plugin
```
https://github.com/github/copilot.vim.git
```

### Java syntac highlighting
```
vi /opt/nvim-linux64/share/nvim/runtime/syntax/java.vim
```

```
# changes to JavaStatement

-syn keyword javaType		boolean char byte short int long float double
-syn keyword javaType		void
+syn keyword javaStatement	boolean char byte short int long float double
+syn keyword javaStatement	void
 syn keyword javaStatement	return
-syn keyword javaStorageClass	static synchronized transient volatile strictfp serializable
+syn keyword javaStatement	static synchronized transient volatile strictfp serializable
 syn keyword javaExceptions	throw try catch finally
 syn keyword javaAssert		assert
-syn keyword javaMethodDecl	throws
+syn keyword javaStatement	throws
 " Differentiate a "MyClass.class" literal from the keyword "class".
-syn match   javaTypedef		"\.\s*\<class\>"ms=s+1
+syn match   javaStatement	"\.\s*\<class\>"ms=s+1
 syn keyword javaClassDecl	enum extends implements interface
 syn match   javaClassDecl	"\<permits\>\%(\s*(\)\@!"
 syn match   javaClassDecl	"\<record\>\%(\s*(\)\@!"
-syn match   javaClassDecl	"^class\>"
-syn match   javaClassDecl	"[^.]\s*\<class\>"ms=s+1
+syn match   javaStatement	"^class\>"
+syn match   javaStatement	"[^.]\s*\<class\>"ms=s+1
 syn match   javaAnnotation	"@\%(\K\k*\.\)*\K\k*\>"
 syn match   javaClassDecl	"@interface\>"
 syn keyword javaBranch		break continue nextgroup=javaUserLabelRef skipwhite
 syn match   javaUserLabelRef	"\k\+" contained
 syn match   javaVarArg		"\.\.\."
-syn keyword javaScopeDecl	public protected private
+syn keyword javaConceptKind	public protected private
 syn keyword javaConceptKind	abstract final
 syn match   javaConceptKind	"\<non-sealed\>"
 syn match   javaConceptKind	"\<sealed\>\%(\s*(\)\@!"

```

