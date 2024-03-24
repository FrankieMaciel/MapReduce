# MapReduce

## Instruções para Executar os Componentes:

1. **FileGenerator:**
   - Execute o FileGenerator utilizando o comando:
     ```
     python FileGenerator.py
     ```
   Este comando gerará os arquivos necessários para o processo de MapReduce.

2. **countingWords:**
   - Execute countingWords usando o comando:
     ```
     python countingWords.py
     ```
   Este script contará as palavras nos arquivos gerados.

3. **grep:**
   - Para usar o grep e buscar por uma palavra específica, utilize o comando:
     ```
     python grep.py abc ./data/file_0.txt ./data/file_1.txt
     ```
   Isso buscará a palavra "abc" nos arquivos especificados.

4. **grep com Expressões Regulares:**
   - Para buscar usando expressões regulares, utilize o comando:
     ```
     python grep.py -e "^abc" ./data/file_0.txt ./data/file_1.txt
     ```
   Isso realizará uma busca usando a expressão regular "^abc" nos arquivos especificados.

**Observação:** Certifique-se de ter os arquivos de dados necessários no diretório correto antes de executar os scripts.
