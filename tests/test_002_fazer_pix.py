
def test_002_fazer_pix(common_page, login_page, home_page, pix_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("12345678900", "10.00")
    pix_page.assert_pix_realizado()
    common_page.voltar_para_home()
    common_page.assert_text("4.990,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Pix para 12345678900 - R$ -10,00")


    
