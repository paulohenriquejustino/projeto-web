import 'dart:io';
import 'dart:math';

void main () {
  print('1 - ATIVIDADE D - NÚMEROS PARES ENTRE 1 E 100');
  print('2 - ATIVIDADE B - FORMAÇÃO DE UM TRIÂNGULO');
  print('3 - ATIVIDADE I - NÚMERO ENTRE O INTERVALO');

  int opcao = int.parse(stdin.readLineSync()!); // fazendo a conversão de string para int

  switch(opcao) {

    case 1:

    //Criando uma lista vazia
    List<int> numeros = [];
    
    //Utilizando for para gerar número de 0 a 100.
    for (int num = 0; num <= 100; num++){
      // Com incrementação!(num++)
      
      if (num % 2 == 0) { //Se num dividido por 2 tiver o resto 0... 
        //Guardando os números dentro da lista criada.
        numeros.add(num);
      }
    }
  
    print("Minha lista de números é $numeros"); // Para mostar a lista coloque o nome da sua lista.
    break;


    case 2:
    // A condição para que esses segmentos formem um 
    //triângulo é a seguinte: sempre que a soma das medidas 
    //dos segmentos que estão sendo girados for maior que a
    // medida do terceiro segmento, é possível construir um 
    // triângulo.

    print('Digite o primeiro número: ');
    int a = int.parse(stdin.readLineSync()!); //função

    print('');// pular linha
    print('Digite o segundo número: ');
    int b = int.parse(stdin.readLineSync()!); //função

    print('');// pular linha
    print('Digite o terceiro número: ');
    int c = int.parse(stdin.readLineSync()!); //função
    print('');
    

    if ((a + b) > c ) {
      print('Forma um trinângulo!');
    } else if ((b + a) > c ) {
      print('Forma um trinângulo!');
    } else if (a <= 0)  {
      print('O número deve ser maior do que zero.');
    } else if (b <= 0)  {
      print('O número deve ser maior do que zero.');
    } else if (c  <= 0)  {
      print('O número deve ser maior do que zero.');
    } else {
      print('Não forma um trinângulo!');
    }
    break;

  }


}