# /// script
# dependencies = [
#     "marimo",
#     "mcp>=1",
#     "pydantic>=2",
#     "vegafusion==2.0.3",
#     "vl-convert-python==1.9.0.post1",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(
    width="medium",
    layout_file="layouts/notebook.slides.json",
    css_file="custom.css",
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Pitacos
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import os

    return mo, os


@app.cell(hide_code=True)
def _(mo):
    def create_parents_letter_accordion():
        accordion = mo.accordion(
            {
                "Pitacos e Uma Carta Para Isis": f"""
                <div style="background-color: #e3f2fd; border-radius: 8px; padding: 25px; border: 1px solid #bbdefb; 
                      font-family: 'Georgia', serif; position: relative;
                      margin: 10px 0;">

                    <p style="line-height: 1.6; font-size: 1.05em;">
                        Isis,
                        <br/><br/>
                        Queria dizer o quanto eu aprecio seu amor e generosidade.
                        Como a minha maior habilidade é fazer a cabeça pra funcionar para achar as coisas, resolvi que o melhor seria escrever uma série de pitacos, que parecem ser sólidos.
                        <br/><br/>
                        Obviamente que estou sendo como um padre dando pitaco em casamento, mas foi a forma que encontrei de te agradecer pelo tanto que você se preocupou e está tentando.
                        <br/><br/>
                        Do padrinho que te ama,<br/>
                        Arthur
                    </p>

                    <div style="text-align: right; margin-top: 10px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" 
                                  fill="#1976d2" opacity="0.8"/>
                        </svg>
                    </div>
                </div>
                """
            },
        )
        return accordion


    parents_letter_accordion = create_parents_letter_accordion()
    return (parents_letter_accordion,)


@app.cell(hide_code=True)
def _(parents_letter_accordion):
    parents_letter_accordion
    return


@app.cell(hide_code=True)
def _(os):
    advice_emojis = ["⭐", "🧸", "🎈", "🖍️", "💡"]

    advice_styles = [
        {"border": "#4285f4", "bg": "#e8f0fe"},
        {"border": "#34a853", "bg": "#e6f4ea"},
        {"border": "#fbbc05", "bg": "#fff8e1"},
        {"border": "#ea4335", "bg": "#fce8e6"},
        {"border": "#9c27b0", "bg": "#f3e5f5"},
    ]

    parenting_advice = {
        0: [
            {
                "t": "**Chinelada parece mesmo que não funciona.**",
                "p": "Uma das maiores meta-análises já feitas mostrou que palmada se associa a mais agressividade, mais problemas de comportamento e uma relação pior com os pais. Meio que a casa que bate ensina que bater resolve.",
                "s": "[Gershoff & Grogan-Kaylor (2016), Journal of Family Psychology](https://pmc.ncbi.nlm.nih.gov/articles/PMC7992110/)",
            },
            {
                "t": "**Comer juntos em família é importante demais.**",
                "p": "Comer junto três vezes ou mais por semana se associa a hábitos alimentares melhores, peso mais saudável e um espaço previsível de convivência sem disputa.",
                "s": "[Hammons & Fiese (2011), Pediatrics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3387875/)",
            },
            {
                "t": "**'É coisa de irmão' pode esconder bullying sério.**",
                "p": "Em um grande estudo longitudinal, bullying frequente entre irmãos quase dobrou o risco de depressão aos 18 anos.",
                "s": "[Bowes et al. (2014), Pediatrics](https://publications.aap.org/pediatrics/article-abstract/134/4/e1032/32993/Sibling-Bullying-and-Risk-of-Depression-Anxiety)",
            },
            {
                "t": "**Fique de olho se alguém ficar mais agressivo.**",
                "p": "Crianças agredidas ao mesmo tempo por irmãos e colegas apresentaram os maiores riscos de depressão.",
                "s": "[Dantchev et al. (2019), Frontiers in Psychiatry](https://doi.org/10.3389/fpsyt.2019.00651)",
            },
        ],
        1: [
            {
                "t": "**Na briga, seja mediador — não juiz.**",
                "p": "Pais treinados para mediar conflitos tiveram filhos que negociavam melhor e chegavam mais a acordos.",
                "s": "[Smith & Ross (2007), Child Development](https://pubmed.ncbi.nlm.nih.gov/17517005/)",
            },
            {
                "t": "**Não entregue a solução pronta. Pergunte qual é o plano deles.**",
                "p": "Quando as próprias crianças participam da solução do conflito, elas negociam mais e brigam menos.",
                "s": "[Ross & Lazinski (2014), Early Education and Development](https://www.tandfonline.com/doi/full/10.1080/10409289.2013.788425)",
            },
            {
                "t": "**Esqueça quem começou. Foque em como termina.**",
                "p": "Direcionar a conversa para soluções concretas favorece acordos e reduz acusações.",
                "s": "[Ross & Lazinski (2014), Early Education and Development](https://www.tandfonline.com/doi/full/10.1080/10409289.2013.788425)",
            },
            {
                "t": "**Ensine a criança a 'dar uma respirada' antes de reagir.**",
                "p": "Treinos de regulação emocional melhoraram a qualidade da relação entre irmãos.",
                "s": "[Kennedy & Kramer (2008), Family Relations](https://experts.illinois.edu/en/publications/improving-emotion-regulation-and-sibling-relationship-quality-the/)",
            },
        ],
        2: [
            {
                "t": "**Seus filhos copiam como VOCÊ lida com o mundo.**",
                "p": "Crianças aprendem regulação emocional observando como os pais lidam com emoções difíceis.",
                "s": "[Ravindran et al. (2015), Journal of Family Psychology](https://pubmed.ncbi.nlm.nih.gov/26053350/)",
            },
            {
                "t": "**Cuidado com a percepção de injustiça.**",
                "p": "O filho que percebe receber tratamento menos favorável tende a apresentar mais ansiedade e problemas de comportamento.",
                "s": "[Jensen & Thomsen (2024), Child Development](https://pubmed.ncbi.nlm.nih.gov/38439142/)",
            },
            {
                "t": "**Cuidado em não ter um favoritismo invisível.**",
                "p": "Meta-análises recentes encontraram tendências consistentes de favoritismo às filhas e aos filhos mais velhos.",
                "s": "[Jensen & Jorgensen-Wells (2025), Psychological Bulletin](https://pubmed.ncbi.nlm.nih.gov/39818912/)",
            },
            {
                "t": "**Mais hostilidade pesa mais do que menos carinho.**",
                "p": "Perder a paciência sistematicamente mais com um filho do que com outro cobra um preço emocional alto.",
                "s": "[Eradus et al. (2024), Journal of Family Psychology](https://pubmed.ncbi.nlm.nih.gov/38271066/)",
            },
        ],
        3: [
            {
                "t": "**'Por que você não é como sua irmã?' Sério, nunca.**",
                "p": "Comparações constantes alimentam sensação de injustiça e rivalidade.",
                "s": "[Padilla et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5110249/)",
            },
            {
                "t": "**Se precisar tratar diferente, explique o motivo.**",
                "p": "Crianças lidam melhor com diferenças quando entendem claramente as razões por trás delas.",
                "s": "[Padilla et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5110249/)",
            },
            {
                "t": "**Quinze minutos a sós com cada filho valem ouro.**",
                "p": "Tempo individual previsível reduz ciúmes e aumenta proximidade entre irmãos.",
                "s": "[Pike, Coldwell & Dunn (2005)](https://pubmed.ncbi.nlm.nih.gov/?term=Pike+Coldwell+Dunn+sibling+relationships+2005)",
            },
            {
                "t": "**Prefira brincadeiras cooperativas às competitivas.**",
                "p": "Jogos de construir-junto fortalecem comportamento pró-social e reduzem rivalidade.",
                "s": "[Pike, Coldwell & Dunn (2005)](https://pubmed.ncbi.nlm.nih.gov/?term=Pike+Coldwell+Dunn+sibling+relationships+2005)",
            },
        ],
        4: [
            {
                "t": "**Diga em voz alta o nome do que se está sentindo.**",
                "p": "Nomear emoções ajuda crianças a desenvolver empatia ao longo do tempo.",
                "s": "[Jambon et al. (2019), Child Development](https://pubmed.ncbi.nlm.nih.gov/?term=Jambon+empathic+concern+siblings+2019)",
            },
            {
                "t": "**Deixe a mais velha ensinar o mais novo.**",
                "p": "O papel de ensinar fortalece empatia, autoestima e proximidade entre irmãos.",
                "s": "[Jambon et al. (2019), Child Development](https://pubmed.ncbi.nlm.nih.gov/?term=Jambon+empathic+concern+siblings+2019)",
            },
            {
                "t": "**Rotina previsível protege emocionalmente.**",
                "p": "Rituais familiares estáveis funcionam como amortecedores emocionais.",
                "s": "[Fiese et al. (2002)](https://pubmed.ncbi.nlm.nih.gov/?term=Fiese+family+routines+rituals+review+2002)",
            },
            {
                "t": "**Em casa, xingar e bater estão fora de cogitação.**",
                "p": "Normalizar agressão verbal ou física aumenta o risco de agressividade futura.",
                "s": "[Tucker & Finkelhor (2017)](https://pubmed.ncbi.nlm.nih.gov/?term=Tucker+Finkelhor+sibling+conflict+aggression+review+2017)",
            },
        ],
        5: [
            {
                "t": "**Apelido humilhante também é agressão.**",
                "p": "Humilhação, exclusão e agressão verbal entre irmãos se associam a ansiedade e depressão posteriores.",
                "s": "[Tucker & Finkelhor (2017)](https://pubmed.ncbi.nlm.nih.gov/?term=Tucker+Finkelhor+sibling+conflict+aggression+review+2017)",
            },
            {
                "t": "**Esperar 'a fase passar' raramente resolve.**",
                "p": "Os programas com melhor evidência usam mediação estruturada e treino de regulação emocional.",
                "s": "[Tucker & Finkelhor (2017)](https://pubmed.ncbi.nlm.nih.gov/?term=Tucker+Finkelhor+sibling+conflict+aggression+review+2017)",
            },
            {
                "t": "**Irmã não é babá oficial (mais fácil dito que fazer).**",
                "p": "Sobrecarregar o filho mais velho com funções parentais se associa a ansiedade futura.",
                "s": "[Hooper et al. (2011)](https://pubmed.ncbi.nlm.nih.gov/?term=Hooper+Parentification+Inventory+2011)",
            },
            {
                "t": "**Mesmo quando há boa vontade, pode ser que a carga seja demais.**",
                "p": "Ansiedade, queda escolar e sono ruim podem indicar sobrecarga excessiva.",
                "s": "[Roberts & Beaton (2024)](https://pubmed.ncbi.nlm.nih.gov/?term=Roberts+Beaton+parentification+young+caregivers+2024)",
            },
        ],
        6: [
            {
                "t": "**Prepare a primogênita antes do bebê chegar (too late haha).**",
                "p": "A transição para irmã mais velha traz mudanças emocionais importantes.",
                "s": "[Zhang et al. (2023)](https://pubmed.ncbi.nlm.nih.gov/?term=Zhang+firstborn+transition+to+siblinghood+2023)",
            },
            {
                "t": "**A infantilidade repentina são comuns nessa fase.**",
                "p": "Pequenas regressões após o nascimento de um irmão são comuns e fazem parte da adaptação.",
                "s": "[Zhang et al. (2023)](https://pubmed.ncbi.nlm.nih.gov/?term=Zhang+firstborn+transition+to+siblinghood+2023)",
            },
            {
                "t": "**Programas para melhorar relações entre irmãos realmente funcionam.**",
                "p": "Intervenções estruturadas aumentaram proximidade e reduziram negatividade.",
                "s": "[Feinberg et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23000632/)",
            },
            {
                "t": "**Filhos diferentes não são um problema.**",
                "p": "Desenvolver identidades distintas pode reduzir comparação e rivalidade.",
                "s": "[Jensen et al. (2015)](https://pubmed.ncbi.nlm.nih.gov/?term=Jensen+Whiteman+siblings+who+are+different+2015)",
            },
        ],
        7: [
            {
                "t": "**Irmãos que se gostam viram adultos que amam melhor.**",
                "p": "Relações calorosas entre irmãos ajudam a quebrar ciclos de hostilidade.",
                "s": "[Masarik et al.](https://www.depts.ttu.edu/hs/hdfs/research/sibs/docs/Masarik-Rogers-Online2019.pdf)",
            },
            {
                "t": "**Dê aos filhos um roteiro para resolver conflitos sozinhos (processo! haha).**",
                "p": "Estratégias explícitas de negociação reduzem conflitos destrutivos.",
                "s": "[Updegraff et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC2742483/)",
            },
            {
                "t": "**Família unida funciona como fator de proteção real.**",
                "p": "Valores fortes de união familiar ajudam crianças e adolescentes a lidar melhor com estresses externos.",
                "s": "[Revisão sistemática sobre irmãos latinx (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11273421/)",
            },
            {
                "t": "**Uma relação sadia entre irmãos tem efeitos muito além do que você espera.**",
                "p": "Calor emocional entre irmãos protege adolescentes contra impactos de estresses externos.",
                "s": "[Sibling Relationships and Adolescent Adjustment](https://pmc.ncbi.nlm.nih.gov/articles/PMC4600416/)",
            },
        ],
        8: [
            {
                "t": "**'Mais velha responsável' não é regra universal.**",
                "p": "A forma como ordem de nascimento influencia relações entre irmãos varia entre culturas.",
                "s": "[Perceptions of Sibling Relationships and Birth Order (2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6426140/)",
            },
            {
                "t": "**Agressão entre irmãos na infância prevê violência futura.**",
                "p": "Conflitos agressivos persistentes aumentam risco de comportamento antissocial mais tarde.",
                "s": "[Tucker & Finkelhor (2017)](https://pubmed.ncbi.nlm.nih.gov/?term=Tucker+Finkelhor+sibling+conflict+aggression+review+2017)",
            },
            {
                "t": "**Não existe uma única teoria para explicar relações entre irmãos.**",
                "p": "Os melhores modelos combinam apego, aprendizagem social e dinâmica familiar.",
                "s": "[Whiteman, McHale & Soli (2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3127252/)",
            },
            {
                "t": "**Se a mais velha começou a fumar, observe o mais novo.**",
                "p": "Ter um irmão fumante aumentou fortemente a chance de adolescentes também fumarem.",
                "s": "[Abreu, Souza & Caiaffa (2011)](https://www.scielo.br/j/csp/a/WpsWmTFCCNwd8Cgn34xCRbS/?lang=pt)",
            },
        ],
        9: [
            {
                "t": "**Coisa doida: muitas crianças pequenas em casa? Vale checar anemia.**",
                "p": "Morar com várias crianças menores de 5 anos esteve associado a maior prevalência de anemia infantil.",
                "s": "[da Silva, Fawzi & Cardoso (2018)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0204504)",
            },
            {
                "t": "**Primogênitos tendem a se exercitar menos (eu atesto! haha).**",
                "p": "Primogênitos apresentaram níveis mais baixos de atividade física em estudos.",
                "s": "[Wells et al. (2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3658103/)",
            },
            {
                "t": "**Não isole o bebê dos irmãos por medo de alergia.**",
                "p": "Ter mais irmãos esteve associado a menos atopia em estudos brasileiros.",
                "s": "[Figueiredo et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5369757/)",
            },
            {
                "t": "**Quando um filho é internado, o irmão saudável também precisa de atenção.**",
                "p": "Irmãos de crianças hospitalizadas frequentemente relatam medo, tristeza e sensação de exclusão.",
                "s": "[Literatura brasileira de enfermagem pediátrica](https://periodicos.ufpe.br/revistas/revistaenfermagem/article/view/240898)",
            },
            {
                "t": "**O melhor presente para seus filhos é um ao outro.**",
                "p": "A relação entre irmãos tende a ser a mais longa da vida e é construída diariamente.",
                "s": "[Síntese das evidências reunidas](https://pmc.ncbi.nlm.nih.gov/articles/PMC3127252/)",
            },
        ],
    }

    # year_value_map uses the 't' (title) from the first advice of each stage
    year_value_map = {}
    for stage_key, advice_list in parenting_advice.items():
        year_value_map[stage_key] = f"Estágio {stage_key}"

    # Load SVG files from disk
    _svg_file_map = {
        0: "sibling_01_backs_v3.svg",
        1: "sibling_02_tugofwar_v2.svg",
        2: "sibling_03_hairpull.svg",
        3: "sibling_04_tooth.svg",
        4: "sibling_05_timeout.svg",
        5: "sibling_06_peeking.svg",
        6: "sibling_07_peace.svg",
        7: "sibling_08_sharing.svg",
        8: "sibling_09_holdinghands.svg",
        9: "sibling_10_embrace.svg",
    }

    _notebook_dir = os.path.dirname(os.path.abspath(__file__))
    flower_svgs = {}
    for _stage, _filename in _svg_file_map.items():
        _svg_path = os.path.join(_notebook_dir, _filename)
        try:
            with open(_svg_path) as _f:
                flower_svgs[_stage] = _f.read()
        except FileNotFoundError:
            flower_svgs[_stage] = f"<!-- SVG não encontrado: {_filename} -->"
    return advice_emojis, advice_styles, flower_svgs, parenting_advice


