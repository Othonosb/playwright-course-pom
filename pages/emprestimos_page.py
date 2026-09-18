from playwright.sync_api import Page, expect

class EmprestimosPage:
    def __init__(self, page: Page):
        self.page = page
        self.contratar_emprestimo_button = self.page.get_by_role("button", name="Contratar Empréstimo")

    def selecionar_emprestimo(self, valor):
        self.page.get_by_role("radio", name=valor).click()

    def contratar_emprestimo(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.contratar_emprestimo_button.click()