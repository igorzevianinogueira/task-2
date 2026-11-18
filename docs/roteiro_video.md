# Roteiro final do vídeo

**Duração-alvo:** 4 minutos e 15 segundos
**Limite do enunciado:** 5 minutos
**Formato:** narração com captura de tela
**Publicação obrigatória:** YouTube como **não listado**

O vídeo é obrigatório para a nota, mesmo sem candidatura ao pódio. Este
roteiro não inclui a frase `QUERO CONCORRER`.

## Como gravar em blocos no OBS

Faça uma única gravação e use **Pausar gravação** entre os blocos.

1. Grave o bloco.
2. Pause a gravação.
3. Prepare a tela do próximo bloco.
4. Respire e retome a gravação.

Isso gera um único arquivo e evita edição para juntar vídeos.

Leia somente o texto em **Fala**. As instruções em **Tela** não devem ser
lidas.

## Preparação

1. Inicie o Streamlit:

   ```bash
   cd tasks/task10_global_solution
   .venv/bin/python -m streamlit run dashboard/app.py
   ```

2. Abra o **Network URL** mostrado pelo Streamlit. Nesta sessão:
   `http://192.168.1.100:8501`.
3. Deixe o navegador em tela cheia e com zoom de 100%.
4. Feche notificações, e-mail, WhatsApp e abas pessoais.
5. Deixe este roteiro em outro monitor ou no celular.
6. Grave um teste de 15 segundos e escute o áudio.

## Bloco 1: abertura

**Tempo:** 0:00–0:30
**Tela:** primeira página do PDF ou visão geral do dashboard.

**Fala**

> Olá, professores. Somos o Grupo 49, da turma 1TIAOA. O grupo é
> formado por Higor Henrique Garcia, Vinicius Alves Lopes dos Anjos,
> Igor Zeviani Nogueira e Humberto Salim.
>
> Esta é a nossa Global Solution: TerraOps Fusion, uma prova de conceito
> que transforma dados espaciais e sensores locais em apoio à decisão
> para o agronegócio.

Pause e prepare o dashboard.

## Bloco 2: problema e proposta

**Tempo:** 0:30–1:00
**Tela:** deixe o Streamlit aberto antes de clicar no botão.

**Fala**

> Hoje, o dado do satélite e a medição feita no solo normalmente chegam
> separados. O satélite oferece visão ampla, mas pode ter atraso ou
> interferência. O sensor local oferece precisão no ponto medido, mas não
> representa sozinho todo o talhão.
>
> Nossa proposta cruza essas duas camadas e apresenta uma prioridade
> operacional em uma única central.

## Bloco 3: pipeline funcionando

**Tempo:** 1:00–1:35
**Tela:** clique em **Executar fusão** na barra lateral.

**Fala**

> Ao clicar em Executar fusão, o sistema inicia um pipeline em Python.
> Ele gera o conjunto de dados, grava as informações em SQLite, treina
> um modelo Random Forest, calcula a fusão e publica um snapshot em JSON.
>
> Nesse fluxo usamos condicionais, laços de repetição, manipulação com
> Pandas, Machine Learning introdutório e consultas SQL.

Espere a mensagem **Fusão concluída**. Pause e posicione o cursor na
primeira coluna.

## Bloco 4: decisão do operador

**Tempo:** 1:35–2:10
**Tela:** aponte para a zona **Decisão**, o índice e a recomendação.

**Fala**

> Esta é a Mission Control. Na primeira zona, o operador vê o
> StressFusion, um índice de zero a cem calculado com dados orbitais,
> dados do solo e a probabilidade produzida pelo modelo.
>
> O número não aparece sozinho. O sistema também apresenta a categoria
> e uma recomendação. Assim, o usuário entende se pode agir ou se precisa
> investigar.

Pause e posicione o cursor no ranking.

## Bloco 5: prioridade da gestora

**Tempo:** 2:10–2:40
**Tela:** percorra a zona **Orbital** e o ranking.

**Fala**

> Na segunda zona, a gestora encontra o ranking dos talhões. A prova de
> conceito trabalha com café, soja e milho, e ordena os lotes pela
> prioridade relativa.
>
> Isso reduz o tempo gasto comparando planilhas e ajuda a direcionar
> primeiro a equipe para os pontos que merecem atenção.

Pause e posicione o cursor nas barras da terceira coluna.

## Bloco 6: divergência e explicabilidade

**Tempo:** 2:40–3:35
**Tela:** aponte para as barras, o delta, a explicação e a ação sugerida.
Role dentro do painel somente se necessário.

**Fala**

> A terceira zona é o principal diferencial da solução. Ela compara o
> NDVI observado pelo satélite com a umidade medida no solo.
>
> Neste exemplo, o risco agregado está baixo, mas existe uma divergência:
> o satélite indica vegetação vigorosa enquanto o sensor registra solo
> seco. Em vez de esconder essa discordância, o sistema calcula o delta,
> apresenta hipóteses e recomenda validar a leitura no campo.
>
> Essa explicação evita tratar a inteligência artificial como resposta
> absoluta. O modelo é introdutório e funciona como apoio à decisão, não
> como substituto do profissional.

Pause e volte para a visão geral.

## Bloco 7: integração e encerramento

**Tempo:** 3:35–4:30
**Tela:** visão geral da Mission Control.

**Fala**

> A solução integra Python, Pandas, estatística, Random Forest, SQLite,
> sensores simulados em ESP32 e Wokwi, visualização de dados e
> privacidade. Os dados da demonstração são fictícios e reproduzíveis.
>
> Como decisão de projeto, usamos dados orbitais em cache e sensores
> simulados para garantir que a prova de conceito possa ser executada
> novamente durante a avaliação. O trabalho foi dividido entre pipeline,
> Machine Learning, interface, documentação e integração da entrega.
>
> O TerraOps Fusion demonstra como a tecnologia espacial pode sair do
> mapa e chegar à decisão prática: satélite e solo, juntos, no tempo
> certo.
>
> O código, a documentação e as instruções de execução estão no
> repositório indicado no PDF. Obrigado.

## Plano de emergência

Se o Streamlit não carregar:

1. Pare a gravação.
2. Rode:

   ```bash
   .venv/bin/python scripts/run_pipeline.py
   .venv/bin/python dashboard/export_video_demo.py
   ```

3. Abra `dashboard/video_demo.html` como contingência.
4. Recomece a gravação.

Se o vídeo passar de 5 minutos, corte primeiro:

1. A segunda frase do bloco 5.
2. A lista de tecnologias do bloco 7.
3. Pausas no começo e no fim.

Não corte a execução do pipeline nem a explicação da divergência.

## Depois da gravação

1. Confira se a duração é menor que 5 minutos.
2. No OBS, remuxe de MKV para MP4.
3. Envie o MP4 ao YouTube.
4. Configure a visibilidade como **Não listado**.
5. Abra o link em janela anônima.
6. Atualize a primeira linha de `link_video.txt`.
7. Gere novamente o PDF.