@app.cell(hide_code=True)
def _():
    tabs_dict_years = {}
    for i in range(10):
        label = f"Estágio {i}"
        tabs_dict_years[label] = f"{i}"
    return (tabs_dict_years,)


@app.cell(hide_code=True)
def _(mo, tabs_dict_years):
    year_tabs = mo.ui.tabs(tabs_dict_years, label="")
    return (year_tabs,)


@app.cell(hide_code=True)
def _(advice_emojis, advice_styles, mo):
    def create_advice_tabs_dictionary(advice_list):
        _advice_tabs_dict = {}
        if not advice_list:
            _advice_tabs_dict["Info"] = mo.md("Nenhum conselho disponível para este estágio.")
        else:
            for i, advice_item in enumerate(advice_list):
                if i < len(advice_emojis) and i < len(advice_styles):
                    tab_key = advice_emojis[i]
                    current_style = advice_styles[i]
                    _t = advice_item.get("t", "")
                    _p = advice_item.get("p", "")
                    _s = advice_item.get("s", "")

                    _rendered = mo.md(f"""{_t}

    {_p}

    {_s}""")
                    advice_content = mo.Html(
                        f"""<div style="background-color: {current_style["bg"]}; border-radius: 4px; padding: 10px 12px; border-left: 3px solid {current_style["border"]};">{_rendered}</div>"""
                    )
                    _advice_tabs_dict[tab_key] = advice_content
                else:
                    tab_key = f"Dica {i + 1}"
                    _t = advice_item.get("t", "") if isinstance(advice_item, dict) else str(advice_item)
                    _p = advice_item.get("p", "") if isinstance(advice_item, dict) else ""
                    _s = advice_item.get("s", "") if isinstance(advice_item, dict) else ""
                    advice_content = mo.md(f"""{_t}

    {_p}

    {_s}""")
                    _advice_tabs_dict[tab_key] = advice_content

        return _advice_tabs_dict

    return (create_advice_tabs_dictionary,)


