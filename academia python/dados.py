import funcoes
erros = funcoes.valida_questoes([{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

        {'titulo': 'Quais o menor e o maior país do mundo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Vaticano e Rússia', 'B': 'Nauru e China', 'C': 'Mônaco e Canadá', 'D': 'São Marino e Índia'},
          'correta': 'A'},

        {'titulo': 'Quantas casas decimais tem o número pi?',
          'nivel': 'facil',
          'opcoes': {'A': 'Milhares', 'B': 'Centenas', 'C': 'Duas', 'D': 'Infinitas'},
          'correta': 'D'},
          
        {'titulo': 'Quem pintou "Guernica"?',
          'nivel': 'facil',
          'opcoes': {'A': 'Paul Cézanne', 'B': 'Pablo Picasso', 'C': 'Salvador Dalí', 'D': 'Tarsila do Amaral'},
          'correta': 'B'},

        {'titulo': 'Em qual local da Ásia o português é língua oficial?',
          'nivel': 'facil',
          'opcoes': {'A': 'Portugal', 'B': 'Índia', 'C': 'Macau', 'D': 'Moçambique'},
          'correta': 'C'},
          
         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},

        {'titulo': 'Qual o nome do presidente do Brasil que ficou conhecido como Jango?',
          'nivel': 'medio',
          'opcoes': {'A': 'João Figueiredo', 'B': 'João Goulart', 'C': 'Getúlio Vargas', 'D': 'Jânio Quadro'},
          'correta': 'D'},

        {'titulo': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
          'nivel': 'medio',
          'opcoes': {'A': 'Asterístico, beneficiente, meteorologia, entertido', 'B': 'Asterisco, beneficente, meteorologia, entretido', 'C': 'Asterístico, beneficiente, metereologia, entretido', 'D': 'Asterisco, beneficiente, metereologia, entretido'},
          'correta': 'B'},
          
        {'titulo': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
          'nivel': 'medio',
          'opcoes': {'A': 'Asterístico, beneficiente, meteorologia, entertido', 'B': 'Asterisco, beneficente, meteorologia, entretido', 'C': 'Asterístico, beneficiente, metereologia, entretido', 'D': 'Asterisco, beneficiente, metereologia, entretido'},
          'correta': 'B'},
          
        {'titulo': 'Qual a montanha mais alta do Brasil?',
          'nivel': 'medio',
          'opcoes': {'A': 'Pico da Neblina', 'B': 'Pico Paraná', 'C': 'Monte Roraima', 'D': 'Pico Maior de Friburgo'},
          'correta': 'A'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'},

        {'titulo': 'Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Tem entre 2 a 4 litros. São retirados 450 mililitros', 'B': 'Tem entre 4 a 6 litros. São retirados 450 mililitros', 'C': 'Tem 10 litros. São retirados 2 litros', 'D': 'Tem 7 litros. São retirados 1,5 litros'},
          'correta': 'B'},

        {'titulo': 'Qual o livro mais vendido no mundo a seguir à Bíblia?',
          'nivel': 'dificil',
          'opcoes': {'A': 'O Senhor dos Anéis', 'B': 'O Pequeno Príncipe', 'C': 'Dom Quixote', 'D': ' Um Conto de Duas Cidades'},
          'correta': 'C'},
      
        {'titulo': 'Qual a altura da rede de vôlei nos jogos masculino e feminino?',
          'nivel': 'dificil',
          'opcoes': {'A': '2,4 para ambos', 'B': '1,8 m e 1,5 m', 'C': '2,43 m e 2,24 m', 'D': '2,45 m e 2,15 m'},
          'correta': 'C'},
            
        {'titulo': 'Em que período da pré-história o fogo foi descoberto?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Neolítico', 'B': 'Paleolítico', 'C': 'Idade dos Metais', 'D': 'Período da Pedra Polida'},
          'correta': 'B'}
        ])
