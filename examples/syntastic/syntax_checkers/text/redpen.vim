" RedPen 
if exists('g:loaded_syntastic_text_redpen_checker')
  finish
endif
let g:loaded_syntastic_text_redpen_checker = 1

let s:save_cpo = &cpo
set cpo&vim

function! SyntaxCheckers_text_redpen_IsAvailable() dict
    return executable(self.getExec())
endfunction

function! SyntaxCheckers_text_redpen_GetLocList() dict
    let makeprg = self.makeprgBuild({
                \ 'args': ''})

    let errorformat =
        \ '%E%f:%l:%c: fatal error: %m,' .
        \ '%E%f:%l:%c: error: %m,' .
        \ '%W%f:%l:%c: warning: %m,' .
        \ '%E%m'

    return SyntasticMake({
        \ 'makeprg': makeprg,
        \ 'errorformat': errorformat,
        \ 'defaults': {'bufnr': bufnr('')},
        \ 'returns': [0, 1] })
endfunction

call g:SyntasticRegistry.CreateAndRegisterChecker({
    \ 'filetype': 'text',
    \ 'name': 'redpen',
    \ 'exec': 'redpen-sublimelinter' })

let &cpo = s:save_cpo
unlet s:save_cpo

" vim: set sw=4 sts=4 et fdm=marker:
