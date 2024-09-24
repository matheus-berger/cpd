import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class MergeSortMesclar {
    
    // Número de arquivos temporários
    int totalArquivos = 10;  

    // Criando buffers para acessar os arquivos temporarios
    private BufferedReader[] readers = new BufferedReader[totalArquivos];

    // Criar o arquivo final onde os dados mesclados serão armazenados
    private FileWriter fileWriter;

    // Para ler as linhas
    private String[] linhas = new String[10];

    // Usar um Map para armazenar o índice do arquivo e o valor atual de cada arquivo
    private Map<Integer, Integer> valoresAtuais = new HashMap<>();

    public MergeSortMesclar() {
        
        // Preenchendo o buffer
        for (int i = 0; i < 10; i++) {
            try {
                readers[i] = new BufferedReader(new FileReader("../memoriaExternaSimulada/temp" + i + ".txt"));
            } catch (IOException e) {
                System.out.println("Ocorreu algum erro ao ler o arquivo temp" + i + ".txt: ");
                e.printStackTrace();
            }
        }

        //
        try {
            fileWriter = new FileWriter("../memoriaExternaSimulada/arquivo_final.txt");
        } catch (Exception e) {
            e.printStackTrace();
        } 
    }

    public void mesclarArquivos() {
        
        // Inicializar a leitura com a primeira linha de cada arquivo
        for (int i = 0; i < totalArquivos; i++) {
            
            try {
                String linha = readers[i].readLine();
                if (linha != null) {
                    valoresAtuais.put(i, Integer.parseInt(linha));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        // Enquanto ainda houver dados para processar
        while (!valoresAtuais.isEmpty()) {
            // Encontrar o menor valor e o índice correspondente
            int menorIndice = -1;
            int menorValor = Integer.MAX_VALUE;
            
            for (Map.Entry<Integer, Integer> entry : valoresAtuais.entrySet()) {
                int indice = entry.getKey();
                int valor = entry.getValue();

                if (valor < menorValor) {
                    menorValor = valor;
                    menorIndice = indice;
                }
            }

            try {
                 // Escrever o menor valor no arquivo final
                fileWriter.write(menorValor + "\n");

                // Ler a próxima linha do arquivo que tinha o menor valor
                String novaLinha = readers[menorIndice].readLine();
                if (novaLinha != null) {
                    valoresAtuais.put(menorIndice, Integer.parseInt(novaLinha));
                } else {
                    // Se o arquivo terminou, removê-lo do mapa
                    valoresAtuais.remove(menorIndice);
                }

                // Fechar todos os arquivos temporários e o arquivo final
                for (BufferedReader reader : readers) {
                    
                    reader.close();
                }
                fileWriter.close();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }   
    }
}

