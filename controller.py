import view
import process
import log

def button_click():
    rezhim = view.inp_mod()
    if rezhim.lower() == 'импорт':
        surname = view.inp_import()
        result = process.search(surname)
        if isinstance(result, str):
            view.view_import_no()
        else:
            view.view_import(result)
    elif rezhim.lower() == 'экспорт':
        result = view.inp_export()
        process.export(result)
    log.log_cash(rezhim, result)
