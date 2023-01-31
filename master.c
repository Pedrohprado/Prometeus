// EmonLib - Version: Latest
#include <EmonLib.h>

// Incluindo bibliotecas e definindo as entradas ativas

#define botao 2
#define led 13
#define buzz 10

// Criação de variáveis

unsigned long int tempoAnterior = 0; // Auxiliar na function millis()

int valorBotao = 0;

int pinSCT = A0;  // Pino analógico conectado ao SCT-013
int tensao = 380; // A tensão foi alterada de 290 para 380
int i = 0;
int potencia;
float correntem;

EnergyMonitor SCT013; // energizando o pino de entrada sct-013

void setup()
{
    SCT013.current(pinSCT, 6.0607); // sensor nao envazivo 111.1 60.0606 6.0607
    pinMode(botao, INPUT);
    pinMode(led, OUTPUT);
    pinMode(buzz, OUTPUT);

    Serial.begin(9600);
}

void loop()
{
    double Irms = SCT013.calcIrms(1480); // Calcula o valor da Corrente

    potencia = Irms * tensao; // Calcula o valor da Potencia Instantanea
    correntem = Irms * 21.31; // Fizemos alteração no valor do mult*

    valorBotao = digitalRead(botao); // instrução que faz a leitura de um INPUT

    if (millis() - tempoAnterior >= 1000)
    {
        tempoAnterior = millis();
        i = i + 1;

        while (correntem >= 2)
        {
            // Serial.print("valor da potencia da rede:");
            // Serial.println(potencia);
            // Serial.print("valor da corrente da rede:");
            // Serial.println(Irms);
            // Serial.print("Corrente de solda:");
            Serial.print(correntem);

            i = 0;
            break;
        }

        if (i >= 100)
        {
            tone(buzz, 1000, 500);
        }
    }
}