;; flycheckify.el: Flycheck configuration example
(require 'flycheck)
(flycheck-define-checker text-redpen
  "Check text with RedPen"
  :command ("/path/to/pyredpen/bin/redpen-flymake" "-p" source)
  :error-patterns ((error line-start (file-name) ":" line ":" column ": "
			  "error: " (message) line-end)
		   (warning line-start (file-name) ":" line ":" column ": "
			    "warning: " (message) line-end))
  :modes text-mode)
(flycheck-define-checker markdown-redpen
  "Check markdown text with RedPen"
  :command ("/path/to/pyredpen/bin/redpen-flymake" "-m" source)
  :error-patterns ((error line-start (file-name) ":" line ":" column ": "
			  "error: " (message) line-end)
		   (warning line-start (file-name) ":" line ":" column ": "
			    "warning: " (message) line-end))
  :modes markdown-mode)
(add-to-list 'flycheck-checkers 'text-redpen)
(add-to-list 'flycheck-checkers 'markdown-redpen)
