# Combo_RSS

## PRIMEIRA INSTALAÇÃO:

## Executar os comandos abaixo:

### Instalar git através do PowerShell

```
winget install --id Git.Git -e --source winget
```

### Clonar repositório através do Git Bash

```
git clone https://github.com/lucasgiannone/combo_rss.git
```

> Token para autenticar na janelinha do GitHub
```
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
```

## ATUALIZAÇAO ATRAVÉS DO BASH
### (Para primeiras versões sem o autoDeploy)

> Executar o fetch através do Git Bash
```
git fetch
```
> Executar o update através do Git Bash
```
git reset --hard origin/main
```
> Após isso abrir o Executar (Win+D) e abrir o local:
```
shell:startup
```
> Copiar o start.bat como atalho nesse diretório