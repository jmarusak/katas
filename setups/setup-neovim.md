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

### Python plugin
```
npm install -g pyright
```
```
git clone https://github.com/neovim/nvim-lspconfig ~/.config/nvim/pack/nvim/start/nvim-lspconfig
```
```
# init.vim
lua << EOF
require'lspconfig'.pyright.setup{}
EOF
```
- Ctrl + n: Show the autocomplete menu.
- Ctrl + p: Navigate backward in the suggestions.
- Ctrl + x + o: Trigger omnifunction completion (useful for LSP).
- Ctrl + x + f: File path completion.
- Ctrl + x + l: Whole-line completion.

- K: Documentation popup on hover()
- Ctrl + k: Signature/parameters inside function

### Java plugin

Eclipse JDT Language Server
```
wget https://www.eclipse.org/downloads/download.php?file=/jdtls/snapshots/jdt-language-server-latest.tar.gz
tar -xvzf jdt-language-server-latest.tar.gz -C ~/.local/share/jdt-language-server
```
init.vim
```
lua << EOF
require'lspconfig'.pyright.setup{}

local lspconfig = require('lspconfig')
local home = os.getenv("HOME")
local workspace_dir = home .. "/tmp/workspace/jdtls/" .. vim.fn.fnamemodify(vim.fn.getcwd(), ":p:h:t")
local config = {
  cmd = {
    'java',
    '-Declipse.application=org.eclipse.jdt.ls.core.id1',
    '-Dosgi.bundles.defaultStartLevel=4',
    '-Declipse.product=org.eclipse.jdt.ls.core.product',
    '-Dlog.level=ALL',
    '-noverify',
    '-Xmx1G',
    '-jar', home .. '/.local/share/jdt-language-server/plugins/org.eclipse.equinox.launcher_1.7.0.v20250404-1055.jar',
    '-configuration', home .. '/.local/share/jdt-language-server/config_linux',
    '-data', workspace_dir
  },
  root_dir = lspconfig.util.root_pattern('.git', 'mvnw', 'gradlew', 'build.gradle', 'pom.xml'),
}
lspconfig.jdtls.setup(config)
EOF

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