@app.cell(hide_code=True)
def _(year_tabs):
    selected_year = int(str(year_tabs.value).split()[-1])
    return (selected_year,)


@app.cell(hide_code=True)
def _(flower_svgs, mo, selected_year):
    svg_display = mo.Html(f"""
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 8px;
        margin: 4px 0;
        max-height: 40vh;
        overflow: hidden;
        background-color: #fafafa;
        border-radius: 8px;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #eee;
    ">
        <style>.svg-container svg {{ max-height: 36vh; width: auto; height: auto; }}</style>
        <div class="svg-container">{flower_svgs.get(selected_year, "<!-- SVG não encontrado -->")}</div>
    </div>
    """)
    return (svg_display,)


@app.cell(hide_code=True)
def _(parenting_advice, selected_year):
    advice_list_for_year = parenting_advice.get(selected_year, [])
    return (advice_list_for_year,)


@app.cell(hide_code=True)
def _(advice_list_for_year, create_advice_tabs_dictionary):
    advice_tabs_dict = create_advice_tabs_dictionary(advice_list_for_year)
    return


@app.cell(hide_code=True)
def _(mo, year_tabs):
    show_years = mo.Html(f"""
    <div style="
        display: flex;
        justify-content: center;
        padding: 6px 8px;
        margin: 2px 0;
    ">
        {year_tabs}
    </div>
    """)
    return (show_years,)


