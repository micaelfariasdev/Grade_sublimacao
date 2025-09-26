from PIL import Image, ImageDraw, ImageFont
import cairosvg
import os
DPI_FINAL = 100


def create_tam_frente(path):
    im = Image.open(path)

    # DPI desejado para a saída impressa (e para os cálculos)

    # Parâmetros de corte (em cm)
    corte_lateral_cm = 2
    corte_baixo_cm = 1

    # Conversão de CM para Pixels (usando o DPI final)
    # 1 polegada = 2.54 cm
    corte_lateral_px = int(corte_lateral_cm * DPI_FINAL / 2.54)
    corte_baixo_px = int(corte_baixo_cm * DPI_FINAL / 2.54)

    largura_original, altura_original = im.size

    # 2. Realizando o Corte Inicial
    # -----------------------------
    # Definindo a área de corte: remover corte_lateral_px de cada lado e corte_baixo_px do fundo.
    left = corte_lateral_px
    upper = 0
    right = largura_original - corte_lateral_px
    lower = altura_original - corte_baixo_px

    im_cortada = im.crop((left, upper, right, lower))

    # 3. Definição dos Tamanhos Finais (em cm)
    # ----------------------------------------
    tamanhos_cm = {
        "P": {"a": 70, "l": 53},
        "M": {"a": 73, "l": 57},
        "G": {"a": 75, "l": 60}
    }

    # 4. Processamento e Salvamento para cada Tamanho
    # -----------------------------------------------
    print("--- Gerando Frentes P, M e G ---")

    for nome, dimensoes in tamanhos_cm.items():
        altura_cm = dimensoes["a"]
        largura_cm = dimensoes["l"]

        nova_largura_px = int(largura_cm * DPI_FINAL / 2.54)
        nova_altura_px = int(altura_cm * DPI_FINAL / 2.54)

        im_final = im_cortada.resize((nova_largura_px, nova_altura_px))

        nome_arquivo = f"BASE/Frente_{nome}.png"

        im_final.save(
            nome_arquivo,
        )

        print(f"✅ Tamanho {nome} salvo em: {nome_arquivo}")
        print(f"   > Dimensões (cm): {largura_cm}x{altura_cm}")
        print(f"   > Dimensões (px): {nova_largura_px}x{nova_altura_px}")
        print(f"   > DPI: {DPI_FINAL}")

    print("\nProcesso concluído.")


def create_tam_costa(path):
    im = Image.open(path)

    # DPI desejado para a saída impressa (e para os cálculos)

    # Parâmetros de corte (em cm)
    corte_lateral_cm = 2
    corte_baixo_cm = 1

    # Conversão de CM para Pixels (usando o DPI final)
    # 1 polegada = 2.54 cm
    corte_lateral_px = int(corte_lateral_cm * DPI_FINAL / 2.54)
    corte_baixo_px = int(corte_baixo_cm * DPI_FINAL / 2.54)

    largura_original, altura_original = im.size

    # 2. Realizando o Corte Inicial
    # -----------------------------
    # Definindo a área de corte: remover corte_lateral_px de cada lado e corte_baixo_px do fundo.
    left = corte_lateral_px
    upper = 0
    right = largura_original - corte_lateral_px
    lower = altura_original - corte_baixo_px

    im_cortada = im.crop((left, upper, right, lower))

    # 3. Definição dos Tamanhos Finais (em cm)
    # ----------------------------------------
    tamanhos_cm = {
        "P": {"a": 75, "l": 53},
        "M": {"a": 77, "l": 57},
        "G": {"a": 80, "l": 60}
    }

    # 4. Processamento e Salvamento para cada Tamanho
    # -----------------------------------------------
    print("--- Gerando Costa P, M e G ---")

    for nome, dimensoes in tamanhos_cm.items():
        altura_cm = dimensoes["a"]
        largura_cm = dimensoes["l"]

        nova_largura_px = int(largura_cm * DPI_FINAL / 2.54)
        nova_altura_px = int(altura_cm * DPI_FINAL / 2.54)

        im_final = im_cortada.resize((nova_largura_px, nova_altura_px))

        nome_arquivo = f"BASE/costa_{nome}.png"

        im_final.save(
            nome_arquivo,
        )

        print(f"✅ Tamanho {nome} salvo em: {nome_arquivo}")
        print(f"   > Dimensões (cm): {largura_cm}x{altura_cm}")
        print(f"   > Dimensões (px): {nova_largura_px}x{nova_altura_px}")
        print(f"   > DPI: {DPI_FINAL}")

    print("\nProcesso concluído.")


