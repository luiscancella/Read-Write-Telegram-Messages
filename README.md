# Read-Write-Telegram-Messages

🇧🇷
Script feito para ler mensagens de grupos/chat no Telegram e compartilhar para outros atraves de um bot do telegram.
Ele foi feito com o intuito de ler chats do Telegram, já que a api não esse oferece suporte, e poder ser mudado para que a pessoa trate os dados da forma que quiser.

🇺🇸
Script made to read messages from groups/chat on Telegram and share to others through a telegram bot.
It was made with the intention of reading Telegram chats, since the api does not support it, and it can be changed so that the person treats the data the way they want.

🇧🇷
-

- Como Instalar?

Instale o arquivo por git clone ou direto pelo link https://github.com/luiscancella/Read-Write-Telegram-Messages/archive/refs/heads/main.zip


- Como usar?

Pré-requisitos:

        Python
        Google Chrome instalado (para usar seus binparios)
        Bibliotecas:
          - BeautifulSoup4
          - Selenium
          - pyTelegramBotAPI
          - webdriver-manager

Com tudo instalado, mude o arquivo config.txt para conter 3 linhas, com as seguintes instruções:

      1 linha : coloque token do seu bot (pego pelo BotFather)
      2 linha : coloque o id do chat que será lido
      3 linha : coloque os ids dos chat que serão reencaminhados as mensagens separados por vírgulas sem espaço

Exemplo:

      k5k4kkjj4jj4jnm5nm5nm
      -3333333
      -123123123,-321321321,-33333333,-9999999999
nota: O id de chat pode ser pego geralmente pela url

🇺🇸
-

- How to install?

Install the file via git clone or direct via the link https://github.com/luiscancella/Read-Write-Telegram-Messages/archive/refs/heads/main.zip

- How to use?

Prerequisites:

        Python
        Google Chrome installed (to use its binaries)
        Libraries:
          - BeautifulSoup4
          - Selenium
          - pyTelegramBotAPI
          -webdriver-manager
      
With everything installed, change the config.txt file to contain 3 lines, with the following instructions:

      1 line : put your bot's token (taken by BotFather)
      2nd line: put the id of the chat that will be read
      3rd line: put the ids of the chats that will be forwarded the messages separated by commas without spaces

Example:

      k5k4kkjj4jj4jnm5nm5nm
      -3333333
      -123123123, -321321321, -33333333, -9999999999
note: The chat id can usually be retrieved from the url
