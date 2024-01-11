# Projeto de Raspagem de Dados do Sistema Hidroweb

Este projeto é um raspador de dados do sistema Hidroweb (https://www.snirh.gov.br/hidroweb/serieshistoricas) desenvolvido para avaliar se a relação entre a altura e a vazão do rio Doce foi alterada devido à tragédia da Samarco. A necessidade de desenvolver esse raspador surgiu devido às limitações do sistema Hidroweb, que permite o download de arquivos com intervalo máximo de 90 dias. Para a finalidade deste projeto, baixar os dados em partes tão pequenas seria uma tarefa muito trabalhosa.

## Objetivo

O objetivo principal deste projeto é avaliar se a relação entre a altura e a vazão do rio Doce foi impactada pela tragédia da Samarco. Inicialmente, optou-se por baixar apenas os dados produzidos pela CPRM na estação em Governador Valadares, com código 185241570, uma vez que as outras estações automáticas/telemétricas estão operando por um período mais curto.

### Metodologias

Para atingir esse objetivo, algumas metodologias estão sendo consideradas:

1. **Equação de Manning**: Uma das abordagens é a aplicação da equação de Manning para calcular a vazão do rio com base na altura. No entanto, é necessário coletar mais dados para utilizar plenamente essa metodologia.

2. **Regressão Simbólica**: Outra abordagem é a utilização de regressão simbólica para caracterizar a equação que governa a relação entre a altura e a vazão antes e depois da tragédia.

3. **Métodos Estatísticos**: Além disso, serão aplicados métodos estatísticos para analisar a variação da relação entre a altura e a vazão ao longo do tempo.

## Estado Atual

Este é um projeto que está em estágio inicial e ainda há muito trabalho a ser feito. A coleta de dados é apenas o primeiro passo, e a análise completa da relação entre a altura e a vazão do rio Doce exigirá mais investigação e processamento de dados. A equipe está comprometida em continuar trabalhando no projeto e buscar insights sobre o impacto da tragédia da Samarco no rio Doce.

Sinta-se à vontade para contribuir ou entrar em contato se tiver interesse em colaborar com este projeto.

