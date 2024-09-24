/*
 * Este algoritmo será responsavel por gerar um arquivo txt de tamanho de 100 MB.
 * Esse arquivo irá junto com o diretorio onde esse algoritimo esta, ira simular uma
 * memoria externa.
 * Esse arquivo ira conter cerca de 12 milhões de linhas onde cada uma possuí um numero inteiro de
 * aproximadamente 6 digitos. 
*/

// Importação de Classes com métodos necessarios
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class GeradorDeDados {

    // Atributo
    static File arquivo = null;
    
    // Método para criar arquivo
    public static void criarArquivo() {
        try {

            // Criando objeto File
            arquivo = new File("dados.txt");

            // Criando arquivo e vendo se ele ja existe
            if (arquivo.createNewFile()) {
                System.out.println("Arquivo Criado: " + arquivo.getName());
            } else {
                System.out.println("O arquivo já existe!");
            }
        
        // Gerando uma exeção caso a criação de arquivo não funcione
        } catch (IOException e) {
            System.out.println("Ocorreu algum erro! Tente novamente.");
            e.printStackTrace();
        }
    }

    // Método para gerar valores inteiros e colocar no arquivo
    public static void preencherArquivo() {
        try {
            
            // Criando o objeto FileWriter para escrever detro do arquivo
            FileWriter fileWriter = new FileWriter("dados.txt");

            // Cria valores até o arquivo ter 10 MB
            while (arquivo.length() < 10000000) {
                
                // Craindo valor inteiro aleatorio entre 100000 - 200000
                int numeroAleatorio = (int)(Math.random() * 200001) + 100000;

                // Escrevendo o valor no documento
                fileWriter.write(numeroAleatorio + "\n");

                // Garantir que o tamanho do arquivo seja atualizado de maneira mais contínua
                fileWriter.flush();
                
            }
            
            // Fechando objeto FileWriter
            fileWriter.close();

            // Printando resultado para o Usuario
            System.out.println("Arquivo preenchido com sucesso!");
            
        // Exeção para caso não seja possivel preencher o arquivo correramente 
        } catch (IOException e) {
            System.out.println("Ocorreu algum erro para preencher o arquivo.");
            e.printStackTrace();
        }
    }

    // método main
    public static void main(String[] args) {
        
        // Chamando função para criar aquivo
        criarArquivo();

        // Vê se o arquivo foi criado corretamente
        if (arquivo != null) {
            // Se foi, preenche o arquivo:
            preencherArquivo();
        }
    }
}
