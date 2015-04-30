;; flymakeify.el: Flymake configuration example
(setq pyredpen-bindir "/path/to/pyredpen/bin/")

(require 'flymake)
(defun redpen-flymake-init-plain ()
  (flymake-simple-make-init-impl
   'flymake-create-temp-with-folder-structure nil nil
   buffer-file-name
   (lambda (source base-dir)
     (list (concat pyredpen-bindir "/redpen-flymake") (list "-p" source)))))

(defun redpen-flymake-init-markdown ()
  (flymake-simple-make-init-impl
   'flymake-create-temp-with-folder-structure nil nil
   buffer-file-name
   (lambda (source base-dir)
     (list (concat pyredpen-bindir "/redpen-flymake") (list "-m" source)))))

(setq flymake-allowed-file-name-masks
      (cons '(".+\\.txt$"
	      redpen-flymake-init-plain
	      flymake-simple-cleanup
	      flymake-get-real-file-name)
	    flymake-allowed-file-name-masks))
(setq flymake-allowed-file-name-masks
      (cons '(".+\\.md$"
	      redpen-flymake-init-markdown
	      flymake-simple-cleanup
	      flymake-get-real-file-name)
	    flymake-allowed-file-name-masks))