#print(erros)
dados = funcoes.transforma_base([{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

        {'titulo': 'Quais o menor e o maior país do mundo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Vaticano e Rússia', 'B': 'Nauru e China', 'C': 'Mônaco e Canadá', 'D': 'São Marino e Índia'},
          'correta': 'A'},

        {'titulo': 'Quantas casas decimais tem o número pi?',
          'nivel': 'facil',
          'opcoes': {'A': 'Milhares', 'B': 'Centenas', 'C': 'Duas', 'D': 'Infinitas'},
          'correta': 'D'},
          
        {'titulo': 'Quem pintou "Guernica"?',
          'nivel': 'facil',
          'opcoes': {'A': 'Paul Cézanne', 'B': 'Pablo Picasso', 'C': 'Salvador Dalí', 'D': 'Tarsila do Amaral'},
          'correta': 'B'},

        {'titulo': 'Em qual local da Ásia o português é língua oficial?',
          'nivel': 'facil',
          'opcoes': {'A': 'Portugal', 'B': 'Índia', 'C': 'Macau', 'D': 'Moçambique'},
          'correta': 'C'},

        {'titulo': 'Quem é o autor de “O Príncipe”?',
          'nivel': 'medio',
          'opcoes': {'A': 'Maquiavel', 'B': 'Antoine de Saint-Exupéry', 'C': 'Montesquieu', 'D': 'Rousseau'},
          'correta': 'A'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},

        {'titulo': 'Qual o nome do presidente do Brasil que ficou conhecido como Jango?',
          'nivel': 'medio',
          'opcoes': {'A': 'João Figueiredo', 'B': 'João Goulart', 'C': 'Getúlio Vargas', 'D': 'Jânio Quadro'},
          'correta': 'D'},

        {'titulo': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
          'nivel': 'medio',
          'opcoes': {'A': 'Asterístico, beneficiente, meteorologia, entertido', 'B': 'Asterisco, beneficente, meteorologia, entretido', 'C': 'Asterístico, beneficiente, metereologia, entretido', 'D': 'Asterisco, beneficiente, metereologia, entretido'},
          'correta': 'B'},
          
        {'titulo': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
          'nivel': 'medio',
          "opcoes": {'A': 'Asterístico, beneficiente, meteorologia, entertido', 'B': 'Asterisco, beneficente, meteorologia, entretido', 'C': 'Asterístico, beneficiente, metereologia, entretido', 'D': 'Asterisco, beneficiente, metereologia, entretido'},
          'correta': 'B'},
          
        {'titulo': 'Qual a montanha mais alta do Brasil?',
          'nivel': 'medio',
          'opcoes': {'A': 'Pico da Neblina', 'B': 'Pico Paraná', 'C': 'Monte Roraima', 'D': 'Pico Maior de Friburgo'},
          'correta': 'A'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'},

        {'titulo': 'Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Tem entre 2 a 4 litros. São retirados 450 mililitros', 'B': 'Tem entre 4 a 6 litros. São retirados 450 mililitros', 'C': 'Tem 10 litros. São retirados 2 litros', 'D': 'Tem 7 litros. São retirados 1,5 litros'},
          'correta': 'B'},

        {'titulo': 'Qual o livro mais vendido no mundo a seguir à Bíblia?',
          'nivel': 'dificil',
          'opcoes': {'A': 'O Senhor dos Anéis', 'B': 'O Pequeno Príncipe', 'C': 'Dom Quixote', 'D': ' Um Conto de Duas Cidades'},
          'correta': 'C'},
      
        {'titulo': 'Qual a altura da rede de vôlei nos jogos masculino e feminino?',
          'nivel': 'dificil',
          'opcoes': {'A': '2,4 para ambos', 'B': '1,8 m e 1,5 m', 'C': '2,43 m e 2,24 m', 'D': '2,45 m e 2,15 m'},
          'correta': 'C'},
            
        {'titulo': 'Em que período da pré-história o fogo foi descoberto?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Neolítico', 'B': 'Paleolítico', 'C': 'Idade dos Metais', 'D': 'Período da Pedra Polida'},
          'correta': 'B'}
        ])
      