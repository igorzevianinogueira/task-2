# Plano de entrega em 90 minutos

O vídeo é obrigatório para a nota. A entrega deve terminar antes das
23h59 de 9 de junho de 2026.

## Cronograma

| Janela | Ação | Resultado |
|---|---|---|
| 0–10 min | Preparar OBS, dashboard e microfone | Ambiente pronto |
| 10–25 min | Gravar no máximo duas tentativas | Vídeo final |
| 25–35 min | Conferir áudio, início e duração | Vídeo aprovado |
| 35–50 min | Enviar como não listado | Link real |
| 50–60 min | Atualizar link e gerar PDF | PDF final |
| 60–70 min | Publicar o repositório | GitHub atualizado |
| 70–80 min | Conferir os dois links | Quality gate |
| 80–90 min | Enviar ao portal | Entrega concluída |

## Configuração rápida do OBS

- **Resolução base e de saída:** 1920 × 1080.
- **FPS:** 30.
- **Formato:** MKV.
- **Codificador:** hardware, quando disponível.
- **Áudio:** 48 kHz.
- **Câmera:** desativada.
- **Fonte:** captura da tela usada na demonstração.

Use **Pausar gravação** entre os blocos do roteiro. Ao terminar, use
**Arquivo > Remuxar gravações** para criar o MP4.

## Regra de qualidade

Faça no máximo duas tentativas completas.

Aceite a gravação quando:

- a voz estiver compreensível;
- a tela estiver legível;
- o pipeline concluir;
- a divergência aparecer;
- a duração for menor que 5 minutos.

Não regrave por pequenas pausas ou movimentos do cursor.

## Publicação no YouTube

Use o título:

`TerraOps Fusion | Global Solution 2026.1 | Grupo 49`

Use a descrição:

`Prova de conceito do Grupo 49 da turma 1TIAOA. O TerraOps Fusion
combina dados orbitais, sensores terrestres, Python, Machine Learning,
SQL e visualização para apoiar decisões no agronegócio.`

Configure o vídeo como **Não listado**. Não use **Privado**.

## Fechamento

Depois de obter o link:

1. Substitua a primeira linha de `link_video.txt`.
2. Rode:

   ```bash
   .venv/bin/python entrega/gerar_pdf.py
   ```

3. Confirme que o PDF não contém `SUBSTITUIR`.
4. Publique a versão final no GitHub.
5. Abra o vídeo e o repositório em uma janela anônima.
6. Envie somente `GlobalSolution_Grupo49.pdf` no portal.
7. Confirme o status de entrega.
8. Salve uma captura da confirmação.

## Checklist

- [ ] Vídeo menor que 5 minutos.
- [ ] Vídeo não listado e acessível sem login.
- [ ] Link real do vídeo no PDF.
- [ ] Link do repositório no PDF.
- [ ] Quatro nomes completos na primeira página.
- [ ] Código apresentado como texto.
- [ ] Repositório remoto contém o projeto mostrado.
- [ ] Grupo 49 correto no portal.
- [ ] Portal mostra a entrega como concluída.
