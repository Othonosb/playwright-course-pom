def test_003_emprestimos(common_page, login_page, home_page, emprestimos_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Empréstimo")
    emprestimos_page.selecionar_emprestimo("R$ 7.000,00")
    emprestimos_page.contratar_emprestimo()
    common_page.assert_text("Transação Realizada com")
    common_page.voltar_para_home()
    common_page.assert_text("12.000,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Empréstimo contratado")






    
   
    

