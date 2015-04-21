(require 'flymake)

(defun redpen-flymake-init ()
  (flymake-simple-make-init-impl
   'flymake-create-temp-with-folder-structure nil nil
   buffer-file-name
   (lambda (source base-dir)
     (let ((redpen-dir "/path/to/redpen"))
	  `("make" ("-sf" ,(concat redpen-dir "/flymake.mk") ,(concat "redpendir=" redpen-dir) ,(concat "CHK_SOURCES=" source) "check-syntax"))))))

(setq flymake-allowed-file-name-masks
      (cons '(".+\\.txt$"
              redpen-flymake-init
              flymake-simple-cleanup
              flymake-get-real-file-name)
            flymake-allowed-file-name-masks))