def create_tam_manga(path):
    im = Image.open(path)
    largura_original, altura_original = im.size

    # 1. Definição do DPI

    # 2. Definição dos Tamanhos Finais (em cm)
    tamanhos_cm = {
        "P": {"a": 38, "l": 43},
        "M": {"a": 40, "l": 46},
        "G": {"a": 42, "l": 48}
    }

    print(f"--- Gerando manga P, M e G com DPI: {DPI_FINAL} ---")

    for nome, dimensoes in tamanhos_cm.items():
        altura_cm = dimensoes["a"]
        largura_cm = dimensoes["l"]

        # 3. Calcular as Dimensões Finais em Pixels
        nova_largura_px = int(largura_cm * DPI_FINAL / 2.54)
        nova_altura_px = int(altura_cm * DPI_FINAL / 2.54)

        # --- Lógica de Corte a Partir do Meio Inferior ---

        # 4. 1º Passo: Redimensionar para a Largura Exata
        # Redimensiona a imagem original (mantendo o aspecto) para que sua largura
        # corresponda à largura final desejada em pixels.
        ratio = nova_largura_px / largura_original
        largura_temp = nova_largura_px
        altura_temp = int(altura_original * ratio)

        im_redimensionada = im.resize((largura_temp, altura_temp))

        # 5. 2º Passo: Cortar o Excesso (de cima)

        # O ponto 'lower' (base) é sempre o final da imagem redimensionada.
        lower = altura_temp

        # O ponto 'upper' (topo) é a altura total menos a altura final necessária.
        # Isso garante que a altura seja a correta e que a base seja mantida.
        upper = altura_temp - nova_altura_px

        # O ponto 'left' é 0 e 'right' é a largura total, pois já redimensionamos
        # para a largura correta (largura_temp == nova_largura_px).
        left = 0
        right = largura_temp

        # Garante que o corte só ocorra se a imagem for grande o suficiente
        # (Se upper for negativo, a imagem redimensionada é muito pequena,
        # então o 'upper' deve ser 0)
        upper = max(0, upper)

        im_final = im_redimensionada.crop((left, upper, right, lower))

        # 6. Salvar o Arquivo
        nome_arquivo = f"BASE/Manga_{nome}.png"

        # Passar o DPI explicitamente
        im_final.save(
            nome_arquivo,
            dpi=(DPI_FINAL, DPI_FINAL)
        )

        print(f"✅ Tamanho {nome} salvo em: {nome_arquivo}")
        print(f"   > Dimensões (cm): {largura_cm}x{altura_cm}")
        print(f"   > Dimensões (px): {im_final.width}x{im_final.height}")
        print(f"   > DPI: {DPI_FINAL}")

    print("\nProcesso concluído.")


