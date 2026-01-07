minerva-doc-validator/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── main.py
│
│   ├── ingestion/
│   │   ├── loader.py
│   │   └── cleaner.py
│
│   ├── parsing/
│   │   ├── structure_parser.py
│   │   └── text_document.py
│
│   ├── multimodal/
│   │   ├── diagram_detector.py
│   │   ├── flowchart_parser.py
│   │   └── diagram_to_text.py
│
│   ├── features/
│   │   ├── structural.py
│   │   ├── linguistic.py
│   │   └── semantic.py
│
│   ├── rag_simulation/
│   │   ├── query_generator.py
│   │   └── retriever.py
│
│   ├── scoring/
│   │   ├── scorer.py
│   │   └── explanations.py
│
│   └── utils/
│       └── text_utils.py







Perfeito. Abaixo está uma Metodologia completa, detalhada, acadêmica e defensável, escrita no nível esperado para um relatório de estágio de verão, TCC forte ou até base de paper aplicado.
Ela está alinhada exatamente com a arquitetura PDF-first que você implementou.

Você pode copiar e colar direto no relatório, ajustando apenas o contexto institucional se quiser.

3. Metodologia
3.1 Visão Geral do Sistema

Este trabalho propõe um sistema automático para validação de documentos destinados a sistemas de Recuperação Aumentada por Geração (RAG), com foco prioritário em documentos PDF, que constituem o formato predominante no contexto de aplicação do projeto Minerva.

O objetivo do sistema é atribuir um score quantitativo de adequação a um documento, indicando o quão apropriado ele está para ser indexado e utilizado por uma IA baseada em RAG. Além do score, o sistema gera explicações interpretáveis, destacando limitações estruturais ou semânticas do documento e sugerindo possíveis melhorias.

A metodologia adotada segue uma abordagem pipeline modular, composta por cinco etapas principais:

Ingestão e extração de conteúdo

Normalização e limpeza textual

Inferência de estrutura documental

Extração de características (features)

Simulação de desempenho em RAG e cálculo do score final

Essa decomposição visa garantir reprodutibilidade, extensibilidade e clareza metodológica.

3.2 Ingestão de Documentos
3.2.1 Estratégia PDF-first

Diferentemente de abordagens genéricas que tratam todos os formatos de forma uniforme, este trabalho adota uma estratégia PDF-first, reconhecendo que documentos PDF apresentam desafios específicos, como:

múltiplas páginas,

estrutura implícita (seções, títulos, hierarquia),

ruídos recorrentes (headers, footers, numeração),

possibilidade de documentos escaneados.

Assim, o sistema identifica o tipo de arquivo no momento da ingestão e seleciona automaticamente o carregador apropriado.

3.2.2 Extração de Texto de PDFs

Para documentos PDF com texto nativo, utiliza-se uma extração página a página, preservando granularidade estrutural. Cada página é representada por um conjunto mínimo de metadados:

número da página,

texto extraído,

quantidade de caracteres.

Essa estratégia permite análises posteriores relacionadas à densidade textual, regularidade estrutural e fragmentação, fatores relevantes para sistemas RAG.

PDFs cuja extração resulta em baixa quantidade total de caracteres são sinalizados como potencialmente escaneados, sendo considerados como limitação atual do sistema e apontados como trabalho futuro para integração com OCR.

3.2.3 Suporte a Outros Formatos

Embora PDFs sejam prioritários, o sistema também suporta arquivos textuais simples (e.g., .txt, .md). Esses documentos passam por uma ingestão simplificada, sendo tratados como texto contínuo, sem granularidade por página.

Essa decisão mantém a generalidade do sistema, sem comprometer o foco principal.

3.3 Limpeza e Normalização Textual

Após a ingestão, o texto extraído passa por uma etapa de normalização, cujo objetivo é reduzir ruídos que impactam negativamente análises linguísticas e semânticas.

As operações incluem:

remoção de espaços redundantes,

normalização de quebras de linha,

remoção de padrões recorrentes irrelevantes (e.g., numeração de páginas).

Essa etapa é fundamental para garantir que métricas posteriores reflitam a qualidade real do conteúdo, e não artefatos de formatação.

3.4 Inferência de Estrutura Documental
3.4.1 Representação Estrutural

O sistema transforma o texto limpo em uma representação intermediária estruturada. Para PDFs, essa representação preserva:

