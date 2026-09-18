from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.chave_pix_input = self.page.get_by_role("textbox", name="Chave Pix:")
        self.valor_input = self.page.get_by_role("textbox", name="Valor:")
        self.enviar_pix_button = self.page.get_by_role("button", name="Enviar Pix")

    def fazer_pix(self, chave_pix, valor):
        self.chave_pix_input.fill(chave_pix)
        self.valor_input.fill(valor)
        self.enviar_pix_button.click()

    def assert_pix_realizado(self):
        expect(self.page.get_by_role("heading", name="Transação Realizada com Sucesso!")).to_be_visible()
        expect(self.page.get_by_text("A transação foi concluída com")).to_be_visible()

    
        
