import flet as ft

def main(page: ft.Page):
    page.title = "Edital Polícia Legislativa"
    page.theme_mode = ft.ThemeMode.LIGHT 
    page.padding = 20 # Aumentei um pouco o espaço nas bordas
    
    # --- DADOS DO EDITAL (Seu conteúdo) ---
    dados_iniciais = [
        # LÍNGUA PORTUGUESA
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "1. Interpretação e tipologia textual"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "2. Processos de construção textual"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "3. A progressão textual"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "4. Coesão, coerência e intertextualidade"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "5. Reescritura de frases"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "6. Domínio vocabular"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "7. Estrangeirismos"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "8. Classes de palavras"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "9. Sintaxe e pontuação"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "10. Variação linguística"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "11. Linguagem denotativa e conotativa"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "12. Nova ortografia"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "13. Acentuação e crase"},
        
        # ... (Mantendo a lógica de todos os outros tópicos aqui)
        # Para economizar espaço na mensagem, o código assume que você
        # manterá a lista completa que já tem. Se precisar dela inteira de novo, avise!
        {"Disciplina": "RACIOCÍNIO LÓGICO", "Tópico": "1. Proposições e conectivos"},
        # ... adicione o resto da sua lista aqui se copiar de novo ...
    ]
    
    # Se você for copiar APENAS este código, certifique-se de que a lista 'dados_iniciais'
    # tenha todos os itens do edital que fizemos antes! 
    # Vou recolocar a lista COMPLETA abaixo para garantir que não falte nada:
    
    dados_iniciais = [
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "1. Interpretação e tipologia textual"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "2. Processos de construção textual"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "3. A progressão textual"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "4. Coesão, coerência e intertextualidade"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "5. Reescritura de frases"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "6. Domínio vocabular"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "7. Estrangeirismos"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "8. Classes de palavras"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "9. Sintaxe e pontuação"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "10. Variação linguística"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "11. Linguagem denotativa e conotativa"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "12. Nova ortografia"},
        {"Disciplina": "LÍNGUA PORTUGUESA", "Tópico": "13. Acentuação e crase"},
        {"Disciplina": "RACIOCÍNIO LÓGICO", "Tópico": "1. Proposições lógicas e conectivos"},
        {"Disciplina": "RACIOCÍNIO LÓGICO", "Tópico": "2. Equivalências lógicas"},
        {"Disciplina": "RACIOCÍNIO LÓGICO", "Tópico": "3. Problemas de raciocínio"},
        {"Disciplina": "RACIOCÍNIO LÓGICO", "Tópico": "4. Diagramas lógicos e tabelas"},
        {"Disciplina": "RACIOCÍNIO LÓGICO", "Tópico": "5. Sequências e padrões"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "1. Formação territorial e ouro"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "2. Goiás no Império"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "3. Primeira República (1889-1930)"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "4. Mudança da capital (Goiânia)"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "5. Goiás contemporâneo"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "6. Aspectos físicos e Cerrado"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "7. População e urbanização"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "8. Economia (Agro/Indústria)"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "9. Organização político-administrativa"},
        {"Disciplina": "REALIDADE DE GOIÁS", "Tópico": "10. Questões contemporâneas"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "1. Arquivos digitais"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "2. PDF"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "3. Windows 10 e superior"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "4. Word (Editores de texto)"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "5. Manipulação de arquivos"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "6. Excel (Planilhas)"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "7. Internet e Segurança"},
        {"Disciplina": "INFORMÁTICA", "Tópico": "8. Transferência de arquivos"},
        {"Disciplina": "LEGISLAÇÃO", "Tópico": "1. Resolução 1.073/2001 (Alego)"},
        {"Disciplina": "LEGISLAÇÃO", "Tópico": "2. Resolução 1.771/2023"},
        {"Disciplina": "LEGISLAÇÃO", "Tópico": "3. Lei 13.675/2018 (SUSP)"},
        {"Disciplina": "CONSTITUCIONAL", "Tópico": "1. Conceito e princípios"},
        {"Disciplina": "CONSTITUCIONAL", "Tópico": "2. Direitos fundamentais"},
        {"Disciplina": "CONSTITUCIONAL", "Tópico": "3. Organização político-administrativa"},
        {"Disciplina": "CONSTITUCIONAL", "Tópico": "4. Administração pública"},
        {"Disciplina": "CONSTITUCIONAL", "Tópico": "5. Organização dos Poderes"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "1. Organização administrativa"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "2. Desconcentração"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "3. Órgãos públicos"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "4. Agentes públicos"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "5. Poderes administrativos"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "6. Ato adm, Licitação e Contratos"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "7. Lei 14.133/2021"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "8. Improbidade Adm (Lei 8.429)"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "9. Acesso à Informação (Lei 12.527)"},
        {"Disciplina": "ADMINISTRATIVO", "Tópico": "10. LGPD (Lei 13.709)"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "1. Relações Humanas e Atendimento"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "2. Trabalho em equipe"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "3. Noções de Defesa Pessoal"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "4. Análise de Riscos e Emergência"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "5. Gerenciamento de crises"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "6. Segurança da Informação"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "7. Proteção e Escoltas"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "8. Condução de veículos"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "9. Segurança Física e Instalações"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "10. Controle de acessos"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "11. Vigilância e Monitoramento"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "12. Incidentes Críticos e Negociação"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "13. Prevenção e Combate a Incêndio"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "14. Condutas do Socorrista (APH)"},
        {"Disciplina": "ATUAÇÃO", "Tópico": "15. Serviços de Inteligência"},
    ]

    # --- LÓGICA DO APP ---
    barra_progresso = ft.ProgressBar(width=400, color="blue", bgcolor="#eeeeee", value=0)
    texto_porcentagem = ft.Text("0% Concluído", size=16, weight="bold")
    todas_caixas = []

    def atualizar_progresso():
        total = len(todas_caixas)
        marcados = 0
        for caixa in todas_caixas:
            if caixa.value == True:
                marcados += 1
        
        if total > 0:
            porcentagem = marcados / total
        else:
            porcentagem = 0
            
        barra_progresso.value = porcentagem
        texto_porcentagem.value = f"{int(porcentagem * 100)}% Concluído"
        
        if porcentagem < 0.3:
            barra_progresso.color = "red"
        elif porcentagem < 0.7:
            barra_progresso.color = "orange"
        else:
            barra_progresso.color = "green"
        page.update()

    def salvar_checkbox(e):
        page.client_storage.set(e.control.label, e.control.value)
        atualizar_progresso()

    nomes_disciplinas = []
    for d in dados_iniciais:
        if d["Disciplina"] not in nomes_disciplinas:
            nomes_disciplinas.append(d["Disciplina"])

    minhas_abas_lista = []

    for disciplina in nomes_disciplinas:
        topicos = [d["Tópico"] for d in dados_iniciais if d["Disciplina"] == disciplina]
        coluna_conteudo = ft.Column(scroll="adaptive")
        
        for t in topicos:
            estava_marcado = page.client_storage.get(t) or False
            check = ft.Checkbox(label=t, value=estava_marcado, on_change=salvar_checkbox)
            coluna_conteudo.controls.append(check)
            todas_caixas.append(check)

        coluna_conteudo.controls.append(ft.Container(height=80))

        icone = "book"
        if "INFORMÁTICA" in disciplina: icone = "computer"
        if "GOIÁS" in disciplina: icone = "map"
        if "DIREITO" in disciplina or "CONSTITUCIONAL" in disciplina: icone = "gavel"
        if "ATUAÇÃO" in disciplina: icone = "security"
        
        aba = ft.Tab(text=disciplina, icon=icone, content=coluna_conteudo)
        minhas_abas_lista.append(aba)

    # --- CONFIGURAÇÃO DA LOGO ---
    # Aqui definimos a imagem. Ela precisa se chamar 'logo.png'
    logo_app = ft.Image(
        src="logo.png",
        width=100,  # Tamanho da logo
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    titulo = ft.Text("Polícia Legislativa", size=24, weight="bold", color="blue")
    
    # Cabeçalho Centralizado
    painel_progresso = ft.Container(
        content=ft.Column([
            ft.Container(height=10), # Espacinho no topo
            ft.Row([logo_app], alignment=ft.MainAxisAlignment.CENTER), # Logo centralizada
            ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),   # Título centralizado
            ft.Container(height=10),
            ft.Row([texto_porcentagem]),
            barra_progresso,
            ft.Divider()
        ]),
        padding=5
    )

    tabs_control = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=minhas_abas_lista,
        scrollable=True,
        expand=1
    )

    page.add(painel_progresso, tabs_control)
    atualizar_progresso()

ft.app(target=main, assets_dir="assets")