conjunto de páginas,

lista de seções inferidas,

relação indireta entre páginas e seções.

Essa representação é encapsulada em um objeto documental específico, permitindo que etapas posteriores sejam agnósticas ao formato original.

3.4.2 Heurísticas de Segmentação

A segmentação em seções é realizada por heurísticas simples, baseadas em:

tamanho mínimo de texto por segmento,

separação por blocos textuais significativos.

Apesar de não utilizar aprendizado supervisionado, essa abordagem se mostrou adequada como baseline e possui a vantagem de ser interpretável e reprodutível, características desejáveis em contexto acadêmico.

3.5 Extração de Características (Features)

A avaliação do documento é realizada a partir de um conjunto de características agrupadas em três categorias: estruturais, linguísticas e semânticas.

3.5.1 Características Estruturais

As características estruturais avaliam a organização global do documento, incluindo:

número total de seções,

tamanho médio das seções,

número de páginas (para PDFs),

densidade média de caracteres por página.

Essas métricas são especialmente relevantes para RAG, pois documentos bem estruturados tendem a gerar chunks mais coerentes, melhorando a recuperação de informação.

3.5.2 Características Linguísticas

As características linguísticas analisam propriedades estatísticas do texto, tais como:

número médio de palavras por seção,

densidade lexical aproximada.

Essas métricas atuam como proxies para avaliar clareza textual, redundância excessiva e ruídos introduzidos por extração inadequada (por exemplo, OCR de baixa qualidade).

3.5.3 Características Semânticas

Dada a natureza exploratória do projeto, as características semânticas são modeladas de forma simplificada, utilizando métricas proxy baseadas na segmentação e no volume textual.

Essa escolha é intencional, visando estabelecer um baseline extensível para futura integração de embeddings e modelos semânticos profundos.

3.6 Simulação de Uso em Sistemas RAG

Para avaliar a adequação do documento ao contexto de RAG, o sistema simula um cenário de recuperação de informação.

3.6.1 Geração de Consultas

Consultas artificiais são geradas a partir de trechos representativos das seções do documento. Essa estratégia busca simular perguntas plausíveis que um usuário faria ao sistema Minerva.

3.6.2 Avaliação de Recuperabilidade

A recuperabilidade é estimada com base na relação entre:

número de consultas geradas,

número de seções disponíveis.

Essa métrica fornece uma estimativa da capacidade do documento de suportar consultas diversas, um aspecto central em sistemas RAG.

3.7 Cálculo do Score Final e Explicabilidade
3.7.1 Agregação do Score

O score final é calculado por meio de uma combinação ponderada das principais dimensões avaliadas:

qualidade estrutural,

densidade informacional,

recuperabilidade para RAG.

Os pesos refletem a importância relativa desses fatores no desempenho de sistemas RAG, com ênfase maior na estrutura documental, especialmente para PDFs.

3.7.2 Geração de Explicações

Além do score numérico, o sistema gera explicações textuais interpretáveis, destacando:

baixa segmentação estrutural,

densidade textual insuficiente,

potenciais limitações para uso em RAG.

Essa abordagem visa tornar o sistema diagnóstico, não apenas avaliativo, auxiliando usuários na melhoria dos documentos.

3.8 Considerações Metodológicas e Limitações

O sistema proposto adota heurísticas determinísticas e métricas proxy como escolha metodológica consciente, priorizando:

interpretabilidade,

facilidade de extensão,

adequação ao contexto de estágio.

Limitações atuais incluem:

ausência de OCR integrado para PDFs escaneados,

ausência de embeddings semânticos profundos,

dependência de heurísticas para inferência estrutural.

Essas limitações são consideradas oportunidades claras para trabalhos futuros.

3.9 Síntese

A metodologia apresentada estabelece uma pipeline modular, extensível e focada em PDFs para validação automática de documentos destinados a sistemas RAG. Ao combinar análise estrutural, linguística e simulação de recuperação, o sistema fornece uma avaliação quantitativa e explicável da adequação documental, alinhada às necessidades do projeto Minerva.

Se você quiser, no próximo passo eu posso:

adaptar esse texto para formato de paper (IEEE/ACM)

reduzir para versão resumida de relatório de estágio

escrever Resultados esperados / Discussão

alinhar a metodologia explicitamente com RAG e LLMs

É só me dizer.