def edit_costa(textos=[], imagens=[]):
    """
    textos -> lista de dicionários: [{"texto": "MICAEL", "altura_cm": 4, "topo_cm": 15, "cor": "#FFF", "espaco_letras": 0}]
    imagens -> lista de dicionários: [{"path": "LOGO.png", "largura_cm": 10, "topo_cm": 5}]
    """
    # ... (Seu código de inicialização) ...
    base = Image.open("BASE/costa_G.png").convert("RGBA")
    draw = ImageDraw.Draw(base)
    largura_img, altura_img = base.size

    # Adiciona textos
    for t in textos:
        altura_px_desejada = int(t["altura_cm"] * DPI_FINAL / 2.54)
        topo_px = int(t["topo_cm"] * DPI_FINAL / 2.54)
        espaco_letras = t.get("espaco_letras", 0)

        base_font_size = 200
        fonte = ImageFont.truetype("BebasNeue-Regular.ttf", base_font_size)
        bbox_inicial = draw.textbbox((0, 0), t["texto"], font=fonte)
        altura_texto_real = bbox_inicial[3] - bbox_inicial[1]
        scale = altura_px_desejada / altura_texto_real
        fonte = ImageFont.truetype(
            "BebasNeue-Regular.ttf", max(1, int(base_font_size * scale)))

        # 2. CALCULE AS LARGURAS CORRETAMENTE
        # O bbox retorna (x0, y0, x1, y1). A largura é x1 - x0.
        larguras = []
        for c in t["texto"]:
            # Usa um ponto de ancoragem para obter o bbox
            bbox_char = draw.textbbox((0, 0), c, font=fonte)
            largura_char = bbox_char[2] - bbox_char[0]
            larguras.append(largura_char)

        # 3. Calcule a largura total final do texto com o espaçamento personalizado
        largura_total_personalizada = sum(
            larguras) + espaco_letras * (len(t["texto"]) + 1)

        # 4. Centralize o texto usando a largura calculada
        x = ((largura_img - largura_total_personalizada) // 2)
        y = topo_px

        # 5. Desenhe o texto, aplicando o espaçamento letra por letra
        for i, c in enumerate(t["texto"]):
            # Use x e y já calculados e avance o x
            draw.text((x, y), c, font=fonte, fill=t.get("cor", "#000"))
            x += max(1, larguras[i] + espaco_letras)

        # --- FIM DA PARTE CORRIGIDA/MELHORADA ---

    # Adiciona imagens
    for img in imagens:
        if img["path"].endswith(".svg"):
            saida = os.path.splitext(img["path"])[0] + ".png"
            cairosvg.svg2png(url=img["path"], write_to=saida)
            img["path"] = saida

        png = Image.open(img["path"]).convert("RGBA")
        largura_px_desejada = int(img["largura_cm"] * DPI_FINAL / 2.54)
        escala = largura_px_desejada / png.width
        nova_altura = int(png.height * escala)
        png_resized = png.resize(
            (largura_px_desejada, nova_altura), Image.LANCZOS)

        # A centralização da imagem já estava correta
        x = (largura_img - png_resized.width) // 2
        y = int(img["topo_cm"] * DPI_FINAL / 2.54)

        base.alpha_composite(png_resized, (x, y))

    base.save("imagem_com_texto.png")


def edit_frente(imagens=[], textos=[]):
    """
    Adiciona imagens e textos a uma base, com alinhamento horizontal personalizável.

    imagens -> lista de dicionários: 
        [{"path": "LOGO.png", "largura_cm": 10, "topo_cm": 5, "alinhamento_cm": "centro"}]

    textos -> lista de dicionários:
        [{"texto": "SEU TEXTO", "altura_cm": 2, "topo_cm": 10, 
          "alinhamento_cm": 5, "espaco_letras": -10, "cor": "#FF0000"}]
    """

    # 1. Configuração da Imagem Base
    base = Image.open("BASE/Frente_G.png")
    largura_img, altura_img = base.size
    draw = ImageDraw.Draw(base)  # Objeto de desenho para o texto

    # --- Processamento de Imagens ---
    for img in imagens:
        # 1. Conversão de SVG para PNG (mantido)
        if img["path"].endswith(".svg"):
            saida = os.path.splitext(img["path"])[0] + ".png"
            # cairosvg.svg2png(url=img["path"], write_to=saida)
            img["path"] = saida

        png = Image.open(img["path"]).convert("RGBA")

        # 2. Redimensionamento da imagem
        largura_px_desejada = int(img["largura_cm"] * DPI_FINAL / 2.54)
        escala = largura_px_desejada / png.width
        nova_altura = int(png.height * escala)
        png_resized = png.resize(
            (largura_px_desejada, nova_altura), Image.LANCZOS)

        # 3. CÁLCULO DA POSIÇÃO HORIZONTAL (X)
        largura_item = png_resized.width  # Largura da imagem
        x_centro = (largura_img - largura_item) // 2

        alinhamento = img.get("alinhamento_cm", "centro")

        if alinhamento == "centro":
            x = x_centro
        else:
            try:
                deslocamento_cm = float(alinhamento)
                deslocamento_px = int(deslocamento_cm * DPI_FINAL / 2.54)
                x = x_centro + deslocamento_px
            except ValueError:
                print(
                    f"Aviso: 'alinhamento_cm' inválido ('{alinhamento}') para {img['path']}. Centralizando.")
                x = x_centro

        # 4. CÁLCULO DA POSIÇÃO VERTICAL (Y)
        y = int(img["topo_cm"] * DPI_FINAL / 2.54)

        # 5. Composição
        base.alpha_composite(png_resized, (x, y))

    # --- Processamento de Textos ---
    for t in textos:
        texto_str = t["texto"]
        altura_cm_desejada = t["altura_cm"]
        topo_cm = t["topo_cm"]
        alinhamento_cm = t.get("alinhamento_cm", "centro")
        # Padroniza para 0 se não for definido
        espaco_letras = t.get("espaco_letras", 0)
        cor = t.get("cor", "#FFFFFF")
        cor_stroke = t.get("cor_stroke", "#FFFFFF")

        altura_px_desejada = int(altura_cm_desejada * DPI_FINAL / 2.54)
        topo_px = int(topo_cm * DPI_FINAL / 2.54)

        # 1. Ajuste Dinâmico do Tamanho da Fonte (Assumindo a fonte 'BebasNeue-Regular.ttf')
        # Calcule o fator de escala com base na altura
        base_font_size = 200  # Tamanho de referência
        try:
            # Use uma fonte temporária para medir a altura do glifo
            fonte_temp = ImageFont.truetype(
                "BebasNeue-Regular.ttf", base_font_size)
            # Usa um caractere de referência
            bbox_inicial = draw.textbbox((0, 0), "A", font=fonte_temp)
            altura_texto_real = bbox_inicial[3] - bbox_inicial[1]

            # Garante que não dividimos por zero
            if altura_texto_real == 0:
                scale = 1  # fallback
            else:
                scale = altura_px_desejada / altura_texto_real

            # Aplica o novo tamanho
            fonte = ImageFont.truetype(
                "BebasNeue-Regular.ttf", max(1, int(base_font_size * scale)))
        except IOError:
            print(
                "Aviso: Fonte 'BebasNeue-Regular.ttf' não encontrada. Usando a fonte padrão.")
            fonte = ImageFont.load_default()
            # Se a fonte padrão for usada, a altura pode não ser exata.

        # 2. CÁLCULO DA LARGURA TOTAL PERSONALIZADA DO TEXTO
        larguras = []
        for c in texto_str:
            # Largura do caractere = x1 - x0 (largura da bounding box)
            bbox_char = draw.textbbox((0, 0), c, font=fonte)
            largura_char = bbox_char[2] - bbox_char[0]
            larguras.append(largura_char)

        # Largura total = soma das larguras + espaçamento extra
        largura_total_personalizada = sum(
            larguras) + espaco_letras * (len(texto_str) - 1)

        # 3. CÁLCULO DA POSIÇÃO HORIZONTAL (X)
        largura_item = largura_total_personalizada
        x_centro = (largura_img - largura_item) // 2

        if alinhamento_cm == "centro":
            x_inicial = x_centro
        else:
            try:
                deslocamento_cm = float(alinhamento_cm)
                deslocamento_px = int(deslocamento_cm * DPI_FINAL / 2.54)
                x_inicial = x_centro + deslocamento_px
            except ValueError:
                print(
                    f"Aviso: 'alinhamento_cm' inválido ('{alinhamento_cm}') para o texto. Centralizando.")
                x_inicial = x_centro

        # 4. Desenhe o texto, aplicando o espaçamento letra por letra
        x_atual = x_inicial
        y = topo_px

        for i, c in enumerate(texto_str):
            draw.text((x_atual, y), c, font=fonte, fill=cor,
                      stroke_fill=cor_stroke, stroke_width=30)
            draw.text((x_atual, y), c, font=fonte, fill=cor)
            # Avança a posição X para a próxima letra
            x_atual += max(1, larguras[i] + espaco_letras)

    # 5. Salva o resultado final
    base.save("imagem_final_editada.png")
    print("Imagem gerada com sucesso: imagem_final_editada.png")

# --- Exemplo de Uso ---
# Certifique-se de ter um arquivo de fonte chamado 'BebasNeue-Regular.ttf' no diretório.


edit_frente(
    imagens=[
        # Imagem 5 cm à esquerda do centro
        {"path": "escudo.png", "largura_cm": 9,
            "topo_cm": 17, "alinhamento_cm": "centro"},
        {"path": "45burguer.png", "largura_cm": 18,
            "topo_cm": 40, "alinhamento_cm": -1},
    ],
    textos=[
        {"texto": "10", "altura_cm": 10, "topo_cm": 25,
         "alinhamento_cm": -0.5, "espaco_letras": -10, "cor": "#ffffff", 'cor_stroke': "#161C3C"},


    ]
)