@app.cell(hide_code=True)
def _(advice_emojis, advice_list_for_year, advice_styles, mo):
    default_advice_tab = advice_emojis[0] if advice_list_for_year else "Info"
    individual_advice_tabs_dict = {}
    if not advice_list_for_year:
        individual_advice_tabs_dict["Info"] = mo.md("Nenhum conselho disponível para este estágio.")
    else:
        for ii, advice_item in enumerate(advice_list_for_year):
            if ii < len(advice_emojis) and ii < len(advice_styles):
                tab_key = advice_emojis[ii]
            else:
                tab_key = f"Dica {ii + 1}"

            _t = advice_item.get("t", "") if isinstance(advice_item, dict) else str(advice_item)
            _p = advice_item.get("p", "") if isinstance(advice_item, dict) else ""
            _s = advice_item.get("s", "") if isinstance(advice_item, dict) else ""

            individual_advice_tabs_dict[tab_key] = mo.md(f"""{_t}

    {_p}

    {_s}""")

    individual_advice_tabs = mo.ui.tabs(individual_advice_tabs_dict, value=default_advice_tab)
    return (individual_advice_tabs,)


@app.cell(hide_code=True)
def _(individual_advice_tabs, mo, show_years, svg_display):
    mo.vstack(
        [
            mo.Html("""
    <div style="text-align: center; font-family: Garamond, serif; font-weight: bold; font-size: 1.4em; margin: 0; padding: 0;">
    Carta para Isis
    </div>
    """),
            show_years,
            svg_display,
            mo.md("---"),
            individual_advice_tabs,
        ]
    )
    return


if __name__ == "__main__":
    app.run()
