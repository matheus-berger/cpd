
/*
 * 
*/

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;


public class MergeSortExterno {
    
    // Número de arquivos de arquivos temporarios salvos 
    private static int arquivosTemporarios = 0;
    // Lista dos nomes dos arquivos temporarios
    private static ArrayList<String> localArquivosTemporarios = new ArrayList<String>();

    // Método para dividir o arquivo de entrada em blocos menores
    public static void dividirEmBlocos() {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("../memoriaExternaSimulada/dados.txt"));
            String linha;
            int contadorBlocos = 0;
            File bloco = new File("bloco" + contadorBlocos + ".txt");
            FileWriter fileWriter = new FileWriter(bloco);
            long tamanhoAtualBloco = 0;

            // Processa cada linha do arquivo
            while ((linha = reader.readLine()) != null) {
                fileWriter.write(linha + "\n");
                tamanhoAtualBloco += linha.length() + 1;  // Considera o \n

                // Quando o tamanho do bloco atingir 1000 KB, cria um novo bloco
                if (tamanhoAtualBloco >= 1000000) {
                    fileWriter.flush();
                    fileWriter.close();
                    mergeSortInterno(bloco);
                    bloco.delete();

                    contadorBlocos++;
                    bloco = new File("bloco" + contadorBlocos + ".txt");
                    fileWriter = new FileWriter(bloco);
                    tamanhoAtualBloco = 0;
                }
            }

            // Processa o último bloco se restar algum dado
            if (tamanhoAtualBloco > 0) {
                fileWriter.flush();
                fileWriter.close();
                mergeSortInterno(bloco);
            }

            // Fecha o leitor
            reader.close();

            // Certifica que o programa termina
            System.out.println("Processamento de blocos concluído.");
            

        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }
    


    // Método para fazer o Merge Sort Interno
    public static void mergeSortInterno(File bloco) {

        try {
            // Cria um BufferedReader para ler cada linha do bloco
            BufferedReader reader = new BufferedReader(new FileReader(bloco));

            // Cria uma lista para armazenar os numeros de cada linha
            ArrayList<Integer> numeros = new ArrayList<Integer>();

            // Variavel para armazenar uma linha
            String linha;

            // Variavel linha recebe cada linha do arquivo, isso irá se repitir até o arquivo terminar
            while ((linha = reader.readLine()) != null) {
                numeros.add(Integer.parseInt(linha));
            }

            // Executa método para ordenar a lista
            sort(numeros);

            // Cria o arquivo temporario na memoria externa após a ter sido lista ordenda
            criarArquivoTemporario(numeros);

            // Fechando objeto bufferReader
            reader.close();
        
        // Gerando a exeção
        } catch (IOException e) {
            System.out.println("Erro ao ler o bloco no Merge Sort Interno: " + e.getMessage());
        }
    }


    // Método Sort
    public static void sort(ArrayList<Integer> lista) {

        // Caso base: se a lista tiver 1 ou menos elementos, já está ordenada
        if (lista.size() <= 1) {
            return;
        }

        // Encontrar o meio da lista
        int meio = lista.size() / 2;

        // Criar duas sublistas
        ArrayList<Integer> esquerda = new ArrayList<>(lista.subList(0, meio));
        ArrayList<Integer> direita = new ArrayList<>(lista.subList(meio, lista.size()));

        // Ordenar cada metade recursivamente
        sort(esquerda);
        sort(direita);

        // Mesclar as duas metades ordenadas
        merge(lista, esquerda, direita);
    }


    // Método para mesclar lista de inteiros
    public static void merge(ArrayList<Integer> lista, ArrayList<Integer> esquerda, ArrayList<Integer> direita) {
        int i = 0, j = 0;

        // Limpar a lista original antes de adicionar os elementos mesclados
        lista.clear();

        // Compara os elementos das sublistas e mescla de volta na lista original
        while (i < esquerda.size() && j < direita.size()) {
            if (esquerda.get(i) <= direita.get(j)) {
                lista.add(esquerda.get(i++));
            } else {
                lista.add(direita.get(j++));
            }
        }

        // Adiciona os elementos restantes da sublista da esquerda (se houver)
        while (i < esquerda.size()) {
            lista.add(esquerda.get(i++));
        }

        // Adiciona os elementos restantes da sublista da direita (se houver)
        while (j < direita.size()) {
            lista.add(direita.get(j++));
        }
    }

       
    // Método para criar arquivo temporario
    public static void criarArquivoTemporario(ArrayList<Integer> lista) {

        // Criando arquivo temporario
        String arquivoTemporarioNome = "temp" + Integer.toString(arquivosTemporarios) + ".txt";
        String localArquivoTemporario = "../memoriaExternaSimulada/" + arquivoTemporarioNome;
        File arquivo = new File(localArquivoTemporario);
        localArquivosTemporarios.add(localArquivoTemporario);
        
        try {
            // Criando o objeto FileWriter
            FileWriter fileWriter = new FileWriter(arquivo);

            // Percorrendo a lista
            for (Integer i : lista) {
                // Escrevendo o valor no documento
                fileWriter.write(i + "\n");

                // Garantir que o tamanho do arquivo seja atualizado de maneira mais contínua
                fileWriter.flush();
            }

            // Fechando o objeto fileWriter
            fileWriter.close();
            
            // Incrementar o contador de arquivos temporários
            arquivosTemporarios++;

        // Gerando uma exeção
        } catch (Exception e) {
            System.out.println("Erro ao escrever no arquivo temporario numero " + arquivosTemporarios + ": " + e.getMessage());
        }
    }

    
    // Método Main
    public static void main(String[] args) {
        
        dividirEmBlocos();

        System.out.println("> Iniciando a mesclagem");

        MergeSortMesclar mesclagem = new MergeSortMesclar();
        mesclagem.mesclarArquivos();

    }
}
