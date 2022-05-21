# Driver para luzes do teclado do Notebook Avell G1513 BS MUV / A52 BS MUV

O notebook Avell A52 é equipado com um teclado retroiluminado com leds RGB, contudo a Avell não fornece suporte Linux.

O chip utilizado para controlar esse recurso é ITE 8291 V0.2, o qual é listado como um dispositivo USB. Através de engenharia reversa e pesquisa em outros projetos - listados nas referências - foi possível desenvolver um driver para a versão 0.02 do dispostivo ITE 8291.

Para verificar se o seu notebook utiliza este dispositivo use o comando abaixo:

```console
$lsusb

Bus 001 Device 003: ID 048d:ce00 Integrated Technology Express, Inc.

```


## Como instalar?

```console

sudo pip3 install avell_a52

```
Configurar udev rules, para utilizar o driver sem necessidade de usar sudo.

Criar o arquivo  **/etc/udev/rules.d/50.ite.rules** com o seguinte conteúdo:

```

SUBSYSTEM !="usb_device", ACTION !="add", GOTO="ite8291_rules_end"
  
SYSFS{idVendor} =="048d", SYSFS{idProduct} =="ce00", SYMLINK+="ite8291"

MODE="0666", OWNER="SUBSTITUIR_POR_SUA_CONTA_DE_USUARIO", GROUP="root"

LABEL="ite8291_rules_end"

```

## Como usar?

O comando para controlar os luzes do teclado é **ligthkeys**, possui vários parâmetros sendo dois principais:

-c color -> Usado para colocar somente uma cor no teclado

-e effect -> Usado para aplicar os efeitos rainbow, breathin, ...

Somente pode ser utilizado um por vez -c ou -e 

-b -> Controle de Brilho

-d -> Direção do Efeito

-s -> Velocidade do Efeito

Tanto -d como o -s, terão efeito quando utilizado em conjunto com o parâmetro -e

-o -> Desligar as luzes do teclado

-w 1 -> Utilizado para salvar um efeito, o qual será utilizado na inicialização.

```console
$ lightkeys --help

usage: lightkeys [-h]
                 [-c {aqua,blue,fuchsia,green,gray,lime,maroon,navy,olive,purple,red,silver,teal,white,yellow,orange}]
                 [-e {rainbow,breathing,flash,mix,waving}] [-s {s1,s2,s3,s4}]
                 [-b {b0,b1,b2,b3,b4}] [-d {left2right,right2left,sync}] [-o]
                 [-w {0,1}]

Control Center Keyboard Lights Avell A52

optional arguments:
  -h, --help            show this help message and exit
  -c {aqua,blue,fuchsia,green,gray,lime,maroon,navy,olive,purple,red,silver,teal,white,yellow,orange}
                        Set color
  -e {rainbow,breathing,flash,mix,waving}
                        Effects
  -s {s1,s2,s3,s4}      Set Speed of effect
  -b {b0,b1,b2,b3,b4}   Adjust the Bright
  -d {left2right,right2left,sync}
                        Direction of effect
  -o                    Turnoff lights
  -w {0,1}              Startup config
```

## Exemplos:

### Aplicar luz azul no teclado

```console

$ lightkeys -c blue

```

### Aplicar o efeito breathing, velocidade máxima e brilho mínimo

```console

$ lightkeys -e breathing -s s4 -b b1

```


### Aplicar o efeito flash, com a direção da direita para a esquerda, velocidade média e brilho máximo e salvar como padrão de inicialização

```console

$ lightkeys -e flash -s s2 -b b4 -d right2left -w 1

```


## Referências

[avell-unofficial-control-center](https://github.com/rodgomesc/avell-unofficial-control-center)

[Project: STAR BEAT!](https://github.com/kirainmoe/project-starbeat)

## Termo de Isenção

O desenvolvedor não se responsabiliza por qualquer dano e/ou prejuízo e/ou lucros cessantes sofridos pelo usuário que se sintam prejudicados em consequência de qualquer motivo de não funcionamento, falha de hardware ou software do aplicativo em questão. 
